# Procedure — DEL-063-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes how the EPC Integrator **produces** the vendor-package review-and-acceptance evidence pack for the DSO storage tank package (`26020-01-PT-19-001`). It is not a procedure to operate the tank.

## Prerequisites

- Accepted upstream snapshot available: `GATE-07_Final_Published_2026-05-24` (`_DEPENDENCIES.md`).
- Source slice accessible: `_Sources/26020-Package_Requirements.docx` heading `26020-01-PT-19-001 - Tanks, DSO`.
- EPC anchor deliverables drafted or available for cross-reference: `DEL-063-01` (Scope of Work), `DEL-063-02` (Package Datasheet), `DEL-063-03` (Construction Work Package).
- Vendor production-unit deliverables available for review: `DEL-063-04` (Vendor Engineered Equipment Package), `DEL-063-05` (Vendor Document Turnover Package). (`_DEPENDENCIES.md` declares no formal upstream edges as of PREPARATION — ASSUMPTION that these are the de facto upstreams via package decomposition.)
- Reviewer assignments and access to the Vendor Document Index (`PRQ-009`) established.

## Steps

1. **Establish the acceptance register.** Create the vendor document review log seeded from the source's "Vendor Engineering Deliverables" enumeration for `26020-01-PT-19-001`. Every listed deliverable becomes one row with disposition fields (`SUBMITTED`, `ACCEPTED`, `REJECTED`, `OPEN`).
2. **Map SOW coverage.** Build a traceability matrix linking `SOW-0209`, `SOW-0210`, `SOW-0211`, `SOW-0212` to acceptance-checklist rows and to evidence artifacts. (Verifies `R-063-06-01`.)
3. **Review Package Datasheet alignment.** Reconcile `DEL-063-02` design values with vendor-submitted Storage Tank Data Sheet (`MEC-011`), Static Equipment Specifications (`MEC-005`), Mechanical Equipment Data Sheets (`MEC-003`), and Mechanical Calculation Package (`MEC-014`). Flag mismatches; defer numeric reconciliation to vendor submittals (do not assert design values not yet in vendor docs). (Verifies `R-063-06-05`, `R-063-06-12`.)
4. **Walk the Basic Scope and Major Included Equipment.** Confirm that the vendor package supplies: one (1) atmospheric DSO storage tank designed and fabricated to modified API 650; 400 bbl nominal; integral heater (vendor-designed, ≥ 32.2 °C / 90 °F); internal coating (floor, walls, roof); insulation for above-pour-point truck-out and handling. (Verifies `R-063-06-03`.)
5. **Review process tie-ins to the DSO separator and caustic regeneration system.** Inspect P&IDs (`PRO-008`), tie-in list (`PIP-004`), and as-built isos (`PIP-008`, `PIP-028`) to confirm level-controlled feed from the DSO separator and routing within the caustic regeneration system. (Verifies `R-063-06-04`.)
6. **Execute interface-by-interface acceptance.** For each source Physical Interface Summary row marked `Yes` for `26020-01-PT-19-001` (Process Piping; Relief / Flare / Vent; Drain / Containment; Area / Exterior Lighting; Grounding / Bonding; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports), complete an interface acceptance checklist row referencing the relevant vendor artifact(s). For each row marked `No`, record explicit exclusion. (Verifies `R-063-06-06`.)
7. **Vessel and registration acceptance.** Review Storage Tank Data Sheet (`MEC-011`), Mechanical Calculation Package (`MEC-014`), and Hydrotest / Pressure Test Packages (`PIP-024`). Issue a registration-applicability memo for `REG-022`; if applicable, confirm jurisdictional registration acceptance (authority TBD — ASSUMPTION), otherwise record formal exclusion. (Verifies `R-063-06-07`, partial `R-063-06-11`.)
8. **Cathodic protection and grounding acceptance.** Review Corrosion Protection Design Basis (`PLN-015`), Cathodic Protection Design Package (`PLN-016`), Grounding / Earthing Study (`ELE-012`), and Earthing / Bonding Layout Drawings (`ELE-019`). Confirm coordination with internal coating to avoid double-protection conflicts. (Verifies `R-063-06-08`.)
9. **Containment and drainage acceptance.** Review Process Sewer / Closed Drain Design Basis (`PRO-023`), Bund / Dike / Secondary Containment Drawings (`CIV-014`), Grading Plan (`CIV-003`), Drainage / Stormwater Management Report (`CIV-004`), and Retention Pond / Containment Basin Design (`CIV-015`) where applicable. (Verifies `R-063-06-09`.)
10. **Quality records audit.** Assemble Supplier Quality Plan (`QLT-006`), ITP execution evidence against `QLT-003`, MTRs (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / Vendor Data Book (`QLT-021` / `MEC-023` / `PRQ-016`). Pay particular attention to internal-coating QA (surface prep, DFT, holiday testing) given high failure cost. (Verifies `R-063-06-10`.)
11. **Turnover readiness.** Confirm SPIR (`PRQ-015`), Logistics / Shipping Plan (`PRQ-013`), and Mechanical Equipment IOM Manual (`MEC-025`) are present and accepted. Hand off the Construction Work Package interface to `DEL-063-03`. (Verifies `R-063-06-11`.)
12. **"By others" boundary confirmation.** Issue a memo cross-referencing `DEL-063-03` Construction Work Package and discipline production packages to confirm that foundations, mounting at site, electrical/instrumentation tie-ins, platforms, staircase, etc., are scoped elsewhere and not expected from the Package Vendor. (Verifies `R-063-06-14`.)
13. **Open-items disposition.** Close or explicitly carry every `TBD`/`TBC` item from the source "Scope Notes / Open Items" (capacity/design throughput; minimum ambient temperature; flow rate; insulation minimum temperature) and from any reviewer-raised open items. (Verifies `R-063-06-13`.)
14. **Issue the acceptance package.** Compile the four acceptance artifacts (document review log; package acceptance checklist; test/inspection evidence bundle; turnover evidence bundle), apply EPC Integrator sign-off, and route for human approval per project governance. (No agent may certify acceptance; this step is human-decided — `K-AUTH-1`.)

## Verification

- Every source-listed "Vendor Engineering Deliverable" row for `26020-01-PT-19-001` appears in the vendor document review log with a disposition.
- Every `Yes`-marked interface in the source's Physical Interface Summary has an acceptance-checklist row with linked evidence; every `No`-marked interface is explicitly recorded as out-of-scope.
- Every requirement `R-063-06-01` through `R-063-06-14` (Specification.md) is linked to at least one verification record.
- All numeric design values in the acceptance pack are either reconciled to a vendor submittal or carried as `TBD` with a named owner.
- Open items from the source's "Scope Notes / Open Items" are closed or carried with explicit disposition.
- Registration applicability for `REG-022` has an explicit ruling (applied or excluded with basis).

## Records

- Vendor document review log (live register; archived at acceptance).
- Package acceptance checklist (SOW-, interface-, and artifact-indexed; signed).
- Test / inspection evidence bundle (FAT records, ITP execution, MTRs, IRC, internal-coating QA).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, SPIR, IOM; `REG-022` or exclusion memo).
- Open-items disposition log.
- "By others" boundary confirmation memo.
- EPC Integrator acceptance sign-off (human-authored; required for binding acceptance — `K-AUTH-1`).
