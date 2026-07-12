#!/usr/bin/env python3
"""Validate root instruction entrypoints and the Claude import contract."""

from __future__ import annotations

import argparse
from pathlib import Path


EXPECTED_CLAUDE = "@AGENTS.md\n"


def validate(repo_root: Path) -> list[str]:
    findings: list[str] = []
    agents = repo_root / "AGENTS.md"
    claude = repo_root / "CLAUDE.md"
    if not agents.is_file():
        findings.append("missing root AGENTS.md")
    if not claude.is_file():
        findings.append("missing root CLAUDE.md")
    elif claude.read_text(encoding="utf-8") != EXPECTED_CLAUDE:
        findings.append("CLAUDE.md must contain exactly '@AGENTS.md\\n'")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_root", nargs="?", default=".")
    args = parser.parse_args()
    findings = validate(Path(args.repo_root).resolve())
    if findings:
        for finding in findings:
            print(f"FAIL: {finding}")
        return 1
    print("PASS: root instruction entrypoints are canonical")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
