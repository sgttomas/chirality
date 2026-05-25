# Specification: DEL-032-02_package-datasheet

## Scope

This specification governs the EPC Integrator-authored Package Datasheet for `PKG-032`, the Cathodic Protection Design and Installation package. The datasheet is a mandatory Gate 5 EPC anchor deliverable and shall provide the technical handoff basis required for third-party vendor or discipline package engineering and design of the facility cathodic protection (CP) system.

The package is a vendor-owned Electrical package under WBS 03. The Package Vendor owns CP package engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed CP design calculations (anode sizing, current-density calculations, soil-resistivity surveys, rectifier sizing) and final equipment selections are excluded from this EPC datasheet unless later provided as vendor data.
- Package-specific CP system type, protected asset list, rectifier rating, anode counts, test-station scheme, and installation locations are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-032-02-001 | The Package Datasheet shall identify `PKG-032`, workbook row 34, WBS 03, CoA tracking number 26020-03-30-023, discipline Electrical, and package name "Cathodic Protection Design and Installation." Source: Workbook Packages row 34; `PACKAGE_REGISTER.csv`. | Datasheet identification review against workbook row and Gate 7 registers. |
| REQ-032-02-002 | The Package Datasheet shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-032`. | Responsibility statement review against Gate 7 package register. |
| REQ-032-02-003 | The Package Datasheet shall include the four applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network. Source: Workbook Packages row 34; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-032`. |
| REQ-032-02-004 | The Package Datasheet shall record the facility-design scope position for CP as stated in the applicable DBM source: the Deepcut DBM excludes CP engineering and supply from the facility design and assigns CP engineering/supply to the owner with facility-side interface support; the Comp & Liquids DBM identifies CP as part of the electrical design scope. The Datasheet shall surface this difference rather than silently choosing one. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Cathodic Protection" section; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical scope paragraph. | Source-citation review; conflict captured in Guidance Conflict Table. |
| REQ-032-02-005 | The Package Datasheet shall not assign unsupported CP-specific technical values (system type, rectifier rating, anode count, protected asset list, test-station locations). Such values shall be marked `TBD` until vendor data or source-supported design basis is accepted. Source: `_REFERENCES.md`; source gap. | Gap review before vendor handoff. |
| REQ-032-02-006 | The Package Datasheet shall require coordination between CP bonding and the facility grounding basis, without overstating package-specific bonding details not present in source. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical/grounding context. | Electrical interface review. |
| REQ-032-02-007 | The Package Datasheet shall carry CP monitoring and control signal interfaces as I&C / Control Cabling and Communications / Network interface facts; detailed signal counts, protocols, and addressing are TBD pending vendor data. Source: `INTERFACE_REGISTER.csv` rows for `PKG-032`. | Interface matrix consistency check. |
| REQ-032-02-008 | The Package Datasheet shall identify source gaps for CP system type, protected assets, rectifier sizing, anode sizing, test-station scheme, and installation location as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before vendor handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation basis for CP rectifier AC feeds, conduit, and bonding referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Industry CP standards (e.g., NACE/AMPP SP-series) | Likely applicable to CP design, installation, and testing for facility buried assets. | ASSUMPTION: likely applicable; not cited in accessible source slices; clause locations TBD until confirmed. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare datasheet identity fields to workbook row 34 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare datasheet matrix to `INTERFACE_REGISTER.csv` rows for `PKG-032`. | Electrical Power, Grounding / Bonding, I&C / Control Cabling, and Communications / Network are present. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Facility-scope position | Confirm both DBM positions (Deepcut exclusion vs. Comp & Liquids inclusion) are surfaced. | Conflict appears in Guidance Conflict Table and is not silently resolved. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Package technical datasheet.
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 34, applicable Gate 7 registers, and the DBM electrical source slices used for CP scope-position evidence.
