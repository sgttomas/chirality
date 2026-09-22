# Dependencies: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

See the current formal `Dependencies.csv` rows whose Direction is UPSTREAM; satisfaction and gates are read from that register, not inferred here.

## Declared Downstream

See the current formal `Dependencies.csv` rows whose Direction is DOWNSTREAM. No new dependency or status is created by this descriptive mirror.

## Current Extracted Dependency Summary — 2026-09-22

Total rows: 10. ACTIVE: 9, RETIRED: 1.

| DependencyID | Class | Type | Direction | Target | Status | SatisfactionStatus |
|---|---|---|---|---|---|---|
| DEP-03-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-03 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-012 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-003 | ANCHOR | OTHER | UPSTREAM | SOW-015 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-004 | ANCHOR | OTHER | UPSTREAM | OBJ-002 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-005 | ANCHOR | OTHER | UPSTREAM | OBJ-003 | ACTIVE | NOT_APPLICABLE |
| DEP-03-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-03-01 | ACTIVE | TBD |
| DEP-03-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-03-02 | ACTIVE | TBD |
| DEP-03-04-008 | EXECUTION | INTERFACE | UPSTREAM | DEL-03-03 | RETIRED | NOT_APPLICABLE |
| DEP-03-04-009 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-05-02 | ACTIVE | TBD |
| DEP-03-04-010 | EXECUTION | CONSTRAINT | UPSTREAM | DEL-03-04-CONFLICT-001 | ACTIVE | SATISFIED |

This is a read-only summary of formal rows. D-GOV-43/D-APP-127 adapt current Runtime ownership and retire daemon proof subjects; formal row amendments, satisfaction changes and basis pins retain their owning process. Earlier notes below remain historical and do not override this current summary.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- This run used only `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read and is not evidence for this register.
- Chosen anchor document: `Datasheet.md` plus `_CONTEXT.md` identity/traceability fields.
- Chosen execution document order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used for PKG, SOW, objective, and deliverable target labels.
- `[RESOLVED] AUTHORITY_CORPUS_APPLIED`: REF-006 is reconciled under the current D-APP-38 authority corpus.
- `[WARNING] ASSUMPTION_EDGES`: DEP-03-04-006 through DEP-03-04-009 are explicit in `Procedure.md` but assumption-labeled there; they remain `Confidence=LOW` and `SatisfactionStatus=TBD`.
- `[RESOLVED] HUMAN_RULING_APPLIED`: DEP-03-04-010 is satisfied by D-APP-40 Option B; explicit user interruption persists `turn.interrupted`, while `turn.cancelled` is reserved for non-user cancellation.
- Parent anchor check: PASS, exactly one ACTIVE `IMPLEMENTS_NODE` anchor.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:35:54-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | superseded source-state warning; ASSUMPTION_EDGES; superseded human-ruling request | 10 |
| 2026-06-21T02:53:33-06:00 | ADQ-05 | CONSERVATIVE | `execution/_Coordination/_DECISIONS/D-APP-40_RULING_2026-06-21.md` | ASSUMPTION_EDGES; HUMAN_RULING_APPLIED | 10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 5 |
| SATISFIED | 1 |
| TBD | 4 |

## Current evidence-locator refresh — 2026-09-22

4 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.
