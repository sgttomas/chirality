# Specification — DEL-064-05 Vendor Document Turnover Package (PKG-064 Tanks, Water (API 650) 4-25)

## Scope

This specification governs the assembly, submittal, review, and final turnover of the **Vendor Document Turnover Package** for PKG-064 — Tanks, Water (API 650) 4-25, covering equipment tags `TK-5317-1` and `TK-5318-1` (two 2,000 bbl modified API-650 atmospheric Process Water Storage Tanks). It addresses what vendor documents shall be produced, when they shall be submitted, how they shall be reviewed by the EPC Integrator, and the final turnover record set that closes the package documentation deliverable.

**In scope** (per `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row for `DEL-064-05`):

- Vendor document register
- Vendor document submittals (engineering, design, shop fabrication of subcomponents, field erection, hydrotest/leak-test, coating, insulation, heat tracing, as-built)
- Source vendor document table rows as artifacts/evidence where available
- Turnover records (final transmittal, acceptance manifest)

**Out of scope:**

- Production of the physical equipment package (covered by DEL-064-04 Vendor Engineered Equipment Package).
- EPC Integrator-issued documents (Scope of Work, Package Datasheet, CWP — DEL-064-01/02/03).
- EPC final review/acceptance of the vendor package (DEL-064-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-DEL-064-05-01 | A **Vendor Document Register** shall be maintained by the Package Vendor that lists every required vendor document, its current submittal status, EPC review code, and a final-for-turnover flag. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row for `DEL-064-05` |
| REQ-DEL-064-05-02 | The required vendor document list shall comply with the requirements stated in `26020-Package_Requirements.docx` package heading 19 (vendor documentation requirements). Specific document categories, submittal timing, and quantities — location TBD (binary source not converted to text). | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` SourceRefRaw |
| REQ-DEL-064-05-03 | Vendor submittals shall be transmitted to the EPC Integrator under the project document control procedure and shall receive an EPC review code prior to fabrication/field-erection progression where required. ASSUMPTION (standard EPC/vendor-document practice); specific review-code matrix — location TBD. | location TBD — `26020-Package_Requirements.docx` package heading 19 |
| REQ-DEL-064-05-04 | At minimum, the final turnover document set shall include: (a) tank datasheets as-built, (b) general arrangement and fabrication/erection drawings as-built, (c) API-650 design calculations (shell, bottom, roof, anchorage, settlement, seismic, wind as applicable), (d) welding procedure specifications and qualification records (WPS/PQR/WPQ), (e) materials test reports and code compliance records, (f) NDE records (RT/UT/PT/MT/VT as applicable), (g) hydrotest / leak-test records, (h) internal coating (Devchem 253 on floor, walls, and roof per DBM) application and inspection records, (i) external insulation and heat-tracing records, (j) PVRV/EPRV documentation, (k) appurtenance documentation (manways, nozzles, level instruments, skim float system), (l) OEM operating and maintenance manuals (where applicable), and (m) spare-parts lists. ASSUMPTION (typical API-650 atmospheric tank turnover set); definitive list — location TBD. | location TBD — `26020-Package_Requirements.docx` package heading 19; `4-25_Deepcut_DBM.md` lines 518, 524 |
| REQ-DEL-064-05-05 | Documentation shall cover both `TK-5317-1` and `TK-5318-1` Process Water Storage Tanks. | `4-25_Deepcut_DBM.md` line 2628; `PACKAGE_REGISTER.csv` row 96 |
| REQ-DEL-064-05-06 | Where Workbook Packages row 96 lists specific vendor documentation columns, those document rows shall be carried as artifacts/evidence within this turnover package (not as separate deliverables). | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes |
| REQ-DEL-064-05-07 | The Package Vendor is the document owner; the EPC Integrator performs interface/integration review of vendor documentation. | `DELIVERABLE_REGISTER.csv` ResponsibleParty |
| REQ-DEL-064-05-08 | A final turnover transmittal/manifest shall be issued documenting the complete, EPC-accepted vendor document set at the close of the package. TBD — exact form and acceptance signature/workflow location TBD. | location TBD |
| REQ-DEL-064-05-09 | Documentation shall evidence compliance with the DBM-stated requirement that water tanks be insulated to prevent winter freezing (insulation system specification, application records, and heat-trace commissioning records included in turnover). | `4-25_Deepcut_DBM.md` line 2509; line 524 |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 19 | Project-level vendor documentation requirements for PKG-064 (authoritative) | location TBD (binary; not converted) |
| Project document control procedure | Submittal format, file naming, transmittal codes, review-cycle workflow | TBD — not identified in locally accessible sources |
| API-650 (modified per project DBM, 16 oz test pressure) | Atmospheric tank design and documentation basis for `TK-5317-1`/`TK-5318-1` | `4-25_Deepcut_DBM.md` line 518 |
| ASME Section IX (welding) | WPS/PQR/WPQ documentation for tank welding | ASSUMPTION — typical for API-650 tanks; location TBD |
| Provincial pressure-equipment / jurisdictional registration | Jurisdictional registration documentation as applicable | ASSUMPTION; location TBD |

## Verification

| Req ID | Verification Approach |
|---|---|
| REQ-DEL-064-05-01 | Inspect the Vendor Document Register; confirm presence of every required line item with status/review code/final-for-turnover flag. |
| REQ-DEL-064-05-02 | Cross-check register against `26020-Package_Requirements.docx` package heading 19 line items (verification deferred until source slice is accessible — location TBD). |
| REQ-DEL-064-05-03 | Inspect transmittal logs; confirm EPC review codes are applied prior to fabrication/erection-release for documents that require pre-fab review. |
| REQ-DEL-064-05-04 | Inspect final turnover binder/electronic set for the listed minimum document categories per tank tag. |
| REQ-DEL-064-05-05 | Confirm coverage of `TK-5317-1` and `TK-5318-1` line items in the register and final set. |
| REQ-DEL-064-05-06 | Trace each Workbook Packages row 96 vendor-doc column entry to a register row and an attached artifact (location TBD pending workbook source slice). |
| REQ-DEL-064-05-07 | Verify document ownership and review actor on transmittals match the declared responsibility model. |
| REQ-DEL-064-05-08 | Inspect final turnover transmittal/manifest and EPC acceptance record. |
| REQ-DEL-064-05-09 | Inspect insulation, internal coating (Devchem 253), and heat-trace records in turnover set; confirm freeze-protection traceability. |

## Documentation

Required artifacts produced by this deliverable (from `_CONTEXT.md` Anticipated Artifacts):

- Vendor Document Register (controlled, status-tracked)
- Vendor document submittals (engineering, design, shop fabrication of subcomponents, field erection, hydrotest, coating, insulation, heat tracing, as-built)
- Source vendor document table rows as artifacts/evidence
- Turnover records (final transmittal manifest, EPC acceptance record)
