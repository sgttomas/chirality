# Procedure — Construction Work Package (VRU 4-25)

DeliverableID: `DEL-047-03_construction-work-package`
ParentPackageID: `PKG-047`

This procedure describes the construction execution steps needed to install, tie in, mechanically complete, and turn over the VRU 4-25 packages to commissioning. It is operational from the EPC Integrator's construction-management perspective.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` reviewed.
- Decomposition row DEL-047-03 (DELIVERABLE_REGISTER.csv) understood.
- SOW-0253..SOW-0256 reviewed (SCOPE_LEDGER.csv).
- DBM-Deepcut "Vapour Recovery Unit" section read and tie-in interfaces understood.
- DEL-047-02 (Package Datasheet) issued or available in draft.
- DEL-047-04 (Vendor-engineered equipment package) drawings, anchor-bolt pattern, weights, and shipping arrangement available.
- DEL-047-05 (Vendor document turnover) installation manual, torque tables, and field-service requirements available.
- Conflict items CFL-1 (motor voltage/power) and CFL-2 (building count) resolved by human ruling before relevant subsections execute (electrical and civil/building).
- Site-wide construction prerequisites (permits, fire protection, lay-down areas, MEWP/crane plans) in place.
- All `TBD` items below cleared or carried as documented holds.

## Steps

### Phase A — Receiving and lay-down

A1. Receive vendor compressor packages at site per shipping plan (DEL-047-04). Verify pack list, inspect for shipping damage, record any exceptions. **Records:** receiving inspection report.

A2. Move packages to lay-down area or directly to setting location. Crane/lift plan: **TBD** (rigging study from EPC construction).

### Phase B — Foundations and setting

B1. Verify pile installation acceptance for each VRU foundation (driving records, load test where required, top-of-pile survey). **Source for pile basis:** SOW-0256; pile design details TBD.

B2. Install pile cap / grout pad per EPC civil drawings. **TBD** drawing reference.

B3. Set each compressor package on anchor bolts per vendor anchor-bolt pattern. Level and grout per vendor tolerance (**TBD** from DEL-047-04).

B4. Install mounting platform, stairs, and access steel per EPC structural drawings. **Source:** SOW-0256.

### Phase C — Building(s) and HVAC

> **HOLD until CFL-2 ruling** (one building per SOW-0254 vs two buildings per DBM).

C1. Erect VRU building(s) per ruled basis. Verify gas-detection coverage, ventilation rates, and EHT zoning per EPC HVAC and F&G packages.

C2. Building functional test prior to package energization.

### Phase D — Mechanical tie-ins

D1. Install inlet tie-in piping from low-pressure vapour sources (storage tanks, low-pressure process vapour sources per DBM) to each VRU first-stage suction flange. Line class, material, slope: **TBD** from mechanical/piping deliverable. Sour-service NACE materials per R1.

D2. Install discharge tie-in piping from each VRU second-stage discharge to the 04-25 Stabilizer Overheads Compressor (SOC) first-stage suction header. Confirm 03-25 VRU discharge tie-in handover point if shared header construction is in EPC scope. **Source:** DBM VRU section.

D3. Install primary seal vent tie-in to LP flare header. **Source:** DBM VRU table; SOW-0255.

D4. Install utility tie-ins (fuel-gas barrier-fluid supply per Plan 53 seal arrangement, instrument air, drains, blanket gas where required). Specific line list: **TBD**.

D5. NDE per accepted weld map and procedure. PWHT per material/thickness. **Procedure reference: TBD**.

D6. Pressure test (hydrostatic or pneumatic per line class) and document. Issue test packages.

### Phase E — Electrical and instrumentation

> **HOLD until CFL-1 ruling** (200 HP / 600 V VFD-ready per SOW-0256 vs 4,000 V per DBM).

E1. Install power cable, conduit/tray, and local disconnect from MCC/VFD lineup to each compressor motor and cooler motor per ruled basis.

E2. Megger and continuity test cables before termination; record results.

E3. Terminate motor and cooler-motor power. Verify rotation by uncoupled bump (or per vendor procedure).

E4. Install instrumentation tubing/cable for vendor-supplied transmitters, RTDs, vibration probes, gas detectors, and barrier-fluid alarm switches.

E5. Loop check against the vendor control narrative (DEL-047-05). Confirm primary seal vent alarm path to facility F&G/DCS.

E6. Energize VFDs in commissioning-controlled sequence (typically commissioning-led; construction supports).

### Phase F — Pre-commissioning and mechanical completion

F1. Flush, clean, and lay-up piping per facility cleanliness standard (**TBD** reference).

F2. Inert/purge sour-service systems prior to first hydrocarbon introduction. Document gas-tests at each step. **Procedure reference:** facility sour-service entry/work procedure — **location TBD** (DBM SEC-14/SEC-15 referenced but not extracted for this deliverable).

F3. Final torque and bolt-up walkdown. Document deltas.

F4. Walkdown punch list with commissioning lead; categorize A/B items.

F5. Issue mechanical completion certificate per facility template.

### Phase G — Turnover

G1. Compile the **Construction interface and turnover checklist** (anticipated artifact per `_CONTEXT.md`). Minimum content per Specification R6.1.

G2. Hand over the system to commissioning. Maintain construction support on call for A-item closure during commissioning.

G3. Document handover signatures. Update PKG-047 status and link the turnover record to DEL-047-06 (EPC vendor package review and acceptance).

## Verification

| Step group | Verification |
|---|---|
| A (Receiving) | Signed receiving inspection report; damage exceptions logged |
| B (Foundations/setting) | Pile records; survey acceptance; grout records; vendor levelling acceptance |
| C (Building/HVAC) | Building functional test; F&G coverage map |
| D (Mechanical) | Weld map closure; NDE coverage; pressure test packages; line walkdowns |
| E (Electrical/I&C) | Megger/continuity; rotation check; loop-check records; VFD configuration verification |
| F (Pre-commissioning) | Cleanliness records; inert/purge gas tests; punch list issued |
| G (Turnover) | Signed mechanical completion certificate; turnover checklist; handover signatures |

## Records

The construction package SHALL retain (and turn over with the package):

- Receiving inspection reports and shipping-damage exceptions.
- Pile records and foundation survey acceptance.
- Weld maps, weld records, NDE reports, PWHT charts (where applicable).
- Pressure test packages (hydro/pneumatic).
- Electrical test records (megger, continuity, motor-rotation bumps, VFD parameter dumps).
- Loop check sheets.
- Inerting/purge gas-test logs.
- Punch list (with A/B classification and close-out evidence).
- Mechanical completion certificate.
- **Construction interface and turnover checklist** (anticipated artifact per `_CONTEXT.md`).
- **Installation and tie-in workface plan** (anticipated artifact per `_CONTEXT.md`).

## TBD / Open Holds

- HOLD on Phase C until CFL-2 (building count) is ruled.
- HOLD on Phase E until CFL-1 (motor voltage/power) is ruled.
- Pile design parameters (B1, B2): TBD from EPC civil/structural package.
- Tie-in line list, isometrics, line classes, slopes (D1, D4): TBD from EPC mechanical/piping package.
- Sour-service entry/purge procedure reference (F2): TBD; DBM SEC-14/SEC-15 not extracted locally for this deliverable.
- Cleanliness standard reference (F1): TBD.
- Crane/rigging plan (A2): TBD.
- Vendor levelling/torque tolerance (B3, F3): TBD from DEL-047-04/DEL-047-05.
