# Guidance: DEL-036-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-036` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 6.9 kV switchgear electrical building (carried per workbook spelling as "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)") while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for switchgear ratings, bus sizing, transformer feed sizing, MCC frame ratings, UPS sizing, building dimensions, and confirmed location until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: medium-voltage service basis, electrical-building construction basis, grounding/bonding basis, cable/raceway basis, and area/placement basis.

## Considerations

The DBM electrical design basis supports a 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded service serving facility process AC inverter-drive motors rated 5,500 hp and above (L2935). It also describes prefabricated modular electrical buildings located in general-purpose areas (L2911, L2973), HVAC sized as n + 1 (L2975), bottom cable entry on elevated pile-supported buildings (L2977), TECK/ACIC interior wiring with EMT for adjacent equipment, an outdoor GFI receptacle, and equipment doors sized for the largest equipment removal (L2979).

The DBM does not provide package-specific switchgear ratings, bus sizes, lineup counts, transformer feed sizing, or interior equipment counts for PKG-036. The DBM equipment list shows facility totals (e.g., Medium Voltage Switchgear quantity 1; Low Voltage Switchgear quantity 2 — L2879-2880); allocation to PKG-036 must be confirmed by detailed design or vendor data. The package-specific Word requirements source did not produce a PKG-036 match during this run; vendor-facing datasheet content should remain conservative until missing detailed requirements are resolved.

Grounding is applicable: major electrical equipment shall be directly connected to the ground grid at two points, and each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system (L2985, L2989). The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing.

Maintenance access is both an explicit workbook interface fact and a DBM constraint: cable tray and conduit routing shall not interfere with maintenance access, equipment doors shall accommodate the largest equipment, and interconnecting trays between pipe racks, process skids, and electrical buildings are field-run (L2979, L2999).

Plot placement: facility-integration design must preserve a minimum 25 m (82 ft) between fired heaters and electrical buildings per OGAOM Sec. 9.6.15 (DBM L298).

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Switchgear / MCC ratings | Mark `TBD` pending package-specific source confirmation. | DBM gives service voltage and general basis but does not confirm package-specific switchgear/MCC ratings. |
| Building 830-1 identity | Treat the workbook spelling as identity-of-record; flag a `CONFLICT` against DBM electrical-building list. | Workbook Packages row 38 names PKG-036 as "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)" but DBM L2811-2816 maps 830-1 to a 4.16 kV building and 820-1 to a 6.9 kV building. |
| Interior equipment count | List candidate equipment scope qualitatively from DBM (L2973); leave quantities and ratings as `TBD`. | DBM lists what electrical buildings may house but does not confirm what is housed in PKG-036 specifically. |
| Building location | Identify general-purpose-area constraint plus 25 m separation from fired heaters; specific coordinates `TBD`. | DBM L2911 and L298 give constraints, not coordinates. |
| Standards | List CEC, OGAOM, area classification, and project electrical specifications as governing bases with locations TBD. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 38 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Switchgear interrupting rating: TBD. No package-specific source slice available."
- Not acceptable without new source: "6.9 kV switchgear is rated 40 kA, 3 s short-circuit withstand with 12 incoming/outgoing breakers." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-036-02-001 | Workbook Packages row 38 names PKG-036 "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)", but the DBM electrical-building list maps 830-1 to "4.16kV Acid Gas / Overheads Compressor Electrical Building" and 820-1 to "6.9kV Inlet / Sales Compressor Electrical Building". | Workbook Packages row 38; `PACKAGE_REGISTER.csv` row `PKG-036` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2811-2816, L2921 | Datasheet Identification/Attributes; Specification REQ-036-02-001/011; Procedure Steps | Preserve workbook identity ("6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)") as package identity-of-record; carry the conflict to detailed design / human ruling before any rename. | TBD |
| HRR-036-02-002 | DBM equipment list identifies Medium Voltage Switchgear quantity 1 and Low Voltage Switchgear quantity 2 across the facility, but allocation to PKG-036 is not confirmed by accessible source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2879-2880 | Workbook Packages row 38; `PACKAGE_REGISTER.csv` row `PKG-036` | Datasheet Attributes/Construction; Specification REQ-036-02-010 | Do not assign equipment quantities to PKG-036 until confirmed; record switchgear counts and ratings as `TBD`. | TBD |
| HRR-036-02-003 | Package-specific exclusions are listed as `TBD; no package-specific exclusions stated in source materials.` in `PACKAGE_REGISTER.csv`. | `PACKAGE_REGISTER.csv` row `PKG-036` | None | Specification Scope/Exclusions | Carry the register's `TBD` exclusion statement forward; do not invent exclusions. | TBD |
