# Specification — DEL-068-05 Vendor Document Turnover Package (PKG-068 TEG Dehydration Unit)

## Scope

This specification governs the assembly, submittal, review, and final turnover of the **Vendor Document Turnover Package** for PKG-068 — TEG Dehydration Unit (CoA 26020-01-PT-22-001). It addresses what vendor documents shall be produced, when they shall be submitted, how they shall be reviewed by the EPC Integrator, and the final turnover record set that closes the package documentation deliverable.

**In scope** (per `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 550):

- Vendor document register (PRQ-009 Vendor Document Index, controlled per DOC-008)
- Vendor document submittals across all subsections enumerated in `26020-Package_Requirements.docx` package heading 23 (Core vendor documents; Core package engineering; Rotating equipment / pumps; Static pressure equipment; Heat transfer equipment; Process package design; Relief / flare / vent design; Process piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Instrumentation and controls interfaces; Fire and gas / technical safety interfaces; Structural, foundations, supports, access)
- Source vendor document table rows as artifacts/evidence where available
- Turnover records — final transmittal, Vendor Data Book / Final Supplier Documentation (PRQ-016), Manufacturing Record Book / Vendor Data Book (QLT-021), and EPC acceptance manifest

**Out of scope:**

- Production of the physical equipment package (covered by DEL-068-04 Vendor Engineered Equipment Package).
- EPC Integrator-issued documents (Scope of Work, Package Datasheet, CWP — DEL-068-01/02/03).
- EPC final review/acceptance of the vendor package (DEL-068-06).
- Vendor-internal engineering procedures behind the documents.

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-DEL-068-05-01 | A **Vendor Document Index (PRQ-009)** shall be maintained by the Package Vendor that lists every required vendor document for PKG-068, its current submittal status, EPC review code, and a final-for-turnover flag. The index shall be controlled per **DOC-008 Vendor Document Control Procedure**. | `26020-Package_Requirements.docx` package heading 23 (PRQ-009; DOC-008); `_CONTEXT.md` Anticipated Artifacts |
| REQ-DEL-068-05-02 | The vendor document set shall include, at minimum, every deliverable enumerated in `26020-Package_Requirements.docx` package heading 23 under the twelve grouped subsections (Core vendor documents through Structural/foundations/supports/access). Where a subsection does not apply to the as-built package configuration, the Vendor shall record a non-applicability disposition on the index with EPC concurrence. | `26020-Package_Requirements.docx` package heading 23, Vendor Engineering Deliverables table |
| REQ-DEL-068-05-03 | Vendor submittals shall be transmitted to the EPC Integrator under the project document control procedure (DOC-008) and shall receive an EPC review code prior to fabrication progression where required. Specific review-code matrix — location TBD (DOC-008 contents not yet locally accessible). | `26020-Package_Requirements.docx` package heading 23 (DOC-008); location TBD |
| REQ-DEL-068-05-04 | The final turnover document set shall include, at minimum: (a) Vendor Data Book / Final Supplier Documentation (PRQ-016); (b) Manufacturing Record Book / Vendor Data Book (QLT-021); (c) Mechanical Equipment IOM Manual (MEC-025); (d) Mechanical Equipment Data Sheets at as-built revision (MEC-003); (e) Equipment General Arrangement Drawing at as-built revision (MEC-016); (f) Equipment FAT / Performance Test Report (MEC-022); (g) Material Test Reports / Certificates (QLT-013); (h) Inspection Release Certificate (QLT-020); (i) Process As-Built PFD/P&ID Package (PRO-028); (j) Piping As-Built Drawings (PIP-028); (k) Electrical Test Records / Energization Package (ELE-030); (l) Instrument As-Built Drawings (INS-029); (m) Spare Parts Interchangeability Record (PRQ-015). | `26020-Package_Requirements.docx` package heading 23 (named deliverables) |
| REQ-DEL-068-05-05 | Documentation shall cover every package equipment item enumerated in the Basic Scope and Major Included Equipment of `26020-Package_Requirements.docx` package heading 23: Inlet Air Cooler; Filter Coalescer; TEG Contactor; Glycol Flash Tank; Glycol Reboiler/Still Column; Glycol Circulation Pumps; Glycol Particulate Filters; Glycol Charcoal Filter; Gas/Glycol Exchanger; Air/Glycol Exchanger; Fuel Gas Scrubber; TEG Make-up Tank; Burner Control Panel. | `26020-Package_Requirements.docx` package heading 23, Basic Scope; Major Included Equipment |
| REQ-DEL-068-05-06 | Static pressure equipment (e.g., TEG Contactor, Glycol Flash Tank, Fuel Gas Scrubber) shall be documented with MEC-005 Static Equipment Specifications, MEC-009 Pressure Vessel Data Sheets, and REG-022 Pressure Equipment Registration Package. | `26020-Package_Requirements.docx` package heading 23, Static pressure equipment subsection |
| REQ-DEL-068-05-07 | Rotating equipment (Glycol Circulation Pumps) shall be documented with MEC-004, MEC-007, MEC-019, PRO-013, and ELE-011. | `26020-Package_Requirements.docx` package heading 23, Rotating equipment / pumps subsection |
| REQ-DEL-068-05-08 | Heat transfer equipment (Inlet Air Cooler, Gas/Glycol Exchanger, Air/Glycol Exchanger, Glycol Reboiler/Still Column) shall be documented with MEC-010 Heat Exchanger Data Sheets, supplemented by the Mechanical Calculation Package (MEC-014). | `26020-Package_Requirements.docx` package heading 23, Heat transfer equipment; Core package engineering subsections |
| REQ-DEL-068-05-09 | Where Workbook Packages row 97 lists specific vendor-documentation columns, those document rows shall be carried as artifacts/evidence within this turnover package (not as separate deliverables). | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` row 550 Notes |
| REQ-DEL-068-05-10 | The Package Vendor is the document owner; the EPC Integrator performs interface/integration review of vendor documentation. | `DELIVERABLE_REGISTER.csv` row 550 ResponsibleParty |
| REQ-DEL-068-05-11 | A final turnover transmittal/manifest shall be issued documenting the complete, EPC-accepted vendor document set at the close of the package. TBD — exact form and acceptance signature/workflow defined by DOC-008 (location TBD). | location TBD |
| REQ-DEL-068-05-12 | Applicable physical interfaces enumerated for PKG-068 (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Area/Exterior Lighting; EHT; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports) shall each have corresponding deliverables present in the package vendor document set per the relevant subsection of heading 23. Interface types listed as "No" in source (Cathodic Protection; Communications/Network; Building HVAC/Services; Grading/Site Drainage/Spill Containment; Product Loading; Pipeline/Pigging) are not required for this package. | `26020-Package_Requirements.docx` package heading 23, Physical Interface Summary; `PACKAGE_REGISTER.csv` row 97 |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 23 | Project-level vendor documentation requirements for PKG-068 (authoritative) | `_Sources/26020-Package_Requirements.docx`, package heading 23 (text-extracted slice) |
| DOC-008 Vendor Document Control Procedure | Submittal format, file naming, transmittal codes, review-cycle workflow | TBD — referenced by heading 23 as a vendor deliverable; project-level controlling instance location TBD |
| ASME Section VIII Div. 1 (and applicable jurisdictional pressure-equipment code) | Pressure vessel code documentation for static pressure equipment (TEG Contactor, Glycol Flash Tank, Fuel Gas Scrubber) — ASSUMPTION based on equipment type and REG-022 reference | location TBD |
| Provincial Pressure Equipment Registration (REG-022) | Required pressure equipment registration package for static pressure equipment | `26020-Package_Requirements.docx` package heading 23 (REG-022) |
| Vendor RFQ basis | `Bid Docs/Budgetary/26020-01-PT-RFQ-22-001_TEG Dehy Unit.docx` | location TBD (not in local sources) |

## Verification

| Req ID | Verification Approach |
|---|---|
| REQ-DEL-068-05-01 | Inspect PRQ-009 Vendor Document Index; confirm presence of every required line item with status/review code/final-for-turnover flag. |
| REQ-DEL-068-05-02 | Cross-check PRQ-009 against the twelve grouped subsections of `26020-Package_Requirements.docx` package heading 23; record EPC-concurred non-applicability dispositions where present. |
| REQ-DEL-068-05-03 | Inspect transmittal logs; confirm EPC review codes are applied prior to fabrication-release for documents that require pre-fab review (matrix per DOC-008 — location TBD). |
| REQ-DEL-068-05-04 | Inspect final turnover binder/electronic set for the listed minimum document categories. |
| REQ-DEL-068-05-05 | Confirm coverage of each enumerated equipment item in the register and final set. |
| REQ-DEL-068-05-06 | Confirm MEC-005, MEC-009, and REG-022 entries exist on the register for each static pressure item and trace to attached artifacts. |
| REQ-DEL-068-05-07 | Confirm MEC-004, MEC-007, MEC-019, PRO-013, and ELE-011 entries exist for the Glycol Circulation Pumps. |
| REQ-DEL-068-05-08 | Confirm MEC-010 entries exist for each heat-transfer item and trace to MEC-014 calculation package coverage. |
| REQ-DEL-068-05-09 | Trace each Workbook Packages row 97 vendor-doc column entry to a register row and an attached artifact (location TBD pending workbook source slice). |
| REQ-DEL-068-05-10 | Verify document ownership and review actor on transmittals match the declared responsibility model. |
| REQ-DEL-068-05-11 | Inspect final turnover transmittal/manifest and EPC acceptance record. |
| REQ-DEL-068-05-12 | Cross-check Physical Interface Summary (heading 23) against deliverables present in the register for each "Yes" interface type. |

## Documentation

Required artifacts produced by this deliverable (from `_CONTEXT.md` Anticipated Artifacts and heading 23):

- PRQ-009 Vendor Document Index (controlled, status-tracked)
- DOC-008 Vendor Document Control Procedure (vendor-issued; governs the rest)
- All submittals enumerated in heading 23, at their final/as-built revisions
- Source vendor document table rows as artifacts/evidence (Workbook row 97 vendor-doc columns; location TBD)
- Turnover records: PRQ-016 Vendor Data Book / Final Supplier Documentation; QLT-021 Manufacturing Record Book / Vendor Data Book; MEC-023 Vendor Data Book / Mechanical Final Documentation; final turnover transmittal manifest; EPC acceptance record
