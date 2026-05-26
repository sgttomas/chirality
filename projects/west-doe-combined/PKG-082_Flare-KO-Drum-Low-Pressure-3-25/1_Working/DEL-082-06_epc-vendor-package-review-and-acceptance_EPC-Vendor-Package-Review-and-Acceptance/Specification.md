# Specification — EPC Vendor Package Review and Acceptance (DEL-082-06)

Normative requirements for the EPC Integrator's review and acceptance of the PKG-082 Flare KO Drum (Low Pressure) 3-25 vendor package and its handoff readiness evidence.

## Scope

### In scope
- EPC Integrator review of the Package Vendor's engineered equipment package (DEL-082-04) against:
  - EPC Scope of Work (DEL-082-01),
  - Package Datasheet (DEL-082-02),
  - Construction Work Package (DEL-082-03).
- Review of the Vendor Document Turnover Package (DEL-082-05) for completeness and code/standards compliance.
- Capture of integration acceptance evidence: document review log, acceptance checklist, test/inspection evidence, turnover evidence (`_CONTEXT.md` Anticipated Artifacts).
- Coverage of SOW items SOW-0079 through SOW-0082.

### Out of scope
- Re-engineering the vendor's package (owned by DEL-082-04 / Package Vendor).
- Authoring vendor source documents (owned by DEL-082-05 / Package Vendor).
- Issuing binding approvals; binding authority remains with the human approver. The deliverable produces acceptance evidence; approval is recorded by the appropriate human-authored record (K-AUTH-1).

## Requirements

| Req ID | Requirement | Source / Authority |
|---|---|---|
| REQ-082-06-01 | Vendor document review log SHALL list every document in the Vendor Document Turnover Package (DEL-082-05) with reviewer, review date, disposition (Accepted / Accepted with Comment / Revise and Resubmit / Rejected), and disposition rationale. | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on disposition vocabulary — standard EPC convention (no source clause). |
| REQ-082-06-02 | Package acceptance checklist SHALL include one row per SOW item (SOW-0079, SOW-0080, SOW-0081, SOW-0082) and a closure status per row. | `_CONTEXT.md` Covers Scope Items |
| REQ-082-06-03 | Package acceptance checklist SHALL verify alignment of vendor deliverables to the Package Datasheet (DEL-082-02). | `_CONTEXT.md` Scope |
| REQ-082-06-04 | Package acceptance checklist SHALL verify alignment of vendor deliverables to the Construction Work Package (DEL-082-03), including skid-edge isolation, vent/drain routing class, and maintenance access. | DBM SEC-09 Isolation Philosophy; Vessel and Exchanger Design |
| REQ-082-06-05 | Test and inspection evidence SHALL include code-required test records (e.g., hydrotest, NDE) and any sour-service material verification records called out by the Package Datasheet. | DBM SEC-09 vessel design philosophy; specific test list location TBD (vendor datasheet). |
| REQ-082-06-06 | Test and inspection evidence SHALL include functional checks of the LP flare KO drum transfer pump (P-3900-2) per the 1 x 100 percent configuration basis. | DBM SEC-09 equipment list row |
| REQ-082-06-07 | Turnover evidence SHALL confirm receipt of the complete Vendor Document Turnover Package (DEL-082-05) before mechanical-completion sign-off. | `_CONTEXT.md` Anticipated Artifacts |
| REQ-082-06-08 | Acceptance evidence SHALL flag any deviation between vendor-supplied design and the LP relief / blowdown basis (LP header carried as 508 mm / 20 in; staggered blowdown; W242510-PRC-REP-000003-001 sequencing). | DBM SEC-07 |
| REQ-082-06-09 | Acceptance evidence SHALL flag any deviation from sour-service isolation (double block/bleed or equivalent) and vent/drain routing classification. | DBM SEC-09 Isolation Philosophy |
| REQ-082-06-10 | Open items, deferred tests, and provisional dispositions SHALL be tracked to closure in the deliverable; unresolved items SHALL be marked `TBD` or `NEEDS_HUMAN_RULING` rather than silently accepted. | K-PROV-1; method convention |
| REQ-082-06-11 | The deliverable SHALL NOT itself issue an approval; all binding approvals are recorded by the human approver in the appropriate gate or status record. | K-AUTH-1 |

ASSUMPTION: Specific code-of-construction (e.g., ASME VIII Div. 1 vs Div. 2) and NDE classes are not cited in the locally accessible source slices. They derive from the Package Datasheet (DEL-082-02) and vendor data once available. Marked `location TBD` in REQ-082-06-05.

## Standards

| Standard / Document | Use | Locally Accessible | Location |
|---|---|---|---|
| 26020-Package_Requirements.docx package heading 35 | Defining the package scope and vendor requirements that acceptance is measured against | Yes (binary, not parsed in-band) | location TBD (binary `.docx`) |
| 26020-Packages_Interfaces_4_export.xlsx — Packages row 56 | Defining interfaces relevant to acceptance | Yes (binary, not parsed in-band) | location TBD (binary `.xlsx`) |
| 3-25_Comp_and_Liquids_DBM.md SEC-06, SEC-07, SEC-09 | Process basis for LP flare KO drum, relief header, blowdown, isolation philosophy, vessel design philosophy | Yes | Section headings as cited |
| W242510-PRC-REP-000003-001 — Plant Shutdown and Blowdown Philosophy | Detailed blowdown sequencing basis | No — referenced by DBM SEC-07 | location TBD |
| Project hazardous-material list | Lube-oil and material storage interface | No — referenced by DBM SEC-07 | location TBD |
| Project prime mover list W242510-PRJ-LST-000003-001 | Cross-reference for prime-mover scope (peripheral to this deliverable) | No | location TBD |

ASSUMPTION: Pressure-vessel construction code, sour-service material standards (e.g., NACE MR0175 / ISO 15156), welding/NDE standards, and hydrotest standards likely apply. Specific clauses cannot be extracted without the Package Datasheet text and vendor data; recorded as ASSUMPTION pending DEL-082-02 source access.

## Verification

| Req ID | Verification Method | Evidence Type |
|---|---|---|
| REQ-082-06-01 | Inspection of completed review log | `vendor_document_review_log` artifact |
| REQ-082-06-02 | Inspection of completed acceptance checklist | `package_acceptance_checklist` artifact |
| REQ-082-06-03 | Inspection — cross-check against DEL-082-02 | Checklist row evidence |
| REQ-082-06-04 | Inspection — cross-check against DEL-082-03 and DBM SEC-09 | Checklist row evidence |
| REQ-082-06-05 | Document review of vendor test/inspection records | `test_inspection_evidence` artifact |
| REQ-082-06-06 | Functional-test record review | `test_inspection_evidence` artifact |
| REQ-082-06-07 | Inspection — turnover package receipt confirmation | `turnover_evidence` artifact |
| REQ-082-06-08 | Engineering review against DBM SEC-07 cited values | Deviation entries in checklist |
| REQ-082-06-09 | Engineering review against DBM SEC-09 isolation philosophy | Deviation entries in checklist |
| REQ-082-06-10 | Status sweep of open items at handoff | `_STATUS.md`, MEMORY.md (if used), checklist closure status |
| REQ-082-06-11 | Confirm no agent-issued approval; only human-authored approval record present | Run records and `_STATUS.md` history |

## Documentation

Required documentation artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- `vendor_document_review_log` — log of every vendor document with disposition and rationale.
- `package_acceptance_checklist` — SOW-item-by-item and datasheet/CWP cross-check.
- `test_inspection_evidence` — code-required and functional test records.
- `turnover_evidence` — receipt confirmation of DEL-082-05 and any punch list closure records.

File-naming convention TBD — defer to project documentation control plan (not in locally accessible sources).
