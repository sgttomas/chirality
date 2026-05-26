# Datasheet — DEL-086-03 Construction Work Package (Flare Stack, Low Pressure)

> Descriptive datasheet for the Construction Work Package (CWP) of PKG-086 Flare Stack (Low Pressure). Values cite the locally accessible authoritative DBM source slices; missing source-specific values are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-086-03_construction-work-package | `_CONTEXT.md` Identity |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` Identity |
| Deliverable Type | EPC Construction Work Package | `_CONTEXT.md` Identity |
| Parent Package ID | PKG-086 | `_CONTEXT.md` Identity |
| Parent Workbook Row | 59 | `_CONTEXT.md` Source Reference |
| Package Name | Flare Stack (Low Pressure) | `_CONTEXT.md` Identity |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Responsible Party | EPC Integrator | `_CONTEXT.md` Identity |
| Mandatory EPC anchor? | Yes (Gate 5 DEC-013) | PROJECT_DECOMP.md line 205 |

## Attributes (Construction Work Package contents)

| Attribute | Value | Source |
|---|---|---|
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv row DEL-086-03 |
| Package function in facility | LP relief disposal element ("piggy-back" on common HP/Cryo flare stack physically at 03-25, shared with 04-25) | DBM-Deepcut `4-25_Deepcut_DBM.md` §Flare and Blowdown (line 2031); DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` lines 56, 497, 499 |
| Covered scope items (SOW) | SOW-0091, SOW-0092, SOW-0093, SOW-0094 | `_CONTEXT.md` Covers Scope Items |
| Supported objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` Supports Objectives |

## Conditions (installation/operating envelope referenced by construction)

| Condition | Value | Source |
|---|---|---|
| LP flare service | Receives TEG regeneration, VRU, and compressor seal-pot services; amine regeneration also routed to LP flare on Deepcut side | DBM-Comp_and_Liquids line 499; DBM-Deepcut line 2029 |
| LP relief header size | 508 mm / 20 in | DBM-Comp_and_Liquids line 499; DBM-Deepcut line 2029 |
| LP flare KO drum (Deepcut basis) | V-3900-1 with KO drum pump P-3900-1 and truck-out provision | DBM-Deepcut line 2029 |
| LP flare KO drum (Comp/Liquids basis) | V-3900-2 with pump P-3900-2 to slop | DBM-Comp_and_Liquids line 499 |
| LP stack OD (element on common stack) | TBD (source: "LP stack OD remains TBD" / "LP element OD TBD") | DBM-Comp_and_Liquids line 499; DBM-Deepcut line 2031 |
| LP stack pilot and purge gas rate | TBC | DBM-Deepcut line 1892 |
| LP flare radiation thermal limits at grade | Inside boundary <= 9 kW/m^2; outside boundary <= 5 kW/m^2 (OGPFR App.1 Sched.1 Sec.2) plus 0.7888 kW/m^2 solar allowance | DBM-Deepcut lines 285-286, 2050, 2057 |
| Smokeless operation criterion | Ringelmann 1 at approximately 5% (TBC) of emergency design case flare loads | DBM-Deepcut line 2031 |
| Supplemental fuel gas | Required to LP flare stack for complete combustion; blended gas to flare shall have LHV >= 20 MJ/Sm^3 | DBM-Deepcut line 2033 |
| LP element drive | Air blower for smokeless operation | DBM-Deepcut line 2031 |
| Heat tracing | HP flare headers outside heated buildings to be electrically heat traced and insulated (except PSV outlets that free-drain). Equivalent LP heat-tracing scope: ASSUMPTION — apply same rule to LP wet relief headers; explicit LP statement not located in accessible slices (location TBD) | DBM-Deepcut line 2033 |
| Header drainage | VRU suction header to LP flare to free-drain without traps and slope toward LP flare knock-out | DBM-Deepcut line 1787 |

## Construction (installation/turnover scope elements)

| Element | Construction-relevant note | Source |
|---|---|---|
| Foundation / structural support | Common HP/Cryo + LP piggy-back stack physically at 03-25, shared with 04-25; foundation, anchorage, and seismic design TBD (location TBD in accessible slices) | DBM-Deepcut line 2030; DBM-Comp_and_Liquids line 497 |
| Stack erection | Common HP/Cryo stack element 660 mm OD x 200 ft tall (TBC); LP element piggy-backs on the same structure; lift plan/crane plan TBD | DBM-Deepcut line 2030, line 2031 |
| Underground / above-grade piping | LP relief header 508 mm (20 in); routes to LP flare KO drum; tie-ins to TEG regen, VRU (incl. V-ball bypass), compressor seal pots, amine regen | DBM-Deepcut lines 1787, 2029; DBM-Comp_and_Liquids line 499 |
| KO drum installation | LP flare KO drum (V-3900-1 / V-3900-2 — see Conflict Table) with transfer pump and truck-out connections | DBM-Deepcut line 2029; DBM-Comp_and_Liquids lines 499, 584 |
| Pilot, purge, ignition, instrumentation | Pilot, pilot proving, auto-ignition, smokeless air-assist, supplemental fuel; pilot/purge rate TBC | DBM-Deepcut lines 2030, 2031, 1892, 2033 |
| Electrical / I&C tie-ins | LP flare pilot/ignition power, smokeless-air blower power, KO drum pump power, instrumentation/F&G; cable schedule and exact loads TBD | INTERFACE_REGISTER.csv PKG-086 rows (Electrical Power, Grounding/Bonding, I&C/Control Cabling) |
| Fire & Gas / Safety | F&G detection and shutdown interfaces at LP stack and KO area | INTERFACE_REGISTER.csv PKG-086 Fire & Gas / Safety Systems row |
| Tie-ins to facility | Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C; F&G; Structural/Foundations/Supports | INTERFACE_REGISTER.csv PKG-086 rows |
| Inspection / NDE scope | Per applicable code basis for relief piping and stack structure — specific class/NDE percentages TBD | (location TBD) |
| Commissioning checks | Pilot light/proving test, smokeless air-assist proof, KO drum level/pump function, header drainage verification, F&G loop tests | DBM-Deepcut lines 2030, 2031, 1787; ASSUMPTION on test list — confirm against final commissioning procedures |
| Turnover deliverables | Mechanical completion certificates, weld/NDE records, instrument loop check sheets, KO drum/pump performance records, redlines | ASSUMPTION (typical EPC turnover content; not literally enumerated in accessible source slices — location TBD) |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (DELIVERABLE_REGISTER.csv, INTERFACE_REGISTER.csv, OBJECTIVE_SCOPE_MAP.csv, PROJECT_DECOMP.md)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (LP flare basis, radiation criteria, header sizes, stack basis)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (LP service split, KO drum, shared interface)
- `_Sources/26020-Package_Requirements.docx` package heading 39 (NOT locally machine-readable as text; source slice location TBD until extracted)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 59 (NOT locally machine-readable as text; source slice location TBD until extracted)
