#!/usr/bin/env python3
"""Opt-in local Serena launcher; absent/incompatible servers leave ordinary tools usable."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    parser.add_argument('--executable', default='serena')
    parser.add_argument('--prefix-arg', action='append', default=[])
    parser.add_argument('--check', action='store_true', help='probe CLI compatibility without starting a server')
    args = parser.parse_args()
    try:
        workspace = Path(args.workspace)
        if not workspace.is_absolute() or not workspace.is_dir():
            raise ValueError('workspace must be an existing absolute directory')
        executable = shutil.which(args.executable)
        if not executable:
            raise ValueError('Serena executable is unavailable')
        prefix = [executable, *args.prefix_arg]
        # Interactive runners must not consume the host's queued MCP request
        # while checking CLI compatibility; reserve stdin for the real server.
        version = subprocess.run([*prefix, '--version'], stdin=subprocess.DEVNULL,
                                 capture_output=True, text=True, timeout=10, check=True)
        help_result = subprocess.run([*prefix, 'start-mcp-server', '--help'], capture_output=True,
                                     stdin=subprocess.DEVNULL, text=True, timeout=10, check=True)
        for option in ('--context', '--mode', '--project', '--agent-interface'):
            if option not in help_result.stdout:
                raise ValueError(f'installed Serena lacks required option {option}')
        command = [*prefix, 'start-mcp-server', '--transport', 'stdio', '--project', str(workspace.resolve()),
                   '--context', str(Path(__file__).resolve().with_name('navigation.yml')),
                   '--mode', 'no-memories', '--mode', 'no-onboarding', '--agent-interface', 'tools']
        if args.check:
            print(json.dumps({'available': True, 'version': version.stdout.strip(), 'command': command,
                              'semantic_delivery_verified': False}))
            return 0
        # Preserve stdio for the MCP host; diagnostics go to stderr.
        os.execv(executable, command)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        message = f'Serena unavailable: {error}. Use rg, source reads, diffs and ordinary checks.'
        print(message, file=sys.stderr)
        if args.check:
            print(json.dumps({'available': False, 'fallback': message, 'semantic_delivery_verified': False}))
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
