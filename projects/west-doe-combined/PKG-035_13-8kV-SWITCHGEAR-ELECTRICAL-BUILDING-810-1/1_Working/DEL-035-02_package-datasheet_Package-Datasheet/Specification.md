# Specification: DEL-035-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-035`, the 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design of the plant main power distribution center and its prefabricated, shop-fabricated electrical building.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (switchgear lineup and the 810-1 electrical building with its housed equipment). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Specific switchgear bus ampacity, short-circuit withstand rating, breaker count and ratings, protective relaying scheme, arc-flash incident-energy results, and detailed equipment population inside the 810-1 building are `TBD` because they depend on facility load-flow, short-circuit, relay coordination, and arc-flash studies not present in the accessible source set.
- 810-1 plot-plan coordinates, building dimensions, HVAC unit sizing, and equipment-by-equipment layout inside the building are `TBD` pending detailed engineering.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-035-02-001 | The Package Datasheet shall identify `PKG-035`, workbook row 37, WBS 01, CoA tracking number 26020-01-30-026, discipline Electrical, and package name "13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)." Source: Workbook Packages row 37; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-035-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment package; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-035`. | Responsibility statement review against Gate 7 package register. |
| REQ-035-02-003 | The Package Datasheet shall include the twelve applicable interface facts: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 37; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-035`. |
| REQ-035-02-004 | The Package Datasheet shall identify the bus as 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, fed from a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer, with the bus sized for the full facility scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System and System Voltages table. | Source citation review against DBM Power System slice. |
| REQ-035-02-005 | The Package Datasheet shall identify the downstream radial distribution to the 6.9 kV Inlet/Sales Compressor, 4.16 kV Acid Gas/Overheads Compressor, 600 V Acid Gas Compressor, 600 V Sales/Overheads Compressor, and 4.16 kV/600 V General Area/Tank Farm/Process Electrical Buildings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System. | Source citation review; downstream list matches DBM. |
| REQ-035-02-006 | The Package Datasheet shall record that power distribution is shared between 04-25 and 03-25 and that the 03-25 main feed is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. | Cross-facility distribution review. |
| REQ-035-02-007 | The Package Datasheet shall describe the building as prefabricated, modular, shop-fabricated, located in a general purpose area, climate-controlled with n+1 HVAC, elevated on piles for bottom cable entry, wired with TECK and ACIC cables, with EMT conduit between adjacent equipment and equipment doors sized for the largest equipment removal. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and building/module list (line 2811). | Building construction review against DBM Electrical Buildings slice. |
| REQ-035-02-008 | The Package Datasheet shall require grounding/bonding consistent with the DBM facility basis: major electrical equipment connected to the ground grid at two points; ground wells at electrical buildings; piles used as electrodes interconnected by a main #2/0 green insulated grounding conductor in the highest-voltage carrying tray. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding. | Grounding interface review. |
| REQ-035-02-009 | The Package Datasheet shall specify 13.8 kV medium-voltage cables as three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Specifications table. | Cable specification review against DBM table. |
| REQ-035-02-010 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Tray and Conduit. | Layout/interface review. |
| REQ-035-02-011 | The Package Datasheet shall record that standby power for this facility is supplied at the 600 V MCC level via TOU standby generators with transfer switches; the prior centralized 13.8 kV emergency-generator concept is eliminated for this scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Standby Power. | Standby power interface review. |
| REQ-035-02-012 | The Package Datasheet shall mark switchgear bus ampacity, short-circuit rating, breaker count/rating, protective relay scheme, arc-flash incident-energy results, 810-1 plot-plan location, HVAC sizing, and detailed in-building equipment population as `TBD` unless source-supported package-specific data becomes available. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |
| REQ-035-02-013 | The Package Datasheet shall preserve the eight supported objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` as directionally relevant context (PACKAGE_HEURISTIC association). Source: `OBJECTIVE_DELIVERABLE_MAP.csv`. | Objective traceability review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, transformer spacing, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards (API RP-505) | Referenced by DBM for Class I Zone 2, Gas Groups IIA and IIB classification; electrical buildings located in general purpose areas. | Applicable as source-supported basis. |
| NEMA VE2 | Cable tray support where installation detail is not included. | Applicable per DBM Cable Tray and Conduit slice. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 37 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-035`. | All twelve applicable interface facts are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Cross-facility distribution | Compare datasheet text to DBM Power System slice and 3-25 DBM line 740. | Sub-feed to 03-25 is recorded correctly. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix (twelve interface facts).
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 37, applicable Gate 7 registers, and the DBM electrical source slices used for the 13.8 kV switchgear and 810-1 electrical building basis.
