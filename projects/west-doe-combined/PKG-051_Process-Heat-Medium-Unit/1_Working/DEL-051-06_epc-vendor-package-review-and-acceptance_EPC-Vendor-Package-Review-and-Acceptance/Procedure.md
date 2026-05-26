# Procedure: DEL-051-06 — EPC Vendor Package Review and Acceptance

> Operational procedure the EPC Integrator follows to produce the acceptance package and reach an acceptance disposition for the PKG-051 Process Heat Medium Unit vendor package.

## Purpose

Define the ordered steps, prerequisites, verifications, and records that produce an auditable EPC acceptance of the PKG-051 vendor package. This procedure produces the acceptance deliverable (review log, checklist, evidence index, turnover index, disposition memo); it does not perform the vendor's engineering or the construction work itself.

## Prerequisites

### Required upstream deliverables (assumed; not human-declared in `_DEPENDENCIES.md`)
- DEL-051-01 Scope of Work — issued.
- DEL-051-02 Package Datasheet — issued.
- DEL-051-03 Construction Work Package — issued.
- DEL-051-04 Vendor Engineered Equipment Package — vendor work substantially complete and submitted.
- DEL-051-05 Vendor Document Turnover Package — vendor document register populated and submittals received.

### Required reference materials
- `_REFERENCES.md` pointers verified accessible.
- DBM-Deepcut Heat Medium Basis section read.
- `26020-Package_Requirements.docx` heading 6 read (or extracted to markdown). *(TBD pending text extract.)*
- `26020-Packages_Interfaces_4_export.xlsx` Package 51 rows read (or extracted). *(TBD pending text extract.)*

### Required team/authority
- Named EPC Integrator acceptance lead.
- Named Package Vendor counterpart.
- Discipline reviewers (mechanical, process, instrumentation, electrical) assigned per acceptance-checklist row.
- Human authority designated to issue the acceptance disposition (per K-AUTH-1).

## Steps

### Stage A — Initiate acceptance run

1. Confirm prerequisites above. Record any gaps as TBD on the acceptance checklist.
2. Open the package acceptance checklist scaffold (one row per REQ-051-06-### from `Specification.md`, plus any project-specific additions).
3. Link the acceptance checklist to the DEL-051-05 vendor document register; do not duplicate the register.

### Stage B — Document review

4. For each vendor document received under DEL-051-05, record in the vendor document review log:
   - document ID / title / revision,
   - reviewer name,
   - review status (`Approved` / `Approved-with-comments` / `Revise-and-resubmit` / `Rejected`),
   - comment-resolution status,
   - acceptance-checklist row(s) it satisfies.
5. Close any "Revise-and-resubmit" loops with the Package Vendor before proceeding to Stage E.

### Stage C — Design conformance review

6. For each REQ-051-06-### in `Specification.md`:
   - locate the vendor evidence (datasheet, calculation, test report) that satisfies it,
   - record the evidence pointer in the acceptance checklist,
   - mark the row `Conforms`, `Conforms-with-condition`, or `Non-conforming`.
7. For the items the DBM flags as TBC/vendor-confirmation (REQ-051-06-011, -014, -019, plus pour point / tubeskin / circulation rate items in `Datasheet.md` Conditions), obtain the vendor's written confirmation and file it as the evidence for the row.
8. Resolve any open items in the Conflict Table in `Guidance.md`. Where a conflict cannot be resolved technically, escalate for human ruling.

### Stage D — Inspection and test evidence aggregation

9. Compile shop-test evidence (MTRs, NDE, hydrotest, welder qualifications, FAT) by component tag.
10. Compile site receipt-inspection records.
11. Compile installation check sheets against DEL-051-03.
12. Compile commissioning test evidence:
    - heat-medium loop integrity (cleanliness, flushing, fill, sampling),
    - heater burner-management functional test (4:1 turndown demonstration),
    - pump-module start under cold-start 15 deg C condition,
    - PSV pop test (API STD 527 referenced) by tag,
    - pop-tank level-switch functional test.
13. Index all evidence in the acceptance evidence index with one row per evidence artifact and a back-link to the checklist row(s) it supports.

### Stage E — Turnover assembly

14. Confirm the final vendor document set is complete per DEL-051-05.
15. Confirm spare-parts list, warranty documentation, calibration records are in the turnover package.
16. Build the outstanding-items (punchlist) log: every "Conforms-with-condition" and "Non-conforming" row in the acceptance checklist that the EPC Integrator agrees to carry forward becomes a tracked punchlist item with named owner and target date.
17. Draft the handover certificate citing the acceptance checklist, evidence index, and punchlist as exhibits.

### Stage F — Acceptance disposition (human decision)

18. EPC Integrator acceptance lead reviews the full acceptance package and proposes a disposition: `Accept`, `Accept with conditions`, or `Reject`.
19. Authorized human signs the acceptance disposition memo. Per K-AUTH-1 this step is not delegable to any agent.
20. If `Accept with conditions`, conditions are recorded as tracked punchlist items with closure owners and dates.
21. If `Reject`, the rejection memo cites the failing acceptance-checklist rows and the required corrective scope; return to Stage B/C/D as appropriate.

## Verification

| Verification | Method | Pass criterion |
|---|---|---|
| Document review log completeness | Audit: every DEL-051-05 register row appears in the review log | 100% coverage |
| Acceptance checklist completeness | Audit: every REQ-051-06-### in `Specification.md` has a checklist row | 100% coverage |
| Evidence linkage | Audit: every checklist row marked `Conforms`/`Conforms-with-condition` cites at least one evidence artifact | 100% of `Conforms` rows linked |
| Punchlist integrity | Audit: every `Conforms-with-condition` and `Non-conforming` row has a corresponding punchlist entry with owner and date | 100% |
| TBD closure (DBM TBC items) | Audit: pour point, tubeskin/film temperature, circulation rates, pump sparing basis, heater minimum-flow basis all carry vendor confirmation or an explicit punchlist deferral | 100% disposition |
| Conflict Table closure | Audit: every Conflict Table row in `Guidance.md` has either a human ruling, an evidence-based resolution, or a recorded condition on the disposition | 100% |
| Disposition authorship | Audit: signature on disposition memo belongs to designated human authority | PASS / FAIL |

## Records

Records produced and retained as the deliverable:

1. **Vendor document review log** (table; one row per vendor document).
2. **Package acceptance checklist** (table; one row per requirement REQ-051-06-###).
3. **Acceptance evidence index** (table; one row per evidence artifact, with back-links).
4. **Turnover package index** (final docs, spares list, warranty, calibration records).
5. **Outstanding-items / punchlist log** (tracked).
6. **Conflict Table closure record** (updated `Guidance.md` Conflict Table with rulings).
7. **Handover certificate** (signed).
8. **Acceptance disposition memo** (signed human decision).
9. **Run record(s)** for each TASK invocation under `_run_records/`.

All records are stored within `{DELIVERABLE_PATH}` or its sub-folders, with cross-links into DEL-051-04 and DEL-051-05 where evidence physically lives in those neighbouring deliverables.
