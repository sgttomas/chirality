# Procedure — DEL-096-04 Vendor Engineered Equipment Package (Tanks, Sour Condensate, API 650)

> Operational deliverable. Describes the steps to **produce** the Vendor Engineered Equipment Package — the vendor design basis and datasheet set plus the physical equipment package — anchored by DEL-096-01 (SOW) and DEL-096-02 (Package Datasheet), and to confirm readiness for EPC integration review (DEL-096-06) and turnover (DEL-096-05).

## Purpose

Produce a sour condensate atmospheric storage tank package (engineering, design, fabrication/supply) and its accompanying vendor design basis and datasheet set, such that the EPC Integrator can install (DEL-096-03), accept (DEL-096-06), and document turnover (DEL-096-05) without further interpretation.

## Prerequisites

- **Anchoring EPC inputs accessible**: DEL-096-01 Scope of Work (ISSUED) and DEL-096-02 Package Datasheet (ISSUED). _Currently OPEN/INITIALIZED at this writing; vendor engagement should follow ISSUE of these anchors. ASSUMPTION._
- **DBM slices accessible**: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-01, SEC-02, SEC-06).
- **Project package-requirements source**: `26020-Package_Requirements.docx` heading 48 — currently `TBD (not locally accessible)`. See Guidance CT-05.
- **Final tank register**: required before fabrication release; current basis is preliminary per DBM line 406. See Guidance CT-03.
- **Final geotechnical report**: required before foundation load deliverable is finalized (DBM SEC-02 preliminary).
- **Governing code text accessible to the vendor**: API 650 (and NACE MR0175 / ISO 15156 per CT-04).
- **Vendor selected** by EPC Integrator (responsibility per `_CONTEXT.md`).
- **VRU header tie-in pressure and design data** available from EPC for vapour-space coordination (R-16).

## Steps

### Pass A — Vendor Engineering Initiation
1. Vendor reviews DEL-096-01 (SOW) and DEL-096-02 (Package Datasheet); logs clarifications/deviations against EPC Integrator.
2. Vendor reviews DBM slices in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` for site, ambient, civil, vapour-recovery, and condensate basis (SEC-01, SEC-02, SEC-06).
3. Vendor reviews this deliverable's Guidance Conflict Table; obtains human rulings on HRR items (CT-01..CT-06) before locking design.
4. Vendor confirms code basis (API 650; see CT-01) and sour-service standard (NACE; see CT-04).

### Pass B — Vendor Design Basis and Datasheet Set
5. Vendor issues **Vendor Design Basis** document citing DEL-096-01/02 and DBM slices; lists deviations; closes HRR items with EPC rulings.
6. Vendor issues **Process Datasheet** per tank service (sour inlet vs. sour storage).
7. Vendor issues **Mechanical/Strength Datasheet** per tank, including design code citation (API 650 + modifications per CT-01).
8. Vendor issues **Materials Selection Diagram** and supporting MTR list (sour-service per R-8, CT-04).
9. Vendor issues **Coating System Specification** (internal coating selection per R-9 / CT-02; external coating per site basis).
10. Vendor issues **Nozzle Schedule** and **GA Drawings** (preserving tank service flexibility per R-18).
11. Vendor issues **Foundation Load Drawings** (dead, live, wind, snow, seismic per R-11, hydrotest, settlement criteria per R-12) for EPC civil design.
12. Vendor issues **Weld Map** and **NDE/ITP Plan** aligned with API 650 (R-15).
13. Vendor issues **PVRV Sizing Calculation** coordinated with EPC VRU header data (R-16).
14. Vendor issues **Vendor P&IDs** (vendor portion of tank skid) showing tank-mounted instrumentation and terminal points to EPC scope.
15. EPC Integrator review cycle on vendor documents; vendor dispositions comments and re-issues.

### Pass C — Fabrication / Supply
16. Vendor releases fabrication only after (a) final tank register confirmation (R-13, CT-03), (b) EPC-accepted vendor design basis, and (c) all HRR items closed.
17. Vendor procures plate, structurals, coating system, instrumentation per accepted MSD; retains MTRs.
18. Vendor executes shop fabrication of tank components (rings/plates/roof panels/structural items) per accepted weld map; performs in-shop NDE.
19. Vendor executes internal coating per accepted coating system on shop-built components where applicable.
20. Vendor ships components to site per shop/field-erection split (proposed under CT-06).
21. Vendor executes field tank erection per accepted GA drawings (field welding, completion of bottoms/roofs, installation of appurtenances).
22. Vendor executes API 650 hydrostatic test, bottom weld vacuum-box test, NDE on field welds, and coating holiday inspection (R-15).
23. Vendor installs tank-mounted instrumentation, PVRVs, manways, stairs/platforms, grounding lugs, nameplate.

### Pass D — Handover to EPC
24. Vendor compiles ITP records, test reports, MTRs, NDE reports, coating reports, hydrotest record, and as-built marked drawings.
25. Vendor transmits the vendor design basis and datasheet set (final issued) to the EPC Integrator.
26. Vendor supports DEL-096-06 EPC vendor package review and acceptance.
27. Vendor supplies inputs to DEL-096-05 Vendor Document Turnover Package (the vendor document register is governed there, not in this deliverable per R-19).
28. EPC Integrator accepts the package or returns deviations; vendor closes deviations and re-issues.

## Verification

| Step / Requirement | Verification Check |
|---|---|
| Steps 1–4 (initiation) | Clarification/deviation log filed; HRR ruling records attached to vendor design basis |
| Step 5 (design basis) | Document review against DEL-096-01/02 traceability matrix (R-1) |
| Steps 6–14 (datasheet set) | EPC discipline review check (process, mechanical, materials, coatings, civil, controls); all R-14 enumerated documents present |
| Step 13 (PVRV) | Sizing calculation reconciled with EPC VRU header design (R-16) |
| Step 15 (EPC review) | Comment-disposition log closed; vendor re-issues stamped |
| Step 16 (release) | Final tank register confirmation logged (R-13, CT-03); HRR closure recorded |
| Steps 17–19 (procurement / shop) | MTR audit; in-shop NDE records; coating QA report |
| Steps 21–23 (field erection / test) | Hydrotest report; vacuum-box record; field NDE report; coating holiday report (R-15) |
| Step 24 (handover compile) | Document index check against R-14 enumerated set + ITP records |
| Step 26 (DEL-096-06) | EPC Integrator acceptance record (separate deliverable, referenced) |
| Step 27 (DEL-096-05) | Vendor document register completeness (separate deliverable, referenced) |

## Records

The following records shall result from execution of this procedure and shall be retained by the Package Vendor and transmitted to the EPC Integrator:

- Vendor Design Basis (final, dated, signed).
- Process Datasheet, Mechanical Datasheet, MSD, Nozzle Schedule, GA Drawings, Foundation Load Drawings, Weld Map, NDE/ITP Plan, PVRV Sizing Calculation, Coating System Specification, Vendor P&IDs (all as-issued and as-built where applicable).
- Comment-disposition logs from EPC Integrator review cycles.
- HRR ruling closure records (CT-01..CT-06).
- MTR file (all heat numbers traced to component locations).
- Shop and field NDE reports.
- Hydrostatic test report; bottom weld vacuum-box test report.
- Internal/external coating QA and holiday test reports.
- Tank nameplate detail and as-installed nameplate photograph.
- As-built marked drawings (transferred to DEL-096-05 for turnover compilation).
- Vendor deviation register (closed at acceptance).
