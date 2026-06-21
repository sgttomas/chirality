# Dependencies: DEL-03-03 Harness API and SSE Compatibility Adapter

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

Source register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 5 |

### Active Rows

| DependencyID | Class | Type | Target | Status |
|---|---|---|---|---|
| DEP-03-03-001 | ANCHOR | OTHER | PKG-03 Runtime Engine Contract and Turn Lifecycle | ACTIVE |
| DEP-03-03-002 | ANCHOR | OTHER | SOW-011 SSE turn stream and session locking | ACTIVE |
| DEP-03-03-003 | ANCHOR | OTHER | SOW-040 UIEvent and HarnessEvent separation | ACTIVE |
| DEP-03-03-004 | ANCHOR | OTHER | OBJ-001 Preserve browser-facing harness experience | ACTIVE |
| DEP-03-03-005 | ANCHOR | OTHER | OBJ-002 Stabilize runtime contract and turn lifecycle | ACTIVE |
| DEP-03-03-006 | EXECUTION | INTERFACE | DOCUMENT RUNTIME_ENGINE_CONTRACT_TURN_ENGINE Runtime Engine Contract TurnEngine boundary | ACTIVE |
| DEP-03-03-007 | EXECUTION | INTERFACE | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | ACTIVE |
| DEP-03-03-008 | EXECUTION | INTERFACE | PKG-05 Session Audit Replay and Tool Result Records | ACTIVE |
| DEP-03-03-009 | EXECUTION | INTERFACE | DEL-04-03 SdkMessageMapper and Provider-Neutral Translation | ACTIVE |
| DEP-03-03-010 | EXECUTION | PREREQUISITE | Current implementation fixture capture | ACTIVE |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract ran on 2026-05-20 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Defaults used: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`, `EXECUTION_DOC_ORDER=AUTO` resolved to `Specification.md`, `Guidance.md`, `Procedure.md`, `_CONTEXT.md`, `_REFERENCES.md`, and existing `_DEPENDENCIES.md`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- `[RESOLVED] SOURCE_STATE`: D-APP-38 current authority-corpus reconciliation supersedes the prior REF-006 source-state warning; PRD-derived route/SSE details are accepted for this tranche.
- `[WARNING] TBD_FIXTURE_CAPTURE`: current implementation fixture capture is an explicit prerequisite but its target location and baseline SHA remain `TBD`.
- Parent anchor check passed: one ACTIVE `IMPLEMENTS_NODE` row is present.
- 2026-06-16 SCC-SAFE-MOVES-001 decomposed `DEP-03-03-006` from a coarse deliverable edge into document-scoped TurnEngine boundary evidence; the row remains active and in objective.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-06-21T03:00:20-06:00 | ADQ-05 | CONSERVATIVE | D-APP-38 current authority corpus and D-APP-40 runtime taxonomy applied | TBD_FIXTURE_CAPTURE | 10 |
| 2026-05-20T19:30:40-06:00 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used | superseded source-state warning; TBD_FIXTURE_CAPTURE | 10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 5 |
| TBD | 5 |
