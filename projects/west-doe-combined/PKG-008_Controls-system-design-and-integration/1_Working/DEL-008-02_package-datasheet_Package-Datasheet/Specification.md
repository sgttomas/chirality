# Specification: Package Datasheet

## Scope

This specification governs the DEL-008-02 package datasheet for PKG-008, Controls system design and integration. The datasheet is an EPC Integrator technical handoff deliverable for the workbook-defined Controls package under WBS 01 and CoA tracking number 26020-01-32-001.

The deliverable shall cover the package technical datasheet, vendor or discipline engineering handoff basis, package interface requirements matrix, and source-supported equipment and design criteria. Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-008-02; Gate 7 `ARTIFACT_REGISTER.csv`, DEL-008-02 rows.

Exclusions: standalone controls power-panel package or deliverable creation is excluded by Gate 6 disposition; controls power-panel interfaces remain interface facts/artifacts under this package datasheet. Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-008 rows.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-001 | The datasheet shall identify PKG-008 as Controls system design and integration, WBS 01, CoA tracking number 26020-01-32-001, discipline Controls. Source: Gate 7 `PACKAGE_REGISTER.csv`, PKG-008. | Confirm fields appear in `Datasheet.md` Identification. |
| REQ-002 | The datasheet shall preserve the accepted responsibility model: EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. Source: Gate 7 `PACKAGE_REGISTER.csv`, PKG-008. | Confirm responsibility language is not replaced with unsupported vendor ownership language. |
| REQ-003 | The datasheet shall include a package interface requirements matrix for Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-008 rows; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row ID #8. | Confirm all applicable interface types are listed consistently. |
| REQ-004 | The datasheet shall retain the interface review note and Gate 6 disposition for controls power-panel interfaces. Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-008 rows. | Confirm note appears in datasheet and guidance/procedure treatment. |
| REQ-005 | The datasheet shall mark detailed equipment, design values, and package-specific controls criteria as `TBD` where accepted sources do not provide a matched source slice. Source: Gate 7 `PACKAGE_REGISTER.csv`, `DocxPackageMatched=FALSE`; `_Sources/26020-Package_Requirements.docx`. | Confirm unsupported values are not invented. |
| REQ-006 | The datasheet shall cite the accepted Gate 7 snapshot and source rows used for non-trivial claims. Source: `_REFERENCES.md`; Gate 7 snapshot registers. | Confirm source citations include file and row/ID references where practical. |

## Standards

| Standard / authority | Status |
|---|---|
| Accepted Gate 7 PROJECT_DECOMP snapshot | Governing decomposition and register authority for this run. |
| Workbook Packages row 9 / exported workbook Packages row ID #8 | Governing package row and interface source for PKG-008. |
| Detailed controls package design standard | TBD - no package-specific standard text is available in the accessible source set for this deliverable. |

## Verification

- Check that all four default document sections are present across the kit.
- Check that datasheet identity fields match `_CONTEXT.md`, Gate 7 `DELIVERABLE_REGISTER.csv`, and Gate 7 `PACKAGE_REGISTER.csv`.
- Check that all applicable PKG-008 interface types are present and consistently named in `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
- Check that detailed equipment and design values remain `TBD` unless a future authoritative source slice supplies them.
- Check that the controls power-panel interface note is retained as an interface fact/artifact disposition, not converted into a separate deliverable requirement.

## Documentation

The completed deliverable should include:

- Package technical datasheet.
- Vendor or discipline engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria, with unsupported fields marked `TBD`.
- Source and register traceability to the Gate 7 snapshot and workbook row.
