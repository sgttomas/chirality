# Datasheet — DEL-074-01 Scope of Work (PKG-074 Caustic Treating, NGL Mercaptan Removal)

> Descriptive datasheet for the EPC Integrator Scope of Work deliverable. Source-anchored to the 04-25 Deepcut DBM and the 26020-Package_Requirements scope ledger entries for PKG-074. Values not explicitly substantiated in accessible sources are marked `TBD` or `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-074-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable name | Scope of Work | `_CONTEXT.md` |
| Parent package ID | `PKG-074` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Workbook package number | 74 | `_CONTEXT.md` |
| Package name | Caustic Treating (NGL Mercaptan Removal) | DELIVERABLE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible party | EPC Integrator | `_CONTEXT.md` |
| Covered scope items | SOW-0059, SOW-0060, SOW-0061, SOW-0062 | SCOPE_LEDGER.csv |
| Supported objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | DELIVERABLE_REGISTER.csv |
| Source basis | Workbook Packages row 51; 26020-Package_Requirements.docx package heading 28 | DELIVERABLE_REGISTER.csv |
| Decomposition snapshot | GATE-07_Final_Published_2026-05-24 | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Process function | Non-regenerative caustic mercaptan removal from cooled C3+ NGL downstream of the de-ethanizer | 4-25_Deepcut_DBM.md SEC-07, "Current-Scope NGL Mercaptan Treating" |
| Plant location | 04-25 Deepcut Gas Plant | 4-25_Deepcut_DBM.md SEC-07 |
| Treating technology | Non-regenerative caustic (no active on-site caustic regeneration column in current basis) | 4-25_Deepcut_DBM.md SEC-07 |
| Process provider model | Third-party proprietary process provider supplies detailed engineering package | 4-25_Deepcut_DBM.md SEC-07 |
| Inlet service | Cooled C3+ NGL from the de-ethanizer outlet path | 4-25_Deepcut_DBM.md SEC-07, Design Parameters table |
| Downstream service | NGL filtration, water wash, molecular-sieve dehydration, NGL storage bullets | 4-25_Deepcut_DBM.md SEC-07 |
| Caustic disposition | Rich caustic to caustic heating and spent-caustic storage/handling | 4-25_Deepcut_DBM.md SEC-07 |
| By-product disposition | Disulphide oil to DSO tank for truck-out; alternate DSO blending into C5+ product TBC | 4-25_Deepcut_DBM.md "Disulphide Oil, Spent Caustic, and Waste Amine" |
| Spent caustic disposition | 400 bbl spent caustic tank; trucked off site for disposal | 4-25_Deepcut_DBM.md SEC-04 |
| Process basis conflict | Brief flags conflict between regenerative DBM basis and non-regenerative SCA-001/VE-8 basis; vendor and process provider must confirm governing basis | SCOPE_LEDGER.csv SOW-0062 |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Design rate | 2,385 m3/d / 15,000 bbl/d | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Design Parameters" |
| Inlet pressure, design | 2,213 kPag | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Design Parameters" |
| Outlet pressure, design | 1,978 kPag | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Design Parameters" |
| Pressure low/high cases | `TBC` | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Design Parameters" |
| Inlet temperature (low / design / high) | 26.7 / 43.3 / 48.8 deg C | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Design Parameters" |
| Fresh caustic concentration | 50 wt% NaOH | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Design Parameters" |
| Circulating caustic concentration | 14.7 wt% NaOH (TBC) | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Design Parameters" |
| Treated NGL sulphur outlet (1 mol% H2S inlet case) | 970 ppmw total S / 122.5 lb/h as S | 4-25_Deepcut_DBM.md NGL sulphur case table |
| Untreated NGL sulphur (1 mol% H2S inlet case) | 4,166 ppmw total S | 4-25_Deepcut_DBM.md NGL sulphur case table |
| NGL C3+ sales product spec, volatile mercaptans | < 175 wppm S | 4-25_Deepcut_DBM.md "NGL C3+ Product" |
| Ambient design extreme | -40 deg C facility design basis | 4-25_Deepcut_DBM.md (facility design basis) |

## Construction

| Item | Value | Source |
|---|---|---|
| Caustic NGL contactor | Mixes NGL and circulating caustic to extract mercaptans | 4-25_Deepcut_DBM.md "NGL Mercaptan Treating Equipment and Utilities" |
| Caustic outlet filters | 2 x 100% independent vessels downstream of contactor | 4-25_Deepcut_DBM.md SEC-07 |
| Water wash and coalescing filtration | Dilutes and removes entrained caustic to protect molecular sieve | 4-25_Deepcut_DBM.md SEC-07 |
| Water wash recycle pumps | Single-stage vertical inline centrifugal, single mechanical seals, 2 x 100% | 4-25_Deepcut_DBM.md SEC-07 |
| Pressurized caustic drain drum (V-6940-1) | Heated, insulated, demister, K < 0.2; vapours to SOC first-stage suction; liquids level-controlled to spent caustic tank | 4-25_Deepcut_DBM.md SEC-07; tag from compressor source table |
| Fresh caustic tank | 1 x 400 bbl, atmospheric, heated, insulated, truck-in, LP fuel-gas blanket, NOT connected to VRU; SG 1.75 TBC | 4-25_Deepcut_DBM.md SEC-07 |
| Spent caustic tank | 1 x 400 bbl, atmospheric, heated, insulated, truck-out, incinerator vent with flame arrestor, LP fuel-gas blanket | 4-25_Deepcut_DBM.md SEC-07 |
| DSO storage tank | 1 x 400 bbl, atmospheric, heated, insulated, truck-out, incinerator vent with flame arrestor, LP fuel-gas blanket; SG 1.75 TBC | 4-25_Deepcut_DBM.md SEC-07 |
| Building | Caustic-containing equipment installed indoors in Mercaptan Treating Unit building (caustic freezing/crystallization risk) | 4-25_Deepcut_DBM.md SEC-07 |
| Safety showers | Water safety showers in building; quantity and locations `TBD`; activation must provide discrete control-room alert | 4-25_Deepcut_DBM.md SEC-07 |
| Materials prohibition | No aluminum in caustic building; insulation cladding/straps in caustic exposure areas in stainless steel; tank materials/coatings `TBD` (polymer or caustic-compatible) | 4-25_Deepcut_DBM.md SEC-07 |
| Incinerator interface | Vapours from spent caustic and DSO tank to incinerator at 3-25 near flare stacks; upstream KO drum | 4-25_Deepcut_DBM.md "Incinerator Interface" |
| Tagged equipment count | Thirteen tagged items listed in source heading 28; one duplicated tag requires reconciliation (per SOW-0062) | SCOPE_LEDGER.csv SOW-0062; full tag list `TBD` (heading 28 not slice-extracted) |
| Major included equipment (per SOW-0061) | Caustic contactor/mixer, caustic outlet filtration, water wash and coalescing equipment, caustic regeneration equipment, heaters/exchangers, circulation and transfer pumps, pressurized caustic drain drum, DSO handling, caustic storage interfaces, incinerator interface, instrumentation, controls, and building-contained caustic equipment | SCOPE_LEDGER.csv SOW-0061 |

## References

- `_REFERENCES.md` (deliverable-local)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-07 "Current-Scope NGL Mercaptan Treating", "Disulphide Oil, Spent Caustic, and Waste Amine", "NGL C3+ Product", "Incinerator Interface"
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (PKG-074 rows)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (SOW-0059 through SOW-0062)
- `26020-Package_Requirements.docx` package heading 28 — referenced; clause-level slice not locally extracted (`location TBD` for clause text)
