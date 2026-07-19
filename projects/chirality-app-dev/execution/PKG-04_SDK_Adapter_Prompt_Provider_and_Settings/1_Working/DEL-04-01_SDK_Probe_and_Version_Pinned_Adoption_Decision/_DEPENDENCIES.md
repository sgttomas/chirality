# Dependencies: DEL-04-01 First-Adapter Probe and Version-Pinned Adoption Decision

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 13 |
| ACTIVE rows | 11 |
| RETIRED rows | 2 |
| ANCHOR rows | 5 |
| EXECUTION rows | 8 |

| DependencyID | Class | Direction | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-04-01-001 | ANCHOR | UPSTREAM | OTHER | PKG-04 | ACTIVE | SATISFIED |
| DEP-04-01-002 | ANCHOR | UPSTREAM | OTHER | SOW-018 | ACTIVE | SATISFIED |
| DEP-04-01-003 | ANCHOR | UPSTREAM | OTHER | SOW-044 | ACTIVE | SATISFIED |
| DEP-04-01-004 | ANCHOR | UPSTREAM | OTHER | SOW-046 | ACTIVE | SATISFIED |
| DEP-04-01-005 | ANCHOR | UPSTREAM | OTHER | OBJ-004 | ACTIVE | SATISFIED |
| DEP-04-01-006 | EXECUTION | UPSTREAM | CONSTRAINT | REF-006 `docs/PRD.md` | ACTIVE | SATISFIED |
| DEP-04-01-007 | EXECUTION | UPSTREAM | PREREQUISITE | first-adapter probe environment | ACTIVE | SATISFIED |
| DEP-04-01-008 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-03-01 | RETIRED | NOT_APPLICABLE |
| DEP-04-01-009 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-01-02 | ACTIVE | SATISFIED |
| DEP-04-01-010 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-02 | ACTIVE | SATISFIED |
| DEP-04-01-011 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-03 | ACTIVE | SATISFIED |
| DEP-04-01-012 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-04 | RETIRED | NOT_APPLICABLE |
| DEP-04-01-013 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-05 | ACTIVE | SATISFIED |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract run at 2026-05-20T19:35:54-0600.
- Runtime overrides: `SCOPE=DEL-04-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (located and used for anchor/target validation).
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Anchor doc selection: `Datasheet.md` and `_CONTEXT.md` were used for explicit identity and traceability anchors.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`.
- `[WARNING] SOURCE_STATE`: `_REFERENCES.md` records REF-006 `docs/PRD.md` as `HASH_MISMATCH`; closure remains dependent on resolving or explicitly accepting that source-state condition.
- `[WARNING] TBD_PROBE_ENVIRONMENT`: the first-adapter probe environment, exact SDK version, subprocess version, transcript/store decision, packaging result, and adoption verdict remain `TBD`.
- 2026-05-24 WORKING_ITEMS CODEV-001 closure assessment set `DEP-04-01-008` to `SATISFIED` based on `Evidence_CODEV-001_SDK_Probe_Record.md` and `Evidence_CODEV-001_Runtime_Engine_Conformance.md`; live SDK query, packaging, and adoption verdict remain unresolved.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No downstream handoff notes were added because `CONSUMER_CONTEXT=NONE`.
- 2026-07-10 D-APP-53 reconciliation correction: the `[WARNING] SOURCE_STATE` note above is resolved — `_REFERENCES.md` now records REF-006 `docs/PRD.md` as `MATCH` under the D-APP-38 authority corpus (live sha256 verified 2026-07-10); `DEP-04-01-006` closed `SATISFIED` and its stale HASH_MISMATCH note corrected. The warning text is retained above as history.
- 2026-07-10 D-APP-53 reconciliation correction: the `[WARNING] TBD_PROBE_ENVIRONMENT` note above is partially stale — SDK package pins (`@anthropic-ai/claude-agent-sdk@0.3.150`, `@anthropic-ai/sdk@0.93.0`), the deterministic test harness, and Electron packaging posture (PKG-09 `Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`) are now recorded. Still open: live Claude Code subprocess version (`BLOCKED_TBD`; live-LLM demonstration owner-gated per D-APP-52) and the adoption-verdict residuals; `DEP-04-01-007` therefore stays `TBD` (annotate-only per plan section 3.5).
- 2026-07-10 D-APP-53 reconciliation (PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md, DRQ-04): closed `DEP-04-01-006` and `DEP-04-01-009` as `SATISFIED`; annotated `DEP-04-01-007` (owner-gated residual) and `DEP-04-01-010..013` (handover not verifiably consumed by DEL-04-02..05) as left OPEN; synced the summary tables with the CSV (`DEP-04-01-008` was retired by RUL-SCC-001-TRANCHE-001 on 2026-05-24 but this file's tables had not been updated). See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`.
- 2026-07-18 WI-PKG04-01 handover-evidence pass under the D-APP-60 instrument (agent decisions under owner-delegated latitude, never owner acts): `DEP-04-01-010` closed `SATISFIED` (mirror `DEP-04-02-006` closed in the same pass); `DEP-04-01-011` and `DEP-04-01-013` annotated and left OPEN solely on the owner-gated live-probe residual (D-APP-52; same residual as `DEP-04-01-007`); `DEP-04-01-012` not decided — referred to the owner in near-miss form (retire-vs-keep both defensible). The rows' stale `Procedure.md#Steps` citations now resolve to `ScopeOfWork.md` CLM-018 step 13 per owner commit `548caa731` (2026-07-13). See `Evidence_HANDOVER_CONSUMPTION_2026-07-18.md` and `_run_records/TASK_RUN_2026-07-18_DEP-04-01-010-013_handover_evidence.md`.
- 2026-07-18 D-APP-63 owner ruling ("Option A with the rider.", ruled in-session by Ryan Tufts; packet `execution/_Coordination/_DECISIONS/D-APP-63_PACKET_DEP-04-01-012_RETIREMENT_2026-07-18.md`): `DEP-04-01-012` retired `RETIRED` / `NOT_APPLICABLE` — the retirement is the owner's act; WI-PKG04-01 executed mechanical conformance only. Rider verbatim: any DEL-04-04-relevant output from the future D-APP-52 live probe mints a NEW row — revival by new recorded basis; the retired row is never reactivated. Summary tables synced (ACTIVE 11 / RETIRED 2; SATISFIED 8 / TBD 3 / NOT_APPLICABLE 2). See `_run_records/TASK_RUN_2026-07-18_DEP-04-01-012_ruling_execution.md`.
- 2026-07-18 D-APP-52 live-demonstration closures (owner's in-session act 2026-07-18, owner at screen; mechanical conformance by run `DAPP52_LIVE_DEMONSTRATION_2026-07-18` under the D-APP-64 overlay): `DEP-04-01-007`, `DEP-04-01-011`, and `DEP-04-01-013` closed `SATISFIED` on `Evidence_DAPP52_LIVE_PROBE_2026-07-18.md` (live claudeCodeVersion 2.1.150, exact observed live `query()` message sequence, live-confirmed error shapes) and `Evidence_DAPP52_PACKAGED_LIVE_PROOF_2026-07-18_summary.json` (packaged live behavior); consumer mirrors `DEP-04-03-007` and `DEP-04-05-007` closed `SATISFIED` in the same pass. RATE_LIMITED not live-triggered (recorded, not fabricated); DEL-04-05 RQ-011 four-class gap remains that deliverable's gated item. D-APP-63 rider check: no DEL-04-04-relevant output from any pack; no new row minted. Summary tables synced (SATISFIED 11 / TBD 0 / NOT_APPLICABLE 2). See `_run_records/TASK_RUN_2026-07-18_DAPP52_live_demonstration_closures.md`.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Anchors | ACTIVE Execution | Warnings |
|---|---|---|---|---:|---:|---|
| 2026-05-20T19:35:54-0600 | UPDATE | CONSERVATIVE | FOUND | 5 | 8 | SOURCE_STATE; TBD_PROBE_ENVIRONMENT |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 2 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 11 |
| TBD | 0 |
| NOT_APPLICABLE | 2 |

| DependencyType | Count |
|---|---:|
| OTHER | 5 |
| CONSTRAINT | 3 |
| PREREQUISITE | 1 |
| HANDOVER | 4 |
