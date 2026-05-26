# Specification — DEL-086-02 Package Datasheet (Flare Stack (Low Pressure))

## Scope

### In Scope

The Package Datasheet shall declare the technical handoff data required for the Package Vendor to perform package engineering, design, vendor documentation, and physical equipment supply for `PKG-086` — Flare Stack (Low Pressure), consisting of:

- One LP flare stack (tag TBD — not stated in accessible source slices). [PACKAGE_REGISTER.csv row 59; DBM §"Flare and Blowdown"]
- One associated LP flare stack blower (tag TBD). [PACKAGE_REGISTER.csv row 59]
- Equipment design data, process conditions, mechanical/structural/material requirements, interface requirements matrix, and source-supported design criteria.

### Out of Scope

- Construction/installation execution (covered by `DEL-086-03` Construction Work Package).
- Vendor package engineering deliverables themselves (covered by `DEL-086-04` Vendor Engineered Equipment Package).
- Vendor document turnover (covered by `DEL-086-05`).
- EPC vendor package review and acceptance (covered by `DEL-086-06`).
- LP flare KO drum scope (`PKG-082`, drum `V-3900-2`, pump `P-3900-2`). [DBM §"Flare and Blowdown"]
- HP/Cryo flare stack scope (separate package; HP/Cryo sonic stack 660 mm OD x 60,957 mm tall per DBM). [DBM §"Flare and Blowdown"]

## Requirements

### R1 — Equipment Identity and Quantity

R1.1 The datasheet SHALL identify the LP flare stack by tag (TBD — `location TBD`: `26020-Package_Requirements.docx` package heading 39).

R1.2 The datasheet SHALL identify the LP flare stack blower by tag (TBD — same source).

R1.3 The datasheet SHALL state the package quantity (ASSUMPTION: 1 stack and 1 blower per facility, consistent with PACKAGE_REGISTER scope statement).

Source: PACKAGE_REGISTER.csv row 59.

### R2 — Process Conditions and Service Definition

R2.1 The datasheet SHALL state design pressure, design temperature, and any cyclic / thermal loading basis for the stack and the blower. (Values: TBD — accessible source slices do not include numeric stack design conditions.)

R2.2 The datasheet SHALL state the LP relief inlet header connection size consistent with the project basis of 508 mm / 20 inch.

Source: DBM §"Flare and Blowdown" (line 499).

R2.3 The datasheet SHALL identify the LP flare service list as receiving TEG regeneration, VRU, and compressor seal-pot relief/vent services.

Source: DBM §"Flare and Blowdown" (line 499).

R2.4 The datasheet SHALL state the LP relief load, blowdown load, and disposition basis. The package SHALL support staggered blowdown to limit maximum relief.

Source: DBM §"Flare and Blowdown" (line 501). Final values: TBD pending flare studies and `W242510-PRC-REP-000003-001`.

### R3 — Stack Mechanical / Structural Requirements

R3.1 The datasheet SHALL state the stack OD and height. (Values: TBD — DBM explicitly states "LP stack OD remains TBD".)

Source: DBM §"Flare and Blowdown" (line 499).

R3.2 The datasheet SHALL state the stack support type (self-supported, guyed, or derrick). ASSUMPTION: self-supported based on PACKAGE_REGISTER Source Basis pointer to `24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf` (budgetary go-by only; not locally accessible — confirmation required).

Source: PACKAGE_REGISTER.csv row 59 Source Basis field.

R3.3 The datasheet SHALL state wind, snow, seismic, and frost design criteria for the stack and blower foundation/anchorage.

Source: DBM §"Foundations" (line 700). Values: TBD pending geotechnical and site civil criteria.

### R4 — Materials and Service Classification

R4.1 The datasheet SHALL identify the inlet/relief service as low-pressure flare/vent service and SHALL state whether sour-service (NACE MR0175 / ISO 15156) requirements apply on the wetted relief envelope. ASSUMPTION: applicable based on facility isolation philosophy; confirm via process simulation/HAZOP (not locally accessible).

Source: DBM §isolation philosophy (line 607).

R4.2 The datasheet SHALL state stack material selection (shell, tip, refractory if any) consistent with combustion temperature and emissions basis. Values: TBD.

### R5 — Blower / Auxiliaries

R5.1 The datasheet SHALL state blower duty (volumetric flow, discharge pressure), driver type, motor rating, and area classification. Values: TBD.

R5.2 The datasheet SHALL state pilot / ignition system type, pilot fuel gas demand, and reliability basis. Values: TBD.

R5.3 The datasheet SHALL identify any purge gas requirements to prevent air ingress. Values: TBD.

### R6 — Interface Requirements

R6.1 The datasheet SHALL include an interface requirements matrix covering the package's applicable interface types: Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; I&C / Control Cabling; Fire & Gas / Safety Systems; Structural / Foundations / Supports.

Source: PACKAGE_REGISTER.csv row 59.

R6.2 The datasheet SHALL identify the shared-facility 03-25 / 04-25 split for the dual flare stack system, marking unresolved owner-interface items as open.

Source: DBM §3.1 cross-facility shared utilities (line 56).

### R7 — Emissions and Permit Basis

R7.1 The datasheet SHALL record the emissions basis used for sizing and operability (combustion efficiency, smokeless design point, permit-relevant inputs). Values: TBD pending emissions confirmation.

Source: DBM §"Emissions Basis" (line 555).

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API Std 521 — Pressure-relieving and Depressuring Systems | Flare relief loads, blowdown, knockout, radiation/dispersion basis | location TBD (standard not in workspace; ASSUMPTION based on industry convention for flare-stack packages) |
| API Std 537 — Flare Details for General Refinery and Petrochemical Service | Flare burner, pilot, ignition, mechanical details | location TBD (ASSUMPTION) |
| API RP 14E — Design of Offshore Production Platform Piping Systems | Relief header sizing/erosional velocity basis | location TBD (ASSUMPTION) |
| NACE MR0175 / ISO 15156 | Sour-service materials on wetted relief envelope (if confirmed sour) | location TBD; applicability per R4.1 |
| Plant Shutdown and Blowdown Philosophy `W242510-PRC-REP-000003-001` | Blowdown sequencing and relief load basis | location TBD (not locally accessible) |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1.x (identity, quantity) | Confirm against `26020-Package_Requirements.docx` package heading 39 once parsed; cross-check with EPC `DEL-086-01` Scope of Work. |
| R2.x (process conditions) | Process engineering review against final flare study and DBM update; cross-check with `DEL-082-02` (LP KO drum) for upstream consistency. |
| R3.x (stack mechanical/structural) | Structural calculations to applicable code; foundation review against site geotechnical report; vendor stack calculations to be reviewed under `DEL-086-06`. |
| R4.x (materials/service) | Process classification confirmation and HAZOP closure; NACE applicability decision recorded in `_DEPENDENCIES.md` as a constraint. |
| R5.x (blower/auxiliaries) | Vendor datasheets and FAT plan reviewed under `DEL-086-06`; site acceptance verified under `DEL-086-03`. |
| R6.x (interfaces) | Interface matrix walked through with EPC discipline leads (mechanical, electrical, I&C, fire & gas, civil/structural); open items tracked. |
| R7.x (emissions) | Confirm emissions inputs against final permit basis; record permit reference once available. |

## Documentation

- Package technical datasheet (this artifact's downstream populated form). [`_CONTEXT.md` anticipated artifacts]
- Vendor engineering handoff basis (narrative). [`_CONTEXT.md`]
- Package interface requirements matrix. [`_CONTEXT.md`]
- Source-supported equipment and design criteria. [`_CONTEXT.md`]
