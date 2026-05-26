# Specification — DEL-090-01 Scope of Work (PKG-090 Vapour Recovery Unit 3-25)

> Normative document. Requirements derive from accessible sources; inferred requirements are labelled `ASSUMPTION`. Missing details are `TBD`.

## Scope

### In scope (EPC Integrator)

This deliverable defines the EPC Integrator Scope of Work for the PKG-090 Vapour Recovery Unit 3-25, comprising:

- Two (2) 100%-capacity VRU compressor packages in lead-lag, housed in a single building (Source: PACKAGE_REGISTER.csv row 100; DBM SEC-06).
- Tagged equipment and package identity list (Source: `_CONTEXT.md` Anticipated Artifacts).
- Package function and integration narrative for the 03-25 facility, including VRU discharge routing to 04-25 SOC suction under SCA-002 (Source: DBM SEC-06; SEC-01).
- Responsibility assignment between EPC Integrator and Package Vendor (Source: PACKAGE_REGISTER.csv row 100 §Ownership column).
- Facility-level integration: tie-ins, constructability, procurement/construction coordination across the interface types listed below (Source: PACKAGE_REGISTER.csv row 100).

### Interface coverage (EPC Integrator owns facility-side integration for):

Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
(Source: PACKAGE_REGISTER.csv row 100 interface types.)

### Out of scope

- Package engineering, package design, vendor documentation, and the physical equipment package itself — these are Package Vendor scope (DEL-090-04). (Source: PACKAGE_REGISTER.csv row 100 §Ownership.)
- Vendor document register and vendor document turnover — separate deliverable DEL-090-05. (Source: DELIVERABLE_REGISTER.csv rows 568, 564.)
- EPC vendor package review/acceptance evidence — separate deliverable DEL-090-06. (Source: DELIVERABLE_REGISTER.csv row 569.)
- Package-specific exclusions stated in source materials: none stated (Source: PACKAGE_REGISTER.csv row 100 Exclusions column = "TBD; no package-specific exclusions stated in source materials.").

## Requirements

### R-090-01 — Package function

The Scope of Work SHALL describe the package process function: collect vapours from condensate and produced-water tank systems and selected process vents, compress vapours through two (2) two-stage Ro-Flo 12S/212M positive-displacement rotary vane compressors driven by 200 HP VFD motors, in lead-lag 2 x 100% configuration, and route discharge to the 04-25 SOC suction (no local 03-25 SOC retained per SCA-002).
Source: DBM SEC-06 §Vapour Recovery; PACKAGE_REGISTER.csv row 100; DBM SEC-01 supersession table.

### R-090-02 — Sour service

The package SHALL be specified for sour service.
Source: PACKAGE_REGISTER.csv row 100.

### R-090-03 — Tagged equipment list

The Scope of Work SHALL identify the package equipment by tag, at minimum: the two VRU compressor packages, the shared building, per-train recycle valves, the VRU suction-header LP-flare bypass V-ball valve, and the LP fuel-gas make-up/blanket-gas regulator.
Source: DBM SEC-06 §Vapour Recovery; PACKAGE_REGISTER.csv row 100. Specific tag numbers `TBD` (location TBD — `26020-Package_Requirements.docx` heading 43 and `26020-03-PT-RFQ-12-001_VRU_1_R0.docx`).

### R-090-04 — VRU recycle control

Each train SHALL be equipped with a recycle valve returning second-stage discharge to first-stage suction, sized for 100% flow at minimum driver speed and lowest discharge pressure.
Source: DBM SEC-06 §Vapour Recovery.

### R-090-05 — Suction-pressure stabilisation

A make-up/blanket-gas regulator from LP fuel gas SHALL maintain minimum suction pressure at maximum turndown.
Source: DBM SEC-06 §Vapour Recovery.

### R-090-06 — LP flare bypass

The VRU suction header SHALL include an LP flare bypass V-ball valve operated by VRU suction pressure. The header SHALL free-drain or slope toward the flare KO interface as defined by detailed design.
Source: DBM SEC-06 §Vapour Recovery.

### R-090-07 — Facility integration interfaces (EPC Integrator)

The EPC Integrator SHALL deliver facility-side integration for each interface type listed in §Scope (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports).
Source: PACKAGE_REGISTER.csv row 100.

### R-090-08 — Responsibility split (Package Vendor vs EPC Integrator)

The Scope of Work SHALL state that the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
Source: PACKAGE_REGISTER.csv row 100 §Ownership.

### R-090-09 — Coverage of decomposition scope items

The Scope of Work SHALL cover SOW-0249, SOW-0250, SOW-0251, SOW-0252.
Source: `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 564. (Detailed text of each SOW item: `TBD` — not located in accessible sources.)

### R-090-10 — Discharge destination consistency with SCA-002

VRU discharge SHALL route to 04-25 SOC suction. Any reintroduction of a local 03-25 SOC is prohibited under SCA-002.
Source: DBM SEC-01 supersession; SEC-06 §Vapour Recovery.

### R-090-11 — Capacity, sizing, and performance basis

Capacity, suction/discharge pressures, flow rates, and turndown SHALL be stated in the Scope of Work. Values: `TBD` (location TBD — `26020-03-PT-RFQ-12-001_VRU_1_R0.docx`; `26020-Package_Requirements.docx` heading 43; bid-docs file not located under `_Sources/`).
(ASSUMPTION: vendor RFQ document carries the design capacity values; pending source access.)

## Standards

| Standard / Document | Applicability | Source / Location |
|---|---|---|
| Project DBM `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Project design basis governing scope, supersession state, and integration boundary | DBM SEC-01, SEC-06, SEC-07 |
| `26020-Package_Requirements.docx` heading 43 | Package-specific requirements | Located at `_Sources/26020-Package_Requirements.docx`; section text location TBD (docx not extracted) |
| `26020-03-PT-RFQ-12-001_VRU_1_R0.docx` | Vendor RFQ defining detailed package requirements | NOT located under accessible `_Sources/`; location TBD |
| SCA-002 (accepted supersession) | Routes VRU discharge to 04-25 SOC suction | DBM SEC-01; SEC-06 |
| External codes (e.g., CSA, ASME, API for sour service) | `TBD` — none cited explicitly in accessible sources for this package | location TBD |

## Verification

| Requirement | Verification Approach | Verifying Artifact |
|---|---|---|
| R-090-01, R-090-02 | Cross-check Scope of Work narrative against DBM SEC-06 and PACKAGE_REGISTER row 100. | DEL-090-01 review record |
| R-090-03 | Tagged equipment list cross-referenced to DEL-090-02 Package Datasheet and DEL-090-04 Vendor Engineered Equipment Package once issued. | DEL-090-02; DEL-090-04 |
| R-090-04, R-090-05, R-090-06 | Vendor package design review against the DBM SEC-06 control description; HAZOP confirmation. | Vendor package design review log (DEL-090-06) |
| R-090-07 | Interface register entries for PKG-090 reviewed against scope text for each listed interface type. | INTERFACE_REGISTER.csv (Gate 7 snapshot) |
| R-090-08 | Responsibility narrative reviewed against PACKAGE_REGISTER row 100 §Ownership. | Decomposition snapshot |
| R-090-09 | Scope-item traceability matrix mapping SOW-0249..0252 to Scope of Work sections. | Traceability matrix (`TBD`) |
| R-090-10 | Cross-check process flow / P&ID basis against SCA-002 supersession statement. | DBM SEC-01; downstream P&ID (`TBD`) |
| R-090-11 | Capacity values confirmed against vendor RFQ source slice once accessible. | Vendor RFQ (location TBD); DEL-090-02 |

## Documentation

The Scope of Work deliverable comprises:

- Package scope of work narrative (this Specification + Datasheet).
- Tagged equipment and package identity list (Datasheet §Tagged Equipment).
- Package function and integration narrative (Datasheet §Attributes; Guidance §Purpose/Principles).
- Responsibility assignment record (Specification R-090-08; Guidance §Considerations).

(Source: `_CONTEXT.md` §Anticipated Artifacts.)
