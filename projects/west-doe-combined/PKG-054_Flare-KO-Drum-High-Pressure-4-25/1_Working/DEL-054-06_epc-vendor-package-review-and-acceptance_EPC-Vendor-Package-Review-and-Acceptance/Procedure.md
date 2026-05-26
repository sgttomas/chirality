# Procedure — DEL-054-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes how the EPC Integrator **produces** the vendor-package review-and-acceptance evidence pack for the HP Flare KO Drum (HP) package. It is not a procedure to operate the equipment.

## Prerequisites

- Accepted upstream snapshot available: `GATE-07_Final_Published_2026-05-24` (`_DEPENDENCIES.md`).
- Source slice accessible: `_Sources/26020-Package_Requirements.docx` Heading 9 — `26020-01-PT-17-002 - Flare KO Drum (HP)`.
- EPC anchor deliverables drafted or available for cross-reference: `DEL-054-01` (Scope of Work), `DEL-054-02` (Package Datasheet), `DEL-054-03` (Construction Work Package).
- Vendor production-unit deliverables available for review: `DEL-054-04` (Vendor Engineered Equipment Package), `DEL-054-05` (Vendor Document Turnover Package). (`_DEPENDENCIES.md` declares no formal upstream edges as of PREPARATION — ASSUMPTION that these are the de facto upstreams via package decomposition.)
- Reviewer assignments and access to the Vendor Document Index (`PRQ-009`) established.

## Steps

1. **Establish the acceptance register.** Create the vendor document review log seeded from the Heading 9 "Vendor Engineering Deliverables" enumeration. Every listed deliverable becomes one row with disposition fields (`SUBMITTED`, `ACCEPTED`, `REJECTED`, `OPEN`).
2. **Map SOW coverage.** Build a traceability matrix linking `SOW-0075`, `SOW-0076`, `SOW-0077`, `SOW-0078` to the acceptance-checklist rows and to evidence artifacts. (Verifies `R-054-06-01`.)
3. **Review Package Datasheet alignment.** Reconcile `DEL-054-02` design values with vendor-submitted `MEC-009`, `MEC-003`, `MEC-007`, and flare-design artifacts (`PRO-014`, `PRO-015`, `PRO-016`, `PRO-017`, `PRO-018`). Flag mismatches; defer numeric reconciliation to the values actually submitted (do not assert design values not yet in vendor docs). (Verifies `R-054-06-11`.)
4. **Walk the Basic Scope and Major Included Equipment.** Confirm that the vendor package supplies: HP flare KO drum `V-4100-1`, transfer pump `P-4100-1`, liquid handling to condensate slop tank, truck-out provision, and related package connections. (Verifies `R-054-06-03`.)
5. **Review the HP/Cryo tie-in.** Inspect P&IDs (`PRO-008`), tie-in list (`PIP-004`), and as-built isos (`PIP-008`, `PIP-028`) to confirm the HP flare header tie-in to the cryogenic flare header downstream of the drum, before the common HP/Cryo flare stack. (Verifies `R-054-06-04`.)
6. **Review EHT and insulation of outdoor HP flare headers.** Inspect `ELE-018` EHT design package, `PIP-020` insulation/heat tracing schedule, and `PIP-021` heat tracing interface package. Confirm energization records (`ELE-030`). (Verifies `R-054-06-05`.)
7. **Execute interface-by-interface acceptance.** For each Heading 9 Physical Interface Summary row marked `Yes`, complete an interface acceptance checklist row referencing the relevant vendor artifact(s). (Verifies `R-054-06-06`.)
8. **Vessel acceptance.** Review pressure-vessel data sheet (`MEC-009`), mechanical calc package (`MEC-014`), hydrotest packages (`PIP-024`), and pressure equipment registration package (`REG-022`). Confirm jurisdictional registration acceptance (authority TBD — ASSUMPTION). (Verifies `R-054-06-07`.)
9. **Rotating-equipment acceptance.** Review pump data sheet (`MEC-007`), NPSH calcs (`PRO-013`), mechanical seal / lube oil spec (`MEC-019`), motor starting study (`ELE-011`), and FAT report (`MEC-022`). (Verifies `R-054-06-08`.)
10. **Quality records audit.** Assemble Supplier Quality Plan (`QLT-006`), ITP execution evidence against `QLT-003`, MTRs (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / Vendor Data Book (`QLT-021` / `MEC-023` / `PRQ-016`). (Verifies `R-054-06-09`.)
11. **Turnover readiness.** Confirm SPIR (`PRQ-015`), Logistics / Shipping Plan (`PRQ-013`), and Mechanical Equipment IOM Manual (`MEC-025`) are present and accepted. Hand off the Construction Work Package interface to `DEL-054-03`. (Verifies `R-054-06-10`.)
12. **Open-items disposition.** Close or explicitly carry every item from the source "Scope Notes / Open Items" and from any reviewer-raised open items. (Verifies `R-054-06-12`.)
13. **Issue the acceptance package.** Compile the four acceptance artifacts (document review log; package acceptance checklist; test/inspection evidence bundle; turnover evidence bundle), apply EPC Integrator sign-off, and route for human approval per project governance. (No agent may certify acceptance; this step is human-decided.)

## Verification

- Every Heading 9 "Vendor Engineering Deliverable" row appears in the vendor document review log with a disposition.
- Every `Yes`-marked interface in the Heading 9 Physical Interface Summary has an acceptance-checklist row with linked evidence.
- Every requirement `R-054-06-01` through `R-054-06-12` (Specification.md) is linked to at least one verification record.
- All numeric design values in the acceptance pack are either reconciled to a vendor submittal or carried as `TBD` with a named owner.
- Open items from the source's "Scope Notes / Open Items" are closed or carried with explicit disposition.

## Records

- Vendor document review log (live register; archived at acceptance).
- Package acceptance checklist (SOW-, interface-, and artifact-indexed; signed).
- Test / inspection evidence bundle (FAT records, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, registration package, SPIR, IOM).
- Open-items disposition log.
- EPC Integrator acceptance sign-off (human-authored; required for binding acceptance — `K-AUTH-1`).
