# Datasheet — DEL-091-03 Construction Work Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-091-03_construction-work-package` | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-091` | `_CONTEXT.md` |
| ParentWorkbookID | 91 | `_CONTEXT.md` |
| PackageName | Tank Farm Pump Building 3-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | SOW-0185, SOW-0186, SOW-0187, SOW-0188 | `_CONTEXT.md`; GATE-07 `SCOPE_LEDGER.csv` rows 186–189 |
| Supports Objectives (ASSUMPTION, package-heuristic) | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row 470 |

## Attributes

### Package physical scope (housed equipment to be installed and tied in)

Equipment list to be physically received, set, aligned, connected, tested, and turned over by the EPC Integrator. Tag and rating data is sourced from SOW-0187.

| Tag | Service | Type | Rated duty / motor | Source |
|---|---|---|---|---|
| P-9295-2 | Building Drain Pump (1) | Graco 1050A pneumatic diaphragm | 11.34 m3/h @ 689 kPag; pneumatically driven | SOW-0187; SOW-0188 |
| P-9290-2 / P-9293-2 | Water Transfer Pumps (2) | Radial centrifugal; single mechanical seal | 150 kW (200 hp); 575 V / 3-ph / 60 Hz; duty 218 m3/d @ 172 kPad | SOW-0187; SOW-0188 |
| P-9215-2 / P-9216-2 | Sour Condensate Booster Pumps (2) | Vertical inline centrifugal; API-682 Plan 14/52 | 18.5 kW (25 hp); 575 V / 3-ph / 60 Hz | SOW-0187 |
| P-9210-2 / P-9220-2 | Condensate Sweetening Feed Pumps (2) | Vertical inline centrifugal; API-682 Plan 14/52 | 55 kW (75 hp) @ 100%; 575 V (voltage explicit `TBD` confirm) | SOW-0187 |
| P-9200-2 | Condensate Skim Pump (1) | Diaphragm positive displacement; Hydracell, sealless | 11 kW (15 hp); 575 V / 3-ph / 60 Hz; 20 m3/h | SOW-0187; SOW-0188 |
| P-9230-2 | Sour Condensate Recycle Pump (1) | Diaphragm positive displacement; Hydracell, sealless | 11 kW (15 hp); 575 V / 3-ph / 60 Hz; 20 m3/h | SOW-0187; SOW-0188 |
| P-9211-2 / P-9221-2 | Condensate Booster Pumps (2) | Vertical inline centrifugal; API-682 Plan 14/52 | 18.5 kW (25 hp) | SOW-0187 |
| P-9240-2 | Condensate Product Recycle Pump (1) | Diaphragm positive displacement; Hydracell, sealless | 11 kW (15 hp); inlet basket strainer (size TBC) | SOW-0187 |

### Construction interface attributes

| Attribute | Value | Source |
|---|---|---|
| Building Drain Pump bag filter / drain piping interface | Required (water transfer pumps draw produced water through bag filter to produced-water pipeline) | SOW-0186 |
| Power supply (motor-driven pumps) | 575 V / 3-ph / 60 Hz from 600 V MCC; starting method DOL or VFD; local control H-O-A or On-Off switch | SOW-0188 |
| Cold start condition | Motors sized for inlet stabilizer composition density at -40 °C start-up | SOW-0188 |
| DCS integration | By Others | SOW-0188 |
| Foundations | By Others | SOW-0188 |
| Electrical supply to MCC | By Others | SOW-0188 |
| Site location | LSD 03-25-80-15W6M, north of Dawson Creek, BC; site elevation 673 m | DBM `3-25_Comp_and_Liquids_DBM.md` §Site |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating specifications | `TBD` (SOW lists "Operating Specs TBC") | SOW-0188 |
| Design conditions | `TBD` (SOW lists "Operating Specs TBC") | SOW-0188 |
| Sour service | Yes (sour condensate, sour produced water in adjacent storage) | DBM §Liquids Hub; SOW-0186 |
| Ambient minimum (motor start) | -40 °C | SOW-0188 |
| Sour Condensate Booster Pump duty | `TBC` | SOW-0188 |
| Sweet Condensate Feed Pump duty | `TBC` | SOW-0188 |
| Condensate Booster Pump duty | `TBC` | SOW-0188 |
| Condensate loading duty | `TBC` | SOW-0188 |

## Construction

The Construction Work Package describes physical installation, build, inspection, tie-in, and turnover of the Tank Farm Pump Building 3-25 package per the Gate 5 EPC Integrator anchor scope (PROJECT_DECOMP §Gate 5, DEC-013).

Anticipated installation work fronts (`ASSUMPTION` from package type + SOW-0186/0187 content; specific construction sequence not yet sourced):

- Receipt, inspection, and set-down of the vendor-supplied pump building / pump skids on EPC-provided foundations (`TBD` foundation design — by Others per SOW-0188).
- Mechanical setting, alignment, and grouting of vertical inline centrifugal pumps and the larger 150 kW horizontal water transfer pumps.
- Piping tie-ins from produced-water storage tanks through bag filter to water transfer pump suction, and pump discharge to the produced-water pipeline (SOW-0186).
- Piping tie-ins from sour condensate storage tanks to sour condensate booster pumps, and onward to the condensate sweetening feed pumps (SOW-0186).
- Electrical tie-ins from the 600 V MCC (by Others) to local motor terminations; local H-O-A / On-Off switches; VFD or DOL starter installation per pump (SOW-0188).
- Instrumentation tie-ins for DCS integration (DCS integration by Others; field instrument installation, loop checks, and termination remain in EPC scope) (`ASSUMPTION`).
- Cold-environment construction provisions for -40 °C start-up (heat tracing, insulation) (`ASSUMPTION` — not explicitly specified in SOW).
- Pre-commissioning, mechanical completion verification, and turnover to commissioning (`ASSUMPTION`; sequence not sourced).

### Anticipated artifacts (from `_CONTEXT.md`)

- Construction work package
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (authoritative basis pointers)
- GATE-07 snapshot: `DELIVERABLE_REGISTER.csv` row 470; `SCOPE_LEDGER.csv` rows 186–189 (SOW-0185..0188); `PROJECT_DECOMP.md` §Gate 5 and §Decisions DEC-013
- DBM source slice: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Site, §Liquids Hub
- Workbook Packages row 84; `_Sources/26020-Package_Requirements.docx` package heading 44 (decomposition-cited; binary not directly slice-read in this run — `location TBD` for clause-level claims)
