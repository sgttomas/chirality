# Datasheet — DEL-088-01 Scope of Work (PKG-088 Caustic Treating, Condensate Mercaptan Removal)

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-088-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | PKG-088 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Package Name | Caustic Treating (Condensate Mercaptan Removal) | PACKAGE_REGISTER.csv |
| Package Tag | 26020-02-PT-27-001 | PACKAGE_REGISTER.csv (PackageTag column) |
| Discipline | Mechanical | PACKAGE_REGISTER.csv |
| WBS | 02 | PACKAGE_REGISTER.csv |
| Workbook Row | 50 | PACKAGE_REGISTER.csv; Workbook Packages row 50 |
| Word Source Heading | 26020-Package_Requirements.docx heading 41 | PACKAGE_REGISTER.csv |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Deliverable Type | EPC Scope of Work | DELIVERABLE_REGISTER.csv |
| Mandatory | TRUE | PACKAGE_REGISTER.csv |
| Covers Scope Items | SOW-0055; SOW-0056; SOW-0057; SOW-0058 | `_CONTEXT.md` |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION: package-grouping heuristic per OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC) |

## Attributes — Package Function and Identity

| Attribute | Value | Source |
|---|---|---|
| Package function | Non-regenerable caustic treating package for C5+ condensate mercaptan removal | PACKAGE_REGISTER.csv (Description); DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating |
| Treating technology | Non-regenerative caustic mercaptan treating, Merichem or equivalent | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Treating capacity | 20,000 bbl/d C5+ condensate | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Caustic regeneration | Not included in 03-25 basis | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Consumables | Fresh caustic and make-up water consumed continuously | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| By-products | Spent caustic waste; DSO (disulphide oil) | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Extractable compounds | H2S, CO2, methyl/ethyl/propyl/butyl mercaptans | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| DSO entrainment, expected | 30 ppmw S | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| DSO entrainment, design | 50 ppmw S (TBC vendor) | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Caustic solution basis | 50 wt% NaOH/H2O; SG 1.75 (TBC) | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |

## Tagged Equipment List (Package-Side)

Per DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §Condensate Mercaptan Treating, the package includes:

| Equipment / Element | Notes | Source |
|---|---|---|
| Caustic C5+ contactor | Primary mercaptan extraction vessel | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Pre-heater | Upstream of contactor | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Caustic outlet filter | Downstream of contactor | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Water wash | Treats outlet condensate | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Fresh caustic tank (atmospheric, 32 oz) | LP fuel-gas blanket, heating, insulation | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Spent caustic tank (atmospheric, 32 oz) | Vents through flame arrestor to incinerator header; supports truck-out; not connected to VRU | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Fresh water tank | Make-up water service | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| DSO tank | Disulphide oil storage interface | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Incinerator interfaces | Overhead, dilution-gas, and enrichment-gas connections | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Individual tag numbers (P&ID-level) | TBD — not enumerated in accessible source slices | location TBD |

ASSUMPTION: Tank quantities and individual tank tag IDs (e.g., separate fresh-caustic, spent-caustic, fresh-water, DSO tanks) are confirmed at the DBM level but specific item-tag numbering remains TBD pending vendor package data and `26020-Package_Requirements.docx` package heading 41 slice (not currently accessible in markdown form).

## Conditions

| Condition | Value | Source |
|---|---|---|
| Feed | Stabilized C5+ condensate returning from 04-25 to 03-25 Liquids Hub | DBM-Comp_and_Liquids §Process Overview; §Streams |
| Design ambient | -40 deg C site design basis | DBM-Comp_and_Liquids §Roads / site basis |
| Caustic-zone material restriction | Aluminum shall NOT be used in the caustic building | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| Caustic drain max temperature | 121 deg C / 250 deg F (TBC) | DBM-Comp_and_Liquids §Drains |
| Caustic drain header rating | minimum 300# ANSI | DBM-Comp_and_Liquids §Drains |

## Construction

| Element | Value | Source |
|---|---|---|
| Package vendor scope | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv (IntegrationModel) |
| EPC Integrator scope | Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | PACKAGE_REGISTER.csv (IntegrationModel) |
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv (InterfaceTypes) |
| Caustic tank materials / coatings | TBC | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |

## References

- `_REFERENCES.md` (this deliverable)
- `_CONTEXT.md` (this deliverable)
- PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv (GATE-07_Final_Published_2026-05-24 snapshot)
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (locally accessible)
- 26020-Package_Requirements.docx heading 41 — referenced but binary; not consumed at clause level (location TBD)
- 26020-Packages_Interfaces_4_export.xlsx — referenced; not consumed at clause level (location TBD)
