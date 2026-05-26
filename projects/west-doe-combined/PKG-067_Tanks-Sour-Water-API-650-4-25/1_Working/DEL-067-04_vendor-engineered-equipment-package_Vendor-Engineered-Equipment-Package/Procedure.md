# Procedure — DEL-067-04 Vendor Engineered Equipment Package (Tanks, Sour Water — API 650, 4-25)

This procedure covers how to **produce** the vendor engineered equipment package deliverable (engineering, design, fabrication/supply of the two produced-water storage tanks `TK-9010-1` and `TK-9020-1`). Operations of the installed tanks are covered separately by site operating procedures.

## Prerequisites

- **Inputs accepted from EPC Integrator:**
  - DEL-067-01 EPC Scope of Work (PKG-067) at INITIALIZED or later. (DELIVERABLE_REGISTER.csv row 528.)
  - DEL-067-02 EPC Package Datasheet (PKG-067) at INITIALIZED or later. (DELIVERABLE_REGISTER.csv row 529.)
- **Source basis available to vendor:**
  - DBM §"Waste Streams and Disposition — Produced Water" (design basis).
  - DBM §"Product Storage and Distribution Summary" (tank count, capacity, residence time).
  - DBM §"Package Line-Item Requirements" row 99 (tag identification).
  - DBM §2.5 "Atmospheric Tank and General Plant Spacing" (siting constraints).
- **Standards available to vendor:** API 650, API 2000, NFPA 30, API 2510, OGAOM (location TBD locally).
- **Declared dependencies:** `_DEPENDENCIES.md` declares none; treat DEL-067-01 / DEL-067-02 as logical upstreams. *ASSUMPTION pending formal declaration.*

## Steps

### Step 1 — Confirm package boundary and tag scope
1.1 Reconcile vendor scope to **2 x produced-water storage tanks (TK-9010-1, TK-9020-1)** per DBM row 99. (DBM Package Line-Item Requirements.)
1.2 Document EPC-owned interfaces (process piping, relief/flare/vent, drain/containment, grounding/bonding, area/exterior lighting, cathodic protection, I&C/control cabling, grading/site drainage/spill containment, structural/foundations/supports). (PACKAGE_REGISTER.csv row 94.)
1.3 Record the package battery limit on the vendor GA drawing.

### Step 2 — Close design conditions
2.1 Confirm tank design SG with EPC Integrator; baseline 1.25 (TBC). (DBM §"Produced Water" prose.)
2.2 Confirm composition envelope (DBM trace list is not comprehensive). (DBM §"Produced Water" prose.) If list stays open at fabrication release, mark as `TBD` in design package and record in MEMORY.
2.3 Confirm flow envelope: summer 1,684 kg/h / 39.9 Am³/d; normal and design **TBC**. (DBM §"Produced Water" table.)

### Step 3 — Tank engineering per API 650 (modified)
3.1 Size each tank to **2,000 bbl nominal**, maximum operating fill **90%**, test pressure **16 oz**. (DBM §"Produced Water" table.)
3.2 Perform thermal expansion check for the 90% fill limit. (DBM §"Produced Water" table.)
3.3 Material selection SHALL account for trace H2S / mercaptan / amine / caustic exposure (sour-service isolation TBD; design for credible sour vapour). (DBM §"Produced Water" prose; §"Assumptions and Unresolved Requirements".)
3.4 Issue tank shell, roof, floor, and nozzle drawings per API 650.

### Step 4 — Coatings, insulation, heating
4.1 Specify **Devchem 253** internal coating on floor, walls, and roof (or vendor-proposed equivalent submitted with qualification data for EPC acceptance). (DBM §"Produced Water" prose.)
4.2 Specify external insulation system (type/thickness TBD by vendor heat-loss calculation).
4.3 Size tank heating for the design produced-water rate and winter ambient (heater type selection: TBD by vendor with EPC review).

### Step 5 — Internals
5.1 Provide a **Kennilworth-type hydrocarbon skim float system** in each tank. (DBM §"Produced Water" prose.)
5.2 Document skim outlet routing to EPC Integrator at battery limit.

### Step 6 — Vent and relief
6.1 Size **PVRV(s)** per **API 2000** for blanket-gas vacuum prevention and normal in-/out-breathing. (DBM §"Produced Water" prose and table.) Provide at least one PVRV per tank.
6.2 Document **EPRV** sizing or carry it as a TBD requiring closure before commissioning. (DBM §"Produced Water" prose.)
6.3 Coordinate tank **isolation philosophy** with HAZOP and EPC Integrator given potential sour vapours. (DBM §"Produced Water" prose; §"Assumptions and Unresolved Requirements".)

### Step 7 — Connections
7.1 Provide nozzles for inlet, outlet (to the 2 x 100% produced water transfer pumps), level, temperature, pressure, drain, manway, vent, and PVRV. (DBM §"Produced Water" table — pump scope; nozzle list otherwise TBD by vendor.)
7.2 Provide **common envirobox truck-out connection** sized for **2.75 m³/min** vacuum-truck pump-out (TBC) and the **55 m³ in 20 min** B-train basis. (DBM §"Produced Water" table.)

### Step 8 — Siting / interface checks
8.1 Confirm the package footprint allows EPC Integrator to honour DBM §2.5 spacing (atmospheric-tank-to-tank ≥ 2.35 m; to public road ≥ 80 m; to pressurized bullets ≥ 30.48 m; etc.). (DBM §2.5.)

### Step 9 — Fabrication and inspection
9.1 Fabricate the tanks under API 650 quality program.
9.2 Witness/document the hydrostatic test (16 oz test pressure) and required NDE per API 650.
9.3 Apply internal coating per the qualified coating MPS; record DFT and cure logs.
9.4 Install insulation and heating; record commissioning checks.

### Step 10 — Vendor package handover
10.1 Compile the vendor package design basis and datasheet set (anticipated artifacts per `_CONTEXT.md`).
10.2 Hand off submittals and the document register through **DEL-067-05 Vendor Document Turnover Package**. (DELIVERABLE_REGISTER.csv row 532.) This deliverable does not directly produce the turnover register.
10.3 Support **DEL-067-06 EPC Vendor Package Review and Acceptance** with test/inspection evidence. (DELIVERABLE_REGISTER.csv row 533.)

## Verification

| Step | Verification |
|---|---|
| Step 1 | Battery-limit drawing reviewed with EPC Integrator; tag list matches DBM row 99 |
| Step 2 | Design SG and composition envelope recorded in vendor design basis; outstanding TBCs listed |
| Step 3 | API 650 calculations stamped; fill-limit and thermal-expansion check recorded |
| Step 4 | Coating qualification report; insulation/heating calculation issued |
| Step 5 | Internals drawing reviewed; Kennilworth skim system datasheet attached |
| Step 6 | PVRV sizing calc per API 2000; EPRV item tracked to closure; HAZOP isolation outcome recorded |
| Step 7 | Nozzle schedule and truck-out connection drawing |
| Step 8 | Plot-plan compliance confirmed by EPC Integrator against DBM §2.5 |
| Step 9 | Hydrostatic test report; NDE records; coating DFT/cure logs; insulation commissioning |
| Step 10 | DEL-067-05 turnover index reconciled; DEL-067-06 acceptance package supplied |

## Records

- Vendor package design basis document
- Vendor package datasheet set (tank datasheets, coating, insulation, heating, PVRV, internals)
- API 650 design calculations and stamped drawings
- PVRV sizing calculation (API 2000 basis)
- EPRV sizing record (or tracked TBD closure note)
- HAZOP isolation philosophy ruling
- Hydrostatic test report; NDE records; coating QA records
- Submittal index handed to DEL-067-05; acceptance evidence handed to DEL-067-06
