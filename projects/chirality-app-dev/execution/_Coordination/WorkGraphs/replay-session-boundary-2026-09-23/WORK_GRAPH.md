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
| W1 — replay projection boundary | WORKING_ITEMS owns App replay source and focused tests. | DEL-05-04 contract, instruction record identity fields and consumed dependencies. | Mixed and foreign-only responses disclose conflict; all exposed session-bearing fields identify selected session; same-session evidence remains. | READY |
| V1 — verify and review actual candidate | WORKING_ITEMS runs applicable checks; independent fresh read-only TASK applies `software-code-review` to frozen full diff. | W1 candidate. | Focused regression, required App product/whole-repo checks and independent review pass; repairs backchecked. | PLANNED |
| P1 — substantive PR | WORKING_ITEMS integrates W1/V1, graph and slice evidence. | V1. | PR merged after required CI and review on actual revision. | PLANNED |
| C1 — bounded closeout | WORKING_ITEMS compares DEL-05-04 SOW, dependencies and governance against integrated implementation via `bounded-reconciliation`; route only eligible unhomed concerns. | P1 merged. | Warranted consequences applied or supported no-change recorded; unmet implementation returned to graph. | PLANNED |
| M1 — terse MEMORY row | WORKING_ITEMS updates DEL-05-04 MEMORY.md. | C1. | Date/run, actual DEL work and central evidence/PR pointers. | PLANNED |
| F1 — final PR | WORKING_ITEMS integrates closeout, MEMORY and completed graph. | C1/M1 and final review/checks. | Final PR merged; Git/PR service confirms merge. | PLANNED |

## Current state and recovery

- Checked basis: clean isolated `/private/tmp/chirality-app-loop-trial`, branch `codex/app-loop-trial`, start `2a9b00fe9e67a4d98017833dace867a01867c591`; current work graph was none.
- Preflight: APP-HOLD-1 ALLOW for DEL-05-04 dispatch and DEL-05-01/02/03/05 and DEL-04-01 accepted-dependency consumption on 2026-09-23. Formal satisfaction and lifecycle fields remain unchanged.
- Next: implement W1, then freeze and review V1. One integration owner for all writes: this WORKING_ITEMS agent. No active child or shared test process at graph creation.
- Graph maintainer: WORKING_ITEMS in this isolated branch. Preserve work and check state here if interrupted.

| Completed work / node | What changed and was checked | Unresolved consequence |
|---|---|---|
| Discovery | Read current decomposition, DEL-05-04 and DEL-05-01/03 SOWs, replay code/types/UI; selected route from three candidates. | W1 implementation and verification. |
