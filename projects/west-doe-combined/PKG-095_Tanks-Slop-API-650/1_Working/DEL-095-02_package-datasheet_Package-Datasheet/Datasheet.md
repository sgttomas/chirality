# Datasheet — DEL-095-02 Package Datasheet

Deliverable: Package Datasheet for PKG-095 Tanks, Slop (API 650).
Authority: descriptive; values and references trace to accessible source slices.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-095-02_package-datasheet` | `_CONTEXT.md` Identity |
| Name | Package Datasheet | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-095` | `_CONTEXT.md` Identity |
| ParentWorkbookID | 95 | `_CONTEXT.md` Identity |
| Package Name | Tanks, Slop (API 650) | `_CONTEXT.md`; PACKAGE_REGISTER.csv row `PKG-095` |
| Workbook Row | 91 | PACKAGE_REGISTER.csv row `PKG-095` |
| WBS | 03 | PACKAGE_REGISTER.csv row `PKG-095` |
| CoA Tracking Number | 26020-03-19-004 | PACKAGE_REGISTER.csv row `PKG-095` |
| Major Equipment Tag (likely) | `TK-9130-2` (ASSUMPTION — labeled "likely" in ARTIFACT_REGISTER row `ART-340A371C42`) | ARTIFACT_REGISTER.csv `ART-340A371C42`; DBM `3-25_Comp_and_Liquids_DBM.md` line 463 |
| Equipment Description | 26020-03-PT-19-004 — Tanks, Slop | PACKAGE_REGISTER.csv row `PKG-095` |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | Slop storage — off-spec condensate / contaminated hydrocarbon liquids requiring segregation from on-spec condensate product | PACKAGE_REGISTER.csv `Function`; DBM 3-25 line 406 |
| Tank Standard | API 650 (Modified atmospheric) — ASSUMPTION: applies by analogy to companion condensate/produced-water tanks (DBM line 421 names API-650 Modified for the same tank family); package name itself states "API 650" | PACKAGE_REGISTER.csv `Package`; DBM 3-25 line 421 |
| Tank Count | 1 | DBM 3-25 line 406 ("one slop tank"); ARTIFACT_REGISTER `ART-340A371C42` |
| Nominal Capacity | 3,800 bbl (ASSUMPTION — DBM 3-25 line 406 places the slop tank in the eleven 3,800 bbl condensate tank set; not separately specified) | DBM 3-25 lines 406, 410 |
| Service Fluid | Off-spec / contaminated condensate; receives liquids from LP fuel-gas scrubber V-3210-2, LP KO drum pump P-3900-2, HP KO drum pumps P-4100-2 / P-4150-2 truck-out / transfer | DBM 3-25 lines 463, 497, 499 |
| Truck-out Connection | Required (slop receives truck-out / transfer liquids from KO drum pumps) | DBM 3-25 lines 497, 499 |
| Internal Coating | TBD — DBM 3-25 line 421 specifies Devchem 253 for produced-water tanks of the same family; not stated for slop |
| External Insulation / Heating | TBD — DBM 3-25 line 421 specifies for produced-water tanks; slop tank not explicitly stated |
| Design Specific Gravity | TBD |
| Design Pressure | TBD (atmospheric per API 650 family — ASSUMPTION) |
| Design Temperature | TBD |
| Vapor Service | LP fuel-gas blanket — ASSUMPTION by analogy to caustic tank basis (DBM line 402); not explicit for slop |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | West Doe (Project 26020) | Project context |
| Battery Limit Owner | EPC Integrator (facility-level integration, interfaces, tie-ins) | PACKAGE_REGISTER.csv `Description` |
| Package Engineering Owner | Package Vendor (package engineering, design, vendor documentation, physical package) | PACKAGE_REGISTER.csv `Description` |
| Hazardous Area Classification | TBD |
| Climatic / Wind / Seismic Loads | TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Tank Type | Atmospheric API 650 (Modified) — ASSUMPTION (see Attributes) | DBM 3-25 line 421 (family analog); package name |
| Material of Construction | TBD |
| Foundation | Per "Structural / Foundations / Supports" interface — facility-supplied | INTERFACE_REGISTER.csv `IFC-D097FBA7EF` |
| Appurtenances | Standard tank appurtenances, connections to drain / recycle / truck-out, standard tank instrumentation | ARTIFACT_REGISTER `ART-340A371C42` |
| Vendor Documentation Package | Per `DEL-095-05_vendor-document-turnover-package` (Vendor Document Index, Control Procedure, Supplier Quality Plan, ITP, etc.) | ARTIFACT_REGISTER rows under `DEL-095-05` |

## Interface Requirements Matrix

Interface facts carried here as evidence per `_CONTEXT.md` Notes; one row per interface declared in INTERFACE_REGISTER.csv for `PKG-095`.

| Interface ID | Interface Type | Applicable | Source |
|---|---|---|---|
| `IFC-80C5346752` | Process Piping | YES | INTERFACE_REGISTER row |
| `IFC-12159F52EA` | Relief / Flare / Vent | YES | INTERFACE_REGISTER row |
| `IFC-0589336378` | Drain / Containment | YES | INTERFACE_REGISTER row |
| `IFC-468169EEAC` | Grounding / Bonding | YES | INTERFACE_REGISTER row |
| `IFC-5DD221B2A0` | Area / Exterior Lighting | YES | INTERFACE_REGISTER row |
| `IFC-AC60F2EB97` | Cathodic Protection | YES | INTERFACE_REGISTER row |
| `IFC-7037F0AE8A` | I&C / Control Cabling | YES | INTERFACE_REGISTER row |
| `IFC-A01689FD3F` | Grading / Site Drainage / Spill Containment | YES | INTERFACE_REGISTER row |
| `IFC-D097FBA7EF` | Structural / Foundations / Supports | YES | INTERFACE_REGISTER row |

## References

- PACKAGE_REGISTER.csv (GATE-07_Final_Published_2026-05-24), row `PKG-095`
- DELIVERABLE_REGISTER.csv (GATE-07), row `DEL-095-02_package-datasheet`
- ARTIFACT_REGISTER.csv (GATE-07), rows for `DEL-095-02`
- INTERFACE_REGISTER.csv (GATE-07), rows for `PKG-095`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 406, 421, 463, 497, 499)
- `_Sources/26020-Package_Requirements.docx` package heading 47 — DOCX; local markdown slice not extracted; `location TBD`
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 91 — XLSX; not directly readable as text; `location TBD`
