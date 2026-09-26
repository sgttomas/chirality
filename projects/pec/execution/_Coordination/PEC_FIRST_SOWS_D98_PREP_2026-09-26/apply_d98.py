#!/usr/bin/env python3
"""D-PEC-98 bound act: create the two first ScopeOfWork.md files, byte-exact.

Usage (from anywhere):
  apply_d98.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

<DIR> holds the candidate files at their repository-relative paths.

Failure semantics:
- Preflight (candidate hashes, targets absent, pinned hashes, write-set plan):
  any failure exits 1 before any byte is written.
- Write: each file is written to a temporary sibling, hash-checked, then renamed
  into place. If any step after the first write fails (I/O error, hash
  mismatch, post-write inventory mismatch), the script removes every temporary
  file and every target it created, and exits 1. On exit 1 no target file and
  no temporary file remains.
- Write-set check: the script inventories every file under projects/pec (path
  and SHA-256) before and after the write and requires the difference to be
  exactly the two targets, both created, with nothing modified or removed.
- A second run fails preflight (targets already exist).
It never touches _STATUS.md or any other existing file. Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

P = "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/"
TARGETS = {
    P + "DEL-02-08_Work_graph_parser/ScopeOfWork.md":
        "03cce13f484a9b595b5162bd662af42bcd67aae37a8843304bf03cfbb3badc0a",
    P + "DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md":
        "aafb54fd6457f09da8304ead444686703d5f8d2c28f4c94ec4eab4d2737b188b",
}
# Read-only files the act re-verifies (values at origin/main 53145aaeb).
PINNED = {
    "projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md": "dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660",
    "projects/pec/execution/_Decomposition/Deliverables.csv": "b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a",
    "projects/pec/execution/_Decomposition/ScopeLedger.csv": "83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df",
    "projects/pec/docs/PRD.md": "fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32",
    P + "DEL-02-08_Work_graph_parser/_STATUS.md": "d80800a48b45a43d641916bd5ee67c4b478e21538281b833e34dbc7cfe5f0eef",
    P + "DEL-02-09_MEMORY_run_index_parser/_STATUS.md": "3e14313c78e2500cabbd3f4897f9095daabc75c6468169074cb4400f4667d768",
    P + "DEL-02-08_Work_graph_parser/Dependencies.csv": "c23cd711fc8762dbd4a8629ba277753544f9f9e91368f789140b040f94cf701e",
    P + "DEL-02-09_MEMORY_run_index_parser/Dependencies.csv": "41afd6dc44f21200f6b2a1c480e9175d98b64d49b12e638bca67edcd15168e4b",
}
TMP_SUFFIX = ".d98tmp"

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def inventory(repo):
    base = repo / "projects/pec"; inv = {}
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        for f in filenames:
            p = Path(dirpath) / f
            if p.is_file() and not p.is_symlink():
                inv[p.relative_to(repo).as_posix()] = sha(p)
    return inv

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True); ap.add_argument("--candidates", required=True)
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    repo, cand = Path(a.repo).resolve(), Path(a.candidates)
    problems = []
    for rel, want in TARGETS.items():
        c = cand / rel
        if not c.is_file(): problems.append(f"candidate missing: {rel}")
        elif sha(c) != want: problems.append(f"candidate hash mismatch: {rel}")
        if (repo / rel).exists() or (repo / (rel + TMP_SUFFIX)).exists(): problems.append(f"target or temporary already exists: {rel}")
        if not (repo / rel).parent.is_dir(): problems.append(f"deliverable folder missing: {rel}")
    for rel, want in PINNED.items():
        f = repo / rel
        if not f.is_file(): problems.append(f"pinned file missing: {rel}")
        elif sha(f) != want: problems.append(f"pinned hash mismatch: {rel}")
    for msg in problems: print("FAIL " + msg)
    if problems:
        print("preflight failed; nothing written"); return 1
    before = inventory(repo)
    planned = set(TARGETS)
    if planned & set(before):
        print("FAIL planned write set overlaps existing files; nothing written"); return 1
    for rel in TARGETS: print(("RENDER " if a.check_only else "PLAN ") + rel)
    if a.check_only:
        print("CHECK write set = grant (2 creates, 0 modifies, 0 removes); nothing written"); return 0
    created, temps = [], []
    try:
        for rel in TARGETS:
            tmp = repo / (rel + TMP_SUFFIX)
            temps.append(tmp); tmp.write_bytes((cand / rel).read_bytes())
            if sha(tmp) != TARGETS[rel]: raise RuntimeError(f"temporary hash mismatch: {rel}")
        for rel in TARGETS:
            os.replace(repo / (rel + TMP_SUFFIX), repo / rel); created.append(repo / rel)
        temps = []
        after = inventory(repo)
        added = set(after) - set(before); removed = set(before) - set(after)
        modified = {k for k in set(after) & set(before) if after[k] != before[k]}
        if added != planned or removed or modified:
            raise RuntimeError(f"write set differs from grant: added={sorted(added - planned)} missing={sorted(planned - added)} removed={sorted(removed)} modified={sorted(modified)}")
        for rel, want in TARGETS.items():
            if after[rel] != want: raise RuntimeError(f"post-write hash mismatch: {rel}")
        for rel, want in PINNED.items():
            if after.get(rel) != want: raise RuntimeError(f"pinned file changed: {rel}")
    except Exception as e:
        for p in temps + created:
            try: p.unlink()
            except FileNotFoundError: pass
        print(f"FAIL {e}; every created target and temporary file removed"); return 1
    for rel in TARGETS: print("WRITE " + rel)
    print("CHECK targets 2/2 byte-exact; write set = grant (2 created, 0 modified, 0 removed under projects/pec); pinned 8/8 unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main())
