"""Missing-server setup through the actual Codex configuration writer."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]
SETUP = REPOSITORY / 'adapters/codex/setup_mcp.py'


class McpSetupTests(unittest.TestCase):
    def invoke(self, workspace, home, *arguments):
        return subprocess.run([sys.executable, str(SETUP), '--workspace', str(workspace),
            '--codex-home', str(home), '--prism-memory', 'shared', *arguments], capture_output=True, text=True)

    def installed_serena_fixture(self, root):
        runner = root / 'fixture-serena'
        runner.write_text('#!' + sys.executable + '\nimport sys\n'
            'if "--version" in sys.argv: print("Serena installed CLI fixture")\n'
            'elif "--help" in sys.argv: print("--context --mode --project --agent-interface")\n'
            'else: raise SystemExit("Fixture never launches MCP")\n')
        runner.chmod(0o755)
        return runner

    @unittest.skipUnless(shutil.which('codex') and shutil.which('npx'), 'requires the actual Codex writer and Node/npm')
    def test_apply_registers_missing_connections_preserves_settings_and_is_idempotent(self):
        with tempfile.TemporaryDirectory(prefix='mentor-mcp-setup-') as tmp:
            root = Path(tmp)
            home = root / 'codex-home'
            home.mkdir()
            config = home / 'config.toml'
            config.write_text('model="gpt-6.1-sol"\n[mcp_servers.unrelated]\ncommand="keep-me"\n'
                              '[mcp_servers.unrelated.env]\nKEEP="unchanged"\n')
            before = tomllib.loads(config.read_text())
            preview = self.invoke(root, home)
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertEqual([c['action'] for c in json.loads(preview.stdout)['connections']],
                             ['setup-required', 'setup-required'])
            self.assertEqual(tomllib.loads(config.read_text()), before)
            runner = self.installed_serena_fixture(root)
            applied = self.invoke(root, home, '--apply', '--serena-executable', str(runner))
            self.assertEqual(applied.returncode, 0, applied.stderr)
            report = json.loads(applied.stdout)
            self.assertEqual([c['action'] for c in report['connections']], ['registered', 'registered'])
            self.assertFalse(report['server_started_by_setup'])
            written = tomllib.loads(config.read_text())
            self.assertEqual(written['model'], before['model'])
            self.assertEqual(written['mcp_servers']['unrelated'], before['mcp_servers']['unrelated'])
            prism = written['mcp_servers']['mentor_prism']
            self.assertEqual(prism['env']['PRISM_STORAGE'], 'local')
            self.assertEqual(prism['args'], ['-y', 'prism-mcp-server@20.21.17'])
            serena = written['mcp_servers']['mentor_serena']
            self.assertEqual(serena['args'][1:3], ['--workspace', str(root.resolve())])
            self.assertIn(str(runner), serena['args'])
            original = config.read_bytes()
            repeated = self.invoke(root, home, '--apply', '--serena-executable', str(root/'unavailable'))
            self.assertEqual(repeated.returncode, 0, repeated.stderr)
            self.assertEqual([c['action'] for c in json.loads(repeated.stdout)['connections']],
                             ['inspect-and-reuse', 'inspect-and-reuse'])
            self.assertEqual(config.read_bytes(), original)
            self.assertFalse((home/'mentor-tools').exists())

    def test_existing_aliases_disabled_and_plugin_connections_are_reused_without_provisioning(self):
        with tempfile.TemporaryDirectory(prefix='mentor-mcp-reuse-') as tmp:
            root = Path(tmp)
            home = root / 'codex-home'
            home.mkdir()
            config = home / 'config.toml'
            original = ('[mcp_servers.memory]\ncommand="npx"\nargs=["prism-mcp-server"]\nenabled=false\n'
                        '[mcp_servers.symbols]\ncommand="serena"\nenabled=false\n')
            config.write_text(original)
            result = self.invoke(root, home, '--apply', '--serena-executable', str(root/'missing'))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual([c['registered_names'] for c in json.loads(result.stdout)['connections']],
                             [['memory'], ['symbols']])
            self.assertEqual(config.read_text(), original)
            config.unlink()
            plugin = self.invoke(root, home, '--apply', '--connected-prism', 'plugin-memory',
                                 '--connected-serena', 'plugin-navigation')
            self.assertEqual(plugin.returncode, 0, plugin.stderr)
            self.assertFalse(config.exists())
            self.assertEqual(list(home.iterdir()), [])
            config.write_text('invalid = [')
            invalid = self.invoke(root, home, '--apply')
            self.assertNotEqual(invalid.returncode, 0)
            self.assertEqual(invalid.stdout, '')
            self.assertEqual(config.read_text(), 'invalid = [')

    def test_separate_memory_reuses_only_a_dedicated_connection_and_never_falls_back_to_shared(self):
        with tempfile.TemporaryDirectory(prefix='mentor-mcp-isolation-') as tmp:
            root = Path(tmp)
            home = root / 'codex-home'
            home.mkdir()
            config = home / 'config.toml'
            shared = '[mcp_servers.prism_mcp]\ncommand="npx"\nargs=["prism-mcp-server"]\n'
            dedicated = ('[mcp_servers.mentor_memory]\ncommand="python3"\nargs=['
                + json.dumps(str(REPOSITORY/'adapters/codex/prism/launch.py'))
                + ',"--volume","mentor-private-data"]\n')
            config.write_text(shared + dedicated)
            result = self.invoke(root, home, '--apply', '--server', 'prism', '--prism-memory', 'separate')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['connections'][0]['registered_names'], ['mentor_memory'])
            self.assertEqual(config.read_text(), shared + dedicated)
            config.write_text(shared)
            preview = self.invoke(root, home, '--server', 'prism', '--prism-memory', 'separate')
            self.assertEqual(json.loads(preview.stdout)['connections'][0]['action'], 'setup-required')
            # An executable Codex is discoverable, while Docker is absent from
            # this process PATH. The actual guard must fail before any host write.
            codex = root/'codex'
            if shutil.which('codex'):
                codex.symlink_to(shutil.which('codex'))
                unavailable = subprocess.run([sys.executable, str(SETUP), '--workspace', str(root),
                    '--codex-home', str(home), '--server', 'prism', '--apply'],
                    env={**os.environ, 'PATH': str(root)}, capture_output=True, text=True)
                self.assertNotEqual(unavailable.returncode, 0)
                self.assertIn('Docker is required', json.loads(unavailable.stdout)['connections'][0]['error'])
                self.assertEqual(config.read_text(), shared)
            invalid = subprocess.run([sys.executable, str(REPOSITORY/'adapters/codex/prism/launch.py'),
                '--volume', '../shared-memory'], capture_output=True, text=True)
            self.assertNotEqual(invalid.returncode, 0)

    @unittest.skipUnless(shutil.which('codex') and shutil.which('npx'), 'requires the actual Codex writer and Node/npm')
    def test_partial_setup_failure_reports_the_completed_connection_without_overwrite(self):
        with tempfile.TemporaryDirectory(prefix='mentor-mcp-partial-') as tmp:
            root = Path(tmp)
            home = root / 'codex-home'
            result = self.invoke(root, home, '--apply', '--serena-executable', str(root/'missing'))
            self.assertNotEqual(result.returncode, 0)
            connections = json.loads(result.stdout)['connections']
            self.assertEqual(connections[0]['action'], 'registered')
            self.assertEqual(connections[1]['action'], 'setup-failed')
            config = home / 'config.toml'
            written = tomllib.loads(config.read_text())
            self.assertIn('mentor_prism', written['mcp_servers'])
            self.assertNotIn('mentor_serena', written['mcp_servers'])
            original = config.read_bytes()
            retry = self.invoke(root, home, '--apply', '--server', 'prism')
            self.assertEqual(retry.returncode, 0, retry.stderr)
            self.assertEqual(config.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
