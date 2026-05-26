# Datasheet: DEL-041-04 — Vendor Engineered Equipment Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-041-04_vendor-engineered-equipment-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (GATE-07) |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-041` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` (GATE-07) |
| ParentWorkbookID | 41 | `_CONTEXT.md` |
| PackageName | 13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Item | `SOW-0042` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` (GATE-07) |
| CoA Tracking Number | 26020-01-30-032 | `PACKAGE_REGISTER.csv` (GATE-07) |
| Source Reference | Workbook Packages row 43 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package class | Vendor-engineered, vendor-supplied physical equipment package | `PACKAGE_REGISTER.csv` (GATE-07) row PKG-041 |
| Service | 13.8 kV standby power, 3.0 MW rating | Package name in `PACKAGE_REGISTER.csv` (GATE-07) — value `location TBD` for vendor design-basis confirmation |
| Vendor scope | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` (GATE-07) ResponsibleParty narrative |
| Integrator scope | Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | `PACKAGE_REGISTER.csv` (GATE-07) ResponsibleParty narrative |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating duty | Standby (non-continuous) generation | ASSUMPTION inferred from package name "STANDBY GENERATOR"; detailed duty cycle `TBD` |
| Site / environment | TBD | No deliverable-local source slice copied during PREPARATION (`_REFERENCES.md` Missing/Deferred) |
| Fuel system | TBD | Not stated in accessible decomposition rows |
| Cooling / exhaust | TBD | Not stated in accessible decomposition rows |
| Acoustic / emissions | TBD | Not stated in accessible decomposition rows |

## Construction

| Component | Description | Source |
|---|---|---|
| Generator set | 3.0 MW, 13.8 kV alternator + prime mover; details `TBD` | ASSUMPTION from package name |
| Generator building / enclosure | Pre-engineered or vendor-supplied building (490-1) housing the generator and ancillaries; configuration `TBD` | ASSUMPTION from package name; "BUILDING (490-1)" |
| Switchgear / breakers | 13.8 kV generator breaker, controls; details `TBD` | ASSUMPTION based on rated voltage |
| Auxiliaries | Starting system, governor/AVR, jacket-water heating, lube system, fuel day tank, exhaust silencer | `TBD` — not in accessible decomposition rows |
| Controls / monitoring | Generator control panel, protective relays, remote/SCADA interface | `TBD` — interface fact present (see References) but device-level detail `location TBD` |

## Interfaces (Facility-Level, EPC Integrator Owned)

Workbook-declared package interfaces (from `INTERFACE_REGISTER.csv` GATE-07, all rows for PKG-041):

- Utility Piping (`IFC-508C53EB72`)
- Drain / Containment (`IFC-1528C860A4`)
- Electrical Power (`IFC-004BB1B385`)
- Grounding / Bonding (`IFC-134CB10F1D`)
- Area / Exterior Lighting (`IFC-8E23F09E7C`)
- I&C / Control Cabling (`IFC-1E6785E532`)
- Communications / Network (`IFC-FEEE41EDAA`)
- Building HVAC / Services (`IFC-7D36256CF5`)
- Fire & Gas / Safety Systems (`IFC-5F7FE5FA2A`)
- Maintenance Access (`IFC-57828C08C8`)
- Grading / Site Drainage / Spill Containment (`IFC-B9452850B5`)
- Structural / Foundations / Supports (`IFC-D0146B1F8C`)

## Anticipated Artifacts

- Vendor engineered physical equipment package (`ART-E2164EA14C`)
- Vendor package design basis and datasheet set (`ART-0CD9C13301`)

Source: `ARTIFACT_REGISTER.csv` (GATE-07).

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`
- Workbook Packages row 43 (location TBD — not locally sliced)
- Shared source root: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources` (no deliverable-specific slice copied)
