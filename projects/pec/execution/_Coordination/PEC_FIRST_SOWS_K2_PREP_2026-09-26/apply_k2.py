#!/usr/bin/env python3
"""K2 first Scope of Work contracts (provisional D-PEC-103) bound act, option A:
create the two first ScopeOfWork.md files for DEL-08-06 and DEL-10-13, byte-exact.

Usage (from anywhere):
  apply_k2.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

<DIR> holds the candidate files at their repository-relative paths.

Failure semantics:
- Preflight: every candidate hashes to its tabled postimage; every target and
  its temporary sibling is absent and its deliverable folder present; every
  pinned read-only file hashes as tabled; and, if this script's directory lies
  below projects/pec/, it must lie below a run root
  (projects/pec/execution/_Coordination/SOW_INIT_K2_*). Any failure exits 1
  before any byte is written. A second run fails here (the targets exist).
- Write: each postimage is written to a temporary sibling, hash-checked, then
  renamed into place. If any step after the first write fails (I/O error, hash
  mismatch, post-write inventory mismatch, changed pinned file), the script
  removes every temporary file and every target it created, and exits 1. On
  exit 1 no target file and no temporary file remains; exit 2 reports an
  incomplete clean-up.
- Write-set check: the script inventories every file under projects/pec (path
  and SHA-256) before and after the write, leaving out only its own directory
  (the run root, where the act's evidence is written while it runs), and
  requires the difference to be exactly the two targets, both created, with
  nothing modified or removed.
It never touches _STATUS.md, MEMORY.md, _DEPENDENCIES.md or any other existing
file. Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

E = "projects/pec/execution/"
D86 = E + "PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/"
D13 = E + "PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/"
# target -> postimage SHA-256 (preimage: absent)
TARGETS = {
    D86 + "ScopeOfWork.md": "aecc513161c1e8a5a984dc2f7878b79783170adc1042fb91e816dc649ef50826",
    D13 + "ScopeOfWork.md": "c7743ee2ab7d795577d08c57d748fa704d3cc58ad55df7eea77bc95fb1b56633",
}
# Read-only files the act re-verifies (values at origin/main 125cfacc1; the first
# five equal at the pin 189f205ff).
PINNED = {
    E + "_Decomposition/SOFTWARE_DECOMP.md": "9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1",
    E + "_Decomposition/Deliverables.csv": "94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805",
    E + "_Decomposition/ScopeLedger.csv": "1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e",
    E + "_Decomposition/ContextBudgetQA.csv": "93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c",
    "projects/pec/docs/PRD.md": "ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe",
    "projects/pec/AGENTS.md": "df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8",
    "_DomainEngines/profiles/pec.yaml": "6858d567ee27bae9b832115a40a41b106a9a2a58a62d661ca0e0c2acff9b314f",
    D86 + "_STATUS.md": "73e21846186b3ab46d4d11042ecb2bb00d0c69a0d7b4fa70734c75e65a892511",
    D86 + "Dependencies.csv": "10d7b0d8ec9939179797082e3a78aa895c2bd52fd1fce8e3d8e2521486eb5050",
    D86 + "_CONTEXT.md": "900748777076fd0ecd16b6e2f95b0105ef590890aace871cb44196d0390136cc",
    D86 + "_REFERENCES.md": "9f19e3a66ada49a396f1b8e1f386a6b3946793b5d1dd9115fe7cc1e630e0987e",
    D86 + "_DEPENDENCIES.md": "6aa230b1cf03a15791b730e4d20a62047053c83df19531feef162fbcbc9f01fd",
    D13 + "_STATUS.md": "c7a5705d7203a26f525317e85fa068d29cfeb49b8686eab1b5cd3e782e22543b",
    D13 + "Dependencies.csv": "334b9edcf1af9334ccae91136cc88e6b4cdc2abf075a3db1a1d5b2c50e7a6e7a",
    D13 + "_CONTEXT.md": "5efdf4a1f0199f50c542a2b3cedcab1229b9331f5a2d5cdc120b325eca588035",
    D13 + "_REFERENCES.md": "c0070adad3a46d2a8b4f70c907829d3fd74589c9782270f2cbab995be2131656",
    D13 + "_DEPENDENCIES.md": "5087e581b00557cac9c245c543d0a690ed2a9fc992a96d8e60769f8a44baeb63",
}
TMP_SUFFIX = ".k2tmp"
SELF_DIR = Path(__file__).resolve().parent
RUN_ROOT_PREFIX = "projects/pec/execution/_Coordination/SOW_INIT_K2_"

def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha(path): return sha_b(Path(path).read_bytes())

def inventory(repo):
    """Every file under projects/pec, except this script's own directory and caches."""
    base = repo / "projects/pec"; inv = {}
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")
                       and (Path(dirpath) / d).resolve() != SELF_DIR]
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
    problems, post_bytes = [], {}
    for rel, want in TARGETS.items():
        c = cand / rel
        if not c.is_file(): problems.append(f"candidate missing: {rel}")
        else:
            post_bytes[rel] = c.read_bytes()
            if sha_b(post_bytes[rel]) != want: problems.append(f"candidate hash mismatch: {rel}")
        if (repo / rel).exists() or (repo / (rel + TMP_SUFFIX)).exists():
            problems.append(f"target or temporary already exists: {rel}")
        if not (repo / rel).parent.is_dir(): problems.append(f"deliverable folder missing: {rel}")
    for rel, want in PINNED.items():
        f = repo / rel
        if not f.is_file(): problems.append(f"pinned file missing: {rel}")
        elif sha(f) != want: problems.append(f"pinned hash mismatch: {rel}")
    try:
        rel_self = SELF_DIR.relative_to(repo).as_posix()
    except ValueError:
        rel_self = None  # the script runs from outside the repository: nothing is excluded
    if rel_self is not None and (rel_self + "/").startswith("projects/pec/") and \
            not rel_self.startswith(RUN_ROOT_PREFIX):
        problems.append(f"script directory {rel_self} lies below projects/pec but not below a run root "
                        f"({RUN_ROOT_PREFIX}*); run the bound copy from its run root or from outside the repository")
    for msg in problems: print("FAIL " + msg)
    if problems:
        print("preflight failed; nothing written"); return 1
    before = inventory(repo)
    planned = set(TARGETS)
    for rel in TARGETS: print(("RENDER " if a.check_only else "PLAN ") + rel)
    if a.check_only:
        print(f"CHECK preflight passed; planned write set {len(TARGETS)} creates, 0 modifies, 0 removes (the inventory check runs in apply mode); nothing written"); return 0
    created = []
    try:
        for rel in TARGETS:
            tmp = repo / (rel + TMP_SUFFIX)
            tmp.write_bytes(post_bytes[rel])
            if sha(tmp) != TARGETS[rel]: raise RuntimeError(f"temporary hash mismatch: {rel}")
            os.replace(tmp, repo / rel); created.append(repo / rel)
        after = inventory(repo)
        added = set(after) - set(before); removed = set(before) - set(after)
        modified = {k for k in set(after) & set(before) if after[k] != before[k]}
        if added != planned or removed or modified:
            raise RuntimeError(f"write set differs from grant: added={sorted(added - planned)} missing={sorted(planned - added)} "
                               f"removed={sorted(removed)} modified={sorted(modified)}")
        for rel, want in TARGETS.items():
            if after[rel] != want: raise RuntimeError(f"post-write hash mismatch: {rel}")
        for rel, want in PINNED.items():
            f = repo / rel
            if not f.is_file() or sha(f) != want: raise RuntimeError(f"pinned file changed: {rel}")
    except Exception as e:
        errs = []
        for p in [repo / (r + TMP_SUFFIX) for r in TARGETS] + created:
            try: p.unlink()
            except FileNotFoundError: pass
            except Exception as e2: errs.append(f"{p}: {e2}")
        if errs:
            print(f"FAIL {e}; CLEAN-UP INCOMPLETE: {errs}"); return 2
        print(f"FAIL {e}; every created target and temporary file removed"); return 1
    for rel in TARGETS: print("WRITE " + rel)
    print(f"CHECK targets {len(TARGETS)}/{len(TARGETS)} byte-exact; write set = grant ({len(TARGETS)} created, 0 modified, 0 removed under projects/pec outside the run root); pinned {len(PINNED)}/{len(PINNED)} unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main())
