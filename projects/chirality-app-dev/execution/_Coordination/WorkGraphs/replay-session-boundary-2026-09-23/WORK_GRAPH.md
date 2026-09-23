# Work graph — selected-session replay boundary

## Intent and selected route

- Stable run identity: `APP-REPLAY-BOUNDARY-2026-09-23`.
- Intended result: a DEL-05-04 selected-session replay projection does not present instruction history, instruction bases, transcript items, events, or session metadata from another session when one response contains conflicting identities. It preserves explicit conflict diagnostics and same-session evidence.
- Steering: owner requested one limited real App development-loop trial; HELP_HUMAN selected the DEL-05-04 boundary slice on 2026-09-23. This graph narrows the implementation to replay response projection and its focused tests. Fractional `maxItems` behavior is a later ordinary DEL-05-04 observation, not this trial or automatic Task Management intake.
- Route: accepted App decomposition SOW-042/SOW-046 → DEL-05-04 ScopeOfWork replay identity/conflict obligations → current `selected-session-replay.ts` and Session lens → focused negative regression and candidate-bound checks. DEL-05-01 central session identity, DEL-05-02 events, DEL-05-03 redaction, DEL-04-01 adapter interface and DEL-05-05 artifacts are consumed as relevant constraints, with no modification to their owners. APP-HOLD-1 dispatch and dependency-consumption preflights returned ALLOW at `2a9b00fe9e67a4d98017833dace867a01867c591`.
- Authority limits: no Runtime contract change, lifecycle promotion, accepted dependency status, issued baseline, manual, formal scope change or release act. Source identity conflicts must remain visible. Redaction is a separate live-sink obligation; this slice preserves its boundary without asserting full redaction conformance.
- Method: `chirality-root:bundled:workflow:construct-local-work-graph`; final closeout uses `chirality-root:bundled:workflow:bounded-reconciliation`. The current graph and pointer are navigation/execution state, not instruction amendments.

## Deliverable scope

| Deliverable / basis | What exists | This undertaking | Nodes |
|---|---|---|---|
| DEL-05-04, ScopeOfWork current replay contract and Dependencies.csv | Projection filters foreign events and recomputes transcript on detected conflict, but returns instruction history and bases unchanged; Session lens renders both. | Detect foreign instruction record identities, suppress their content, keep same-session records and truthful conflict evidence. | W1, V1, P1, C1, M1, F1 |

## Work

| ID / outcome | Scope and owner | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 — replay projection boundary | WORKING_ITEMS owns App replay source and focused tests. | DEL-05-04 contract, instruction record identity fields and consumed dependencies. | Mixed and foreign-only responses disclose conflict; all exposed session-bearing fields identify selected session; same-session evidence remains. | COMPLETE at `d82568bc1`; focused replay 8/8 and typecheck pass. |
| V1 — verify and review actual candidate | WORKING_ITEMS runs applicable checks; independent fresh read-only TASK applies `software-code-review` to frozen full diff. | W1 candidate. | Focused regression, required App product/whole-repo checks and independent review pass; repairs backchecked. | COMPLETE: independent full-diff PASS through the merged `57e3cf680` head, full Vitest/typecheck/build, harness self-check/pytest, hold scan and controlled premerge PASS. See `RUN_EVIDENCE.md`, machine reports and PR #866 CI. |
| P1 — substantive PR | WORKING_ITEMS integrates W1/V1, graph and slice evidence. | V1. | PR merged after required CI and review on actual revision. | COMPLETE: [PR #866](https://github.com/sgttomas/chirality/pull/866) merged as `2ea7725230c5c370a5b008138d4486ed427b3bd2` from reviewed head `57e3cf680df807e28962d074e1f65cfa99088ac0`; required CI passed. |
| C1 — bounded closeout | WORKING_ITEMS compares DEL-05-04 SOW, dependencies and governance against integrated implementation via `bounded-reconciliation`; route only eligible unhomed concerns. | P1 merged. | Warranted consequences applied or supported no-change recorded; unmet implementation returned to graph. | COMPLETE: comparison below; descriptive dependency counts corrected, formal fields unchanged, no eligible Task Management intake. |
| M1 — terse MEMORY row | WORKING_ITEMS updates DEL-05-04 MEMORY.md. | C1. | Date/run, actual DEL work and central evidence/PR pointers. | COMPLETE: run row links central evidence, merged substantive PR #866 and [final PR #868](https://github.com/sgttomas/chirality/pull/868). |
| F1 — final PR | WORKING_ITEMS integrates closeout, MEMORY and completed graph. | C1/M1 and final review/checks. | Final PR merged; Git/PR service confirms merge. | ACTIVE: [PR #868](https://github.com/sgttomas/chirality/pull/868) is open; local final records checks PASS (`FINAL_RECORD_CHECKS.json`, `FINAL_COMPARE.txt`, `FINAL_PATH_CHECK.txt`). F1 is COMPLETE when its actual reviewed/CI-passing head merges, verified through GitHub. |

## Bounded closeout — merged basis `2ea772523`

`chirality-root:bundled:workflow:bounded-reconciliation` compared the merged
replay change and [PR #866](https://github.com/sgttomas/chirality/pull/866) with
DEL-05-04's current ScopeOfWork.md, Dependencies.csv, _DEPENDENCIES.md,
_CONTEXT.md, _REFERENCES.md, _STATUS.md and MEMORY.md. The current Scope of Work
already requires explicit conflicting evidence and read-only projection from
canonical records and retains the future live-proof obligations; the accepted
scope, requirements and verification limits need no amendment. _CONTEXT.md and
_REFERENCES.md remain accurate, and _STATUS.md remains IN_PROGRESS. The merged
slice did not satisfy the separate session-store or redaction dependencies or
create a new formal relationship.

Formal `Dependencies.csv` has 9 ACTIVE rows: 7 SATISFIED and 2 PENDING
(`DEP-05-04-005` DEL-05-01; `DEP-05-04-008` redaction constraint). The
descriptive _DEPENDENCIES.md table agrees, but its counts said 9 SATISFIED;
this closeout corrects only those counts to match the formal rows. The
direct formal-row/count/MEMORY-link check is recorded in `CLOSEOUT_COMPARE.txt`.
The fractional `maxItems` observation belongs to DEL-05-04 for possible later
work, while the existing live-proof residuals already have this deliverable
home. Neither is an unhomed material concern; no Task Management intake is
eligible. No lifecycle, dependency satisfaction, authority pin, decision or
release state changes.

After binding final PR #868 in MEMORY, `FINAL_COMPARE.txt` rechecks the formal
CSV and descriptive counts, graph pointer/path, both local evidence links and
both PR URLs. `FINAL_RECORD_CHECKS.json` and `FINAL_PATH_CHECK.txt` retain the
required records-only check results. The frontend source gates from P1 are
unaffected by this final PR's document-only diff.

## Current state and recovery

- Checked basis: clean isolated branch `codex/app-loop-trial` from `2a9b00fe9e67a4d98017833dace867a01867c591`; current work graph was none at start. Host checkout paths are retained in run evidence artifacts.
- Preflight: APP-HOLD-1 ALLOW for DEL-05-04 dispatch and DEL-05-01/02/03/05 and DEL-04-01 accepted-dependency consumption on 2026-09-23. Formal satisfaction and lifecycle fields remain unchanged.
- Next: obtain fresh read-only review and required CI on final PR #868's actual head, then merge F1. One integration owner for all writes: this WORKING_ITEMS agent. No shared test process is running.
- Graph maintainer: WORKING_ITEMS in this isolated branch. Preserve work and check state here if interrupted.

| Completed work / node | What changed and was checked | Unresolved consequence |
|---|---|---|
| Discovery | Read current decomposition, DEL-05-04 and DEL-05-01/03 SOWs, replay code/types/UI; selected route from three candidates. | W1 implementation and verification. |
| W1/V1 | `d82568bc1` filters foreign instruction records and preserves selected transcript on instruction-only conflict; reviewer PASS on the final `57e3cf680` substantive head, required CI passed and PR #866 merged. Checks linked in `RUN_EVIDENCE.md`. | C1/M1/F1 final closeout only. |
| P1/C1 | PR #866 merged as `2ea772523`; bounded comparison above supports no SOW/context/reference/status amendment and corrects only the descriptive dependency counts. | F1 checks/review/merge. |
| M1 | DEL-05-04 MEMORY run row now links the graph, central evidence and both PRs. | F1 checks/review/merge. |
