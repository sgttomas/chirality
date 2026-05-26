# Datasheet — PKG-068 TEG Dehydration Unit (Package Datasheet)

> EPC-Integrator-authored technical handoff data for third-party Package Vendor engineering and design of the 04-25 Deepcut process-gas TEG dehydration unit. Values are extracted from accessible source materials; unresolved items are marked `TBD` or `ASSUMPTION` per the deliverable's authority hierarchy.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-068-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | `PKG-068` | `_CONTEXT.md` |
| Parent Workbook ID | 68 | `_CONTEXT.md` |
| Package Name | TEG Dehydration Unit | `_CONTEXT.md` |
| Package CoA Tracking | `26020-01-22-001` | `PACKAGE_REGISTER.csv` (Gate 7 snapshot) |
| Facility / WBS | 04-25 (Deepcut) / WBS 01 | `PACKAGE_REGISTER.csv`; `4-25_Deepcut_DBM.md` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party (this deliverable) | EPC Integrator | `_CONTEXT.md` |
| Package Vendor Scope Owner | Package Vendor (vendor-owned package engineering, design, documentation, and physical equipment) | `PACKAGE_REGISTER.csv` Responsibility Model |
| Service | Process-gas TEG dehydration of sweet sour-origin gas, downstream of amine treating, upstream of molecular-sieve dehydration | `4-25_Deepcut_DBM.md` SEC-06 Process Description |
| Module Tag (reference) | `570-1 TEG Dehydration Module` (Shop) | `4-25_Deepcut_DBM.md` |
| Tagged Equipment Set (reference) | AC-5720-1, AC-5700-1, AC-5702-1, AC-5795-1, ACF-5720-1, ACF-5700-1, T-5793-1, T-5770-1, T-5710-1, T-5712-1, V-5725-1, D-5715-1, D-5717-1, V-5775-1, E-5740-1, E-5742-1, F-5755-1, F-5750-1, F-5760-1, F-5705-1, F-5707-1, E-5790-1, E-5793-1, P-5797-1, P-5798-1, P-5730-1, P-5780-1, P-5781-1, V-5798-1, TK-5730-1 | `PACKAGE_REGISTER.csv`; `4-25_Deepcut_DBM.md` equipment row 104 |

## Attributes

### Package equipment scope (Package Vendor delivery)

| Item | Description | Source |
|---|---|---|
| Inlet Air Cooler (TEG inlet cooler) | Aerial cooler with automatic warm-air recirculation, automated side-air and recirculation louvers, electric or heat-medium plenum heater | `PACKAGE_REGISTER.csv`; `4-25_Deepcut_DBM.md` SEC-06 TEG Equipment |
| TEG Inlet Filter / Coalescer | Removes free water, aerosols, contaminants, amine carryover, particulates upstream of contactor | same |
| TEG Contactor | Structured packing absorber; dehydrates gas with triethylene glycol | same |
| Glycol Flash Tank | Three-phase rich-TEG flash separator | same |
| Glycol Reboiler / Still Column | TEG regeneration (BKU reboiler, still, stripping column) | same |
| Glycol Circulation Pumps | Lean TEG circulation to contactor | same |
| Glycol Particulate Filters | Full-flow rich-TEG particle filtration | same |
| Glycol Charcoal Filter | Rich-TEG slipstream activated-carbon filtration | same |
| Gas/Glycol Exchanger | Lean/rich TEG heat exchanger | same |
| Air/Glycol Exchanger | Multi-service aerial cooler (lean TEG + still overheads bundles) | same |
| Fuel Gas Scrubber | Conditions LP fuel gas used as TEG stripping gas | `PACKAGE_REGISTER.csv` scope list |
| TEG Make-up Tank | Atmospheric heated/insulated storage with fuel-gas blanket; no VRU connection | `4-25_Deepcut_DBM.md` |
| Burner Control Panel | Reboiler burner management (heat-medium-driven equivalent if applicable) | `PACKAGE_REGISTER.csv` scope list; configuration TBD |

ASSUMPTION: The "Burner Control Panel" line item is carried verbatim from the workbook package scope. The 04-25 DBM specifies a 425 degF heat-medium-fired reboiler (see Conditions) rather than a direct-fired burner; vendor to confirm fired-burner vs heat-medium reboiler configuration during package engineering. SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06.

### Design / process attributes (TEG unit)

| Attribute | Value | Source |
|---|---|---|
| Inlet gas, summer (Normal / Design / Max) | 303.8 / 329.2 / 329.2 MMSCFD | `4-25_Deepcut_DBM.md` SEC-06 TEG Design Values |
| Inlet gas, winter (Normal / Design / Max) | 308.4 / 335 / 335 MMSCFD | same |
| Recycled regeneration gas (from mol-sieve regen scrubber overheads) | 0–25 MMSCFD; design 25 MMSCFD | same |
| Total contactor flow, summer (Normal / Design) | 329 / 354.2 MMSCFD | same |
| Total contactor flow, winter (Normal / Design) | 333 / 360 MMSCFD | same |
| Operating pressure (basis) | 1100 psig / 7584 kPag — TBC; 1085 psig / 7481 kPag unresolved alternate | same; flagged TBC |
| TEG inlet gas temperature, summer | 43 degC (110 degF) | same |
| TEG inlet gas temperature, winter | 35 degC (95 degF) | same |
| Inlet water content | Fully water-saturated at 43 degC and confirmed inlet pressure | same |
| Contactor outlet water (design) | <= 4 lb H2O / MMSCF at defined inlet conditions | same |
| Downstream molecular-sieve tolerance | 10 lb H2O / MMSCF acceptable to mol-sieve | same |
| Contactor turndown | 3:1 inlet-gas turndown (TBC) | same |
| TEG regeneration turndown | 2:1 circulation-rate turndown | same |
| TEG reboiler heat-medium supply | 425 degF via mixing valves | same |
| Reboiler temperature (still bottoms) | 395 degF | same |
| Reboiler operating pressure | 3.25 psig | same |
| Regenerated lean TEG purity (design) | 99.80 wt% at 45.0 USGPM, 136.4 SCFM stripping gas, <3 lb H2O/MMSCF outlet | same |
| Regenerated lean TEG purity (expected) | 99.74 wt% at 44.3 USGPM, 111.8 SCFM, <4 lb H2O/MMSCF outlet | same |
| TEG circulation, design | 45.0 USGPM | same |
| TEG circulation, expected | 43.2 USGPM | same |
| Flash drum operating pressure | 60 psig (overhead flash gas routes to stabilizer overheads compressor 1st-stage suction ~50 psig) | same |
| Flash gas, design | 0.065 MMSCFD at 45 USGPM | same |
| Flash gas, expected | 0.0018 MMSCFD at 43.2 USGPM | same |
| TEG stripping gas (LP fuel gas) | 5 psig regulated; cases 56.8 / 111.8 / 136.4 SCFM at 22.5 / 44.3 / 45.0 USGPM | same |
| Still overheads recovery | Cooled, partially condensed, recovered to VRU suction header; normal backpressure ~<0.5 psig | same |
| Lean TEG cooler outlet temperature | 110 degF or 15 degF above contactor inlet gas temperature, whichever is lower | same |
| Still overheads separator | Demister; 5 min retention LAL→LAH; 2 x 100% bottoms pumps | same |
| TEG surge tank | 30 min retention at design circulation; design pressure 50 psig | same |
| TEG circulation pumps | 2 x 100% motor-driven positive-displacement rotary-vane; single mechanical seals | same |
| TEG filtration | Full-flow rich-TEG particle filter @ nominal 5 micron; 20% rich-TEG slipstream through charcoal/carbon + 5 micron | same |
| TEG drain | Equipment expected to contain liquid TEG for maintenance draining; 300# ANSI full flange rating; thermal PSV outlets routed by separate line to produced-water drain header (TBC) | `4-25_Deepcut_DBM.md` SEC-06 drainage table |

### Sparing and configuration

| Item | Sparing | Source |
|---|---|---|
| TEG Inlet Filter Coalescer | 1 x 100% with manual bypass/isolation for filter change while operating | `4-25_Deepcut_DBM.md` SEC-06 |
| TEG Contactor | TBD — 1 x 100% unit-level vs 2 x 50% contactor-vessel basis unresolved | same (TEG Open Items) |
| Lean/Rich TEG Exchanger | 1 x 100% bloc-welded plate exchanger; type and sparing TBC | same |
| TEG Circulation Pumps | 2 x 100% | same |
| Still Overheads Bottoms Pumps | 2 x 100%; standby auto-start on high level; piping sized for both pumps at design capacity | same |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour-origin sweet gas (post-amine), water-saturated, dehydrated to cryogenic-tolerable spec | `4-25_Deepcut_DBM.md` SEC-06 |
| Sulphur exposure | Sour-service design discipline applies to TEG package equipment in contact with process-side gas containing residual H2S/COS/mercaptans | ASSUMPTION based on `4-25_Deepcut_DBM.md` references to methyl mercaptan risk in TEG carbon-filter discussion and sour-service safety objective (`OBJ-009`); vendor to confirm material selection per detailed engineering |
| Battery-limit inlet | From amine absorber overhead (sweet, hot, water-saturated gas) blended with cooled water-saturated mol-sieve regeneration gas | `4-25_Deepcut_DBM.md` SEC-06 Process Description |
| Battery-limit outlet | Dehydrated gas to Inlet/TEG Dehydration Cross-Exchanger then to molecular-sieve dehydration | same |
| Rich-TEG path | Flash drum (60 psig) → filtration → lean/rich exchanger → still column → reboiler (3.25 psig, 395 degF) → surge tank | same |
| Stripping gas supply | LP fuel gas, 5 psig regulated, 0.30 MMSCFD (8.48 e3m3/d) sized basis | `4-25_Deepcut_DBM.md` SEC-08 utility table |
| Heat medium supply (reboiler) | 425 degF supply | `4-25_Deepcut_DBM.md` SEC-06; SEC-09 single-loop heat-medium basis |
| Heat-medium reboiler duty | TEG reboiler E-5790-1: 674.6 kW (2.3 design metric); 220/428 process / 166/330 utility — interpret per heat-medium reboiler table | `4-25_Deepcut_DBM.md` heat-medium reboiler row |
| Ambient design conditions | Per 04-25 facility ambient basis (TBD reference — DBM section to be cited; outdoor multilevel module installation assumed for adjacent mol-sieve packages) | TBD location |
| Winterization | Plenum heat and warm-air recirculation on TEG inlet cooler and lean-TEG cooler; glycol tracing per facility insulation philosophy | `4-25_Deepcut_DBM.md` SEC-06 equipment table; insulation references |
| Sour service / safety | Sour-service codes/standards per `OBJ-009`; flare/blowdown routing: contactor automated outlet blowdown to HP flare; flash-drum automated low-pressure blowdown to LP flare | `4-25_Deepcut_DBM.md` SEC-06; SEC-08 LP flare table |

## Construction

| Construction Attribute | Value | Source |
|---|---|---|
| Modularity | Shop-fabricated module `570-1 TEG Dehydration Module` | `4-25_Deepcut_DBM.md` module table |
| Installation | Outdoor module within 04-25 lease; aerial coolers above grade per facility convention | ASSUMPTION based on adjacent mol-sieve "outdoors on a multilevel module" and aerial-cooler equipment list; vendor to confirm |
| Foundations / supports / pipe-rack tie-ins | EPC Integrator scope (interface IFC-0B65AE534B — Structural / Foundations / Supports applies to this package) | `INTERFACE_REGISTER.csv`; `PACKAGE_REGISTER.csv` Responsibility Model |
| Vessel sizing (contactor reference) | 102 in ID x 60 ft S/S (basis only; final sparing TBD) | `4-25_Deepcut_DBM.md` SEC-06 |
| Lean/rich TEG exchanger | Bloc-welded plate exchanger, no polymer gaskets, bolted cover for cleaning | same |
| Reboiler type | BKU-type (heat-medium fired) | same |
| Tower internals | Structured packing in contactor (≥3 theoretical stages, FS ≤ 3.0 at design); inlet/outlet mesh and vane vertical-flow demisters | same |
| Filtration media | 5 micron particulate; activated carbon for slipstream | same |
| Materials | Sour-service-compatible materials selection per facility specs — specific material grades TBD; methyl mercaptan exposure consideration for TEG carbon-filter location is TBC | `4-25_Deepcut_DBM.md` SEC-06 TEG Open Items |
| Flange / drain rating | 300# ANSI for TEG drain service (TBC) | `4-25_Deepcut_DBM.md` SEC-06 drain table |
| Insulation / heat tracing | Per facility insulation specification (hot and cold insulation; glycol tracing referenced) | `4-25_Deepcut_DBM.md` insulation reference row |

### Package interface requirements (EPC integration scope — carried as datasheet evidence per `_CONTEXT.md` Notes)

Per `INTERFACE_REGISTER.csv` (Gate 7), the following X-column workbook interface facts apply to `PKG-068`. Each is the EPC Integrator's responsibility to design, install, terminate, and commission unless otherwise noted. The vendor package must provide tie-in points, terminations, and design data to allow the EPC to discharge these interfaces.

| Interface ID | Interface Type | Workbook Fact | Source |
|---|---|---|---|
| IFC-5242875251 | Process Piping | YES (interface applies) | `INTERFACE_REGISTER.csv` |
| IFC-8AFEC4B531 | Utility Piping | YES | same |
| IFC-9432C19C68 | Relief / Flare / Vent | YES | same |
| IFC-0CC21E6251 | Drain / Containment | YES | same |
| IFC-230C589A38 | Electrical Power | YES | same |
| IFC-A75CF67B27 | EHT | YES | same |
| IFC-BBADD0BD10 | Grounding / Bonding | YES | same |
| IFC-2A49A0639A | Area / Exterior Lighting | YES | same |
| IFC-ECD6D46F5A | I&C / Control Cabling | YES | same |
| IFC-A4653976DF | Building HVAC / Services | YES | same |
| IFC-AC3A79E94B | Fire & Gas / Safety Systems | YES | same |
| IFC-7286F463F5 | Maintenance Access | YES | same |
| IFC-0B65AE534B | Structural / Foundations / Supports | YES | same |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- Gate 7 PROJECT_DECOMP snapshot — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (this deliverable's row)
  - `PACKAGE_REGISTER.csv` (PKG-068 row, scope, tagged equipment, responsibility model)
  - `INTERFACE_REGISTER.csv` (13 interface facts for PKG-068)
  - `ARTIFACT_REGISTER.csv` (datasheet artifact catalog including ART-355EBDBAD7, ART-CCC3AE418E, ART-7CE5313EC5, and per-interface evidence artifacts)
  - `OBJECTIVE_REGISTER.csv` (OBJ-001, OBJ-003 through OBJ-010)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Process-Gas TEG Dehydration Basis (SEC-06); Heat-Medium (SEC-09); Utilities (SEC-08); module table; tagged equipment row 104
- `_Sources/26020-Package_Requirements.docx` — package heading 23 (BINARY .docx; not directly readable in current run; relevant requirements TBD pending text extraction). location TBD within document.
- `_Sources/DBM-Deepcut/Trace_Appendix.md` — referenced but not consulted in this pass

## Notes

- Mandatory Gate 5 EPC anchor deliverable per `_CONTEXT.md`. Interface facts are intentionally carried in this datasheet as evidence rather than being decomposed into standalone deliverables.
- All design values above are extracted from the 04-25 DBM. Vendor to verify against final detailed engineering. Unresolved items are recorded in `Guidance.md`'s Conflict Table.
