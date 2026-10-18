"""Private package lifecycle through the real Codex installer and cached helpers."""

import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('codex'), 'requires the actual Codex plugin installer')
class PrivatePluginTests(unittest.TestCase):
    def test_native_install_cached_controls_update_disable_and_remove_preserve_user_state(self):
        with tempfile.TemporaryDirectory(prefix='mentor-private-plugin-') as temporary:
            root = Path(temporary).resolve()
            source = root / "Mentor's $private source"
            # Only repository-owned package resources enter this fixture.
            for directory in ('core', 'runtime', 'adapters', '.codex-plugin'):
                shutil.copytree(REPOSITORY / directory, source / directory)
            catalog = source / '.agents/plugins'
            catalog.mkdir(parents=True)
            shutil.copy2(REPOSITORY / '.agents/plugins/marketplace.json', catalog / 'marketplace.json')
            home = root / 'codex-home'
            home.mkdir()
            config = home / 'config.toml'
            config.write_text('model="keep-this-model"\n[mcp_servers.unrelated]\ncommand="keep-this-server"\n')
            environment = {**os.environ, 'CODEX_HOME': str(home), 'MENTOR_DATA_DIR': str(root / 'data')}
            workspace = root / 'learner workspace'
            workspace.mkdir()

            def command(arguments, **kwargs):
                result = subprocess.run(arguments, env=environment, cwd=workspace,
                                        capture_output=True, text=True, timeout=30, **kwargs)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            def codex(*arguments):
                return command(['codex', *arguments, '--json'])

            codex('plugin', 'marketplace', 'add', str(source))
            installed = codex('plugin', 'add', 'mentor@mentor-private')
            cached = Path(installed['installedPath'])
            self.assertTrue(cached.is_relative_to(home))
            self.assertEqual(codex('plugin', 'list', '--marketplace', 'mentor-private')['installed'][0]['enabled'], True)
            manifest = json.loads((cached / '.codex-plugin/plugin.json').read_text())
            hooks = json.loads((cached / manifest['hooks']).read_text())
            hook = hooks['hooks']['SessionStart'][0]['hooks'][0]['command']
            environment['PLUGIN_ROOT'] = str(cached)
            event = json.dumps({'hook_event_name': 'SessionStart', 'source': 'startup', 'cwd': str(workspace)})
            context = command(hook, shell=True, input=event)['hookSpecificOutput']['additionalContext']
            for name in ('mentor-interview', 'mentor-review', 'mentor-feedback', 'mentor-pr-check'):
                self.assertIn('$mentor:' + name, context)
            control = shlex.split(context.split('Base shell command: ', 1)[1].split('\n', 1)[0])
            manual = command([*control, '--scope', 'project', 'set-coding-mode', 'manual'])
            self.assertTrue(manual['persisted'])
            record = Path(manual['preference_path'])
            before = record.read_bytes()

            # The installed snapshot must work when the authoring checkout is gone.
            unavailable_source = source.with_name('temporarily unavailable source')
            source.rename(unavailable_source)
            try:
                for name in ('mentor-interview', 'mentor-review', 'mentor-feedback', 'mentor-pr-check'):
                    entry = cached / 'adapters/codex/skills' / name / 'scripts/context.py'
                    loaded = command([sys.executable, str(entry), '--workspace', str(workspace)])
                    self.assertEqual(loaded['status']['effective']['coding_mode'], 'manual')
                    self.assertTrue(Path(loaded['workflow_path']).is_relative_to(cached))
                self.assertEqual(command(control + ['status'])['effective']['coding_mode'], 'manual')
            finally:
                unavailable_source.rename(source)

            # Disable in actual host config, then ask the native registry to reload it.
            settings = config.read_text()
            config.write_text(settings.replace('enabled = true', 'enabled = false'))
            self.assertFalse(codex('plugin', 'list', '--marketplace', 'mentor-private')['installed'][0]['enabled'])
            config.write_text(settings)

            source_manifest = source / '.codex-plugin/plugin.json'
            updated = json.loads(source_manifest.read_text())
            updated['version'] = '0.1.1'
            source_manifest.write_text(json.dumps(updated))
            policy = source / 'core/policy.md'
            policy.write_text(policy.read_text() + '\nPrivate update fixture.\n')
            refreshed = codex('plugin', 'add', 'mentor@mentor-private')
            self.assertEqual(refreshed['version'], '0.1.1')
            new_cache = Path(refreshed['installedPath'])
            environment['PLUGIN_ROOT'] = str(new_cache)
            refreshed_context = command(hook, shell=True, input=event)['hookSpecificOutput']['additionalContext']
            self.assertIn('Private update fixture.', refreshed_context)
            self.assertIn('"coding_mode": "manual"', refreshed_context)
            self.assertEqual(record.read_bytes(), before)

            codex('plugin', 'remove', 'mentor@mentor-private')
            self.assertEqual(codex('plugin', 'list', '--marketplace', 'mentor-private')['installed'], [])
            self.assertFalse(new_cache.exists())
            self.assertEqual(record.read_bytes(), before)
            remaining = tomllib.loads(config.read_text())
            self.assertEqual(remaining['model'], 'keep-this-model')
            self.assertEqual(remaining['mcp_servers']['unrelated']['command'], 'keep-this-server')


if __name__ == '__main__':
    unittest.main()
