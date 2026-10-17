#!/usr/bin/env python3
"""Reuse existing MCP connections or set up missing ones in the selected Codex home."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tomllib
import venv

PRISM_PACKAGE = 'prism-mcp-server@20.21.17'
SERENA_SOURCE = 'git+https://github.com/oraios/serena@3b99f8b024dafd58c962ea6e74f37c8a730ef532'
UV_PACKAGE = 'uv==0.12.23'
ADAPTER = Path(__file__).resolve().parent


def existing_connections(home, server, connected, prism_memory='separate'):
    """Include aliases and host/plugin inventory supplied by the primary agent."""
    config = home / 'config.toml'
    settings = tomllib.loads(config.read_text()) if config.exists() else {}
    entries = settings.get('mcp_servers', {})
    if not isinstance(entries, dict) or any(not isinstance(entry, dict) for entry in entries.values()):
        raise ValueError('MCP registrations must be tables')
    names = set(connected)
    for name, entry in entries.items():
        launcher = str(entry.get('command', '')) + ' ' + str(entry.get('args', []))
        matching = server in name.lower() or server in launcher.lower()
        if server == 'prism' and prism_memory == 'separate':
            # A shared Workflow server is not compatible with requested storage
            # isolation. Reuse an existing Mentor launcher, or a dedicated
            # connection explicitly identified in the actual host inventory.
            matching = matching and '/prism/launch.py' in launcher and '--volume' in entry.get('args', [])
        if matching:
            names.add(name)
    return sorted(names)


def run(command, *, environment, workspace, timeout=180):
    """Keep installation/host diagnostics off the result JSON stream."""
    return subprocess.run(command, env=environment, cwd=workspace, stdin=subprocess.DEVNULL,
                          stdout=sys.stderr, stderr=sys.stderr, check=True, timeout=timeout)


def serena_command(home, workspace, requested_executable, environment):
    executable = shutil.which(requested_executable or 'serena')
    prefix = []
    if requested_executable and not executable:
        raise ValueError(f'requested Serena executable is unavailable: {requested_executable}')
    if not executable:
        executable = shutil.which('uvx')
        if not executable:
            # Bootstrap a runner in this host's local tools directory, without
            # changing system Python, global packages or another host's setup.
            runner_home = home / 'mentor-tools' / 'uv'
            executable_path = runner_home / 'bin' / 'uvx'
            if not executable_path.is_file():
                venv.EnvBuilder(with_pip=True).create(runner_home)
                run([str(runner_home / 'bin' / 'python'), '-m', 'pip', 'install', UV_PACKAGE],
                    environment=environment, workspace=workspace)
            executable = str(executable_path)
        prefix = ['--from', SERENA_SOURCE, 'serena']
        # The first command installs/caches the pinned server before the launcher's
        # short compatibility probes. It does not start an MCP session.
        run([executable, *prefix, '--version'], environment=environment, workspace=workspace)
    command = [sys.executable, str(ADAPTER / 'serena' / 'launch.py'),
               '--workspace', str(workspace), '--executable', executable]
    command += ['--prefix-arg=' + value for value in prefix]
    run([*command, '--check'], environment=environment, workspace=workspace, timeout=30)
    return command


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    parser.add_argument('--codex-home', default=os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    parser.add_argument('--server', choices=('both', 'prism', 'serena'), default='both')
    parser.add_argument('--connected-prism', action='append', default=[])
    parser.add_argument('--connected-serena', action='append', default=[])
    parser.add_argument('--serena-executable', help='Use this installed runner instead of provisioning Serena')
    parser.add_argument('--prism-memory', choices=('separate', 'shared'), default='separate')
    parser.add_argument('--prism-volume', default='mentor-prism-data')
    parser.add_argument('--apply', action='store_true', help='Install missing dependencies and register missing connections')
    args = parser.parse_args()
    results = []
    failed = False
    try:
        workspace = Path(args.workspace)
        home = Path(args.codex_home)
        if not workspace.is_absolute() or not workspace.is_dir() or not home.is_absolute():
            raise ValueError('workspace must exist and workspace/codex-home must be absolute')
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', args.prism_volume):
            raise ValueError('prism-volume must be a Docker volume name, not a filesystem path')
        workspace = workspace.resolve()
        selected = ('prism', 'serena') if args.server == 'both' else (args.server,)
        environment = {**os.environ, 'CODEX_HOME': str(home)}
        for server in selected:
            connected = getattr(args, 'connected_' + server)
            names = existing_connections(home, server, connected, args.prism_memory)
            if names:
                results.append({'server': server, 'action': 'inspect-and-reuse', 'registered_names': names,
                                'registration_written': False, 'live_connection_verified': False})
                continue
            if not args.apply:
                results.append({'server': server, 'action': 'setup-required', 'registration_written': False})
                continue
            try:
                codex = shutil.which('codex')
                if not codex:
                    raise ValueError('Codex CLI is unavailable; install Codex before host setup')
                server_environment = []
                if server == 'prism':
                    if args.prism_memory == 'separate':
                        docker = shutil.which('docker')
                        if not docker:
                            raise ValueError('Docker is required for separate Mentor memory; shared Workflow memory is not a fallback')
                        run([docker, 'info', '--format', '{{.ServerVersion}}'],
                            environment=environment, workspace=workspace, timeout=15)
                        image = 'mentor-prism:20.21.17'
                        image_exists = subprocess.run([docker, 'image', 'inspect', image],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False).returncode == 0
                        if not image_exists:
                            run([docker, 'build', '--tag', image, str(ADAPTER / 'prism')],
                                environment=environment, workspace=workspace, timeout=300)
                        command = [sys.executable, str(ADAPTER / 'prism' / 'launch.py'),
                                   '--volume', args.prism_volume, '--image', image]
                    else:
                        npx = shutil.which('npx')
                        if not npx or not shutil.which('node'):
                            raise ValueError('Node.js/npm is unavailable; install it to provision Prism')
                        command = [npx, '-y', PRISM_PACKAGE]
                        server_environment = ['--env', 'PRISM_STORAGE=local']
                else:
                    cache = str(home / 'mentor-tools' / 'uv-cache')
                    environment['UV_CACHE_DIR'] = cache
                    command = serena_command(home, workspace, args.serena_executable, environment)
                    server_environment = ['--env', 'UV_CACHE_DIR=' + cache]
                # Installation can take time. Re-read before adding so a connection
                # set up in the meantime is reused, rather than overwritten.
                names = existing_connections(home, server, connected, args.prism_memory)
                if names:
                    results.append({'server': server, 'action': 'inspect-and-reuse', 'registered_names': names,
                                    'registration_written': False, 'live_connection_verified': False})
                    continue
                name = 'mentor_' + server
                config = home / 'config.toml'
                entries = tomllib.loads(config.read_text()).get('mcp_servers', {}) if config.exists() else {}
                # A prior shared Mentor registration must remain untouched too.
                # The isolated purpose gets its own name instead of an overwrite.
                if name in entries:
                    name += '_isolated'
                if name in entries:
                    raise ValueError(f'{name} already exists but is incompatible; inspect it instead of overwriting')
                # Codex's writer requires its home to exist even on first setup.
                # Create it only on the requested missing-connection write path.
                home.mkdir(parents=True, exist_ok=True)
                run([codex, 'mcp', 'add', name, *server_environment, '--', *command],
                    environment=environment, workspace=workspace, timeout=30)
                written = tomllib.loads((home / 'config.toml').read_text())['mcp_servers'].get(name)
                if not written or written.get('command') != command[0] or written.get('args') != command[1:]:
                    raise ValueError('host registration readback did not match the requested launch command')
                results.append({'server': server, 'action': 'registered', 'registered_names': [name],
                                'registration_written': True, 'live_connection_verified': False,
                                'next': 'Restart/reload the host, inspect exposed tools and verify the selected project.'})
            except (OSError, ValueError, subprocess.SubprocessError) as error:
                failed = True
                results.append({'server': server, 'action': 'setup-failed', 'error': str(error),
                                'next': 'Continue with ordinary tools; fix the reported dependency and retry.'})
    except (OSError, UnicodeError, ValueError, TypeError) as error:
        print(f'MCP setup unavailable: {error}; continue Mentor with ordinary tools.', file=sys.stderr)
        return 1
    json.dump({'connections': results, 'server_started_by_setup': False}, sys.stdout, indent=2)
    sys.stdout.write('\n')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
