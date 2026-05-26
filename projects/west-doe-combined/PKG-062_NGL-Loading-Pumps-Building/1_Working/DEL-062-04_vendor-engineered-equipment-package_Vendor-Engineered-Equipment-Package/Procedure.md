# Procedure — DEL-062-04 Vendor Engineered Equipment Package (NGL Loading Pumps Building)

> Operational procedure for producing and accepting the vendor-engineered NGL Loading Pumps Building equipment package. The procedure covers vendor execution and EPC-side checkpoints needed for package release into integration (DEL-062-06).

## Purpose

Define the controlled steps to take the deliverable from the EPC scope-of-work / package datasheet inputs through vendor engineering, fabrication, building erection, and turnover, with verification at each phase against `Specification.md`.

## Prerequisites

Inputs the vendor needs in hand before substantive engineering begins:

1. EPC Scope of Work for PKG-062 — `DEL-062-01_scope-of-work` (ASSUMPTION: upstream within PKG-062 deliverable set).
2. Package Datasheet for PKG-062 — `DEL-062-02_package-datasheet` (ASSUMPTION).
3. Workbook Packages row 76 reference set and `26020-Package_Requirements.docx` package heading 16 (cited; source slice location TBD for direct reads).
4. Site basis information sufficient to confirm R7.1/R7.2 (−40 °C start-up condition; operating and design conditions TBC). [SOW-0156]
5. Boundary declarations confirming exclusions: DCS integration, foundations, MCC supply — all "by others." [SOW-0156]
6. References listed in `_REFERENCES.md` (GATE-07 PROJECT_DECOMP snapshot and shared `_Sources` root).

## Steps

### Step 1 — Kickoff and source confirmation

1.1 Confirm the binding scope envelope with the EPC: 4 × Blackmer LGL4B in parallel; LPG storage-to-truck-loading service; 68 m³/hr @ 345 kPad per pump (TDH TBC); self-framing building, site-erected. [SOW-0154; SOW-0155]
1.2 Confirm exclusions: DCS integration, foundations, electrical supply to MCC. [SOW-0156]
1.3 Confirm motor sizing basis (inlet stabilizer composition density at −40 °C start-up). [SOW-0156]
1.4 Capture any open items as TBDs against `Specification.md` requirements.

### Step 2 — Process and hydraulic design

2.1 Develop hydraulic profile from storage to truck loading to confirm TDH. [R2.2]
2.2 Confirm pump operating point and verify NPSHa vs. NPSHr; document margin.
2.3 Select seals and materials for LPG service. [R3.2]
2.4 Issue process datasheet for the LGL4B selection.

### Step 3 — Mechanical and building design

3.1 Develop pump skid / baseplate and discharge/suction header arrangement for parallel operation. [R1.3]
3.2 Develop the self-framing building design (layout, dimensions, structural, HVAC, lighting, area classification). [R6]
3.3 Define winterization provisions appropriate to the −40 °C start-up requirement. [R7.1]
3.4 Define foundation interface (anchor pattern, loads) for "by others" foundation scope; do not include foundations in vendor scope. [R8.1]

### Step 4 — Electrical and controls interface design

4.1 Select 575 V / 3-phase / 60 Hz motors sized per R4.2. [SOW-0156]
4.2 Define motor feeder interface to the 600 V MCC (by others); produce electrical load and connection data. [R4.3; R8.2]
4.3 Define local Hand-Off-Auto / On-Off control devices and local control panel. [R5.1]
4.4 Produce I/O list and controls interface schedule to support EPC DCS integration (by others). [R5.2; OBJ-006]
4.5 Define fire/gas detection and shutdown interface points if applicable to LPG service (TBD; coordinate with EPC). [OBJ-009]

### Step 5 — Vendor documentation

5.1 Issue vendor package design basis. [R10.1]
5.2 Issue vendor package datasheet set (pumps, motors, building, instrumentation). [R10.1]
5.3 Issue interface drawings (mechanical/process, electrical, controls, building anchorage). [R8.2]
5.4 Track turnover deliverables for DEL-062-05 vendor document turnover.

### Step 6 — Fabrication and FAT

6.1 Fabricate / procure pumps and motors per approved data sheets.
6.2 Perform Factory Acceptance Test:
- pump performance at the rated point (68 m³/hr @ 345 kPad), [R2.1]
- motor electrical checks, [R4]
- local control functional checks. [R5.1]
6.3 Generate FAT reports and material/certification records.

### Step 7 — Delivery and site erection

7.1 Coordinate building delivery with the EPC foundation schedule (foundations by others). [SOW-0156]
7.2 Erect the self-framing building at site. [SOW-0155]
7.3 Install pumps, motors, and local control devices in the building.
7.4 Coordinate MCC feed cut-in with the EPC (electrical supply to MCC is by others). [SOW-0156]

### Step 8 — Site verification and handoff

8.1 Mechanical completion checks of the package per `Specification.md` Verification table.
8.2 Low-temperature start-up demonstration or equivalent vendor calculation acceptance for R4.2 / R7.1. [ASSUMPTION on method]
8.3 Transmit interface package to EPC for integration review (DEL-062-06).
8.4 Compile turnover documentation per DEL-062-05.

## Verification

| Step | Verification |
|---|---|
| Step 1 | EPC signoff that scope envelope and exclusions match Specification R1, R8. |
| Step 2 | Hydraulic calc review; pump curves; NPSH check. |
| Step 3 | Mechanical/building drawings review; foundation interface drawing accepted by EPC. |
| Step 4 | Electrical and I&C interface review with EPC; MCC coordination memo. |
| Step 5 | Document register check (interim) per DEL-062-05 plan. |
| Step 6 | FAT reports accepted by EPC; material/certification records complete. |
| Step 7 | Site delivery and erection inspection records; coordinated cut-ins. |
| Step 8 | Pre-handoff verification per Specification Verification table; EPC review status per DEL-062-06. |

## Records

The following records should result from this procedure and feed downstream deliverables:

- Vendor package design basis (R10.1).
- Vendor package datasheet set (R10.1).
- Equipment data sheets — pumps and motors.
- Hydraulic and motor-sizing calculations (with −40 °C start-up basis).
- Interface drawings/schedules (process, electrical, controls, fire/gas if applicable, building anchorage).
- FAT reports and certifications.
- Site erection inspection records.
- Turnover document register (feeds DEL-062-05).
- Open items list captured against Specification TBDs.
