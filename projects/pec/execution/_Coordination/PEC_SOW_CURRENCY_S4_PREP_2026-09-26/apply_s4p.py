#!/usr/bin/env python3
"""S4 Scope of Work currency (provisional D-PEC-102) bound act: replace eight
existing ScopeOfWork.md files with the tabled candidate bytes, byte-exact.

Usage (from anywhere):
  apply_s4p.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

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
  exactly the eight targets, each modified from preimage to postimage, with
  nothing created or removed. The script's own directory (the run root, where
  the act's evidence is written) is left out of the inventory, so recording
  output there during the run cannot trip the check. If the script's directory
  path begins with projects/pec/ but not with the run-root prefix
  projects/pec/execution/_Coordination/SOW_CURRENCY_S4_, preflight refuses; a
  placement the guard does not refuse still fails closed at the inventory.
It never touches _STATUS.md, MEMORY.md or any other file. Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

E = "projects/pec/execution/"
# target -> (preimage SHA-256, postimage SHA-256)
TARGETS = {
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md":
        ("6f4e8c66a5712ba73e5000f1eafbfd5dd821bb4c339a23d77aa46b5b558830ae",
         "13fa50fead2bba13ec4c7d8dba8a1e8cac0a95e60a29725205b5e11e823b7ee8"),
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md":
        ("a2b50f870aa30fb45e06b1f4cf1b300ff522a19490066c1e2d898b9022c0e65a",
         "8445deaeb4546f1a05101ea955faa574dcd1ed53c120028bc73cde8712efb19d"),
    E + "PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md":
        ("8ac1dc050efbd22530700d140a57944d0f82f48bcb2f9994bee4cddd588a3d76",
         "310dbb20e393a2aca47601f0dce413d3acbbd3eb532ea0ad47831b57d58b398c"),
    E + "PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md":
        ("013c615a0c91d7d2545d7dfc0faecfe509b0c7409f450fdefd01125d2aef3138",
         "2031526ef7e3000882d3731afa6de13e97ad1704e61cc17ff9ef5bd51ae9be23"),
    E + "PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md":
        ("6d1ec1ad9796973656d6d0d60739b4dbf8cd134a2b17c8c878ee2ff4c098222b",
         "35af0e22fe6254fb9ebae2a34e12e1e0ecf78ad451155cec07fdc1002d36600e"),
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md":
        ("6ec7432bf8cfe86cc973c50b8c2a24a0305c55c7a64522d0c47778050e59ec6d",
         "bce89565795b809c3a9255f210900ef198f2007af294e56a8d0c13e62c62750f"),
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/ScopeOfWork.md":
        ("e007f5307fce88fd7e31957bb4676f35d83bc971de3e0278e3dae906bd8e4e02",
         "5f7bd434694c8a87bba512ba74a8b8f2dee4f5e2a0ab10e5a50c234e432b196f"),
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md":
        ("cbcabbde6882baf5330e90cdd6e1cf4a9d9aa1da076643a27f84ff4cb7696ff8",
         "a9319e289a3381be4dc5fe1aacc3f7397550e12edcbdf1c5fdaa1011b171ef26"),
}
# Read-only files the act re-verifies (values at origin/main 125cfacc1).
PINNED = {
    E + "_Decomposition/SOFTWARE_DECOMP.md":
        "9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1",
    E + "_Decomposition/Deliverables.csv":
        "94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805",
    E + "_Decomposition/ScopeLedger.csv":
        "1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e",
    E + "_Decomposition/ContextBudgetQA.csv":
        "93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c",
    "projects/pec/docs/PRD.md":
        "ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe",
    "projects/pec/AGENTS.md":
        "df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8",
    E + "_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md":
        "69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_STATUS.md":
        "41510909e60227808ff0e4b597603dea2eb8f28703cf2359b0b6058afe94ac31",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_STATUS.md":
        "d876ae1a5ce679209baa0cf19b82e86f66d83d1f5608550b2a9d2faa60f2abad",
    E + "PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_STATUS.md":
        "ac61a8db734b2767627d412cab419bf801b7382e0ba840b88e546445b8b4262d",
    E + "PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_STATUS.md":
        "88cf8d11cbfc39375ce929f83b2a1080e3b322e7edc34d1f58ab6ed2fbe5f2ec",
    E + "PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_STATUS.md":
        "fc3c58ad3ac877cdcef616aae75b31f26878c8f93b8ae319fbd520a4e0d33054",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_STATUS.md":
        "c8a82497502085ba69b65dae496e8bfedaeff4d7129c35502416952718d4af34",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_STATUS.md":
        "ec35873b5b95a4e1f6dee31f9abd34b2f9ddf5403b0c85b8ce0e1a6014f2573a",
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_STATUS.md":
        "ab9646cb68e4226a4d39e737a4a23c8ca28d563d9045c12c3cb5c88fd3f8e1fb",
    E + "PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/Dependencies.csv":
        "4438197af5d66b5ebb642222547d9e9d2b40ffe7294cac7e52342badc99dc76d",
    E + "PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/Dependencies.csv":
        "1eb7eccf2f5390e7280711ae3cf56b71256787407ac8b56fb71c97a049a081d9",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/Dependencies.csv":
        "1ad180b4a85c0187458630da636c328344a841492a1c04750e675b7a1a96ae8d",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/Dependencies.csv":
        "0d479ce3a539844a5387edc8c680b83c704b77ff1e1b6ae11c6c4c2984023518",
}
TMP_SUFFIX = ".s4ptmp"

def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha(path): return sha_b(Path(path).read_bytes())

SELF_DIR = Path(__file__).resolve().parent  # the run root when the script runs from it
RUN_ROOT_PREFIX = "projects/pec/execution/_Coordination/SOW_CURRENCY_S4_"  # the only in-tree home it accepts

def inventory(repo):
    """Every file under projects/pec, except this script's own directory (the run
    root, where the act's evidence is written while it runs) and caches."""
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
    try:
        rel_self = SELF_DIR.relative_to(repo).as_posix()
    except ValueError:
        rel_self = None  # the script runs from outside the repository: nothing is excluded
    if rel_self is not None and rel_self.startswith("projects/pec/") and \
            not rel_self.startswith(RUN_ROOT_PREFIX):
        problems.append(f"script directory {rel_self} is inside projects/pec but is not a run root "
                        f"({RUN_ROOT_PREFIX}*); run the bound copy from its run root or from outside the repository")
    for msg in problems: print("FAIL " + msg)
    if problems:
        print("preflight failed; nothing written"); return 1
    before = inventory(repo)
    for rel in TARGETS: print(("RENDER " if a.check_only else "PLAN ") + rel)
    if a.check_only:
        print(f"CHECK preflight passed; planned write set {len(TARGETS)} modifies, 0 creates, 0 removes (not yet inventoried; the inventory check runs in apply mode); nothing written"); return 0
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
    print(f"CHECK targets {len(TARGETS)}/{len(TARGETS)} byte-exact; write set = grant (0 created, {len(TARGETS)} modified, 0 removed under projects/pec outside the run root); pinned {len(PINNED)}/{len(PINNED)} unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main())
