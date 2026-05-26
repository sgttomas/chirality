# Datasheet — DEL-073-03 Construction Work Package (PKG-073 Amine Treating Unit)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-073-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-073 |
| PackageName | Amine Treating Unit (ATU) |
| Workbook Package Number | 73 (Workbook Packages row 49) |
| Discipline | Mechanical |
| Deliverable Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Facility | 04-25 Deepcut Gas Plant (West Doe Deepcut expansion) |
| Authoritative Source Basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Amine Treating Basis); `_Sources/26020-Package_Requirements.docx` package heading 27 (location TBD — binary source, slice not locally accessible) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Removes H2S (and allows controlled CO2 slip) from high-pressure inlet gas using an MDEA-based solvent; produces sweet gas to downstream TEG dehydration. | DBM-Deepcut Sec. "Amine Treating Basis / Process Description" |
| Process modules in scope | Module 1 — Amine Gas Sweetening; Module 2 — Amine Regeneration. | PROJECT_DECOMP PACKAGE_REGISTER row PKG-073 Supply |
| Vendor scope | Complete Amine Treating Unit package (package engineering, design, vendor documentation, physical equipment package). | PACKAGE_REGISTER row PKG-073 |
| EPC Integrator scope | Integration of the vendor package into the facility: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration. | PACKAGE_REGISTER row PKG-073 |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md` Anticipated Artifacts |
| Covers Scope Items | SOW-0051, SOW-0052, SOW-0053, SOW-0054 | `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-heuristic mapping per `OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`) | OBJECTIVE_DELIVERABLE_MAP / `_CONTEXT.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| ATU normal operating pressure | 7722 kPag (design 7722 kPag; low TBD) | DBM-Deepcut "Amine Design Values" |
| Plant raw inlet flow basis (summer) | 300–307.5 MMSCFD (design 307.5 MMSCFD) | DBM-Deepcut "Amine Design Values" |
| Plant raw inlet flow basis (winter) | 300–312.0 MMSCFD (design 312.0 MMSCFD) | DBM-Deepcut "Amine Design Values" |
| Inlet temperature (gas to ATU) | Winter 36.8 °C; summer 44.1 °C | DBM-Deepcut "Amine Design Values" |
| Sweet gas H2S target | ≤ 4 ppmv H2S at absorber outlet | DBM-Deepcut "Amine Design Values" |
| Sales gas CO2 target | ≤ 2 mol% (MDEA selected for CO2 slip; H2S removal has priority) | DBM-Deepcut "Amine Design Values" |
| Inlet H2S basis | ~ 1.0 mol% (plant inlet basis; may be marginally shifted by SOC discharge blending) | DBM-Deepcut "Amine Design Values" |
| Site design ambient temperature | -40 °C minimum / +35 °C maximum (extreme -49.2 / +38.9 °C) | DBM-Deepcut Sec. 2 site basis |
| Hazardous area / safety interface scope | Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. | PACKAGE_REGISTER row PKG-073 "Applicable interface types" |

## Construction

| Construction Element | Description | Source |
|---|---|---|
| Major tagged equipment (representative) | AC-5340-1, AC-5342-1, AC-5305-1, E-5370-1, E-5375-1, E-5360-1, F-5392-1, F-5394-1, F-5365-1, F-5367-1, F-5390-1, F-5210-1, F-5220-1, P-5327-1, P-5397-1, P-5330-1, P-5333-1, P-5335-1, P-5312-1, P-5380-1, P-5381-1, P-5347-1, P-5348-1, TK-5310-1, TK-5398-1, TK-5315-1, T-5230-1, T-5240-1, T-5350-1, V-5325-1, V-5328-1, V-5345-1, V-5355-1, V-5250-1, V-5260-1. | DBM-Deepcut Sec. "Amine Treating Unit" equipment table |
| Absorber configuration | 2 × 50% upflow gas amine absorbers with top demisters. | DBM-Deepcut "Amine Equipment and Design Requirements" |
| Inlet coalescers | 2 × 100% amine inlet gas filter/coalescers upstream of absorbers. | Same |
| Lean/rich amine exchangers | 2 × 50% plate-and-frame exchangers (turndown). | Same |
| Charge pumps | 3 × 57.5% multi-stage horizontal centrifugal pumps (API-610 axial-split casing basis, model TBC). | Same |
| Regenerator | 20 actual trays (18 stripping); ≤70% jet/downcomer flood; two water-wash stages. | Same |
| Reboiler | BKU kettle hot-oil reboiler; 350 °F heat-medium supply via mixing valves; skin ≤350 °F. | Same |
| Surge tank | ~30 min surge volume at design circulation; LP fuel-gas blanket; secondary containment; truck-out connection. | Same |
| Modularization basis (overall plant) | Modular construction requirements coordinated with the plot plan as layout matures. | DBM-Deepcut Sec. 2.3 (layout/maintainability basis) |
| Construction sequencing | TBD — to be developed in the workface plan against PKG-073 tie-ins (process gas, utilities, flare, drains, electrical, I&C, structural). |
| Inspection / NDE plan | TBD — vendor and EPC integrator to develop per discipline (mechanical, piping, electrical, I&C) prior to construction. |
| Turnover documentation set | Construction turnover checklist (per anticipated artifacts); will reference DEL-073-05 (Vendor Document Turnover Package) and DEL-073-06 (EPC Vendor Package Review and Acceptance). | `_CONTEXT.md`; DELIVERABLE_REGISTER rows 261–263 |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Amine Treating Basis (Process Description, Design Values, Equipment Requirements, Open Items) and Amine Treating Unit equipment list.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` — PKG-073 row.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — DEL-073-03 row and PKG-073 sibling deliverables.
- `_Sources/26020-Package_Requirements.docx` package heading 27 — referenced by decomposition; binary source not locally text-accessible (location TBD for clause-level claims).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — referenced by decomposition; binary source not locally text-accessible (location TBD).
