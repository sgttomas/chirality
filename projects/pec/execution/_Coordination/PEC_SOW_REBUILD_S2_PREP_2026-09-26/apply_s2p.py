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
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md":
        ("43f1f57a13bb96b3235bbbb460342bd03518c503f23cb8b0560914f27a2f0170",
         "14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88"),
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md":
        ("5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8",
         "2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e"),
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md":
        ("c3e7928cbbcf1c552883f8268bff4899996f9943cc8fb1b52ca14c223bd7d872",
         "c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b"),
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/ScopeOfWork.md":
        ("bdb4eea0143ef6c777b0ed5914e7a8846d818437f77ec96cea03d8557f3bcb87",
         "18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1"),
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md":
        ("192df47d8d3d15316951066a24032b9a7d7a6cd0b660935fcb1799daf8af907e",
         "0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92"),
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/ScopeOfWork.md":
        ("c8ca6292bae19d2da754918bdf530d32a4c0a8348146ed10743acfd0acfbbec8",
         "53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928"),
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md":
        ("d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559",
         "a07d5f17305598731e98d853f71361d0f8a1def3597d5b25c48eb25f03ff9079"),
}
# Read-only files the act re-verifies (values at origin/main c76434101; unchanged since aca930622).
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
    "projects/pec/v2/config/loops.json":
        "fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7",
    "projects/pec/v2/config/loops.schema.json":
        "104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143",
    "projects/pec/AGENTS.md":
        "df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8",
    E + "_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md":
        "69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_STATUS.md":
        "26ec3a6e3d4b557cff30ff5a18014c5c9f2eef4da23bf0c25f19cf87b01af83d",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_STATUS.md":
        "20e6db0216943cf93d734cf97a18c50ece47706e6a012e47580aea9745e5e90d",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_STATUS.md":
        "6f94c04f79b678082b0407f93ec9c898d988c2693c0d1e19791f5cff985cf06f",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_STATUS.md":
        "2ac8fd42d7c72f85fbf65daea10b6935c4a84dd1629756a55988476fc05d86a9",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_STATUS.md":
        "5feb5e170d196146a3a83fff4e1558468e85ea83ee7b35faba6e106ac6f589bb",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_STATUS.md":
        "a20147a10b21b709e6f31e0178b53921d58109447f8d607f3afe2e35b27ed055",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_STATUS.md":
        "653daef4a2eb08b74866d405534b41e0031c7c3590ac8f39be5f7a42c584060a",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/Dependencies.csv":
        "e736ce9a34f31b88c19c007371a87ddafbfc32544beeb0fc1a08dae8aca61a6d",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/Dependencies.csv":
        "51c7b725b91d7659496964f08b2d2d4934bd158c3fadc65be42dbf110436dfa1",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/Dependencies.csv":
        "c456c77f0203c24a1a4aae04fd286610a4391666cbd285548854079f731c1643",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/Dependencies.csv":
        "563b4c281ded7a410cf7587b71fc562f321b254e317ced29f42a6d306dd3e701",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/Dependencies.csv":
        "90f555eb870ed47e693456e6768060307bb93c2f48bfadf9344a22b6111618b1",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/Dependencies.csv":
        "8a88f50b462c9dc0614c6cac08f00fc3e6fa977e994b3ab1e56c3478a4cbc335",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/Dependencies.csv":
        "00b5a872ca0a62c9246591d513af11637e3e15dc764824fd28b7d8219f3c3ee3",
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
