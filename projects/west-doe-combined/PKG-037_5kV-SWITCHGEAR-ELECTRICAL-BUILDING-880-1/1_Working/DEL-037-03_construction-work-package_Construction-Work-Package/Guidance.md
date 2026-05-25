# Guidance: DEL-037-03_construction-work-package

## Purpose

The Construction Work Package for `PKG-037` (5kV SWITCHGEAR ELECTRICAL BUILDING, 880-1) translates the accepted EPC Scope of Work and Package Datasheet into how the package will be physically installed, tied in, inspected, and turned over. It exists so the EPC Integrator can execute site installation of the vendor-delivered prefabricated electrical building consistent with the DBM electrical design basis, without invading the Package Vendor's engineering scope.

## Principles

- Honor the accepted responsibility split: the Package Vendor delivers the engineered building and its housed switchgear and panels; the EPC Integrator performs site installation, tie-ins, and facility integration. Do not let the construction package re-engineer vendor equipment. (`PACKAGE_REGISTER.csv` row `PKG-037`.)
- Build to the DBM electrical-building basis: prefabricated, modular, elevated on piles with bottom cable entry, n+1 HVAC, TECK/ACIC wiring, EMT between adjacent panels, exterior GFI receptacle, and door/transom sizing for the largest housed equipment. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section.)
- Treat the Gate 7 interface register as the construction tie-in master list. Each interface fact for `PKG-037` is a coordination obligation, not a discretionary item.
- Where source material does not pin a value (lift plans, plot coordinates, schedule), mark it `TBD` rather than inventing it. Anchor any inference as `ASSUMPTION`.

## Considerations

- Pile-supported, elevated foundations are a constructability prerequisite to preserve bottom-entry cable access; coordinate civil/structural and electrical sequencing accordingly. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section.)
- Grounding installation must connect major equipment to the ground grid at two points and include ground wells at the building for test access; sequence ground-grid installation before energization activities. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding section.)
- HVAC commissioning to confirm n+1 redundancy is a turnover gate, not a punch-list item, because building environmental control is required to maintain housed switchgear and electronic equipment.
- Maintenance access (door sizing, transom removability) cannot be allowed to degrade during installation; protect access provisions when staging materials.
- Twelve interfaces apply to this package; treat each as a coordination thread with the responsible facility discipline rather than rolling them up as a single "tie-in" line item.

## Trade-offs

- Field tie-in sequence vs. vendor delivery: site readiness (foundations, ground grid, drainage) must precede building set; schedule pressure to set the building early should be resisted when pre-set tie-ins are incomplete.
- Schedule compression vs. inspection completeness: skipping documented grounding tests or HVAC functional checks to make turnover dates produces unverified handoffs and is not acceptable under the verification requirements.
- Local field modifications vs. vendor-engineered package: any field modification to the engineered building requires Package Vendor coordination, captured under `DEL-037-06_epc-vendor-package-review-and-acceptance`.

## Examples

- An incoming MV power cable for the 5 kV switchgear bus enters from below through pile-supported tray space; the construction package coordinates tray installation under the building before building set so cables can be pulled into the bottom-entry openings without retrofit.
- A communications/network rack tie-in to the facility network is planned and inspected against the I&C/Control Cabling and Communications/Network interface facts (`IFC-F5B78B59CE`, `IFC-1ECBDB6397`), not deferred to commissioning.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-037-03-001 | The Gate 7 PACKAGE_REGISTER lists exclusions as `TBD; no package-specific exclusions stated in source materials`, while standard EPC construction packages typically scope out vendor engineering. | `PACKAGE_REGISTER.csv` row `PKG-037` | This deliverable's Specification "Exclusions" section | Specification Scope/Exclusions | PROPOSAL: Adopt the exclusions stated in this Specification (vendor engineering, vendor turnover, EPC acceptance, detailed schedule/lift plans) as the construction-package working exclusions, pending human ruling. | TBD |
| HRR-037-03-002 | DBM-Deepcut describes electrical-building basis broadly but does not name Building 880-1 specifically, while the workbook row 39 identifies `5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section | Workbook Packages row 39; `PACKAGE_REGISTER.csv` row `PKG-037` | Datasheet Attributes; Construction sections | PROPOSAL: Apply DBM electrical-building basis to Building 880-1 by analogy with other named electrical buildings in DBM Section list; mark any 880-1-specific dimensional or layout data as `TBD` until detailed design source is available. | TBD |
| HRR-037-03-003 | DBM lists named MV switchgear buildings (e.g., 810-1, 820-1, 830-1) but does not enumerate 880-1; the package identity asserts a 5 kV switchgear building at 880-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list | Workbook Packages row 39 | Datasheet Identification/Attributes | PROPOSAL: Accept workbook identity (5 kV class, Building 880-1) as authoritative for the package; record 5 kV-specific bus/rating data as `TBD` pending vendor engineered package data. | TBD |
