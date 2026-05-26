# Specification — DEL-088-02 Package Datasheet (PKG-088 Caustic Treating)

`epistemic-status: DRAFT (Pass 1+2)`

## Scope

This Package Datasheet specifies the EPC-Integrator-issued technical handoff data required for a third-party Package Vendor to engineer, design, fabricate, and supply the PKG-088 non-regenerative caustic treating (condensate mercaptan removal) package, and for EPC to integrate that package into the 03-25 Liquids Hub.

In scope:

- Package identification and tagging (`26020-02-PT-27-001`).
- Process duty, capacity, and treating chemistry envelope.
- Equipment items belonging to the vendor package boundary.
- Interface types crossing the package boundary into the facility.
- Vendor/EPC responsibility split.

Excluded (out of package scope):

- Caustic regeneration equipment — not in 03-25 basis. [Source: DBM §"Condensate Mercaptan Treating"]
- Sales-condensate LACT custody-transfer equipment — third-party NRM scope. [Source: DBM §Overview]
- Other package-specific exclusions: TBD — no package-specific exclusions stated in source materials. [Source: PACKAGE_REGISTER.csv PKG-088 "Exclusions" field]

## Requirements

### R-088-02-01 — Treating Duty (Source-grounded)

The package SHALL provide non-regenerative caustic mercaptan treating of C5+ stabilized condensate at 20,000 bbl/d. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-02 — Extractable Targets (Source-grounded)

The package SHALL be designed to extract H2S, CO2, and methyl/ethyl/propyl/butyl mercaptans. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-03 — DSO Entrainment Envelope (Source-grounded)

Design DSO entrainment SHALL be 50 ppmw S (TBC vendor); expected operating DSO entrainment is 30 ppmw S. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-04 — Caustic Solution Basis (Source-grounded)

Caustic solution basis SHALL be 50 wt% NaOH/H2O; SG 1.75 (TBC). [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-05 — Equipment Set (Source-grounded)

The vendor package SHALL include, at minimum: caustic C5+ contactor; pre-heater; caustic outlet filter; water wash; DSO tank; spent-caustic tank; fresh-caustic tank; fresh-water tank. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-06 — Caustic Tank Configuration (Source-grounded)

Fresh and spent caustic tanks SHALL be atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-07 — Spent Caustic Venting (Source-grounded)

The spent caustic tank SHALL vent through a flame arrestor to the incinerator header and SHALL support truck-out. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-08 — VRU Routing Exclusion (Source-grounded)

Fresh caustic SHALL NOT be connected to the VRU. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-09 — Material Restriction (Source-grounded)

Aluminum SHALL NOT be used in the caustic building. Caustic tank material/coating details remain TBC and SHALL be confirmed by vendor and EPC. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-10 — Facility Interfaces (Source-grounded)

The package SHALL provide the following defined interface types into the facility: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. [Source: PACKAGE_REGISTER.csv PKG-088]

### R-088-02-11 — Incinerator Tie-Ins (Source-grounded)

The package SHALL provide overhead, dilution-gas, and enrichment-gas interfaces to the facility incinerator. [Source: DBM §"Condensate Mercaptan Treating"]

### R-088-02-12 — Instrument-Air Demand (Source-grounded, value TBC)

Instrument-air demand for caustic oxidation SHALL be confirmed against the 03-25 basis of 214 SCFM TBC. [Source: DBM §"Instrument Air"]

### R-088-02-13 — Responsibility Split (Source-grounded)

Package Vendor is responsible for package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator is responsible for facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination. [Source: PACKAGE_REGISTER.csv PKG-088]

### R-088-02-14 — Operating Conditions (TBD)

Process operating temperature, pressure, and feed composition limits TBD — not present in accessible source slice. Vendor datasheet from `26020-Package_Requirements.docx` package heading 41 to be resolved when locally readable.

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Project Design Basis Memorandum (03-25 Comp_and_Liquids DBM) | Authoritative for treating duty and equipment envelope | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| 26020 Package Requirements (package heading 41) | Package-specific vendor-document requirements | `_Sources/26020-Package_Requirements.docx`, location TBD (binary not locally readable in this run) |
| 26020 Packages/Interfaces export | Package boundary interface matrix | `_Sources/26020-Packages_Interfaces_4_export.xlsx`, location TBD |
| ASSUMPTION: applicable Canadian provincial pressure-vessel and electrical area-classification codes | Likely applicable to caustic building and package electrical; clause-level requirements not derivable here | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| R-088-02-01 Treating duty | Vendor capacity test / performance guarantee against 20,000 bbl/d feed |
| R-088-02-02, R-088-02-03 Extractables / DSO | Sampling and lab analysis of treated condensate per vendor test protocol |
| R-088-02-04 Caustic basis | Specification review; caustic strength sampling during commissioning |
| R-088-02-05, R-088-02-06 Equipment / tanks | Vendor document review (P&IDs, equipment list, tank datasheets); construction inspection |
| R-088-02-07 Venting | Vendor P&ID review; site verification of flame arrestor and incinerator header tie-in |
| R-088-02-08 VRU exclusion | Vendor P&ID review and field walkdown |
| R-088-02-09 Material | Vendor MTR / material certificates; caustic building material verification |
| R-088-02-10, R-088-02-11 Interfaces | Interface register reconciliation against vendor tie-in list; tie-in walkdown |
| R-088-02-12 Instrument air | Instrument-air loading calculation reconciliation between vendor and facility |
| R-088-02-13 Responsibility | RACI confirmation in EPC-Vendor contract |
| R-088-02-14 Operating conditions | Pending source resolution; verification TBD |

## Documentation

The vendor package shall produce, at minimum:

- Package technical datasheet (this document is the EPC-issued counterpart).
- Vendor engineering handoff basis package.
- Package interface requirements matrix.
- Source-supported equipment list and design criteria.

[Source: DELIVERABLE_REGISTER.csv DEL-088-02 "Anticipated Artifacts"]
