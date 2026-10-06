"""Real process-boundary checks; these do not prove native host hook delivery."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]


class CodexAdapterContractTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="mentor-adapter-")
        self.addCleanup(self.temporary.cleanup)
        root = Path(self.temporary.name)
        self.checkout = root / "Mentor's $development checkout"
        self.workspace = root / "unrelated learner workspace"
        self.workspace.mkdir()
        self.adapter = self.checkout / "adapters" / "codex"
        shutil.copytree(REPOSITORY / "adapters" / "codex", self.adapter)
        self.policy = self.checkout / "core" / "policy.md"
        self.policy.parent.mkdir()
        shutil.copy(REPOSITORY / "core" / "policy.md", self.policy)

    def configured_command(self):
        result = subprocess.run(
            [sys.executable, str(self.adapter / "development_config.py")],
            cwd=self.workspace, capture_output=True, text=True, check=True,
        )
        config = json.loads(result.stdout)
        return config["hooks"]["SessionStart"][0]["hooks"][0]["command"]

    def invoke(self, payload, command=None):
        return subprocess.run(
            command or [sys.executable, str(self.adapter / "session_start.py")],
            shell=command is not None,
            cwd=self.workspace, input=payload, capture_output=True, text=True,
            timeout=10,
        )

    def test_configured_entry_reads_current_core_from_an_unrelated_directory(self):
        command = self.configured_command()
        for source in ("startup", "resume", "clear", "compact"):
            with self.subTest(source=source):
                # Changing the resource after generating config detects adapters
                # that embed a stale copy or load a workspace-relative file.
                resource = f"Development policy revision for {source}: café."
                self.policy.write_text(resource, encoding="utf-8")
                result = self.invoke(json.dumps({
                    "hook_event_name": "SessionStart", "source": source,
                    "cwd": str(self.workspace), "session_id": "contract-test",
                }), command)
                self.assertEqual(result.returncode, 0, result.stderr)
                output = json.loads(result.stdout)["hookSpecificOutput"]
                self.assertEqual(output["hookEventName"], "SessionStart")
                self.assertEqual(output["additionalContext"], resource)
                self.assertEqual(result.stderr, "")

    def test_unavailable_or_invalid_core_fails_visibly_without_context(self):
        event = json.dumps({"hook_event_name": "SessionStart", "source": "startup"})
        for content in (None, b"  \n", b"\xff"):
            with self.subTest(content=content):
                self.policy.unlink(missing_ok=True)
                if content is not None:
                    self.policy.write_bytes(content)
                result = self.invoke(event)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("Mentor", result.stderr)

    def test_invalid_event_is_rejected_at_the_process_boundary(self):
        events = [
            "not JSON", "[]", "{}",
            json.dumps({"hook_event_name": "Stop", "source": "startup"}),
            json.dumps({"hook_event_name": "SessionStart", "source": "unknown"}),
            json.dumps({"hook_event_name": "SessionStart", "source": []}),
        ]
        for event in events:
            with self.subTest(event=event):
                result = self.invoke(event)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("Mentor", result.stderr)


if __name__ == "__main__":
    unittest.main()
