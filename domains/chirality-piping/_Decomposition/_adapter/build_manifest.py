#!/usr/bin/env python3
"""Build the file-level Source_Manifest.csv for the chirality-piping domain pack.

Walks the SOURCE repo (projects/chirality-piping/), classifies every file by the
Gate-1 source boundary, computes SHA-256, and emits a reference-compatible
9-column manifest. AtomizeInV1 is NOT a manifest column; it is derived from
SourceGroup by the intake adapter (run_intake.py).

Boundary rules are documented in _Sources/SOURCE_BOUNDARY.md.
"""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

# --- paths -----------------------------------------------------------------
PACK_ROOT = Path(__file__).resolve().parents[2]            # domains/chirality-piping
REPO_ROOT = (PACK_ROOT / "../../projects/chirality-piping").resolve()
OUT = PACK_ROOT / "_Sources" / "Source_Manifest.csv"

FIELDS = ["SourceDocID", "SourceName", "RepoRelPath", "SourceGroup",
          "AuthorityRole", "IncludeInIndex", "ArchiveState", "ExpectedSha256", "Notes"]

SLUG_RE = re.compile(r"[^A-Za-z0-9]+")

# --- exclusions ------------------------------------------------------------
# Top-level repo folders never admitted.
TOP_EXCLUDE_DIRS = {".archive", ".github", ".claude", "init", "plans",
                    "provenance", ".git", ".pytest_cache", "node_modules",
                    "examples", "fixtures"}
# Anywhere-excluded path segments.
SEG_EXCLUDE = {".archive", "_Archive", "_run_records", "0_References",
               "node_modules", "target", "dist", ".next", "dist-electron",
               ".chirality", "__pycache__", ".pytest_cache"}
EXCLUDE_BASENAMES = {".DS_Store", "_LATEST.md", "LICENSE.md", "INIT.md",
                     "package.json", "package-lock.json", "requirements-dev.txt"}
EXCLUDE_EXTS = {".map", ".pyc", ".lock", ".wasm", ".tsbuildinfo", ".gitignore"}

# Process-log basenames / prefixes -> excluded everywhere (provenance, not knowledge).
PROCESS_LOG_BASENAMES = {
    "RUN_SUMMARY.md", "Decision_Log.md", "Brief.md", "Handoff_State.md",
    "ACCEPTANCE_RECORD.md", "APPROVAL_RECORD.md", "PROPOSAL_RECORD.md",
    "Review_Summary.md", "QA_Report.md", "_REVIEW.md",
    # deliverable meta docs (only KT-suffix docs are admitted in deliverables)
    "_SEMANTIC.md", "_SEMANTIC_LENSING.md", "_CONTEXT.md", "_DEPENDENCIES.md",
    "_REFERENCES.md", "_STATUS.md", "MEMORY.md",
}
PROCESS_LOG_PREFIXES = ("TASK_RUN_", "RUN_", "PREPARATION_RUN_")
# Substrings marking a file as inter-session coordination / handoff (process only).
PROCESS_LOG_SUBSTRINGS = ("NEXT_INSTANCE", "NEXT_SESSION")

# Deliverable admission: the four canonical knowledge-type docs by basename suffix.
DELIVERABLE_KT_SUFFIXES = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")

# Code roots -> grouped, atomized source unit per top-level folder.
CODE_DIRS = {
    "core": "CODE_CORE", "apps": "CODE_APPS", "tests": "CODE_TESTS",
    "tools": "CODE_TOOLS", "validation": "CODE_VALIDATION",
}
CODE_EXTS = {".py", ".rs", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
             ".css", ".scss", ".html", ".toml", ".md"}

# Index-only structured data.
SCHEMA_EXTS = {".yaml", ".yml", ".json"}


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def doc_id(rel: str) -> str:
    stem = rel.rsplit(".", 1)[0] if "." in Path(rel).name else rel
    return "SRC-" + SLUG_RE.sub("-", stem).strip("-").upper()


def is_excluded(rel: str) -> bool:
    parts = rel.split("/")
    if parts[0] in TOP_EXCLUDE_DIRS:
        return True
    if any(seg in SEG_EXCLUDE for seg in parts):
        return True
    name = Path(rel).name
    if name in EXCLUDE_BASENAMES:
        return True
    if Path(rel).suffix in EXCLUDE_EXTS:
        return True
    return False


def is_process_log(name: str) -> bool:
    return (name in PROCESS_LOG_BASENAMES
            or name.startswith(PROCESS_LOG_PREFIXES)
            or any(s in name for s in PROCESS_LOG_SUBSTRINGS))


def classify(rel: str):
    """Return (SourceGroup, AuthorityRole, IncludeInIndex, Notes) or None to skip."""
    name = Path(rel).name
    ext = Path(rel).suffix
    parts = rel.split("/")
    top = parts[0]

    # --- root governance ---------------------------------------------------
    # INIT.md is a session-bootstrap launcher (no headings, no domain knowledge);
    # excluded via EXCLUDE_BASENAMES above.
    if rel in {"AGENTS.md", "README.md", "CONTRIBUTING.md"}:
        return ("ROOT_DOCS", "ROOT_AUTHORITY", "YES", "Root agent-operating / project governance.")

    # --- top-level governance/ policy --------------------------------------
    if top == "governance" and ext == ".md" and not is_process_log(name):
        return ("PRODUCT_DOCS", "GOVERNANCE_AUTHORITY", "YES", "Root governance policy.")

    # --- docs/ -------------------------------------------------------------
    if top == "docs":
        if is_process_log(name):
            return None
        if ext == ".md":
            return ("PRODUCT_DOCS", "PRODUCT_AUTHORITY", "YES", "Product/specification handbook.")
        if name == "MANIFEST.json":
            return ("SCHEMAS", "SCHEMA_AUTHORITY", "YES", "Docs manifest sidecar; index-only.")
        return None

    # --- api/ + schemas/ : index-only structured data ----------------------
    if top == "api" and ext in SCHEMA_EXTS:
        return ("SCHEMAS", "SCHEMA_AUTHORITY", "YES", "API boundary contract; index-only.")
    if top == "schemas" and ext in SCHEMA_EXTS:
        return ("SCHEMAS", "SCHEMA_AUTHORITY", "YES", "Canonical domain schema; index-only.")

    # --- execution/ --------------------------------------------------------
    if top == "execution":
        if ext != ".md" or is_process_log(name):
            return None
        # deliverable: admit ONLY the four canonical knowledge-type docs.
        if len(parts) >= 4 and parts[2] == "1_Working" and parts[3].startswith("DEL-"):
            if name.endswith(DELIVERABLE_KT_SUFFIXES):
                return ("EXECUTION_DELIVERABLE", "DELIVERABLE_AUTHORITY", "YES",
                        "Deliverable knowledge-type doc (Datasheet/Specification/Guidance/Procedure suffix).")
            return None
        # governance: only _Decomposition and _ScopeChange subtrees.
        if len(parts) >= 2 and parts[1] in {"_Decomposition", "_ScopeChange"}:
            return ("EXECUTION_GOVERNANCE", "GOVERNANCE_AUTHORITY", "YES",
                    "Execution governance (software-decomposition / scope-change) doc.")
        return None

    # --- code roots --------------------------------------------------------
    if top in CODE_DIRS:
        if ext in CODE_EXTS:
            return (CODE_DIRS[top], "CODE_AUTHORITY", "YES",
                    f"{top}/ source; grouped code unit (atomized).")
        return None

    return None


def main() -> int:
    rows = []
    seen_ids: dict[str, str] = {}
    for p in sorted(REPO_ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(REPO_ROOT).as_posix()
        if is_excluded(rel):
            continue
        c = classify(rel)
        if c is None:
            continue
        group, authority, include, notes = c
        sid = doc_id(rel)
        if sid in seen_ids:
            sid = f"{sid}-{len(seen_ids)}"  # disambiguate rare collisions
        seen_ids[sid] = rel
        rows.append({
            "SourceDocID": sid,
            "SourceName": Path(rel).name,
            "RepoRelPath": rel,
            "SourceGroup": group,
            "AuthorityRole": authority,
            "IncludeInIndex": include,
            "ArchiveState": "ACTIVE",
            "ExpectedSha256": sha256_file(p),
            "Notes": notes,
        })

    rows.sort(key=lambda r: (r["SourceGroup"], r["RepoRelPath"]))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    # summary to stdout
    from collections import Counter
    by_group = Counter(r["SourceGroup"] for r in rows)
    print(f"repo_root={REPO_ROOT}")
    print(f"manifest={OUT}")
    print(f"total_rows={len(rows)}")
    for g in sorted(by_group):
        print(f"  {g:24s} {by_group[g]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
