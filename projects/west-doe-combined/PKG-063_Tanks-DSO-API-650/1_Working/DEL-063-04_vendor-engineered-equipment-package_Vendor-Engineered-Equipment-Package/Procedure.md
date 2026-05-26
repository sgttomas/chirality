# Procedure — DEL-063-04 Vendor Engineered Equipment Package (Tanks, DSO API 650)

## Purpose

Operational procedure for producing the vendor engineered equipment package for the DSO storage tank TK-6770-1 — from receipt of EPC inputs through vendor-internal acceptance and readiness for turnover (DEL-063-05) and EPC review (DEL-063-06).

## Prerequisites

- Approved EPC Scope of Work (DEL-063-01) for PKG-063 received from EPC Integrator. (`_CONTEXT.md` sibling)
- Approved Package Datasheet (DEL-063-02) received. (`_CONTEXT.md` sibling)
- Access to authoritative references:
  - `_REFERENCES.md` and the Gate-07 PROJECT_DECOMP snapshot.
  - 4-25 Deepcut DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) for service context.
  - 3-25 Comp & Liquids DBM (for shared incinerator/gas-detection context).
  - 26020-Package_Requirements.docx, heading 18 (binary; vendor to confirm slice content — `location TBD`).
- Declared upstream dependencies: none formally declared in `_DEPENDENCIES.md`; treat DEL-063-01 and DEL-063-02 as upstream by package convention. ASSUMPTION pending dependency-extract.
- Vendor quality system meeting API 650 requirements.

## Steps

### Step 1 — Inputs Intake and Gap Review
1. Receive and log the Scope of Work and Package Datasheet.
2. Compile the open-issue list against the available DBM TBCs (specific gravity 1.75 TBC, tank location indoor/outdoor, alternate C5+ disposal path, materials selection). See Guidance Conflict Table.
3. Issue a Request for Information (RFI) to EPC for each open TBC. Records: RFI log.

### Step 2 — Design Basis
1. Develop the vendor design basis from the Package Datasheet and DBM source slices (DBM-Deepcut L528, L1530, L1564, L1570; L1646 for "Modified API 650" question).
2. Confirm governing code edition (API 650 — edition TBD via EPC).
3. Fix design SG (default 1.75 per source; close TBC with EPC).
4. Records: Vendor Design Basis document.

### Step 3 — Mechanical Design Calculations
1. Shell, bottom, roof, anchorage, and seismic/wind calculations to API 650.
2. Nozzle schedule and reinforcement.
3. Heat-loss and heating-system sizing for required minimum DSO temperature (set point — TBD).
4. Blanket gas regulator and relief sizing (API 2000 — `location TBD`).
5. Flame arrestor selection and certification for incinerator-header service.
6. Records: stamped calculation set.

### Step 4 — Materials Selection
1. Select materials compatible with DSO chemistry and operating temperature (selection — TBD; vendor recommendation with EPC ruling).
2. Confirm any cladding/coating in caustic exposure areas (DBM-Deepcut L1566) is or is not applicable to the DSO tank.
3. Records: Materials Selection Report.

### Step 5 — Drawings
1. General arrangement and nozzle orientation.
2. Foundation interface drawing (foundation by EPC unless explicitly in vendor scope — TBD).
3. P&ID-input markup for blanket, vapour, truck-out, and (PROPOSAL) C5+ alternate-disposal connections.
4. Records: vendor drawing register.

### Step 6 — Fabrication
1. Welding Procedure Specifications and Procedure Qualification Records to API 650 / ASME IX.
2. NDE plan (RT/UT/MT/PT) per code and Package Datasheet additions.
3. Surface preparation, painting/coating, insulation per specification.
4. Records: fabrication traveler, NDE reports, coating reports, insulation reports.

### Step 7 — Testing
1. Hydrostatic test per API 650.
2. Leak test of vapour connections after assembly.
3. Functional check of integral instrumentation provided in vendor scope.
4. Records: test reports signed by vendor QA.

### Step 8 — Package Assembly and Pre-Shipment
1. Assemble heater, insulation, blanket regulator, flame arrestor, and integral instrumentation per vendor scope split.
2. Vendor pre-shipment inspection.
3. Records: pre-shipment inspection report; punch list.

### Step 9 — Handoff Readiness for DEL-063-05 / DEL-063-06
1. Compile the vendor document data book (datasheet, calculations, drawings, materials report, fabrication records, NDE, test reports, coatings, insulation, ITP, O&M, spares, as-builts).
2. Transfer to DEL-063-05 (Vendor Document Turnover Package).
3. Support EPC review under DEL-063-06.

## Verification

- API 650 design report complete and stamped.
- Hydrostatic test passed (per Step 7).
- All vendor RFIs answered or carried with EPC-acknowledged dispositions.
- Flame arrestor certified for the as-designed vapour service.
- Heating system meets the EPC-confirmed minimum DSO temperature set point.
- Document data book completeness check against the anticipated artifact list in `_CONTEXT.md`.
- Open `TBD` and `CONFLICT` items from Datasheet/Specification/Guidance are either closed by EPC ruling or carried forward with explicit dispositions.

## Records

- Vendor Design Basis
- Stamped design calculations
- Materials Selection Report
- Vendor drawing set (GA, nozzle, foundation interface, P&ID inputs)
- Fabrication traveler and NDE records
- Coating, insulation, and heating data sheets
- Hydrostatic and leak-test reports
- Inspection and Test Plan and signed records
- Operating and Maintenance manuals
- Spare parts list
- As-built drawings
- RFI log and EPC rulings on TBDs
- Pre-shipment inspection report and punch list
