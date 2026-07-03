# Practitioner Harness — Development Backlog

> **Epistemic status: queued work — not authority, not a status surface.**
> Items here are candidate harness development, recorded so intent survives
> across sessions. Execution follows the established harness pattern: branch +
> PR, owner merges (PR #12/#13 precedent); any change that moves a pinned live
> measurement carries its conscious pin update in the same PR
> (`test_live_baseline.py`'s own convention). Remove an item by PR when done
> or when the owner declines it. Provenance: bridge-loop reflection of
> 2026-07-02 (`_DomainEngines/bridge/LOOP_RECEIPTS.md`, Receipt 0) unless
> noted.

## HB-1 — Comparison anchors fully into harness-recorded form

The reformed bridge-loop protocol forbids prose measurement anchors (receipts
carry pass/fail only), on the finding that the anchors which actually caught
regressions on 2026-07-02 were the harness-recorded ones (live pins, the
adapter drift baseline) — not the prose copies in the old Loop Log. Gaps to
close: loop-level expected state such as the suite pass-count and self-check
severity totals currently have no recorded home at all. Shape: either extend
`test_live_baseline.py` with a pinned severity-totals check, or a small
committed baselines record the harness compares against and reports deltas on
(trend statement, never BLOCK), with the conscious-update convention.

## HB-2 — Generated owner-queue / bridge-status view

Replace hand-maintained owner-queue prose (retired from the bridge workplan
2026-07-02) with a derived view — e.g. `harness.py bridge-status`. Inputs all
exist as structured records today: decision-register rows in
AWAITING_RULING/held states (three registers), the ADOPTED profile's
open_issues live-binding gate line, brief lifecycle states via the
`--verify-adoption` machinery, and `_DomainEngines/bridge/LOOP_RECEIPTS.md`
for the latest gate outcome. Output: a sourced pick-list of owner-shaped acts,
same posture as `next` (the tool never selects; generated view, not
authority). Precondition observed in the reflection: every human act must
have a structured primary artifact — the 2026-07-02 ruling records and
Decision_Log show the current record shapes suffice.

## HB-3 — Broaden the machine-absolute-path detector

`ABS_PATH_RE` (`cmd_self_check.py`, GEN-1/GEN-8/evidence checks) matches
`/Users/` only. Found 2026-07-02: a validation report regenerated inside a
`/private/tmp` worktree silently dropped the `ABS_PATH_IN_EVIDENCE` INFO —
only the exactly-one live pin (CI on PR #17) exposed it. Shape: extend the
pattern to other machine-absolute roots (`/private/`, `/home/`, `/tmp/`,
`/var/folders/`), update the synthetic fixtures, and carry the conscious pin
updates for any live-count movement in the same PR.

## HB-4 — Classify environment-dependent unresolved refs

Fresh clones/worktrees measure more `UNRESOLVED_SOURCE_REF` WARNs than a
working checkout because committed adopted briefs carry `evidence_targets`
refs into gitignored `_harness_generated/` paths (four such refs as of
2026-07-02; see the CHANGE prep packet
`_DomainEngines/bridge/CHANGE_PREP_2026-07-02_profile_result_schema_hooks.md`
§3 for the full accounting). Options: (a) GEN-5 classifies refs that resolve
into a declared gitignored generated root as INFO
("environment-dependent generated-artifact ref") instead of WARN; (b) the
brief generator emits evidence_targets in a form that survives adoption into
the governed record. Either way the fresh-clone and checkout baselines
converge.

## HB-5 — Coordination-artifact check mode (optional, lower priority)

`scope-check`/`evidence-check`/`closeout-digest` are brief-fenced; the
reformed loop protocol covers coordination/control artifacts (decision
packets, CHANGE preps, design docs) with procedural adversarial review
instead. A harness-native analogue — citation resolution over a git diff
range, register-row consistency, convention-precedent presence — would make
that check mechanical. Only worth building if the coordination-artifact
volume stays high after the bridge loop resumes.
