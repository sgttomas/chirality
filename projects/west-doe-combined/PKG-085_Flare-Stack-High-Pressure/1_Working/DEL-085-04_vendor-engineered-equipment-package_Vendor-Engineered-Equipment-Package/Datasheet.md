# Datasheet — DEL-085-04 Vendor Engineered Equipment Package (Flare Stack, High Pressure)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-085-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-085` Flare Stack (High Pressure) | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Covers Scope Items | SOW-0087, SOW-0088, SOW-0089, SOW-0090 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Supports Objectives (ASSUMPTION, package-grouping heuristic) | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; PACKAGE_HEURISTIC association |
| Authoritative Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |
| Source Reference | Workbook Packages row 58; 26020-Package_Requirements.docx package heading 38 | `_CONTEXT.md` |

## Attributes

The vendor engineered equipment package is the physical flare-stack equipment package (engineering, design, fabrication/supply, and physical hardware) developed by the Package Vendor from EPC Scope of Work (`DEL-085-01`) and Package Datasheet (`DEL-085-02`) inputs.

| Attribute | Value | Notes / Source |
|---|---|---|
| Service | High-pressure (HP) relief/blowdown disposal via HP flare | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Flare and Blowdown section |
| Stack Configuration (current source basis) | Sonic HP/Cryo flare stack, 660 mm OD by 60,957 mm tall (dual HP/Cryo and LP stack arrangement; LP stack OD TBD) | 3-25 DBM Flare and Blowdown |
| HP Relief Header Size (current source basis) | 508 mm (20 in) | 3-25 DBM Flare and Blowdown |
| HP KO Drums Feeding HP Flare | V-4100-2 (compressor area), V-4150-2 (tank farm); both manifold to HP flare | 3-25 DBM Flare and Blowdown |
| KO Drum Transfer Pumps | P-4100-2, P-4150-2; truck-out or transfer to slop; 1 x 100% per drum | 3-25 DBM Flare and Blowdown; Equipment Count table |
| Tributary Services (HP) | Inlet separator relief/blowdown; stabilizer flash/feed separator relief and blowdown; stabilizer tower relief and blowdown; MPFF blowdown; SOC HP relief/blowdown; pig receiver HP vent; contactor blowdown | 4-25 Deepcut DBM (HP flare routing statements); 3-25 DBM |
| Plant 04-25 Interfaces Carried | HP flare service for stabilizer, MPFF, SOC, inlet separators, pig receiver | 4-25 Deepcut DBM |
| Shared/cross-facility status | HP/Cryo and LP dual flare stack is a shared 03-25 / 04-25 system; exact service split and owner interface carried as open interface items | 3-25 DBM utilities narrative |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Allowable thermal radiation flux (inside boundary, blackened area) | ≤ 9 kW/m² | 4-25 Deepcut DBM Flare and Incinerator Spacing; OGPFR Appendix 1, Schedule 1, Sec. 2 (external regulatory ref TBD) |
| Allowable thermal radiation flux (outside boundary) | ≤ 5 kW/m² | 4-25 Deepcut DBM; OGPFR Appendix 1, Schedule 1, Sec. 2 (external ref TBD) |
| Spacing: flare to nearest plant equipment | 25 m (82 ft) | 4-25 Deepcut DBM; OGAOM Sec. 9.6.15 |
| Spacing: flare to nearest public road or property line | 80 m (262.5 ft) | 4-25 Deepcut DBM; OGAOM Sec. 9.6.15 |
| Spacing: flare to atmospheric condensate tanks | 50 m (164 ft) | 4-25 Deepcut DBM; OGAOM Sec. 9.6.15 |
| Spacing: flare to separators / atmospheric produced-water tanks | 25 m (82 ft) | 4-25 Deepcut DBM; OGAOM Sec. 9.6.15 |
| Spacing: flare to pressurized bullets | 30.48 m (100 ft) | 4-25 Deepcut DBM; API 2510 |
| Spacing: flare KO tanks to vegetation / fire hazards | 10 m (32 ft) | 4-25 Deepcut DBM; OGAOM Sec. 9.6.15 |
| Spacing: fired heater to flare/incinerator | 25 m (82 ft) | 4-25 Deepcut DBM; OGAOM Sec. 9.6.15 |
| Relief/blowdown design loads | Final flare studies required; current basis stated as preliminary | 3-25 DBM Plant Information Summary ("blowdown and relief basis require final flare studies") |
| Site environmental design loads (snow, wind, seismic, frost, vibration) | Per discipline civil/structural basis | 3-25 DBM Foundations narrative (flare/stack elements explicitly listed) |

## Construction

| Item | Value | Source |
|---|---|---|
| Stack type | Sonic HP/Cryo (current source basis) | 3-25 DBM Flare and Blowdown |
| Stack OD x Height | 660 mm OD x 60,957 mm tall (HP/Cryo); LP OD TBD | 3-25 DBM |
| KO drum configuration | Two HP KO drums upstream of HP flare (V-4100-2 compressor area; V-4150-2 tank farm) | 3-25 DBM |
| Transfer pumps per KO drum | 1 x 100% | 3-25 DBM Equipment Count |
| Foundations | Designed per final geotechnical report and equipment-specific anchorage; flare/stack elements explicitly named | 3-25 DBM Foundations |
| Detection at flare/vent interfaces | LEL, H2S, methyl mercaptan, fire detection per process hazards; counts/locations TBD pending detailed design | 3-25 DBM Detection narrative |
| Vendor package scope boundaries (mechanical, structural, instrumentation, controls, electrical, painting/coating, insulation/tracing, supply of bulks) | TBD — defined by EPC SOW (`DEL-085-01`) and Package Datasheet (`DEL-085-02`) | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Tagged equipment list within vendor scope | TBD — to be issued by Package Vendor and reconciled against EPC SOW tagged equipment list | DELIVERABLE_REGISTER.csv DEL-085-01 anticipated artifacts |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- `_DEPENDENCIES.md` (this deliverable)
- GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP snapshot — DELIVERABLE_REGISTER.csv (row DEL-085-04 and sibling rows DEL-085-01 through DEL-085-06)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — Flare and Blowdown; Equipment Count; Utilities; Foundations; Detection
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Flare and Incinerator Spacing; HP flare service interfaces (inlet separators, MPFF, stabilizers, SOC)
- 26020-Package_Requirements.docx package heading 38 — referenced by `_CONTEXT.md`; location accessible as `.docx`, slice not extracted for this run (location TBD)
- OGPFR Appendix 1, Schedule 1, Sec. 2 — referenced by 4-25 Deepcut DBM; external regulatory document, slice TBD
- OGAOM Sec. 9.6.15 — referenced by 4-25 Deepcut DBM; external regulatory document, slice TBD
- API 2510 — referenced by 4-25 Deepcut DBM; external industry standard, slice TBD
