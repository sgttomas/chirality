# Datasheet — DEL-106-03 Construction Work Package (Yard Lighting)

> Descriptive view of the deliverable as a controlled artifact set. Values are drawn from the GATE-07 accepted decomposition snapshot. Source-specific technical attributes (loads, fixture types, layouts) are not present in deliverable-local source slices and are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-106-03_construction-work-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (GATE-07) |
| Name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-106` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| ParentWorkbookID | 106 | `_CONTEXT.md` |
| PackageName | Yard Lighting | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| CoA Tracking | 26020-01-30-001 | `PACKAGE_REGISTER.csv` (GATE-07) |
| WBS | TBD (workbook row 12; not stated) | `PACKAGE_REGISTER.csv` |
| Source basis | Workbook Packages row 12 (`26020-Packages_Interfaces_4_export.xlsx`) | `_REFERENCES.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | Mandatory Gate 5 EPC anchor deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. | `DELIVERABLE_REGISTER.csv` (Description) |
| Package role | Vendor-engineered package; EPC Integrator owns facility integration, tie-ins, constructability, and procurement/construction coordination. | `PACKAGE_REGISTER.csv` (ResponsibilityModel) |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` (rows for `DEL-106-03`) |
| Artifact IDs | `ART-88F0D51520` (Construction work package); `ART-F0EC8767B3` (Installation and tie-in workface plan); `ART-FC16B15401` (Construction interface and turnover checklist). | `ARTIFACT_REGISTER.csv` |
| Covers scope item | `SOW-0011` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Applicable package interfaces | Electrical Power; Grounding / Bonding; Area / Exterior Lighting | `INTERFACE_REGISTER.csv` (IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / facility | 04-25 Deepcut facility scope (parent objective context) | `OBJECTIVE_REGISTER.csv` (OBJ-001) — ASSUMPTION (best-effort mapping via PACKAGE_HEURISTIC) |
| Service | Yard (exterior) lighting for facility operations | `PACKAGE_REGISTER.csv` (Name + Discipline) |
| Sour-service / safety regime applicability | Applies via OBJ-009 (sour-service safety, fire/gas, codes & standards) | `OBJECTIVE_REGISTER.csv` (OBJ-009) — ASSUMPTION: package-grouping heuristic |
| Environmental / weather conditions | `TBD` (not stated in deliverable-local source slices) | location TBD (`DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 referenced by OBJ-005 but not deliverable-local) |
| Hazardous-area classification at installation locations | `TBD` | location TBD |
| Power system characteristics (voltage, phasing, frequency) | `TBD` | location TBD (`DBM-Deepcut` SEC-12 Electrical Basis) |
| Grounding / bonding system reference | `TBD` | location TBD |

## Construction

| Element | Value | Source |
|---|---|---|
| Installation scope | Physical installation of vendor-supplied yard-lighting package equipment and tie-in to facility electrical, grounding, and civil/structural systems. | ASSUMPTION based on `PACKAGE_REGISTER.csv` ResponsibilityModel + `INTERFACE_REGISTER.csv` |
| Tie-in interfaces (construction-facing) | Electrical Power; Grounding / Bonding; Area / Exterior Lighting | `INTERFACE_REGISTER.csv` |
| Civil / structural tie-ins (poles, foundations, conduit routing, trenching) | `TBD` | location TBD (OBJ-008 references DBM-Deepcut SEC-11 not deliverable-local) |
| Major equipment list (fixtures, poles, panels, distribution gear) | `TBD` (vendor-supplied; defined in `DEL-106-04`) | location TBD |
| Construction sequence / workface plan | `TBD` until vendor package and tie-in basis are accessible | location TBD |
| Inspection points | `TBD` | location TBD |
| Turnover scope and acceptance basis | Turnover into facility per EPC integration responsibility; acceptance per `DEL-106-06_epc-vendor-package-review-and-acceptance`. | `DELIVERABLE_REGISTER.csv` (DEL-106-06) |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- GATE-07 snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (rows for `DEL-106-01..06`)
  - `PACKAGE_REGISTER.csv` (PKG-106)
  - `ARTIFACT_REGISTER.csv` (artifacts under `DEL-106-03`)
  - `INTERFACE_REGISTER.csv` (PKG-106 interfaces)
  - `OBJECTIVE_REGISTER.csv` (OBJ-001, OBJ-004, OBJ-005, OBJ-008, OBJ-009, OBJ-010)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- Workbook Packages row 12 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) — referenced; not parsed as deliverable-local slice.
- `26020-Package_Requirements.docx` — referenced by OBJ-004/OBJ-010; not parsed as deliverable-local slice.
- DBM-Deepcut / DBM-Comp_and_Liquids — referenced by OBJ-005/008/009/010; not parsed as deliverable-local slice.
