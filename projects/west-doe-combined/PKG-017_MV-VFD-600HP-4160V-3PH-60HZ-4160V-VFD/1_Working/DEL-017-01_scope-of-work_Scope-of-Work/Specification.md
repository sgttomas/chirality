# Specification: DEL-017-01_scope-of-work

## Scope

This specification governs the EPC Integrator-authored Scope of Work for `PKG-017`, the workbook-named "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD" package. The Scope of Work is a mandatory Gate 5 EPC anchor deliverable and shall define the full package scope including tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative.

The package is a vendor-owned Electrical package under WBS 02 (CoA 26020-02-30-008). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design (VFD topology, converter/inverter sizing, harmonic filtering selection, cooling design, certified drawings, vendor BOM) is excluded from this EPC Scope of Work unless later provided as vendor data.
- Detailed harmonic and reactive-power mitigation design is excluded; per DBM SCA-001 VE #37 it remains a detailed electrical study item.
- Driven-motor and process-equipment scope (the compressor or other prime mover the VFD starts/drives) is excluded from this package scope unless the workbook explicitly assigns it to PKG-017; the accessible source does not establish that assignment.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-017-01-001 | The Scope of Work shall identify `PKG-017`, workbook row 19, WBS 02, CoA tracking number 26020-02-30-008, discipline Electrical, and the package name "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD". Source: Workbook Packages row 19; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-017-01-002 | The Scope of Work shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-017`. | Responsibility statement review against Gate 7 package register. |
| REQ-017-01-003 | The Scope of Work shall include the six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 19; `INTERFACE_REGISTER.csv` rows for `PKG-017`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-017`. |
| REQ-017-01-004 | The Scope of Work shall identify the medium-voltage service basis as 4,160 V, 3 phase, 3 wire, 60 Hz LRG and shall not assign unsupported package-specific load values. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages table. | Source citation review; unsupported values remain `TBD`. |
| REQ-017-01-005 | The Scope of Work shall describe the MV VFD integration with the 4160V MCC and the plant PLC central control panel EtherNet interface as the communications/network interface basis. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section. | Cross-check against interface matrix entry for Communications / Network. |
| REQ-017-01-006 | The Scope of Work shall preserve harmonic and reactive-power mitigation as a downstream detailed-electrical-study item and shall not pre-commit a mitigation approach. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section, SCA-001 VE #37. | TBD/open-item review. |
| REQ-017-01-007 | The Scope of Work shall require power-to-control circuit separation at 13.8 kV, 4,160 V, and 600 V by distance, shielding, or routing as defined by detailed design. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings/Raceways section. | Routing/interface review. |
| REQ-017-01-008 | The Scope of Work shall require cable tray and conduit routing to preserve maintenance access. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings/Raceways and Maintenance Access references. | Layout/interface review against the package interface matrix. |
| REQ-017-01-009 | The Scope of Work shall flag the inconsistency between the workbook package title ("600HP, 4160V") and the DBM-confirmed MV process drives (4,000 V; 3,878 kW / 5,200 hp) and shall keep driven-equipment identity, VFD rating, and tagged equipment as `TBD` until human ruling. Source: Workbook Packages row 19; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Inlet Compressor Drive section. | Conflict-table review (see Guidance HRR-017-01-001). |
| REQ-017-01-010 | The Scope of Work shall identify source gaps for tagged equipment, VFD topology, sizing, cooling, location, supports, and load identity as `TBD` instead of invented values. Source: `_REFERENCES.md`; source gap. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards (Class I Zone 2, Gas Groups IIA/IIB; API RP 505 fugitive-emission basis) | Applicable to electrical equipment, conduit sealing, and installation classification. | Applicable; package-specific classification TBD. |
| NEMA MG1 | Applicable to driven-motor basis cited in DBM for inverter-duty service; applicability to PKG-017 depends on driven-motor identification. | Conditionally applicable; driven-equipment identity TBD. |
| SCA-001 VE #34 (starting VFDs) and VE #37 (capacitor-bank removal where VFDs are present) | Governing supersession items for MV VFD basis. | Authoritative governance items from DBM. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, objectives, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare Scope of Work identity fields to workbook row 19 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare interface matrix in the Scope of Work to `INTERFACE_REGISTER.csv` rows for `PKG-017`. | All six applicable interfaces are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| DBM-VFD basis consistency | Confirm starting-VFD basis (SCA-001 VE #34), capacitor-bank policy (VE #37), MCC interface, and MV service voltage match DBM text. | No unsupported deviation. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD`s. | No unresolved internal inconsistency. |
| Title-vs-DBM rating conflict | Confirm the workbook-title-versus-DBM-rating issue is recorded in the Guidance Conflict Table and carried as `NEEDS_HUMAN_RULING`. | Conflict captured; values remain `TBD` until human ruling. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package scope of work (EPC Scope of Work).
- Tagged equipment and package identity list (source-supported entries only; gaps as `TBD`).
- Package function and whole-facility integration narrative.
- Package responsibility assignment record.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 19, applicable Gate 7 registers, and the DBM electrical source slices used for MV service basis, 4160V MCC, VFD governance items, raceway/maintenance-access basis, and area classification.
