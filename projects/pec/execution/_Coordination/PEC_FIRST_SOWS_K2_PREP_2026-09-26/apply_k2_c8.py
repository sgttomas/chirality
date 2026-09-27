#!/usr/bin/env python3
"""K2 (provisional D-PEC-103) bound act for add-on C8 only: record the owner's
constraint C-08 standing-node classification of DEL-10-13 by replacing its
_DEPENDENCIES.md with the tabled postimage, byte-exact (one added line in the
human-owned "Dependency Tracking Mode" section). Run only if the ruling selects
C8, and only after option A's act (apply_k2.py) has passed.

Usage (from anywhere):
  apply_k2_c8.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

<DIR> holds the postimage at its repository-relative path.

Failure semantics:
- Preflight: the candidate hashes to its postimage; the target holds its
  preimage; no temporary sibling exists; the DEL-10-13 contract exists with its
  option-A postimage hash; every pinned file hashes as tabled; and, if this
  script's directory lies below projects/pec/, it must lie below a run root
  (projects/pec/execution/_Coordination/SOW_INIT_K2_*). Any failure exits 1
  before any byte is written. A second run fails here.
- Write: temporary sibling, hash check, rename. If a later step fails, the
  target is restored from the preimage bytes read at preflight and every
  temporary file is removed (exit 1); exit 2 reports an incomplete rollback.
- Write-set check: inventory of projects/pec (except this script's directory)
  before and after; the difference must be exactly the one target, modified.
Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

E = "projects/pec/execution/"
D13 = E + "PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/"
TARGET = D13 + "_DEPENDENCIES.md"
PRE = "5087e581b00557cac9c245c543d0a690ed2a9fc992a96d8e60769f8a44baeb63"
POST = "609aa807710feef11bf8506324cb2a79996f3d6ce5a6eb623ec9516e3ac65693"
# _STATUS.md is deliberately not pinned: add-on S, if selected, may already have run.
PINNED = {
    D13 + "ScopeOfWork.md": "@@DEL-10-13@@",  # option A's postimage: C8 runs after A
    D13 + "Dependencies.csv": "334b9edcf1af9334ccae91136cc88e6b4cdc2abf075a3db1a1d5b2c50e7a6e7a",
    E + "_Decomposition/Deliverables.csv": "94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805",
}
TMP_SUFFIX = ".k2c8tmp"
SELF_DIR = Path(__file__).resolve().parent
RUN_ROOT_PREFIX = "projects/pec/execution/_Coordination/SOW_INIT_K2_"

def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha(p): return sha_b(Path(p).read_bytes())

def inventory(repo):
    base = repo / "projects/pec"; inv = {}
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")
                       and (Path(dirpath) / d).resolve() != SELF_DIR]
        for f in filenames:
            p = Path(dirpath) / f
            if p.is_file() and not p.is_symlink():
                inv[p.relative_to(repo).as_posix()] = sha(p)
    return inv

def put(repo, data, want):
    tmp = repo / (TARGET + TMP_SUFFIX)
    tmp.write_bytes(data)
    if sha(tmp) != want: raise RuntimeError("temporary hash mismatch")
    os.replace(tmp, repo / TARGET)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True); ap.add_argument("--candidates", required=True)
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    repo, cand = Path(a.repo).resolve(), Path(a.candidates)
    problems = []
    c = cand / TARGET
    post_bytes = c.read_bytes() if c.is_file() else None
    if post_bytes is None: problems.append(f"candidate missing: {TARGET}")
    elif sha_b(post_bytes) != POST: problems.append(f"candidate hash mismatch: {TARGET}")
    t = repo / TARGET
    pre_bytes = t.read_bytes() if t.is_file() else None
    if pre_bytes is None: problems.append(f"target missing: {TARGET}")
    elif sha_b(pre_bytes) != PRE: problems.append(f"target does not hold its preimage (already applied or changed): {TARGET}")
    if (repo / (TARGET + TMP_SUFFIX)).exists(): problems.append("temporary already exists")
    for rel, want in PINNED.items():
        f = repo / rel
        if not f.is_file(): problems.append(f"pinned file missing: {rel}")
        elif sha(f) != want: problems.append(f"pinned hash mismatch: {rel}")
    try:
        rel_self = SELF_DIR.relative_to(repo).as_posix()
    except ValueError:
        rel_self = None
    if rel_self is not None and (rel_self + "/").startswith("projects/pec/") and \
            not rel_self.startswith(RUN_ROOT_PREFIX):
        problems.append(f"script directory {rel_self} lies below projects/pec but not below a run root ({RUN_ROOT_PREFIX}*)")
    for m in problems: print("FAIL " + m)
    if problems:
        print("preflight failed; nothing written"); return 1
    before = inventory(repo)
    print(("RENDER " if a.check_only else "PLAN ") + TARGET)
    if a.check_only:
        print("CHECK preflight passed; planned write set 1 modify, 0 creates, 0 removes; nothing written"); return 0
    replaced = False
    try:
        put(repo, post_bytes, POST); replaced = True
        after = inventory(repo)
        added = set(after) - set(before); removed = set(before) - set(after)
        modified = {k for k in set(after) & set(before) if after[k] != before[k]}
        if added or removed or modified != {TARGET}:
            raise RuntimeError(f"write set differs from grant: added={sorted(added)} removed={sorted(removed)} modified={sorted(modified)}")
        if after[TARGET] != POST: raise RuntimeError("post-write hash mismatch")
        for rel, want in PINNED.items():
            if sha(repo / rel) != want: raise RuntimeError(f"pinned file changed: {rel}")
    except Exception as e:
        err = None
        try: (repo / (TARGET + TMP_SUFFIX)).unlink()
        except FileNotFoundError: pass
        if replaced:
            try: put(repo, pre_bytes, PRE)
            except Exception as e2: err = e2
        try: (repo / (TARGET + TMP_SUFFIX)).unlink()
        except FileNotFoundError: pass
        if err:
            print(f"FAIL {e}; ROLLBACK INCOMPLETE: {err}"); return 2
        print(f"FAIL {e}; target restored to its preimage and every temporary file removed"); return 1
    print("WRITE " + TARGET)
    print(f"CHECK target byte-exact; write set = grant (0 created, 1 modified, 0 removed under projects/pec outside the run root); pinned {len(PINNED)}/{len(PINNED)} unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main())
