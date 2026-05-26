# Procedure — DEL-067-06 EPC Vendor Package Review and Acceptance

## Purpose

Produce the EPC Integrator's review-and-acceptance evidence pack for `PKG-067` Tanks, Sour Water (API 650) 4-25 (`26020-01-PT-19-005`; expected vessel tags `TK-9010-1`, `TK-9020-1`), demonstrating that `DEL-067-04` Vendor Engineered Equipment Package and `DEL-067-05` Vendor Document Turnover satisfy `DEL-067-01..03` and the Specification of this deliverable.

## Prerequisites

- `DEL-067-01_scope-of-work` (Scope of Work) accepted by the Owner.
- `DEL-067-02_package-datasheet` (Package Datasheet) issued to the Package Vendor and current.
- `DEL-067-03_construction-work-package` (Construction Work Package) issued and current.
- `DEL-067-04_vendor-engineered-equipment-package` and `DEL-067-05_vendor-document-turnover-package` at a maturity acceptable for integration review. (`_DEPENDENCIES.md` declares no upstream/downstream edges as of PREPARATION; this prerequisite is therefore stated as an `ASSUMPTION`-grade gate.)
- Access to: `_Sources/26020-Package_Requirements.docx` (Heading 22) — at minimum via the Markdown extract once produced; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` registers.
- Reviewer team assigned (EPC Integrator lead reviewer plus discipline reviewers for Process, Mechanical / Static Equipment, Piping, Electrical, I&C, Civil/Structural, Coatings & Insulation, Quality).

## Steps

1. **Establish acceptance baseline.**
   - Confirm the current revision of `DEL-067-02` Package Datasheet, `DEL-067-01` SOW, and `DEL-067-03` Construction Work Package are the references used for acceptance.
   - Record register-source basis used: `DELIVERABLE_REGISTER.csv` row `DEL-067-06`; `PACKAGE_REGISTER.csv` row `PKG-067`; `INTERFACE_REGISTER.csv` PKG-067 rows; `ARTIFACT_REGISTER.csv` `ART-5AF4728A78`, `ART-E14BC1C993`.
   - Record DBM-source basis used: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 493, 502-524, 261-297, 564-565.

2. **Receive and index vendor documents.**
   - Receive the Vendor Document Index (from `DEL-067-05`) and the vendor's engineering deliverable submittals.
   - Build the vendor document review log: one row per vendor deliverable; columns for submittal ID, revision, reviewer, due date, disposition (Accepted / Accepted with Comment / Rejected / Open), and link to comment register.

3. **Build the package acceptance checklist (SOW-, interface-, and artifact-indexed).**
   - Add one section per requirement in `Specification.md` (`R-067-06-01` through `R-067-06-14`).
   - For each requirement, list the evidence to be inspected and the acceptance criterion (numeric or qualitative).

4. **Conduct discipline reviews.** For each discipline:
   - Process / Static Equipment: confirm tank design code (modified API 650), 16 oz test pressure (DBM line 518), fluid-characterization assumptions (DBM line 508), capacity, design SG, PVRV/EPRV scope, blanket-gas/VRU interface, sour-vapour isolation philosophy.
   - Mechanical / Piping: confirm nozzles, appurtenances, supports, hydrotest plan, piping tie-ins per `INTERFACE_REGISTER.csv` PKG-067 Process Piping, Drain/Containment, Relief/Flare/Vent.
   - Electrical: confirm heat-tracing design, area-lighting interface, grounding/bonding, cathodic protection.
   - I&C: confirm tank instrumentation (level, temperature, pressure, hydrocarbon skim float status), control narrative integration.
   - Civil/Structural: confirm foundations, grading/site-drainage/spill-containment integration; bund / containment volume per applicable code.
   - Coatings & Insulation: confirm internal Devchem 253 application records and external insulation/heating package.
   - Quality: confirm MTRs, ITP execution, IRC, NDE, weld maps, sour-service material compliance.
   - Each discipline produces an entry in the comment register with disposition recommendations.

5. **Verify physical interfaces (interface walk-down).**
   - Walk down the as-built / as-installed configuration against each `YES`-marked interface row in `INTERFACE_REGISTER.csv` for PKG-067.
   - Record acceptance per interface; flag any non-conformance.

6. **Verify plant-spacing constraints.**
   - Dimensional check of as-built plot vs. NFPA 30 / OGAOM 9.6.15 values (DBM lines 261-297): tank-to-tank, tank-to-flare, tank-to-fired-heater, tank-to-road.
   - Record measured distances in the acceptance checklist.

7. **Collect test and inspection evidence.**
   - Hydrotest / leak-test packages.
   - Coating QA records (DFT, holiday testing, Devchem 253 application records).
   - Heat-trace energization and commissioning records.
   - Instrumentation FAT / loop-check records.
   - PVRV / EPRV bench-test records.
   - Material certificates and weld NDE records.

8. **Collect turnover evidence.**
   - Manufacturing Record Book / Vendor Data Book.
   - Pressure-equipment registration package (provincial jurisdiction TBD per `CONF-067-06-02`).
   - SPIR (Spare Parts Interchangeability Record).
   - IOM (operation, maintenance, inspection).
   - Pre-startup walk-down records.

9. **Resolve / carry open items.**
   - For each open item identified by the DBM (DBM lines 521-524, 564-565) or raised during review, record disposition: Closed (with evidence) or Carried (with target close date, responsible party, and commissioning impact).
   - Refresh the Conflict Table in `Guidance.md` if new conflicts emerge.

10. **Issue the EPC acceptance decision.**
    - Produce the acceptance recommendation: Accepted / Accepted with Carryover / Rejected.
    - Where Accepted with Carryover, list each carryover item with mitigation.
    - Route for human approval per project change-control practice; the EPC Integrator and Owner are the binding signatories — this deliverable does not itself constitute an approval.

11. **Finalize the deliverable artifacts.**
    - Vendor document review log (final).
    - Package acceptance checklist (final, signed by discipline reviewers).
    - Test / inspection evidence bundle (indexed).
    - Turnover evidence bundle (indexed).
    - Open-items disposition log (final).

## Verification

| Step | Verification |
|---|---|
| 1 | Acceptance baseline references match the latest accepted revisions of `DEL-067-01..03` and the GATE-07 register set. |
| 2 | Vendor document review log row count = vendor document index count; no orphans. |
| 3 | Every requirement (`R-067-06-01` through `R-067-06-14`) has at least one row in the checklist. |
| 4 | Every discipline review has an entry; no discipline is "not reviewed". |
| 5 | Every `YES`-marked PKG-067 interface row in `INTERFACE_REGISTER.csv` has an acceptance result. |
| 6 | Plot-plan dimensional check is documented with measured values; no spacing value left "as designed" without measurement. |
| 7 | Test/inspection evidence bundle has an explicit cross-link from each evidence document to the requirement(s) it satisfies. |
| 8 | Turnover bundle is complete or carryover items are explicit. |
| 9 | All open items have a disposition; none are silently closed. |
| 10 | Acceptance decision routes to human signatories; this deliverable carries the recommendation, not the approval. |
| 11 | Final artifact set matches `_CONTEXT.md` Anticipated Artifacts list. |

## Records

The following records constitute the deliverable upon completion:

- `Vendor_Document_Review_Log.{csv|xlsx}` — per-document review log.
- `Package_Acceptance_Checklist.{csv|xlsx}` — SOW-, interface-, requirement-, and artifact-indexed.
- `Test_Inspection_Evidence/` — indexed bundle of MTRs, ITP records, IRC, hydrotest packages, coating QA, heat-trace records, instrumentation FAT, PVRV/EPRV bench tests.
- `Turnover_Evidence/` — indexed bundle of MRB / VDB, pressure-equipment registration package, SPIR, IOM.
- `Open_Items_Disposition_Log.{csv|xlsx}` — per-item status and carryover plan.
- `Acceptance_Decision.md` — recommendation, signatories, carryover summary, and links to evidence.

Specific filenames, formats, and IDs are TBD pending project document-control conventions; the table above states the artifact set, not naming.
