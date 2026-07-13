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
| ACTIVE rows | 12 |
| RETIRED rows | 1 |
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
| DEP-04-01-007 | EXECUTION | UPSTREAM | PREREQUISITE | first-adapter probe environment | ACTIVE | TBD |
| DEP-04-01-008 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-03-01 | RETIRED | NOT_APPLICABLE |
| DEP-04-01-009 | EXECUTION | UPSTREAM | CONSTRAINT | DEL-01-02 | ACTIVE | SATISFIED |
| DEP-04-01-010 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-02 | ACTIVE | TBD |
| DEP-04-01-011 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-03 | ACTIVE | TBD |
| DEP-04-01-012 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-04 | ACTIVE | TBD |
| DEP-04-01-013 | EXECUTION | DOWNSTREAM | HANDOVER | DEL-04-05 | ACTIVE | TBD |

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

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Anchors | ACTIVE Execution | Warnings |
|---|---|---|---|---:|---:|---|
| 2026-05-20T19:35:54-0600 | UPDATE | CONSERVATIVE | FOUND | 5 | 8 | SOURCE_STATE; TBD_PROBE_ENVIRONMENT |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 1 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 7 |
| TBD | 5 |
| NOT_APPLICABLE | 1 |

| DependencyType | Count |
|---|---:|
| OTHER | 5 |
| CONSTRAINT | 3 |
| PREREQUISITE | 1 |
| HANDOVER | 4 |
