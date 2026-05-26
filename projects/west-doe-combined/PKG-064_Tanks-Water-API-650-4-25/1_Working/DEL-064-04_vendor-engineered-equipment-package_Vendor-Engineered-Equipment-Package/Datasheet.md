# Datasheet: DEL-064-04 — Vendor Engineered Equipment Package (Tanks, Water (API 650) 4-25)

> Pass 1/Pass 2 draft from `TASK + four-documents`. Substantive claims are source-grounded to the West Doe Deepcut DBM (4-25). Values not present in accessible sources are marked `TBD`. Inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-064-04_vendor-engineered-equipment-package` | `_CONTEXT.md` Identity |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` Identity |
| Parent Package | `PKG-064` — Tanks, Water (API 650) 4-25 | `_CONTEXT.md` Identity |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` Identity |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` Identity |
| Covers Scope Items | SOW-0233; SOW-0234; SOW-0235; SOW-0236 | `_CONTEXT.md` Covers Scope Items |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION — PACKAGE_HEURISTIC association at PKG-064 level) | `_CONTEXT.md`; PROJECT_DECOMP OBJECTIVE_DELIVERABLE_MAP |
| Package Line-Item Equipment Count | 2 process water storage tanks | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. Equipment & Package Line-Item Requirements (rows 2560, 2628) |
| Equipment Tags | TK-5317-1, TK-5318-1 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 2628 |
| Facility / LSD | 4-25 (Deepcut), LSD 04-25-80-15W6 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | Process water storage (used as make-up water for amine treating unit, Module 530) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. NGL Mercaptan Caustic Treating Make-up Water (line ~1556) and Module 530 description (line ~1132) |
| Governing tank standard | API 650 (modified, atmospheric) — applied as an analogue to other 4-25 atmospheric storage tanks | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518, 1646; ASSUMPTION: same modified-API-650 basis applies to process water tank line — confirm against vendor design basis |
| Tank quantity | 2 (x100% nominal sparing — ASSUMPTION) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 2628 |
| Tank capacity (each) | TBD — not specified in accessible source slices for the process water tanks | source TBD |
| Tank design specific gravity | TBD — accessible source gives produced water tank design SG = 1.25 (TBC) and condensate tank SG = 1.0; no process-water-tank-specific SG located | source TBD; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. Produced Water |
| Tank design pressure | Atmospheric with 16 oz test pressure (ASSUMPTION — by analogy with produced water and condensate tanks at 4-25) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518, 1646–1648 |
| Maximum fill | 90% of tank volume (ASSUMPTION — by analogy with produced water and condensate tanks) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 519, 1648 |
| Blanket gas | Provided for winter vacuum prevention; API 2000 basis for blanket / vent rates (ASSUMPTION — by analogy with other atmospheric 4-25 tanks) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows ~520, ~1664 |
| VRU connection | Process water storage tank vapours are not explicitly listed in the VRU gas-source table; produced water tanks and C5+ tanks are. ASSUMPTION: process water tanks are not VRU-connected unless detailed engineering shows otherwise | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. VRU gas source table (line ~1714) |
| Insulation / heat tracing | TBD — produced water tanks are externally insulated and heated; "water tanks shall be insulated to prevent winter freezing" appears as a general 4-25 statement (line 2509). ASSUMPTION: process water tanks are similarly insulated and freeze-protected | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2509, line 524 |
| Internal coating | TBD — produced water tanks use Devchem 253; process water tank coating not specified | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 |
| Associated transfer pumps | PROCESS WATER TRANSFER PUMPS (x2) located in Tank Farm Pump Building 2 (separate deliverable scope) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Tank Farm Pump Building row |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | LSD 04-25-80-15W6, approximately 22.2 km north of Dawson Creek, BC | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01 |
| Ambient design range | Per West Doe Deepcut site basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-02 Site (TBD — specific min/max not extracted in this draft) |
| Plant spacing — atmospheric tank | Plant spacing rules per "Atmospheric Tank and General Plant Spacing" section apply | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Sec. Atmospheric Tank and General Plant Spacing (line ~261) |
| Distance from flare | Reference: 25 m (82 ft) between flare and separators or atmospheric produced-water tanks per OGAOM Sec. 9.6.15; ASSUMPTION: applies to process water tank by analogue | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 283 |
| Containment / berm | TBD — specific berm sizing not in accessible source slices | source TBD |
| Stored fluid hazard class | Process water — non-hazardous in normal operation (ASSUMPTION); confirm via vendor MSDS / process basis | source TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Material — shell/floor/roof | TBD — not in accessible source slices for process water tanks | source TBD |
| Foundation / ring wall | TBD | source TBD |
| Nozzles, manways, internals | TBD — vendor scope per Package Datasheet handoff | source TBD; `_CONTEXT.md` Scope |
| Vents / PVRV / EPRV | PVRV per atmospheric-tank practice (ASSUMPTION); EPRV sizing for review during detailed engineering (analogue to produced water tanks) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 |
| Heat tracing / insulation | Insulated for winter freeze protection (per line 2509) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2509 |
| Coatings | TBD | source TBD |
| Instrumentation | Level, temperature, pressure (PVRV) at minimum — ASSUMPTION based on typical atmospheric storage tank practice | source TBD |

## References

- `_REFERENCES.md` (this deliverable)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — West Doe Deepcut DBM (locally accessible)
- `_Sources/26020-Package_Requirements.docx` — package requirements (binary; not directly accessible in this run; relevant content as cited via decomposition row reference "package heading 19") — `location TBD`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 543
