# Specification: DEL-102-04 — EPC / Structural Discipline Production Package

## Scope

**In scope.** Establish the EPC Integrator (or assigned discipline subcontractor) structural discipline production unit for the non-vendor scope of PKG-102 (Monolithic concrete foundations), WBS 01. The deliverable carries forward the workbook-defined package basis and Deepcut DBM support material into a discipline production package suitable for downstream structural engineering, design, procurement, and construction handoff.

Source: `DELIVERABLE_REGISTER.csv` row DEL-102-04; `PACKAGE_REGISTER.csv` PKG-102.

**Out of scope / boundary.**
- Vendor-engineered equipment package activities (PKG-102 has no separate vendor-package ownership model per `PACKAGE_REGISTER.csv`).
- EPC Scope of Work narrative (DEL-102-01), Package Datasheet (DEL-102-02), and Construction Work Package (DEL-102-03) which are sibling deliverables.
- Detailed structural design clauses; these are explicitly source-limited and remain open for Gate 5 disposition (`_CONTEXT.md` Notes; `ARTIFACT_REGISTER.csv` ART-712FAD4E91).

## Requirements

The following are the source-supported requirements for this production unit. Items not directly evidenced by accessible sources are marked **TBD** or **ASSUMPTION** and must not be treated as binding without human ruling.

| ReqID | Requirement | Source / Label |
|---|---|---|
| R-01 | The production unit shall cover the non-vendor structural scope of the workbook-defined PKG-102 'Monolithic concrete foundations' under WBS 01. | `DELIVERABLE_REGISTER.csv` row DEL-102-04 |
| R-02 | The production unit shall carry conservatively from the workbook (row 103) and from Deepcut DBM support material; it shall not invent design content that is not source-supported. | `DELIVERABLE_REGISTER.csv` row DEL-102-04; `PACKAGE_REGISTER.csv` PKG-102 SourceRefs |
| R-03 | The production unit shall produce a discipline production package basis artifact (ART-5C2432867E). | `ARTIFACT_REGISTER.csv` ART-5C2432867E |
| R-04 | The production unit shall produce a TBD discipline deliverable register listing the structural sub-deliverables anticipated for full execution. | `DELIVERABLE_REGISTER.csv` row DEL-102-04 AnticipatedArtifacts; `_CONTEXT.md` |
| R-05 | The production unit shall produce a source-limited requirements closure record (ART-712FAD4E91) that explicitly enumerates the gaps remaining for Gate 5 disposition. | `ARTIFACT_REGISTER.csv` ART-712FAD4E91 |
| R-06 | The production unit shall respect the recorded PKG-102 physical interface set: Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv` IFC-1EDEDC0453, IFC-8283744B5B; `PACKAGE_REGISTER.csv` PKG-102 InterfaceTypes |
| R-07 | Responsibility assignment (EPC Integrator vs. discipline subcontractor) shall be confirmed by human assignment; the source set does not predetermine the responsibility model. | `PACKAGE_REGISTER.csv` PKG-102 ResponsibilityModel; `_CONTEXT.md` (ASSUMPTION until human-confirmed) |
| R-08 | The production unit shall trace to scope item SOW-0258 and shall record support for objectives OBJ-001 and OBJ-008 (best-effort PACKAGE_HEURISTIC mapping; ASSUMPTION). | `DELIVERABLE_REGISTER.csv` row DEL-102-04 |
| R-09 | Detailed structural design requirements (loads, materials, geometry, code references, design criteria) — **TBD**, location TBD; not present in the locally accessible source set. | `_CONTEXT.md` Notes; `ARTIFACT_REGISTER.csv` ART-712FAD4E91 |

## Standards

- Governing structural design codes for monolithic concrete foundations — **TBD**, location TBD. The locally accessible source set (decomposition registers, `_REFERENCES.md`) does not enumerate governing structural codes for PKG-102. Candidate standards (e.g., concrete design codes, foundation design codes) are **ASSUMPTION: likely applicable**; clause-level requirements shall not be derived until source slices are accessible.
- Project workbook (`26020-Package_Requirements.docx`, row 103) — referenced authoritatively by the decomposition but the underlying slice is not copied to the deliverable folder (`_REFERENCES.md` Missing/Deferred). Location: TBD.
- DBM-Deepcut/4-25_Deepcut_DBM.md — referenced authoritatively by `PACKAGE_REGISTER.csv` PKG-102 SourceRefs; underlying slice not copied. Location: TBD.

## Verification

| ReqID | Verification Approach |
|---|---|
| R-01 | Documented scope statement in the production package basis cross-checks `DELIVERABLE_REGISTER.csv` row DEL-102-04. |
| R-02 | Source-traceability table in the production package basis cites only workbook row 103 and DBM-Deepcut entries; absence of unsourced content audited. |
| R-03 | ART-5C2432867E artifact produced and registered. |
| R-04 | Discipline deliverable register exists and is marked `TBD-Detailed` where source-limited. |
| R-05 | Source-limited requirements closure record (ART-712FAD4E91) lists every gap with provenance and disposition route. |
| R-06 | Interface matrix in the production package basis matches `INTERFACE_REGISTER.csv` PKG-102 rows. |
| R-07 | Responsibility assignment confirmed in writing by the human authority (PMO/EPC Integrator). |
| R-08 | Scope item and objective trace recorded; ASSUMPTION label preserved until human ruling. |
| R-09 | Closed when source slices become locally accessible; otherwise remains TBD with explicit gap entry. |

## Documentation

Anticipated artifacts (from `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row DEL-102-04 / `ARTIFACT_REGISTER.csv` PKG-102 DEL-102-04 rows):

- Discipline production package basis (ART-5C2432867E)
- TBD discipline deliverable register
- Source-limited requirements closure record (ART-712FAD4E91)
