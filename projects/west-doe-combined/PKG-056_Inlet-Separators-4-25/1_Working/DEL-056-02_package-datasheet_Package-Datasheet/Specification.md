# Package Datasheet — Specification (DEL-056-02, PKG-056 Inlet Separators 4-25)

> Normative document. Requirements are derived only from accessible sources or are explicitly labeled `ASSUMPTION`. Unsupported items are `TBD`.

## Scope

This Specification defines the EPC Integrator Package Datasheet for PKG-056 "Inlet Separators 4-25". It governs the technical data that the EPC Integrator hands off to a third-party Package Vendor for vendor-package engineering, design, and fabrication of two identical horizontal three-phase inlet separator packages serving the 4-25 West Doe Deepcut facility, including plot reservation for a future third separator (current basis per DBM line 589).

**Covers (in scope):**
- Tagged equipment list, sparing, and process function for the inlet separator packages.
- Operating and design conditions (pressure, temperature, flow, retention).
- Mechanical construction basis (orientation, coating, internals).
- Interface applicability matrix for the package boundary.
- Vendor engineering deliverable list inherited from `26020-Package_Requirements.docx` heading 11.

**Excludes (by-others, per source):**
- Interconnecting piping at skid edge.
- DCS integration.
- Foundations.
- Electrical power supply from plant MCC.
- Installation and erection.

Source: `26020-Package_Requirements.docx` heading "26020-01-PT-17-004 - Inlet Separators", "Scope Notes / Open Items".

## Requirements

### R1 — Equipment Inventory
- R1.1 The package shall provide two (2) identical horizontal three-phase separators, sparing 2 x 50%. [Source: Package Requirements heading 11, "Major Included Equipment"]
- R1.2 Each separator shall be internally coated with Devchem 253; associated piping shall not be internally coated. [Source: Package Requirements heading 11; DBM line 646]
- R1.3 Each separator shall include a manually adjustable weir and a vertical high-performance mesh/vane mist eliminator. Final mist-eliminator selection is subject to operations review. [Source: DBM line 646]
- R1.4 Each separator shall include de-sanding nozzles. [Source: Package Requirements heading 11]
- R1.5 The package shall provide a heated self-framing building covering instrumentation and one vessel end. [Source: Package Requirements heading 11]
- R1.6 Each separator shall be provided with one (1) liquid outlet heater (HEX) sized to heat cold liquid from approximately -26 °C to a temperature sufficient to keep the MPFF level-control-valve feed above hydrate and freeze thresholds. Outlet temperature target and heat duty: **TBD pending process simulation**. Heat medium: **TBD** (candidate media: warm glycol, process cross-exchange). [Source: DBM line 648]

### R2 — Valves and Isolation
- R2.1 Each separator shall have at least two parallel balanced-globe inlet pressure control valves (PCVs): one for main inlet and one for drive-gas connection, both with hardened trim recommended for two-phase hydrocarbon throttling. [Source: Package Requirements heading 11; DBM line 646]
- R2.2 Inlet PCV design differential pressure shall be <= 5 psid at design inlet pressure. [Source: DBM line 646]
- R2.3 An outlet manual isolation valve shall be provided to permit PCV maintenance without blowing down the full separator. [Source: DBM line 646]
- R2.4 A skid-edge inlet isolation valve shall be provided to isolate inlet PCVs for maintenance. [Source: DBM line 646]

### R3 — Operating Conditions
- R3.1 Operating pressure range: 4,502 to 4,998 kPag (653 to 725 psig). [Source: Package Requirements heading 11]
- R3.2 Operating temperature range: 12.5 to 33.2 °C. [Source: Package Requirements heading 11]
- R3.3 Operating gas flow rate per train: 3,184 e3m3/d (112.5 MMSCFD). [Source: Package Requirements heading 11]
- R3.4 Operating produced-water flow rate: 10 Am3/d. [Source: Package Requirements heading 11]
- R3.5 Operating raw-condensate flow rate: 616 Am3/d. [Source: Package Requirements heading 11]
- R3.6 Maximum inlet operating pressure of 1,300 psig is the current design basis (ASSUMPTION: based on 90% of an assumed upstream gathering-pipeline MAOP of 1,440 psig; must be validated during detailed engineering). [Source: DBM line 628]

### R4 — Design Conditions
- R4.1 Design pressure: 9,377 kPag. [Source: Package Requirements heading 11, "Design conditions"]
- R4.2 Design temperature range: 2.8 to 34 °C. [Source: Package Requirements heading 11]
- R4.3 Design gas flow rate per train: 6,368 e3m3/d (225 MMSCFD). [Source: Package Requirements heading 11]
- R4.4 Design produced-water flow: 10 m3/d. [Source: Package Requirements heading 11]
- R4.5 Design raw-condensate flow: 616 m3/d. [Source: Package Requirements heading 11]
- R4.6 Facility inlet separator total design vapour: 300 MMSCFD. [Source: DBM line 622]
- R4.7 Plant-gate design pressure up to the inlet-separator inlet PCV downstream manual isolation shall have an MAWP equal to the upstream inlet pipeline. [Source: DBM line 628]
- R4.8 Downstream of the inlet-separator inlet PCV: design pressure shall be 1,360 psig to the J-T valve/expander outlet isolation in the cryogenic unit (equivalent to 600# flanges at 200 °F). Molecular-sieve system requires 900# flanges. [Source: DBM line 628]
- R4.9 Inlet separator shut-ESDV pressure shutdown setpoint: 1,360 psig. [Source: DBM line 809]
- R4.10 Slug capacity per separator: 33.9 m3 (source authority; **CONFLICT** with DBM 31.8 m3 / 33.9 m3 reported unresolved — see Conflict Table in Guidance.md). [Source: Package Requirements heading 11; DBM line 591]
- R4.11 Water retention time: **TBD**. [Source: Package Requirements heading 11]
- R4.12 Condensate retention time: **TBD**. [Source: Package Requirements heading 11]

### R5 — Two-Phase / Start-Up Operability
- R5.1 The package shall be designed to accept two-phase flow during winter or shutdown cooling. [Source: DBM line 630]
- R5.2 The package shall accommodate methanol injection upstream for hydrate suppression. [Source: DBM lines 630, 834]
- R5.3 Each separator shall be capable of receiving drive gas (sales-gas source upstream of the sales splitter; inlet-compressor discharge as alternate); drive-gas flow shall be separately metered per package. [Source: DBM line 811]

### R6 — Materials and Sour Service
- R6.1 The package is in sour service (sour gas, sour raw condensate, sour water). All wetted materials shall comply with sour-service requirements consistent with the design basis. Specific material-of-construction standards (e.g., NACE MR0175 / ISO 15156) — **location TBD** (not directly cited in accessible source slice). [Source: Package Requirements heading 11, "Basic Scope"]
- R6.2 Internal coating: Devchem 253 on vessels only. [Source: Package Requirements heading 11]

### R7 — Interface Applicability
- R7.1 The package interfaces shall conform to the applicability matrix in `Datasheet.md` §"Interface Applicability Matrix", derived from `26020-Packages_Interfaces_4_export.xlsx` row 68. [Source: Package Requirements heading 11, "Physical Interface Summary"]
- R7.2 Interface PE notes carried at Datasheet remain authoritative for Vendor coordination; package-level interface coordination notes are **TBD** at this stage (per Package Requirements heading 11, "Interface Coordination Notes: TBD").

### R8 — Vendor Engineering Deliverables (Inherited Requirements)
The vendor package shall deliver the vendor engineering deliverable set listed in `26020-Package_Requirements.docx` heading 11, "Vendor Engineering Deliverables". The grouped list is reproduced in `Guidance.md` §"Vendor Document Set"; each listed Deliverable ID is a requirement on Vendor scope.

## Standards

Specific governing codes/standards are not enumerated in the directly accessible source slice for PKG-056 (heading 11 of `26020-Package_Requirements.docx`). The following are commonly applicable for this equipment class; treat each as **ASSUMPTION** pending confirmation against the project Design Basis Memorandum or Vendor RFQ document `Bid Docs/Budgetary/26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` (referenced by source but not text-extracted — **location TBD**):

| Standard | Subject | Status |
|---|---|---|
| ASME BPVC Section VIII Div. 1/2 | Pressure vessel design | ASSUMPTION; location TBD |
| NACE MR0175 / ISO 15156 | Sour-service materials | ASSUMPTION; location TBD |
| API 12J / API SPEC 12J | Oil-gas separator sizing | ASSUMPTION; location TBD |
| CSA / ABSA pressure equipment registration | Provincial pressure-equipment registration (Alberta context — ASSUMPTION based on "West Doe Deepcut" naming) | ASSUMPTION; location TBD |

## Verification

| Req. ID | Verification Approach |
|---|---|
| R1.1, R1.2, R1.5 | Vendor MEC-002 Mechanical Equipment List; MEC-003 Equipment Data Sheets; MEC-016 GA Drawing |
| R1.3, R1.4 | MEC-006 Package Equipment Specifications; operations review record (TBD) |
| R1.6 | Process datasheet for HEX; process simulation report (TBD) |
| R2.1-R2.4 | INS-016 Control Valve Data Sheets; INS-017 On-Off / Shutdown Valve Data Sheets; PIP-018 Valve Data Sheets |
| R3.x, R4.x | MEC-003 Equipment Data Sheets; MEC-009 Pressure Vessel Data Sheets; MEC-014 Mechanical Calculation Package |
| R4.7-R4.9 | PRO-014 Relief and Flare Design Basis; PRO-015 PSV Sizing; CTL-005 Cause and Effect Matrix |
| R4.10 | Slug-capacity calculation in MEC-014; reconcile against DBM line 591 (Conflict Table) |
| R5.x | CTL-003 Control Narrative; PRO-008 P&IDs |
| R6.1, R6.2 | MEC-005 Static Equipment Specifications; QLT-013 Material Test Reports |
| R7.x | CTL-026 Package Vendor Interface Specification; interface punch sign-off |
| R8 | Vendor Document Index (PRQ-009) and full vendor deliverable register |

## Documentation

The following deliverable artifacts are required as outputs informed by this Specification (per `_CONTEXT.md` §"Anticipated Artifacts"):

- Package technical datasheet (this Specification + companion `Datasheet.md`)
- Vendor engineering handoff basis (this document set, packaged for Vendor RFQ issue)
- Package interface requirements matrix (Datasheet §"Interface Applicability Matrix" + referenced spreadsheet row 68)
- Source-supported equipment and design criteria (Datasheet attributes/conditions/construction)

The full Vendor engineering deliverable list (R8) is itemized in `Guidance.md` for reader clarity.
