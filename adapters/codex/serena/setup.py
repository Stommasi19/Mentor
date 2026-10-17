#!/usr/bin/env python3
"""Inspect registration or print an opt-in snippet; never overwrite host configuration."""
import argparse
import json
import os
from pathlib import Path
import sys
import subprocess
import tomllib


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    parser.add_argument('--config', default=str(Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'config.toml'))
    parser.add_argument('--connected-server', action='append', default=[],
                        help='Name already observed in the live host inventory (including plugin connections)')
    parser.add_argument('--executable', help='Use an installed runner rather than provisioning one')
    parser.add_argument('--apply', action='store_true', help='Set up Serena if the connection is missing')
    args = parser.parse_args()
    try:
        workspace = Path(args.workspace)
        if not workspace.is_absolute() or not workspace.is_dir():
            raise ValueError('workspace must be an existing absolute directory')
        configuration = Path(args.config)
        if args.apply:
            if not configuration.is_absolute() or configuration.name != 'config.toml':
                raise ValueError('apply requires an absolute Codex config.toml path')
            command = [sys.executable, str(Path(__file__).resolve().parent.parent / 'setup_mcp.py'),
                       '--workspace', str(workspace), '--codex-home', str(configuration.parent), '--server', 'serena', '--apply']
            for name in args.connected_server:
                command += ['--connected-serena', name]
            if args.executable:
                command += ['--serena-executable', args.executable]
            return subprocess.call(command)
        settings = tomllib.loads(configuration.read_text()) if configuration.exists() else {}
        servers = settings.get('mcp_servers', {})
        if not isinstance(servers, dict) or any(not isinstance(entry, dict) for entry in servers.values()):
            raise ValueError('MCP registrations must be tables')
        registered = sorted({name for name, entry in servers.items()
            if 'serena' in name.lower() or 'serena' in
            (str(entry.get('command', '')) + ' ' + str(entry.get('args', []))).lower()}
            | set(args.connected_server))
        if registered:
            print(json.dumps({'registered_names': registered, 'action': 'inspect-and-reuse',
                'live_connection_verified': False,
                'next': 'Verify exposed tools, activate the selected project, disable memory/onboarding and editing, then use read-only symbols/references. Do not add a duplicate registration or choose another port. If disabled/incompatible, use ordinary tools.'}))
            return 0
        launcher = Path(__file__).resolve().with_name('launch.py')
        print('# Opt-in example only: review in the host, then verify actual delivery.')
        print('[mcp_servers.mentor_serena]')
        print('command = ' + json.dumps(sys.executable))
        print('args = ' + json.dumps([str(launcher), '--workspace', str(workspace.resolve()), '--executable', args.executable or 'serena']))
    except (OSError, ValueError) as error:
        print(f'Serena setup failed: {error}; retain ordinary-tool fallback.', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
