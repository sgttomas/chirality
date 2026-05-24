# Dependencies: DEL-08-04 Type 2 Subagent Governance Bridge

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no declared upstream dependency edges have been accepted outside the extracted register.

## Declared Downstream

TBD - no declared downstream dependency edges have been accepted outside the extracted register.

## Extracted Dependency Register

| Metric | Count |
|---|---:|
| Total rows | 6 |
| ACTIVE rows | 6 |
| RETIRED rows | 0 |
| ANCHOR rows | 1 |
| EXECUTION rows | 5 |

| DependencyID | Class | Direction | Type | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-08-04-001 | ANCHOR | UPSTREAM | OTHER | WBS_NODE | SOW-063 Governed subagent runtime | ACTIVE |
| DEP-08-04-002 | EXECUTION | UPSTREAM | PREREQUISITE | DOCUMENT | Accepted source corpus for DEL-08-04 | ACTIVE |
| DEP-08-04-003 | EXECUTION | UPSTREAM | PREREQUISITE | UNKNOWN | Existing `evaluateSubagentGovernance` behavior or target contract | ACTIVE |
| DEP-08-04-004 | EXECUTION | UPSTREAM | PREREQUISITE | UNKNOWN | Permission overlay and hook infrastructure | ACTIVE |
| DEP-08-04-005 | EXECUTION | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | ACTIVE |
| DEP-08-04-006 | EXECUTION | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-08-05 Subagent Child Run Records and Artifacts | ACTIVE |

## Run Notes

- Runtime overrides: `SCOPE=DEL-08-04`; `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=NONE`.
- Source selection: `SOURCE_DOCS=AUTO`; `DOC_ROLE_MAP=DEFAULT`; `ANCHOR_DOC=Datasheet.md` with `_CONTEXT.md` traceability cross-check; `EXECUTION_DOC_ORDER=Procedure.md, Specification.md, Guidance.md, Datasheet.md, _REFERENCES.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Decomposition authority located and used for DEL-08-04, SOW-063, DEL-04-01, and DEL-08-05 resolution.
- [WARNING] SOURCE_HASH_MISMATCH: `_REFERENCES.md` reports REF-006 expected SHA `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` and actual SHA `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`; source documents state this is a warning, not a blocker.
- [WARNING] TARGET_UNRESOLVED: `evaluateSubagentGovernance` implementation/target contract remains `TBD` in the source.
- [WARNING] TARGET_UNRESOLVED: permission overlay and hook infrastructure are explicit prerequisites, but no single stable target deliverable is named in the local source; the row preserves `TargetType=UNKNOWN`.
- [WARNING] TARGET_INFERRED: SDK probe prerequisite was resolved to DEL-04-01 from decomposition because the local source names SDK/R0/R1 probes rather than a deliverable ID.
- Parent anchor check: PASS; exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.

## Run History

- 2026-05-20T20:54: `TASK + dependency-extract`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, decomposition located, warnings: SOURCE_HASH_MISMATCH, TARGET_UNRESOLVED x2, TARGET_INFERRED x1. ACTIVE counts: ANCHOR=1, EXECUTION=5.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 6 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| PENDING | 1 |
| TBD | 5 |

## Downstream Handoff Notes

Not applicable; `CONSUMER_CONTEXT=NONE`.
