# Procedure — Construction Work Package (DEL-095-03)

## Purpose

This Procedure defines the field execution and turnover steps for installing one API 650 modified atmospheric slop storage tank (likely TK-9130-2) and its appurtenances at the facility, tying it into the slop process, relief/vent, drain/containment, electrical, cathodic protection, instrumentation, and truck-out systems, and producing the construction interface and turnover checklist for Gate 5 handoff.

## Prerequisites

1. **Upstream deliverable readiness (DECLARED upstreams are currently "None declared"; ASSUMPTION-level dependencies apply):**
   - Civil foundation (ringwall and/or pad) for the slop tank accepted by the relevant civil/earthworks package (ASSUMPTION — civil package linkage TBD; see `_DEPENDENCIES.md`).
   - Package Vendor scope ready (DEL-095-04): tank engineering and design issued for construction; equipment/material delivered to site with vendor data book (Package Vendor scope per PACKAGE_REGISTER PKG-095).
   - Site grading, drainage, secondary containment (dike/liner), and access roads complete enough to permit tank erection, hydrotest, and truck-out access (civil/grading scope).
   - Process engineering has issued IFC P&IDs confirming the slop source list, disposition path, and tank design basis (open per SOW-0216).
   - Tie-in stubs for slop inlet lines, recycle/disposition outlet, truck-out, vent/relief, drain/containment, grounding, CP, lighting, and instrumentation available at correct elevation and orientation.
2. **References available on site:**
   - DELIVERABLE_REGISTER.csv row DEL-095-03, PACKAGE_REGISTER.csv row PKG-095, SCOPE_LEDGER.csv rows SOW-0213..0216, INTERFACE_REGISTER.csv PKG-095 rows (PROJECT_DECOMP GATE-07 snapshot).
   - 26020-Package_Requirements.docx package heading 47 (source slice location TBD).
   - Package Vendor's certified API 650 design package and vendor data book.
   - This deliverable's `Specification.md`, `Guidance.md`, and `Datasheet.md`.
3. **Permits and plans:**
   - Hot work, confined space, and lift permits per site procedures.
   - Lift plan for any large prefabricated tank sub-assemblies (engineered lift if mass/dimensions warrant — TBD).
   - Workface plan integrating piping, electrical, instrumentation, insulation/coating (if any), grounding/CP, and civil interface crews.
   - Hydrotest plan including water sourcing, fill/empty rates, settlement survey points, and post-test disposition.
4. **Tag and identity verification:**
   - Confirm P&ID equipment tag for the slop tank (likely TK-9130-2 per SOW-0215; subject to vendor/process confirmation — HRR per Conflict Table C-095-03-02).
   - Confirm package companion register tag (26020-03-PT-19-004 per PACKAGE_REGISTER) on construction interface checklist.

## Steps

### Phase 1 — Pre-Erection Readiness

1. Confirm foundation acceptance from the civil package: ringwall/pad survey (elevation, level, flatness), anchor bolt template (if applicable), underpad readiness, and grout readiness. Sign foundation acceptance row on the construction interface checklist.
2. Verify dike/secondary containment geometry, liner integrity, and drain routing to the slop-compatible containment drain destination.
3. Verify tank location vs. tank-farm spacing, environmental, and regulatory constraints applicable at the site (TBD per site jurisdiction — see Specification Standards).
4. Receive vendor-supplied tank materials and appurtenances; verify vendor data book completeness, shipping damage inspection, and material traceability (MTRs).

### Phase 2 — Tank Erection

5. Execute tank erection per the Package Vendor's certified API 650 design and the chosen erection method (conventional bottom-up or jacked-roof — vendor/contractor decision; capture in workface plan).
6. Perform welding, weld inspection, and NDE per API 650 and the vendor's QA plan, including:
   - Bottom plate vacuum-box test.
   - Shell course longitudinal and circumferential weld NDE per API 650 (visual + applicable RT/UT/MT/PT as called by vendor design).
   - Roof and roof-to-shell weld NDE.
7. Install tank appurtenances (manways, nozzles, stairway, platform, gauging points, vent, anchor straps if any) per vendor design.
8. Capture weld map and NDE reports.

### Phase 3 — Process and Utility Tie-Ins

9. Complete tie-ins of slop inlet lines from the slop sources defined by process engineering (off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, treating-unit drains, and other contaminated hydrocarbon liquids per IFC P&IDs).
10. Complete tie-ins of tank recycle/disposition outlet and truck-out connection(s).
11. Complete tie-ins of vent / pressure-vacuum relief per Relief / Flare / Vent interface (routing per IFC P&IDs — atmospheric vent vs. flare/vent routing TBD per process).
12. Complete tie-ins of drain/containment piping to the slop-compatible facility drain system.
13. Pressure-test newly fabricated field tie-in piping per applicable code and project test plan.
14. Perform PMI/MTR verification on a documented sample of installed field-piping materials.

### Phase 4 — Electrical, CP, Lighting, and Instrumentation

15. Install grounding/bonding for the tank, appurtenances, and truck-out hookup; perform continuity test and capture record.
16. Install and commission the cathodic protection system per vendor specification; capture commissioning record.
17. Install area/exterior lighting per electrical design; commission and record.
18. Install I&C / control cabling and the standard tank instrumentation set (level, temperature, pressure as applicable, overfill protection per process design); perform loop checks; capture loop check sheets and overfill protection functional test.

### Phase 5 — Hydrotest and Settlement Survey

19. Perform pre-hydrotest settlement survey at vendor-designated reference points.
20. Fill the tank with hydrotest water per the vendor and project hydrotest plan; hold at test condition for the specified duration; inspect for leaks; capture hydrotest record.
21. Perform during-fill and post-test settlement surveys; verify settlement is within vendor acceptance criteria.
22. Drain and dispose of hydrotest water per the hydrotest plan and environmental requirements; capture disposal record.

### Phase 6 — Lining/Coating (conditional) and Final Readiness

23. If the vendor design specifies an interior lining or coating for slop service, apply per the vendor's sequencing relative to hydrotest (pre- or post-test as specified); capture application and cure records. If no lining is specified, mark this step N/A on the checklist.
24. Complete external coating/insulation per vendor design (if applicable).

### Phase 7 — Inspection, Punch List, and Turnover

25. Walkdown installation against certified P&IDs and isometrics with the EPC Integrator, Package Vendor representative, and operations representative. Generate punch list.
26. Resolve A-priority punch items before mechanical completion; track B/C items into commissioning.
27. Compile the **construction interface and turnover checklist** with signed rows for the nine PKG-095 interface types (Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports), plus foundation acceptance, tank erection, weld/NDE, hydrotest, settlement, CP commissioning, lighting commissioning, lining/coating (if applicable), and overfill protection functional test.
28. Hand over the completed turnover package (vendor data book + construction records) to the EPC Integrator for Gate 5 / pre-commissioning.

## Verification

| Step | Verification |
|---|---|
| 1 | Signed foundation acceptance row; survey within tolerance. |
| 2 | Dike geometry / liner integrity inspection; drain routing flow check. |
| 3 | Documented spacing / regulatory location check (TBD per jurisdiction). |
| 4 | Vendor data book completeness; MTR file. |
| 5-8 | Weld map; NDE reports (vacuum-box, shell, roof); appurtenance install sign-off. |
| 9-12 | Pressure test certificates; weld map closeout for tie-ins; walkdown vs. P&IDs. |
| 13-14 | Pressure test record; PMI/MTR sample record. |
| 15 | Grounding continuity test record. |
| 16 | CP commissioning record. |
| 17 | Lighting commissioning record. |
| 18 | Instrument loop check sheets; overfill protection functional test record. |
| 19-22 | Settlement survey records (pre/during/post); hydrotest record; hydrotest water disposal record. |
| 23-24 | Lining/coating application and cure record (if applicable); external coating/insulation record. |
| 25-26 | Signed walkdown sheets and punch list. |
| 27-28 | Completed and signed construction interface and turnover checklist; turnover package transmittal. |

## Records

- Vendor data book (API 650 slop tank).
- Foundation acceptance form (ringwall/pad survey, anchor bolt template if applicable).
- Dike / secondary containment inspection record.
- Site spacing / regulatory location record (TBD per jurisdiction).
- Material traceability (MTRs) file.
- Weld map and NDE reports (bottom vacuum-box, shell, roof).
- Appurtenance install sign-offs.
- Tie-in pressure test certificates; PMI/MTR sample record.
- Grounding/bonding continuity test record.
- Cathodic protection commissioning record.
- Area/exterior lighting commissioning record.
- Instrument loop check sheets; overfill protection functional test record.
- Pre/during/post hydrotest settlement survey records.
- Hydrotest record; hydrotest water sourcing and disposal record.
- Interior lining/coating application and cure record (if applicable).
- External coating/insulation record (if applicable).
- Walkdown sheets and punch list (with closure evidence).
- Construction interface and turnover checklist (signed; nine PKG-095 interfaces + tank-specific items).
- As-built redlines.
- Transmittal of the turnover package to EPC Integrator / Gate 5 reviewer.
