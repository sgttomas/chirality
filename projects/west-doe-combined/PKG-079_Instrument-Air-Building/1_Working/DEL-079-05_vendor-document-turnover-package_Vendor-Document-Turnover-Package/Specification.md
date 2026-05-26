# Specification: DEL-079-05_vendor-document-turnover-package

## Scope

This specification governs the Vendor Document Turnover Package for `PKG-079`, the Instrument Air Building package. The deliverable is a Gate 5 vendor-owned package deliverable consisting of the vendor document register, vendor document submittals, source-required vendor document table rows carried as artifacts where available, and final turnover records, with EPC Integrator interface/integration review.

The package is a vendor-owned Mechanical (instrument air) package under WBS 01, CoA tracking number 26020-01-39-001. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed-design content (calculations, certified drawings, equipment selections) is conveyed *through* this deliverable as documents (the vendor data books and engineering deliverables) but is not itself authored by this deliverable; the deliverable is the document register, submittals, and turnover record set.
- Items declared "by others" in the source Scope Notes / Open Items (shipping compressor packages to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs) are outside the vendor package supply scope and therefore outside the vendor turnover-document scope.
- Detailed package-specific submittal-stage definitions, hold/issue review codes, transmittal numbering, and turnover acceptance criteria are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-079-05-001 | The deliverable shall identify `PKG-079`, workbook row 69, WBS 01, CoA tracking number 26020-01-39-001, discipline Mechanical, and package name "Instrument Air Building." Source: Workbook Packages row 69; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-079-05-002 | The deliverable shall state the accepted responsibility split: Package Vendor owns vendor documentation and physical equipment; EPC Integrator performs interface/integration review. Source: `PACKAGE_REGISTER.csv` row `PKG-079`; `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`. | Responsibility statement review against Gate 7 register. |
| REQ-079-05-003 | The deliverable shall include a vendor document register covering every required vendor document enumerated in the source Vendor Engineering Deliverables table for heading 32 (Core vendor documents; Core package engineering; Rotating equipment / compressors; Static pressure equipment; Utility piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Instrumentation and controls interfaces; Building / HVAC / code interfaces; Fire and gas / technical safety interfaces; Structural, foundations, supports, access). Source: `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table; `ARTIFACT_REGISTER.csv` rows for `DEL-079-05`. | Register completeness review against the source table and `ARTIFACT_REGISTER.csv` rows. |
| REQ-079-05-004 | The deliverable shall include vendor submittals tracked by the document register, governed by the Vendor Document Control Procedure (`DOC-008`) and indexed by the Vendor Document Index (`PRQ-009`). Source: `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table (Core vendor documents). | Submittal log / transmittal review against `PRQ-009` and `DOC-008`. |
| REQ-079-05-005 | The deliverable shall carry each source-listed Vendor Engineering Deliverables row as an artifact/evidence entry in `ARTIFACT_REGISTER.csv`, not as a separate deliverable. Source: `_CONTEXT.md` notes; `DELIVERABLE_REGISTER.csv` row `DEL-079-05`; `ARTIFACT_REGISTER.csv` rows for `DEL-079-05`. | Artifact register cross-check (artifact count and `SourceRowRef` per source vendor-document code). |
| REQ-079-05-006 | The deliverable shall include final turnover records covering at minimum the source-listed turnover artifacts: Manufacturing Record Book / Vendor Data Book (`QLT-021`), Vendor Data Book / Final Supplier Documentation (`PRQ-016`), Vendor Data Book / Mechanical Final Documentation (`MEC-023`), Equipment FAT / Performance Test Report (`MEC-022`), Inspection Release Certificate (`QLT-020`), Material Test Reports / Certificates (`QLT-013`), Spare Parts Interchangeability Record (`PRQ-015`), Mechanical Equipment IOM Manual (`MEC-025`), Electrical Test Records / Energization Package (`ELE-030`), and Instrument As-Built Drawings (`INS-029`). Source: `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table. | Turnover record completeness review against the enumerated source rows. |
| REQ-079-05-007 | The deliverable shall represent the ten applicable interface facts for `PKG-079` (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) within the vendor documentation that crosses each interface. Source: Workbook Packages row 69; `INTERFACE_REGISTER.csv` rows for `PKG-079`; `_Sources/26020-Package_Requirements.docx`, heading 32, Physical Interface Summary. | Interface matrix check against `INTERFACE_REGISTER.csv` and the source Physical Interface Summary. |
| REQ-079-05-008 | The deliverable shall preserve the source package design / set conditions (PSV set 948 kPag (137.5 psig); delivered instrument air maximum water dew point -73.3 °C at 1000 kPag) in the vendor data sheets and shall reflect the source-stated equipment ratings (2 x 1113 SCFM at 861 kPag (125 psig) oil-injected rotary screw compressors driven by 2 x 250 HP electric motors; one wet air receiver; two dryer pre-filters; one regenerative desiccant air dryer; one after-filter; one or two dry air receivers). Source: `_Sources/26020-Package_Requirements.docx`, heading 32, Basic Scope and Major Included Equipment. | Vendor data-sheet / equipment list cross-check. |
| REQ-079-05-009 | The deliverable shall preserve source spelling and identity (package name "Instrument Air Building"; CoA `26020-01-39-001`) as recorded in Workbook row 69 and `PACKAGE_REGISTER.csv`. Source: Workbook Packages row 69. | Spelling/identity review. |
| REQ-079-05-010 | The deliverable shall identify source gaps for detailed submittal stages, hold/issue review codes, transmittal numbering, and turnover acceptance criteria as `TBD` instead of invented values, while preserving the source-listed Vendor Engineering Deliverables document codes verbatim. Source: `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table; `_Sources/26020-Package_Requirements.docx`, heading 32, Interface Coordination Notes (TBD). | Gap review before vendor handoff and EPC acceptance. |
| REQ-079-05-011 | The deliverable shall align the vendor scope to the cited RFQ source basis `Bid Docs/Budgetary/26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` and shall not extend scope beyond it (e.g., shall not absorb by-others items shipping/installation/tie-in/electrical/mounting platform/stairs). Source: `_Sources/26020-Package_Requirements.docx`, heading 32, Source Basis and Scope Notes / Open Items. | Scope-boundary review. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Vendor RFQ source basis | `Bid Docs/Budgetary/26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` is cited as the package source basis; vendor documentation aligns with this RFQ. | `_Sources/26020-Package_Requirements.docx`, heading 32, Source Basis. |
| Project mechanical / equipment package deliverables basis | Vendor document registers are a required package deliverable for mechanical/equipment packages. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, mechanical package deliverables paragraph (line 617). |
| Pressure equipment / registration | Pressure Equipment Registration Package (`REG-022`) is a listed vendor engineering deliverable in the Rotating equipment / compressors category. | `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table. |
| Fire & gas / functional safety basis | TSF-002 (philosophy), TSF-003 (mapping), TSF-004 (detector layout), TSF-009 (SIL determination), TSF-011 (SRS), TSF-013 (supplier SIL / safety manual), and TSF-028 (emergency response inputs) are listed as required vendor engineering deliverables. | `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table (Fire and gas / technical safety interfaces). |
| Fire code / building code compliance | Fire Code / Building Code Compliance Package (`REG-021`) is a listed vendor engineering deliverable; specific codes/clauses are `TBD` (not stated in accessible source). | `_Sources/26020-Package_Requirements.docx`, heading 32, Vendor Engineering Deliverables table (Building / HVAC / code interfaces). |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare deliverable identity fields to Workbook row 69 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Vendor document register presence | Confirm a vendor document register exists in the turnover package and includes one row per source-listed Vendor Engineering Deliverables entry plus category-level evidence rows. | Register exists and is mirrored in `ARTIFACT_REGISTER.csv` rows for `DEL-079-05`. |
| Interface completeness | Compare vendor document/turnover content to `INTERFACE_REGISTER.csv` rows for `PKG-079` and to the source Physical Interface Summary. | All ten applicable interface facts are represented in vendor documentation crossing each interface. |
| Equipment / conditions fidelity | Check vendor data sheets against source equipment ratings and set conditions (PSV 948 kPag; dew point -73.3 °C at 1000 kPag; 2 x 1113 SCFM at 861 kPag; 2 x 250 HP motors). | Vendor values equal source values or differences are explicitly documented and resolved. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and `_CONTEXT.md`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, document codes, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Vendor document register (`ART-95A888C02E`) listing every source-required vendor document code by category.
- Vendor Document Index (`PRQ-009`) and Vendor Document Control Procedure (`DOC-008`).
- Vendor document submittals (transmittals and revision control under `DOC-008`).
- Source vendor document table rows carried as artifacts/evidence — one `ARTIFACT_REGISTER.csv` row per source vendor-document code, plus category-level evidence rows for each Vendor Engineering Deliverables category.
- Final turnover records: at minimum `QLT-021`, `PRQ-016`, `MEC-023`, `MEC-022`, `QLT-020`, `QLT-013`, `PRQ-015`, `MEC-025`, `ELE-030`, `INS-029`.
- Source-gap / `TBD` list (submittal stages, hold/issue codes, transmittal numbering, acceptance criteria, Interface Coordination Notes) for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, Workbook row 69, applicable Gate 7 registers, the Package Requirements heading 32 source slice (Source Basis, Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables, Interface Coordination Notes), and the DBM source slice used for the package-deliverable basis.
