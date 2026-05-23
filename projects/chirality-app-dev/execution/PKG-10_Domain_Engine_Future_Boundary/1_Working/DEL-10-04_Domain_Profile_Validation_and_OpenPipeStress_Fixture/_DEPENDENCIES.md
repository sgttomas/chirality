# Dependencies: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

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
- 2026-05-20 dependency-extract run:
  - Runtime overrides: `SCOPE=DEL-10-04`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
  - Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located and used.
  - Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority.
  - `ANCHOR_DOC=AUTO` resolved to `Datasheet.md`; execution docs were read as `Procedure.md`, `Specification.md`, `Guidance.md`, `_CONTEXT.md`, `_REFERENCES.md`.
  - Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed as evidence.
  - PKG-10 future-boundary/gated posture preserved; no current-release domain-engine work or implementation dependency was activated.
  - Existing declared dependency lists remain `TBD`; no declared edges were promoted without evidence.
  - `[WARNING] SOURCE_HASH_MISMATCH`: `_REFERENCES.md` reports `docs/PRD.md` REF-006 as `HASH_MISMATCH`; this run preserved the warning and used only the allowed local derivative documents plus decomposition authority.
  - `[WARNING] FUTURE_AMENDMENT_TBD`: accepted PKG-10 amendment or explicit human authorization remains a required upstream gate.
  - `[WARNING] RESPONSIBLE_PARTY_TBD`: `ResponsibleParty` remains `TBD`.
  - `[WARNING] TEST_PATH_TBD`: concrete future test path and adapter manifest location remain `TBD`.
  - `[WARNING] PROJECT_GRAPH_VALIDATION_TBD`: project-level FULL_GRAPH validation remains pending after local register creation.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEL-10-04-DEP-001 | ANCHOR | OTHER | UPSTREAM | PKG-10 Domain Engine Future Boundary | ACTIVE |
| DEL-10-04-DEP-002 | ANCHOR | OTHER | UPSTREAM | SOW-070 OpenPipeStress fixture profile | ACTIVE |
| DEL-10-04-DEP-003 | ANCHOR | OTHER | UPSTREAM | OBJ-010 Future domain-engine boundary objective | ACTIVE |
| DEL-10-04-DEP-004 | EXECUTION | CONSTRAINT | UPSTREAM | Accepted PKG-10 amendment or explicit human authorization | ACTIVE |
| DEL-10-04-DEP-005 | EXECUTION | PREREQUISITE | UPSTREAM | Accessible source corpus for domain profile validation | ACTIVE |
| DEL-10-04-DEP-006 | EXECUTION | PREREQUISITE | UPSTREAM | ResponsibleParty assignment | ACTIVE |
| DEL-10-04-DEP-007 | EXECUTION | PREREQUISITE | UPSTREAM | Concrete future test path and adapter manifest location | ACTIVE |
| DEL-10-04-DEP-008 | EXECUTION | PREREQUISITE | UPSTREAM | Dependency extraction and project graph validation | ACTIVE |

## Lifecycle Summary

| Metric | Count |
|---|---:|
| Total rows | 8 |
| ACTIVE rows | 8 |
| RETIRED rows | 0 |
| ANCHOR rows | 3 |
| EXECUTION rows | 5 |
| OTHER rows | 3 |
| CONSTRAINT rows | 1 |
| PREREQUISITE rows | 4 |
| `SatisfactionStatus=PENDING` | 8 |

Closure state: dependency register schema is present and all extracted rows are ACTIVE; satisfaction remains `PENDING` until future amendment, ownership assignment, concrete test/manifest paths, and downstream graph validation are accepted or waived.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T21:07:24-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH; FUTURE_AMENDMENT_TBD; RESPONSIBLE_PARTY_TBD; TEST_PATH_TBD; PROJECT_GRAPH_VALIDATION_TBD | ANCHOR=3; EXECUTION=5; TOTAL=8 |
