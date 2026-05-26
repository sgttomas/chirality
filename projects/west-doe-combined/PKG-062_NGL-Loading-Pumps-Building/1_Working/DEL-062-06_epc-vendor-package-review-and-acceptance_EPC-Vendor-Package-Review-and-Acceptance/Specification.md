# Specification — DEL-062-06 EPC Vendor Package Review and Acceptance

## Scope

This deliverable specifies the EPC integrator review and acceptance evidence required to accept the vendor-supplied **NGL Loading Pumps Building** package (PKG-062) for handoff to construction, commissioning, and turnover. It covers the four NGL loading pumps P-9510-1, P-9520-1, P-9530-1, P-9540-1 and their building-scope ancillaries (DBM-Deepcut 4-25_Deepcut_DBM.md line 2610).

**In scope:**
- EPC integrator review of vendor package documents against the EPC Scope of Work (DEL-062-01), Package Datasheet (DEL-062-02), and Construction Work Package (DEL-062-03). ASSUMPTION on exact upstream contents (sibling deliverables not consumed in this run).
- Acceptance disposition for the Vendor Engineered Equipment Package (DEL-062-04) and Vendor Document Turnover Package (DEL-062-05).
- Production of the acceptance evidence artifacts listed in `_CONTEXT.md` Anticipated Artifacts.

**Out of scope:**
- Vendor-side engineering, fabrication, or factory testing (covered by DEL-062-04).
- Site construction execution (covered by DEL-062-03).
- Commissioning execution beyond turnover readiness verification.

## Requirements

| ID | Requirement | Verification Hook | Source |
|---|---|---|---|
| REQ-062-06-001 | EPC integrator SHALL produce a vendor document review log covering every controlled document delivered in the Vendor Document Turnover Package (DEL-062-05). | Procedure §Steps — Document Review; Records §Vendor document review log | _CONTEXT.md Anticipated Artifacts |
| REQ-062-06-002 | EPC integrator SHALL produce a package acceptance checklist asserting line-by-line compliance with the EPC Scope of Work (SOW-0153 through SOW-0156). | Procedure §Steps — Acceptance Checklist; Records §Package acceptance checklist | _CONTEXT.md Covers Scope Items |
| REQ-062-06-003 | Acceptance SHALL include test/inspection evidence for the four NGL loading pumps (P-9510-1, P-9520-1, P-9530-1, P-9540-1). | Procedure §Steps — Test/Inspection Evidence; Records §Test/inspection evidence | DBM-Deepcut line 2610 |
| REQ-062-06-004 | Acceptance SHALL include turnover evidence demonstrating package handoff readiness (mechanical completion, document turnover, punch list disposition). | Procedure §Steps — Turnover; Records §Turnover evidence | _CONTEXT.md Anticipated Artifacts |
| REQ-062-06-005 | Acceptance criteria SHALL trace to the EPC Scope of Work line items SOW-0153, SOW-0154, SOW-0155, SOW-0156. | Procedure §Verification — SOW traceability check | _CONTEXT.md |
| REQ-062-06-006 | Acceptance package SHALL reflect the package boundary as defined for PKG-062 in the Deepcut DBM package roster (4 equipment items, rotary vane pump technology, NGL service). | Procedure §Steps — Boundary Check | DBM-Deepcut lines 2549, 2610 |
| REQ-062-06-007 | Detailed acceptance thresholds (performance test tolerances, NDE/QA acceptance levels, vibration limits, seal-leak criteria) — location TBD. ASSUMPTION: governed by Package Datasheet (DEL-062-02) and applicable API/ASME codes for rotary vane / positive-displacement pump packages. | Procedure §Verification — Datasheet conformance | location TBD — datasheet not consumed in this run |

## Standards

| Standard | Applicability | Source |
|---|---|---|
| API 674 (Reciprocating / Positive-Displacement Pumps) — likely applicable to rotary vane pump package | location TBD; ASSUMPTION based on pump technology family | DBM-Deepcut line 2610 (ASSUMPTION) |
| EPC project specifications / contractor standards | Govern review and acceptance methodology — location TBD | TBD |
| Project QA/QC plan | Governs inspection and acceptance evidence — location TBD | TBD |

## Verification

| Requirement | Method | Evidence |
|---|---|---|
| REQ-062-06-001 | Document review against turnover index | Vendor document review log |
| REQ-062-06-002 | Line-item compliance review against EPC SoW | Package acceptance checklist |
| REQ-062-06-003 | Inspection / FAT / SAT records review | Test/inspection evidence file |
| REQ-062-06-004 | Walkdown and turnover gate review | Turnover evidence file |
| REQ-062-06-005 | Traceability matrix SOW-0153..0156 ↔ acceptance items | Within package acceptance checklist |
| REQ-062-06-006 | Package boundary check vs DBM roster | Within package acceptance checklist (tag list confirmation) |
| REQ-062-06-007 | Datasheet conformance review | Within vendor document review log (TBD pending datasheet consumption) |

## Documentation

Required artifacts (per _CONTEXT.md Anticipated Artifacts):
- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence
- Turnover evidence

These artifacts together form the acceptance evidence file for PKG-062.
