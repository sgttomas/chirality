# Procedure — DEL-061-06 EPC Vendor Package Review and Acceptance

**Interpretation:** This procedure describes how the EPC Integrator **produces** the vendor-package review-and-acceptance evidence pack for the NGL Booster and Transfer Pumps Building (`PKG-061`). It is not a procedure to operate the equipment.

## Prerequisites

- Accepted upstream snapshot available: `GATE-07_Final_Published_2026-05-24` (`_DEPENDENCIES.md`).
- Source slice locally accessible: `_Sources/26020-Package_Requirements.docx` Heading 17 — `NGL Booster and Transfer Pumps Building`. (At time of this initialization run the Heading 17 slice is NOT locally accessible in markdown; converting / extracting the slice is a precondition for moving beyond `INITIALIZED` to a source-grounded acceptance pack.)
- Interface workbook row resolved: `_Sources/26020-Packages_Interfaces_4_export.xlsx` package row 75 columns enumerated to a usable interface set.
- EPC anchor deliverables drafted or available for cross-reference: `DEL-061-01` (Scope of Work), `DEL-061-02` (Package Datasheet), `DEL-061-03` (Construction Work Package).
- Vendor production-unit deliverables available for review: `DEL-061-04` (Vendor Engineered Equipment Package), `DEL-061-05` (Vendor Document Turnover Package). (`_DEPENDENCIES.md` declares no formal upstream edges as of PREPARATION — ASSUMPTION that these are the de facto upstreams via package decomposition.)
- Reviewer assignments and access to the Vendor Document Index (`PRQ-009`) established.

## Steps

1. **Resolve the Heading 17 source slice.** Before substantive acceptance, ensure `26020-Package_Requirements.docx` Heading 17 is locally accessible in markdown so that "Basic Scope", "Major Included Equipment", "Location / Status", "Scope Notes / Open Items", "Physical Interface Summary", and "Vendor Engineering Deliverables" content can be read. Without this, the acceptance pack will be structurally complete but cannot be source-grounded at the clause level. (Verifies precondition.)
2. **Establish the acceptance register.** Create the vendor document review log seeded from the Heading 17 "Vendor Engineering Deliverables" enumeration. Every listed deliverable becomes one row with disposition fields (`SUBMITTED`, `ACCEPTED`, `REJECTED`, `OPEN`). (Verifies `R-061-06-02`.)
3. **Map SOW coverage.** Build a traceability matrix linking `SOW-0149`, `SOW-0150`, `SOW-0151`, `SOW-0152` to the acceptance-checklist rows and to evidence artifacts. (Verifies `R-061-06-01`.)
4. **Review Package Datasheet alignment.** Reconcile `DEL-061-02` design values with vendor-submitted pump data sheets (`MEC-007`), NPSH calcs (`PRO-013`), and other rotating-equipment artifacts. Flag mismatches; defer numeric reconciliation to the values actually submitted (do not assert design values not yet in vendor docs). (Verifies `R-061-06-11`.)
5. **Walk the Basic Scope and Major Included Equipment.** Confirm that the vendor package supplies the booster and transfer pumps and the housing building scope as enumerated in Heading 17 "Basic Scope" / "Major Included Equipment". Specific items TBD until source slice is locally accessible. (Verifies `R-061-06-03`.)
6. **Execute interface-by-interface acceptance.** For each Heading 17 Physical Interface Summary row marked `Yes`, complete an interface acceptance checklist row referencing the relevant vendor artifact(s); cross-check `26020-Packages_Interfaces_4_export.xlsx` row 75. (Verifies `R-061-06-05`.)
7. **Rotating-equipment acceptance.** Review pump data sheets (`MEC-007`), NPSH calcs (`PRO-013`), mechanical seal / lube oil spec (`MEC-019`), motor starting study (`ELE-011`), and FAT report (`MEC-022`) for each booster and transfer pump. (Verifies `R-061-06-06`.)
8. **Building / enclosure acceptance.** Review architectural, structural, HVAC, and life-safety submittals for the pumps building. Specific artifact codes TBD until Heading 17 source slice is locally accessible. (Verifies `R-061-06-07`.)
9. **Electrical, area-classification, and F&G acceptance.** Review area-classification drawings, motor specifications, building lighting, EHT (if any), grounding/bonding, and fire/gas detection submittals. (Verifies `R-061-06-08`.)
10. **Quality records audit.** Assemble Supplier Quality Plan (`QLT-006`), ITP execution evidence against `QLT-003`, MTRs (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / Vendor Data Book (`QLT-021` / `MEC-023` / `PRQ-016`). (Verifies `R-061-06-09`.)
11. **Turnover readiness.** Confirm SPIR (`PRQ-015`), Logistics / Shipping Plan (`PRQ-013`), Mechanical Equipment IOM Manual (`MEC-025`), and building-handover records are present and accepted. Hand off the Construction Work Package interface to `DEL-061-03`. (Verifies `R-061-06-10`.)
12. **Open-items disposition.** Close or explicitly carry every item from the Heading 17 "Scope Notes / Open Items" and from any reviewer-raised open items. (Verifies `R-061-06-04`, `R-061-06-12`.)
13. **Issue the acceptance package.** Compile the acceptance artifacts (document review log; package acceptance checklist; test/inspection evidence bundle; turnover evidence bundle; open-items disposition log), apply EPC Integrator sign-off, and route for human approval per project governance. (No agent may certify acceptance; this step is human-decided per `K-AUTH-1`.)

## Verification

- Every Heading 17 "Vendor Engineering Deliverable" row appears in the vendor document review log with a disposition.
- Every `Yes`-marked interface in the Heading 17 Physical Interface Summary has an acceptance-checklist row with linked evidence.
- Every requirement `R-061-06-01` through `R-061-06-12` (`Specification.md`) is linked to at least one verification record.
- All numeric design values in the acceptance pack are either reconciled to a vendor submittal or carried as `TBD` with a named owner.
- Open items from the Heading 17 "Scope Notes / Open Items" are closed or carried with explicit disposition.
- Building scope (architectural, structural, HVAC, F&G) is covered alongside rotating-equipment scope; no discipline gaps.

## Records

- Vendor document review log (live register; archived at acceptance).
- Package acceptance checklist (SOW-, interface-, and artifact-indexed; signed).
- Test / inspection evidence bundle (FAT records, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages where applicable, SPIR, IOM, building-handover records).
- Open-items disposition log.
- EPC Integrator acceptance sign-off (human-authored; required for binding acceptance — `K-AUTH-1`).
