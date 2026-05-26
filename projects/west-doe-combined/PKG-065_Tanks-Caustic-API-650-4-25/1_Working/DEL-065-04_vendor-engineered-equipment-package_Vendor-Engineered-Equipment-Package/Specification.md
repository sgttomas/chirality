# Specification — DEL-065-04 Vendor Engineered Equipment Package

## Scope

This specification governs the Package Vendor production unit for `PKG-065` "Tanks, Caustic (API 650) 4-25". The unit comprises the vendor's engineering, design, fabrication/supply, and the physical equipment package developed from the EPC Scope of Work (DEL-065-01) and EPC Package Datasheet (DEL-065-02).

In scope (Package Vendor):
- Engineering, design, vendor documentation, and physical equipment package for the Spent Caustic Tank (TK-6780-1) and the Fresh Caustic Tank, both per modified API 650, 400 bbl nominal capacity (Source: SOW-0198, SOW-0199; `26020-Package_Requirements.docx` package heading 20).
- Design of the integral spent-caustic tank heater (≥ 32.2 °C / 90 °F) (Source: SOW-0199).
- Vendor package design basis and datasheet set (Source: `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` ART-5507339ADA).

Explicitly excluded (By Others — EPC Integrator):
- Foundations, mounting of tanks at site, electrical/instrumentation install, platforms, staircases, etc. (Source: SOW-0200 "By others").
- Whole-facility integration, tie-ins, constructability, procurement/construction coordination, and facility-level integration (Source: `PACKAGE_REGISTER.csv` row 87 — Responsibility split).

## Requirements

### R-01 Code of Construction
Both tanks SHALL be designed and fabricated to modified API 650. The specific modifications are not enumerated in the available source slice (`location TBD`); the vendor SHALL propose and document deviations from the base standard for EPC Integrator review. (Source: SOW-0199.)

### R-02 Capacity
Each tank SHALL have a nominal capacity of 400 bbl. (Source: SOW-0198, SOW-0199, SOW-0200.)

### R-03 Design Pressure (Spent Caustic Tank, TK-6780-1)
The Spent Caustic Tank SHALL be designed for 32 oz internal pressure and 1.0 oz vacuum, atmospheric service. (Source: SOW-0199.)

### R-04 Design Pressure (Fresh Caustic Tank)
ASSUMPTION: Fresh Caustic Tank design pressure SHALL match the Spent Caustic Tank (32 oz / 1.0 oz vacuum). The source slice (SOW-0198) does not explicitly state Fresh Caustic Tank design pressure (`location TBD`); the vendor SHALL confirm with the EPC Integrator before fabrication.

### R-05 Minimum Process Temperature
The Spent Caustic Tank SHALL be provided complete with a heater sized to maintain ≥ 32.2 °C (90 °F) minimum. Vendor SHALL design the heater. (Source: SOW-0199.) Heater sizing for the Fresh Caustic Tank is `TBD` — vendor to confirm requirement with the EPC Integrator (no explicit source statement).

### R-06 Minimum Design Temperature
Design temperature minimum SHALL be the site minimum ambient temperature. The specific value is `TBD` and SHALL be drawn from the EPC Package Datasheet (DEL-065-02) prior to fabrication. (Source: SOW-0200 "Minimum ambient temperature".)

### R-07 Service / Fluid Compatibility
- Spent Caustic Tank SHALL be compatible with spent caustic from the pressurized caustic drain drum V-6940-1, with circulating caustic concentration of ~14.7 wt% NaOH (TBC). (Source: DBM-Deepcut §Mercaptan Treating Unit; SOW-0199.)
- Fresh Caustic Tank SHALL be compatible with 50 wt% NaOH fresh caustic solution. (Source: DBM-Deepcut §Mercaptan Treating Unit.)
- Material of construction is `TBD` (ASSUMPTION: caustic-compatible carbon steel selection per vendor's standard practice for caustic service per modified API 650; vendor to propose).

### R-08 Capacity / Throughput / Flow Rates
Design throughput, in-flow rate, and out-flow rate are `TBD` per source ("Capacity/design throughput: TBC"; "Flow rate: TBD"). Vendor SHALL receive values from the EPC Package Datasheet (DEL-065-02) before finalizing nozzle sizing. (Source: SOW-0200.)

### R-09 Interface Provisions
The package SHALL provide connection terminations compatible with the following PKG-065 interface types (Source: `PACKAGE_REGISTER.csv` row 87; `INTERFACE_REGISTER.csv`):
- Process Piping, Relief / Flare / Vent, Drain / Containment, Grounding / Bonding, Cathodic Protection, I&C / Control Cabling, Structural / Foundations / Supports.
- Area / Exterior Lighting and Grading / Site Drainage / Spill Containment are EPC-Integrator-owned interfaces; the package SHALL be compatible with them but does not supply them.

### R-10 Out-of-Scope Confirmation
Vendor SHALL NOT supply foundations, site mounting, electrical/instrumentation installation, platforms, or staircases. (Source: SOW-0200 "By others".)

### R-11 Vendor Documentation Turnover
Vendor documentation turnover artifacts are produced under DEL-065-05; this deliverable SHALL provide the engineering basis content required by DEL-065-05. (Source: `_DEPENDENCIES.md` (no declared edges; ASSUMPTION based on companion deliverable list in SOW-0197) and the parent deliverable list in SOW-0197/0198/0199/0200.)

## Standards

| Standard | Applicability | Source / Location |
|---|---|---|
| API 650 (modified) | Tank design and fabrication for both tanks | SOW-0199; `26020-Package_Requirements.docx` pkg heading 20 — modifications `location TBD` |
| EPC Package Datasheet (DEL-065-02) | Site/process design conditions, interface specifics | `_CONTEXT.md` Decomposition Reference |
| EPC Scope of Work (DEL-065-01) | Package boundaries and responsibility assignment | `_CONTEXT.md`; ARTIFACT_REGISTER.csv ART-266824F1FD |

Additional governing codes (e.g., ASME B31.3 for piping limits, electrical classification per applicable area code) are `TBD` in the available source slice; vendor SHALL propose and EPC Integrator SHALL confirm.

## Verification

| Requirement | Verification Approach |
|---|---|
| R-01 (modified API 650) | Vendor design review, API 650 calculation package, third-party inspection of fabrication |
| R-02 (capacity) | Dimensional check at fabrication; capacity calculation in vendor design basis |
| R-03 / R-04 (design pressure) | Pressure-vessel calculation; hydrotest/leak test per modified API 650 |
| R-05 (heater) | Heater duty calculation; functional test of heater control loop at FAT |
| R-06 (min design temperature) | Material certification (CVN where required); design calculation against site min ambient (value from DEL-065-02) |
| R-07 (fluid compatibility) | MOC selection rationale in vendor design basis; coating/lining qualification (if used) |
| R-08 (throughput / flow) | Nozzle sizing calculation against confirmed values from DEL-065-02 |
| R-09 (interfaces) | Interface compliance matrix in vendor documentation; cross-check with INTERFACE_REGISTER PKG-065 rows |
| R-10 (exclusions) | Scope-split confirmation in vendor doc transmittal; EPC Integrator acceptance per DEL-065-06 |
| R-11 (documentation) | Acceptance under DEL-065-05 vendor document turnover package |

## Documentation

Anticipated artifacts (Source: `_CONTEXT.md`; `ARTIFACT_REGISTER.csv` ART-AF35D29822, ART-5507339ADA):

- Vendor engineered physical equipment package (the hardware itself — covered by ART-AF35D29822).
- Vendor package design basis and datasheet set (covered by ART-5507339ADA).
- Engineering basis content sufficient to feed:
  - DEL-065-05 Vendor Document Turnover Package.
  - DEL-065-06 EPC Vendor Package Review and Acceptance.
