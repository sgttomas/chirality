# Specification: DEL-086-06 — EPC Vendor Package Review and Acceptance

## Scope

This specification governs the EPC Integrator's review, integration acceptance, and handoff-readiness determination for the Flare Stack (Low Pressure) vendor package (`PKG-086`).

**In scope** (per `_CONTEXT.md` and DELIVERABLE_REGISTER.csv row DEL-086-06):
- Review of vendor package deliverables (DEL-086-04 Vendor Engineered Equipment Package; DEL-086-05 Vendor Document Turnover Package) against the EPC basis documents.
- Determination of integration acceptance against EPC Scope of Work (DEL-086-01), Package Datasheet (DEL-086-02), and Construction Work Package (DEL-086-03).
- Production of acceptance evidence: vendor document review log, package acceptance checklist, test/inspection evidence, turnover evidence.

**Out of scope:**
- Vendor-internal engineering, design, fabrication, and supply (owned by DEL-086-04).
- Vendor document generation and turnover compilation (owned by DEL-086-05).
- Physical construction execution (owned by DEL-086-03 / field execution).

## Requirements

| ID | Requirement | Source | Label |
|---|---|---|---|
| REQ-086-06-01 | The EPC Integrator SHALL review each vendor submittal in DEL-086-05 against the corresponding requirement in the EPC Scope of Work (DEL-086-01) and Package Datasheet (DEL-086-02). | DELIVERABLE_REGISTER.csv (DEL-086-06 Description) | derived |
| REQ-086-06-02 | The vendor document review log SHALL record, for each submittal: submittal ID, revision, reviewer, disposition, basis-document reference, and date. | `_CONTEXT.md` Anticipated Artifacts | ASSUMPTION (standard EPC review-log content) |
| REQ-086-06-03 | The package acceptance checklist SHALL trace each acceptance criterion to its basis item in DEL-086-01, DEL-086-02, or DEL-086-03. | DELIVERABLE_REGISTER.csv (DEL-086-06 Description) | derived |
| REQ-086-06-04 | Test and inspection evidence SHALL be collected and indexed for each acceptance-critical item identified in the Package Datasheet (DEL-086-02). | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv | derived |
| REQ-086-06-05 | Turnover evidence SHALL demonstrate readiness for handoff to construction execution (DEL-086-03 workface) and downstream operations. | `_CONTEXT.md` Anticipated Artifacts | derived |
| REQ-086-06-06 | Non-conformances identified during review SHALL be tracked to documented closure prior to acceptance. | ASSUMPTION — standard EPC practice; specific NCR regime TBD | ASSUMPTION |
| REQ-086-06-07 | Acceptance SHALL cover scope items SOW-0091, SOW-0092, SOW-0093, SOW-0094. | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv | derived |
| REQ-086-06-08 | Specific acceptance criteria, witness/hold-points, and inspection sample sizes | TBD — `26020-Package_Requirements.docx` heading 39 not locally extracted | TBD |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| Project EPC Scope of Work governing standards | Inherited from DEL-086-01 | location TBD |
| Package Datasheet design codes for flare stack (low pressure) | Inherited from DEL-086-02 | location TBD (likely API 521 / API 537 family) — ASSUMPTION |
| Site QA/QC and turnover regime | Inherited from project DBM / EPC plan | location TBD |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-086-06-01 | Vendor document review log entries cross-checked against DEL-086-01 / DEL-086-02 requirement IDs. |
| REQ-086-06-02 | Inspection of review-log structure for required fields. |
| REQ-086-06-03 | Trace audit: each checklist row resolves to a basis-document reference. |
| REQ-086-06-04 | Inventory of test/inspection records vs. acceptance-critical item list from DEL-086-02. |
| REQ-086-06-05 | Turnover evidence completeness review against DEL-086-03 handoff requirements. |
| REQ-086-06-06 | NCR register reviewed; all NCRs in `Closed` state at acceptance. |
| REQ-086-06-07 | Coverage matrix mapping checklist items to SOW-0091..0094. |
| REQ-086-06-08 | TBD pending source extraction. |

## Documentation

Required artifacts (from `_CONTEXT.md`):
- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence index
- Turnover evidence package
