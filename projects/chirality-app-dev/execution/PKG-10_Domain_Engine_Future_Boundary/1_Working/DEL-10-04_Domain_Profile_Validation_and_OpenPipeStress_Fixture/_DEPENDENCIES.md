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
- 2026-07-10 D-APP-53 reconciliation (plan DRQ-09; authority `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`, Option A): rows re-verified against the live tree. Closed `PENDING -> SATISFIED`: DEP-10-04-001/-002/-003 (anchors live in decomposition) and -005 (source corpus REF-002..REF-006 all `MATCH` in `_REFERENCES.md`). Annotate-only per plan §3.5, stay PENDING: DEP-10-04-004 (accepted PKG-10 amendment — owner call; D-APP-50/51/52 and D-T0-06 exist but their amendment status is not this loop's to rule; F-APP-3 reaffirmed) and DEP-10-04-006 (ResponsibleParty — owner act; still TBD in `_CONTEXT.md`/`Datasheet.md`). Left open with reasons: DEP-10-04-007 (test paths now exist but no source assigns a domain-engine adapter manifest location) and DEP-10-04-008 (fresh FULL_GRAPH DepClosure snapshot over the reconciled registers pending plan DRQ-11). Dated corrections: the 2026-05-20 `SOURCE_HASH_MISMATCH` warning is resolved — `_REFERENCES.md` line 12 now records REF-006 `docs/PRD.md` Status MATCH (SHA `ac35fba4...`); `TEST_PATH_TBD` is now partial (tests exist, manifest location does not). See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. No lifecycle transition (F-APP-4).

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-10-04-001 | ANCHOR | OTHER | UPSTREAM | PKG-10 Domain Engine Future Boundary | ACTIVE |
| DEP-10-04-002 | ANCHOR | OTHER | UPSTREAM | SOW-070 OpenPipeStress fixture profile | ACTIVE |
| DEP-10-04-003 | ANCHOR | OTHER | UPSTREAM | OBJ-010 Future domain-engine boundary objective | ACTIVE |
| DEP-10-04-004 | EXECUTION | CONSTRAINT | UPSTREAM | Accepted PKG-10 amendment or explicit human authorization | ACTIVE |
| DEP-10-04-005 | EXECUTION | PREREQUISITE | UPSTREAM | Accessible source corpus for domain profile validation | ACTIVE |
| DEP-10-04-006 | EXECUTION | PREREQUISITE | UPSTREAM | ResponsibleParty assignment | ACTIVE |
| DEP-10-04-007 | EXECUTION | PREREQUISITE | UPSTREAM | Concrete future test path and adapter manifest location | ACTIVE |
| DEP-10-04-008 | EXECUTION | PREREQUISITE | UPSTREAM | Dependency extraction and project graph validation | ACTIVE |

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
| `SatisfactionStatus=SATISFIED` | 4 |
| `SatisfactionStatus=PENDING` | 4 |

Closure state: dependency register schema is present and all extracted rows are ACTIVE; satisfaction remains `PENDING` until future amendment, ownership assignment, concrete test/manifest paths, and downstream graph validation are accepted or waived.

Closure state update (2026-07-10, D-APP-53 reconciliation; previously `PENDING` 8): anchors and the source-corpus prerequisite are SATISFIED on live evidence. The four remaining PENDING rows are the owner-gated amendment (DEP-10-04-004), the owner ResponsibleParty act (DEP-10-04-006), the unassigned adapter-manifest location (DEP-10-04-007), and the DRQ-11 fresh FULL_GRAPH snapshot (DEP-10-04-008).

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T21:07:24-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOURCE_HASH_MISMATCH; FUTURE_AMENDMENT_TBD; RESPONSIBLE_PARTY_TBD; TEST_PATH_TBD; PROJECT_GRAPH_VALIDATION_TBD | ANCHOR=3; EXECUTION=5; TOTAL=8 |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | located; anchors re-verified | 4 rows SATISFIED; -004/-006 annotate-only (owner-gated); -007/-008 left open with reasons; SOURCE_HASH_MISMATCH resolved (REF-006 MATCH); linter PASS 0/0 | ANCHOR=3; EXECUTION=5; TOTAL=8 |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-157
- **Current counts:** ACTIVE 8; RETIRED 0; PENDING=3; SATISFIED=5.
- **Correction:** DEP-10-04-008 is SATISFIED against D53A; four prior PENDING rows are now three.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
- **2026-07-16 (D-APP-58):** DEP-10-04-007 is SATISFIED — docs/SPEC.md §18 now assigns the adapter-manifest location convention `_DomainEngines/profiles/<profileId>.adapter.yaml` / `domain-engine-adapter-manifest/v1` (agent selection under owner-delegated latitude; ruling record `execution/_Coordination/_DECISIONS/D-APP-58_RULING_2026-07-16.md`); the four test paths stand per D-APP-53. Manifest instances do not yet exist and remain engine-side/bridge future scope. Three prior PENDING rows are now two (DEP-10-04-004, DEP-10-04-006 — both owner acts).
