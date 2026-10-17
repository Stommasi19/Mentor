# Private Mentor installation

This installs the local checkout as a private Codex plugin. It submits nothing
to a public directory, creates no GitHub release and installs no MCP service.
The package keeps one canonical `core/`, `runtime/` and Codex adapter. The native
installer copies them into its plugin cache, so installed workflows do not depend
on this checkout's absolute location.

Tested: Codex CLI/app-server 0.160.1, Python 3.14, macOS arm64. Python 3.11+ and a
POSIX shell are prerequisites. Other hosts/platforms are unverified. The manifest
uses the Codex compatibility package format supported by the tested CLI.

## Install

From the Mentor checkout, using your existing Codex account/profile:

```sh
codex plugin marketplace add "$PWD"
codex plugin add mentor@mentor-private
codex plugin list --marketplace mentor-private --json
```

The local catalog is named `mentor-private`; it is available only where you add
that source. Keep the checkout for future updates. Codex maintains registration
and cache files through its native installer; do not copy files into its cache
or fabricate trust records. Remove any earlier Mentor development-hook entry and
manual Mentor skill links before enabling the installed plugin, preserving all
other hooks/skills. This prevents duplicate Mentor context/workflow registrations.

Restart Codex in a learner project. Open `/hooks`, review the Mentor command and
grant trust through the normal host flow, then start a fresh session. An installed
or enabled entry is not proof the hook executed. Check host hook results before
assuming Mentor is active. Use `/skills` to select one of the installed workflows:

- `$mentor:mentor-interview`
- `$mentor:mentor-review`
- `$mentor:mentor-feedback`
- `$mentor:mentor-pr-check`

The package's hook advertises these namespaced identifiers; development skill
registrations retain their original bare names. All four full workflows remain
explicit-only. Ordinary guidance does not require invoking a skill.

Say “save manual coding for this project” to keep ownership of all implementation
with guidance, progressive hints and review. “Use assisted coding” changes only
this conversation; request project scope explicitly to save it. A requested
demonstration is temporary and does not switch your saved mode. Manual mode
guides agent behavior; it does not revoke host filesystem permissions.

Prism and Serena are optional. Their requested setup/reuse remains in the
[MCP guide](../adapters/codex/MCP-SETUP.md); installing Mentor starts neither.
Prism defaults to separate Mentor storage and must not silently use Workflow's
shared connection. Keep local-document/ordinary-tool fallback when unavailable.

## Update, disable and remove

After bringing this checkout to the desired revision, reinstall from the same
registered local source:

```sh
codex plugin add mentor@mentor-private
```

The native installer refreshes the cached package. Version changes select the new
version; the lifecycle check exercised 0.1.0 to 0.1.1 in a disposable source.
Restart sessions and review any changed hook through the normal trust flow.
If you move the source checkout, remove/re-add the marketplace using its new
absolute location before reinstalling. Do not edit a running cache in place.

Disable Mentor using host plugin settings, or set this entry in the relevant
Codex config and restart. Preserve unrelated configuration:

```toml
[plugins."mentor@mentor-private"]
enabled = false
```

Set it back to `true` to re-enable, retaining required hook trust. The tested CLI's
plugin listing reflected saved config changes; a transient CLI `-c` override did
not change that listing, so do not use it as proof of disabled runtime delivery.

To uninstall the package and optionally remove its catalog registration:

```sh
codex plugin remove mentor@mentor-private
codex plugin marketplace remove mentor-private
```

Mentor preferences, interview plans and reports stay in `MENTOR_DATA_DIR` or
`~/.mentor`, outside the plugin cache. Uninstall leaves them intact; delete those
records separately only if intended. Requested MCP registrations, Docker volumes
and other host plugins are separate and are not removed with Mentor.

## Verification limits

Real native install/list/update/disable/remove, cached workflow execution and
app-server plugin/skill/hook discovery were checked in a disposable host home.
The discovered hook was untrusted as expected. A normal TUI trust check could
not reach `/hooks` because host account-routing discovery failed before startup;
automatic trusted hook delivery and a live manual-mode conversation remain
pending for this revision. No trust hash or bypass flag was supplied. See
[private package evidence](evidence/private-plugin.md).

Format reference: [official OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins).
Public distribution remains deferred and requires a separate request.
