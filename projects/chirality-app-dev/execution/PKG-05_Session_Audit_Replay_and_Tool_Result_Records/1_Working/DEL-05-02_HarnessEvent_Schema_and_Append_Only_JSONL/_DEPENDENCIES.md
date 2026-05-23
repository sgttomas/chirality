# Dependencies: DEL-05-02 HarnessEvent Schema and Append-Only JSONL

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
- TASK + dependency-extract ran on 2026-05-20 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Defaults used: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`, `EXECUTION_DOC_ORDER=AUTO` resolved to `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`, and existing `_DEPENDENCIES.md`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Human read boundary applied: `_STATUS.md` was not read because it was not in the allowed evidence list for dependency extraction.
- `[WARNING] REF-006_HASH_MISMATCH`: `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived details remain source-state-warning context.
- Parent anchor check passed: one ACTIVE `IMPLEMENTS_NODE` row is present.

## Extracted Dependency Register

Source register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 7 |

### Active Rows

| DependencyID | Class | Type | Target | Status |
|---|---|---|---|---|
| DEP-DEL-05-02-001 | ANCHOR | OTHER | PKG-05 Session Audit Replay and Tool Result Records | ACTIVE |
| DEP-DEL-05-02-002 | ANCHOR | OTHER | SOW-014 Persist accepted user input before execution | ACTIVE |
| DEP-DEL-05-02-003 | ANCHOR | OTHER | SOW-015 Persist terminal turn outcomes | ACTIVE |
| DEP-DEL-05-02-004 | ANCHOR | OTHER | SOW-039 Append-only HarnessEvent JSONL | ACTIVE |
| DEP-DEL-05-02-005 | ANCHOR | OTHER | OBJ-003 Make accepted turns SDK messages terminal outcomes tool activity and replay auditable through Chirality-owned session records | ACTIVE |
| DEP-DEL-05-02-006 | EXECUTION | INTERFACE | DEL-05-01 Canonical Session Folder and Legacy Session Migration | ACTIVE |
| DEP-DEL-05-02-007 | EXECUTION | INTERFACE | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | ACTIVE |
| DEP-DEL-05-02-008 | EXECUTION | ENABLES | DEL-05-04 Runtime Replay and Transcript View | ACTIVE |
| DEP-DEL-05-02-009 | EXECUTION | CONSTRAINT | DEL-05-03 Redacted RunLogger and Secret Hygiene | ACTIVE |
| DEP-DEL-05-02-010 | EXECUTION | INTERFACE | DEL-05-05 ToolResultStore and Session Artifacts | ACTIVE |
| DEP-DEL-05-02-011 | EXECUTION | INTERFACE | DEL-03-03 Harness API and SSE Compatibility Adapter | ACTIVE |
| DEP-DEL-05-02-012 | EXECUTION | INTERFACE | DEL-04-03 SdkMessageMapper and Provider-Neutral Translation | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:41:22-06:00 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used | REF-006_HASH_MISMATCH | 12 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 5 |
| TBD | 7 |
