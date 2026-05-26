# Procedure — DEL-052-06 EPC Vendor Package Review and Acceptance

## Purpose

Operational procedure to produce the EPC review and acceptance record set for PKG-052 (Inlet / TEG Dehy Cross Exchanger E-5718-1): vendor document review log, package acceptance/turnover checklist, factory/shop test and inspection evidence, and turnover evidence.

## Prerequisites

### Authority Inputs (EPC-side)

- `DEL-052-01` Scope of Work — accepted/issued state (ASSUMPTION: required before acceptance entries can be traced; not formally declared in `_DEPENDENCIES.md`).
- `DEL-052-02` Package Datasheet — accepted/issued state (ASSUMPTION as above).
- `DEL-052-03` Construction Work Package — accepted/issued state (ASSUMPTION as above).

### Vendor Inputs (under review)

- `DEL-052-04` Vendor Engineered Equipment Package — supplied for review (ASSUMPTION: this is the engineering input stream).
- `DEL-052-05` Vendor Document Turnover Package — submittals supplied for review (ASSUMPTION as above).

### Reference Materials

- Decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (accessible).
- `26020-Package_Requirements.docx` package heading 7 — required for clause-level acceptance criteria (location TBD; binary).
- `26020-Packages_Interfaces_4_export.xlsx` — Packages row 62 interface inventory (location TBD; accessible mirror in `INTERFACE_REGISTER.csv`).
- Vendor RFQ basis `26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx` (location TBD; not present under `_Sources/`).

### Tooling / Roles

- EPC Integrator review lead (assignee TBD).
- Package Vendor point of contact for clarifications (assignee TBD).
- Document control system for review log persistence (TBD).

## Steps

1. **Initialize review record set.**
   1.1 Create the four artifact placeholders for this deliverable: vendor document review log (`ART-F0F5332A58`), package acceptance and turnover checklist (`ART-21EEB708EC`), factory/shop test and inspection evidence (`ART-7F212499D9`), and turnover evidence.
   1.2 Populate the header of each artifact with PKG-052 identity from `_CONTEXT.md` (deliverable ID, package ID, equipment tag `26020-01-16-001` / E-5718-1, duty 5514.3 kW / 18.82 MMBTU/hr).

2. **Assemble the requirements baseline.**
   2.1 Extract requirements from `DEL-052-01` (SOW), `DEL-052-02` (Package Datasheet), `DEL-052-03` (CWP).
   2.2 Extract source-side requirements from `26020-Package_Requirements.docx` package heading 7 once locally accessible; record extraction provenance. (Step blocked at `TBD` until source is text-accessible.)
   2.3 Index the PKG-052 interface inventory from `INTERFACE_REGISTER.csv` (Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports) as a separate acceptance lane.

3. **Receive and log vendor submittals.**
   3.1 For each submittal supplied under `DEL-052-05`, create a review log entry citing the submittal ID, revision, date received, and the requirement(s) it satisfies.
   3.2 Mark entries with no matching requirement as `Unexpected — needs ruling`.
   3.3 Mark requirements with no matching submittal as `Missing — vendor follow-up`.

4. **Conduct document review.**
   4.1 Review each submittal against its requirement baseline; record disposition `Accept` / `Accept with comment` / `Reject` and the comment text.
   4.2 Route `Reject` entries back to the vendor; loop step 3 for resubmittals.
   4.3 Close out the review log when every requirement entry has a closed disposition.

5. **Record factory/shop test and inspection evidence.**
   5.1 Receive factory/shop test reports and inspection evidence covering the supplied equipment (E-5718-1; TEMA 'R' BEM) and accompanying piping/instrumentation and skid.
   5.2 Map each test/inspection to the acceptance criteria defined in step 2.2 (criteria TBD pending source access).
   5.3 Record acceptance disposition per test/inspection; capture deviations and approved waivers.

6. **Walk integration acceptance per interface.**
   6.1 For each PKG-052 interface row from step 2.3, record an integration acceptance entry that confirms physical and functional readiness against CWP (`DEL-052-03`).
   6.2 Flag any interface for which the vendor package does not match the EPC interface expectation; surface in the review log as a comment or rejection.

7. **Assemble package acceptance and turnover checklist.**
   7.1 Roll up dispositions from steps 4, 5, and 6 into the package acceptance checklist; one row per requirement / test / interface lane.
   7.2 Close out the checklist when every row is `Accepted` (with or without comments tracked in the punch list).

8. **Compile turnover evidence.**
   8.1 Assemble custody-transfer records, punch list status, and residual-action register substantiating handoff readiness.
   8.2 Reference the closed acceptance checklist (step 7) and the test/inspection evidence (step 5) by ID.

9. **Final integration review and sign-off.**
   9.1 The EPC Integrator review lead confirms the four artifacts are complete and internally consistent.
   9.2 Human sign-off is recorded outside this deliverable (per K-AUTH-1: only humans author binding approval records).

## Verification

| Check | How |
|---|---|
| Review log covers every `DEL-052-05` submittal. | Compare submittal index from `DEL-052-05` against review-log entries. |
| Acceptance checklist covers every requirement in `DEL-052-01`, `DEL-052-02`, `DEL-052-03`. | Cross-walk requirement IDs to checklist rows. |
| Every PKG-052 interface row has an acceptance entry. | Cross-walk `INTERFACE_REGISTER.csv` PKG-052 rows to checklist interface lane. |
| Test/inspection evidence dispositions are mapped to source acceptance criteria. | Inspect step 5.2 traceability column; mark `TBD` if source clauses still inaccessible. |
| Turnover evidence references the closed acceptance checklist and test evidence. | Inspect turnover record IDs against step 7 and step 5 outputs. |

## Records

- Vendor document review and comment log (`ART-F0F5332A58`)
- Package acceptance and turnover checklist (`ART-21EEB708EC`)
- Factory/shop test and inspection evidence (`ART-7F212499D9`)
- Turnover evidence record set (per `_CONTEXT.md` Anticipated Artifacts)
- This deliverable's `_run_records/` entries for each review pass.
