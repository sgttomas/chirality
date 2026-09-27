#!/usr/bin/env python3
"""D1 premise amendment (provisional D-PEC-105) bound act: replace existing
files with the tabled candidate bytes, byte-exact.

Group A (always): the DEL-00-03 SPEC, the DEL-00-03 Scope of Work and the
DEL-00-01 ADRs. Group P (only with --with-addon-p, when the owner selects
add-on P): the DEL-00-01 Scope of Work.

Usage (from anywhere):
  apply_d1p.py --repo <REPO_ROOT> --candidates <DIR> [--with-addon-p] [--check-only]

<DIR> holds the candidate files at their repository-relative paths. In the
default mode only the group-A candidates are read; the group-P candidate is
read only with --with-addon-p.

Failure semantics:
- Preflight: every selected candidate hashes to its tabled postimage; every
  target (selected or not) exists and hashes to its tabled preimage; no
  temporary sibling of any target exists; every pinned read-only file hashes as
  tabled; the run-root guard passes. Any failure exits 1 before any byte is
  written. A second run fails here (the selected targets no longer hold their
  preimages).
- Write: each selected postimage is written to a temporary sibling
  (<target>.d1ptmp), hash-checked, then renamed over its target. If any step
  after the first write fails (I/O error, hash mismatch, post-write inventory
  mismatch, changed pinned file, unselected target changed), the script
  restores every replaced target from the preimage bytes it read at preflight
  (again through a temporary sibling), removes every temporary file, and exits
  1. On exit 1 every selected target holds its preimage and no temporary file
  remains (the act never writes an unselected target, so it holds whatever it
  held; a change to it is reported, not repaired). Exit 2 means the rollback
  itself failed (reported target by target).
- Write-set check: the script inventories every file under projects/pec (path
  and SHA-256) before and after the write and requires the difference to be
  exactly the selected targets, each modified from preimage to postimage, with
  nothing created or removed; an unselected target stays byte-identical at its
  preimage. The script's own directory (the run root, where the act's evidence
  is written) is left out of the inventory. If the script's directory path
  begins with projects/pec/ but not with the run-root prefix
  projects/pec/execution/_Coordination/D1_PREMISE_AMEND_, preflight refuses; a
  placement the guard does not refuse still fails closed at the inventory.
It never touches _STATUS.md, _REVIEW.md, MEMORY.md or any other file.
Stdlib only.
"""
import argparse, hashlib, os, sys
from pathlib import Path

E = "projects/pec/execution/"
# target -> (group, key, preimage SHA-256, postimage SHA-256)
TARGETS = {
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md":
        ("A", "DEL-00-03_SPEC",
         "cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae",
         "f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617"),
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/ScopeOfWork.md":
        ("A", "DEL-00-03_SOW",
         "3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741",
         "0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843"),
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md":
        ("A", "DEL-00-01_ADR",
         "f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5",
         "ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e"),
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md":
        ("P", "DEL-00-01_SOW",
         "4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740",
         "3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647"),
}
# Read-only files the act re-verifies before and after the write.
# Rendered by build_apply_d1p.py at basis commit f0a6159c9440557d18a728416166cc1e3e0c862d (f0a6159c9); PINNED values and preimages read there.
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
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_STATUS.md":
        "41c871a5e4c07655a1f526aeb20f74603099f0b5997bbba4d7a8fcc2897ceeea",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_REVIEW.md":
        "c417418e96bfb8e230634049c7ee359fb84ad688a7946b5f819e21b2bc5d6968",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/Review_Findings.csv":
        "3f1cec3bf34776b3cc7e9d0fdacd3dd268e6ddf9dfb4e51855d0d1efa40e25e0",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/Dependencies.csv":
        "a8573c64bf2828add66cba70e00b91115e8d885060b905a689e5ee1d60654467",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_CONTEXT.md":
        "f9647800b5bba9cb13ebedc666ca680d6b41ee00344afffcd4a9817a0ac25701",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_REFERENCES.md":
        "f38d9257b5fff875a7e9d11c9832ed2e08a814a24eac2b3390a95f76e61387eb",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_STATUS.md":
        "629ca0dda894954943b694680ebbaf8688615e0ca3fefa1a18ef84c2cd606cfb",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_REVIEW.md":
        "200125240bbed6cd7e3dd2cc64d0cc8619348cf2cbdfaae3e5ee9d169f8c8b97",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/Review_Findings.csv":
        "fd28bac592572edcdff196fb40fc8d6ebeaf1bab97f8cb207f67196cddc9301e",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/Dependencies.csv":
        "5b42f2de2a098fb8f833736ebaf15445bd50734a9341b7fb19e7fa1d0112cde2",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_CONTEXT.md":
        "d4742ccaf65aeb05620e88413b14c56f416a23920d1b044538ee3a174b05be14",
    E + "PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/_REFERENCES.md":
        "fb18afbb27fe54493f6dac0df890d86359db43ad0b4b8fefbd84075bf68a1146",
}
TMP_SUFFIX = ".d1ptmp"
NEVER = ("_STATUS.md", "_REVIEW.md", "MEMORY.md")

def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha(path): return sha_b(Path(path).read_bytes())

SELF_DIR = Path(__file__).resolve().parent  # the run root when the script runs from it
RUN_ROOT_PREFIX = "projects/pec/execution/_Coordination/D1_PREMISE_AMEND_"  # the only in-tree home it accepts

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
    ap.add_argument("--with-addon-p", action="store_true",
                    help="also write the group-P target (only when the owner selected add-on P)")
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    repo, cand = Path(a.repo).resolve(), Path(a.candidates)
    groups = ("A", "P") if a.with_addon_p else ("A",)
    mode = "+".join(groups)
    selected = [rel for rel, (g, _k, _pre, _post) in TARGETS.items() if g in groups]
    unselected = [rel for rel in TARGETS if rel not in selected]
    problems, pre_bytes, post_bytes = [], {}, {}
    for rel in TARGETS:
        if Path(rel).name in NEVER:
            problems.append(f"target is a file this act never touches: {rel}")
    for rel, (g, key, pre, post) in TARGETS.items():
        if rel in selected:
            c = cand / rel
            if not c.is_file(): problems.append(f"candidate missing: {key} {rel}")
            else:
                post_bytes[rel] = c.read_bytes()
                if sha_b(post_bytes[rel]) != post: problems.append(f"candidate hash mismatch: {key} {rel}")
        t = repo / rel
        if not t.is_file(): problems.append(f"target missing: {key} {rel}")
        else:
            pre_bytes[rel] = t.read_bytes()
            if sha_b(pre_bytes[rel]) != pre:
                what = "already applied or changed" if rel in selected else "unselected target changed"
                problems.append(f"target does not hold its preimage ({what}): {key} {rel}")
        if (repo / (rel + TMP_SUFFIX)).exists(): problems.append(f"temporary already exists: {rel}{TMP_SUFFIX}")
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
        problems.append(f"script directory {rel_self} is inside projects/pec but is not a run root "
                        f"({RUN_ROOT_PREFIX}*); run the bound copy from its run root or from outside the repository")
    print(f"MODE {mode}: {len(selected)} selected target(s), {len(unselected)} held at preimage")
    for msg in problems: print("FAIL " + msg)
    if problems:
        print("preflight failed; nothing written"); return 1
    before = inventory(repo)
    for rel in selected: print(("RENDER " if a.check_only else "PLAN ") + f"{TARGETS[rel][1]} {rel}")
    for rel in unselected: print(f"HOLD {TARGETS[rel][1]} {rel}")
    if a.check_only:
        print(f"CHECK preflight passed; mode {mode}; planned write set {len(selected)} modifies, 0 creates, 0 removes "
              f"(inventory of {len(before)} files taken; the write-set check runs in apply mode); nothing written"); return 0
    replaced = []
    try:
        for rel in selected:
            put(repo, rel, post_bytes[rel], TARGETS[rel][3]); replaced.append(rel)
        after = inventory(repo)
        added = set(after) - set(before); removed = set(before) - set(after)
        modified = {k for k in set(after) & set(before) if after[k] != before[k]}
        if added or removed or modified != set(selected):
            raise RuntimeError(f"write set differs from grant: added={sorted(added)} removed={sorted(removed)} "
                               f"unexpected={sorted(modified - set(selected))} missing={sorted(set(selected) - modified)}")
        for rel in selected:
            if after[rel] != TARGETS[rel][3]: raise RuntimeError(f"post-write hash mismatch: {rel}")
        for rel in unselected:
            if after.get(rel) != TARGETS[rel][2]: raise RuntimeError(f"unselected target changed: {rel}")
        for rel, want in PINNED.items():
            if after.get(rel) != want: raise RuntimeError(f"pinned file changed: {rel}")
    except Exception as e:
        errs = []
        for rel in TARGETS:
            try: (repo / (rel + TMP_SUFFIX)).unlink()
            except Exception: pass  # retried below; only the final state counts
        for rel in replaced:
            try: put(repo, rel, pre_bytes[rel], TARGETS[rel][2])
            except Exception as e2: errs.append(f"{rel}: {e2}")
        for rel in TARGETS:
            try: (repo / (rel + TMP_SUFFIX)).unlink()
            except FileNotFoundError: pass
            except Exception as e2: errs.append(f"{rel}{TMP_SUFFIX}: {e2}")
        for rel in selected:  # final state: every target this act may write is at its preimage, no temporary left
            try:
                if sha(repo / rel) != TARGETS[rel][2]: errs.append(f"{rel}: not at its preimage after rollback")
            except Exception as e2: errs.append(f"{rel}: {e2}")
            if (repo / (rel + TMP_SUFFIX)).exists() and not any(x.startswith(rel + TMP_SUFFIX) for x in errs):
                errs.append(f"{rel}{TMP_SUFFIX}: still present after rollback")
        if errs:
            print(f"FAIL {e}; ROLLBACK INCOMPLETE: {errs}"); return 2
        print(f"FAIL {e}; every replaced target restored to its preimage and every temporary file removed"); return 1
    for rel in selected: print(f"WRITE {TARGETS[rel][1]} {rel}")
    print(f"CHECK mode {mode}; targets {len(selected)}/{len(selected)} byte-exact; write set = grant (0 created, "
          f"{len(selected)} modified, 0 removed under projects/pec outside the run root); "
          f"held at preimage {len(unselected)}/{len(unselected)}; pinned {len(PINNED)}/{len(PINNED)} unchanged")
    return 0

if __name__ == "__main__":
    sys.exit(main())
