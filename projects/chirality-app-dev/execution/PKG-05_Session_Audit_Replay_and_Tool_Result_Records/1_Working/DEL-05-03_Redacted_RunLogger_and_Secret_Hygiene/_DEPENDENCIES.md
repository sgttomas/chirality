# Dependencies: DEL-05-03 Redacted RunLogger and Secret Hygiene

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

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK dependency-extract run on 2026-05-20 used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for anchor and target resolution.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- `[WARNING] UNKNOWN_TBD_RETAINED`: final redaction helper path, run logger path, configured-secret schema, replacement token, and exact policy integration point remain TBD in source documents.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor is present.

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-05-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-05 Session Audit, Replay, and Tool Result Records | ACTIVE | SATISFIED |
| DEP-05-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-021 Provider error classification | ACTIVE | SATISFIED |
| DEP-05-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-041 Runtime redaction | ACTIVE | SATISFIED |
| DEP-05-03-004 | ANCHOR | OTHER | UPSTREAM | OBJ-003 Chirality-owned session auditability | ACTIVE | SATISFIED |
| DEP-05-03-005 | ANCHOR | OTHER | UPSTREAM | OBJ-008 Repeatable validation/key/security checks | ACTIVE | SATISFIED |
| DEP-05-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE | SATISFIED |
| DEP-05-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE | SATISFIED |
| DEP-05-03-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE | SATISFIED |
| DEP-05-03-009 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` hash-mismatch warning | ACTIVE | PENDING |
| DEP-05-03-010 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-05 Anthropic Provider Key, Base URL, and Network Bridge | ACTIVE | PENDING |
| DEP-05-03-011 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-02 HarnessEvent Schema and Append-Only JSONL | ACTIVE | PENDING |
| DEP-05-03-012 | EXECUTION | CONSTRAINT | DOWNSTREAM | DEL-05-05 ToolResultStore and Session Artifacts | ACTIVE | PENDING |
| DEP-05-03-013 | EXECUTION | CONSTRAINT | UPSTREAM | UNKNOWN/TBD final module paths and configured-secret schema | ACTIVE | PENDING |
| DEP-05-03-014 | EXECUTION | INTERFACE | UPSTREAM | Root-runtime operational records and closed field vocabulary | ACTIVE | PENDING |

## Run Notes - 2026-09-03 v3 pathway seating (additive UPDATE)

- `TASK + dependency-extract` method applied in-line by the A12 seating tranche (ephemeral Agent 2 generalist; no TASK run record under `_run_records/` because that path is outside the tranche write set); `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`.
- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`, SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`; `ScopeOfWork.md` re-pinned to that commit in the same tranche.
- Scope of this pass: exactly one new row, `DEP-05-03-014`, making the v3 gate/interface edge consumed by the seated `Remaining` item explicit. Existing rows are preserved byte-identically (no `LastSeen` refresh, no retirement); the full two-pass re-extraction is not claimed for them.
- Evidence: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L324`; quote: "verify that Root-runtime operational records exclude credentials and secrets".
- Target resolution: Root-owned targets keep `TargetLocation=TBD` (no Root path is invented); deliverable targets resolve against the applied decomposition.
- `[WARNING] PROJECT_ID_FORMAT_PROFILE`: the generic `validate_id_format.sh` three-digit profile rejects the accepted two-digit App identities; accepted decomposition IDs are preserved (same finding as the Gate-5 refresh).
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- A2-B / SCC posture: no objective-relative feedback edge was added or linearized; the post-application audit's nine-node SCC remains a warning-bearing derivative finding.
- Schema validation: `python3 tools/validation/validate_dependencies_schema.py Dependencies.csv` PASS after the append; see `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/DEPENDENCY_REFRESH.md`.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:41:22-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | REF-006_HASH_MISMATCH; UNKNOWN_TBD_RETAINED | 13 |
| 2026-09-03T00:00:00-06:00 | UPDATE (additive, one row) | CONSERVATIVE | applied `d6f6cadb2` SHA-256 `932b890e…168716f` | PROJECT_ID_FORMAT_PROFILE; existing rows preserved without LastSeen refresh | 13 |

## Lifecycle Summary

| Metric | Count |
|---|---:|
| ACTIVE rows | 13 |
| RETIRED rows | 1 |
| ANCHOR rows | 5 |
| EXECUTION rows | 9 |
| UPSTREAM rows | 13 |
| DOWNSTREAM rows | 1 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 9 |
| PENDING | 4 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-126
- **Current counts:** ACTIVE 12; RETIRED 1; NOT_APPLICABLE=1; PENDING=3; SATISFIED=9.
- **Correction:** DEP-05-03-011 is RETIRED.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
