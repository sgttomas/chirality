"""I107 SB: B1's reviewed delta table (delta_reviewed_b1.json) for I65's delta_inventory2.py, from a dry run's
inventory (57c92a7b33 -> the PR head). An entry is written only for a hunk that SQ's Pass A produced and RV124
(RV-Q) reviewed, shown mechanically:
  (a) the file's PR-head blob equals NUM 75cd6be76b's, and b1 ddc8eaaf54's (SQ's head 69002bc862 with registration.diff
      applied), except retained_memory.rs, where NUM 75cd6be76b's change is ROOT's comment-only citation correction;
  (b) every removed line of the hunk is removed, and every added line added, by the same file's part of one of
      the three reviewed diffs: SQ's G5 commit (law/profile_block.diff, 57c92a7b33 -> b075c5c59f), SQ's G6
      commit (g6/g6_commit.diff, b075c5c59f -> 69002bc862) and registration.diff (69002bc862 -> ddc8eaaf54);
      prep_identity.sh's P3-P5 show those files equal Git, byte for byte. A comment line may also come from ROOT's
      citation correction (P5b: comment lines only), which is named as such and is not a review.
A hunk that fails (a) or (b) gets no entry, so the pass stops on it (5), or reads it (6) for a qualification test.
Usage: python3 mk_delta_reviewed.py <repo> <dry-run delta_inventory.json> <out json>  (Git reads only)"""
import json, os, re, subprocess, sys
repo, inv_p, out_p = sys.argv[1:4]
R0 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SQ = os.path.join(R0, "I104", "b1_sq_01")
P = "projects/chirality-piping/"; HEAD = "d07006c2f001be5565646d6f1cf046e6dc96006c"; REG = "ddc8eaaf5496e8fc0f4d6b905b38cae1e9b88bd0"
NUM = "75cd6be76bd6407fc24e0f1da834c2135407b69e"   # NUM: ROOT's comment-only citation correction of the threshold_bytes entry
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
git = lambda *a: subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=env, check=True).stdout.strip()
DIFFS = {"SQ G5 (law/profile_block.diff, 57c92a7b33..b075c5c59f)": os.path.join(SQ, "_run_records", "law", "profile_block.diff"),
         "SQ G6 (g6/g6_commit.diff, b075c5c59f..69002bc862)": os.path.join(SQ, "_run_records", "g6", "g6_commit.diff"),
         "R6b registration (registration.diff, 69002bc862..ddc8eaaf54)": os.path.join(SQ, "registration.diff")}
def parts(path, text=None):
    """{file rel: (removed lines, added lines)} from a unified diff, stripped"""
    out, cur = {}, None
    for l in (text if text is not None else open(path, encoding="utf-8").read()).split("\n"):
        m = re.match(r"^\+\+\+ b/" + re.escape(P) + r"(.*)$", l)
        if m: cur = out.setdefault(m.group(1), (set(), set())); continue
        if l.startswith("--- ") or l.startswith("diff --git"): continue
        if cur is not None and l.startswith("-"): cur[0].add(l[1:].strip())
        elif cur is not None and l.startswith("+"): cur[1].add(l[1:].strip())
    return out
PARTS = {k: parts(v) for k, v in DIFFS.items()}
# ROOT's citation correction (RR "I108's package returned; the `threshold_bytes` citation corrected; ..."; NUM 75cd6be76b):
# not a reviewed diff, so only its comment lines are accepted as a source
CORR = "ROOT's citation correction (comment lines only; git diff ddc8eaaf54 75cd6be76b)"
PARTS[CORR] = {k: ({x for x in v[0] if x.startswith("//")}, {x for x in v[1] if x.startswith("//")})
               for k, v in parts(None, git("diff", REG, NUM, "--", P + "core/product_physics/src/retained_memory.rs")).items()}
WHAT = {
 "core/product_physics/src/retained_memory.rs#threshold_bytes":
   "R6b's registration: `threshold_bytes` = 11_274_289_152 (M = 10.5 GiB) and its comment, in `REGISTERED_PROFILES` (an item: a static's "
   "field, no allocation or text). RV124 REVIEW §2-3: M confirmed; registration.diff applies as one hunk; PP 741/1 (Mac t13)/79 registered. "
   "This pass gates its bytes (entry: equal to NUM 75cd6be76b's; entry_code: its code lines equal to b1 ddc8eaaf54's; m) and the law tests at that M (law, law_sq).",
 "core/product_physics/src/retained_memory.rs#F_T11_LATE_CAPTURE":
   "SQ G6's SF-1 (RR \"RV112 passes SA\"): G-B's late bound in the const fn `phase_caps` becomes T11 - F_T11_LATE_CAPTURE / C (integer "
   "arithmetic on profile constants: no allocation or text, so TEXT and the profile are unchanged by it). RV124 REVIEW §1.5 and §4: exact "
   "(every coefficient a multiple of C, pinned), G-B's bound 405,120 B in-build; M01-M03 and M09 killed. This pass runs those law tests (law).",
 "core/product_physics/src/retained_memory_law_tests.rs":
   "SQ's G6 re-pins (PLAN_v2 §3.3, A1-N-3, I89's value pins, SF-1, N-1, N-2) at M = 10.5 GiB. RV124 REVIEW §4: every listed re-pin present and right; "
   "20 of 21 mutants killed (M17 equivalent, Q-N4). This pass runs them (law: 0 failed; law_sq: the in-build record equals SQ's).",
 "core/product_physics/src/retained_memory_witness_tests.rs":
   "SQ's S1 witnesses and DEF-O reports (PLAN_v2 §3.4; SQ item 9). RV124 REVIEW §5: every entry point passes, outcomes asserted. "
   "This pass runs SQ's 40 entry points, one process each (witnesses gate: equal to SQ's lines).",
 "core/product_physics/tests/retained_memory_challenge.rs":
   "SQ's challenge (PLAN_v2 §3.5, A1-S-1, CAP_BYTES 16 GiB). RV124 REVIEW §6: all 27 entries and the default pass, each peak within its bound. "
   "This pass runs every entry (challenge gate: peaks and bounds equal to SQ's).",
}
inv = json.load(open(inv_p)); need = inv["unreviewed"] + inv["unreviewed_qualification_tests"]
entries, refused = [], []
for r in need:
    rel = r["file"]
    try:
        hb = git("rev-parse", f"{HEAD}:{P}{rel}")
        same = hb == git("rev-parse", f"{NUM}:{P}{rel}") and (hb == git("rev-parse", f"{REG}:{P}{rel}") or rel in PARTS[CORR])
    except subprocess.CalledProcessError:
        same = False
    hunk = git("diff", "-U0", inv["old"], inv["new"], "--", P + rel).split("\n")
    lines, cur = [], None
    for l in hunk:
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", l)
        if m:
            n, nc = int(m.group(3)), int(m.group(4) or 1)
            cur = (f"{n}-{n + nc - 1}" if nc else f"after {n}"); continue
        if cur == r["new_lines"] and l[:1] in "-+" and not l.startswith(("---", "+++")): lines.append(l)
    minus = [l[1:].strip() for l in lines if l.startswith("-")]; plus = [l[1:].strip() for l in lines if l.startswith("+")]
    src = {}
    ok = same and (len(minus), len(plus)) == (r["removed"], r["added"])
    for x, k in [(x, 0) for x in minus] + [(x, 1) for x in plus]:
        hit = [name for name, pp in PARTS.items() if rel in pp and x in pp[rel][k]]
        if not hit: ok = False; break
        for h in hit: src[h] = src.get(h, 0) + 1
    if not ok:
        refused.append({"file": rel, "new_lines": r["new_lines"], "class": r["class"], "fingerprint": r["fingerprint"], "head_blob_is_b1s": same}); continue
    entries.append({"fingerprint": r["fingerprint"], "file": rel, "at_final_basis": f"{os.path.basename(rel)}:{r['new_lines']}", "class": r["class"],
                    "removed": r["removed"], "added": r["added"], "from_reviewed_diffs": sorted(src),
                    "evidence": WHAT.get(rel) or next((v for k, v in WHAT.items() if k.startswith(rel + "#") and any(k.split("#")[1] in x for x in plus)), "(no file evidence)") +
                                (" Its comment lines come from ROOT's comment-only citation correction (NUM 75cd6be76b), which cites RR \"R6b: ...\" for M." if CORR in src else "") + " Mechanical: the PR head's blob of this file is b1 ddc8eaaf54's, and every line of this hunk is "
                                "removed or added by the named reviewed diff(s).",
                    "reviewed_by": ("" if CORR not in src else "the code lines: ") + "RV124 (RV-Q), R/REVIEW_RV124/b1_sq_01/REVIEW.md sha256 9bb6f81143f60b7e2edaf7d49887d4a0579acd3ea37d7abe6dac3bf4751a2531 "
                                   "(PASS, 0/0/5), which reviewed SQ's G5 and G6 commits and registration.diff; entry written by I107 (SB) for RV-Q's confirmation"})
json.dump({"about": "B1 Pass B (I107): reviewed entries for the hunks of 57c92a7b33 (SQ's TEXT basis) -> 8248921552 (PR-B1's head) that need one "
                    "(class live, item, cfg-test-stmt, data-live or qualification-test), keyed by delta_inventory2.py's fingerprint. Each is SQ's "
                    "Pass A change, reviewed by RV124, tied to the reviewed diff by mk_delta_reviewed.py.",
           "dry_run_inventory": {"old": inv["old"], "new": inv["new"], "needing_entries": len(need)},
           "entries": entries, "refused": refused}, open(out_p, "w"), indent=1)
print(json.dumps({"needing": len(need), "entries": len(entries), "refused": len(refused)}))
sys.exit(1 if refused else 0)
