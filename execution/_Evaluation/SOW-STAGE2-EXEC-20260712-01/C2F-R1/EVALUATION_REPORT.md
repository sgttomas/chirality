# C2F-R1 Independent Consumer Remediation Evaluation Report

Verdict: `BLOCKED`
Gate disposition: `C2G_NOT_ELIGIBLE`
Scoring: none

## Outcome

C2R-R1/R2 and C2A-R1 close all three blockers recorded by the original C2F:
unruled self-bound authority is refused by the root resolver/converter and App
scanner, ISSUED conversion now requires and emits accepted-basis/source/status
bindings, and the root C2A evidence pointer is terminal. Current source hashes,
caller sets, containment, and recorded required checks reconcile.

The repaired consumer gate nevertheless remains blocked. One classified active
root caller, `tools/scope_of_work/derive_review_checklist.py`, strips the raw
`--migration-authority` before calling the repaired resolver. A leading/trailing
padded ruled token therefore succeeds, emits a checklist for `MIGRATION_DUAL`,
and records the normalized ruled authority. This directly violates the sealed
raw-equality and padded-state fail-closed criterion and D-GOV-16 items 4 and 8.

## Basis, method, and coverage

The basis and method are frozen in `EVALUATION_PROTOCOL.md`; exact results and
the reproduction are recorded in `reports/DIAGNOSTICS.md` and
`reproduction/padded-checklist/`. Coverage includes the original C2F evidence,
all 64 exact caller rows, all nine App rows, the 48 root and four App subject
paths, both remediation lanes, current hashes, terminal returns, root pointers,
and recorded root/App/export/build/self-check/practitioner/premerge evidence.

No subject, Git, deliverable, control, status, lifecycle, receipt, release,
H1/H2, retirement, or parent snapshot state was modified. No child was
delegated and no expensive suite was rerun.

## Question results

| Question | Result | Evidence |
|---|---|---|
| 64 exact callers and nine App callers classified | PASS | P0 exact and P2_ROOT sets are identical at 64; App has 9/9 rows and no row outside P0 |
| exact contained and disjoint source changes | PASS | 48 root + 4 App subject paths; intersection 0; live hash mismatches 0; forbidden subject paths 0 |
| exact raw authority and fail-closed states | BLOCKED | root resolver/converter and App scanner pass; active root checklist wrapper accepts padded ruled authority after `.strip()` |
| mandatory ISSUED bindings | PASS | accepted basis, source commit, four source hashes, status hash, exact embedding, and status-byte preservation are implemented and regression-evidenced |
| root C2A terminal pointer | PASS | `WORKING-C2A` and `WORKING-C2A-R1` root status/return pairs are terminal PASS |
| current required check evidence | PASS_WITH_CONTENT_EXCEPTION | root 18 focused/791 full tools and prior unaffected validators/export evidence; App 76 focused/713 full plus typecheck/build/self-check/practitioner/premerge all terminal green at matching hashes |

## Original blocker closure

| Original finding | Remediation result | Status |
|---|---|---|
| `EVAL-C2F-001` arbitrary self-bound unruled authority | root and App now compare to the exact ruled token; unruled/alternate regressions pass at matching hashes | `CLOSED_AS_WRITTEN` |
| `EVAL-C2F-002` missing ISSUED accepted-basis binding | converter requires safe accepted basis and emits it with source/status bindings | `CLOSED` |
| `EVAL-C2F-003` stale root C2A pointer | root initial and repair pointers are terminal with present returns | `CLOSED` |

`EVAL-C2F-004`, the low non-blocking absence of a direct DocumentView
component regression, remains open and does not cause this verdict.

## New blocking finding

`EVAL-C2F-R1-001` (`CONTENT_AUTHORITY`, blocker):

- `derive_review_checklist.py:163` assigns
  `args.migration_authority.strip()` before calling the exact resolver at
  lines 165–169;
- the active caller is classified in P0/P2_ROOT and its current hash matches
  the manifest, so this is neither an unknown caller nor stale evidence;
- the root padded regression at
  `test_scope_of_work_tools.py:93-129` exercises converter and validator seams,
  but not the checklist wrapper; and
- the quarantined reproduction passed `" <ruled-token> "`, exited `0`, wrote
  `padded-authority-output.json`, selected `MIGRATION_DUAL`, and reported the
  stripped exact token.

The green full-tool count does not close an untested mandatory negative state.
This content/authority blocker cannot be averaged against mechanical PASS.

## Classified outcomes

- Schema/mechanical: `PASS`. Required returns and pointers are terminal and
  current hashes reconcile.
- Content/authority: `BLOCKED` by `EVAL-C2F-R1-001`; original findings 001 and
  002 otherwise close.
- Preservation/containment: `PASS`; canon hashes are unchanged, root/App writes
  are exact and disjoint, and no governed deliverable/control/lifecycle path is
  in the subject diff.
- Execution substrate: `PASS`. No remediation waiver or current substrate
  fallback is active; historical substrate events remain preserved in C2F.

## Recommendations and decision queue

No new human authority is required. Route a narrow root caller repair to
`HELPS_HUMANS`:

1. pass the raw CLI authority from `derive_review_checklist.py` to the resolver
   without normalization;
2. add a regression that uses an exact candidate marker but a padded supplied
   authority and proves non-zero exit plus no checklist output;
3. refresh the affected P2_ROOT caller/test hashes and root terminal evidence;
4. run the affected checklist/Scope-of-Work tests and full root tools suite;
   rerun other root checks only if their governed inputs change; and
5. rerun independent C2F-R1. App expensive checks need not repeat if its two
   repaired hashes and terminal evidence remain unchanged.

C2G remains parked until the repaired C2F fan-in passes.
