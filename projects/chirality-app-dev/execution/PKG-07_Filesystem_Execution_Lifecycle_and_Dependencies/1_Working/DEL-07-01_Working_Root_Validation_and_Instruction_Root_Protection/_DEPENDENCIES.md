# Dependencies: DEL-07-01 Working Root Validation and Instruction Root Protection

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
- 2026-05-20 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Decomposition authority used: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; status: located and used for anchor validation.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- [RESOLVED 2026-07-12] REF-006 docs/PRD.md is MATCH under D-APP-38; the mismatch warning remains only in dated 2026-05-20 run history.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor is present.
- No `[WARNING] MISSING_DECOMPOSITION`: the explicit decomposition path was available.
- Conservative exclusion: no dependency edge was emitted for `DEL-06-04`; `Guidance.md` identifies the relationship as an inferred coordination note, not an accepted dependency edge.

## Extracted Dependency Register

| DependencyID | Class | Type | Target | Status | Evidence |
|---|---|---|---|---|---|
| DEP-07-01-001 | ANCHOR | OTHER / IMPLEMENTS_NODE | DEL-07-01 Working Root Validation and Instruction Root Protection | ACTIVE | `Datasheet.md`; decomposition DEL-07-01 row |
| DEP-07-01-002 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-002 Working-root selection and validation | ACTIVE | `_CONTEXT.md`; decomposition SOW ledger |
| DEP-07-01-003 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-027 Path containment and instruction-root protection | ACTIVE | `_CONTEXT.md`; decomposition SOW ledger |
| DEP-07-01-004 | EXECUTION | CONSTRAINT | REF-006 `docs/PRD.md` reference state MATCH | RETIRED | `_REFERENCES.md` |
| DEP-07-01-005 | EXECUTION | PREREQUISITE | UNKNOWN code module locations for implementation | ACTIVE | `Specification.md`; `Procedure.md` |

## Lifecycle Summary

| Metric | Count |
|---|---:|
| ACTIVE rows | 4 |
| RETIRED rows | 1 |
| ANCHOR rows | 3 |
| EXECUTION rows | 2 |
| Satisfaction `NOT_APPLICABLE` | 3 |
| Satisfaction `TBD` | 1 |

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20T19:47:21-0600 | UPDATE | CONSERVATIVE | located | 5 | SOURCE_HASH_MISMATCH |

## D-APP-56 R5 P40 register annotation (2026-07-12)

REF-006 is MATCH under D-APP-38. Any HASH_MISMATCH token retained in the dated Run History is extraction provenance, not current dependency state. Structured-row status and summary counts above reflect Dependencies.csv after UPD-077..079.

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-130
- **Current counts:** ACTIVE 4; RETIRED 1; NOT_APPLICABLE=4; SATISFIED=1.
- **Correction:** DEP-07-01-005 resolves to landed implementation modules and is SATISFIED.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
