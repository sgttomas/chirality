# Specification — DEL-053-04 Vendor Engineered Equipment Package (Flare KO Drum, Cryo)

> Normative specification for the Package Vendor deliverable. Establishes scope, requirements, governing standards (named where supported), verification approach, and required documentation. Vendor-specific design values are TBD pending issuance of the EPC Package Datasheet (DEL-053-02).

## Scope

### In scope (vendor)
- Package engineering and detailed design of the cryogenic flare knock-out drum V-4110-1 and the associated electric immersion heater H-4112-1 supplied as a single equipment package. [SCOPE_LEDGER SOW-0068, SOW-0069]
- Fabrication / supply of the physical equipment package. [SCOPE_LEDGER SOW-0067; DELIVERABLE_REGISTER DEL-053-04]
- Vendor package design basis and datasheet set anchored to the EPC Package Datasheet (DEL-053-02). [_CONTEXT.md Anticipated Artifacts]
- Vendor-controlled internals, immersion heater design, nozzle schedule, and skid/structural arrangement within the defined package boundary.

### Out of scope (assigned elsewhere)
- Facility integration, tie-ins, constructability, procurement/construction coordination, and facility-level integration are owned by the EPC Integrator. [PACKAGE_REGISTER row 53; SCOPE_LEDGER SOW-0067]
- Cryogenic relief header design upstream of the package boundary (610 mm / 304SS header) and HP/cryo combined downstream piping. [DBM-Deepcut flare header table]
- EPC Scope of Work (DEL-053-01), EPC Package Datasheet (DEL-053-02), and Construction Work Package (DEL-053-03) authorship — vendor consumes these as inputs and contributes evidence to EPC review (DEL-053-06).

### Boundary
- Vendor package boundary terminates at interface points (process inlet from cryogenic relief header; outlet to combined HP/cryo header; electrical supply terminations to heater; instrument/control terminations; drain). Exact terminal-point list: **TBD** — to be confirmed against DEL-053-02 Package Datasheet.

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| R-053-04-01 | The package shall provide cryogenic flare knock-out service for PSV reliefs originating in cryogenic and molecular-sieve-dehydrated systems relieving below -45.5 degC. | DBM-Deepcut "Cryogenic flare" row; SCOPE_LEDGER SOW-0070 |
| R-053-04-02 | The package shall be supplied as a single equipment package including drum V-4110-1 and electric immersion heater H-4112-1. | SCOPE_LEDGER SOW-0068, SOW-0069 |
| R-053-04-03 | The drum shall accept inlet from the 610 mm (24 in) cryogenic relief header (304SS) and discharge to the combined HP/cryo header downstream of both KO drums prior to the HP/cryo stack. | DBM-Deepcut "Cryogenic flare" row and flare header table |
| R-053-04-04 | Materials of construction shall be suitable for the package's minimum design metal temperature (driven by PSV relief temperatures below -45.5 degC). Specific MOC selection: **TBD by vendor**. | DBM-Deepcut "Cryogenic flare" row; ASSUMPTION pending datasheet |
| R-053-04-05 | The package shall be sized to handle the cryogenic flare relief load. Specific design flow, design pressure, and sizing margin: **TBD** — required from EPC Package Datasheet (DEL-053-02); cryogenic-unit J-T valve mechanical stroke limitation ensures control-failure mass flow does not exceed cryogenic flare design flow. | DBM-Deepcut J-T valve note; design values location TBD |
| R-053-04-06 | The immersion heater (H-4112-1) shall be electrically powered. Duty (kW), voltage class, sheath material, and watt density: **TBD by vendor**. | DBM-Deepcut equipment list; vendor scope |
| R-053-04-07 | Pressure-containing components shall be designed and stamped per the applicable pressure vessel code. ASSUMPTION: ASME BPVC Section VIII Division 1 with CRN where required by Canadian jurisdictional registration. | ASSUMPTION (industry convention; not stated in accessible sources) |
| R-053-04-08 | The package shall be designed for the project's specified interfaces: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. Specific interface deliverables shall be defined in the EPC Package Datasheet (DEL-053-02). | PACKAGE_REGISTER row 53 (Applicable interface types) |
| R-053-04-09 | Service shall be treated as non-sour per the project brief unless EPC Package Datasheet (DEL-053-02) supersedes. | SCOPE_LEDGER SOW-0070 |
| R-053-04-10 | Cryogenic flare header heat tracing is NOT required (water not expected in cryogenic flare service); package insulation system shall be defined by vendor consistent with this policy. | DBM-Deepcut flare section (header heat-trace policy) |

## Standards

| Standard / Code | Applicability | Source |
|---|---|---|
| ASME BPVC Section VIII Div. 1 (pressure vessels) | Drum V-4110-1 pressure containment | ASSUMPTION: location TBD |
| Canadian Registration Number (CRN) | Provincial pressure equipment registration | ASSUMPTION: location TBD |
| Applicable electrical/area-classification standards (CSA / CEC) for heater H-4112-1 | Heater electrical design | ASSUMPTION: location TBD |
| Process / piping code at package terminations | Inlet/outlet flange ratings | location TBD; to be aligned with DEL-053-02 |
| 26020-Package_Requirements.docx package heading 8 | Project-specific package requirements | Referenced by SCOPE_LEDGER; **location TBD** in this run |

## Verification

| Verification | Method | Maps to |
|---|---|---|
| Pressure containment | Hydrotest per ASME and code stamping | R-053-04-04, R-053-04-07 |
| Material conformance | Mill certificates; PMI where required; impact test reports at MDMT | R-053-04-04 |
| Heater performance | Factory acceptance test of immersion heater duty and controls (FAT) | R-053-04-06 |
| Dimensional / nozzle conformance | Dimensional inspection vs. vendor drawings approved by EPC | R-053-04-02, R-053-04-08 |
| Sizing / process performance | Vendor sizing calc package reviewed against DEL-053-02 inputs | R-053-04-05 |
| Interface conformance | Interface check list against DEL-053-02 interface matrix | R-053-04-08 |
| Documentation completeness | Submittal of vendor document package per DEL-053-05 register | All |

## Documentation

Required vendor-produced artifacts (see also DEL-053-05 Vendor Document Turnover Package):
- Vendor equipment datasheet set (drum and heater).
- Vendor package design basis.
- Pressure vessel calculations and code stamping certificates (U-stamp, CRN where applicable).
- Fabrication drawings (GA, nozzle orientation, internals).
- Heater design package (electrical, control, FAT report).
- Material test reports (MTRs); NDE records; hydrotest record.
- Dimensional inspection report.
- Surface preparation and coating records.
- O&M manual and spare parts list.
- Vendor turnover package per DEL-053-05.
