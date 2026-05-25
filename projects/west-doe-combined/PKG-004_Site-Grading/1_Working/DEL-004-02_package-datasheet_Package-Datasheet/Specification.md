# Specification: DEL-004-02_package-datasheet — Package Datasheet

## Scope

This specification governs the EPC Integrator package datasheet for PKG-004 Site Grading. The datasheet is the technical handoff deliverable for the Civil Site Grading package under WBS 02 and CoA tracking number 26020-01-42-003.

The deliverable shall cover:

- package identity and source basis from Workbook Packages row 5;
- civil/site grading data needed for discipline package engineering and design;
- the declared interface facts for Drain / Containment and Grading / Site Drainage / Spill Containment;
- source-supported design conditions from the 03-25 DBM civil, drainage, site data, and construction-scope sections;
- package interface requirements matrix evidence carried as datasheet content.

The deliverable shall not close package-specific exclusions, final hydrology, final geotechnical, or unstated construction criteria where the accepted source set leaves those items open. Those items remain `TBD` or require human/design authority ruling.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `PACKAGE_REGISTER.csv`; `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 5.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-004-02-001 | The datasheet shall identify PKG-004 as Site Grading, Discipline Civil, WBS 02, Workbook ID 4, Workbook Packages row 5, and CoA tracking number 26020-01-42-003. Source: Gate 7 `PACKAGE_REGISTER.csv`; workbook row 5. | Check datasheet Identification section against Gate 7 registers and workbook row 5. |
| REQ-004-02-002 | The datasheet shall state that the package has recorded interfaces for Drain / Containment and Grading / Site Drainage / Spill Containment. Source: Gate 7 `INTERFACE_REGISTER.csv`; workbook row 5. | Check interface matrix against Gate 7 interface IDs IFC-FA26BF6895 and IFC-D2D12F4CA2. |
| REQ-004-02-003 | The datasheet shall preserve the Gate 7 artifact intent: package technical datasheet, vendor engineering handoff basis, and package interface requirements matrix. Source: Gate 7 `ARTIFACT_REGISTER.csv`. | Check produced datasheet sections map to ART-9A243FF51E, ART-14CC383E7F, and ART-51CD6E8AF8. |
| REQ-004-02-004 | The datasheet shall include civil design conditions that are explicitly available from the 03-25 DBM, including elevation 673 m AMSL, design ambient temperature -40 deg C to +35 deg C, and the status of preliminary geotechnical and hydrology bases. Source: 03-25 DBM SEC-02 and SEC-11. | Check conditions table for the values and their open-status qualifiers. |
| REQ-004-02-005 | The datasheet shall require civil/site grading content to address grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security where applicable to Site Grading. Source: 03-25 DBM SEC-11 Site and Civil Conditions. | Check Construction section for each named civil design coverage item or `TBD` if not applicable. |
| REQ-004-02-006 | The datasheet shall require surface-water management to prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. Source: 03-25 DBM SEC-11 Surface Water and Drainage. | Check surface-water and drainage requirements in datasheet and procedure verification. |
| REQ-004-02-007 | The datasheet shall state that retention pond sizing and drainage design use the current precipitation and storm basis until hydrology is updated. Source: 03-25 DBM SEC-11 Surface Water and Drainage; SEC-02 rainfall basis. | Check that hydrology finality is not overstated. |
| REQ-004-02-008 | The datasheet shall state that process-contaminated drainage routes to the appropriate drain or containment system rather than surface-water discharge. Source: 03-25 DBM SEC-11 Surface Water and Drainage. | Check interface matrix and drainage narrative. |
| REQ-004-02-009 | The datasheet shall list civil/structural governing content as NBCC, geotechnical report, site data, civil drawings, and surface-water management, with unavailable source documents marked `location TBD` or `TBD`. Source: 03-25 DBM SEC-15 table. | Check Standards section and unresolved items. |

## Standards

| Standard / Governing Content | Status in Current Source Set | Source |
|---|---|---|
| NBCC | Referenced; clause-level source text not available in deliverable folder. | 03-25 DBM SEC-15 table; location TBD |
| Final geotechnical report | Required before foundation design closure; report not available in current deliverable-local source set. | 03-25 DBM SEC-02 and SEC-11 |
| Site data | Current basis available in 03-25 DBM; detailed source artifacts not copied locally. | 03-25 DBM SEC-02 |
| Civil drawings | Must be verified before final issue; drawings not available in current deliverable-local source set. | 03-25 DBM SEC-11 Layout Basis |
| Surface-water management | Required governing content; hydrology update remains pending. | 03-25 DBM SEC-02 and SEC-11 |
| Environmental/regulatory | BCER permits, water regulations, consultation/notification, and waste management permit are referenced in DBM governing content; source documents not available in deliverable-local source set. | 03-25 DBM SEC-15 table; location TBD |

## Verification

| Verification Item | Method |
|---|---|
| Identity and scope | Compare against `_CONTEXT.md`, Gate 7 `PACKAGE_REGISTER.csv`, and Gate 7 `DELIVERABLE_REGISTER.csv`. |
| Interface facts | Compare workbook row 5 X-columns and Gate 7 `INTERFACE_REGISTER.csv` for Drain / Containment and Grading / Site Drainage / Spill Containment. |
| Civil design conditions | Compare values and qualifiers against 03-25 DBM SEC-02 and SEC-11. |
| Open assumptions | Confirm all unavailable final inputs, including final geotechnical report, hydrology update, civil drawings, and package-specific exclusions, remain marked `TBD` or source-limited. |
| Cross-document consistency | Confirm Datasheet, Guidance, and Procedure use the same package identity, interface names, and open-item wording. |

## Documentation

Required datasheet package records:

- package technical datasheet;
- vendor or discipline engineering handoff basis;
- package interface requirements matrix;
- source-supported equipment and design criteria, with unsupported values marked `TBD`;
- source list and open source-gap list;
- verification record against Gate 7 registers, workbook row 5, and 03-25 DBM civil/site drainage source slices.
