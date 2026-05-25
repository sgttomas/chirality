# Guidance: DEL-013-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-013` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 100A DC UNINTERUPTIBLE POWER SUPPLY package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "100A DC UNINTERUPTIBLE POWER SUPPLY" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for UPS ratings, autonomy, battery, charger, feeder, distribution, building/room assignment, and support details until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: UPS services, standby power interface, electrical-building housing possibilities, grounding/bonding, cable tray, conduit, and maintenance-access constraints.

## Considerations

The DBM electrical design basis supports a general UPS service basis of 120 VAC / 125 VDC for control system, selected emergency or critical lighting, MV breaker control, and MV protective relay loads. It also states that standby power supports UPS systems and other critical systems during outages or turnaround, while leaving generator sizing, transfer-switch ratings/configuration, load shedding, sequencing, and TOU standard confirmation as `TBD`.

The workbook row and Gate 7 registers support the existence and interface profile of the package, but not detailed UPS performance values. The package-specific Word requirements source did not produce a PKG-013 match during this run; therefore, vendor-facing datasheet content should remain conservative until the missing detailed requirements are resolved.

Grounding and bonding are applicable interface topics. The DBM source contains facility grounding basis, including two-point grounding for major electrical equipment and separate copper ground conductors for certain electrical equipment. The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing or connection details.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The datasheet should require electrical routing and physical placement to preserve maintenance access, but detailed clearances remain `TBD` unless issued by detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| UPS quantity / rating | Mark `TBD` pending package-specific source confirmation. | DBM equipment list identifies uninterruptible power supply quantity but does not confirm allocation or rating for this package. |
| 100A DC interpretation | Treat "100A DC" as package title only until source confirms output/load rating. | Workbook name contains the phrase, but no accessible source slice defines whether it is charger output, DC distribution capacity, load, or another rating. |
| Electrical-building location | Identify as possible context, not a confirmed location. | DBM says electrical buildings may house UPS systems but does not locate PKG-013. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations TBD. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 15 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Battery autonomy: TBD. No package-specific source slice available."
- Not acceptable without new source: "UPS output is 100 A at 125 VDC with X minutes autonomy." The accessible source set does not establish this value.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-013-02-001 | Package title says "100A DC", but accessible sources do not define the technical meaning, rating basis, voltage, battery autonomy, or charger/distribution configuration. | Workbook Packages row 15; `PACKAGE_REGISTER.csv` row `PKG-013` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, UPS services and electrical-building source slices | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat "100A DC" as title/identity only and keep detailed UPS parameters `TBD` until vendor data or detailed electrical source is accepted. | TBD |
| HRR-013-02-002 | The DBM equipment list identifies "Uninterruptible Power Supply" quantity 2, but allocation to the PKG-013 100A DC UPS package is not confirmed. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical equipment list | Workbook Packages row 15; Gate 7 `PACKAGE_REGISTER.csv` | Datasheet Attributes; Specification Requirements | Do not assign quantity to PKG-013 until confirmed; record UPS count/rating as `TBD`. | TBD |
