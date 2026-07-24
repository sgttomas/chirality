#!/usr/bin/env python3
"""Build the public chirality-app export staging tree."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
import sys
from pathlib import Path


PROFILE_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROFILE_DIR.parents[1]
DEFAULT_STAGE = PROFILE_DIR / "staging"
MANIFEST_PATH = PROFILE_DIR / "export-manifest.csv"
REPORT_PATH = PROFILE_DIR / "export-report.md"

ROOT_FILES = [
    ".gitignore",
    "AGENTS.md",
    "CLAUDE.md",
    "CHIRALITY_FRAMEWORK.md",
    "PROFESSIONAL_ENGINEERING.md",
    "LICENSE.md",
]

PUBLIC_ROOT_FILES = {
    "README.md": PROFILE_DIR / "PUBLIC_README.md",
}

ROOT_DIRS = [
    ".github",
    "agents",
    "skills",
    "tools",
    "docs",
    "init",
    "runtime",
]

EXCLUDED_PUBLIC_PATHS = {
    ".github/workflows/harness-premerge.yml",
    "tools/practitioner_harness/BACKLOG.md",
}

EXCLUDED_PUBLIC_PREFIXES = (
    "docs/governance_harness/briefs/",
)

SKIP_DIRS = {
    ".git",
    ".Archive",
    ".archive",
    ".claude",
    ".chirality",
    ".checkpoints",
    ".pytest_cache",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    ".next",
    "dist",
    "dist-electron",
    "build",
    "target",
    "out",
    "artifacts",
    "_Sources",
    "_LocalIndexes",
    "migration",
    "projects",
    "domains",
    "plans",
    "exports",
}

SKIP_FILE_NAMES = {
    ".DS_Store",
}

SKIP_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".zip",
    ".pdf",
    ".PDF",
    ".tsbuildinfo",
}

TEXT_SUFFIXES = {
    ".cjs",
    ".css",
    ".csv",
    ".html",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".plist",
    ".py",
    ".sh",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}

PUBLIC_REPLACEMENTS = [
    ("/Users/ryan/ai-env/projects/chirality-app-test/test/", "examples/"),
    ("/Users/ryan/ai-env/projects/chirality-app-test/", "<legacy-chirality-app-test>/"),
    ("/Users/ryan/ai-env/projects/chirality-app-dev/", "<legacy-chirality-app-dev>/"),
    ("/Users/ryan/ai-env/projects/chirality-piping/", "<legacy-chirality-piping>/"),
    ("/Users/ryan/ai-env/projects/chirality-app", "<chirality-app-root>"),
    ("/Users/ryan/ai-env/projects/chirality", "<chirality-root>"),
]

PUBLIC_README_REQUIRED_MARKERS = (
    "https://github.com/sgttomas/chirality-app/releases/latest",
    "The desktop application source is not currently included",
    "runtime/",
)

PUBLIC_README_FORBIDDEN_MARKERS = (
    "This repository is the private canonical source tree",
    "## Private Canonical Repository",
    "Private maintainer and development roots",
    "projects/chirality-app-dev",
    "exports/chirality-app",
)


def should_skip(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return True
    if path.name in SKIP_FILE_NAMES:
        return True
    if path.suffix in SKIP_SUFFIXES:
        return True
    if path.name.startswith(".env"):
        return True
    return False


def copy_tree(src: Path, dest: Path, root_name: str) -> None:
    for path in src.rglob("*"):
        rel = path.relative_to(src)
        public_rel = (Path(root_name) / rel).as_posix()
        if public_rel in EXCLUDED_PUBLIC_PATHS or public_rel.startswith(EXCLUDED_PUBLIC_PREFIXES):
            continue
        if should_skip(rel):
            if path.is_dir():
                continue
            continue
        target = dest / rel
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)


def write_public_init_prompt(stage: Path) -> None:
    target = stage / "init" / "init-prompt.md"
    target.write_text(
        """# Public session init prompt

This public export does not include the private project loop entrypoints. Start
from the target workspace and select an Agent 0 or Agent 1 role from
`AGENTS.md`.

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Read `{REPO_ROOT}/AGENTS.md`, then read the selected instruction package under
`{REPO_ROOT}/agents/`.

State the target workspace, objective, accepted basis, authority, read scope,
write scope, tools, expected return, and human decision points before acting.
</init-prompt>
""",
        encoding="utf-8",
    )


def sanitize_text_files(stage: Path) -> int:
    changed = 0
    for path in stage.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = text
        for old, new in PUBLIC_REPLACEMENTS:
            updated = updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def build_stage(stage: Path) -> int:
    missing = [name for name in ROOT_FILES + ROOT_DIRS if not (REPO_ROOT / name).exists()]
    missing.extend(
        str(source.relative_to(REPO_ROOT))
        for source in PUBLIC_ROOT_FILES.values()
        if not source.exists()
    )
    if missing:
        raise SystemExit(
            "allowlisted roots missing from repo root: "
            + ", ".join(missing)
            + "; update ROOT_FILES/ROOT_DIRS to match the tree"
        )

    claude_contract = (REPO_ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    if claude_contract != "@AGENTS.md\n":
        raise SystemExit("CLAUDE.md must contain exactly '@AGENTS.md\\n'")

    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)

    for name in ROOT_FILES:
        shutil.copy2(REPO_ROOT / name, stage / name)

    for public_name, source in PUBLIC_ROOT_FILES.items():
        shutil.copy2(source, stage / public_name)

    for name in ROOT_DIRS:
        copy_tree(REPO_ROOT / name, stage / name, name)

    write_public_init_prompt(stage)

    return sanitize_text_files(stage)


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def write_manifest(stage: Path, output: Path) -> int:
    rows = []
    for path in iter_files(stage):
        rel = path.relative_to(stage).as_posix()
        data = path.read_bytes()
        rows.append(
            {
                "path": rel,
                "size_bytes": str(len(data)),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    with output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["path", "size_bytes", "sha256"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def boundary_findings(stage: Path) -> list[str]:
    findings: list[str] = []
    public_readme = stage / "README.md"
    if not public_readme.is_file():
        findings.append("public README is missing: README.md")
    else:
        public_readme_text = public_readme.read_text(encoding="utf-8")
        for marker in PUBLIC_README_REQUIRED_MARKERS:
            if marker not in public_readme_text:
                findings.append(f"public README missing required marker: {marker}")
        for marker in PUBLIC_README_FORBIDDEN_MARKERS:
            if marker.casefold() in public_readme_text.casefold():
                findings.append(f"private canonical README marker in public README: {marker}")

    forbidden_top = {"projects", "domains", "migration", "plans", "exports"}
    for path in stage.rglob("*"):
        rel = path.relative_to(stage).as_posix()
        parts = path.relative_to(stage).parts
        if parts and parts[0] in forbidden_top:
            findings.append(f"forbidden top-level path: {rel}")
        if path.is_dir() and path.name in SKIP_DIRS:
            findings.append(f"forbidden directory: {rel}")
        if path.is_file():
            if path.name in SKIP_FILE_NAMES or path.name.startswith(".env") or path.suffix in {".pyc", ".zip", ".pdf", ".PDF", ".tsbuildinfo"}:
                findings.append(f"forbidden file: {rel}")
            if path.suffix in TEXT_SUFFIXES:
                try:
                    text = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                private_home = re.search(
                    r"(?:/Users/|/home/)(?!<|example(?:/|\b)|fixture(?:/|\b))[^/\s`]+/",
                    text,
                ) or re.search(
                    r"[A-Za-z]:\\Users\\(?!example(?:\\|\b)|fixture(?:\\|\b))[^\\\s`]+\\",
                    text,
                )
                if private_home:
                    findings.append(f"private absolute path reference: {rel}")
    return findings


def write_report(stage: Path, manifest_count: int, sanitized_count: int, findings: list[str], output: Path) -> None:
    top_counts: dict[str, int] = {}
    for path in iter_files(stage):
        rel = path.relative_to(stage)
        top = rel.parts[0] if rel.parts else rel.as_posix()
        top_counts[top] = top_counts.get(top, 0) + 1

    try:
        stage_display = stage.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        stage_display = str(stage)

    lines = [
        "# chirality-app Public Export Report",
        "",
        "Generated from private `chirality` export profile `exports/chirality-app`.",
        "",
        f"- Staging path: `{stage_display}`",
        f"- Manifest rows: {manifest_count}",
        f"- Text files sanitized for private absolute paths: {sanitized_count}",
        f"- Boundary findings: {len(findings)}",
        "",
        "## Top-Level File Counts",
        "",
        "| Path | Files |",
        "|---|---:|",
    ]
    for key in sorted(top_counts):
        lines.append(f"| `{key}` | {top_counts[key]} |")
    lines.extend(["", "## Boundary Findings", ""])
    if findings:
        lines.extend(f"- {item}" for item in findings[:500])
        if len(findings) > 500:
            lines.append(f"- ... {len(findings) - 500} additional findings omitted")
    else:
        lines.append("No boundary findings.")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def apply_target(stage: Path, target: Path) -> None:
    if not (target / ".git").exists():
        raise SystemExit(f"refusing to apply: target has no .git directory: {target}")
    for item in target.iterdir():
        if item.name == ".git":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    for item in stage.iterdir():
        dest = target / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage-dir", default=str(DEFAULT_STAGE))
    parser.add_argument("--apply-target", help="Replace a local chirality-app worktree from the clean staging tree")
    args = parser.parse_args()

    stage = Path(args.stage_dir).resolve()
    sanitized_count = build_stage(stage)
    manifest_count = write_manifest(stage, MANIFEST_PATH)
    findings = boundary_findings(stage)
    write_report(stage, manifest_count, sanitized_count, findings, REPORT_PATH)

    if findings:
        print(f"export failed boundary scan with {len(findings)} findings", file=sys.stderr)
        print(f"see {REPORT_PATH}", file=sys.stderr)
        return 2

    if args.apply_target:
        apply_target(stage, Path(args.apply_target).resolve())
        print(f"applied public export to {args.apply_target}")
    print(f"staged {manifest_count} files at {stage}")
    print(f"wrote {MANIFEST_PATH}")
    print(f"wrote {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
