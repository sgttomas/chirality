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
         '8379b7d6bf650c7e3864449edb691e79fafd6966ce2f789c07c866cdcdcc4922'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-2.json':
        (None,
         '1af4cfa4520da4fbaaf7c57924da3f733611b915c3f0dac36a3f88a7b300d860'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FC-3.json':
        (None,
         'a02fc9722fedd1545215f9999be05eb4593417c649f304915d29bd6f403c39f7'),
    'projects/pec/v2/tests/parsers/fixtures/pinned/goldens/FX-PEC-0.json':
        (None,
         '4adf49757bfe6e71cd07d3397fe6260acee184efabdc294b83442c4b0b1e7b5a'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/MANIFEST.json':
        (None,
         '60b467d4a414db60fd55ef563464fcc12a3f54e74a9a5ea11560d30d846a0c8f'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/entry_without_readable_run_token.md':
        (None,
         '38243567f072606fe5214a0e86223a32bf6c62bbe7de7a3205e2a10f7c4313cc'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/file_without_run_index_entry.md':
        (None,
         '21891babb92e21a16637b7851a1ec1ce91e9145974baf8903788f5b0553fbf41'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/links_in_each_form_bullet.md':
        (None,
         '29972401929b3e3bd0c83691cb001be5f7b50dbb720e49627e5cec9aaaaa39cc'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/links_in_each_form_heading.md':
        (None,
         'd98b0e6baa3deaa330ffec5731224b083c58a0bc8fd2c43b11b007e8f5f5c0f4'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/links_in_each_form_table.md':
        (None,
         'f0b7561f1d92ba20b56edfdaedc006714b1bac92b1e14c100d61ba479de8ce29'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/prose_in_every_position_bullet.md':
        (None,
         '02843c9a1769a221dda1c4900905cacf7be7948bd3480b218dde3af497df6547'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/prose_in_every_position_heading.md':
        (None,
         '456d3d87c7adbb8efba45ecc9c6bf8381cdc39081300073e658862e261830748'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/prose_in_every_position_table.md':
        (None,
         'f436fd3263efb1bf27029c0942cc1e8038d21bb665349d1b1cc9f8ffd32ef1c7'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/runs_section_mixed_with_dated_sections.md':
        (None,
         '20d7ffb89b8fe47a7b03d017aaf60c4aa3148dac1793496638548c3c424f77a9'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/template_table_form.md':
        (None,
         '4bdf79945eff6308fda4a7f0f1c3ac603181e2d8d1e49964c8b404d62e77067f'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/memory/unreadable_date.md':
        (None,
         'd5b0ff8be0a05f75ebbd450a5ea2ae0a9583fd3a630c756bb1670ff145ecea63'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/receipts/malformed_ledger.md':
        (None,
         '44dd411d61dac4e192c192d96aabf2681b982ae42682884bbbcbc8127ed7cbd7'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/receipts/marker_carrying_ledger_entry.md':
        (None,
         'aa74d4e35883dc02dcb1162700258974da1c796cb5c8fa4f10386c5e390c27b1'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/receipts/prose_in_every_position_central.md':
        (None,
         '8a91d677f951bdb2621f1242114fd7acc74e747820890111fd2455bfe3bd0045'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/receipts/prose_in_every_position_ledger.md':
        (None,
         '9acf2a98c38c1758e2df28ef8a89ce67268403c9b235216cedbbd5e0c939c782'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/receipts/prose_structured_ledger_entry.md':
        (None,
         '66df3795f7aa49a292f57095ba5720c4247ded553492ce0925784325ae4d0e90'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/receipts/receipt_folder_diverges_from_cursor.md':
        (None,
         'b5582c4d7c3963eb45432f6c95d5584ba9627c8d1f401ed87f7f50b5b2256fdc'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/receipts/receipt_without_examined_through.md':
        (None,
         '8ab389eebe7a35448098afde63834d96847b27d6b8f972a70e8e60226da5f072'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/duplicated_run_identity.md':
        (None,
         'cb0f16cbd96e15d9973eefb2db75c394fa2ad77926f0310296d77caace398e8f'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/links_and_bindings.md':
        (None,
         'e06d4323510ed2eb2c604908a766745056f11a451bdf46c5bcefeb87dec9fb1d'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/missing_run_identity.md':
        (None,
         '1394b4b435ce33c43b5e6280d5098d1170af9d5db805946df62334c7166a1a1e'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/no_node_table.md':
        (None,
         '3192a26bffaff4bc62035f72be52b6ad08eb47eada25f4ad4891d7cd11d6674d'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/prose_in_every_position.md':
        (None,
         '1752d8e889a32ff5123b63e6231f8cfd71bb896d4bd96bfe97cc5177d410a166'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/two_graphs_bind_one_deliverable_a.md':
        (None,
         '2517e96eeaa4311370af7cabf4f7d7c9df0e6460e7fbde5581c5c1830fe28462'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/two_graphs_bind_one_deliverable_b.md':
        (None,
         'f8492a641361b7e6183ce76dcbaf18b70d1369cc5bd89e98607cfb2a3e64853c'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/unrecognized_state_token.md':
        (None,
         'a6142d24708ecddcd2b74c20e2b2ba8f685e339e480c5ed83db4edf13be0e376'),
    'projects/pec/v2/tests/parsers/fixtures/synthetic/work_graph/unresolved_pr_number.md':
        (None,
         '03bf235275cad181cdfc131a63c439896658b5651871831c59c4ade00f65075f'),
    'projects/pec/v2/tests/parsers/test_parser_fixture_integrity.py':
        (None,
         '70fc24b49aa6681ccbd6c03fbed37149b854a85be373ce23043812d9d5103203'),
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
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md':
        '2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26',
    'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md':
        'eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e',
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
