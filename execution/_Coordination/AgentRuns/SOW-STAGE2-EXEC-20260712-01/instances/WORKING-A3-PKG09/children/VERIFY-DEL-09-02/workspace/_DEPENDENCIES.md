# Dependencies: DEL-09-02 Section 9 Runtime Validation Additions

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
- 2026-05-20 dependency-extract run used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority loaded: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor validation and target-label resolution were available.
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read and was not consumed as evidence.
- Defaults applied: SOURCE_DOCS=AUTO, DOC_ROLE_MAP=DEFAULT, ANCHOR_DOC=Datasheet.md, EXECUTION_DOC_ORDER=Specification.md then Guidance.md then Procedure.md then Datasheet.md.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- [WARNING] TBD_SURFACES: exact validation registry path, runner entrypoint, local validation command, summary schema path, and summary fields remain TBD in source documents.
- No `[WARNING] FLOATING_NODE`: one active `IMPLEMENTS_NODE` anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one active `IMPLEMENTS_NODE` anchor was extracted.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 25 |
| ACTIVE rows | 25 |
| RETIRED rows | 0 |
| ANCHOR rows | 13 |
| EXECUTION rows | 12 |
| IMPLEMENTS_NODE anchors | 1 |
| TRACES_TO_REQUIREMENT anchors | 12 |
| UPSTREAM execution rows | 12 |
| DOWNSTREAM execution rows | 0 |

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-09-02-001 | ANCHOR | OTHER | UPSTREAM | DEL-09-02 Section 9 Runtime Validation Additions | ACTIVE |
| DEP-09-02-002 | ANCHOR | OTHER | UPSTREAM | SOW-036 Section 8/9 validation | ACTIVE |
| DEP-09-02-003 | ANCHOR | OTHER | UPSTREAM | SOW-037 Product-owned engine contract | ACTIVE |
| DEP-09-02-004 | ANCHOR | OTHER | UPSTREAM | SOW-039 Append-only HarnessEvent JSONL | ACTIVE |
| DEP-09-02-005 | ANCHOR | OTHER | UPSTREAM | SOW-045 SDK settings isolation | ACTIVE |
| DEP-09-02-006 | ANCHOR | OTHER | UPSTREAM | SOW-054 Structured permission decisions | ACTIVE |
| DEP-09-02-007 | ANCHOR | OTHER | UPSTREAM | SOW-057 Hooks and fail-closed behavior | ACTIVE |
| DEP-09-02-008 | ANCHOR | OTHER | UPSTREAM | SOW-063 Governed subagent runtime | ACTIVE |
| DEP-09-02-009 | ANCHOR | OTHER | UPSTREAM | OBJ-002 Product-owned runtime contracts | ACTIVE |
| DEP-09-02-010 | ANCHOR | OTHER | UPSTREAM | OBJ-003 Auditable Chirality-owned session records | ACTIVE |
| DEP-09-02-011 | ANCHOR | OTHER | UPSTREAM | OBJ-005 Capability-policy tool governance with explicit hard-deny precedence | ACTIVE |
| DEP-09-02-012 | ANCHOR | OTHER | UPSTREAM | OBJ-007 Agent-suite integrity and governed subagent delegation | ACTIVE |
| DEP-09-02-013 | ANCHOR | OTHER | UPSTREAM | OBJ-008 Explicit and repeatable validation and release checks | ACTIVE |
| DEP-09-02-014 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-09-01 Section 8 Harness Validation Preservation | ACTIVE |
| DEP-09-02-015 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-01 AgentEnginePort and Engine Conformance Suite | ACTIVE |
| DEP-09-02-016 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-03 SdkMessageMapper and Provider-Neutral Translation | ACTIVE |
| DEP-09-02-017 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-02 HarnessEvent Schema and Append-Only JSONL | ACTIVE |
| DEP-09-02-018 | EXECUTION | INTERFACE | UPSTREAM | DEL-04-02 SdkOptionsBuilder and Settings Isolation | ACTIVE |
| DEP-09-02-019 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-01 ChiralityPermissionOverlay and Mode Mapping | ACTIVE |
| DEP-09-02-020 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-03 Initial Chirality MCP Read Tools | ACTIVE |
| DEP-09-02-021 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-04 Write/Edit Surface and Path Hooks | ACTIVE |
| DEP-09-02-022 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-06 Hook Lifecycle and Compaction Mirror | ACTIVE |
| DEP-09-02-023 | EXECUTION | INTERFACE | UPSTREAM | DEL-05-05 ToolResultStore and Session Artifacts | ACTIVE |
| DEP-09-02-024 | EXECUTION | INTERFACE | UPSTREAM | DEL-08-04 Type 2 Subagent Governance Bridge | ACTIVE |
| DEP-09-02-025 | EXECUTION | INTERFACE | UPSTREAM | DEL-08-05 Subagent Child Run Records and Artifacts | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ActiveRows |
|---|---|---|---|---|---:|
| 2026-05-20T20:54:54-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` loaded | PRD_HASH_MISMATCH; TBD_SURFACES | 25 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 25 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 25 |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.
