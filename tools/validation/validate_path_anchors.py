#!/usr/bin/env python3
"""Validate live agent surfaces do not bake machine-local home paths.

This validator is intentionally narrow. It checks instruction and executable
handoff surfaces that future agents may read as live directions. It ignores
historical evidence, generated outputs, archives, and plans.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


HOME_PATH_RE = re.compile(
    r"(?<![\w{])(?:/(?:Users|home)/[A-Za-z0-9._-]+[^\s`'\"<>)\]]*|[A-Za-z]:\\Users\\[A-Za-z0-9._-]+[^\s`'\"<>)\]]*)"
)

ACTIVE_COORDINATION_FILES = {"NEXT_INSTANCE_PROMPT.md", "_COORDINATION.md"}
TOOL_SUFFIXES = {".md", ".py", ".sh", ".swift", ".yml", ".yaml", ".json"}
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".sh", ".swift"}
EXCLUDED_DIR_NAMES = {
    ".git",
    ".archive",
    "__pycache__",
    "_run_records",
    "_Decomposition",
    "_Sources",
    "exports",
    "node_modules",
    "plans",
}


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    match: str
    text: str


def has_excluded_part(rel_path: Path) -> bool:
    return any(part in EXCLUDED_DIR_NAMES for part in rel_path.parts)


def is_tool_test(rel_path: Path) -> bool:
    return rel_path.parts[:1] == ("tools",) and rel_path.name.startswith("test_")


def is_live_surface(rel_path: Path) -> bool:
    if has_excluded_part(rel_path) or is_tool_test(rel_path):
        return False

    if rel_path in {Path("AGENTS.md"), Path("CLAUDE.md")}:
        return True

    if not rel_path.parts:
        return False

    top = rel_path.parts[0]
    if top == "agents" and rel_path.suffix in TEXT_SUFFIXES:
        return True
    if top == "skills" and rel_path.suffix in TEXT_SUFFIXES:
        return True
    if top == "tools" and rel_path.suffix in TOOL_SUFFIXES:
        return True
    if top == "init" and rel_path.suffix == ".md":
        return True

    if top in {"projects", "domains"}:
        if len(rel_path.parts) >= 4 and rel_path.parts[2] == "init" and rel_path.suffix == ".md":
            return True
        if (
            len(rel_path.parts) == 5
            and rel_path.parts[2] == "execution"
            and rel_path.parts[3] == "_Coordination"
            and rel_path.name in ACTIVE_COORDINATION_FILES
        ):
            return True

    return False


def iter_live_surface_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        rel_path = path.relative_to(repo_root)
        if is_live_surface(rel_path):
            files.append(path)
    return sorted(files)


def scan_file(path: Path, repo_root: Path) -> list[Finding]:
    rel = path.relative_to(repo_root).as_posix()
    findings: list[Finding] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return findings

    for line_no, line in enumerate(lines, start=1):
        for match in HOME_PATH_RE.finditer(line):
            findings.append(
                Finding(
                    path=rel,
                    line=line_no,
                    match=match.group(0),
                    text=line.strip(),
                )
            )
    return findings


def scan(repo_root: Path) -> dict[str, object]:
    root = repo_root.resolve()
    checked_files = iter_live_surface_files(root)
    findings: list[Finding] = []
    for path in checked_files:
        findings.extend(scan_file(path, root))
    return {
        "repo_root": str(root),
        "checked_file_count": len(checked_files),
        "finding_count": len(findings),
        "findings": [asdict(finding) for finding in findings],
    }


def render_text(report: dict[str, object]) -> str:
    finding_count = int(report["finding_count"])
    checked_count = int(report["checked_file_count"])
    if finding_count == 0:
        return f"PASS: no literal home-dir absolute paths found in {checked_count} live path-anchor surfaces"

    lines = [
        f"FAIL: {finding_count} literal home-dir absolute path finding(s) in {checked_count} live path-anchor surfaces"
    ]
    for finding in report["findings"]:
        lines.append(f"{finding['path']}:{finding['line']}: {finding['match']}")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_root", nargs="?", default=".", help="Repository root to scan.")
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--json", action="store_true", help="Emit JSON report.")
    output.add_argument("--text", action="store_true", help="Emit text report.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    report = scan(Path(args.repo_root))
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(render_text(report))
    return 0 if int(report["finding_count"]) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
