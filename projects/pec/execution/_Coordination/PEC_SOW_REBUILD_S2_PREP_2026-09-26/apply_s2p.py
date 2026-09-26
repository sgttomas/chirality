#!/usr/bin/env python3
"""S2 Scope of Work rebuild (provisional D-PEC-100) bound act: replace seven
existing ScopeOfWork.md files with the tabled candidate bytes, byte-exact.

Usage (from anywhere):
  apply_s2p.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

<DIR> holds the candidate files at their repository-relative paths.

Failure semantics:
- Preflight: every candidate hashes to its tabled postimage; every target
  exists and hashes to its tabled preimage; no temporary sibling exists; every
  pinned read-only file hashes as tabled. Any failure exits 1 before any byte
  is written. A second run fails here (the targets no longer hold their
  preimages).
- Write: each postimage is written to a temporary sibling, hash-checked, then
  renamed over its target. If any step after the first write fails (I/O error,
  hash mismatch, post-write inventory mismatch, changed pinned file), the
  script restores every replaced target from the preimage bytes it read at
  preflight (again through a temporary sibling), removes every temporary file,
  and exits 1. On exit 1 every target holds its preimage and no temporary
  file remains.
- Write-set check: the script inventories every file under projects/pec (path
  and SHA-256) before and after the write and requires the difference to be
  exactly the seven targets, each modified from preimage to postimage, with
  nothing created or removed.
It never touches _STATUS.md, MEMORY.md or any other file. Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

E = "projects/pec/execution/"
# target -> (preimage SHA-256, postimage SHA-256)
TARGETS = {
    # @@TARGETS@@
}
# Read-only files the act re-verifies (values at origin/main @@OBS@@).
PINNED = {
    # @@PINNED@@
}
TMP_SUFFIX = ".s2ptmp"

def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha(path): return sha_b(Path(path).read_bytes())

def inventory(repo):
    base = repo / "projects/pec"; inv = {}
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        for f in filenames:
            p = Path(dirpath) / f
            if p.is_file() and not p.is_symlink():
                inv[p.relative_to(repo).as_posix()] = sha(p)
    return inv

def put(repo, rel, data, want):
    tmp = repo / (rel + TMP_SUFFIX)
    tmp.write_bytes(data)
    if sha(tmp) != want:
        raise RuntimeError(f"temporary hash mismatch: {rel}")
    os.replace(tmp, repo / rel)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True); ap.add_argument("--candidates", required=True)
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    repo, cand = Path(a.repo).resolve(), Path(a.candidates)
    problems, pre_bytes, post_bytes = [], {}, {}
    for rel, (pre, post) in TARGETS.items():
        c = cand / rel
        if not c.is_file(): problems.append(f"candidate missing: {rel}")
        else:
            post_bytes[rel] = c.read_bytes()
            if sha_b(post_bytes[rel]) != post: problems.append(f"candidate hash mismatch: {rel}")
        t = repo / rel
        if not t.is_file(): problems.append(f"target missing: {rel}")
        else:
            pre_bytes[rel] = t.read_bytes()
            if sha_b(pre_bytes[rel]) != pre:
                problems.append(f"target does not hold its preimage (already applied or changed): {rel}")
        if (repo / (rel + TMP_SUFFIX)).exists(): problems.append(f"temporary already exists: {rel}")
    for rel, want in PINNED.items():
        f = repo / rel
        if not f.is_file(): problems.append(f"pinned file missing: {rel}")
        elif sha(f) != want: problems.append(f"pinned hash mismatch: {rel}")
    for msg in problems: print("FAIL " + msg)
    if problems:
        print("preflight failed; nothing written"); return 1
    before = inventory(repo)
    for rel in TARGETS: print(("RENDER " if a.check_only else "PLAN ") + rel)
    if a.check_only:
        print(f"CHECK write set = grant (0 creates, {len(TARGETS)} modifies, 0 removes); nothing written"); return 0
    replaced = []
    try:
        for rel, (pre, post) in TARGETS.items():
            put(repo, rel, post_bytes[rel], post); replaced.append(rel)
        after = inventory(repo)
        added = set(after) - set(before); removed = set(before) - set(after)
        modified = {k for k in set(after) & set(before) if after[k] != before[k]}
        if added or removed or modified != set(TARGETS):
            raise RuntimeError(f"write set differs from grant: added={sorted(added)} removed={sorted(removed)} "
                               f"unexpected={sorted(modified - set(TARGETS))} missing={sorted(set(TARGETS) - modified)}")
        for rel, (pre, post) in TARGETS.items():
            if after[rel] != post: raise RuntimeError(f"post-write hash mismatch: {rel}")
        for rel, want in PINNED.items():
            if after.get(rel) != want: raise RuntimeError(f"pinned file changed: {rel}")
    except Exception as e:
        errs = []
        for rel in TARGETS:
            try: (repo / (rel + TMP_SUFFIX)).unlink()
            except FileNotFoundError: pass
        for rel in replaced:
            try: put(repo, rel, pre_bytes[rel], TARGETS[rel][0])
            except Exception as e2: errs.append(f"{rel}: {e2}")
        for rel in TARGETS:
            try: (repo / (rel + TMP_SUFFIX)).unlink()
            except FileNotFoundError: pass
        if errs:
            print(f"FAIL {e}; ROLLBACK INCOMPLETE: {errs}"); return 2
        print(f"FAIL {e}; every replaced target restored to its preimage and every temporary file removed"); return 1
    for rel in TARGETS: print("WRITE " + rel)
    print(f"CHECK targets {len(TARGETS)}/{len(TARGETS)} byte-exact; write set = grant (0 created, {len(TARGETS)} modified, 0 removed under projects/pec); pinned {len(PINNED)}/{len(PINNED)} unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main())
