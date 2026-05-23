# Datasheet: DEL-02-01 Desktop Shell and Matrix Navigation

## Identification

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| PackageID | PKG-02 |
| PackageName | Desktop Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-01 |
| DeliverableName | Desktop Shell and Matrix Navigation |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | M |
| Current State at P1/P2 authoring | OPEN |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary surface | Desktop shell navigation for PORTAL, PIPELINE, and WORKBENCH | REF-006 `docs/PRD.md` Section 8.1 FR-001; decomposition DEL-02-01 |
| Matrix shape | 3 rows by 4 columns | REF-006 Section 8.2 FR-007; REF-004 `docs/TYPES.md` Section 4.3 |
| Matrix rows | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE` | REF-006 Section 8.2 FR-007; REF-004 Section 4.1 |
| Matrix columns | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING` | REF-006 Section 8.2 FR-007; REF-004 Section 4.2 |
| NORMATIVE destination | WORKBENCH | REF-004 Section 4.1; REF-006 Section 7.2 |
| OPERATIVE destination | PIPELINE | REF-004 Section 4.1; REF-006 Section 7.2 |
| EVALUATIVE destination | WORKBENCH | REF-004 Section 4.1; REF-006 Section 7.2 |
| Shell routes | `/`, `/pipeline`, `/workbench` | REF-006 Section 8.1 FR-001 |
| Active route indication | Required | REF-006 Section 8.1 FR-001 |
| Anticipated artifacts | Navigation components; matrix UI tests; route query handling | `_CONTEXT.md`; decomposition DEL-02-01 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Scope items covered | SOW-001, SOW-005 | `_CONTEXT.md`; decomposition SSOW and traceability |
| Objective supported | OBJ-001 | `_CONTEXT.md`; decomposition objective mapping |
| Inclusions | UI and operator workflow behavior | `_CONTEXT.md`; decomposition PKG-02 package row |
| Exclusions | Runtime engine internals | `_CONTEXT.md`; decomposition PKG-02 package row |
| PRD source status | `HASH_MISMATCH` observed and treated as source warning per dispatch | `_REFERENCES.md`; dispatch instruction |
| Dependency extraction | Deferred; `Dependencies.csv` not produced in this run | Dispatch instruction; `_DEPENDENCIES.md` initial population rule |

## Construction

| Item | Required Construction Detail | Source |
|---|---|---|
| Header navigation | Must route to PORTAL, PIPELINE, and WORKBENCH via `/`, `/pipeline`, and `/workbench` | REF-006 Section 8.1 FR-001 |
| PORTAL matrix | Must render canonical rows and columns | REF-006 Section 8.2 FR-007; REF-004 Section 4 |
| Matrix cell routing | Must route NORMATIVE and EVALUATIVE cells to WORKBENCH and OPERATIVE cells to PIPELINE | REF-006 Section 8.2 FR-008; REF-004 Section 4.1 |
| Route state | Query handling is anticipated; exact query parameter names are TBD for this deliverable because source text does not define them here | `_CONTEXT.md`; unsupported detail marked TBD |
| Tests | Matrix UI tests are anticipated; exact test framework and fixture names are TBD | `_CONTEXT.md`; unsupported detail marked TBD |

## References

| RefID | Source Used | Relevant Slice |
|---|---|---|
| REF-004 | `docs/TYPES.md` | Section 4 UI Navigation Vocabulary |
| REF-006 | `docs/PRD.md` | Sections 7.2, 8.1, 8.2, and package mapping |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOW-001, SOW-005, OBJ-001, PKG-02, DEL-02-01 |
| LOCAL | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` | Deliverable identity, source status, and dependency deferral |
