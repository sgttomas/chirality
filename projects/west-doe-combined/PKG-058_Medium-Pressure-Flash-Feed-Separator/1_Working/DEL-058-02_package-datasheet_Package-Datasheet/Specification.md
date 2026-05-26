# Specification — DEL-058-02 Package Datasheet (PKG-058 Medium Pressure Flash Feed Separator)

> Normative requirements for the EPC Package Datasheet deliverable. Requirements are derived from accessible source slices in the 04-25 Deepcut DBM and from the deliverable-local context. Inferred requirements are labeled **ASSUMPTION**. Missing source values remain **TBD**.

## Scope

### In scope

- Defines what the PKG-058 Package Datasheet artifact MUST contain so that a third-party vendor or downstream discipline can engineer/design the package.
- Covers the two MPFF separators (V-7110-1, V-7310-1) and their HCL heater bundles (E-7120-1, E-7320-1) as a single package datasheet, consistent with the source equipment register and `_CONTEXT.md` package boundary.
- Carries interface facts (per `_CONTEXT.md` Notes) as evidence inside this deliverable rather than as standalone deliverables.

### Out of scope

- Detailed vessel mechanical design (vendor responsibility once the datasheet is issued).
- Resolution of upstream HEX thermal reassessment, heater-bundle disposition, and other source TBDs (those resolve in detailed engineering, not in this datasheet).
- DOMAIN/SOFTWARE four-document method variations (this package is PROJECT_DECOMP).

### Covers scope items

- `SOW-0139`, `SOW-0140`, `SOW-0141`, `SOW-0142` (source: `_CONTEXT.md`).

### Supports objectives (explicit mapping)

- `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (source: `OBJECTIVE_DELIVERABLE_MAP.csv`, GATE-07 snapshot; explicit DEL-058-02 rows).

## Requirements

### R1 — Identification content

The datasheet MUST identify:
- Package ID (`PKG-058`) and name (Medium Pressure Flash Feed Separator).
- Equipment tags V-7110-1, V-7310-1, E-7120-1, E-7320-1 with x2/x2 quantity.
- Modules 710-1 and 730-1 (shop-assembled).
- Sparing basis 2 x 100% with explicit note that no sparing exists for the line-pack off-design case.
  - Source: DBM-Deepcut §"MPFF and Stabilizer Train Relationship"; equipment register.

### R2 — Process operating conditions

The datasheet MUST present operating pressure, operating temperature, and inlet flow (two-phase, liquid, vapour) cases (Low / Expected Normal / Expected High / Design) per separator. Tabulated values MUST match DBM-Deepcut §"MPFF Operating and Capacity Basis"; deviations require an authority ruling.
- Operating pressure design value: 1724 kPag (Low/High TBD per source).
- Design winter inlet flows: 12.91 MMSCFD two-phase; 19.58 m3/h liquid; 4.143 MMSCFD vapour.
- Operating temperature: 40 deg C **ASSUMPTION** pending detailed engineering thermal reassessment.

### R3 — Internals and process

The datasheet MUST state:
- Mistex demister internal; no internal coating.
- Minimum 10 minutes liquid residence time between weir height and NLL-interface.
- Automated blowdown valve required.
- LP fuel gas purge / drive gas regulation requirement.
- Methanol injection provision upstream of MPFF inlet LCV.
  - Source: DBM-Deepcut §"MPFF Operating and Capacity Basis".

### R4 — Heater bundle disposition

The datasheet MUST record the heater bundle disposition status:
- U-bundle / BKU arrangement, heat medium tube side, original 140 deg F / 87 deg F duty basis, 10% excess surface area for line-pack (E-7120-1, E-7320-1 design duty 762 kW / 2.6 MM BTU/h with 118/245-80/175 supply/return).
- Retention / de-rate / removal disposition is **TBD** pending thermal re-simulation.
- Vessel nozzle provisions MUST be preserved until disposition is confirmed.
  - Source: DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"Heat Medium Users and Duties".

### R5 — Interfaces

The datasheet MUST enumerate interfaces in a matrix covering, at minimum:
- Inlet separator liquid outlet feed (via inlet-separator liquid outlet heater).
- SOC third-stage suction (overhead vapour).
- Downstream stabilizer flash/feed separator (liquid bottoms).
- Heat medium loop (if heater bundle retained).
- LP fuel gas (purge / drive).
- Methanol injection.
- HP flare (relief / blowdown — **ASSUMPTION** based on adjacent equipment routing).
- Closed hydrocarbon drain, BOP controls, electrical, heat tracing/winterization (**ASSUMPTION** by analogy with adjacent MPFF/SOC interface text).
  - Source: DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"Inlet Separator Interfaces"; §"MPFF Interfaces"; SOC source capacity table.

### R6 — Open items and TBD register

The datasheet MUST surface (not silently resolve) the source-declared TBDs:
- MPFF low / expected-high operating pressure.
- MPFF post-HEX inlet temperatures.
- Heater bundle retention/sizing/heat-medium conditions.
- 03-25 condensate routing to MPFF versus direct stabilizer feed.
- Inlet separator legacy "4 vessels" annotation tied to upstream quantity conflict.
- Vessel design pressure/temperature and materials of construction (not present in accessible source) — **TBD**.

### R7 — Mechanical / materials (gap)

Vessel design pressure, design temperature, corrosion allowance, materials of construction, nozzle schedule, and process-safety design code references are **TBD** in the accessible source set. The datasheet MUST mark these fields TBD and route resolution to detailed-engineering inputs (vendor data sheets / 26020-Package_Requirements.docx package heading 13 once accessible).

### R8 — Sparing / availability

The datasheet MUST state the MPFF train-pairing rule: one MPFF is mechanically tied to one stabilizer; both packages must be operational to handle the line-pack maximum.
- Source: DBM-Deepcut §"MPFF and Stabilizer Train Relationship".

### R9 — Provenance

Each non-trivial value or requirement statement MUST cite its source slice (file + section). Where the exact source location is not locally resolvable, the field MUST be labeled `location TBD` rather than silently asserted.

## Standards

| Standard / Document | Use | Location status |
|---|---|---|
| 26020-Package_Requirements.docx package heading 13 | EPC package requirements basis (per decomposition row) | **location TBD** (no markdown extract locally accessible) |
| 26020-Packages_Interfaces_4_export.xlsx Packages row 71 | Package/interface definition (per decomposition row) | **location TBD** (no markdown extract locally accessible) |
| Applicable pressure-vessel code (ASME Section VIII Div. 1 anticipated) | Vessel design code | **ASSUMPTION** — not stated in accessible MPFF source slices |
| Process safety / relief design (API 521 anticipated) | Relief sizing basis | **ASSUMPTION** — not stated in accessible MPFF source slices |

## Verification

| Requirement | Verification approach |
|---|---|
| R1 Identification | Field presence check against `_CONTEXT.md` and equipment register; values match DBM-Deepcut equipment register rows 52-53 |
| R2 Operating conditions | Table-by-table comparison against DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| R3 Internals/process | Cross-check Datasheet attributes section against DBM-Deepcut source slice |
| R4 Heater bundle | Confirm Datasheet records disposition as TBD with original-basis values |
| R5 Interfaces | Interface matrix review against DBM-Deepcut §"MPFF Operating and Capacity Basis", §"MPFF Interfaces", SOC source table |
| R6 Open items | TBD register present and matches source TBDs |
| R7 Mechanical/materials | TBD entries present; not back-filled by invention |
| R8 Train pairing | Statement present and matches source |
| R9 Provenance | Each non-trivial entry cites source slice or `location TBD` |

## Documentation (Required Artifacts)

Per `_CONTEXT.md` anticipated artifacts:
- Package technical datasheet (this deliverable).
- Vendor engineering handoff basis.
- Package interface requirements matrix (carried within this deliverable as evidence; see Datasheet §Interfaces and Specification R5).
- Source-supported equipment and design criteria (tabulated in Datasheet).
