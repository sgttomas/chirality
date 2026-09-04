# Coordinator decisions — APPDEV_V3_NODE_H_2026-09-03

Recorded so the owner sees them at byte review. Each entry is a HELP_HUMAN
(coordinator) act transcribed by the implementer from the coordinator's
in-session direction; none is an owner ruling. Truthful attribution (workplan
non-negotiable 1). Implementer-latitude decisions (method choices inside the
sealed brief) are recorded in `RETURN.md` §4, not here.

## D0 — 2026-09-03 — sealed brief (round 1)

The launch brief (`instances/H1_IMPLEMENTER/LAUNCH_BRIEF.md`) is the only
coordinator direction received before the first freeze. Its Step 0 gate was
resolved by the implementer under the committed workplan rule
(`STEP0_DISCOVERY.md` §4): the `NOT_SELECTABLE_UNTIL` tag was flipped to
`SELECTABLE` with the cited merged act, as the brief permits when the rule
permits it.

No further coordinator decision had been issued at the first freeze; later
directions (review dispositions, closeout deltas) are appended below as they
occur.

## D1 — 2026-09-03 — round-1 review disposition (re-freeze required)

Direction (verbatim gist): "Node H round-1 review verdict: FAIL on one MAJOR
(H1-F1); zero BLOCKER … file it verbatim in your run record
(`instances/H2_REVIEWER/REVIEW_01_2026-09-03_over_021e1f186.md`, never edited).
Required: H1-F1 (per-run manifests written before the EXIT-trap teardown; make
the per-run manifest the last act of teardown, regenerate both from the retained
bytes, add them to the bundle manifest, correct EVIDENCE.md §7 and RETURN.md §1
item 1). Strongly recommended: H1-F2 (fail fast on an occupied port; restrict
the kill to `$NEXT_PID` and children), H1-F3 (only `rm -rf` a mktemp-created
`USER_DATA`; document the shared `HARNESS_TMP_ROOT`). NOTEs at your discretion
(H1-F4, F5, F6, F7, F8, F9, F12). Selectability flip ruled WITHIN_AUTHORITY;
keep it. Do not rerun the full Section 8 suite unless the script change requires
regenerated run trees. No product source change. Commit the remediation as a new
commit, re-freeze, report REVIEW_READY. Do not push."

Effect: round 2 applies H1-F1, F2, F3 and the NOTEs F4, F5, F6, F7, F8, F10, F12
now; H1-F9 (quote the pre-flip tag in the History line) is a closeout act and is
carried to the closeout commit. The retained run trees are unchanged; the two
per-run manifests were regenerated from the retained bytes.

## D2 — 2026-09-03 — closeout disposition after review-2 PASS

Direction (verbatim gist): "REVIEW_PASS — round-2 head da3ceb310, verdict PASS
(H1-F1 FIXED; zero BLOCKER/MAJOR/MINOR; five NOTEs H2-F1..F5). File it verbatim
as `instances/H2_REVIEWER/REVIEW_02_2026-09-03_over_da3ceb310.md`. No reviewed
script, comparator, captured-run, or manifest byte may change after PASS except
where a narrative file is regenerated into the bundle manifest. H2-F2/H2-F5:
one-clause narrative corrections in the closeout commit; regenerate the bundle
manifest. H1-F9: quote the pre-flip tag verbatim in the `_STATUS.md` History
line. H2-F1/F3/F4: record as residuals; if worth a bounded follow-on, seed one
SELECTABLE evidence-only item with write locus limited to the rerun script and
its evidence. Decide remove-vs-revise for V3-01 per its `Removed when`. Drop the
DRAFT banner. Then HANDOFF_STATE.md, run-record MANIFEST.sha256, CHECKS.json
closeout round, receipt (Receipt-216, Parent Receipt-212), rebase onto
origin/main 1d9b37970, validators, `git diff --check`, change-scope with
`--base 1d9b37970 --head <head>`, corpus status, APP-HOLD preflight. STOP before
pushing: write the PR body to the scratchpad; HELP_HUMAN pushes and opens the
PR. Remove wt-base now; keep wt-nodeH."

Effect: applied as written. V3-01 is revised, not removed (its `Removed when`
names revision after each v3 landing and removal only at G5 fan-in, which has
not occurred); because PRs 687–689 already touched a named trigger surface, the
revised item stays `SELECTABLE` with revision 2 owed instead of being parked.
V3-02 seeded for H2-F1/F3/F4. The bundle manifest was regenerated because
`EVIDENCE.md` is pinned in it; no captured-run, script, comparator, or
per-run-manifest byte changed after PASS.
