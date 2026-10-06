"""Preference contracts through real control/hook processes and temporary files."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
DEFAULTS = {"level": "guided", "coaching_enabled": True}


class PreferenceContractTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="mentor-state-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.workspace = self.root / "workspace"
        self.workspace.mkdir()
        self.data = self.root / "data"
        self.project_id = hashlib.sha256(os.fsencode(self.workspace.resolve())).hexdigest()
        self.record = self.data / "projects" / self.project_id / "preferences.json"

    def invoke(self, action="status", value=None, scope="session", session=None,
               field="all", data=None, project_id=None, check=True):
        args = [sys.executable, str(REPOSITORY / "adapters/codex/control.py"),
                "--data-root", str(data or self.data), "--project-id", project_id or self.project_id,
                "--scope", scope, "--field", field, "--session", json.dumps(session or {}), action]
        if value is not None:
            args.append(value)
        result = subprocess.run(args, cwd=self.root, capture_output=True, text=True, check=check)
        return json.loads(result.stdout) if check else result

    def hook(self, workspace=None, data=None):
        result = subprocess.run([sys.executable, str(REPOSITORY / "adapters/codex/session_start.py")],
            input=json.dumps({"hook_event_name": "SessionStart", "source": "startup",
                              "cwd": str(workspace or self.workspace)}),
            env={**os.environ, "MENTOR_DATA_DIR": str(data or self.data)},
            cwd=self.root, capture_output=True, text=True, check=True)
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        status = json.loads(context.split("## Mentor project defaults (not session overrides)\n")[1].split("\n\n")[0])
        return context, status

    def test_session_controls_refresh_and_return_to_defaults_never_write(self):
        status = self.invoke()
        self.assertEqual(status["effective"], DEFAULTS)
        self.assertEqual(status["record_state"], "missing")
        session = self.invoke("set-level", "independent")["session"]
        paused = self.invoke("pause", session=session)
        self.assertEqual(paused["effective"], {"level": "independent", "coaching_enabled": False})
        resumed = self.invoke("resume", session=paused["session"])
        self.assertEqual(resumed["effective"], {"level": "independent", "coaching_enabled": True})
        self.assertFalse(self.data.exists())
        saved = self.invoke("set-level", "supported", "project")
        before = self.record.read_bytes()
        refreshed = self.invoke(session=paused["session"])
        self.assertEqual(refreshed["saved"], {"level": "supported", "coaching_enabled": True})
        self.assertEqual(refreshed["effective"], paused["effective"])
        returned = self.invoke("use-project", session=paused["session"], field="level")
        self.assertEqual(returned["effective"], {"level": "supported", "coaching_enabled": False})
        self.assertEqual(self.invoke("use-project", session=returned["session"])["session"]["overrides"], {})
        self.assertEqual(self.record.read_bytes(), before)
        self.assertTrue(saved["persisted"])

    def test_project_writes_preserve_other_saved_field_and_override_reset_is_local(self):
        self.invoke("set-level", "supported", "project")
        session = self.invoke("set-level", "independent")["session"]
        result = self.invoke("pause", scope="project", session=session)
        self.assertEqual(result["saved"], {"level": "supported", "coaching_enabled": False})
        self.assertEqual(result["session"]["overrides"], {"level": "independent"})
        self.assertEqual(self.invoke()["effective"], result["saved"])
        resumed_session = self.invoke("resume", session=result["session"])["session"]
        level_saved = self.invoke("set-level", "guided", "project", resumed_session)
        self.assertEqual(level_saved["saved"], {"level": "guided", "coaching_enabled": False})
        self.assertEqual(level_saved["session"]["overrides"], {"coaching_enabled": True})
        self.assertEqual(level_saved["effective"], {"level": "guided", "coaching_enabled": True})
        other_id = "b" * 64
        self.invoke("pause", scope="project", project_id=other_id)
        other_record = self.data / "projects" / other_id / "preferences.json"
        other_bytes = other_record.read_bytes()
        reset = self.invoke("reset", scope="project", session=session)
        self.assertEqual(reset["session"]["overrides"], {})
        self.assertEqual(reset["saved"], DEFAULTS)
        self.assertEqual(self.invoke(session=session)["effective"]["level"], "independent")
        self.assertEqual(other_record.read_bytes(), other_bytes)
        self.assertEqual(set(json.loads(self.record.read_text())), {"schema_version", "level", "coaching_enabled"})

    def test_invalid_records_survive_mutations_until_explicit_reset(self):
        self.record.parent.mkdir(parents=True)
        records = [b"not JSON", b"\xff", b"[]", b'{"schema_version":2,"level":"guided","coaching_enabled":true}',
                   b'{"schema_version":true,"level":"guided","coaching_enabled":true}',
                   b'{"schema_version":1,"level":"Guided","coaching_enabled":true}',
                   b'{"schema_version":1,"level":"guided","coaching_enabled":1}',
                   b'{"schema_version":1,"level":"guided","coaching_enabled":true,"extra":0}']
        for content in records:
            with self.subTest(content=content):
                self.record.write_bytes(content)
                failed = self.invoke("set-level", "independent", "project")
                self.assertFalse(failed["persisted"])
                self.assertEqual(failed["effective"]["level"], "independent")
                self.assertEqual(failed["session"]["unsaved"], ["level"])
                self.assertTrue(failed["warnings"])
                self.assertEqual(self.record.read_bytes(), content)
                context, status = self.hook()
                self.assertTrue(status["warnings"])
                self.assertEqual(status["effective"], DEFAULTS)
                self.assertTrue(context.startswith((REPOSITORY / "core/policy.md").read_text().strip()))
                self.assertTrue(self.invoke("reset", scope="project")["persisted"])
                self.assertEqual(self.invoke()["saved"], DEFAULTS)

    def test_real_permission_failures_preserve_record_and_apply_unsaved_requests(self):
        if os.geteuid() == 0:
            self.skipTest("real permission checks require a non-root OS user")
        self.invoke("set-level", "supported", "project")
        before = self.record.read_bytes()
        directory = self.record.parent
        directory.chmod(0o500)
        try:
            changed = self.invoke("pause", scope="project")
            self.assertFalse(changed["persisted"])
            self.assertEqual(changed["saved"]["coaching_enabled"], True)
            self.assertEqual(changed["effective"]["coaching_enabled"], False)
            failed_reset = self.invoke("reset", scope="project", session=changed["session"])
            self.assertFalse(failed_reset["persisted"])
            self.assertEqual(failed_reset["effective"], DEFAULTS)
            self.assertEqual(set(failed_reset["session"]["unsaved"]), set(DEFAULTS))
            self.assertEqual(self.record.read_bytes(), before)
            self.assertEqual(list(directory.iterdir()), [self.record])
        finally:
            directory.chmod(0o700)
        self.record.chmod(0)
        try:
            unreadable = self.invoke("pause", scope="project")
            self.assertEqual(unreadable["record_state"], "unreadable")
            self.assertFalse(unreadable["persisted"])
            self.assertTrue(self.invoke("reset", scope="project")["persisted"])
        finally:
            self.record.chmod(0o600)

    def test_invalid_commands_do_not_write_or_claim_success(self):
        for action, value, scope, session in [
            ("set-level", "expert", "project", {}), ("reset", None, "session", {}),
            ("pause", "false", "project", {}), ("status", None, "project", {}),
            ("pause", None, "project", {"overrides": {"coaching_enabled": 1}}),
            ("status", None, "session", {"unsaved": ["level"]}),
        ]:
            with self.subTest(action=action, value=value, scope=scope):
                result = self.invoke(action, value, scope, session, check=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertFalse(self.data.exists())
        bad_root = self.invoke("pause", scope="project", data="relative")
        self.assertFalse(bad_root["persisted"])
        self.assertIsNone(bad_root["preference_path"])
        blocker = self.root / "not-a-directory"
        blocker.write_text("keep")
        blocked = self.invoke("reset", scope="project", data=blocker)
        self.assertFalse(blocked["persisted"])
        self.assertEqual(blocker.read_text(), "keep")

    def test_identity_worktrees_symlinks_and_hook_tool_cwd_share_only_the_same_project(self):
        def git(*args):
            return subprocess.run(["git", *args], cwd=self.workspace, capture_output=True, text=True, check=True)
        git("init")
        git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "--allow-empty", "-m", "fixture")
        nested = self.workspace / "nested"
        nested.mkdir()
        worktree = self.root / "worktree"
        git("worktree", "add", "-b", "probe", str(worktree))
        alias = self.root / "alias"
        alias.symlink_to(self.workspace, target_is_directory=True)
        expected_id = hashlib.sha256(os.fsencode((self.workspace / ".git").resolve())).hexdigest()
        self.invoke("set-level", "supported", "project", project_id=expected_id)
        for path in (self.workspace, nested, worktree, alias):
            with self.subTest(path=path):
                context, status = self.hook(path)
                self.assertEqual(status["saved"]["level"], "supported")
                base = context.split("Base shell command: ")[1].split("\n")[0]
                result = subprocess.run(base + " status", shell=True, cwd=self.root,
                                        capture_output=True, text=True, check=True,
                                        env={key: val for key, val in os.environ.items() if key != "MENTOR_DATA_DIR"})
                self.assertEqual(json.loads(result.stdout)["saved"], status["saved"])
        clone = self.root / "clone"
        git("clone", str(self.workspace), str(clone))
        self.assertEqual(self.hook(clone)[1]["record_state"], "missing")
        separate_workspace = self.root / "separate-git-workspace"
        common_directory = self.root / "common directory "
        # Whitespace is part of a filesystem identity, including at its end.
        git("init", "--separate-git-dir", str(common_directory), str(separate_workspace))
        separate_id = hashlib.sha256(os.fsencode(common_directory.resolve())).hexdigest()
        separate_status = self.hook(separate_workspace)[1]
        self.assertEqual(separate_status["preference_path"],
                         str(self.data.resolve() / "projects" / separate_id / "preferences.json"))
        non_git = self.root / "non-git"
        non_git.mkdir()
        sub = non_git / "sub"
        sub.mkdir()
        self.assertNotEqual(self.hook(non_git)[1]["preference_path"], self.hook(sub)[1]["preference_path"])
        for workspace, data in ((self.root / "absent", self.data), (self.workspace, "relative")):
            context, status = self.hook(workspace, data)
            self.assertEqual(status["record_state"], "unavailable")
            self.assertIsNone(status["preference_path"])
            self.assertTrue(status["warnings"])
        broken = self.root / "broken-repo"
        broken.mkdir()
        (broken / ".git").write_text("gitdir: /missing/mentor-test-repo\n")
        self.assertEqual(self.hook(broken)[1]["record_state"], "unavailable")


if __name__ == "__main__":
    unittest.main()
