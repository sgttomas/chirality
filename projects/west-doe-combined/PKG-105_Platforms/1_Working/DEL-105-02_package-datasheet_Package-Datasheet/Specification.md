# Specification — DEL-105-02 Package Datasheet (PKG-105 Platforms)

> Normative requirements for the Package Datasheet artifact that the EPC Integrator hands to third-party vendor/discipline engineering for the Structural Platforms package (PKG-105, Workbook row 106).

## Scope

**Covers.** This Specification governs the content, structure, and source-fidelity of the **Package Datasheet** deliverable for `PKG-105 Platforms`. It applies to the datasheet's identification block, technical attributes, design/loading conditions, construction basis, interface requirements matrix, vendor engineering handoff basis, and associated interface-fact evidence.

**Excludes.**
- Authoring of the EPC Scope of Work itself (handled by `DEL-105-01_scope-of-work`).
- Construction work package content (handled by `DEL-105-03_construction-work-package`).
- Detailed structural design/calculations and discipline production drawings (handled by `DEL-105-04_epc-structural-discipline-production-package`).
- Authoring or modifying upstream decomposition records, interface register entries, or scope-ledger rows.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| R-1 | The datasheet SHALL identify the package by `PKG-105`, name "Platforms", workbook row 106, WBS 01, discipline Structural, and Responsible Party "EPC Integrator". | `PACKAGE_REGISTER.csv`; `DELIVERABLE_REGISTER.csv` |
| R-2 | The datasheet SHALL include the workbook-derived package function statement (Structural platforms package for WBS 01 per SOW-0261). | `SCOPE_LEDGER.csv` SOW-0261 |
| R-3 | The datasheet SHALL cite governing civil/structural codes: NBC Canada, CAN/CSA-S16, CAN/CSA A23.3, Canadian Foundation Engineering Manual, CSA G40.20/G40.21 (350W/300W), CSA A23.1/A23.2. | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Governing Civil and Structural Basis |
| R-4 | The datasheet SHALL state foundation basis as driven steel piles unless detailed engineering establishes otherwise. | DBM SEC-11 §Piles and Foundations |
| R-5 | The datasheet SHALL state that geotechnical parameters (bearing capacity, LPILE curves, dynamic design criteria, pavement) are TBD pending the geotechnical assessment report. | DBM SEC-11 §Geotechnical and Topographical Assumptions |
| R-6 | The datasheet SHALL include the Package Interface Requirements Matrix listing the three workbook interface facts: IFC-26E3DCAD56 (Area/Exterior Lighting), IFC-07C472C58B (Grading/Site Drainage/Spill Containment), IFC-B7C0A01E38 (Structural/Foundations/Supports), each with applicability and disposition. | `INTERFACE_REGISTER.csv` |
| R-7 | The datasheet SHALL record the Gate 6 disposition that platform-to-equipment tie-ins are the EPC Integrator's responsibility via the overall 3D model and integrated P&ID set. | `ARTIFACT_REGISTER.csv` (ART-39021CDFB3 / ART-217A830349 / ART-1FA7F21048 / ART-749A9EEC06 Notes); `INTERFACE_REGISTER.csv` Notes |
| R-8 | Each non-trivial value in the datasheet SHALL cite its source (file + section) or be marked `TBD` with the missing source named. | Authority hierarchy; K-PROV-1 |
| R-9 | Inferences and best-effort associations (including the objective→package mapping for OBJ-001/005/008/010) SHALL be labeled **ASSUMPTION**. | `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC mode) |
| R-10 | The datasheet SHALL preserve the anticipated artifact set: package technical datasheet, vendor engineering handoff basis, package interface requirements matrix, source-supported equipment and design criteria. | `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts |
| R-11 | The datasheet SHALL NOT invent values for tagged equipment, platform counts, geometry, or materials not present in accessible source slices. | Skill non-negotiable: "Source-anchored with explicit assumptions" |
| R-12 | The datasheet SHALL identify the Vendor Engineering Handoff Basis content (technical basis, battery limits, design expectations, source-supported requirements) and mark unresolved items TBD. | `ARTIFACT_REGISTER.csv` ART-EA98D39386 |

## Standards

| Standard / Code | Role | Location |
|---|---|---|
| National Building Code of Canada (latest edition) | Building / loading basis | DBM SEC-11 §Governing Civil and Structural Basis |
| CAN/CSA-S16 — Design of Steel Structures | Steel design code | DBM SEC-11 §Governing Civil and Structural Basis |
| CAN/CSA A23.3 — Design of Concrete Structures | Concrete design code | DBM SEC-11 §Governing Civil and Structural Basis |
| Canadian Foundation Engineering Manual | Foundation engineering reference | DBM SEC-11 §Governing Civil and Structural Basis |
| CSA G40.20 / G40.21 (350W; 300W) | Structural steel materials | DBM SEC-11 §Governing Civil and Structural Basis |
| CSA A23.1 / A23.2 | Concrete materials / construction / testing | DBM SEC-11 §Governing Civil and Structural Basis |
| Workbook row 106 (CoA 26020-01-36-005) | Package identity / interface authority | `PACKAGE_REGISTER.csv` (raw workbook slice: location TBD) |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-1 | Cross-check datasheet identification block against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. |
| R-2 | Cross-check function statement against `SCOPE_LEDGER.csv` SOW-0261 wording. |
| R-3, R-4, R-5 | Cite-check against DBM SEC-11 source slices; each cited basis row matches DBM table or paragraph. |
| R-6 | Verify the three IFC rows appear with exact IDs, types, and applicability from `INTERFACE_REGISTER.csv`. |
| R-7 | Verify Gate 6 disposition wording matches `ARTIFACT_REGISTER.csv` Notes for the four interface-fact / disposition artifacts. |
| R-8, R-9, R-11 | QA review for source citations, ASSUMPTION/TBD labeling, and absence of invented values. |
| R-10 | Confirm anticipated artifact set listed in datasheet matches `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts. |
| R-12 | Confirm vendor handoff basis section identifies the four content categories and marks unresolved items TBD. |

## Documentation

Required artifacts produced by or alongside this datasheet:

- `Datasheet.md` (this deliverable's primary artifact)
- Package Interface Requirements Matrix (table within `Datasheet.md`)
- Vendor Engineering Handoff Basis section (within `Datasheet.md`)
- Interface-fact evidence rows mapped to ART-39021CDFB3, ART-217A830349, ART-1FA7F21048, ART-749A9EEC06
- Source-supported equipment and design-criteria entries (TBD where source-limited)
