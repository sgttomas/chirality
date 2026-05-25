# Specification: DEL-037-01_scope-of-work — Scope of Work

## Scope

This deliverable specifies the EPC scope-of-work content for `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)`, a vendor-owned Electrical package under WBS 01 with CoA tracking number `26020-01-30-028`. It covers the package identity, source basis, package function, scope inclusions, exclusions/deferred items, applicable interface types, responsibility assignment, and whole-facility integration narrative for the 880-1 electrical building.

Included scope:

- Carry `SOW-0038`: workbook-defined vendor-responsible Electrical package "5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)" as a distinct flat project package; Package Vendor owns engineering/design/equipment and EPC Integrator owns facility integration (`SCOPE_LEDGER.csv`, `SOW-0038`).
- Document the twelve declared interface types for PKG-037 (`INTERFACE_REGISTER.csv`, rows for `PKG-037`).
- Align the scope narrative with the SEC-12 Electrical Basis for electrical buildings, grounding, cable systems, and area classification where source-supported (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12).
- Record package-specific design values not present in accessible sources as `TBD` rather than inferring them from the package name or general electrical text.

Excluded or deferred scope:

- Package-specific exclusions are `TBD`; no source-specific exclusions are stated for PKG-037 (`PACKAGE_REGISTER.csv`, `PKG-037`).
- 880-1 building location, area assignment, dimensions, foundation design, and tagged equipment list remain `TBD` because the accessible DBM building designations table does not enumerate an 880-1 building.
- 5 kV switchgear bus voltage, rating, lineup, breaker count, protection scheme, transformer feeder origin, and load assignments remain `TBD` because the accessible SEC-12 system-voltages table does not list a 5 kV medium-voltage service class (it lists 13.8 kV, 6.9 kV, and 4.160 kV medium-voltage services and a 5 kV cable insulation rating for 4.160 kV cable).
- Vendor engineered equipment scope content is owned by `DEL-037-04_vendor-engineered-equipment-package`, not by this scope-of-work deliverable.
- Vendor documentation/turnover scope is owned by `DEL-037-05_vendor-document-turnover-package`, not by this scope-of-work deliverable.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-037-01-01 | The scope of work shall identify `PKG-037 — 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1)` as a vendor-owned Electrical package under WBS 01 with CoA tracking number `26020-01-30-028`. | `PACKAGE_REGISTER.csv`, `PKG-037` |
| REQ-037-01-02 | The scope of work shall identify `SOW-0038` as the covered scope item and retain the package as a distinct flat project package. | `SCOPE_LEDGER.csv`, `SOW-0038` |
| REQ-037-01-03 | The scope of work shall include the mandatory EPC scope-of-work artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | `DELIVERABLE_REGISTER.csv`, `DEL-037-01_scope-of-work`; `ARTIFACT_REGISTER.csv` rows for `DEL-037-01_scope-of-work` |
| REQ-037-01-04 | The scope of work shall include the twelve declared interface types for PKG-037: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | `INTERFACE_REGISTER.csv`, rows for `PKG-037` |
| REQ-037-01-05 | The scope of work shall record the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv`, `PKG-037` |
| REQ-037-01-06 | The scope of work shall describe the package as an electrical building intended to house medium-voltage switchgear and associated electrical building equipment as determined by detailed design, consistent with the SEC-12 electrical buildings basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" subsection of SEC-12 |
| REQ-037-01-07 | The scope of work shall require the electrical building to be a prefabricated, modular building located in a general purpose area, with HVAC sized n + 1, bottom cable entry, elevated on piles, TECK/ACIC wiring, EMT conduit for adjacent panel interconnections, an outdoor GFI receptacle, and equipment doors or removable transoms sized for the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" subsection of SEC-12 |
| REQ-037-01-08 | The scope of work shall require electrical equipment to comply with CSA C22.1-21 Canadian Electrical Code, applicable BC provincial/local electrical codes, and the requirements of the electrical inspection authority designated by the project owner, with deviations requiring formal owner approval. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Governing Codes, Standards, Specifications, and Studies" paragraph of SEC-12 |
| REQ-037-01-09 | The scope of work shall require all major electrical equipment to be directly connected to the ground grid at two points and require ground wells at the electrical building for maintenance and operational testing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Grounding and Bonding" subsection of SEC-12 |
| REQ-037-01-10 | The scope of work shall carry the 880-1 building tag from the workbook package name and shall record building location, area assignment, and adjacency to specific process modules as `TBD` because accessible source does not enumerate an 880-1 building. | Workbook Packages row 39; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building designations table |
| REQ-037-01-11 | The scope of work shall carry "5kV switchgear" from the workbook package name and shall record bus voltage class, rating, lineup, breaker count, protection scheme, and transformer feeder origin as `TBD` because accessible source does not enumerate a 5 kV medium-voltage service. ASSUMPTION: 5 kV class refers to metal-clad switchgear typically used for 4.16 kV systems; final interpretation requires human ruling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 system-voltages table and medium-voltage cable table |
| REQ-037-01-12 | The scope of work shall list package-specific exclusions as `TBD` until source-specific exclusions are stated or ruled. | `PACKAGE_REGISTER.csv`, `PKG-037` |

## Standards

| Standard or governing content | Status | Source |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Applicable to electrical design and installation | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 governing codes paragraph |
| Applicable BC provincial and local electrical codes and regulations | Applicable; specific bulletins not enumerated in accessible source | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 governing codes paragraph |
| Designated electrical inspection authority requirements | Applicable | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 governing codes paragraph |
| CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER | Applicable standards and regulatory bodies; clause locations TBD | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 governing codes paragraph |
| Project electrical and instrumentation specifications (SEC-12 Table 12-1) | Govern the electrical distribution design and equipment procurement basis; the table contents themselves are referenced by the DBM and must be obtained for detailed design | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 governing codes paragraph |
| Third-party certification (CSA, ULc, FM, ETL, or other NRTL) | Required for all supplied electrical equipment | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 governing codes paragraph |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-037-01-01 through REQ-037-01-05 | Check scope-of-work identity, contents, interface list, and responsibility split against Gate 7 registers and Workbook Packages row 39. |
| REQ-037-01-06 through REQ-037-01-09 | Check electrical-building, codes, and grounding language against SEC-12 Electrical Basis source slices. |
| REQ-037-01-10 | Confirm building tag and location with detailed civil/electrical layout or owner ruling before final issue. |
| REQ-037-01-11 | Confirm "5kV switchgear" interpretation, bus voltage, and rating with owner ruling or vendor package response before final issue. |
| REQ-037-01-12 | Carry package-specific exclusions as `TBD`; close out only when stated by source or by ruling. |

## Documentation

The scope-of-work package shall produce or reference:

- Package scope of work (`ART-53C9B45AD0`).
- Tagged equipment and package identity list (`ART-CD3C1783C4`), with `TBD` for individual equipment tags until detailed design.
- Package function and whole-facility integration narrative (`ART-1DFABB8A68`).
- Package responsibility assignment record (`ART-833F44316B`).
- Interface summary covering the twelve declared PKG-037 interfaces.
- Source basis list and open / `TBD` / human-ruling list.
