# Specification — DEL-067-05 Vendor Document Turnover Package (PKG-067 Tanks, Sour Water (API 650) 4-25)

## Scope

This specification governs the assembly, submittal, review, and final turnover of the **Vendor Document Turnover Package** for PKG-067 — Tanks, Sour Water (API 650) 4-25, covering two produced-water / sour-water atmospheric storage tanks (tags `TK-9010-1` and `TK-9020-1` — ASSUMPTION; tag mapping per `4-25_Deepcut_DBM.md` tank-list region, section TBD). It addresses what vendor documents shall be produced, when they shall be submitted, how they shall be reviewed by the EPC Integrator, and the final turnover record set that closes the package documentation deliverable.

**In scope** (per `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-067-05 row):

- Vendor document register
- Vendor document submittals (engineering, design, fabrication / field-erection, testing, shipping, as-built)
- Source vendor document table rows as artifacts/evidence where available
- Turnover records (final transmittal, acceptance manifest)

**Out of scope:**

- Production of the physical equipment package (covered by DEL-067-04 Vendor Engineered Equipment Package).
- EPC Integrator-issued documents (Scope of Work, Package Datasheet, CWP — DEL-067-01/02/03).
- EPC final review/acceptance of the vendor package (DEL-067-06).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-DEL-067-05-01 | A **Vendor Document Register** shall be maintained by the Package Vendor that lists every required vendor document, its current submittal status, EPC review code, and a final-for-turnover flag. | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` DEL-067-05 row |
| REQ-DEL-067-05-02 | The required vendor document list shall comply with the requirements stated in `26020-Package_Requirements.docx` package heading 22 (vendor documentation requirements). Specific document categories, submittal timing, and quantities — location TBD (binary source not converted to text). | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` SourceRefs |
| REQ-DEL-067-05-03 | Vendor submittals shall be transmitted to the EPC Integrator under the project document control procedure and shall receive an EPC review code prior to fabrication-release / field-erection progression where required. ASSUMPTION (standard EPC/vendor-document practice); specific review-code matrix — location TBD. | location TBD — `26020-Package_Requirements.docx` package heading 22 |
| REQ-DEL-067-05-04 | At minimum, the final turnover document set shall include: (a) tank datasheets as-built, (b) general arrangement / fabrication / erection drawings as-built (including foundation interface), (c) materials test reports for plate, shell, and bottom components, (d) weld procedure specifications and PQRs, (e) NDE records (shell and bottom weld inspection, vacuum-box testing as applicable), (f) hydrostatic test records, (g) interior coating / lining records (where specified for sour-water service), (h) API-650 nameplate / Manufacturer's data report, (i) OEM operating and maintenance manuals, and (j) spare-parts lists. ASSUMPTION (typical API-650 sour-water tank turnover set); definitive list — location TBD. | location TBD — `26020-Package_Requirements.docx` package heading 22 |
| REQ-DEL-067-05-05 | Documentation shall cover both produced-water / sour-water storage tanks (`TK-9010-1` and `TK-9020-1` — ASSUMPTION on tags). | `4-25_Deepcut_DBM.md` tank-list region (section TBD); `PACKAGE_REGISTER.csv` row 94 |
| REQ-DEL-067-05-06 | Where Workbook Packages row 94 lists specific vendor documentation columns, those document rows shall be carried as artifacts/evidence within this turnover package (not as separate deliverables). | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes |
| REQ-DEL-067-05-07 | The Package Vendor is the document owner; the EPC Integrator performs interface/integration review of vendor documentation. | `DELIVERABLE_REGISTER.csv` DEL-067-05 row ResponsibleParty |
| REQ-DEL-067-05-08 | A final turnover transmittal/manifest shall be issued documenting the complete, EPC-accepted vendor document set at the close of the package. TBD — exact form and acceptance signature/workflow location TBD. | location TBD |
| REQ-DEL-067-05-09 | Where the tank materials, coatings, or welding are governed by sour-service requirements (e.g., NACE MR0175 / ISO 15156), associated certifications and qualification records shall be included in the turnover set. ASSUMPTION (sour service applicability); definitive applicability — location TBD pending source confirmation. | location TBD |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 22 | Project-level vendor documentation requirements for PKG-067 (authoritative) | location TBD (binary; not converted) |
| Project document control procedure | Submittal format, file naming, transmittal codes, review-cycle workflow | TBD — not identified in locally accessible sources |
| API Standard 650 (Welded Tanks for Oil Storage) | Tank design, fabrication, inspection, and nameplate documentation for `TK-9010-1` / `TK-9020-1` (per package name; modified API-650 specification noted in 4-25 DBM) | `4-25_Deepcut_DBM.md` "Condensate tank specification | Modified API 650" entry (section TBD; sour-water-tank-specific confirmation TBD) |
| NACE MR0175 / ISO 15156 | Sour-service materials and weld qualification documentation — ASSUMPTION on applicability for sour-water-service tanks | location TBD |

## Verification

| Req ID | Verification Approach |
|---|---|
| REQ-DEL-067-05-01 | Inspect the Vendor Document Register; confirm presence of every required line item with status/review code/final-for-turnover flag. |
| REQ-DEL-067-05-02 | Cross-check register against `26020-Package_Requirements.docx` package heading 22 line items (verification deferred until source slice is accessible — location TBD). |
| REQ-DEL-067-05-03 | Inspect transmittal logs; confirm EPC review codes are applied prior to fabrication-release / field erection-release for documents that require pre-execution review. |
| REQ-DEL-067-05-04 | Inspect final turnover binder/electronic set for the listed minimum document categories per tank. |
| REQ-DEL-067-05-05 | Confirm coverage of `TK-9010-1` and `TK-9020-1` line items in the register and final set. |
| REQ-DEL-067-05-06 | Trace each Workbook Packages row 94 vendor-doc column entry to a register row and an attached artifact (location TBD pending workbook source slice). |
| REQ-DEL-067-05-07 | Verify document ownership and review actor on transmittals match the declared responsibility model. |
| REQ-DEL-067-05-08 | Inspect final turnover transmittal/manifest and EPC acceptance record. |
| REQ-DEL-067-05-09 | Inspect sour-service material/weld qualification certifications when sour-service applicability is confirmed (TBD). |

## Documentation

Required artifacts produced by this deliverable (from `_CONTEXT.md` Anticipated Artifacts):

- Vendor Document Register (controlled, status-tracked)
- Vendor document submittals (engineering, design, fabrication / field erection, testing, as-built)
- Source vendor document table rows as artifacts/evidence
- Turnover records (final transmittal manifest, EPC acceptance record)
