# Specification: DEL-060-05_vendor-document-turnover-package

## Scope

This specification governs the Package Vendor-authored Vendor Document Turnover Package for `PKG-060`, the Tank Farm Pump Building 4-25. The deliverable comprises the vendor document register, vendor document submittals, source-required vendor documentation captured as artifacts, and turnover records, with EPC Integrator interface/integration review.

The package is a vendor-owned Mechanical pump-building package under WBS 01 (CoA tracking number 26020-01-18-001). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- EPC-authored deliverables (Scope of Work, Package Datasheet, Construction Work Package, EPC Vendor Package Review and Acceptance) are not produced by this deliverable; they are covered by their own DEL-060 entries.
- The detailed vendor document numbering convention, submittal acceptance criteria, and turnover record templates are `TBD` because the accessible source set does not include an extracted package-specific vendor-document specification (`26020-Package_Requirements.docx package heading 15` is referenced but not extracted to markdown for this run).

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-060-05-001 | The Vendor Document Turnover Package shall identify `PKG-060`, workbook row 85, WBS 01, CoA tracking number 26020-01-18-001, discipline Mechanical, and package name "Tank Farm Pump Building 4-25." Source: Workbook Packages row 85; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-060-05-002 | The Vendor Document Turnover Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces and performs vendor-document interface/integration review feeding `DEL-060-06`. Source: `PACKAGE_REGISTER.csv` row `PKG-060`; `DELIVERABLE_REGISTER.csv` rows `DEL-060-05`, `DEL-060-06`. | Responsibility statement review. |
| REQ-060-05-003 | The Vendor Document Turnover Package shall include the four anticipated artifact categories: vendor document register, vendor document submittals, source vendor document table rows as artifacts where available, and turnover records. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. | Artifact-set completeness review. |
| REQ-060-05-004 | The vendor document register shall enumerate, at minimum, the vendor document categories and items recorded in `ARTIFACT_REGISTER.csv` for `DEL-060-05`. These include: Core vendor documents (Vendor Document Index, Vendor Document Control Procedure, Supplier Quality Plan, ITP, MTRs/Certificates, Inspection Release Certificate, Manufacturing Record Book / Vendor Data Book, Logistics/Shipping Plan, SPIR, Vendor Data Book / Final Supplier Documentation); Core package engineering (Mechanical Design Basis, Mechanical Equipment List, Mechanical Equipment Data Sheets, Package Equipment Specifications, Mechanical Calculation Package, Equipment GA Drawing, Equipment Installation/Setting Drawings, Lifting/Handling Study, Equipment FAT Procedure and Report, Vendor Data Book / Mechanical Final Documentation, Mechanical Spares/Special Tools Requirements, Mechanical Equipment IOM Manual). Source: `ARTIFACT_REGISTER.csv` rows for `DEL-060-05`. | Register completeness check against `ARTIFACT_REGISTER.csv`. |
| REQ-060-05-005 | The vendor document register shall include rotating-equipment/pump vendor documents required by the pump-building scope: Rotating Equipment Specifications, Pump Data Sheets, Mechanical Seal / Lube Oil Specification, Pump Hydraulic / NPSH Calculations, and Motor Starting Study. Source: `ARTIFACT_REGISTER.csv` Rotating equipment / pumps category; pump-building scope basis in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2555, 2618-2622. | Rotating-equipment artifact coverage check. |
| REQ-060-05-006 | The vendor document register shall include relief/flare/vent design vendor documents: Relief and Flare Design Basis, PSV/Pressure Relief Sizing Calculations, Relief Valve Data Sheets, Flare Load Summary, and Blowdown/Depressurization Study. Source: `ARTIFACT_REGISTER.csv` Relief / flare / vent design category; `INTERFACE_REGISTER.csv` `IFC-89861F9A53`. | Relief artifact coverage check. |
| REQ-060-05-007 | The vendor document register shall include process-piping interface vendor documents: P&IDs, Piping Line List, Tie-In List / Tie-In Scope Sheets, Equipment Arrangement / Piping General Arrangement, Piping Plans and Sections, Piping Isometrics, Fabrication Isometrics with BOM, Piping MTO, Valve Data Sheets, Hydrotest/Pressure Test Packages, Flushing/Cleaning/Drying Procedure, and Piping As-Built Drawings. Source: `ARTIFACT_REGISTER.csv` Process piping interfaces category; `INTERFACE_REGISTER.csv` `IFC-40CB9DE2A3`. | Process-piping artifact coverage check. |
| REQ-060-05-008 | The vendor document register shall include utility-piping, drainage/containment, electrical and grounding, EHT, I&C, building/HVAC/code, fire-and-gas/technical-safety, and structural/access vendor documents enumerated for these categories in `ARTIFACT_REGISTER.csv`. Source: `ARTIFACT_REGISTER.csv` rows for `DEL-060-05`; `INTERFACE_REGISTER.csv` rows for `PKG-060`. | Category coverage check against `ARTIFACT_REGISTER.csv` and `INTERFACE_REGISTER.csv`. |
| REQ-060-05-009 | The Vendor Document Turnover Package shall preserve all fourteen PKG-060 interface facts (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) and provide vendor documentation supporting each applicable interface. Source: Workbook Packages row 85; `INTERFACE_REGISTER.csv` rows for `PKG-060`. | Interface coverage check against `INTERFACE_REGISTER.csv`. |
| REQ-060-05-010 | The Vendor Document Turnover Package shall record source gaps as `TBD` rather than invented requirements. Items where source slices do not define content (vendor document numbering scheme, turnover record templates, submittal acceptance criteria, specific cathodic protection artifact, vendor sparing list specifics) shall be `TBD` until vendor data or extracted source resolves them. Source: source-availability gap; `_REFERENCES.md` missing-references note. | Gap review before turnover acceptance. |
| REQ-060-05-011 | Individual source vendor document table rows (Vendor Engineering Deliverables table in `26020-Package_Requirements.docx`) shall be captured as artifacts/evidence, not promoted to separate deliverables. Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes column. | Artifact-versus-deliverable check. |
| REQ-060-05-012 | The Vendor Document Turnover Package shall be subject to EPC Integrator interface/integration review and shall feed `DEL-060-06_epc-vendor-package-review-and-acceptance`. Source: `DELIVERABLE_REGISTER.csv` rows `DEL-060-05`, `DEL-060-06`. | Handoff review against `DEL-060-06`. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 15 (Vendor Engineering Deliverables table) | Defines the package-specific vendor document categories and items. | Applicable; source text not extracted to markdown for this run; vendor-document categories used here are taken from `ARTIFACT_REGISTER.csv` rows derived from this source. |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Defines the pump-building scope (pump complement, duties, basic process tie-ins) that vendor documentation must address. | Applicable. |
| Project vendor document control specification | Governs vendor document numbering, submittal workflow, and turnover format. | ASSUMPTION: applicable; document location TBD (no accessible source slice). |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare turnover package identification to workbook row 85 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact-set completeness | Confirm the four anticipated artifact categories (register, submittals, source rows, turnover records) are present. | All four categories are produced or explicitly marked `TBD` with rationale. |
| Vendor document category coverage | Compare vendor document register to `ARTIFACT_REGISTER.csv` category headers for `DEL-060-05`. | All artifact-register category headers are addressed; gaps are explicit. |
| Rotating-equipment artifact coverage | Compare vendor documents to `ARTIFACT_REGISTER.csv` Rotating equipment / pumps category. | All listed rotating-equipment artifacts are produced or explicitly excluded with rationale. |
| Interface coverage | Compare vendor documents to `INTERFACE_REGISTER.csv` rows for `PKG-060`. | All fourteen interface facts have corresponding vendor documentation or a recorded gap. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| EPC review handoff | Confirm the turnover package is presented to `DEL-060-06`. | Handoff evidence recorded. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register (per `ARTIFACT_REGISTER.csv` row `ART-0D208A7734`).
- Vendor document submittals (one per register row, per Package Vendor submittal workflow).
- Source vendor document table rows captured as artifacts where available (per `ARTIFACT_REGISTER.csv` rows for `DEL-060-05`).
- Turnover records (final supplier documentation, vendor data books, IRC, MTRs, MRB; per `ARTIFACT_REGISTER.csv` Core vendor documents category).
- Source-gap / `TBD` list for vendor or human resolution (numbering scheme, turnover record templates, submittal acceptance criteria, CP artifact location).

The deliverable shall cite the Gate 7 snapshot, workbook row 85, applicable Gate 7 registers, and the DBM 4-25 source slices used for package scope basis.
