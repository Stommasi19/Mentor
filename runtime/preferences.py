"""Neutral project preferences and conversation control transitions.

Session state is supplied by the caller, never persisted. Hosts map their own
configuration to an explicit data root and carry the resolved project ID forward.
"""

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


LEVELS = ("junior", "mid-level", "senior")
LEGACY_LEVELS = {"guided": "junior", "supported": "mid-level", "independent": "senior"}
DEFAULTS = {"level": "junior", "coaching_enabled": True}


def canonical_level(value: str) -> str:
    """Translate only known legacy choices; never guess a learner's level."""
    if not isinstance(value, str):
        raise ValueError("invalid level")
    translated = LEGACY_LEVELS.get(value, value)
    if translated not in LEVELS:
        raise ValueError("invalid level")
    return translated


def resolve_project(workspace: str) -> str:
    """Hash the canonical Git common directory, or a non-Git workspace root."""
    root = Path(workspace).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("workspace must be a directory")
    lookup = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--path-format=absolute", "--git-common-dir"],
        capture_output=True, text=True, timeout=5,
        # Ambient Git overrides must not select a different repository.
        env={**{key: value for key, value in os.environ.items() if not key.startswith("GIT_")},
             "LC_ALL": "C"},
    )
    if lookup.returncode == 0:
        # Remove Git's line terminator, not whitespace belonging to the path.
        identity = Path(lookup.stdout.removesuffix("\n")).resolve(strict=True)
        if not identity.is_dir():
            raise ValueError("Git common directory is unavailable")
    elif "not a git repository" in lookup.stderr.lower():
        # A broken .git marker is a failed lookup, not a new non-Git identity.
        if any((parent / ".git").exists() or (parent / ".git").is_symlink()
               for parent in (root, *root.parents)):
            raise ValueError("Git project identity could not be resolved")
        identity = root
    else:
        raise ValueError(f"Git project lookup failed: {lookup.stderr.strip()}")
    return hashlib.sha256(os.fsencode(identity)).hexdigest()


def resolve_data_root(value: str) -> Path:
    path = Path(value)
    if not value or not path.is_absolute():
        raise ValueError("data root must be an absolute path")
    return path.resolve()


def validate_values(values: dict) -> None:
    if values.get("level") not in LEVELS or type(values.get("coaching_enabled")) is not bool:
        raise ValueError("expected exact level enum and coaching boolean")


@dataclass
class ProjectPreferences:
    """A read result keeps fallback defaults separate from verified saved values."""

    defaults: dict
    saved: dict | None
    state: str
    warning: str | None = None
    legacy_level: str | None = None


class PreferenceStore:
    def __init__(self, data_root: str | None, project_id: str | None,
                 unavailable_reason: str | None = None):
        self.path = None
        self.warning = unavailable_reason
        if unavailable_reason:
            return
        try:
            if not isinstance(project_id, str) or not re.fullmatch(r"[0-9a-f]{64}", project_id):
                raise ValueError("project identity is unavailable or invalid")
            root = resolve_data_root(data_root or "")
            self.path = root / "projects" / project_id / "preferences.json"
        except (OSError, ValueError, RuntimeError) as error:
            self.warning = str(error)

    def read(self) -> ProjectPreferences:
        if self.path is None:
            return ProjectPreferences(dict(DEFAULTS), None, "unavailable", self.warning)
        try:
            # Opening directly distinguishes absent records from permission errors.
            content = self.path.read_text(encoding="utf-8")
        except FileNotFoundError:
            if self.path.is_symlink():
                return ProjectPreferences(dict(DEFAULTS), None, "invalid", "record is a broken symlink")
            return ProjectPreferences(dict(DEFAULTS), None, "missing")
        except (OSError, UnicodeError) as error:
            return ProjectPreferences(dict(DEFAULTS), None, "unreadable", str(error))
        try:
            record = json.loads(content)
            if not isinstance(record, dict) or set(record) != {"schema_version", *DEFAULTS}:
                raise ValueError("invalid preference fields")
            version = record["schema_version"]
            if type(version) is not int or version not in (1, 2):
                raise ValueError("unsupported schema version")
            values = {field: record[field] for field in DEFAULTS}
            legacy = None
            if version == 1:
                if not isinstance(values["level"], str) or values["level"] not in LEGACY_LEVELS:
                    raise ValueError("invalid version-1 level")
                legacy = values["level"]
                values["level"] = LEGACY_LEVELS[legacy]
            validate_values(values)
            return ProjectPreferences(values, dict(values), "saved", legacy_level=legacy)
        except (ValueError, TypeError) as error:
            return ProjectPreferences(dict(DEFAULTS), None, "invalid", str(error))

    def write(self, values: dict) -> None:
        """Replace atomically; failures before replacement preserve the old record.

        Concurrent writers are last-completed-write wins, without a field merge.
        A readback mismatch is reported as unverified persistence.
        """
        validate_values(values)
        if self.path is None:
            raise ValueError(self.warning or "persistence unavailable")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                             dir=self.path.parent, delete=False) as stream:
                temporary = Path(stream.name)
                json.dump({"schema_version": 2, **values}, stream, indent=2)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, self.path)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        if self.read().saved != values:
            raise ValueError("write completed but persistence readback did not match; refresh status")


def validate_session(session: dict) -> dict:
    if not isinstance(session, dict) or set(session) - {"overrides", "unsaved"}:
        raise ValueError("session must contain overrides and optional unsaved fields")
    overrides = session.get("overrides", {})
    unsaved = session.get("unsaved", [])
    if not isinstance(overrides, dict) or set(overrides) - set(DEFAULTS):
        raise ValueError("invalid session override fields")
    overrides = dict(overrides)
    if "level" in overrides:
        overrides["level"] = canonical_level(overrides["level"])
    validate_values({**DEFAULTS, **overrides})
    if (not isinstance(unsaved, list) or any(field not in overrides for field in unsaved)
            or len(set(unsaved)) != len(unsaved)):
        raise ValueError("unsaved fields must name existing session overrides")
    return {"overrides": dict(overrides), "unsaved": list(unsaved)}


def control(store: PreferenceStore, action: str = "status", scope: str = "session",
            value: str | None = None, field: str = "all", session: dict | None = None) -> dict:
    """Apply one validated operation, returning the next conversation state."""
    current = validate_session(session if session is not None else {})
    if scope not in ("session", "project") or field not in ("all", *DEFAULTS):
        raise ValueError("invalid scope or field")
    if action not in ("status", "set-level", "pause", "resume", "use-project", "reset"):
        raise ValueError("invalid control action")
    if action == "set-level":
        value = canonical_level(value)
    if action != "set-level" and value is not None:
        raise ValueError("only set-level accepts a value")
    if action == "reset" and scope != "project":
        raise ValueError("reset requires explicit project scope")
    if action in ("status", "use-project") and scope != "session":
        raise ValueError("status and use-project are session operations")
    if action != "use-project" and field != "all":
        raise ValueError("field selection applies only to use-project")

    loaded = store.read()
    warnings = [loaded.warning] if loaded.warning else []
    changed = {}
    persisted = None
    if action == "set-level":
        changed = {"level": value}
    elif action in ("pause", "resume"):
        changed = {"coaching_enabled": action == "resume"}
    elif action == "reset":
        changed = dict(DEFAULTS)
    elif action == "use-project":
        selected = list(DEFAULTS) if field == "all" else [field]
        for selected_field in selected:
            current["overrides"].pop(selected_field, None)
            if selected_field in current["unsaved"]:
                current["unsaved"].remove(selected_field)

    if changed and scope == "project":
        try:
            if action != "reset" and loaded.state not in ("missing", "saved"):
                raise ValueError("cannot overwrite unavailable/invalid preferences; explicit project reset required")
            # Use saved defaults, never the other field's temporary session value.
            store.write({**loaded.defaults, **changed})
            persisted = True
            loaded = store.read()
            warnings = [loaded.warning] if loaded.warning else []
            for changed_field in changed:
                current["overrides"].pop(changed_field, None)
                if changed_field in current["unsaved"]:
                    current["unsaved"].remove(changed_field)
        except (OSError, ValueError) as error:
            persisted = False
            warnings.append(f"Project save not verified: {error}. Requested change applies as an unsaved session override.")
            current["overrides"].update(changed)
            for changed_field in changed:
                if changed_field not in current["unsaved"]:
                    current["unsaved"].append(changed_field)
    elif changed:
        current["overrides"].update(changed)
        current["unsaved"] = [item for item in current["unsaved"] if item not in changed]

    if current["unsaved"]:
        warnings.append("Unsaved project requests remain session overrides: " + ", ".join(current["unsaved"]))
    return {
        "action": action, "scope": scope, "requested": changed,
        "effective": {**loaded.defaults, **current["overrides"]},
        "project_defaults": loaded.defaults, "saved": loaded.saved,
        "record_state": loaded.state, "persisted": persisted,
        "legacy_saved_level": loaded.legacy_level,
        "legacy_session_level": (session or {}).get("overrides", {}).get("level")
        if (session or {}).get("overrides", {}).get("level") in LEGACY_LEVELS else None,
        "session": current, "warnings": warnings,
        "preference_path": str(store.path) if store.path else None,
    }
