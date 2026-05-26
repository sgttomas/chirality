# Datasheet — DEL-100-02 Package Datasheet (PKG-100 Hydrogen Peroxide Sweetening Unit)

> Descriptive (FACT/ASSUMPTION/TBD-labeled). Values are grounded in locally accessible sources; missing values are `TBD`.
> Source key:
> - `DBM` = `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
> - `PKG-REG` = `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`, row `PKG-100`
> - `DEL-REG` = same snapshot `DELIVERABLE_REGISTER.csv`, row `DEL-100-02_package-datasheet`
> - `IFC-REG` = same snapshot `INTERFACE_REGISTER.csv`, rows for `PKG-100`
> - `PKG-REQ` = `_Sources/26020-Package_Requirements.docx` package heading 52 (binary; not locally text-accessible — `location TBD`)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-100-02_package-datasheet` | FACT — `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | FACT — `_CONTEXT.md` |
| Parent Package ID | `PKG-100` | FACT — `_CONTEXT.md` |
| Parent Workbook ID | 100 | FACT — `_CONTEXT.md` |
| Package Name | Hydrogen Peroxide Sweetening Unit | FACT — `_CONTEXT.md`; `PKG-REG` |
| Package Tag | `26020-03-PT-27-001 - Hydrogen Peroxide Sweetening Unit` | FACT — `PKG-REG` |
| RFQ / Source Basis | `26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` | FACT — `PKG-REG` Word Source Basis |
| Discipline | Mechanical | FACT — `_CONTEXT.md`; `PKG-REG` |
| Deliverable Type | EPC Package Datasheet | FACT — `_CONTEXT.md`; `DEL-REG` |
| Responsible Party | EPC Integrator | FACT — `_CONTEXT.md`; `DEL-REG` |
| Package Vendor Scope | Package engineering, package design, vendor documentation, physical equipment package | FACT — `PKG-REG` |
| EPC Integrator Scope | Integration into the whole process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | FACT — `PKG-REG` |
| WBS | 03 | FACT — `PKG-REG` |
| Workbook Row | 63 | FACT — `PKG-REG`; `_CONTEXT.md` |

## Attributes

### Package Function

| Attribute | Value | Source |
|---|---|---|
| Service | Sour water hydrogen peroxide treatment | FACT — `PKG-REG` package scope |
| Process Function | Sour water is routed to the static mixer and then to the Hydrogen Peroxide Reactors for treatment. Hydrogen peroxide is pumped in from the H2O2 tank by the H2O2 pumps. Treated water is sent to produced water storage tanks. | FACT — `PKG-REG` package scope; consistent with `DBM` lines 214, 216 |
| Quantity (packages) | 1 | FACT — `DBM` line 40 ("one sour-water H2O2 treatment package"); `DBM` line 427 ("One package") |
| Throughput / Capacity | 3,840 m3/d (carried `TBC` in DBM) | ASSUMPTION (carried-`TBC`) — `DBM` line 427 |

### Equipment Constituents

| Equipment | Quantity | Source |
|---|---|---|
| Hydrogen Peroxide Pumps (chemical injection pumps) | TBD | FACT (presence) — `PKG-REG` package scope; quantity not stated in accessible source |
| Hydrogen Peroxide Reactors | TBD (>=1) | FACT (presence) — `PKG-REG` package scope; quantity not stated in accessible source |
| Static Mixer | TBD (>=1) | FACT (presence) — `PKG-REG` package scope; quantity not stated in accessible source |
| H2O2 Storage Tank (upstream supply; not in package boundary — see Notes) | 1 × 400 bbl | FACT — `DBM` lines 216, 428 |

### Battery Limits / Boundaries (Interfaces)

The PKG-100 package interfaces (all marked applicable in `IFC-REG`):

| Interface Type | Interface ID | Source |
|---|---|---|
| Process Piping | `IFC-7AF1D6F0D5` | FACT — `IFC-REG` |
| Utility Piping | `IFC-C9C5C50D7F` | FACT — `IFC-REG` |
| Relief / Flare / Vent | `IFC-6D0847A80A` | FACT — `IFC-REG` |
| Drain / Containment | `IFC-DB6DD6511D` | FACT — `IFC-REG` |
| Electrical Power | `IFC-62EE7F54FE` | FACT — `IFC-REG` |
| EHT (Electric Heat Tracing) | `IFC-5CD88768D1` | FACT — `IFC-REG` |
| Grounding / Bonding | `IFC-052932D9A1` | FACT — `IFC-REG` |
| Area / Exterior Lighting | `IFC-3169DD9620` | FACT — `IFC-REG` |
| I&C / Control Cabling | `IFC-950BB7D168` | FACT — `IFC-REG` |
| Building HVAC / Services | `IFC-56086E492D` | FACT — `IFC-REG` |
| Fire & Gas / Safety Systems | `IFC-D38D454C74` | FACT — `IFC-REG` |
| Maintenance Access | `IFC-FC62996C71` | FACT — `IFC-REG` |
| Structural / Foundations / Supports | `IFC-B76BAF7A9C` | FACT — `IFC-REG` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site elevation | 673 m AMSL | FACT — `DBM` SEC-11 line ~ ambient block |
| Design ambient temperature | -40 °C to +35 °C | FACT — `DBM` SEC-11 ambient block |
| Inlet stream | Sour produced water (from 03-25 produced-water storage system) | FACT — `DBM` line 214 |
| Outlet stream | Treated water to produced-water storage tanks | FACT — `PKG-REG` package scope |
| Chemical reagent | Hydrogen peroxide (H2O2) supplied from H2O2 storage tank by H2O2 pumps | FACT — `PKG-REG`; `DBM` lines 216, 428 |
| Design pressure | TBD — not stated in accessible sources | TBD — likely in `PKG-REQ` (not text-accessible); `location TBD` |
| Design temperature | TBD — not stated in accessible sources | TBD — likely in `PKG-REQ`; `location TBD` |
| Materials of construction | TBD — not stated in accessible sources | TBD — likely in `PKG-REQ`; `location TBD` |
| Hazardous area classification | TBD — package-specific value not stated; facility-level basis exists | TBD — `DBM` SEC-11 references "hazardous area classification" generally |
| Winterization | Required (consistent with -40 °C design basis; EHT interface applicable) | ASSUMPTION — derived from `DBM` ambient + `IFC-REG` EHT row |

## Construction

| Item | Value | Source |
|---|---|---|
| Package Architecture | Skid-mounted vendor package (static mixer + reactors + injection pumps) | ASSUMPTION — typical for vendor packages of this type; not explicit in accessible sources |
| Modularization | TBD | TBD — not stated |
| Fabrication standards | TBD | TBD — likely in `PKG-REQ`; `location TBD` |
| Inspection requirements | TBD | TBD — likely in `PKG-REQ`; `location TBD` |
| Shipping configuration | TBD | TBD |
| Site assembly / tie-ins | EPC Integrator scope (see Battery Limits) | FACT — `PKG-REG` |

## References

- `DBM` — `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 22, 35, 40, 214, 216, 427-428, 655, 679, 696; SEC-11 ambient/elevation block)
- `PKG-REG` — Gate 7 `PACKAGE_REGISTER.csv`, row `PKG-100`
- `DEL-REG` — Gate 7 `DELIVERABLE_REGISTER.csv`, row `DEL-100-02_package-datasheet`
- `IFC-REG` — Gate 7 `INTERFACE_REGISTER.csv`, rows for `PKG-100` (13 applicable interfaces)
- `PKG-REQ` — `_Sources/26020-Package_Requirements.docx` package heading 52 (binary; not text-accessible to this drafting pass — `location TBD` for clause-level claims)
- `PKG-REQ-XLS` — `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; not text-accessible — `location TBD`)
- `RFQ` — `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` (referenced by `PKG-REG`; not present under `_Sources` — `location TBD`)

## Notes

- The H2O2 storage tank (1 × 400 bbl) is recorded by `DBM` as part of the 03-25 facility chemical system, not necessarily inside this vendor package boundary. The package as scoped by `PKG-REG` includes injection pumps, reactors, and static mixer. Storage-tank scope assignment to PKG-100 vs. a separate facility tankage scope is `TBD` (see Guidance Conflict Table).
- Numeric process design values (P, T, materials, MOC) are not derivable from accessible sources and are flagged `TBD` rather than invented.
