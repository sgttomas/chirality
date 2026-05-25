# Specification: DEL-027-01_scope-of-work

## Scope

This specification governs the EPC Integrator-authored Scope of Work for `PKG-027`, the Transformer `TXP-8301-1` STEP DOWN DISTRIBUTION TRANSFORMER package, rated 20/26 MVA with voltage relationship 13.8 kV / 6.9 kV / 0.4 kV as labelled in the workbook source. The Scope of Work is a mandatory Gate 5 EPC anchor deliverable and shall define the full package scope, including tagged equipment, package function, source basis, boundaries, whole-facility integration narrative, and responsibility assignment.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, factory test reports, and final equipment selections are excluded from this EPC Scope of Work unless later provided as vendor data.
- Package-specific final ratings (impedance, BIL, cooling class, vector group, tap configuration, noise level, losses), physical location, and finalized winding configuration on the 0.4 kV winding remain `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-027-01-001 | The Scope of Work shall identify `PKG-027`, workbook row 29, WBS 01, CoA tracking number 26020-01-30-018, discipline Electrical, and the package name as written in the workbook ("Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV"). Source: Workbook Packages row 29; `PACKAGE_REGISTER.csv`. | Identity review against workbook row 29 and Gate 7 registers. |
| REQ-027-01-002 | The Scope of Work shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-027`. | Responsibility statement review against Gate 7 package register. |
| REQ-027-01-003 | The Scope of Work shall list the tagged equipment for the package: `TXP-8301-1` step-down distribution transformer. Source: Workbook Packages row 29 (package name). | Tagged equipment list review against workbook row 29. |
| REQ-027-01-004 | The Scope of Work shall describe the package function as a 13.8 kV-to-6.9 kV step-down distribution transformer that supplies the facility 6.9 kV process motor distribution from the facility 13.8 kV switchgear, and shall record the 0.4 kV winding as identified in the workbook label pending source confirmation. Source: Workbook Packages row 29; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical distribution and 6.9 kV MCC paragraphs. | Function narrative review against DBM electrical source slices. |
| REQ-027-01-005 | The Scope of Work shall include the full set of applicable interface facts for `PKG-027`: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 29; `INTERFACE_REGISTER.csv` rows for `PKG-027`. | Interface matrix check against `INTERFACE_REGISTER.csv`. |
| REQ-027-01-006 | The Scope of Work shall require the 6.9 kV side neutral grounding to follow the DBM rule "each 6.9 kV transformer shall be grounded using a 100 A, 10 s neutral grounding resistor and shall operate as a tripping system," and shall require connection to the facility ground grid at two points. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Grounding scope review against DBM grounding paragraphs. |
| REQ-027-01-007 | The Scope of Work shall require CEC-compliant spacing for large oil-filled transformers, structural-steel or precast-concrete bearing foundations, and review of secondary containment per DBM guidance. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers and foundations paragraphs. | Civil/structural and CEC compliance review. |
| REQ-027-01-008 | The Scope of Work shall preserve as `TBD` (not as invented values) the items not supported by accessible source: cooling class (ONAN/ONAF), impedance, BIL, vector group, tap configuration, losses, noise level, weight, oil volume, installation location/building, and the technical role of the labelled 0.4 kV winding. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` search yielded no PKG-027-specific match. | Gap / `TBD` review before vendor handoff. |
| REQ-027-01-009 | The Scope of Work shall record the supported objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` as the directional package-objective association from the Gate 7 objective-deliverable map under the `PACKAGE_HEURISTIC` mode (best-effort, ASSUMPTION). Source: `OBJECTIVE_DELIVERABLE_MAP.csv`. | Objective association review against the Gate 7 map. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical clearance, spacing, grounding/bonding, and installation basis for large oil-filled transformers and electrical-equipment grounding. | Applicable as source-supported design basis; clause locations `TBD`. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by the DBM electrical section. | Applicable; document location `TBD`. |
| Area classification standards | Apply to electrical-equipment installation where hazardous/non-hazardous areas are defined. | Applicable; package area classification `TBD`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |
| Industry transformer standards (e.g., CSA/IEEE/IEC for power transformers) | Applicable to vendor design and factory testing of the 20/26 MVA transformer. | `ASSUMPTION`; specific standard selection deferred to vendor and EPC review. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare Scope of Work identity fields to workbook row 29 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Tagged equipment | Compare tagged equipment to workbook row 29 package name. | `TXP-8301-1` is identified. |
| Function and integration narrative | Trace function narrative to DBM electrical source slices. | Narrative is consistent with the 13.8 kV switchgear distribution to the 6.9 kV motor distribution. |
| Interface completeness | Compare scope interface list to `INTERFACE_REGISTER.csv` rows for `PKG-027`. | All seven interface facts are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` row `PKG-027`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package scope of work narrative.
- Tagged equipment and package identity list.
- Package function and whole-facility integration narrative.
- Responsibility assignment record (Package Vendor / EPC Integrator split).
- Package interface fact list with cross-references to `INTERFACE_REGISTER.csv`.
- Source-gap / `TBD` and `ASSUMPTION` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 29, applicable Gate 7 registers, and the DBM electrical source slices used for the 13.8 kV/6.9 kV distribution basis and transformer installation guidance.
