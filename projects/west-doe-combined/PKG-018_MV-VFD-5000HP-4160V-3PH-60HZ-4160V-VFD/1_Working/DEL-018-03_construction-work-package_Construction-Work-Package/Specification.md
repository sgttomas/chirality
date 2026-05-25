# Specification: DEL-018-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-018`, the "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 02 with CoA tracking number 26020-02-30-009. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC construction work package unless later provided as vendor data.
- Detailed VFD ratings, topology, harmonic mitigation, cooling, enclosure class, bypass configuration, weights, dimensions, lift plans, modular split, foundation loads, cable schedules, and commissioning hold points are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-018-03-001 | The Construction Work Package shall identify `PKG-018`, workbook row 20, WBS 02, CoA tracking number 26020-02-30-009, discipline Electrical, and package name "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 20; `PACKAGE_REGISTER.csv` row `PKG-018`. | Identification review against workbook row and Gate 7 registers. |
| REQ-018-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and construction tie-ins. Source: `PACKAGE_REGISTER.csv` row `PKG-018`. | Responsibility statement review against Gate 7 package register. |
| REQ-018-03-003 | The Construction Work Package shall include all six applicable PKG-018 interface facts in the construction interface and turnover checklist: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 20; `INTERFACE_REGISTER.csv`. | Construction interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-018`. |
| REQ-018-03-004 | The Construction Work Package shall require installation and tie-in workface planning aligned with the facility construction scope (mechanical hookups, home-run cabling, terminations, pipe supports, tie-ins, and module offloading/setting). Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, construction scope paragraph. | Workface plan review against DBM construction scope. |
| REQ-018-03-005 | The Construction Work Package shall coordinate VFD tie-in to the 4160V MCC, including field-fused contactor, motor protection relay, and EtherNet/PRP communication to the plant PLC central control panel. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC and BPCS/RIO sections. | Tie-in verification against detailed-design electrical and controls drawings. |
| REQ-018-03-006 | The Construction Work Package shall conform to facility grounding basis (two-point ground-grid connection for major electrical equipment; separate CEC-sized copper ground conductors for distribution transformers, panelboards, and three-phase motors larger than 100 hp). Package-specific application shall be confirmed by detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Grounding installation inspection against detailed-design drawings. |
| REQ-018-03-007 | The Construction Work Package shall require cable tray and conduit routing that preserves maintenance access for the VFD equipment and its tie-in interfaces. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray and conduit paragraph. | Maintenance access walkdown. |
| REQ-018-03-008 | The Construction Work Package shall record harmonic and reactive-power mitigation actions only after detailed electrical studies complete; capacitor banks are removed from the synchronous bus on MCC-8200 where VFDs are present per SCA-001 VE #37. Construction shall not introduce mitigation outside accepted detailed-design output. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 4160V MCC section. | Detailed-design output review prior to installation of mitigation equipment. |
| REQ-018-03-009 | The Construction Work Package shall be aligned to the plot plan, equipment list, and construction work package register before issue for construction. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, miscellaneous facilities alignment paragraph. | Issue-for-construction readiness review. |
| REQ-018-03-010 | The Construction Work Package shall preserve TBDs for VFD ratings/topology, modular split, lift plan, foundation loads, cable schedules, installation location, pre-energization checks, and commissioning hold points until source-supported package-specific basis or vendor data is accepted. Source: `_REFERENCES.md`; source-gap review. | Gap review before turnover. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding/bonding sizing and electrical installation basis referenced by DBM. | Applicable; clause locations TBD. |
| NEMA MG1 (motor basis) | Applicable to the driven motor basis (inverter-duty, Class F insulation, Class B rise, etc.) under SCA-001 VE #34. | Applicable to motor; VFD-specific clauses TBD. |
| Project electrical and construction specifications | Voltage, MCC, grounding, cable, raceway, and construction installation basis referenced by DBM. | Applicable; document locations TBD. |
| Area classification standards | Applicable to electrical equipment placement, conduit sealing, and installation in any classified area. | Applicable; package location/classification TBD. |
| SCA-001 VE #34 and #37 | Establish starting-VFD basis for the inlet compressor motors and remove synchronous-bus capacitor banks on MCC-8200 where VFDs are present. | Authoritative SCA actions cited by DBM. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, interface facts, and objectives. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 20 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare construction interface and turnover checklist to `INTERFACE_REGISTER.csv` rows for `PKG-018`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are `TBD`/`ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare construction work package responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Workface plan alignment | Compare installation and tie-in workface plan to DBM construction scope and Package Datasheet. | No unscoped work introduced; all listed work traces to accepted basis. |
| Tie-in completeness | Walkdown VFD-to-4160V MCC and BPCS/PRP tie-ins. | All declared tie-ins installed, tested, and recorded. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Turnover record completeness | Construction interface and turnover checklist completed with sign-offs. | All interface tie-ins are closed or carried as known open items into commissioning. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 20, applicable Gate 7 registers, and the DBM construction/electrical source slices used for installation and tie-in basis.
