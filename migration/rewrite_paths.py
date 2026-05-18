#!/usr/bin/env python3
"""Inventory and apply approved path rewrites for the Chirality repo migration."""

from __future__ import annotations

import argparse
import csv
import os
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PATTERNS = [
    "/Users/ryan/ai-env/projects/chirality-app",
    "/Users/ryan/ai-env/projects/chirality-app-test",
    "/Users/ryan/ai-env/projects/chirality-app-dev",
    "/Users/ryan/ai-env/projects/chirality-piping",
    "chirality-app-test/",
    "domain-test/",
    "project-test/",
]

SKIP_DIRS = {
    ".git",
    ".archive",
    ".Archive",
    "_archive",
    "_Archive",
    ".claude",
    ".chirality",
    ".checkpoints",
    "__pycache__",
    ".pytest_cache",
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
}

TEXT_SUFFIXES = {
    ".csv",
    ".json",
    ".js",
    ".jsx",
    ".md",
    ".mjs",
    ".py",
    ".sh",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True)
class Rewrite:
    old: str
    new: str


def load_rewrites(path: Path) -> list[Rewrite]:
    text = path.read_text(encoding="utf-8")
    rewrites: list[Rewrite] = []
    current: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line == "rewrites:":
            continue
        if line.startswith("- old:"):
            if current:
                rewrites.append(Rewrite(current["old"], current["new"]))
                current = {}
            current["old"] = line.split(":", 1)[1].strip().strip('"')
        elif line.startswith("old:"):
            current["old"] = line.split(":", 1)[1].strip().strip('"')
        elif line.startswith("new:"):
            current["new"] = line.split(":", 1)[1].strip().strip('"')
    if current:
        rewrites.append(Rewrite(current["old"], current["new"]))
    return rewrites


def is_probably_text(path: Path) -> bool:
    if path.suffix in TEXT_SUFFIXES:
        return True
    try:
        sample = path.read_bytes()[:4096]
    except OSError:
        return False
    return b"\0" not in sample


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        base = Path(dirpath)
        for name in filenames:
            path = base / name
            if path.name == ".DS_Store" or path.suffix in {".pyc", ".zip", ".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff"}:
                continue
            rel = path.relative_to(root).as_posix()
            if rel.startswith("migration/path_reference_audit") and rel.endswith(".csv"):
                continue
            if is_probably_text(path):
                yield path


def classify(rel: str, match: str) -> str:
    parts = rel.split("/")
    if rel.startswith("migration/"):
        return "historical"
    if rel.startswith("exports/"):
        return "historical"
    if "/historical-imports/" in rel:
        return "historical"
    if rel.startswith("plans/historical-imports/"):
        return "historical"
    if "/provenance/" in rel:
        return "historical"
    if "/_run_records/" in rel or rel.endswith("source-state.md"):
        return "historical"
    if rel.startswith("examples/"):
        return "example-only"
    if rel.startswith("projects/") and "/execution/" in rel:
        return "historical"
    if "/_Sources/" in rel or "_Sources/" in match:
        return "manual-domain-corpus"
    if rel.startswith(("agents/", "skills/", "tools/", "docs/")):
        return "active"
    if rel.startswith("projects/") and any(p in parts for p in ["docs", "frontend", "apps", "api", "core", "schemas", "tests", "validation", "plans", "init"]):
        return "active"
    if rel.startswith("domains/") and not any(p in rel for p in ["/_Sources/", "/_LocalIndexes/"]):
        return "active"
    return "needs-review"


def inventory(root: Path, output: Path, patterns: list[str], rewrites: list[Rewrite]) -> int:
    rows: list[dict[str, str]] = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), start=1):
            matches = [p for p in patterns if p in line]
            for match in matches:
                replacement = ""
                for rw in rewrites:
                    if rw.old in line:
                        replacement = rw.new
                        break
                rows.append(
                    {
                        "file": rel,
                        "line": str(lineno),
                        "match": match,
                        "classification": classify(rel, match),
                        "action": "rewrite" if replacement else "none",
                        "replacement": replacement,
                        "excerpt": line.strip()[:500],
                    }
                )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["file", "line", "match", "classification", "action", "replacement", "excerpt"],
        )
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def apply_rewrites(root: Path, audit: Path, rewrites: list[Rewrite]) -> tuple[int, int]:
    active_files: set[str] = set()
    with audit.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row["classification"] == "active" and row["action"] == "rewrite":
                active_files.add(row["file"])
    changed_files = 0
    replacements = 0
    for rel in sorted(active_files):
        path = root / rel
        text = path.read_text(encoding="utf-8")
        new_text = text
        for rw in rewrites:
            count = new_text.count(rw.old)
            if count:
                replacements += count
                new_text = new_text.replace(rw.old, rw.new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed_files += 1
    return changed_files, replacements


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root to scan")
    parser.add_argument("--map", default="migration/path_map.yaml", help="Path rewrite map")
    parser.add_argument("--audit", default="migration/path_reference_audit.csv", help="Audit CSV path")
    parser.add_argument("--inventory", action="store_true", help="Write path reference inventory")
    parser.add_argument("--apply", action="store_true", help="Apply active rewrites from audit CSV")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    rewrites = load_rewrites(root / args.map)
    patterns = sorted(set(DEFAULT_PATTERNS + [rw.old for rw in rewrites]), key=len, reverse=True)
    audit = root / args.audit

    if args.inventory:
        count = inventory(root, audit, patterns, rewrites)
        print(f"wrote {count} references to {audit}")
    if args.apply:
        changed, replacements = apply_rewrites(root, audit, rewrites)
        print(f"rewrote {replacements} references in {changed} files")
    if not args.inventory and not args.apply:
        parser.error("choose --inventory and/or --apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
