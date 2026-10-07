"""Real process-boundary checks; these do not prove native host hook delivery."""

import hashlib
import json
import os
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
        shutil.copytree(REPOSITORY / "core" / "workflows", self.policy.parent / "workflows")
        shutil.copytree(REPOSITORY / "runtime", self.checkout / "runtime")
        self.data_root = root / "local data"

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
            env={**os.environ, "MENTOR_DATA_DIR": str(self.data_root)},
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
                context = output["additionalContext"]
                self.assertTrue(context.startswith(resource + "\n\n"))
                # Execute the actual delivered guidance from a different cwd,
                # without the hook environment. This owns quoting/location risk.
                base = context.split("Base shell command: ", 1)[1].split("\n", 1)[0]
                status = subprocess.run(base + " --session '{}' status", shell=True,
                                        cwd=self.checkout, capture_output=True, text=True, check=True)
                result_status = json.loads(status.stdout)
                self.assertEqual(result_status["effective"], {"level": "guided", "coaching_enabled": True})
                self.assertEqual(result_status["preference_path"], str(self.data_root.resolve() / "projects" /
                    hashlib.sha256(os.fsencode(self.workspace.resolve())).hexdigest() /
                    "preferences.json"))
                self.assertFalse(self.data_root.exists())
                self.assertEqual(result.stderr, "")

    def test_unavailable_or_invalid_core_fails_visibly_without_context(self):
        event = json.dumps({"hook_event_name": "SessionStart", "source": "startup"})
        workflow = self.policy.parent / "workflows" / "controls.md"
        interview = self.policy.parent / "workflows" / "interview.md"
        for resource in (self.policy, workflow, interview):
            original = resource.read_bytes()
            for content in (None, b"  \n", b"\xff"):
                with self.subTest(resource=resource.name, content=content):
                    resource.unlink(missing_ok=True)
                    if content is not None:
                        resource.write_bytes(content)
                    result = self.invoke(event)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, "")
                    self.assertIn("Mentor", result.stderr)
            resource.write_bytes(original)

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
