#!/usr/bin/env python3
"""Build the exact Gate-3 decomposition patch from the accepted Git basis."""

from __future__ import annotations

import difflib
import subprocess
from pathlib import Path


SCA = Path(__file__).resolve().parent
BASIS = "c487b7dd57a378e2f74417118e78e7f61a161629"
TARGET = Path(
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)
CANDIDATE = SCA / "Candidate_Tree" / TARGET
OUTPUT = SCA / "Gate_3_Exact_Decomposition.patch"


def repo_root() -> Path:
    for parent in [SCA, *SCA.parents]:
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("repository root not found")


def main() -> None:
    root = repo_root()
    before = subprocess.check_output(
        ["git", "show", f"{BASIS}:{TARGET.as_posix()}"],
        cwd=root,
        text=True,
    )
    after = CANDIDATE.read_text(encoding="utf-8")
    diff = "".join(
        difflib.unified_diff(
            before.splitlines(keepends=True),
            after.splitlines(keepends=True),
            fromfile=f"a/{TARGET.as_posix()}",
            tofile=f"b/{TARGET.as_posix()}",
            n=0,
        )
    )
    if not diff:
        raise SystemExit("candidate has no changes")
    OUTPUT.write_text(diff, encoding="utf-8")
    print(f"PASS output={OUTPUT}")


if __name__ == "__main__":
    main()
