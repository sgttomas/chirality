#!/usr/bin/env python3
"""B6 Lane A4 steps 4-5: tranche manifest and the three notices.

Starts from the §6.1 / §6.3 drafts (hash-verified by extract_drafts.py), fills
the slots of AGENTS_MD_CANDIDATE_DIFF.md §9, and adds exactly one named
amendment-1 addition to each (amendment 1 §"Verification rule"). Proves that
removing the addition and restoring slot defaults yields each draft hash.
Usage: apply_a4_manifest_notices.py [--dry-run]
"""
import hashlib, pathlib, sys, json
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
S = pathlib.Path(__file__).parent / "drafts"
DRY = "--dry-run" in sys.argv
APP, APPC = "2026-09-26", "20260926"
BASIS = "94e9255b68d6cda15926c7ee0187d6e9a759a43b"
AGENTS_POST = "4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c"
A1DIR = "projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26"
Q1 = "Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them."
Q2 = "revision 4: drop remaining-items and remaining-loop; yes, ride checkpoint 3.  SCA-006 pinned."
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def need(label, got, exp):
    if got != exp: sys.exit(f"ABORT {label}: {got} != {exp}")
def rep(s, old, new, count=1, label=""):
    c = s.count(old)
    if c != count: sys.exit(f"ABORT {label}: {c} hits (expected {count}) for {old[:70]!r}")
    return s.replace(old, new)

EXP = {"manifest": "852b1d5b876500fb4970df8b688394ad2c15883ede6f4a8e8cd821989efbbc45",
       "root": "43cfa3183ed242d7ec3d349e77cce6403e2355bc8965ed93560f2917c132b930",
       "app": "eb927e1f061fd81760079868e78ee288134d180ad41a9c20c0bbdf8ed00b704a",
       "runtime": "385e5e2f5495634470c1c3439b6c8937edc88074132b4f89de211b67ffadc8bc"}
D = {k: (S / f"draft_{k}.txt").read_text() for k in EXP}
for k in EXP: need(f"draft {k}", sha(D[k]), EXP[k])

# ---------------- manifest ----------------
m = D["manifest"]
slots_m = []
def mslot(old, new, count=1, label=""):
    global m
    m = rep(m, old, new, count, label); slots_m.append({"slot": label, "default": old, "applied": new, "count": count})
mslot("PEC-SCA006-OPERATIONAL-RELIANCE-20260925", f"PEC-SCA006-OPERATIONAL-RELIANCE-{APPC}", 2, "tranche_id and instruction_surface_paths item 2 date part")
mslot("\ndate: 2026-09-25\n", f"\ndate: {APP}\n", 1, "date")
mslot("basis: 4d5f7b91102b7106ff74b98118b2bda2fe873f36", f"basis: {BASIS}", 1, "basis (checkpoint-3 basis commit)")
mslot("NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md", f"NOTICE_{APP}_PEC_SCA-006_OPERATIONAL_RELIANCE.md", 6, "notice dates (instruction_surface_paths 3-5, routed_to 3)")
mslot("'[SLOT CP2-ACT: the owner's checkpoint-2 act, transcribed\n    verbatim from the group-2 DECISION.md]'",
      "'SCA-006 CP2: accept; Q1 a; Q2 a'", 1, "CP2-ACT (verbatim checkpoint-2 act)")
mslot("[SLOT CP2-VARIANT: AGENTS.candidate.md, which\n    carries SCA-006 Seq 14-17 plus the work-graph node I1 corrections, or\n    AGENTS.candidate_without_I1.md, which carries SCA-006 Seq 14-17 only]",
      "AGENTS.candidate.md, which\n    carries SCA-006 Seq 14-17 plus the work-graph node I1 corrections", 1, "CP2-VARIANT (Q-CP2-1 (a))")
# authorization_date keeps 2026-09-25: the checkpoint-2 act that accepted the exact text
assert "  authorization_date: 2026-09-25\n" in m
assert "checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md" in m  # group-2 token keeps its act-date value
ADD_M = f"""group2_amendment_1:
  recorded_in: {A1DIR}/DECISION.md
  owner_words:
    - "{Q1}"
    - "{Q2}"
  words_by: Ryan Tufts
  words_date: {APP}
  change: >-
    One addition to this tranche: in projects/pec/AGENTS.md the paragraph at
    AGENTS.candidate.md L261-270 (applied L261-272), which began "PEC's
    deliverable `_STATUS.md` `## Remaining` sections stay in place as", is
    replaced, and no other line changes. The replacement states the owner's
    direction: PEC adds no new `## Remaining` sections or entries; no PEC feed
    profile reads them, so the coordination plane does not scan them; new open
    scope goes to the work graph and its governing records. It keeps the status
    quo for the existing sections until any retirement ruling (they stay in
    place, each item's gate markers still bind that item, and they are updated
    only under a packet that opens that `_STATUS.md`) and keeps retirement, as
    App and Piping did, a separate owner-directed undertaking. It decides no
    retirement. Exact hunk:
    projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/AGENTS_MD_AMENDMENT1_DIFF.md.
  verification: >-
    Amendment 1 section "Verification rule" amends the projects/pec/AGENTS.md
    hash check in `checks` for this tranche: the applied file equals
    49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d with its
    application-date slot filled, except this one hunk. Applied SHA-256
    {AGENTS_POST}.
  owner_hunk_approval: >-
    Amendment 1 requires the owner's explicit approval of the exact hunk text
    before the checkpoint-3 application PR merges; display alone is not
    enough. HELP_HUMAN obtains and records that approval. This manifest does
    not record it and grants nothing.
"""
assert m.endswith("  - No CHECKING, ISSUED, acceptance, release or operational-reliance act.\n")
manifest = m + ADD_M
# proof: strip the addition and restore defaults -> draft
back = manifest[: -len(ADD_M)]
for s in reversed(slots_m):
    back = back.replace(s["applied"], s["default"])
need("manifest reverse proof", sha(back), EXP["manifest"])

# ---------------- notices ----------------
ADD_N = f"""**SCA-006 checkpoint group 2 amendment 1 (2026-09-26).** The owner directed,
verbatim:

> {Q1}

> {Q2}

Recorded at
`{A1DIR}/`.
The one correction it adds to `projects/pec/AGENTS.md`: PEC adds no new
deliverable `## Remaining` sections or entries, and no PEC feed profile reads
them. The existing sections stay in place until any retirement ruling, which
is a separate owner-directed undertaking.

"""
ANCHOR = "Changed paths and authority:\n"
notices = {}
paths = {"root": f"execution/_Coordination/NOTICE_{APP}_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
         "app": f"projects/chirality-app-dev/execution/_Coordination/NOTICE_{APP}_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
         "runtime": f"projects/chirality-runtime/execution/_Coordination/NOTICE_{APP}_PEC_SCA-006_OPERATIONAL_RELIANCE.md"}
res = {"manifest": {"path": f"docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-{APPC}.yaml",
                    "draft": EXP["manifest"], "postimage": sha(manifest), "slots": slots_m,
                    "kept": {"authorization_date": "2026-09-25", "group-2 token": "SCA-006_GROUP-2_2026-09-25"}}}
for k in ("root", "app", "runtime"):
    n = D[k]
    assert "checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/" in n
    n = rep(n, "PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml", f"PEC-SCA006-OPERATIONAL-RELIANCE-{APPC}.yaml", 1, f"{k} manifest path")
    n = rep(n, ANCHOR, ADD_N + ANCHOR, 1, f"{k} anchor")
    back = n.replace(ADD_N, "", 1).replace(f"PEC-SCA006-OPERATIONAL-RELIANCE-{APPC}.yaml", "PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml")
    need(f"{k} reverse proof", sha(back), EXP[k])
    for p in (R / paths[k]).parent, :
        if not p.is_dir(): sys.exit(f"ABORT missing dir {p}")
    if (R / paths[k]).exists(): sys.exit(f"ABORT {paths[k]} already exists")
    notices[k] = n
    res[k] = {"path": paths[k], "draft": EXP[k], "postimage": sha(n)}
# every line check
for label, text in [("manifest", manifest)] + list(notices.items()):
    for i, line in enumerate(text.split("\n")):
        if line != line.rstrip() or "\t" in line: sys.exit(f"ABORT whitespace {label} L{i+1}")
if not DRY:
    mp = R / res["manifest"]["path"]
    if mp.exists(): sys.exit("ABORT manifest exists")
    mp.write_text(manifest)
    for k, n in notices.items(): (R / paths[k]).write_text(n)
res["mode"] = "dry-run" if DRY else "written"
print(json.dumps(res, indent=1))
