# Dependencies: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

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
- TASK + dependency-extract updated this register on 2026-05-20T21:02:18-0600 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` outputs are invalid evidence and were not read or consumed.
- Anchor document selection: `_CONTEXT.md` and `Datasheet.md`; execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`, `_REFERENCES.md`.
- Decomposition status: available and used to validate PKG-09, DEL-09-04, SOW-030, SOW-072, SOW-073, OI-003, and OI-004.
- [WARNING] REF-006_HASH_MISMATCH: `_REFERENCES.md` marks `docs/PRD.md` as `HASH_MISMATCH`; assignment override treats this as a source warning only for this run.
- [WARNING] OPEN_ISSUE_TARGET_TYPE: OI-003 and OI-004 were preserved as `TargetType=UNKNOWN` because `OPEN_ISSUE` is not a Dependencies.csv v3.1 target enum.
- No `[WARNING] FLOATING_NODE`: one ACTIVE parent anchor (`DEP-09-04-001`) exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE parent anchor exists.

## Extracted Dependency Register

`Dependencies.csv` v3.1 contains 9 ACTIVE rows.

### Counts

| Dimension | Counts |
|---|---|
| DependencyClass | ANCHOR=4; EXECUTION=5 |
| DependencyType | OTHER=4; PREREQUISITE=2; CONSTRAINT=3 |
| Status | ACTIVE=9 |
| SatisfactionStatus | NOT_APPLICABLE=3; TBD=6 |
| TargetType | PACKAGE=1; REQUIREMENT=4; EXTERNAL=2; UNKNOWN=2 |

### Compact Register

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-09-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-09 - Validation, Packaging, Security, and Release | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-030 - Instruction-root resources | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-072 - macOS arm64 unsigned DMG release target | ACTIVE | NOT_APPLICABLE |
| DEP-09-04-004 | ANCHOR | OTHER | UPSTREAM | SOW-073 - Source completeness for instruction-root assets | ACTIVE | TBD |
| DEP-09-04-005 | EXECUTION | PREREQUISITE | UPSTREAM | Node.js and frontend npm dependencies | ACTIVE | TBD |
| DEP-09-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | Pre-packaging local validation commands | ACTIVE | TBD |
| DEP-09-04-007 | EXECUTION | CONSTRAINT | UPSTREAM | OI-004 - Instruction-root source completeness | ACTIVE | TBD |
| DEP-09-04-008 | EXECUTION | CONSTRAINT | UPSTREAM | OI-003 - SDK subprocess and macOS DMG packaging verification | ACTIVE | TBD |
| DEP-09-04-009 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-09-04-REQ-009 - current shipped Anthropic packaged network guardrails | ACTIVE | TBD |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---|
| 2026-05-20T21:02:18-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | REF-006_HASH_MISMATCH; OPEN_ISSUE_TARGET_TYPE | 9 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 3 |
| TBD | 6 |

Closure remains open because six ACTIVE rows have `SatisfactionStatus=TBD`; no edge should be treated as satisfied until evidence is accepted by the owning workflow.
