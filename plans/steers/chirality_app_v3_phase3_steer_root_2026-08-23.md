# STANDING DIRECTION — Root governance loop — v3 release pathway, Phase 3 (R7 SOW-acceptance transcription, lifecycle initialization, harness repin, dependency extraction, evidence reruns)

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing. Owner: Ryan Tufts. Scope: Root Phase 3 of the v3 release pathway. Target workspace: Root governance loop. Paste together with `plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md`; earlier records are already transcribed in Receipts 114–122 and are cited, not re-pasted.


Owner-carried steer, drafted by HELP_HUMAN 2026-08-23 from the owner's R7
ruling. Paste whole with the attached R7 record; transcribe both verbatim
into the closeout receipt as CHAT_TRANSCRIPTION. R7-A accepts the seven SOWs
as published; this tranche transcribes that acceptance, initializes the seven
carriers, consciously repins the practitioner-harness live baseline in the
same PR, extracts dependencies per the approved plan §4.1, and re-derives the
dependency evidence. Estimates and schedule remain later acts.

## Basis gate (check before any write; stop and report if any line fails)

- `origin/main` contains merge commit `f66bd7f5af7bdf5dc07579f3a507482aca85bd03` (PR #640). Branch from current `main`.
- `AGENTS.md` SHA-256 `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- The seven `ScopeOfWork.md` files carry exactly the R7-A SHA-256 values (listed in the R7 record); every carrier `_STATUS.md` is `OPEN`; the four Phase-1 metadata files per carrier are unchanged from PR #637.
- Live decomposition is applied revision 1.3; deliverable register `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`; `_LATEST.md` `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.
- `execution/_harness/adapter.yaml` SHA-256 `02f01e8a95e1190d0587c56444843fa3d6bc2bb03c4e64ec702ba20758369d41` (the current 53/46-INITIALIZED/7-OPEN pin basis).
- `execution/_Coordination/_TaskManagement/REGISTER.csv` SHA-256 `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518` (19 live; untouched by this tranche).
- `execution/_Coordination/HANDOFF_STATE.md` SHA-256 `b545fc972e68d86ecb683b174346fb37d380be8f84fd9ee36c94a20d3b9a1ea9`.
- Last Root receipt is 122. This tranche writes Receipt 123.
- `plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md` is present in the paste; its SHA-256 is recorded in the receipt.

## Objective

Make the R7 acceptance effective in governed state: each accepted SOW's
frontmatter status becomes accepted-by-R7, each carrier's lifecycle
initializes per the house convention, the practitioner-harness live-tree
baseline is consciously repinned in the same PR under a live manifest,
dependencies are extracted from accepted truth into the seven
`_DEPENDENCIES.md` files with a DEL-02-06 fan-in reassessment, and the
dependency graph and closure audit are re-derived as current derivative
evidence. No estimate, schedule, implementation, activation, TM-register,
pin, or App act. No hold is lifted.

## Nodes (N=3, ordered N1 → N2 → N3; Agent 2 instances with sealed briefs under `execution/_Coordination/AgentRuns/ROOT_V3_PHASE3_2026-08-<DD>/instances/<NODE>/`)

### N1 — Acceptance transcription, lifecycle initialization, harness repin
Write targets, exactly: the seven `ScopeOfWork.md` frontmatter status lines; the seven carrier `_STATUS.md` files; `execution/_harness/adapter.yaml`; `tools/practitioner_harness/test_root_adoption.py`; `tools/validation/test_validate_root_harness_adapter.py`; one new live manifest `docs/governance_harness/tranche_manifests/ROOT-HARNESS-STATUS-REPIN-2026-08-<DD>.yaml`.
1. In each accepted SOW, change only the frontmatter line `status: DRAFT_AWAITING_OWNER_ACCEPTANCE` → `status: ACCEPTED_BY_OWNER_R7 (record SHA-256 dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53)` (exact one-line diff per file, shown in the receipt; no other SOW byte changes).
2. Transition each carrier `_STATUS.md` from `OPEN` to `INITIALIZED` per the house lifecycle convention, appending the dated history entry citing R7-A and the accepted SOW SHA; no other lifecycle content invented.
3. Consciously repin the live practitioner-harness baseline in the same PR (the #637 precedent): update `execution/_harness/adapter.yaml` and the two pinned test files to the exactly measured post-transition values (expected shape: 53 status files, 53 INITIALIZED, 0 OPEN, zero mismatches; unparseable count as actually measured after the history entries are written — measure, never guess). Cover the three instruction-surface paths plus the manifest itself with the new live manifest (schema v1; basis = current `main`; `m2_gate` human-gated-pr, `self_merge: false`, authorization = this steer section verbatim; `m6_notice: pending`, `routed_to: []`; `derivative_disposition: deferred` for `exports/chirality-app/**`).
Check surface: seven one-line SOW diffs; seven `_STATUS.md` transitions with exactly one new history entry each; `python3 -m pytest tools/practitioner_harness/test_root_adoption.py tools/validation/test_validate_root_harness_adapter.py -q` fully green on the post-transition tree; CI-form G4 PASS with the added manifest covering every instruction-surface path.

### N2 — Dependency extraction (plan §4.1)
Write targets, exactly: the seven carrier `_DEPENDENCIES.md` files and `execution/PKG-02_…/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_DEPENDENCIES.md`.
- Extract dependencies only from accepted truth: the accepted SOWs, the applied register rows, the approved `Propagation_Plan.md`, and existing accepted carrier contracts. Record for each carrier its upstream/downstream edges among the 53 deliverables, with each edge citing the accepted source that grounds it. Cross-loop App coupling is recorded only as notice/fan-in edges, never foreign authority (plan §4.1).
- Reassess DEL-02-06 as the integration/fan-in carrier: update only its `_DEPENDENCIES.md` to record the six DEL-02-07..12 evidence fan-in edges and DEL-04-11's validator relationship, citing the accepted SOWs; no `_CONTEXT.md`, SOW, or `_STATUS.md` change.
- An edge that cannot be grounded in accepted truth is omitted and reported, never invented.
Check surface: every recorded edge carries its grounding citation; no new deliverable, scope, or objective content; DEL-02-06's other files byte-identical.

### N3 — Evidence reruns (derivative)
Write targets, exactly: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/DEP_GRAPH_POST_PHASE3/` (new) and `…/Evidence/AUDIT_DEP_CLOSURE_POST_PHASE3/` (new). Earlier evidence folders are preserved untouched.
- Re-derive the objective-relative `WORK_GRAPH.json`/`DAG.md` from live nodes including the extracted dependencies; recompute SCCs; a needed cut/merge is human-gated — record it as a blocker and stop that step.
- Fresh `AUDIT_DEP_CLOSURE` over the post-extraction state; expected: 53 deliverables, zero unresolved closure violations, the Phase-1 initialized-empty warning cleared or explained.
- Both outputs cite the accepted snapshot, R7, and this tranche's N1/N2 outputs, and name their next required rerun (after estimates/schedule or any dependency change).
Check surface: graph node set equals the 53 register rows plus packages; SCC report present; closure verdict recorded with reasons; no write outside the two new folders.

## Not selectable in this tranche
`AGENTS.md`, `agents/**`, `docs/**` beyond the one named manifest, `tools/**` beyond the two named test files, the seven live decomposition files, `execution/_ScopeChange/**` beyond the two new Evidence folders, any `_CONTEXT.md` or `_REFERENCES.md`, DEL-02-06's `_CONTEXT.md`/`ScopeOfWork.md`/`_STATUS.md`, estimates, schedules, the Task Management register, `runtime/**`, `projects/**`, `exports/**`, pins, and any App surface. No lifecycle state beyond the seven OPEN → INITIALIZED transitions.

## Failure rule
Unlimited repair with fresh re-review per node. Never widen a node's write
set; if a needed write falls outside it, report and stop that node. A
harness assertion that cannot be satisfied by measured values is reported
with the exact failure, not force-fitted.

## Closeout
One tranche, one branch `codex/root-v3-phase3-2026-08-<DD>`, one PR to
`main`, commits in order N1 → N2 → N3. Append Receipt 123 with: this steer
and the R7 record as CHAT_TRANSCRIPTION (record both SHA-256 values);
per-node write sets; the seven one-line SOW diffs; the seven lifecycle
transitions; the measured harness repin values; every extracted edge count;
graph/SCC/closure results; validator outputs including the CI-form G4 output;
`execution/_Coordination/HANDOFF_STATE.md` updated (Phase 3 done; remaining:
estimates, schedule, their evidence reruns, and the separately gated
implementation pathway). Run before pushing: the standard validator set and
`git diff --check`. Evidence-whitespace convention applies to any captured
logs. Do not merge. If `main` advances, request sync authorization from the
owner and record it in the receipt. HELP_HUMAN byte-verifies before
endorsement.
