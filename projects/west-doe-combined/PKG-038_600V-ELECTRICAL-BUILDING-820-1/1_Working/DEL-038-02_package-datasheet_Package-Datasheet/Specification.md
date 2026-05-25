# Specification: DEL-038-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-038`, the 600V ELECTRICAL BUILDING (820-1) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Specific quantities, ratings, layout dimensions, HVAC unit sizing, MCC line-up details, and UPS battery autonomy are `TBD` because the accessible source set does not establish PKG-038-specific values.
- Cathodic protection engineering and supply are excluded from the facility design scope.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-038-02-001 | The Package Datasheet shall identify `PKG-038`, workbook row 40, WBS 01, CoA tracking number 26020-01-30-029, discipline Electrical, and package name "600V ELECTRICAL BUILDING (820-1)." Source: Workbook Packages row 40; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-038-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-038`. | Responsibility statement review against Gate 7 package register. |
| REQ-038-02-003 | The Package Datasheet shall include all twelve applicable interface facts for `PKG-038`: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 40; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-038`. |
| REQ-038-02-004 | The Package Datasheet shall require the building to be a prefabricated, modular electrical building located in a general purpose area, elevated on piles with bottom cable entry, internally wired with TECK and ACIC cables with EMT conduit between adjacent equipment, and provided with an outdoor GFI receptacle. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Compliance review against DBM Electrical Buildings basis. |
| REQ-038-02-005 | The Package Datasheet shall require 600 V services to be 3 phase, 3 wire, 60 Hz, high-resistance grounded with a 5 A continuous resistor, and shall require 600 V MCCs to be traditional MCCs with electronic motor overload relays. Standalone 600 V VFDs are not allowed unless dedicated to large motors; 600 V VFDs shall be provided as part of the 600 V MCC lineup. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, low-voltage services table and Motor Control section. | Datasheet content review against DBM low-voltage and MCC basis. |
| REQ-038-02-006 | The Package Datasheet shall require HVAC for the electrical building to be sized as an n + 1 system so that failure or maintenance of one unit does not affect building heating and cooling. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | HVAC basis review against DBM electrical-building paragraph. |
| REQ-038-02-007 | The Package Datasheet shall require grounding consistent with DBM Grounding and Bonding: 600 V transformers grounded by 5 A continuous high-resistance grounding resistor; 600 V MCCs with power metering and ground/resistor fault detection; ground-fault protection on 600 V systems alarm-only; major electrical equipment directly connected to the ground grid at two points; ground wells at electrical buildings for maintenance and operational testing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section. | Grounding requirement review against DBM grounding paragraphs. |
| REQ-038-02-008 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access, and shall require conduit sealing across area-classification boundaries per the Canadian Electrical Code. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Tray and Conduit section. | Layout/interface review against the package interface matrix. |
| REQ-038-02-009 | The Package Datasheet shall require electric building heaters provided with the package to be 600 V, 3 phase rated equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Building Heaters section. | Heater rating review. |
| REQ-038-02-010 | The Package Datasheet shall mark as `TBD` (rather than invented) the package-specific equipment counts, ratings, layout dimensions, UPS battery autonomy, HVAC unit sizing, and MCC line-up details when no source-supported PKG-038 slice is available. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` (no PKG-038 slice processed in this run). | Gap review before vendor handoff. |
| REQ-038-02-011 | The Package Datasheet shall preserve and surface the 820-1 building-identifier conflict between the workbook package name and the DBM electrical-building list (where 820-1 is named "6.9 kV Inlet / Sales Compressor Electrical Building" and 600 V buildings are listed as 840-1, 850-1, and 860-1) until a human ruling resolves it. Source: Workbook Packages row 40; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list. | Conflict Table review (HRR-038-02-001). |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support and sealing, area-classification compliance, and electrical installation basis referenced throughout DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to enclosure selection, conduit sealing, and equipment installation classification (electrical buildings located in general purpose areas). | Applicable; package location/classification confirmed as general purpose per DBM. |
| Building code (exit lighting and battery backup) | Exit lights shall be provided with battery backup as required by building code; emergency lighting per building code. | Applicable; clause locations TBD. |
| NEMA VE2 | Cable tray support where a project support detail is not included. | Applicable per DBM Cable, Wire, and Raceways. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 40 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-038`. | All twelve PKG-038 interface facts are present. |
| Building basis compliance | Check datasheet text against DBM Electrical Buildings source slice. | Prefabricated/modular construction, general-purpose area, elevation on piles, bottom cable entry, HVAC n + 1, TECK/ACIC internal wiring, EMT use between adjacent equipment, outdoor GFI receptacle, and door/transom equipment removal are all represented. |
| 600 V service / MCC compliance | Check datasheet against DBM low-voltage and MCC basis. | 600 V 3-phase 3-wire 60 Hz, 5 A high-resistance grounding, traditional MCCs with electronic overload relays, 600 V VFDs within MCC lineup, SCR heater-control panels supplied by 600 V MCC feeder breakers are represented. |
| Grounding compliance | Check datasheet against DBM Grounding and Bonding slice. | Two-point ground connections for major equipment, 600 V transformer grounding resistor, ground wells at electrical building, alarm-only 600 V ground-fault protection are represented. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |
| Conflict preservation | Confirm the 820-1 building-identifier conflict appears in Guidance Conflict Table and run record. | HRR-038-02-001 present. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix (twelve interface facts for `PKG-038`).
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 40, applicable Gate 7 registers, and the DBM electrical source slices used for the building/MCC/UPS/grounding/cabling design basis.
