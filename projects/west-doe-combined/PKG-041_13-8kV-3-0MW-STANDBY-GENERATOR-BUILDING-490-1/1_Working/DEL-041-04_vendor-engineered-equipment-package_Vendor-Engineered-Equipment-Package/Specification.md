# Specification: DEL-041-04 — Vendor Engineered Equipment Package

## Scope

### In Scope (Package Vendor)

Engineering, design, fabrication/supply, and delivery of the physical equipment package for the 13.8 kV, 3.0 MW standby generator building (490-1) under PKG-041, developed from the EPC Scope of Work (`DEL-041-01`) and the EPC Package Datasheet (`DEL-041-02`). Source: `DELIVERABLE_REGISTER.csv` (GATE-07) row `DEL-041-04`.

Specifically includes:

- Vendor package engineering and design.
- Vendor documentation supporting the engineered package (vendor-side; turnover register is `DEL-041-05`).
- Fabrication/supply of the physical equipment package.
- Vendor package design basis and datasheet set (`ART-0CD9C13301`).

Source: `PACKAGE_REGISTER.csv` (GATE-07) ResponsibleParty narrative; `ARTIFACT_REGISTER.csv` (GATE-07).

### Out of Scope

- Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination — owned by EPC Integrator (`PACKAGE_REGISTER.csv` GATE-07).
- Construction Work Package authoring (`DEL-041-03`).
- Vendor Document Turnover Package (`DEL-041-05`).
- EPC vendor package review and acceptance (`DEL-041-06`).

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| REQ-04-01 | Package shall be engineered and designed to satisfy the EPC Scope of Work (`DEL-041-01`) and EPC Package Datasheet (`DEL-041-02`) for PKG-041. | `DELIVERABLE_REGISTER.csv` (GATE-07) — Description column for `DEL-041-04` |
| REQ-04-02 | Package shall provide 13.8 kV, 3.0 MW standby generation in building 490-1. | Package name in `PACKAGE_REGISTER.csv` (GATE-07); detailed performance values `location TBD` |
| REQ-04-03 | Package shall be capable of interfacing with the EPC Integrator at each of the twelve declared facility interface points (Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports). | `INTERFACE_REGISTER.csv` (GATE-07) rows for PKG-041 |
| REQ-04-04 | Package vendor shall produce a vendor package design basis and datasheet set covering each interface and operating condition. | `ARTIFACT_REGISTER.csv` (GATE-07) row `ART-0CD9C13301` |
| REQ-04-05 | Package shall be deliverable as a physical equipment package (i.e., fabricated, supplied, and shippable as a coordinated unit). | `ARTIFACT_REGISTER.csv` (GATE-07) row `ART-E2164EA14C`; `PACKAGE_REGISTER.csv` (GATE-07) vendor scope narrative |
| REQ-04-06 | Package shall be subject to EPC Integrator integration review prior to acceptance (`DEL-041-06`). | `DELIVERABLE_REGISTER.csv` (GATE-07) Responsible column for `DEL-041-04`; `DEL-041-06` |
| REQ-04-07 | Detailed code/standards (NEC, NFPA 110, NFPA 37, IEEE C37.x, etc.) shall apply per the EPC Package Datasheet. ASSUMPTION: applicable codes — specific clauses `location TBD`. | ASSUMPTION; no accessible source slice |

## Standards

Governing standards are nominated through the EPC Package Datasheet (`DEL-041-02`). Specific standards and clauses are `location TBD` because deliverable-specific source slices have not been copied locally (`_REFERENCES.md` Missing/Deferred section). Likely applicable standards (ASSUMPTION):

- NFPA 110 — Emergency and Standby Power Systems (location TBD)
- NFPA 37 — Stationary Combustion Engines and Gas Turbines (location TBD)
- NEC (NFPA 70) — Article 445 Generators, Article 700/701/702 Emergency/Legally Required Standby/Optional Standby (location TBD)
- IEEE C37 series — Switchgear/protective relaying (location TBD)
- IEEE 446/493 — Emergency and standby power / reliability (location TBD)
- ANSI C50.13 — Cylindrical-rotor synchronous generators (location TBD)

## Verification

| Req | Verification Method | Notes |
|---|---|---|
| REQ-04-01 | Design review by EPC Integrator against `DEL-041-01`/`DEL-041-02` | Performed within `DEL-041-06` |
| REQ-04-02 | Factory/shop test and inspection of the generator package | `ART-53AD41FE27` (referenced via `DEL-041-06`) |
| REQ-04-03 | Interface compliance review against `INTERFACE_REGISTER.csv` rows | EPC Integrator review |
| REQ-04-04 | Document review of vendor package design basis and datasheet set | Vendor turnover via `DEL-041-05`; review via `DEL-041-06` |
| REQ-04-05 | Physical delivery inspection / receiving inspection | TBD — inspection plan not in accessible sources |
| REQ-04-06 | Acceptance record per `DEL-041-06` | `ART-0E8BDED2A8` |
| REQ-04-07 | Code compliance certification by vendor; EPC review | location TBD |

## Documentation

Required documentation set (artifacts produced by this deliverable):

- Vendor engineered physical equipment package (`ART-E2164EA14C`).
- Vendor package design basis and datasheet set (`ART-0CD9C13301`).

Companion documentation flowing through other deliverables:

- Vendor document register and submittals: `DEL-041-05` (`ART-866D2094F2`).
- Factory/shop test and inspection evidence: `DEL-041-06` (`ART-53AD41FE27`).

Source: `ARTIFACT_REGISTER.csv` (GATE-07).
