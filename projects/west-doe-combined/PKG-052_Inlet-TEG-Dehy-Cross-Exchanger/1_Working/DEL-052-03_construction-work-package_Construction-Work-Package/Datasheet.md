# Datasheet — DEL-052-03 Construction Work Package (Inlet / TEG Dehy Cross Exchanger)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-052-03_construction-work-package | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | PKG-052 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-052 |
| PackageName | Inlet / TEG Dehy Cross Exchanger | `PACKAGE_REGISTER.csv` row PKG-052 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` row PKG-052 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row PKG-052 |
| Workbook Source | Workbook Packages row 62 | `DELIVERABLE_REGISTER.csv` row DEL-052-03 |
| Type | EPC Construction Work Package | `DELIVERABLE_REGISTER.csv` row DEL-052-03 |
| ResponsibleParty | EPC Integrator | `DELIVERABLE_REGISTER.csv` row DEL-052-03 |
| Covers Scope Items | SOW-0103, SOW-0104, SOW-0105, SOW-0106 | `SCOPE_LEDGER.csv` rows SOW-0103..SOW-0106; `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `DELIVERABLE_REGISTER.csv` row DEL-052-03 (ASSUMPTION: package-heuristic mapping) |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_CONTEXT.md`; `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Cold sour gas from the inlet separator flows to the TEG heat exchanger, where it exchanges heat with sweet gas leaving the amine sweetening unit; the sour gas then flows to the inlet compressors. | `SCOPE_LEDGER.csv` SOW-0104; `PACKAGE_REGISTER.csv` PKG-052 Description |
| Vendor / EPC Split | Package Vendor owns package engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. | `PACKAGE_REGISTER.csv` PKG-052 ResponsibilityModel |
| Applicable Interfaces (9) | Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-052 (9 rows, all Applicable=YES) |
| Package Exclusions | TBD — no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` PKG-052 Exclusions ("TBD; no package-specific exclusions stated in source materials.") |
| By Others (construction-relevant) | Interconnecting piping, DCS integration, foundations, electrical supply to MCC. | `SCOPE_LEDGER.csv` SOW-0106 (Scope notes and open items) |
| Tagged Equipment | E-5718-1 — Inlet / TEG DEHY Cross Exchanger (1x); TEMA 'R' BEM, bonnet front-end stationary head, one-pass shell, fixed tube-sheet rear-end head. | `SCOPE_LEDGER.csv` SOW-0105; `PACKAGE_REGISTER.csv` PKG-052 ScopeStatement |
| Tracking Number | 26020-01-PT-16-001 — Inlet TEG Cross Exchanger | `PACKAGE_REGISTER.csv` PKG-052 (tracking number column) |
| Sour Service Applicability | Applies — sour gas service stated in process function (cold sour gas inlet). | `SCOPE_LEDGER.csv` SOW-0104; `OBJECTIVE_REGISTER.csv` OBJ-009 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / Facility | 04-25 Deepcut facility, WBS 01 | `OBJECTIVE_REGISTER.csv` OBJ-001; `PACKAGE_REGISTER.csv` PKG-052 |
| Heat Duty | 5514.3 kW (18.82 MMBTU/hr) | `SCOPE_LEDGER.csv` SOW-0105, SOW-0106; `PACKAGE_REGISTER.csv` PKG-052 ScopeStatement |
| Sour Gas Side Flow (treated) | ~4480.28 m³/hr (units as stated in source; note SOW-0106 records "m6/hr" which is presumed a transcription artifact — flagged TBD for reconciliation against source slice) | `SCOPE_LEDGER.csv` SOW-0106 |
| Sweet Gas Side Flow | ~7236.64 m³/hr | `SCOPE_LEDGER.csv` SOW-0106 |
| Sour Gas Inlet (P, T) | TBC (To Be Confirmed in source) | `SCOPE_LEDGER.csv` SOW-0106 |
| Sour Gas Outlet (P, T) | 4355 kPag, 28 °C | `SCOPE_LEDGER.csv` SOW-0106 |
| Sweet Gas Inlet (P, T) | 7640.9 kPag, 50 °C | `SCOPE_LEDGER.csv` SOW-0106 |
| Sweet Gas Outlet (P, T) | 7430 kPag, 16 °C | `SCOPE_LEDGER.csv` SOW-0106 |
| Design Pressure | 9756 kPag (1415 psig) | `SCOPE_LEDGER.csv` SOW-0106 |
| Design Temperature | 66 °C | `SCOPE_LEDGER.csv` SOW-0106 |
| Ambient Design Temperatures | -40 °C min, +35 °C max | `SCOPE_LEDGER.csv` SOW-0106 |
| Driver | None | `SCOPE_LEDGER.csv` SOW-0106 |
| Construction Sequencing Constraint | TBD — sequencing with adjacent PKG-052 deliverables (vendor package delivery DEL-052-04, foundations, electrical, controls tie-ins) | location TBD |
| Turnover Target | Mechanical completion to commissioning handoff per OBJ-010 (commissioning/turnover and controlled open-item closure). | `OBJECTIVE_REGISTER.csv` OBJ-010 |

## Construction (Artifacts Produced)

| ArtifactID | Artifact | Type | Source |
|---|---|---|---|
| ART-2444495F85 | Construction work package | EPC Construction Work Package | `ARTIFACT_REGISTER.csv` DEL-052-03 |
| ART-F79E686395 | Installation and tie-in workface plan | Construction Tie-In Evidence | `ARTIFACT_REGISTER.csv` DEL-052-03 |
| ART-0E330BEA94 | Construction interface and turnover checklist | Construction Interface Evidence | `ARTIFACT_REGISTER.csv` DEL-052-03 |

## References

- `_CONTEXT.md` (deliverable identity, scope, objectives mapping)
- `_REFERENCES.md` (decomposition basis pointers)
- `DELIVERABLE_REGISTER.csv` row DEL-052-03
- `PACKAGE_REGISTER.csv` row PKG-052
- `SCOPE_LEDGER.csv` rows SOW-0103, SOW-0104, SOW-0105, SOW-0106
- `ARTIFACT_REGISTER.csv` rows ART-2444495F85, ART-F79E686395, ART-0E330BEA94
- `INTERFACE_REGISTER.csv` PKG-052 rows (9 interface facts)
- `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010
- 26020-Package_Requirements.docx package heading 7 — present under `_Sources/` as binary `.docx`; section-level text not deliverable-local (location TBD for clause-level citation)
- 26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx — vendor RFQ source basis referenced by `PACKAGE_REGISTER.csv` PKG-052 (location TBD; not deliverable-local)
- DBM-Deepcut/4-25_Deepcut_DBM.md — design basis referenced by `PACKAGE_REGISTER.csv` PKG-052 and OBJ-001/OBJ-009 (location TBD; not deliverable-local)
