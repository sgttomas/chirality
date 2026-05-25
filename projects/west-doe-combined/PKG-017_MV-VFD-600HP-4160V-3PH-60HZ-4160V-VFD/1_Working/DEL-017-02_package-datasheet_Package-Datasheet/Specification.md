# Specification: DEL-017-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-017`, the MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02 (CoA tracking 26020-02-30-008). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, harmonic study results, motor matching analysis, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Driven-motor identity, VFD output rating, continuous vs. starting duty basis, control profile, filter/reactor selections, enclosure ratings, cooling basis, and installation location are `TBD` because the accessible source set does not provide confirmed package-specific values for `PKG-017`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-017-02-001 | The Package Datasheet shall identify `PKG-017`, workbook row 19, WBS 02, CoA tracking number 26020-02-30-008, discipline Electrical, and package name "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 19; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-017-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-017`. | Responsibility statement review against Gate 7 package register. |
| REQ-017-02-003 | The Package Datasheet shall include the six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 19; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-017`. |
| REQ-017-02-004 | The Package Datasheet shall identify the medium-voltage service basis as 4,160 V, 3-phase, 3-wire, 60 Hz LRG, and shall align rated input voltage with this bus. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical voltage/service table. | Source citation review against DBM electrical service table. |
| REQ-017-02-005 | The Package Datasheet shall not assign package-specific values for driven-motor identity, output HP rating, output current, duty cycle, control profile, or filter/reactor configuration without source support; such values shall be carried as `TBD` until vendor data or detailed electrical study confirms them. Source: source gap; package-specific `26020-Package_Requirements.docx` slice not in source root. | TBD/open-item review. |
| REQ-017-02-006 | The Package Datasheet shall require harmonic and reactive-power mitigation to be determined by detailed electrical studies, consistent with SCA-001 VE #37 which removes capacitor banks from synchronous buses where VFDs are present. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SCA-001 / 4160V MCC paragraphs. | Source citation review; carry as a study/design-basis requirement. |
| REQ-017-02-007 | The Package Datasheet shall capture grounding/bonding requirements applicable to MV electrical equipment without overstating package-specific grounding details not present in source (e.g., two-point ground grid connection for major electrical equipment per DBM basis). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Electrical interface review. |
| REQ-017-02-008 | The Package Datasheet shall require power circuits at 13.8 kV, 4,160 V, and 600 V to be separated from control and instrument circuits by distance, shielding, or routing per project electrical specifications and detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable/conduit paragraphs. | Cable/conduit routing review. |
| REQ-017-02-009 | The Package Datasheet shall require cable tray and conduit routing to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray / maintenance paragraphs. | Layout/interface review against the package interface matrix. |
| REQ-017-02-010 | The Package Datasheet shall require I&C and communications/network integration coordination with the plant PLC central control panel, consistent with the documented EtherNet data-acquisition pattern at the 4160V MCC. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph. | Control/communications interface review. |
| REQ-017-02-011 | The Package Datasheet shall preserve `-40 deg C` site minimum ambient as the ambient design basis for any exposed package elements; indoor placement in prefabricated electrical buildings is the documented MV-VFD housing context, subject to detailed design. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` site basis; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical buildings paragraph. | Ambient/installation review. |
| REQ-017-02-012 | The Package Datasheet shall identify source gaps for driven load, VFD output rating, control profile, filters, cooling, enclosure rating, installation location, and supports as `TBD` instead of invented values. Source: `_REFERENCES.md`; package-search result. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conductor sizing, equipment grounding, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| NEMA MG1 (motor basis class) | Documented as the pairing motor basis class for MV inverter-duty motors at the facility. Applicability to the specific PKG-017 driven motor is TBD pending motor identification. | Applicable as design-basis context; specific motor data TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined; indoor electrical-building placement is typical. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 19 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-017`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| MV service basis alignment | Confirm rated input voltage aligns with the documented 4,160 V, 3-phase, 60 Hz LRG MV service bus. | DBM electrical voltage/service table citation present. |
| Harmonic / reactive-power treatment | Confirm requirement to defer to detailed electrical studies, and that capacitor-bank removal (SCA-001 VE #37) is noted where applicable. | DBM SCA-001 / 4160V MCC citation present. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix (six interface facts).
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution (driven load, output rating, control profile, filters, cooling, enclosure, installation location, supports).

The deliverable shall cite the Gate 7 snapshot, workbook row 19, applicable Gate 7 registers, and the DBM electrical source slices used for MV service, MV VFD context, harmonic mitigation, grounding/bonding, cable routing, and electrical-building housing.
