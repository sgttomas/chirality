# Procedure — EPC Vendor Package Review and Acceptance (DEL-025-06)

## Purpose

Procedure to produce and apply the EPC Integrator's review-and-acceptance record set for PKG-025 (MV VFD — 5000 HP, 6.9 kV, 3-phase, 60 Hz).

## Prerequisites

- Accepted EPC anchor deliverables:
  - `DEL-025-01` Scope of Work — accepted.
  - `DEL-025-02` Package Datasheet — accepted.
  - `DEL-025-03` Construction Work Package — accepted.
- Vendor-provided packages received:
  - `DEL-025-04` Vendor Engineered Equipment Package.
  - `DEL-025-05` Vendor Document Turnover Package.
- Reference set available:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
  - Gate 7 PROJECT_DECOMP snapshot registers.
  - `_Sources/26020-Package_Requirements.docx` (TBD — open before acceptance per Conflict Table CFT-2).
- Declared dependencies are DECLARED-mode and currently empty (`_DEPENDENCIES.md`). Confirm whether DEL-025-04 and DEL-025-05 should be declared upstream before acceptance is signed.

## Steps

1. **Initialize the acceptance record set** in this deliverable folder: create or update the vendor document review log, package acceptance checklist, test/inspection evidence index, and turnover evidence index.
2. **Build the acceptance trace matrix**: rows from `DEL-025-01` (SOW lines), `DEL-025-02` (Datasheet lines), `DEL-025-03` (CWP turnover lines); columns for vendor-evidence origin (`DEL-025-04` / `DEL-025-05` reference), reviewer, status, comments.
3. **Verify package identity and rating** (REQ-025-06-03): compare vendor package nameplate / datasheet to the EPC Datasheet `DEL-025-02` and to DBM §Medium-voltage services. Resolve or route Conflict Table CFT-1 (5000 HP vs ≥5,500 hp).
4. **Verify housing and layout fit** (REQ-025-06-04): compare vendor footprint and clearance data to the MV electrical-building configuration described in DBM §Electrical buildings.
5. **Verify interface coverage** (REQ-025-06-05): for each declared interface type (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports), confirm a vendor interface definition exists, matches `DEL-025-02`, and has an assigned owner.
6. **Review vendor documents** (REQ-025-06-01): walk the `DEL-025-05` document register; log every document with disposition. Mark missing classes as gaps.
7. **Review test and inspection evidence** (REQ-025-06-06): inspect FAT/routine/inspection reports and NCR closures; confirm pass/fail evidence and that any open NCR has a routed closure plan. Specific witness/hold points are `TBD` (Conflict Table CFT-2).
8. **Verify turnover completeness** (REQ-025-06-07): cross-check `DEL-025-03` turnover lines against signed turnover evidence.
9. **Compile the acceptance decision record** (REQ-025-06-08, REQ-025-06-09): assemble the trace matrix, the open-item list (with routing), the vendor and EPC revision IDs in scope, and the recommended acceptance disposition (accept / accept-with-conditions / reject).
10. **Submit for binding human acceptance**: per K-AUTH-1, the EPC Integrator's designated authority signs. Agent drafts are not the decision.
11. **File** the acceptance record set under this deliverable; update `_STATUS.md` only through the project's governance workflow (not by this skill beyond INITIALIZED).

## Verification

- The acceptance checklist contains every SOW, Datasheet, and CWP line with an evidence link or an explicit `TBD` / open-item route.
- Every interface type from `PACKAGE_REGISTER.csv` (PKG-025) has a corresponding accepted interface row.
- Every Conflict Table entry from `Guidance.md` is either resolved (with citation) or carried into the open-item list with an owner and a due date (`TBD` if unknown).
- The acceptance decision record carries a binding human signature.

## Records

- Vendor document review log.
- Package acceptance checklist (trace matrix).
- Test / inspection evidence index (with NCR register).
- Turnover evidence index.
- Acceptance decision record (signed).
- Open-item / deviation register (with routing).

Records remain within this deliverable folder; no writes occur outside scope.
