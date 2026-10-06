#!/usr/bin/env python3
"""Build one candidate and run the independent S01 checks in a fresh directory."""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path, help="directory containing ExpenseSummary.csproj")
    parser.add_argument("--reserved", action="store_true", help="also run reserved transfer cases")
    arguments = parser.parse_args()
    candidate = arguments.candidate.resolve()
    if not (candidate / "ExpenseSummary.csproj").is_file():
        parser.error("candidate must contain ExpenseSummary.csproj")

    checks = Path(__file__).resolve().parent / "checks"
    try:
        with tempfile.TemporaryDirectory(prefix="mentor-expense-checks-") as temporary:
            project_directory = Path(temporary)
            for name in ("ExpenseSummary.Checks.csproj", "Program.cs"):
                shutil.copy(checks / name, project_directory / name)
            project = project_directory / "ExpenseSummary.Checks.csproj"
            candidate_property = f"-p:CandidateDirectory={candidate}"

            # Every candidate uses the same assembly name. Rebuild its reference
            # assembly and isolate check outputs to avoid reusing another run.
            build = subprocess.run([
                "dotnet", "build", str(project), "--no-incremental", candidate_property,
            ], check=False)
            if build.returncode != 0:
                return build.returncode
            command = ["dotnet", "run", "--project", str(project), "--no-build", candidate_property]
            if arguments.reserved:
                command.extend(["--", "--reserved"])
            return subprocess.run(command, check=False).returncode
    except OSError as error:
        print(f"Expense checks failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
