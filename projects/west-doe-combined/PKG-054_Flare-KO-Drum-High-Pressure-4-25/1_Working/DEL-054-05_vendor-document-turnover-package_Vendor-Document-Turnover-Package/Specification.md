# Specification — DEL-054-05 Vendor Document Turnover Package (PKG-054 Flare KO Drum (High Pressure) 4-25)

## Scope

This specification governs the assembly, submittal, review, and final turnover of the **Vendor Document Turnover Package** for PKG-054 — Flare KO Drum (High Pressure) 4-25, covering equipment tags `V-4100-1` (HP flare KO drum) and `P-4100-1` (HP flare KO drum transfer pump). It addresses what vendor documents shall be produced, when they shall be submitted, how they shall be reviewed by the EPC Integrator, and the final turnover record set that closes the package documentation deliverable.

**In scope** (per `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 298):

- Vendor document register
- Vendor document submittals (engineering, design, fabrication, FAT, shipping, as-built)
- Source vendor document table rows as artifacts/evidence where available
- Turnover records (final transmittal, acceptance manifest)

**Out of scope:**

- Production of the physical equipment package (covered by DEL-054-04 Vendor Engineered Equipment Package).
- EPC Integrator-issued documents (Scope of Work, Package Datasheet, CWP — DEL-054-01/02/03).
- EPC final review/acceptance of the vendor package (DEL-054-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-DEL-054-05-01 | A **Vendor Document Register** shall be maintained by the Package Vendor that lists every required vendor document, its current submittal status, EPC review code, and a final-for-turnover flag. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row 298 |
| REQ-DEL-054-05-02 | The required vendor document list shall comply with the requirements stated in `26020-Package_Requirements.docx` package heading 9 (vendor documentation requirements). Specific document categories, submittal timing, and quantities — location TBD (binary source not converted to text). | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` SourceRefRaw |
| REQ-DEL-054-05-03 | Vendor submittals shall be transmitted to the EPC Integrator under the project document control procedure and shall receive an EPC review code prior to fabrication progression where required. ASSUMPTION (standard EPC/vendor-document practice); specific review-code matrix — location TBD. | location TBD — `26020-Package_Requirements.docx` package heading 9 |
| REQ-DEL-054-05-04 | At minimum, the final turnover document set shall include: (a) equipment datasheets as-built, (b) general arrangement / fabrication drawings as-built, (c) materials test reports and code certifications (ASME U-stamp or jurisdictional registration as applicable), (d) NDE records, (e) FAT records, (f) OEM operating and maintenance manuals, and (g) spare-parts lists. ASSUMPTION (typical vendor-document turnover set); definitive list — location TBD. | location TBD — `26020-Package_Requirements.docx` package heading 9 |
| REQ-DEL-054-05-05 | Documentation shall cover both `V-4100-1` (HP flare KO drum, pressure vessel) and `P-4100-1` (HP flare KO drum transfer pump). | `4-25_Deepcut_DBM.md` line 2580; `PACKAGE_REGISTER.csv` row 55 |
| REQ-DEL-054-05-06 | Where Workbook Packages row 55 lists specific vendor documentation columns, those document rows shall be carried as artifacts/evidence within this turnover package (not as separate deliverables). | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes |
| REQ-DEL-054-05-07 | The Package Vendor is the document owner; the EPC Integrator performs interface/integration review of vendor documentation. | `DELIVERABLE_REGISTER.csv` row 298 ResponsibleParty |
| REQ-DEL-054-05-08 | A final turnover transmittal/manifest shall be issued documenting the complete, EPC-accepted vendor document set at the close of the package. TBD — exact form and acceptance signature/workflow location TBD. | location TBD |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 9 | Project-level vendor documentation requirements for PKG-054 (authoritative) | location TBD (binary; not converted) |
| Project document control procedure | Submittal format, file naming, transmittal codes, review-cycle workflow | TBD — not identified in locally accessible sources |
| ASME Section VIII Div. 1 (and applicable jurisdictional code) | Pressure vessel `V-4100-1` code documentation (U-stamp / CRN package, MTRs, NDE) — ASSUMPTION based on equipment type | location TBD |
| API-11P (or vendor demister sizing basis) | Sizing/internals documentation context if applicable to KO drum demister — referenced for sibling design basis only | `4-25_Deepcut_DBM.md` line 963 (compressor suction scrubber context, not authoritative for KO drum) |

## Verification

| Req ID | Verification Approach |
|---|---|
| REQ-DEL-054-05-01 | Inspect the Vendor Document Register; confirm presence of every required line item with status/review code/final-for-turnover flag. |
| REQ-DEL-054-05-02 | Cross-check register against `26020-Package_Requirements.docx` package heading 9 line items (verification deferred until source slice is accessible — location TBD). |
| REQ-DEL-054-05-03 | Inspect transmittal logs; confirm EPC review codes are applied prior to fabrication-release for documents that require pre-fab review. |
| REQ-DEL-054-05-04 | Inspect final turnover binder/electronic set for the listed minimum document categories per equipment tag. |
| REQ-DEL-054-05-05 | Confirm coverage of `V-4100-1` and `P-4100-1` line items in the register and final set. |
| REQ-DEL-054-05-06 | Trace each Workbook Packages row 55 vendor-doc column entry to a register row and an attached artifact (location TBD pending workbook source slice). |
| REQ-DEL-054-05-07 | Verify document ownership and review actor on transmittals match the declared responsibility model. |
| REQ-DEL-054-05-08 | Inspect final turnover transmittal/manifest and EPC acceptance record. |

## Documentation

Required artifacts produced by this deliverable (from `_CONTEXT.md` Anticipated Artifacts):

- Vendor Document Register (controlled, status-tracked)
- Vendor document submittals (engineering, design, fabrication, FAT, as-built)
- Source vendor document table rows as artifacts/evidence
- Turnover records (final transmittal manifest, EPC acceptance record)
