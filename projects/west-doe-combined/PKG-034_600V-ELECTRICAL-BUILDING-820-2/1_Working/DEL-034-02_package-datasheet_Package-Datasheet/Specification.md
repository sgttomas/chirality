# Specification: DEL-034-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-034`, the 600V ELECTRICAL BUILDING (820-2) package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Building-specific equipment ratings, internal equipment list and quantities, single-line, plot location, transformer feeder source, HVAC unit sizing, and detailed area classification are `TBD` because the accessible source set does not provide confirmed PKG-034 / 820-2 building-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-034-02-001 | The Package Datasheet shall identify `PKG-034`, workbook row 36, WBS 02, CoA tracking number 26020-02-30-025, discipline Electrical, and package name "600V ELECTRICAL BUILDING (820-2)." Source: Workbook Packages row 36; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-034-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-034`. | Responsibility statement review against Gate 7 package register. |
| REQ-034-02-003 | The Package Datasheet shall include all twelve applicable interface facts: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 36; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-034`. |
| REQ-034-02-004 | The Package Datasheet shall describe the building construction basis (prefabricated modular building, general-purpose area location, n+1 HVAC, bottom cable entry, pile-elevated foundation) per the DBM electrical-building basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Source citation review. |
| REQ-034-02-005 | The Package Datasheet shall describe the internal wiring basis (TECK and ACIC cables, EMT conduit between adjacent equipment, outdoor GFI receptacle, equipment doors/transoms sized for removal of the largest equipment). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Source citation review. |
| REQ-034-02-006 | The Package Datasheet shall identify the standby power interface at the 600 V MCC level via low-voltage standby natural-gas generators with transfer switch and shall mark transfer-switch type, emergency bus configuration, generator count, rating, and load-shedding/critical-load list as `TBD`. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and Standby Power section. | TBD/open-item review. |
| REQ-034-02-007 | The Package Datasheet shall capture grounding/bonding requirements applicable to electrical equipment (two-point ground-grid connection, ground wells at electrical buildings, green-insulated above-grade conductors in PVC where mechanical protection is required, compression connections) without overstating package-specific conductor sizing. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Electrical interface review. |
| REQ-034-02-008 | The Package Datasheet shall require cable tray and conduit routing and equipment-door sizing to preserve maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and raceway paragraphs. | Layout/interface review. |
| REQ-034-02-009 | The Package Datasheet shall require foundation design per the final geotechnical report, equipment loads, snow/wind/seismic criteria, frost protection, vibration, settlement, and maintenance access, with equipment-specific foundation and anchorage checks for the electrical building. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, foundations section. | Structural interface review. |
| REQ-034-02-010 | The Package Datasheet shall identify source gaps for PKG-034 / 820-2 internal equipment list, ratings, quantities, single-line, transformer feeder source, plot location, area classification, and HVAC unit sizing as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |
| REQ-034-02-011 | The Package Datasheet shall preserve the workbook tag "820-2" as package identity and shall not infer detailed scope by analogy to other 600 V electrical buildings (e.g., 840-1, 850-1, 860-1) without source confirmation. Source: Workbook Packages row 36; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building enumeration. | Identity/scope review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by the DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification; the DBM places electrical buildings in general-purpose areas. | Applicable; specific PKG-034 classification TBD. |
| Building/HVAC basis | DBM electrical-building HVAC sized n+1; detailed HVAC standard references TBD. | Applicable as design basis. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 36 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-034`. | All twelve interface facts are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| 820-2 identity preservation | Confirm no scope is inferred from sibling electrical buildings without source. | Datasheet does not introduce equipment, ratings, or location for PKG-034 by analogy. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 36, applicable Gate 7 registers, and the DBM electrical-building / 600V MCC source slices used as design basis.
