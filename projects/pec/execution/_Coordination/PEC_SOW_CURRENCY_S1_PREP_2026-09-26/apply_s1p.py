#!/usr/bin/env python3
"""S1 Scope of Work currency (provisional D-PEC-104) bound act: replace twelve
existing ScopeOfWork.md files with the tabled candidate bytes, byte-exact.
(Pattern of the D-PEC-100 act script apply_s2p.py; S1 targets and pins.)

Usage (from anywhere):
  apply_s1p.py --repo <REPO_ROOT> --candidates <DIR> [--check-only]

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
  exactly the twelve targets, each modified from preimage to postimage, with
  nothing created or removed. The script's own directory (the run root, where
  the act's evidence is written) is left out of the inventory, so recording
  output there during the run cannot trip the check. If the script sits inside
  projects/pec anywhere other than a run root (projects/pec/execution/
  _Coordination/SOW_CURRENCY_S1_*), preflight refuses, so the exclusion can
  never cover another directory.
It never touches _STATUS.md, MEMORY.md or any other file. Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

E = "projects/pec/execution/"
# target -> (preimage SHA-256, postimage SHA-256)
TARGETS = {
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md":
        ("986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341",
         "65c7f4086f8a053c41219c4966dd062a3821d43927c24fffe29f4e9046d2a367"),
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/ScopeOfWork.md":
        ("4dd777f8f30cf5483d3c33bd002359e7266f8e411e74ba8655e2afc5aa367e62",
         "16ac1cd956c90f0e757c9ce54c4e6645eea50e6d46d69b26f8052ad0484cca41"),
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md":
        ("53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53",
         "347f73c7969cc777027110f101faec6ad40c728e17e095aa2270f268498798bb"),
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/ScopeOfWork.md":
        ("5d286ec97f4c262be9e106537e3b7527e9756b6dd5bf0f1beb8259e1ca114440",
         "82caf28a3757089ec07cd9a21ef70f97840fda7b92f1017236ce5062fdf55872"),
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/ScopeOfWork.md":
        ("5f20b1c48f4f383a07240e04bdf524e8b2443af37cb745c549f939cd6bb8db6e",
         "84e55e58e6632845f7462970180c052ebec5fc677072a4bd883f871a002ffa86"),
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md":
        ("564955235aeab60f169e6377dd9d5bb5fbe2a88a8cc66094e17f6f83987792d2",
         "5b71d3583b2e661564acf889c0a0d6fef93ce24302f29845c3cda0a367ae8276"),
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/ScopeOfWork.md":
        ("d1335c01c54686427d6a04658a43ce9e5c4abe2e446e0acf4d1e87df3a7785b5",
         "d823d55d9e714ac3142c02ee5d599d7167e0836c89c1abee7c513b072073a3d0"),
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/ScopeOfWork.md":
        ("5ce8ab72425ab417c90c3e64a152912a7e39b243f3905e65477dbfd91a40eaa7",
         "c2b88cb65c71bf017fc42c85e164470f0ea86696bd100ed0157d4c2a53f79526"),
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md":
        ("90de9c2d93d8350805410753a21f19c5cf141e48c3e94ffc8096621b3a42c97e",
         "f9c3a057717292e7ccd6def6e0496f69ad6c5100457b15cd17b37477adff8bd4"),
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md":
        ("933c012cf16bb161b0ac1acdbf3caeaac408fa441b6e175b8fc2e7d8b265a579",
         "925fb53b6a9852cc8de3173cc5a4a31333123ffdcd3b4cca57e11432ffcdd5c9"),
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/ScopeOfWork.md":
        ("99730e4e85ce4920d676d9fd62d26c193d5fd714ea0592c15462f37a62011a82",
         "f5590cf55b19f3170cb04e65340e076e672d5d54d8f1e98385372d1dd8f3436e"),
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md":
        ("640f23711f93ec7e987742ed5ed998bea04c681f14bff06bdf2e35a669fcbd5e",
         "813839a080d7e245a0174959bc4f67be265cfabfd5b2177f83cb6fdc934737c8"),
}
# Read-only files the act re-verifies (values at origin/main 125cfacc1, except the two S4 postimages marked below).
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
    # S4 postimages (provisional D-PEC-102) that DEL-04-05 quotes; the act refuses before S4 lands
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md":
        "98a3a3ec227380db2dd030c9c1ca31535d67071a44a3b79508ab4566b32771a0",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md":
        "10819cb2ea90c7663a51bfc400d44e50a0d688325935d30472c8f29e3f087e18",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_STATUS.md":
        "76e76eee155679c3b15b65b2f136a0efd6d79034d033553edcc130f4b5ab709c",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_STATUS.md":
        "b04e097ce114564d35d8e0ec9db2bd8b208467b335bebb42f35991dc6684daa0",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_STATUS.md":
        "7d3eeb9888f10f6e938c7a0c08ff22ee1907df89812064ee76a95e0fdaeae60c",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_STATUS.md":
        "be9b2ae22c49882be9ddd4ab89c7135dc6c250d5b0e78903a1193c2fcff63938",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_STATUS.md":
        "c0691c05ae0f549424f8ab42ed5845485f399312d50f44a357af11f14b335dd1",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_STATUS.md":
        "6509149665f8e7bae97fecfc73cc0f1b4a066fb856c67ba0f3019300f1a2a62f",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_STATUS.md":
        "1aaa65af822b06405d6d7a12740b99b1b0268dfb1eb79966022037b6e827e8b1",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_STATUS.md":
        "7d70fca0dc1853067a28a349cb01f8778af2a9a9c50cb1c5c51e3254b02ac3bf",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_STATUS.md":
        "9d63c0e7838e52d495f684e875a9c0e35b01e9c19055815d6261838db2844653",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_STATUS.md":
        "48f900d8c3f11e1374d155f2859d337c58d924db776bcd1766b077f20e4f9ca8",
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_STATUS.md":
        "03ec8ff022c153f1ba59876718b5ca591d29e9a3806209a8f5454dc63d9fd4a0",
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_STATUS.md":
        "ec684074371c922cd40c4f5e0260685d492f7914553845ad6cc4ea0f9d769ce8",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/Dependencies.csv":
        "e422c16797c1f5bf0ea19f47a714eacd4bbaa4534b7358a5cde7f413266a4fad",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/Dependencies.csv":
        "aea82da5d83d993f7730391527392fdd079fce4f38abd8baed0b81334c35376f",
    E + "PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/Dependencies.csv":
        "d3a255dcbad6656de0feccdb5c343a775bbd42a5ec9dc97d152560479e74b6d2",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/Dependencies.csv":
        "e736ce9a34f31b88c19c007371a87ddafbfc32544beeb0fc1a08dae8aca61a6d",
    E + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/Dependencies.csv":
        "51c7b725b91d7659496964f08b2d2d4934bd158c3fadc65be42dbf110436dfa1",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/Dependencies.csv":
        "150d1261fb6c1739cd160ae9bbc529b3619ce1a1a7b2f1721afeab5983c97ea5",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/Dependencies.csv":
        "5fcf53b3b6e51a77c1d2ecba536eec1a748a12f1a4b0a2c347c76efcc385033b",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/Dependencies.csv":
        "3e4c8f84a2c68b96306a4db0387869f26b3f6c4bda5f35cb084e9d394f4a83ad",
    E + "PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/Dependencies.csv":
        "1774144b8968cc11016ff4de7185026c0e606a043f0624bcc69ef79960e6cea4",
    E + "PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/Dependencies.csv":
        "7de4da4ae4610118d58e7fb1332f6aca3c9d97e9139ff4131bf0a3c1ee2b4efa",
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/Dependencies.csv":
        "a547b53d9712d22d93daade037debac4659571b01d662f1201c29a9d02396ea7",
    E + "PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/Dependencies.csv":
        "ebcd9b43734315aff524a17f0766a97e041cd46ff661423e82af38b3c4a3f8b7",
}
TMP_SUFFIX = ".s1ptmp"

def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha(path): return sha_b(Path(path).read_bytes())

SELF_DIR = Path(__file__).resolve().parent  # the run root when the script runs from it
RUN_ROOT_PREFIX = "projects/pec/execution/_Coordination/SOW_CURRENCY_S1_"  # the only in-tree home it accepts

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
