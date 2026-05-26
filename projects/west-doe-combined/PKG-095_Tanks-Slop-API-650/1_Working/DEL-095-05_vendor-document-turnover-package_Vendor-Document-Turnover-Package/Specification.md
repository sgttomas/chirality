# Specification — DEL-095-05 Vendor Document Turnover Package

## Scope

This specification defines the normative requirements for the **Vendor Document Turnover Package** produced by the Package Vendor for `PKG-095 Tanks, Slop (API 650)`, and reviewed by the EPC Integrator.

**In scope:**
- Vendor document register for the PKG-095 vendor-engineered equipment.
- Vendor document submittals issued by the Package Vendor across the package lifecycle.
- Source-required vendor documentation rows identified by the package requirements source (heading 47 of `26020-Package_Requirements.docx`) — carried as artifacts/evidence.
- Turnover records assembled at handover from vendor to EPC Integrator (and from EPC Integrator to facility owner) for PKG-095.

**Out of scope:**
- Vendor engineering/design content itself (that is the Vendor Engineered Equipment Package, `DEL-095-04`).
- EPC review/acceptance decisions (that is `DEL-095-06`).
- Construction/installation execution records (Construction Work Package, `DEL-095-03`).

## Requirements

| ID | Requirement | Source | Notes |
|---|---|---|---|
| REQ-095-05-01 | The Package Vendor shall maintain and submit a **Vendor Document Register** listing every document associated with the PKG-095 package, including its document number, revision, status, expected submittal date, and current submittal state. | DBM §"Mechanical Package Structure" (line 617: "Package deliverables shall include … vendor document registers"); DELIVERABLE_REGISTER row DEL-095-05 | Register is the index for items REQ-02..REQ-05. |
| REQ-095-05-02 | The Package Vendor shall issue **vendor document submittals** under controlled revisions, addressing every document row required by the source vendor document table at `26020-Package_Requirements.docx` heading 47 where rows are available. | DELIVERABLE_REGISTER row DEL-095-05; SCOPE_LEDGER SOW-0213 | Specific source rows TBD — heading-47 source slice not extracted locally. ASSUMPTION: standard API 650 tank vendor documents apply (see Datasheet ASSUMPTION). |
| REQ-095-05-03 | Each submittal shall preserve a clear scope boundary between vendor-engineered/vendor-supplied content and EPC Integrator integration content. | SCOPE_LEDGER SOW-0213; DBM §"Mechanical Package Structure" (line 617) | |
| REQ-095-05-04 | The Package Vendor shall preserve **source-required vendor documents** (the rows from the source vendor document table that are available) as artifacts within this package; these rows shall not be promoted to separate deliverables. | `_CONTEXT.md` Notes | |
| REQ-095-05-05 | The Package Vendor shall assemble **turnover records** sufficient to evidence (a) document completeness against the register and (b) acceptance readiness against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | DELIVERABLE_REGISTER row DEL-095-05; row DEL-095-06 (EPC review/acceptance interface) | |
| REQ-095-05-06 | The vendor document register and submittals shall be tagged to the package equipment scope items (SOW-0213..SOW-0216) and traceable to the equipment list anchored by the API 650 atmospheric slop tank (likely TK-9130-2) and its appurtenances/instrumentation. | SCOPE_LEDGER SOW-0214; SOW-0215 | Equipment-level tagging is required; final equipment list confirmation depends on resolution of SOW-0216 open items. |
| REQ-095-05-07 | The EPC Integrator shall perform interface/integration review of vendor documents; review findings and dispositions shall be captured in `DEL-095-06` (EPC Vendor Package Review and Acceptance) and referenced from this package's turnover records. | DELIVERABLE_REGISTER row DEL-095-05 (ResponsibleParty); row DEL-095-06 | |
| REQ-095-05-08 | Document classes typical for an API 650 atmospheric storage tank vendor package — including but not limited to GA drawings, foundation loads, nozzle schedules, MTRs, weld/NDE reports, hydrotest records, coating reports, calibration/strapping reports, and IOM manuals — shall be addressed by the register when included in heading-47 source rows. | ASSUMPTION based on tank-package convention; DBM §"Mechanical Package Structure" | ASSUMPTION — pending extraction of heading-47 source slice. |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| API 650 (atmospheric storage tanks) | Governing fabrication/design standard for the slop tank package; vendor documents must support compliance evidence | Implied by PKG-095 name and SOW-0215; clause-level location TBD |
| 26020-Package_Requirements.docx, heading 47 (Tanks, Slop) | Project-specific vendor document table and package requirements | `_Sources/26020-Package_Requirements.docx` — binary, location TBD (not extracted locally) |
| Workbook Packages row 91 | Authoritative scope/responsibility allocation for PKG-095 | SCOPE_LEDGER SOW-0213 |
| `3-25_Comp_and_Liquids_DBM.md` §"Mechanical Package Structure" | Required mechanical package deliverable elements including vendor document registers | Line 617 |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-095-05-01 | Review of the vendor document register against package equipment list; completeness check against heading-47 source rows when extracted. |
| REQ-095-05-02 | Submittal log audit; one-to-one match between register rows and issued submittal revisions. |
| REQ-095-05-03 | Scope-boundary review by EPC Integrator (DEL-095-06). |
| REQ-095-05-04 | Folder/repository inspection confirms source-table rows present as artifacts within this deliverable, not promoted elsewhere. |
| REQ-095-05-05 | Turnover record completeness check at package acceptance gate; sign-off evidence captured. |
| REQ-095-05-06 | Cross-reference register entries to equipment tags and SOW IDs; trace report. |
| REQ-095-05-07 | DEL-095-06 review-log entries reference back to this turnover package. |
| REQ-095-05-08 | Heading-47 source row extraction (when performed) confirms the assumed document classes; register updated accordingly. |

## Documentation

Required artifacts (this deliverable):

- `VendorDocumentRegister` (instance, vendor-issued; format vendor-defined unless EPC dictates) — TBD format.
- Vendor document submittals (controlled-revision documents) — set TBD pending heading-47 source rows.
- Source vendor document table rows — artifacts/evidence; format inherited from source.
- Turnover record package (transmittal log, document completeness checklist, acceptance sign-off) — TBD format.

ASSUMPTION: Register and turnover record format conventions (file types, schema) are TBD pending project document control basis.
