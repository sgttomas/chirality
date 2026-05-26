# Procedure — DEL-063-03 Construction Work Package (Tanks, DSO (API 650))

> Operational procedure for producing the CWP deliverable bundle AND for executing CWP-governed site work for `PKG-063 Tanks, DSO (API 650)`. Source-anchored to `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. Detailed site sequencing (durations, crew sizes, lift/erection plans, hydrotest water source) is `TBD` until the project execution plan, the vendor/EPC tank datasheet, and the heading-18 slice of `_Sources/26020-Package_Requirements.docx` are accessible.

## Purpose

To assemble, issue, and execute the Construction Work Package for the DSO (disulphide oil) tank package (API 650) so that the installed tank and its tie-ins are mechanically complete, hydrostatically tested per API 650, registered (as applicable), instrumented, F&G-protected, and accepted for handover to commissioning, with traceable records back to `SOW-0209`–`SOW-0212`.

## Prerequisites

### Decomposition / Governance

- Accepted upstream decomposition snapshot `GATE-07_Final_Published_2026-05-24` (cited in `_REFERENCES.md`).
- `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md` for this deliverable.

### Source Materials (Accessible)

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (caustic mercaptan treating + DSO service slice; tank winterization basis; F&G governance; drain headers).

### Source Materials (Cited but Inaccessible — TBD)

- `_Sources/26020-Package_Requirements.docx` heading 18 (PKG-063 package-requirements slice — not transcribed into `_REFERENCES.md`).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 90 (PKG-063 interface row — not transcribed).

### Upstream Deliverables in PKG-063 (ASSUMPTION on numbering pattern from sibling packages)

- `DEL-063-01_scope-of-work` — package scope of work (ASSUMPTION: precedes CWP issue).
- `DEL-063-02_package-datasheet` — package technical datasheet (ASSUMPTION: precedes CWP issue).
- `DEL-063-04_vendor-engineered-equipment-package` — vendor tank engineering/delivery (precedes site erection and tie-in) (ASSUMPTION).
- `DEL-063-05_vendor-document-turnover-package` — vendor document set (drives much of the CWP content) (ASSUMPTION).

### Required Vendor / EPC Inputs Before Site Work

- DSO tank datasheet (capacity, dimensions, plate basis, anchorage, internal coating, insulation, EHT, instrumentation list).
- Foundation drawings and anchor-bolt embedment drawings (depends on geotechnical report per DBM line 700).
- Tank erection plan (field-erected): plate handling, shell jacking, weld map, weld procedures.
- Internal coating specification for DSO service (TBD — see Guidance Conflict C-3).
- Piping tie-in list, isometrics, fabrication isometrics, MTO for DSO inlet/transfer/drain/vent/blanket lines.
- Electrical installation set (cable schedule, routing, terminations, energization package).
- Instrumentation set (location plans, hook-up drawings, loop diagrams, wiring/termination, junction boxes, cable schedule, I/O list).
- F&G detector layout (TBD pending detailed design per DBM line 838).
- ITP and inspection-release certificate.

### Project Inputs (currently `TBD`)

- Project hydrotest / NDE specification.
- Project welding specification.
- Project mechanical completion / turnover procedure.
- Pressure equipment registration jurisdictional procedure (if applicable to DSO scope).
- Site HSE / hot-work / confined-space / lift-plan permit procedures.
- Final geotechnical report (DBM line 700 dependency for foundation closure).
- Hydrotest water source and disposal plan.
- DSO internal coating specification.

## Steps

### Phase A — Assemble the CWP Document Bundle (EPC Integrator office work)

A1. **Confirm scope demarcation.** Extract heading 18 from `_Sources/26020-Package_Requirements.docx` for PKG-063 and capture any "By others" / EPC Integrator workface items verbatim. Until that extraction is done, demarcation entries in `Datasheet.md` and `Specification.md` are `ASSUMPTION` (see Guidance Conflict C-1).

A2. **Build the SOW-trace matrix.** Map every CWP work item to `SOW-0209`, `SOW-0210`, `SOW-0211`, `SOW-0212`.

A3. **Build the interface plan** from `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 90, instantiating one workface package per "Yes" interface. Until row 90 is transcribed, the interface plan is `ASSUMPTION` (see Guidance Conflict C-2).

A4. **Sequence on a CPM basis** (durations TBD). Default sequencing ASSUMPTION: Geotechnical review → Foundation (ringwall/pile/slab) → Plate/Material Receipt → Field Erection (bottom → shell → roof) → Internal Coating (if site-applied) → External Insulation & EHT → Tie-In Piping → Electrical & Instrumentation Termination → F&G Installation → Hydrostatic Test (API 650) → Piping Hydrotest & Flush/Dry → Energization → Loop Checks → SAT → Mechanical Completion → Turnover.

A5. **Define record templates** for each verification item in `Specification.md` `R-CWP-16` through `R-CWP-20`, including the API 650 hydrostatic test settlement-survey record.

A6. **Issue the Construction work package, Installation and tie-in workface plan, and Construction interface and turnover checklist** as the three CWP artifacts named in `_CONTEXT.md`.

### Phase B — Site Execution

B1. **Receiving & QA-in.** Witness the inspection release certificate; perform receiving inspection on vendor-supplied tank materials (plates, internals, ladders, manways, nozzles) and on vendor-supplied piping/electrical/instrumentation items. Record any transit damage.

B2. **Foundation acceptance.** Construct foundation per the geotechnical-report-based design (ringwall/pile/slab — TBD); survey ringwall flatness or pile cut-off elevations and anchor-bolt template; release foundation for erection.

B3. **Field erection (API 650).** Set bottom plates; weld bottom seams (with vacuum-box leak test); erect shell courses (jacking or course-by-course) with WPS-qualified welders; radiograph shell seams per API 650; install roof; install internals (manways, nozzles, weirs/baffles if any); record alignment and roundness.

B4. **Internal coating (if site-applied).** Surface preparation per coating manufacturer; coating application (TBD product per Guidance Conflict C-3); DFT measurement; holiday test.

B5. **External insulation and EHT.** Install insulation and electric heat tracing on tank shell and freeze-prone piping per the −40 °C site basis (DBM line 145); commission EHT circuits.

B6. **Tie-in piping.** Execute weld map for DSO inlet, DSO transfer (to DSO pumps 2 × 100 % — DBM line 577), drain (300# ANSI minimum per DBM line 493), vent/blanket (disposition TBD per Guidance Conflict C-5), and instrument taps; perform NDE per project welding spec (TBD); install valves; close tie-ins.

B7. **Flush, dry, and pressure-test (piping).** Execute flushing/cleaning/drying for tie-in piping; execute piping hydrotest packs per project pressure-test specification (TBD).

B8. **API 650 hydrostatic test (tank).** Fill the tank with water per API 650 Section 7; perform settlement survey at prescribed fill levels; inspect for leaks (bottom-to-shell, shell seams, nozzles); drain and dispose of test water per project plan (TBD); document settlement survey and acceptance.

B9. **Electrical installation and energization.** Pull cable; terminate; perform megger/continuity; complete the energization package; coordinate any starter/MCC configuration for tank-side loads (mixer if any — TBD; instrumentation; EHT; lighting).

B10. **Instrumentation install and loop check.** Install level (incl. high/high-high alarms), temperature, pressure (if applicable), and analytical instruments; terminate; run loops back to the facility control system; verify against the cause-and-effect matrix.

B11. **Fire & gas functional test.** Install F&G devices (LEL, H2S, methyl mercaptan, fire — per DBM line 838 governance area for tankage and DSO systems); functional-test per project F&G procedure (TBD).

B12. **Pressure equipment registration (if applicable).** Submit registration package per jurisdictional procedure (TBD); obtain acceptance prior to pressurization of any registered pressurized piping/equipment.

B13. **Spill containment and drainage finish.** Verify bund/dyke construction; verify drain interceptors and routing; verify containment volume (ASSUMPTION: 110 % of largest tank within the bund, per common code practice).

B14. **SAT.** Execute site portions of any vendor FAT scope re-verified at site, plus instrumentation and F&G SAT.

B15. **Mechanical completion.** Walk down against the Construction interface and turnover checklist; clear punch list (or carry forward with disposition); issue MC certificate (template TBD).

B16. **Turnover to commissioning.** Hand over the turnover dossier: MC certificate; ITP closure; inspection releases; weld map and NDE reports; bottom vacuum-box record; API 650 hydrostatic test record with settlement survey; piping hydrotest packs; coating DFT/holiday records; insulation/EHT records; electrical test records; loop check sheets; F&G functional records; spares received register; IOM; as-built drawings (tank, piping, electrical, instrumentation).

## Verification

| Step | Verification |
|---|---|
| A1–A6 | CWP bundle issued (three artifacts named in `_CONTEXT.md` present); SOW-trace matrix reviewed; interface plan source row referenced |
| B1 | Inspection Release Certificate on file; receiving inspection record signed |
| B2 | Foundation as-built; ringwall flatness or pile cut-off survey; anchor-bolt template survey |
| B3 | Plate MTRs; WPS/WPQ records; weld map; radiograph reports; bottom vacuum-box record; roundness/plumb survey |
| B4 | Surface-prep blast profile; DFT measurements; holiday-test record |
| B5 | Insulation inspection; EHT continuity and circuit test record |
| B6 | Tie-in punch-list closure; weld map closure; NDE acceptance reports on tie-in piping |
| B7 | Flush certification; piping hydrotest charts/sign-offs filed |
| B8 | API 650 hydrostatic test record with settlement survey; leak inspection record; test-water disposal record |
| B9 | Megger, continuity; energization checklist closed |
| B10 | Loop check sheets reconciled to instrument loop diagrams and cause-and-effect matrix |
| B11 | F&G device functional test records filed |
| B12 | Pressure equipment registration acceptance evidence on file (if applicable) |
| B13 | Bund volume verification; drain functional test |
| B14 | SAT closure report filed |
| B15 | MC certificate issued with punch-list dispositioned |
| B16 | Turnover dossier accepted by commissioning lead |

## Records

The CWP must produce, collect, or route the following records at close-out (origin in parentheses):

- Construction work package (this deliverable bundle).
- Installation and tie-in workface plan (this deliverable bundle).
- Construction interface and turnover checklist (this deliverable bundle).
- Inspection Release Certificate (vendor).
- Material Test Reports / Certificates for tank plates and tie-in piping (vendor / mill).
- Manufacturing Record Book / Vendor Data Book (vendor).
- Foundation as-built records (site).
- Plate handling and erection records (site).
- Weld map and NDE reports (site).
- Bottom vacuum-box leak test record (site).
- API 650 hydrostatic test record with settlement survey (site).
- Piping hydrotest packs and flushing/drying records (site).
- Surface preparation, coating DFT, and holiday-test records (site).
- Insulation installation and EHT commissioning records (site).
- Electrical test records and energization package (site).
- Loop check sheets (site, against instrument loop diagrams and cause-and-effect matrix).
- F&G functional test records (site).
- Pressure equipment registration acceptance (jurisdiction, if applicable).
- Bund volume verification and drain functional test records (site).
- SAT records (site / vendor).
- Mechanical completion certificate (project MC procedure — TBD).
- Punch list and dispositions.
- Spares received register; IOM.
- As-built drawings: tank, piping, electrical, instrumentation.
