# Procedure — EPC Vendor Package Review and Acceptance (DEL-064-06)

## Purpose

Step-by-step operational procedure for the EPC Integrator to review the Tanks, Water (PKG-064; tag `26020-01-PT-19-002`) vendor package submittals and produce the four anticipated artifacts: vendor document review log, package acceptance checklist, test/inspection evidence pack, and turnover evidence.

## Prerequisites

- The four reference deliverables in PKG-064 are available at their working location or a known snapshot:
  - DEL-064-01 — Scope of Work
  - DEL-064-02 — Package Datasheet
  - DEL-064-03 — Construction Work Package
  - DEL-064-04 — Vendor Engineered Equipment Package (vendor submittals to be reviewed)
  - DEL-064-05 — Vendor Document Turnover Package
- Source materials accessible:
  - `_Sources/26020-Package_Requirements.docx` (heading 19 "26020-01-PT-19-002 - Tanks, Water")
  - Latest Packages Interfaces workbook (currently `_Sources/26020-Packages_Interfaces_4_export.xlsx`; reconcile against the version cited in source — see Guidance Conflict Table CT-1).
- Decomposition snapshot reference: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Reviewer authorization: EPC Integrator (lead reviewer) plus Package Vendor representative for clarifications. [Source: `_CONTEXT.md` ResponsibleParty]
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` at the time of this run; treat upstream traceability as evidence-driven rather than blocker-driven.

## Steps

### Step 1 — Establish the Acceptance Inventory baseline
1. Open `Datasheet.md` "Acceptance Inventory — Vendor Engineering Deliverables to Review".
2. For each row, create a line in the vendor document review log with columns: Group, Deliverable ID (source), Deliverable Name, Vendor submittal ID (TBD), Submittal version, Received date, Reviewer, Disposition (pending), Disposition date, Comments, Superseded-by.
3. Record the source row reference for each entry (SRC1 "Vendor Engineering Deliverables").

### Step 2 — Build the interface coverage matrix
1. Open `Datasheet.md` "Interfaces Subject to Review" and list every interface marked "Yes".
2. For each "Yes" interface, list the vendor deliverable IDs from the Acceptance Inventory that satisfy it (mapping defined in Specification R-6).
3. For each interface marked "No", flag any vendor submittal that claims coverage in that area for human ruling (Specification R-7).

### Step 3 — Pre-acceptance technical review of core technical deliverables
Verify these against the Datasheet Attributes and Specification requirements before broader acceptance:
1. MEC-001 Mechanical Design Basis — confirm it enumerates the modification points to API 650 (Specification R-4, Guidance Conflict CT-3). If absent, reject and return to vendor; do not proceed to Step 4 for tank-related items.
2. MEC-005 Static Equipment Specifications and MEC-011 Storage Tank Data Sheets — confirm design pressure 32 oz / 1.0 oz vacuum, design temperature -40 to 60 deg C, capacity 2 x 2,000 bbl, sweet produced water service, LP fuel gas blanket provision, external insulation and heating provision (Specification R-3, R-5).
3. MEC-014 Mechanical Calculation Package — confirm calculations support the Datasheet values.
4. PRO-014 Relief and Flare Design Basis, PRO-015 PSV Sizing Calculations, PRO-016 Relief Valve Data Sheets — confirm the LP fuel gas blanketing scheme has a defined relief path (Guidance "Vapour-space safety basis").
5. STR-005 Foundation Design Calculations and STR-013 Anchor Bolt / Embedment Drawings — confirm they declare the vendor/EPC scope split at the tank base (Guidance "By others" exclusion).
6. PLN-015 Corrosion Protection Design Basis and PLN-016 Cathodic Protection Design Package — confirm coverage matches the "Cathodic Protection: Yes" interface.
7. Heater provisioning (Guidance Conflict CT-2): confirm whether vendor-supplied integral heater or EPC-supplied service; route to human ruling if ambiguous.

### Step 4 — Per-item review and disposition
For each remaining row in the review log:
1. Receive vendor submittal; record submittal ID, version, received date.
2. Apply Specification requirements R-1 through R-12.
3. Set disposition: ACCEPT, ACCEPT-WITH-COMMENT (record deviation), or REJECT (record reason; require resubmittal).
4. For ACCEPT-WITH-COMMENT: capture the deviation in the package acceptance checklist and tag for human ruling if material.
5. Re-review superseded submittals; close prior entries with "Superseded-by" pointer.

### Step 5 — Quality and inspection evidence assembly
1. Confirm QLT-003 Inspection and Test Plan is reviewed and witnessed/sampled per the agreed witness/hold-point plan.
2. Confirm QLT-013 Material Test Reports / Certificates are received and traceable to heat numbers on installed materials.
3. Confirm QLT-020 Inspection Release Certificate is issued.
4. Confirm MEC-021 Equipment FAT Procedure was approved and MEC-022 Equipment FAT Performance Test Report has been issued and reviewed.
5. Confirm PIP-024 Hydrotest / Pressure Test Packages are complete for in-vendor-scope piping.
6. Build the test/inspection evidence pack with references to the above; record locations.

### Step 6 — Open-item closure (TBD list)
For each source-declared open item (Specification R-10):
- "Other throughputs: TBD" — confirm vendor-provided throughputs across all operating modes.
- "Operating temperature: TBD for Item No. 1" — confirm vendor-stated operating temperature consistent with design temperature and freeze-prevention basis.
- "Interface Coordination Notes: TBD" — confirm at least one entry of substance, or explicitly waive with human ruling.
Record disposition for each: CLOSED (with evidence pointer), CARRIED (with named deviation and human ruling), or REJECTED (return to vendor).

### Step 7 — Cross-deliverable reconciliation
1. Cross-check the completed review log against DEL-064-05 Vendor Document Turnover Package register (Specification R-8). Every accepted item should appear in turnover; every turnover item should appear here.
2. Cross-check accepted scope against DEL-064-01 Scope of Work boundary; flag any out-of-bounds acceptance.
3. Cross-check accepted scope against DEL-064-03 Construction Work Package readiness; flag any item that constrains construction sequence.

### Step 8 — Acceptance decision
1. Tally the package acceptance checklist: number of ACCEPT, ACCEPT-WITH-COMMENT, REJECT entries; number of open Conflict Table items (`Guidance.md`); number of carried deviations.
2. Apply the decision rule (proposed): PACKAGE ACCEPTED only when there are zero REJECT entries on safety-critical items (relief, blanketing, structural anchoring, cathodic protection, FAT) and zero open Conflict Table items affecting those areas. Otherwise PACKAGE NOT YET ACCEPTED with a list of blocking items.
3. Record the decision, the reviewer(s), and the date in the acceptance checklist.

### Step 9 — Turnover evidence handoff
1. Compile the turnover evidence pack: acceptance decision, review log final version, acceptance checklist, test/inspection evidence pack, and resolved-deviation register.
2. Hand off to operations / commissioning per the project handoff convention. [Method TBD; defer to the project-level handoff procedure.]

## Verification

| Step | Verification |
|---|---|
| 1 | Review log row count equals Acceptance Inventory row count plus any vendor-added items. |
| 2 | Every "Yes" interface has at least one mapped vendor deliverable; every "No" interface has zero claimed vendor coverage (or one explicit human ruling). |
| 3 | Each core technical deliverable shows source-cited attribute confirmation in the package acceptance checklist. |
| 4 | Every row in the review log has a final disposition and disposition date. |
| 5 | Test/inspection evidence pack includes all five enumerated artifacts (QLT-003, QLT-013, QLT-020, MEC-022, PIP-024). |
| 6 | Each source-declared open item has a disposition entry. |
| 7 | Cross-deliverable reconciliation produces zero unresolved deltas, or each delta has a human ruling. |
| 8 | Acceptance decision is recorded with reviewer, date, and basis. |
| 9 | Turnover handoff is logged with recipient and acknowledgement. |

## Records

The following records result from this procedure (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log (Step 1, finalized in Step 4).
- Package acceptance checklist (Steps 3-8; signed in Step 8).
- Test/inspection evidence pack (Step 5).
- Turnover evidence (Step 9).
- Conflict resolution log (entries promoted from `Guidance.md` Conflict Table with their rulings).

## Source Key

- SRC1 = `_Sources/26020-Package_Requirements.docx`, heading 19 ("26020-01-PT-19-002 - Tanks, Water"). Sections cited inline and in `Specification.md`.
