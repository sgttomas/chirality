# Datasheet: DEL-02-01 Desktop Shell and Matrix Navigation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

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
| Primary surface | Loop-first desktop shell navigation: PORTAL as the primary header entry, with WORKBENCH and PIPELINE reachable as right-sidebar tertiary forms and preserved deep links | REF-006 `docs/PRD.md` Section 8.1 FR-001; decomposition DEL-02-01; D-APP-28/D-APP-31/D-APP-32 |
| Matrix shape | 3 rows by 4 columns | REF-006 Section 8.2 FR-007; REF-004 `docs/TYPES.md` Section 4.3 |
| Matrix rows | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE` | REF-006 Section 8.2 FR-007; REF-004 Section 4.1 |
| Matrix columns | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING` | REF-006 Section 8.2 FR-007; REF-004 Section 4.2 |
| NORMATIVE destination | Mounted live-loop persona context | REF-004 Section 4.1; REF-006 Section 7.2; D-APP-28/D-APP-30 |
| OPERATIVE destination | PIPELINE sidebar/deep-link intent | REF-004 Section 4.1; REF-006 Section 7.2; D-APP-28/D-APP-31 |
| EVALUATIVE destination | Mounted live-loop persona context | REF-004 Section 4.1; REF-006 Section 7.2; D-APP-28/D-APP-30 |
| Shell routes | `/` is the primary header entry; `/pipeline` and `/workbench` are preserved deep-link route entries that open right-sidebar tertiary forms | REF-006 Section 8.1 FR-001; D-APP-28/D-APP-31/D-APP-32 |
| Active route indication | Required for rendered primary header links; Workbench/Pipeline active context is sidebar-tab state | REF-006 Section 8.1 FR-001; D-APP-28 |
| Anticipated artifacts | Navigation components; matrix UI tests; route query handling; AMD-01 render tests | `_CONTEXT.md`; decomposition DEL-02-01; D-APP-36 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Scope items covered | SOW-001, SOW-005 | `_CONTEXT.md`; decomposition SSOW and traceability |
| Objective supported | OBJ-001 | `_CONTEXT.md`; decomposition objective mapping |
| Inclusions | UI and operator workflow behavior | `_CONTEXT.md`; decomposition PKG-02 package row |
| Exclusions | Runtime engine internals | `_CONTEXT.md`; decomposition PKG-02 package row |
| PRD source status | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; dispatch instruction — reconciled under D-APP-38 |
| Dependency extraction | Deferred; `Dependencies.csv` not produced in this run | Dispatch instruction; `_DEPENDENCIES.md` initial population rule |

## Construction

| Item | Required Construction Detail | Source |
|---|---|---|
| Header/navigation | Must expose PORTAL in primary header navigation and preserve `/pipeline` and `/workbench` as loop-first deep-link route entries | REF-006 Section 8.1 FR-001; D-APP-28/D-APP-31/D-APP-32 |
| PORTAL matrix | Must render canonical rows and columns | REF-006 Section 8.2 FR-007; REF-004 Section 4 |
| Matrix cell routing | Must route NORMATIVE and EVALUATIVE cells to mounted live-loop persona context and OPERATIVE cells to PIPELINE intent | REF-006 Section 8.2 FR-008; REF-004 Section 4.1; D-APP-28/D-APP-30/D-APP-31 |
| Route state | Current implementation evidence uses `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` keys; older source text does not independently name all keys | `_CONTEXT.md`; ADQ-13 implementation evidence |
| Tests | Matrix, route wrapper, sidebar, and disabled-state render tests are recorded under ADQ-13 | `_CONTEXT.md`; D-APP-36; ADQ-13 evidence |

## References

| RefID | Source Used | Relevant Slice |
|---|---|---|
| REF-004 | `docs/TYPES.md` | Section 4 UI Navigation Vocabulary |
| REF-006 | `docs/PRD.md` | Sections 7.2, 8.1, 8.2, and package mapping |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | SOW-001, SOW-005, OBJ-001, PKG-02, DEL-02-01 |
| LOCAL | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` | Deliverable identity, source status, and dependency deferral |

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-105 supersedes run-scoped dependency-extraction deferral wording: the extracted register exists and is live. UPD-106 is implemented by the governed PORTAL active-link render test.
