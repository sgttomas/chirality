# Datasheet — DEL-087-03 Construction Work Package (PKG-087 Incinerator)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-087-03_construction-work-package | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | PKG-087 | `_CONTEXT.md` |
| ParentWorkbookID | 87 | `_CONTEXT.md` |
| PackageName | Incinerator | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv row PKG-087 |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; PACKAGE_REGISTER.csv row PKG-087 (EPC Integrator owns facility-level integration) |
| Covers SOW | SOW-0111; SOW-0112; SOW-0113; SOW-0114 | `_CONTEXT.md` |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (PACKAGE_HEURISTIC association — ASSUMPTION) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package equipment (per source) | Qty 1 incinerator knockout drum; Qty 1 incinerator knockout drum transfer pump; Qty 1 incinerator – low pressure flare stack; Qty 1 incinerator blower | PACKAGE_REGISTER.csv PKG-087 (Workbook row 64) |
| Process function | Vapours from the spent caustic storage tank and the caustic regeneration column overheads flow to the incinerator | PACKAGE_REGISTER.csv PKG-087 |
| WBS | 02 | PACKAGE_REGISTER.csv PKG-087 |
| Service allocation | Shared-interface incinerator between 03-25 and 04-25; exact service split open | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 547, 555 |
| Connected source streams | Spent caustic storage tank vent (flame-arrestor route to incinerator header); caustic process overheads | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 400, 402 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Design basis emissions inputs | Prime mover list, emissions summary, emergency generator count/rating, incinerator service split, flare relief and blowdown loads — not yet finalized | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 555 |
| Permit-final emissions values | TBD (DBM scoping only; not permit-final) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 555 |
| Hazardous area classification | TBD (location TBD — source slice not accessible) | TBD |
| Site civil/foundation parameters | TBD (depends on package foundation design — location TBD) | TBD |
| Tie-in pressures / temperatures / flows | TBD per interface (see Specification) | TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Installation scope | Field installation of the package (knockout drum, transfer pump, LP flare stack, blower) into the integrated facility | PACKAGE_REGISTER.csv PKG-087; ASSUMPTION (installation language inferred from deliverable type EPC Construction Work Package) |
| Tie-in interfaces (declared YES) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER.csv (12 rows for PKG-087) |
| Inspection / Test plan | TBD (not stated in accessible sources) | TBD |
| Turnover scope | Construction interface and turnover checklist (artifact) | `_CONTEXT.md` Anticipated Artifacts |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md` |
| Exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv PKG-087 (Exclusions field) |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row `DEL-087-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-087`; `INTERFACE_REGISTER.csv` (12 rows for PKG-087)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (locally accessible)
- `_Sources/26020-Package_Requirements.docx` — package heading 40 (NOT locally readable as text; location TBD for clause-level citation)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 64 (binary; values surfaced via PACKAGE_REGISTER.csv / INTERFACE_REGISTER.csv extracts)
- `Bid Docs/Budgetary/26020-01-PT-RFQ-25-003_Incinerator.docx` (referenced by PACKAGE_REGISTER; NOT locally accessible — location TBD)
