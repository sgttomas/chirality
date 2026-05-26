# Specification — DEL-063-05 Vendor Document Turnover Package

> Normative specification for the Vendor Document Turnover Package for PKG-063 Tanks, DSO (API 650).

## Scope

This specification governs the Package Vendor's compiled documentation set turned over for PKG-063 Tanks, DSO (API 650), and the EPC Integrator's interface/integration review of that set.

**In scope**
- The vendor document register and its maintenance over the package lifecycle.
- Vendor document submittals required by the source (26020-Package_Requirements.docx heading 18) and by the EPC Scope of Work (`DEL-063-01`) and Package Datasheet (`DEL-063-02`).
- Source-required vendor documentation explicitly called out in the source (specific list TBD).
- Turnover records evidencing transmittal, review, acceptance, and final handover.

**Out of scope**
- The vendor engineered equipment package itself (covered by `DEL-063-04`).
- Construction installation/tie-in execution (covered by `DEL-063-03_construction-work-package`).
- EPC Integrator's vendor package review and acceptance disposition (covered by `DEL-063-06_epc-vendor-package-review-and-acceptance`).
- Individual source document table rows as standalone deliverables (they remain evidence/artifacts per decomposition Notes).

Source: `_CONTEXT.md`; DELIVERABLE_REGISTER row 508.

## Requirements

> Each requirement cites its source. Requirements whose substance depends on the unread heading-18 source slice are marked TBD with `location TBD`.

### R-01 Coverage of source-required documentation
The Vendor Document Turnover Package SHALL include every vendor document explicitly required by 26020-Package_Requirements.docx, package heading 18 (location TBD).
- Source: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER row 508 SourceReference column.
- Specific document list: TBD (source slice not accessible at drafting time).

### R-02 Vendor document register
The Package Vendor SHALL maintain a vendor document register that, at minimum, identifies for each vendor document: document number, title, type/class, current revision, status (Issued for Review / Issued for Construction / Issued for Use / As-Built / Final), transmittal reference, and required submittal/turnover stage.
- Source: ASSUMPTION (industry convention for vendor document registers); source heading 18 may prescribe specific register fields — `location TBD`.

### R-03 Submittal compliance with EPC handoff basis
Vendor document submittals SHALL be consistent with the EPC Scope of Work (`DEL-063-01`) and the Package Datasheet (`DEL-063-02`).
- Source: PROPOSAL based on decomposition relationships among PKG-063 deliverables (rows 504, 505, 508).

### R-04 Coverage of SOW items
The Vendor Document Turnover Package SHALL provide evidence (via the register, submittals, and turnover records) sufficient to support closure of SOW-0209, SOW-0210, SOW-0211, and SOW-0212.
- Source: `_CONTEXT.md` Covers Scope Items; DELIVERABLE_REGISTER row 508.

### R-05 Turnover records
Turnover records SHALL evidence final transmittal and EPC Integrator acceptance for each document required for handover (final list TBD).
- Source: `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on acceptance signature requirement (specific signoff form TBD).

### R-06 EPC Integrator interface/integration review
Vendor submittals SHALL be made available to the EPC Integrator for interface/integration review prior to acceptance for handover.
- Source: `_CONTEXT.md` ResponsibleParty ("Package Vendor … with EPC Integrator interface/integration review"); DELIVERABLE_REGISTER row 508.

### R-07 Source artifact preservation
Where individual source vendor document table rows are available, they SHALL be preserved as artifacts/evidence within the package rather than restructured as separate deliverables.
- Source: DELIVERABLE_REGISTER row 508 Notes column.

### R-08 Governing tank code conformance evidence
Vendor documents for tank construction, fabrication, inspection, and testing SHALL evidence conformance with the governing tank code.
- Governing code: ASSUMPTION — API 650 (Welded Tanks for Oil Storage), inferred from package name "Tanks, DSO (API 650)".
- Specific clauses, NDE classes, and acceptance criteria: TBD (`location TBD` in API 650).

### R-09 Document numbering and revision control
Each vendor document SHALL have a unique number, revision, and date.
- Numbering convention: TBD (vendor- or project-defined; source slice unread).

## Standards

| Standard | Use | Location |
|---|---|---|
| API 650 (Welded Tanks for Oil Storage) | Governing tank code (assumed from package name) | location TBD |
| 26020-Package_Requirements.docx package heading 18 | Source-required vendor documentation list and conditions | location TBD (binary docx; slice not accessible) |
| Workbook Packages row 90 (26020-Packages_Interfaces_4_export.xlsx) | Source register row for PKG-063 | location TBD (binary xlsx; slice not accessible) |

ASSUMPTION: Additional discipline standards (e.g., ASME Sec. V/VIII/IX for welding and NDE; coatings standards) may apply via API 650 references — TBD until source is accessible.

## Verification

| Requirement | Verification approach | Verification evidence |
|---|---|---|
| R-01 | Cross-check vendor document register against the heading-18 required list | Coverage matrix in `Procedure.md` Verification step (table populated when source accessible) |
| R-02 | Inspection of register fields | Register file (vendor-supplied) |
| R-03 | Cross-reference each submittal to SOW (`DEL-063-01`) and Datasheet (`DEL-063-02`) line items | Traceability matrix (artifact) |
| R-04 | Verify each SOW item (SOW-0209..0212) is supported by at least one register entry / submittal | SOW-coverage matrix (artifact) |
| R-05 | Inspection of turnover records | Turnover transmittal log; acceptance records |
| R-06 | Confirmation that EPC Integrator has received and reviewed submittals | Review log (linked to `DEL-063-06`) |
| R-07 | Inspection of evidence folder | Captured source rows as artifacts |
| R-08 | Vendor-supplied conformance certs / inspection records | Mill certs, weld records, NDE reports, hydrotest records (specific set TBD) |
| R-09 | Inspection of register entries | Vendor document register |

## Documentation

Required artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document register (master index).
- Vendor document submittals (issued documents per the register).
- Source vendor document table rows captured as artifacts (where available).
- Turnover records (transmittal logs, acceptance/sign-off records, final handover set).

Optional/supporting artifacts (PROPOSAL):
- SOW coverage matrix (SOW-0209..0212 → submittals).
- Heading-18 coverage matrix (source-required → submittals) — populated when source slice is accessible.
- Standard conformance evidence index (API 650 and referenced sub-standards).
