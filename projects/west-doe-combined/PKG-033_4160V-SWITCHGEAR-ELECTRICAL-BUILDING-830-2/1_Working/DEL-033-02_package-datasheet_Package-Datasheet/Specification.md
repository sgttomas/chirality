# Specification: DEL-033-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-033`, the 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package (the prefabricated 4.16 kV switchgear electrical building). The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, factory acceptance test reports, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Detailed switchgear ratings (continuous current, short-circuit withstand, BIL, bus configuration), protective relay settings, single-line specifics, feeder lists, and final building dimensions are `TBD` because the accessible source set does not provide confirmed package-specific values for 830-2.
- Per Gate 7 `PACKAGE_REGISTER.csv`, no package-specific exclusions are stated in source materials (`TBD`).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-033-02-001 | The Package Datasheet shall identify `PKG-033`, workbook row 35, WBS 02, CoA tracking number 26020-02-30-024, discipline Electrical, and package name "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)." Source: Workbook Packages row 35; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-033-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment package (4.16 kV switchgear electrical building); EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-033`. | Responsibility statement review against Gate 7 package register. |
| REQ-033-02-003 | The Package Datasheet shall include the twelve applicable interface facts for PKG-033: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 35; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-033`. |
| REQ-033-02-004 | The Package Datasheet shall identify nominal switchgear voltage as 4.16 kV, 3-phase, 60 Hz, consistent with the workbook package name and the DBM medium-voltage services basis. Detailed ratings (continuous, short-circuit, BIL, grounding class) shall be marked `TBD` unless source-supported. Source: Workbook Packages row 35; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services row. | Voltage and rating review against source slices. |
| REQ-033-02-005 | The Package Datasheet shall describe the electrical building configuration consistent with the DBM electrical-buildings basis: prefabricated modular, climate-controlled, n+1 HVAC, bottom cable entry, elevated on piles, TECK/ACIC cable types, EMT conduit between adjacent panels, and equipment-door sizing for the largest equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section. | Configuration check against DBM source slice. |
| REQ-033-02-006 | The Package Datasheet shall require grounding and bonding consistent with DBM facility grounding basis: two-point ground-grid connection for major electrical equipment, ground wells at electrical buildings, green-insulated above-grade conductors in PVC conduit where mechanical protection is required, and compression-type connections. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraph. | Electrical/grounding interface review. |
| REQ-033-02-007 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access and shall conform to the DBM raceway basis (shop pre-installed main tray, field-run limited to field-constructed portions). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-033-02-008 | The Package Datasheet shall locate the electrical building in a general purpose area in accordance with the DBM area-classification basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification paragraph. | Area classification review. |
| REQ-033-02-009 | The Package Datasheet shall preserve standby power requirements as an interface and mark generator sizing, transfer switching, load shedding, sequencing, and TOU standard confirmation as `TBD` unless later source material resolves them. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, emergency-power rows. | TBD / open-item review. |
| REQ-033-02-010 | The Package Datasheet shall identify source gaps for switchgear count/rating, breaker quantities, protection scheme, single-line details, building dimensions, and final 830-2 plot location as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` (no confirmed PKG-033 match in this run). | Gap review before vendor handoff. |
| REQ-033-02-011 | The Package Datasheet shall surface the "830-2" building-tag ambiguity as `NEEDS_HUMAN_RULING` because the DBM enumerates 810-1, 820-1, 830-1, 840-1, 850-1, 860-1, but does not enumerate "830-2". Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building list (lines 2811-2816); Workbook Packages row 35. | Cross-source check at acceptance. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location `TBD`. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification; building shall be placed in general purpose area. | Applicable; package location/classification details `TBD`. |
| IEEE / ANSI / NEMA MV switchgear standards (e.g., for metal-clad MV switchgear) | `ASSUMPTION`: applicable to 4.16 kV switchgear procurement and testing. | Applicable as `ASSUMPTION`; not directly cited in accessible source slices. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 35 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-033`. | All twelve applicable interfaces are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, voltage, and `TBD`s. | No unresolved internal inconsistency. |
| Building-tag resolution | Confirm whether "830-2" is a new building or an alternate/second unit related to the existing 830-1 4.16 kV electrical building. | Human ruling captured; datasheet text aligned to ruling. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis (technical basis, battery limits, design expectations, source-supported requirements).
- Package interface requirements matrix (twelve interface facts).
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 35, applicable Gate 7 registers, and the DBM electrical source slices used for switchgear voltage basis, electrical-building configuration, grounding, raceway, HVAC, area classification, and standby power.
