"""Read-only request preparation and project isolation at the adapter CLI boundary."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HANDLER = Path(__file__).resolve().parents[1] / 'adapters/codex/prism/context.py'


class PrismContextTests(unittest.TestCase):
    def invoke(self, workspace, *arguments, record=None, env=None):
        if arguments and arguments[0] == 'load':
            arguments = (*arguments, '--server-name', 'mentor-memory-connection')
        return subprocess.run([sys.executable, str(HANDLER), '--workspace', str(workspace), *arguments],
                              input=json.dumps(record) if record is not None else None,
                              capture_output=True, text=True, cwd=workspace.parent, env=env)

    def test_existing_aliased_disabled_and_plugin_connections_never_request_a_server(self):
        with tempfile.TemporaryDirectory(prefix='mentor-prism-registration-') as tmp:
            root = Path(tmp)
            config = root / 'config.toml'
            original = ('[mcp_servers.project_memory]\ncommand="npx"\n'
                        'args=["-y","prism-mcp-server@20.21.17"]\nenabled=false\n'
                        '[mcp_servers.project_memory.env]\nAPI_SECRET="not-for-output"\n'
                        '[mcp_servers.learning_memory]\ncommand="python3"\nargs=['
                        + json.dumps(str(HANDLER.with_name('launch.py')))
                        + ',"--volume","mentor-private-data"]\n')
            config.write_text(original)
            for options in (['--config', str(config)], []):
                result = self.invoke(root, 'inspect', *options, env={**os.environ, 'CODEX_HOME': str(root)})
                self.assertEqual(result.returncode, 0, result.stderr)
                inspected = json.loads(result.stdout)
                self.assertEqual(inspected['registered_names'], ['learning_memory', 'project_memory'])
                self.assertEqual(inspected['action'], 'inspect-and-reuse')
                self.assertFalse(inspected['registrations'][0]['enabled'])
                self.assertFalse(inspected['live_connection_verified'])
                self.assertFalse(inspected['server_started'])
                self.assertNotIn('not-for-output', result.stdout)
                self.assertEqual(config.read_text(), original)
            config.unlink()
            plugin = self.invoke(root, 'inspect', '--config', str(config), '--connected-server', 'plugin-memory')
            self.assertEqual(plugin.returncode, 0, plugin.stderr)
            self.assertEqual(json.loads(plugin.stdout)['action'], 'inspect-and-reuse')
            absent = self.invoke(root, 'inspect', '--config', str(config))
            self.assertEqual(absent.returncode, 0, absent.stderr)
            self.assertEqual(json.loads(absent.stdout)['action'], 'ordinary-tool-fallback')
            self.assertFalse(config.exists())
            config.write_text('broken = [')
            invalid = self.invoke(root, 'inspect', '--config', str(config))
            self.assertNotEqual(invalid.returncode, 0)
            self.assertEqual(invalid.stdout, '')
            self.assertEqual(config.read_text(), 'broken = [')

    def test_load_and_requested_save_keep_the_explicit_project_version_and_no_local_writes(self):
        with tempfile.TemporaryDirectory(prefix='mentor-prism-projects-') as tmp:
            root = Path(tmp)
            workspace = root / "Project's $workspace"
            workspace.mkdir()
            preferences = workspace / 'preferences.json'
            preferences.write_text('{"level":"junior","coaching_enabled":false}')
            loaded = self.invoke(workspace, 'load', '--project', 'owner-current-project', '--conversation-id', 'session-a')
            self.assertEqual(loaded.returncode, 0, loaded.stderr)
            prepared = json.loads(loaded.stdout)
            request = prepared['requests'][0]
            self.assertEqual(request['tool'], 'session_load_context')
            self.assertEqual(request['server'], 'mentor-memory-connection')
            self.assertEqual(request['arguments']['project'], 'owner-current-project')
            self.assertEqual(request['arguments']['conversation_id'], 'session-a')
            self.assertNotIn('level', request['arguments'])
            self.assertNotIn('prompt', request['arguments'])
            self.assertFalse(prepared['executed'])
            record = {'summary': 'Checked health endpoint.', 'todos': ['Check failures.'],
                      'decisions': ['Keep native connection.'], 'files_changed': ['api.py'],
                      'active_branch': 'feature/health', 'key_context': 'Local checks passed.'}
            for version in (7, None):
                session = {**prepared['session'], 'expected_version': version}
                saved = self.invoke(workspace, 'save', '--session', json.dumps(session), record=record)
                self.assertEqual(saved.returncode, 0, saved.stderr)
                result = json.loads(saved.stdout)
                ledger, handoff = result['requests']
                self.assertEqual(ledger['tool'], 'session_save_ledger')
                self.assertEqual(handoff['tool'], 'session_save_handoff')
                for call in (ledger, handoff):
                    self.assertEqual(call['server'], 'mentor-memory-connection')
                    self.assertEqual(call['arguments']['project'], 'owner-current-project')
                    self.assertEqual(call['arguments']['conversation_id'], 'session-a')
                self.assertEqual(handoff['arguments']['open_todos'], ['Check failures.'])
                self.assertTrue(handoff['arguments']['disable_merge'])
                self.assertEqual(handoff['arguments'].get('expected_version'), version)
                self.assertFalse(result['executed'])
            self.assertEqual(preferences.read_text(), '{"level":"junior","coaching_enabled":false}')
            self.assertEqual(list(workspace.iterdir()), [preferences])
            other = root / 'other-project'
            other.mkdir()
            rejected = self.invoke(other, 'save', '--session', json.dumps(session), record=record)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertEqual(rejected.stdout, '')
            self.assertEqual(list(other.iterdir()), [])

    def test_missing_load_version_invalid_records_and_learner_fields_produce_no_requests(self):
        with tempfile.TemporaryDirectory(prefix='mentor-prism-invalid-') as tmp:
            root = Path(tmp)
            loaded = self.invoke(root, 'load', '--project', 'owner-project', '--conversation-id', 'session-b')
            session = json.loads(loaded.stdout)['session']
            cases = [(session, {'summary': 'Work checked.'}),
                     ({key: value for key, value in {**session, 'expected_version': 1}.items()
                       if key != 'server_name'}, {'summary': 'Work checked.'}),
                     ({**session, 'expected_version': True}, {'summary': 'Work checked.'}),
                     ({**session, 'expected_version': -1}, {'summary': 'Work checked.'}),
                     ({**session, 'expected_version': 1}, {'summary': 'Work checked.', 'learner_grade': 'senior'}),
                     ({**session, 'expected_version': 1}, {'summary': 'Work checked.', 'transcript': []}),
                     ({**session, 'expected_version': 1}, {'summary': 'Work checked.', 'todos': 'not an array'}),
                     ({**session, 'expected_version': 1}, {'summary': ''})]
            for binding, record in cases:
                with self.subTest(binding=binding, record=record):
                    result = self.invoke(root, 'save', '--session', json.dumps(binding), record=record)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, '')
            self.assertEqual(list(root.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
