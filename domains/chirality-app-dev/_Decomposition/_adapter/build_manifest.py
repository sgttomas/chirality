#!/usr/bin/env python3
"""Build the file-level Source_Manifest.csv for the chirality-app-dev domain pack.

Walks the SOURCE repo (projects/chirality-app-dev/), classifies every file by the
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
PACK_ROOT = Path(__file__).resolve().parents[2]            # domains/chirality-app-dev
REPO_ROOT = (PACK_ROOT / "../../projects/chirality-app-dev").resolve()
OUT = PACK_ROOT / "_Sources" / "Source_Manifest.csv"

FIELDS = ["SourceDocID", "SourceName", "RepoRelPath", "SourceGroup",
          "AuthorityRole", "IncludeInIndex", "ArchiveState", "ExpectedSha256", "Notes"]

SLUG_RE = re.compile(r"[^A-Za-z0-9]+")

# --- exclusions ------------------------------------------------------------
# Top-level repo folders/files never admitted.
TOP_EXCLUDE_DIRS = {".archive", ".github", "init", "plans", "provenance", ".git"}
# Anywhere-excluded path segments.
SEG_EXCLUDE = {".archive", "_Archive", "node_modules", "dist", ".next",
               "dist-electron", ".chirality", "__pycache__"}
EXCLUDE_BASENAMES = {".DS_Store"}
EXCLUDE_EXTS = {".map", ".pyc"}

# Deliverable admission: knowledge-type docs by basename SUFFIX, so nested
# Packet_Datasheet.md / Case_Datasheet.md etc. are admitted alongside the
# canonical Datasheet.md/Specification.md/Guidance.md/Procedure.md (OI-009).
DELIVERABLE_KT_SUFFIXES = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")

# Frontend code roots admitted index-only.
FRONTEND_CODE_DIRS = ("frontend/src/", "frontend/electron/", "frontend/scripts/")
FRONTEND_CODE_EXTS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
                      ".css", ".scss", ".json", ".yaml", ".yml", ".html"}


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
    if Path(rel).name in EXCLUDE_BASENAMES:
        return True
    if Path(rel).suffix in EXCLUDE_EXTS:
        return True
    return False


def classify(rel: str):
    """Return (SourceGroup, AuthorityRole, IncludeInIndex, Notes) or None to skip."""
    name = Path(rel).name
    ext = Path(rel).suffix
    parts = rel.split("/")

    # --- root --------------------------------------------------------------
    if rel == "AGENTS.md":
        return ("ROOT_DOCS", "ROOT_AUTHORITY", "YES", "Root agent-operating governance.")

    # --- docs/ -------------------------------------------------------------
    if parts[0] == "docs":
        if ext == ".md":
            return ("PRODUCT_DOCS", "PRODUCT_AUTHORITY", "YES", "Product/specification handbook.")
        if name == "MANIFEST.json":
            return ("PRODUCT_DOCS", "PRODUCT_AUTHORITY", "YES", "Docs manifest sidecar; index-only.")
        return None

    # --- execution/ --------------------------------------------------------
    if parts[0] == "execution":
        if ext != ".md":
            return None  # csv/json/py data + scripts excluded
        # process logs -> excluded entirely (not indexed, not atomized)
        if "_run_records" in parts or name in {"RUN_SUMMARY.md", "Decision_Log.md"}:
            return None
        # deliverable: admit ONLY the four canonical knowledge-type docs
        # (operator direction). Meta docs (_SEMANTIC/_CONTEXT/_DEPENDENCIES/
        # _REFERENCES/_STATUS/_SEMANTIC_LENSING), CONTROL/README, and nested
        # non-canonical packet docs are NOT admitted.
        if len(parts) >= 4 and parts[2] == "1_Working" and parts[3].startswith("DEL-"):
            if name.endswith(DELIVERABLE_KT_SUFFIXES):
                return ("EXECUTION_DELIVERABLE", "DELIVERABLE_AUTHORITY", "YES",
                        "Deliverable knowledge-type doc (Datasheet/Specification/Guidance/Procedure suffix; incl. nested Packet_/Case_).")
            return None  # non-KT deliverable file (meta docs, QA/Rationale/Contract, CONTROL/README) excluded
        # everything else substantive -> governance
        return ("EXECUTION_GOVERNANCE", "GOVERNANCE_AUTHORITY", "YES",
                "Execution governance / reconciliation / scope-change / decomposition doc.")

    # --- frontend/ ---------------------------------------------------------
    if parts[0] == "frontend":
        if ext == ".md":
            return ("FRONTEND_DOCS", "FRONTEND_AUTHORITY", "YES", "Frontend prose doc.")
        # index-only code: under code roots, or a top-level frontend config file
        under_code_root = any(rel.startswith(d) for d in FRONTEND_CODE_DIRS)
        top_level_config = (len(parts) == 2 and ext in FRONTEND_CODE_EXTS)
        if (under_code_root or top_level_config) and ext in FRONTEND_CODE_EXTS:
            return ("FRONTEND_SRC", "FRONTEND_CODE", "YES",
                    "Frontend application source; index-only, not atomized.")
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
