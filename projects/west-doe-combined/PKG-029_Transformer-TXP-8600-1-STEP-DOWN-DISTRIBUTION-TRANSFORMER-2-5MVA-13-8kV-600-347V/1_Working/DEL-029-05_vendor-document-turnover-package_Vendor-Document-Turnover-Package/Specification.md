# Specification: DEL-029-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor Vendor Document Turnover Package for `PKG-029`, the Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER (2.5 MVA, 13.8 kV / 600 / 347 V). The deliverable provides the vendor document register, submittals, source-required vendor documentation, and turnover records for the package, with EPC Integrator interface/integration review.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration, and review of vendor documentation.

Exclusions:

- This deliverable does not author EPC documents (Scope of Work, Package Datasheet, Construction Work Package, or EPC review/acceptance log).
- This deliverable does not perform vendor package engineering or design itself; it organizes and turns over the documentation that results from `DEL-029-04` and supporting vendor work.
- Detailed vendor-document content classes, submittal stages, and turnover records that are not present in the accessible source set remain `TBD` and are not invented here.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-029-05-001 | The Vendor Document Turnover Package shall identify `PKG-029`, workbook row 31, WBS 01, CoA tracking number 26020-01-30-020, discipline Electrical, tagged equipment TXP-8600-1, and package name "Transformer TXP-8600-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V." Source: Workbook Packages row 31; `PACKAGE_REGISTER.csv`. | Identity field review against workbook row and Gate 7 registers. |
| REQ-029-05-002 | The deliverable shall state the responsibility split: Package Vendor owns vendor documentation; EPC Integrator performs interface/integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-029`; `_CONTEXT.md`. | Responsibility statement review against Gate 7 package register. |
| REQ-029-05-003 | The deliverable shall include a vendor document register listing all vendor documents for `PKG-029`, with document number, title, revision, status, submittal date, review disposition, and turnover status. Where source material does not enumerate document classes, the register shall be populated by the Package Vendor consistent with the project document control procedure. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, mechanical packages paragraph (line 617); `ARTIFACT_REGISTER.csv` row `ART-91D8A203E0`. | Register completeness review at submittal milestones and turnover. |
| REQ-029-05-004 | The deliverable shall include vendor submittals covering, at minimum, certified drawings (general arrangement, electrical schematics, foundation/anchorage), nameplate data, factory acceptance test reports, O&M manuals, and recommended spare parts. Submittal-stage enumeration and project-specific document classes beyond this minimum remain `ASSUMPTION` pending project document control procedure confirmation. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, mechanical packages paragraph (line 617); Source gap for project document control procedure. | Submittal completeness review against vendor document register. |
| REQ-029-05-005 | The deliverable shall include turnover records sufficient for EPC integration acceptance, including final certified documentation, completed factory test evidence, and warranty/spares documentation. Specific turnover record types not present in accessible source material remain `TBD` pending project turnover procedure. Source: `_CONTEXT.md` (turnover records); Source gap for enumerated turnover types. | Turnover-completeness review at handoff to `DEL-029-06`. |
| REQ-029-05-006 | Vendor documentation shall represent the seven interface facts for `PKG-029`: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports. Source: Workbook Packages row 31; `INTERFACE_REGISTER.csv` rows for `PKG-029`. | Interface coverage check against `INTERFACE_REGISTER.csv` rows for `PKG-029`. |
| REQ-029-05-007 | Vendor grounding documentation shall be consistent with the DBM electrical design basis: major electrical equipment connected to the ground grid at two points; distribution transformers shall have a separate copper ground conductor sized per CEC; 600 V transformers grounded by 5 A continuous high-resistance grounding resistor. Package-specific applicability shall be confirmed during detailed engineering. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs (lines 2985, 2989, 2991). | Vendor grounding document review against DBM grounding slice and CEC. |
| REQ-029-05-008 | Vendor foundation/support documentation shall be consistent with the DBM transformer foundation basis (precast concrete bearing foundations; structural steel transformer bases) and shall enable EPC structural design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundations and transformers paragraphs (lines 2745, 2949). | Vendor structural document review against DBM transformer slice. |
| REQ-029-05-009 | If supplied as oil-filled, vendor documentation shall address CEC spacing and a secondary containment review; transformer selection shall avoid or limit containment requirements where practical. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph (line 2949). | Vendor documentation review against DBM transformer slice; verify CEC spacing and containment statements. |
| REQ-029-05-010 | The deliverable shall mark unsupported document classes, submittal stages, and turnover record types as `TBD` rather than inventing values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` has no accessible `PKG-029` match. | TBD/open-item review before turnover handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding sizing, transformer spacing, electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage, grounding, cable, raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Project document control procedure | Governs vendor submittal stages, numbering, transmittal, review disposition, and turnover handoff. | ASSUMPTION: a project document control procedure exists; document location TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity fields to workbook row 31 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface coverage | Compare vendor documentation set to `INTERFACE_REGISTER.csv` rows for `PKG-029`. | All seven interface facts are represented in vendor documentation. |
| Source fidelity | Check every non-trivial requirement against cited DBM source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as confirmed requirements. |
| Register completeness | Inspect vendor document register at each submittal milestone and at turnover. | Register lists all submitted documents with status; missing items marked `TBD` with owner. |
| Turnover completeness | Inspect turnover records at handoff to `DEL-029-06` (EPC Vendor Package Review and Acceptance). | Turnover set is sufficient for EPC review and acceptance; gaps recorded as `TBD` for human ruling. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register.
- Vendor document submittals (per register).
- Source vendor document table rows captured as artifacts/evidence where available.
- Turnover records.
- `TBD` / open-item list for unresolved document classes, submittal stages, or turnover content.

The deliverable shall cite the Gate 7 snapshot, workbook row 31, applicable Gate 7 registers, and DBM source slices used for grounding, transformer foundation, voltage system context, and mechanical/equipment package deliverable expectations.
