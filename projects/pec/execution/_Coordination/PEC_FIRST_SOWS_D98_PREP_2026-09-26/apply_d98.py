#!/usr/bin/env python3
"""D-PEC-98 bound act: create the two first ScopeOfWork.md files, byte-exact.

Usage (from anywhere):
  apply_d98.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

<DIR> holds the candidate files at their repository-relative paths
(projects/pec/execution/PKG-02_.../ScopeOfWork.md). Before any write it checks:
the pinned candidate hashes; that both targets are absent; the pinned basis and
preserved-file hashes; and that the write set equals the grant. It writes
nothing on any failure (exit 1) and fails if run a second time. Stdlib only.
It never touches _STATUS.md or any other file.
"""
import argparse, hashlib, sys
from pathlib import Path

P = "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/"
TARGETS = {
    P + "DEL-02-08_Work_graph_parser/ScopeOfWork.md":
        "b28cf13d93851dc875575dafd759171205a75bc4bb63ef67e103fa2094d10b24",
    P + "DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md":
        "c9705ca28da82687e82bccdeb1bca5e271833d267c4afe23526965c4e13c7bd9",
}
# Read-only basis and files the act must leave byte-identical (values at 7a00a88df).
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

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    repo, cand = Path(a.repo), Path(a.candidates)
    problems = []
    for rel, want in TARGETS.items():
        c = cand / rel
        if not c.is_file(): problems.append(f"candidate missing: {rel}")
        elif sha(c) != want: problems.append(f"candidate hash mismatch: {rel}")
        if (repo / rel).exists(): problems.append(f"target already exists: {rel}")
        if not (repo / rel).parent.is_dir(): problems.append(f"deliverable folder missing: {rel}")
    for rel, want in PINNED.items():
        f = repo / rel
        if not f.is_file(): problems.append(f"pinned file missing: {rel}")
        elif sha(f) != want: problems.append(f"pinned hash mismatch: {rel}")
    for msg in problems: print("FAIL " + msg)
    if problems:
        print("nothing written"); return 1
    for rel in TARGETS: print(("RENDER " if a.check_only else "WRITE ") + rel)
    if a.check_only: return 0
    for rel in TARGETS:
        (repo / rel).write_bytes((cand / rel).read_bytes())
    post = [rel for rel, want in TARGETS.items() if sha(repo / rel) != want]
    post += [rel for rel, want in PINNED.items() if sha(repo / rel) != want]
    if post:
        print("FAIL post-write hash check: " + ", ".join(post)); return 1
    print("CHECK targets 2/2 byte-exact; pinned 8/8 unchanged"); return 0

if __name__ == "__main__":
    sys.exit(main())
