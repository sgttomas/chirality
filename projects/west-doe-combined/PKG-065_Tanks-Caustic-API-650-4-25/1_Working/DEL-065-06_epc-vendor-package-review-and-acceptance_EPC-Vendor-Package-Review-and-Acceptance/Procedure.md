# Procedure — DEL-065-06 EPC Vendor Package Review and Acceptance

EpistemicStatus: DRAFT (Pass 1/Pass 2)

## Purpose

Operational procedure for the EPC Integrator to produce the vendor document review log, package acceptance checklist, test/inspection evidence package, and turnover evidence for `PKG-065` (Tanks, Caustic API 650, 4-25). (`_CONTEXT.md` Scope and Anticipated Artifacts.)

## Prerequisites

Inputs required before this procedure can run to completion:

- **EPC Scope of Work** — DEL-065-01 (DELIVERABLE_REGISTER.csv row 486).
- **EPC Package Datasheet** — DEL-065-02 (row 487).
- **EPC Construction Work Package** — DEL-065-03 (row 488).
- **Vendor Engineered Equipment Package** — DEL-065-04 (row 489).
- **Vendor Document Turnover Package** — DEL-065-05 (row 490).
- **Authoritative references** — API 650 (location TBD), `26020-Package_Requirements.docx` package heading 20 (binary, slice TBD), DBM-Deepcut `4-25_Deepcut_DBM.md` (locally accessible).
- **Declared upstream dependencies** — none declared in `_DEPENDENCIES.md`; treat the five sibling deliverables above as de-facto upstream evidence inputs (ASSUMPTION).

## Steps

1. **Assemble the acceptance basis.** Snapshot the latest accepted versions of DEL-065-01, DEL-065-02, and DEL-065-03. Record source paths and revisions in the vendor document review log header.
2. **Index vendor submittals.** Build the vendor document review log from the index in DEL-065-05. One row per submittal. Columns: submittal ID, title, revision, received date, reviewer, disposition (A/B/C or equivalent — exact scheme TBD), date dispositioned, comments.
3. **Conformance review — Scope of Work.** For each requirement in DEL-065-01, identify the vendor evidence and record a conformance status in the acceptance checklist (REQ-06-02).
4. **Conformance review — Package Datasheet.** For each datasheet attribute in DEL-065-02 (and the DBM-cited values in `Datasheet.md` REQ-06-04 to REQ-06-08), confirm the vendor value matches or is dispositioned. Record deviations.
5. **Code conformance — API 650.** Verify code stamps, nameplates, design calculations, weld inspection records, and pressure-test records. Capture any clauses where vendor approach deviates from API 650 (REQ-06-03). Source slices for specific clauses: TBD.
6. **Material acceptance.** Confirm absence of aluminum in caustic building; SS cladding/straps in caustic exposure areas; polymer or other caustic-compatible tank materials (REQ-06-07; DBM line 1566).
7. **Installation acceptance.** Confirm indoor installation within Mercaptan Treating Unit building or immediately adjacent area (REQ-06-08; DBM line 1552).
8. **Safety-system acceptance.** Confirm safety-shower provisions with discrete control-room alert; flag shower quantity/locations as open TBD (REQ-06-09; DBM line 1552).
9. **Construction Work Package alignment.** Verify tie-ins, turnover checklist items, and installation/inspection plan from DEL-065-03 are addressed by vendor documentation (REQ-06-10).
10. **Cross-facility interface check.** Verify spent caustic tank off-gas routing to the 3-25 incinerator, including KO drum, flame arrestor, and supplemental fuel-gas basis (DBM lines 1562, 1570–1572). Carry supplemental fuel-gas rate as TBD if not closed.
11. **Test and inspection evidence package.** Collect all ITRs, NDE reports, hydrostatic / pneumatic test records, and witness/hold-point closure records (REQ-06-11). Specific test list: TBD pending API 650 clause review.
12. **Turnover evidence package.** Assemble turnover documents per the format defined for the project (TBD); confirm completeness against the turnover checklist from DEL-065-03 (REQ-06-12).
13. **Open-item register.** For each TBD or unresolved deviation, record owner, target close date, and acceptance condition (with-comments vs. hold).
14. **Acceptance disposition.** EPC Integrator records final disposition (accepted / accepted with carry-forward / not accepted) with supporting artifact references.

## Verification

- Every requirement in `Specification.md` has at least one row in the acceptance checklist with a disposition.
- Every submittal in DEL-065-05 has a row in the vendor document review log with a disposition.
- Every API 650 verification activity (code stamp, calcs, NDE, pressure test) has a referenced ITR or equivalent.
- The open-item register lists every TBD, with owner and target close date (target dates may themselves be TBD on first pass).
- Cross-facility interface evidence (3-25 incinerator route) is explicitly addressed, not assumed.

## Records

The procedure produces:

- `Vendor document review log` — one row per vendor submittal with disposition.
- `Package acceptance checklist` — one row per Specification requirement with verification evidence and disposition.
- `Test / inspection evidence` — ITR, NDE, pressure-test, and witness/hold-point records.
- `Turnover evidence` — turnover dossier (format TBD).
- `Open-item register` — TBDs and dispositioned deviations carried forward.
- `Acceptance disposition record` — final EPC Integrator sign-off, including any conditions of acceptance.

All records are stored within this deliverable folder or referenced from it.
