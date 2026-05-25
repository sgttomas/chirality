# Specification: DEL-017-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package (CWP) for `PKG-017`, the "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD" package. The CWP is a mandatory Gate 5 EPC anchor deliverable and shall describe how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 02 (CoA `26020-02-30-008`). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, factory acceptance test records, and certified equipment drawings are excluded from this CWP except where referenced as construction prerequisites.
- Detailed electrical studies (short-circuit, coordination, harmonics, arc-flash) are not produced by the CWP; CWP shall consume their results as hold points or acceptance criteria once accepted.
- Specific 600 HP motor identity, driven-equipment tag, exact installation location, foundation drawings, and cooling-system configuration are `TBD` because the accessible source set does not provide confirmed package-specific values for PKG-017.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-017-03-001 | The CWP shall identify `PKG-017`, workbook row 19, WBS 02, CoA tracking number 26020-02-30-008, discipline Electrical, and package name "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD". Source: Workbook Packages row 19; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-017-03-002 | The CWP shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. Source: `PACKAGE_REGISTER.csv` row `PKG-017`. | Responsibility-statement review against Gate 7 package register. |
| REQ-017-03-003 | The CWP shall produce the three required artifacts: construction work package (ART-1C1724D3C4), installation and tie-in workface plan (ART-65539C633A), and construction interface and turnover checklist (ART-3A7676CD16). Source: `ARTIFACT_REGISTER.csv` rows for `DEL-017-03`. | Artifact register completeness check. |
| REQ-017-03-004 | The CWP shall address each of the six applicable interface facts for PKG-017 — Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports — as construction tie-in scopes. Source: `INTERFACE_REGISTER.csv` rows for `PKG-017`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-017-03-005 | The CWP shall require MV power tie-in to originate at the 4160V MCC or other feeder identified by accepted electrical detailed design, with phase rotation, insulation, and protective-relay verification prior to energization. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section. | Pre-energization test record review. |
| REQ-017-03-006 | The CWP shall require segregation of MV power circuits from control and instrument circuits by distance, shielding, or routing per project electrical specifications. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 768. | Field walkdown against project electrical specifications. |
| REQ-017-03-007 | The CWP shall require grounding and bonding of the VFD enclosure and associated equipment to the facility ground grid in accordance with CEC and project electrical specifications. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical grounding paragraphs. | Grounding continuity test record. |
| REQ-017-03-008 | The CWP shall require communication/network tie-in from the VFD to the plant PLC central control panel via the EtherNet path defined at the 4160V MCC unless detailed design specifies an alternate path. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC paragraph. | Communication loop test. |
| REQ-017-03-009 | The CWP shall preserve maintenance-access clearances around the VFD package and require that cable tray and conduit routing not interfere with maintenance access. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings/raceways paragraphs. | Layout walkdown against maintenance-access criteria. |
| REQ-017-03-010 | The CWP shall require foundation, anchorage, and support installation per the accepted civil/structural design, including levelling, grouting, and project loading criteria (snow, wind, seismic, -40 °C). Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, foundations paragraph (line 700). | Foundation inspection and anchor torque records. |
| REQ-017-03-011 | The CWP shall include a construction interface and turnover checklist documenting tie-in completion, inspection, test, and handover evidence to commissioning. Source: `ARTIFACT_REGISTER.csv` row `ART-3A7676CD16`. | Turnover checklist completeness review. |
| REQ-017-03-012 | The CWP shall mark as `TBD` any value (driven-machine identity, foundation drawings, cooling provisions, exact location, lift weights, cable schedules) that is not confirmed by accessible source or accepted detailed design, rather than inventing values. Source: `_REFERENCES.md`; source gap. | Open-item review before issue for construction. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding, conduit support, MV installation, and electrical construction basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable where VFD installation location intersects a classified area; package-specific area classification TBD. | Applicable; package classification TBD. |
| NEMA MG1 (motor basis) | Referenced by DBM for motor compliance generally; relevance to the VFD-driven machine TBD pending identity of the 600 HP motor. | `ASSUMPTION`: applicable to the driven machine; not directly normative on the VFD enclosure. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare CWP identity fields to workbook row 19 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare CWP scope to `INTERFACE_REGISTER.csv` rows for `PKG-017`. | All six interface facts represented as construction tie-in scopes. |
| Artifact completeness | Cross-check artifacts produced against `ARTIFACT_REGISTER.csv` rows for `DEL-017-03`. | All three artifacts present. |
| Source fidelity | Verify each non-trivial value/requirement against cited source slice. | Unsupported values are `TBD` or `ASSUMPTION`, not asserted as construction requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Pre-energization readiness | Confirm hold points exist for grounding continuity, insulation, hi-pot, phase rotation, and relay coordination prior to energization. | Hold-point list present and signed off in turnover checklist. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (ART-1C1724D3C4).
- Installation and tie-in workface plan (ART-65539C633A).
- Construction interface and turnover checklist (ART-3A7676CD16).
- Source-gap / `TBD` list for vendor or human resolution (driven-machine identity, location, foundations, cooling).
- Cross-reference to Gate 7 snapshot, workbook row 19, applicable Gate 7 registers, and the DBM electrical source slices used.
