#!/usr/bin/env python3
"""X1 parser fixture suites (provisional D-PEC-106) bound act: create the tabled
new files under projects/pec/v2/tests/parsers/ and replace
projects/pec/software-workflow.json with its tabled postimage, byte-exact.

Usage (from anywhere):
  apply_x1p.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

<DIR> holds the candidate files at their repository-relative paths.

Failure semantics:
- Preflight: every candidate hashes to its tabled postimage; every modified
  target exists and holds its tabled preimage; every created target and the
  new directory projects/pec/v2/tests/parsers are absent; no temporary sibling
  exists; every pinned read-only file hashes as tabled. Any failure exits 1
  before any byte is written. A second run fails here (the targets no longer
  hold their preimages or absences).
- Write: each postimage is written to a temporary sibling, hash-checked, then
  renamed into place. If any step after the first write fails (I/O error,
  hash mismatch, post-write inventory mismatch, changed pinned file), the
  script removes every file it created, restores every replaced target from
  the preimage bytes it read at preflight, removes every directory it created
  and every temporary file, and exits 1. On exit 1 the tree under projects/pec
  is as it was before the run. Exit 2 reports an incomplete rollback.
- Write-set check: the script inventories every file under projects/pec (path
  and SHA-256) before and after the write and requires the difference to be
  exactly the tabled targets: the created files created with their
  postimages, the one modified file moved from preimage to postimage, and
  nothing else created, modified or removed. The script's own directory (the
  run root, where the act's evidence is written) is left out of the
  inventory. If the script sits inside projects/pec anywhere other than a run
  root (projects/pec/execution/_Coordination/X1_FIXTURES_*), preflight refuses.
It never touches _STATUS.md, MEMORY.md, a Scope of Work or any other file.
Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

# target -> (preimage SHA-256 or None when the file is created, postimage SHA-256)
TARGETS = {
    'projects/pec/software-workflow.json':
        ('8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b',
         'd55fff77a1d216a7b1ab78b16e3ff3f2747fb3b542a2b269367ec3afa83e0bbd'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/MANIFEST.json':
        (None,
         '0a07807081840f55c581c36264bec76b254d1c956574c0806a014140a423a5a9'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-1.json':
        (None,
         '3e93a8d7d4b6350a2268ec091d6796db1dcdf488d5025a2d18a6adb0d674d68e'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-2.json':
        (None,
         '19c9a6e8fc1b55efeefa7537cfc46ff508344b34d993a613aaf3812da4fe4770'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-3.json':
        (None,
         'a23725af786c9da96faf8c3b971b0ae0b4ed06c7ceb10132e6b93e81ac8efb25'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FX-PEC-0.json':
        (None,
         'ea38966446ce5b3eb4d4ff9f4841ac96fc7b9dfa5cfb98967ac724131c43a6b1'),
    'projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py':
        (None,
         '1ec0a7902c95907439d3579e2eed4308922b92ed1798cbc1eb2b42dc99d65bd3'),
}
# The one directory the act creates; it must be absent before the act.
NEW_DIR = "projects/pec/v2/tests/parsers"
# Read-only files the act re-verifies (values at the observation commit).
PINNED = {
    'projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md':
        '9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1',
    'projects/pec/execution/_Decomposition/Deliverables.csv':
        '94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805',
    'projects/pec/execution/_Decomposition/ScopeLedger.csv':
        '1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e',
    'projects/pec/docs/PRD.md':
        'ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe',
    'projects/pec/AGENTS.md':
        'df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8',
    'projects/pec/v2/config/loops.json':
        'fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7',
    'projects/pec/v2/config/loops.schema.json':
        '104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143',
    'projects/pec/v2/config/service_core_posture.json':
        '20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed',
    'projects/pec/v2/tools/check_service_core_posture.py':
        '03be20a5d54551d7c01e1ce2ef1c36c4f2435c1a66809116dd4555cef0588f89',
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md':
        'c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b',
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_STATUS.md':
        '6f94c04f79b678082b0407f93ec9c898d988c2693c0d1e19791f5cff985cf06f',
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md':
        '2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26',
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_STATUS.md':
        '4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe',
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md':
        'eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e',
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_STATUS.md':
        'e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056',
}
TMP_SUFFIX = ".x1ptmp"

def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha(path): return sha_b(Path(path).read_bytes())

SELF_DIR = Path(__file__).resolve().parent
RUN_ROOT_PREFIX = "projects/pec/execution/_Coordination/X1_FIXTURES_"

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
    if (repo / NEW_DIR).exists():
        problems.append(f"new directory already exists (already applied or changed): {NEW_DIR}")
    for rel, (pre, post) in TARGETS.items():
        c = cand / rel
        if not c.is_file(): problems.append(f"candidate missing: {rel}")
        else:
            post_bytes[rel] = c.read_bytes()
            if sha_b(post_bytes[rel]) != post: problems.append(f"candidate hash mismatch: {rel}")
        t = repo / rel
        if pre is None:
            if t.exists() or t.is_symlink(): problems.append(f"created target already exists: {rel}")
        elif not t.is_file(): problems.append(f"target missing: {rel}")
        else:
            pre_bytes[rel] = t.read_bytes()
            if sha_b(pre_bytes[rel]) != pre:
                problems.append(f"target does not hold its preimage (already applied or changed): {rel}")
        if (repo / (rel + TMP_SUFFIX)).exists(): problems.append(f"temporary already exists: {rel}")
    for rel, want in PINNED.items():
        f = repo / rel
        if not f.is_file(): problems.append(f"pinned file missing: {rel}")
        elif sha(f) != want: problems.append(f"pinned hash mismatch: {rel}")
    try:
        rel_self = SELF_DIR.relative_to(repo).as_posix()
    except ValueError:
        rel_self = None
    if rel_self is not None and rel_self.startswith("projects/pec/") and \
            not rel_self.startswith(RUN_ROOT_PREFIX):
        problems.append(f"script directory {rel_self} is inside projects/pec but is not a run root "
                        f"({RUN_ROOT_PREFIX}*); run the bound copy from its run root or from outside the repository")
    for msg in problems: print("FAIL " + msg)
    if problems:
        print("preflight failed; nothing written"); return 1
    creates = [r for r, (pre, _) in TARGETS.items() if pre is None]
    modifies = [r for r, (pre, _) in TARGETS.items() if pre is not None]
    for rel in TARGETS: print(("RENDER " if a.check_only else "PLAN ") + ("create " if rel in creates else "modify ") + rel)
    if a.check_only:
        print(f"CHECK preflight passed; planned write set {len(creates)} creates, {len(modifies)} modifies, 0 removes (the inventory check runs in apply mode); nothing written"); return 0
    before = inventory(repo)
    written, made_dirs = [], []
    try:
        for rel, (pre, post) in TARGETS.items():
            parent = (repo / rel).parent
            missing = []
            while not parent.exists():
                missing.append(parent); parent = parent.parent
            for d in reversed(missing):
                d.mkdir(); made_dirs.append(d)
            put(repo, rel, post_bytes[rel], post); written.append(rel)
        after = inventory(repo)
        added = set(after) - set(before); removed = set(before) - set(after)
        modified = {k for k in set(after) & set(before) if after[k] != before[k]}
        if added != set(creates) or removed or modified != set(modifies):
            raise RuntimeError(f"write set differs from grant: unexpected_added={sorted(added - set(creates))} "
                               f"missing_added={sorted(set(creates) - added)} removed={sorted(removed)} "
                               f"unexpected_modified={sorted(modified - set(modifies))} missing_modified={sorted(set(modifies) - modified)}")
        for rel, (pre, post) in TARGETS.items():
            if after[rel] != post: raise RuntimeError(f"post-write hash mismatch: {rel}")
        for rel, want in PINNED.items():
            if after.get(rel) != want: raise RuntimeError(f"pinned file changed: {rel}")
    except Exception as e:
        errs = []
        for rel in TARGETS:
            try: (repo / (rel + TMP_SUFFIX)).unlink()
            except FileNotFoundError: pass
            except Exception as e2: errs.append(f"{rel}{TMP_SUFFIX}: {e2}")
        for rel in written:
            try:
                if TARGETS[rel][0] is None: (repo / rel).unlink()
                else: put(repo, rel, pre_bytes[rel], TARGETS[rel][0])
            except Exception as e2: errs.append(f"{rel}: {e2}")
        for rel in TARGETS:
            try: (repo / (rel + TMP_SUFFIX)).unlink()
            except FileNotFoundError: pass
        for d in reversed(made_dirs):
            try: d.rmdir()
            except FileNotFoundError: pass
            except Exception as e2: errs.append(f"{d}: {e2}")
        if errs:
            print(f"FAIL {e}; ROLLBACK INCOMPLETE: {errs}"); return 2
        print(f"FAIL {e}; every created file and directory removed, every replaced target restored to its preimage, no temporary file left"); return 1
    for rel in TARGETS: print(("WRITE create " if rel in creates else "WRITE modify ") + rel)
    print(f"CHECK targets {len(TARGETS)}/{len(TARGETS)} byte-exact; write set = grant ({len(creates)} created, {len(modifies)} modified, 0 removed under projects/pec outside the run root); pinned {len(PINNED)}/{len(PINNED)} unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main())
