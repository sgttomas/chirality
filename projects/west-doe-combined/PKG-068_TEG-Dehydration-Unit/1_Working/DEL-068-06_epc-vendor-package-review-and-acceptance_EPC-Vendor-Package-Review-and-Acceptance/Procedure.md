# Procedure — DEL-068-06 EPC Vendor Package Review and Acceptance (TEG Dehydration Unit)

**Interpretation:** This procedure describes how the EPC Integrator **produces** the vendor-package review-and-acceptance evidence pack for the TEG Dehydration Unit package (`PKG-068`). It is not a procedure to operate the TEG unit.

## Prerequisites

- Accepted upstream snapshot available: `GATE-07_Final_Published_2026-05-24` (`_DEPENDENCIES.md`).
- Source slices accessible:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-05 ("TEG Dehydration Basis", "TEG Package Equipment"), "Utility Integration Basis", "Control System Architecture";
  - `_Sources/26020-Package_Requirements.docx` heading 23 — "TEG Dehydration Unit" (binary; sub-list extraction is itself a prerequisite — see Step 0);
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 97 (binary; column-level extraction is also a prerequisite — see Step 0).
- EPC anchor deliverables drafted or available for cross-reference: `DEL-068-01` (Scope of Work), `DEL-068-02` (Package Datasheet), `DEL-068-03` (Construction Work Package).
- Vendor production-unit deliverables available for review: `DEL-068-04` (Vendor Engineered Equipment Package), `DEL-068-05` (Vendor Document Turnover Package). (`_DEPENDENCIES.md` declares no formal upstream edges as of PREPARATION — ASSUMPTION that these are the de facto upstreams via package decomposition.)
- Reviewer assignments and access to the Vendor Document Index established.

## Steps

0. **Extract binary source slices.** Before substantive acceptance work, extract:
   - `26020-Package_Requirements.docx` heading 23 "Vendor Engineering Deliverables", "Basic Scope", "Major Included Equipment", "Scope Notes / Open Items", and "Physical Interface Summary" into a markdown slice under `_Sources/` (or capture in `_REFERENCES.md` for this deliverable);
   - `26020-Packages_Interfaces_4_export.xlsx` Packages row 97 per-interface columns into a markdown slice or CSV under `_Sources/`.
   Without these slices, requirements `R-068-06-02`, `R-068-06-06`, `R-068-06-07`, `R-068-06-09`, `R-068-06-10`, and `R-068-06-12` cannot be fully traced. (Closes Conflict-Table items `C-068-06-01` and `C-068-06-02`.)
1. **Establish the acceptance register.** Create the vendor document review log seeded from the heading 23 "Vendor Engineering Deliverables" enumeration extracted in Step 0. Every listed deliverable becomes one row with disposition fields (`SUBMITTED`, `ACCEPTED`, `REJECTED`, `OPEN`). (Verifies `R-068-06-02`.)
2. **Map SOW coverage.** Build a traceability matrix linking `SOW-0237`, `SOW-0238`, `SOW-0239`, `SOW-0240` to the acceptance-checklist rows and to evidence artifacts. (Verifies `R-068-06-01`.)
3. **Walk the package equipment scope.** Confirm that the vendor package supplies every item in SEC-05 "TEG Package Equipment": inlet filter coalescer, contactor, level pot, lean TEG cooler, flash drum, full-flow rich-TEG solids filters, charcoal filter, lean/rich exchanger, rich-TEG solids filter, TEG pumps (2 x 100 percent), still column, stripping column, reflux condenser, reboiler, surge drum, regen cooler, regen overhead scrubber, regen overhead pumps, makeup tank, and makeup pump. Reconcile to the vendor equipment list and GA drawings. (Verifies `R-068-06-03`.)
4. **Review process tie-ins.** Inspect P&IDs and tie-in lists to confirm: inlet from second-stage compressor discharge at 800 psig (SCA-002 basis); treated-gas export to 04-25 inlet gathering; flash-gas pressure-regulated to 04-25 SOC first-stage suction; contactor blowdown automated to HP flare; regen overhead to LP flare via LP KO drum `V-3900-2`. Cross-reference HP flare package (`PKG-054`) and the LP flare KO drum package for interface acceptance. (Verifies `R-068-06-04`.)
5. **Review utility tie-ins.** Confirm LP fuel-gas supply to TEG stripping (reboiler / stripping column), instrument air, electrical power, and heat-tracing / insulation where applicable. Inspect commissioning records for heat-trace energization and fuel-gas pressure regulation. (Verifies `R-068-06-05`.)
6. **Execute interface-by-interface acceptance.** For each interface flag from the extracted Packages row 97 slice, complete an interface acceptance checklist row referencing the relevant vendor artifact(s) and the corresponding EPC interface owner. (Verifies `R-068-06-06`.)
7. **Vessel acceptance.** Review pressure-vessel data sheets, mechanical calc packages, hydrotest packages, and Pressure Equipment Registration Package for coded vessels (contactor, flash drum, surge drum, regen overhead scrubber, and any other coded shells). Confirm jurisdictional registration acceptance (authority TBD — ASSUMPTION). (Verifies `R-068-06-07`.)
8. **Rotating-equipment acceptance.** Review pump data sheets, NPSH calculations, mechanical seal / lube oil specs, motor starting study, and FAT reports for TEG pumps, regen overhead pumps, and makeup pump. Confirm 2 x 100 percent configuration and single mechanical seal compliance for the TEG pumps. (Verifies `R-068-06-08`.)
9. **Quality records audit.** Assemble Supplier Quality Plan, ITP execution evidence, MTRs, Inspection Release Certificate, and Manufacturing Record Book / Vendor Data Book. (Verifies `R-068-06-09`.)
10. **Turnover readiness.** Confirm SPIR, Logistics / Shipping Plan, and Mechanical Equipment IOM Manual are present and accepted. Hand off the Construction Work Package interface to `DEL-068-03`. (Verifies `R-068-06-10`.)
11. **Numeric reconciliation.** Build a reconciliation table between SEC-05 design values (and `DEL-068-02` Package Datasheet) and vendor-submitted values: gas flow (82.5 MMSCFD normal/design); inlet pressures (4,502 / 5,378 / 4,502 / 6,205 kPag low/normal/design/maximum); expected inlet temperature (110 deg F); outlet water (4 lb H2O/MMSCF); contactor turndown (3:1 TBC); regeneration turndown (2:1); surge drum 30 min retention at 50 psig; contactor at least three theoretical stages with Fs not more than 3.0 and inlet/outlet demisters; rich-TEG 5 micron full-flow filtration plus 20 percent carbon/particle slipstream. Flag variances. (Verifies `R-068-06-11`.)
12. **Control-system integration acceptance.** Review the package PLC / Unit Control System integration with the BPCS: replicated values, alarm priorities, trip interfaces, protocol (Modbus / Kepware KepserverEX where applicable), final package data maps, permissive logic. (Verifies `R-068-06-13`.)
13. **Makeup-tank and flash-drum walk-down.** Confirm makeup tank is atmospheric, fuel-gas blanketed, heated/insulated, and NOT connected to VRU; confirm flash-drum hydrocarbon-liquid manual drain to produced-water drain. (Verifies `R-068-06-14`.)
14. **Produced-water-interface awareness note.** Record in the acceptance pack that TEG is among the produced-water contaminants identified in the current source set, and cross-reference the produced-water package interface. No re-engineering performed here. (Verifies `R-068-06-15`.)
15. **Open-items disposition.** Close or explicitly carry every item from the extracted heading 23 "Scope Notes / Open Items" slice and from any reviewer-raised open items. (Verifies `R-068-06-12`.)
16. **Issue the acceptance package.** Compile the acceptance artifacts (vendor document review log; package acceptance checklist; test/inspection evidence bundle; turnover evidence bundle; open-items disposition log), apply EPC Integrator sign-off, and route for human approval per project governance. (No agent may certify acceptance; this step is human-decided per `K-AUTH-1`.)

## Verification

- Binary source slices (heading 23; Packages row 97) extracted and recorded under `_Sources/` (or referenced from `_REFERENCES.md`) before acceptance closure.
- Every heading 23 "Vendor Engineering Deliverable" row appears in the vendor document review log with a disposition.
- Every interface flag from Packages row 97 has an acceptance-checklist row with linked evidence.
- Every requirement `R-068-06-01` through `R-068-06-15` (Specification.md) is linked to at least one verification record.
- All numeric design values in the acceptance pack are either reconciled to a vendor submittal or carried as `TBD` with a named owner.
- Open items from the source's "Scope Notes / Open Items" are closed or carried with explicit disposition.
- Makeup-tank VRU exclusion explicitly confirmed at walk-down.

## Records

- Extracted source-slice markdown / CSV files under `_Sources/` (heading 23 slice; Packages row 97 slice).
- Vendor document review log (live register; archived at acceptance).
- Package acceptance checklist (SOW-, interface-, equipment-, and artifact-indexed; signed).
- Test / inspection evidence bundle (FAT records, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages, registration package, SPIR, IOM).
- Open-items disposition log.
- Numeric reconciliation table (SEC-05 / `DEL-068-02` vs. vendor submittals).
- Package-PLC / BPCS integration test records.
- EPC Integrator acceptance sign-off (human-authored; required for binding acceptance — `K-AUTH-1`).
