"""Optional setup's nonmutation and absent-server fallback at the real CLI boundary."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest

DIRECTORY = Path(__file__).resolve().parents[1] / 'adapters/codex/serena'


class SerenaSetupTests(unittest.TestCase):
    def test_launcher_preserves_mcp_input_during_runner_preflight(self):
        with tempfile.TemporaryDirectory(prefix='mentor-serena-stdio-') as tmp:
            root = Path(tmp)
            runner = root / 'runner.py'
            # Interactive runners such as Docker read their inherited stdin,
            # even when the wrapped command only prints version/help text.
            runner.write_text('''import sys
if "--version" in sys.argv:
    sys.stdin.read()
    print("Serena test runner")
elif "--help" in sys.argv:
    sys.stdin.read()
    print("--context --mode --project --agent-interface")
else:
    sys.stdout.write(sys.stdin.read())
''')
            request = '{"jsonrpc":"2.0","id":1,"method":"initialize"}\n'
            result = subprocess.run([sys.executable, str(DIRECTORY/'launch.py'),
                '--workspace', str(root), '--executable', sys.executable,
                '--prefix-arg=' + str(runner)], input=request, capture_output=True,
                text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, request)

    def test_existing_registration_is_preserved_and_missing_server_falls_back(self):
        with tempfile.TemporaryDirectory(prefix='mentor-serena-') as tmp:
            root = Path(tmp)
            configuration = root / 'config.toml'
            original = '[mcp_servers.serena]\ncommand="existing-launcher"\n'
            configuration.write_text(original)
            command = [sys.executable, str(DIRECTORY/'setup.py'), '--workspace', str(root), '--config', str(configuration)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['action'], 'inspect-and-reuse')
            self.assertEqual(configuration.read_text(), original)
            alias = '[mcp_servers.symbols]\ncommand="serena"\nargs=["start-mcp-server"]\nenabled=false\n'
            configuration.write_text(alias)
            aliased = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(aliased.returncode, 0, aliased.stderr)
            self.assertEqual(json.loads(aliased.stdout)['registered_names'], ['symbols'])
            self.assertEqual(configuration.read_text(), alias)
            configuration.unlink()
            connected = subprocess.run(command + ['--connected-server', 'plugin-symbols'], capture_output=True, text=True)
            self.assertEqual(connected.returncode, 0, connected.stderr)
            self.assertEqual(json.loads(connected.stdout)['action'], 'inspect-and-reuse')
            self.assertFalse(configuration.exists())
            new = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(new.returncode, 0, new.stderr)
            server = tomllib.loads(new.stdout)['mcp_servers']['mentor_serena']
            self.assertEqual(server['args'][1:3], ['--workspace', str(root.resolve())])
            self.assertFalse(configuration.exists())
            fallback = subprocess.run([sys.executable, str(DIRECTORY/'launch.py'), '--workspace', str(root),
                '--executable', str(root/'absent-serena'), '--check'], capture_output=True, text=True)
            self.assertEqual(fallback.returncode, 2)
            self.assertFalse(json.loads(fallback.stdout)['available'])
            self.assertFalse(json.loads(fallback.stdout)['semantic_delivery_verified'])
            self.assertIn('ordinary checks', fallback.stderr)


if __name__ == '__main__':
    unittest.main()
