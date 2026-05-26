# Specification — DEL-063-03 Construction Work Package (Tanks, DSO (API 650))

> Normative requirements for the Construction Work Package (CWP) for `PKG-063 Tanks, DSO (API 650)`. Primary accessible source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (caustic mercaptan treating + DSO service slice). The package-requirements DOCX (`_Sources/26020-Package_Requirements.docx` heading 18) is cited by `_CONTEXT.md` but its slice is not transcribed into `_REFERENCES.md` — content that depends solely on that slice is `TBD`. Inferred requirements are labelled `ASSUMPTION`.

## Scope

### In Scope

- Define how the DSO tank package (API 650) will be physically installed, built, inspected, turned over, and tied into the larger facility, per `_CONTEXT.md` Scope.
- Workface-level installation plan for: foundation construction (ringwall or pile-supported, TBD); tank erection (field-erected API 650 work); welding/NDE; surface preparation, internal coating, and external insulation; tie-in piping (DSO inlet, DSO transfer to DSO pumps 2 × 100 %, drain, vent/blanket if applicable); electrical power, lighting, EHT; instrumentation hook-up and loop verification; fire & gas device installation; structural platform/stairs/manway access; grounding/bonding; spill containment finishing.
- Construction interface management and turnover documentation across EPC Integrator and the tank/process-package vendors.

### Out of Scope (boundary clarifications)

- Process design of the upstream caustic mercaptan treating package and definition of DSO service conditions (handled by upstream package basis — `DEL-063-01_scope-of-work`, `DEL-063-02_package-datasheet` analogues; `TBD`).
- Vendor-supplied tank engineering itself (e.g. detailed plate design, weld procedures, internal coating selection) is delivered by the vendor; the CWP receives those artifacts as inputs.
- Operations of the DSO tank post-handover (commissioning handles process bring-up).

## Requirements

### R-CWP-1 — Package Identification

The CWP MUST identify the package by `PKG-063 Tanks, DSO (API 650)` and reference the GATE-07 decomposition snapshot. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.)

### R-CWP-2 — Construction Scope Coverage

The CWP MUST cover scope items `SOW-0209`, `SOW-0210`, `SOW-0211`, `SOW-0212` and trace its work breakdown back to these IDs. (Source: `_CONTEXT.md` Covers Scope Items; `DELIVERABLE_REGISTER.csv`.)

### R-CWP-3 — Tank Construction Standard

The CWP MUST execute tank construction to API 650 (Modified atmospheric — ASSUMPTION by analogy with the produced-water tank basis line 421). The specific Modified clauses, plate basis, and shell course details are inputs from the vendor/EPC tank datasheet (TBD; not in accessible `_REFERENCES.md`). (Source: `_CONTEXT.md` PackageName; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 421; ASSUMPTION.)

### R-CWP-4 — Foundation and Setting

The CWP MUST include a foundation plan (ringwall, slab, or pile-supported — TBD pending geotechnical report; DBM line 700 requires foundations be designed to the final geotechnical report, equipment loads, snow/wind/seismic, frost protection, vibration, settlement, and maintenance access). Anchorage MUST be sized for tank-applicable wind/seismic/sloshing per API 650 Appendix E (ASSUMPTION). (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 700.)

### R-CWP-5 — Lifting, Handling, and Transport

The CWP MUST incorporate the vendor's lifting study (analogue: `MEC-018` per sibling EPC CWPs) and define rigging plans, crane picks, load paths, plate handling, and laydown sequencing. Field-erected tanks substitute plate handling and shell-jacking sequences for single-skid lifts. (ASSUMPTION on artifact ID equivalence; precedent: sibling `DEL-049-03`.)

### R-CWP-6 — Tank Welding and NDE

The CWP MUST execute tank welding per API 650 (shell vertical and horizontal seams, bottom plate, roof) using project-approved WPSs and welders; NDE per API 650 (radiography of shell seams, vacuum-box of bottom seams, hydrostatic test in Section 7) MUST be planned and recorded. Project welding/NDE specification is `TBD` (not in `_REFERENCES.md`); base requirements come from API 650 itself.

### R-CWP-7 — Surface Preparation, Internal Coating, External Insulation, EHT

The CWP MUST execute surface preparation, internal coating (selection TBD for DSO service; produced-water tank precedent is Devchem 253 per DBM line 421 — DSO sulphur/hydrocarbon compatibility requires separate confirmation), external insulation, and electric heat tracing consistent with the −40 °C site basis (DBM line 145). (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 145, 256, 421.)

### R-CWP-8 — Pressure Testing and Cleaning

The CWP MUST include a hydrostatic test plan per API 650 Section 7 (water fill, settlement survey, foundation check) plus piping pressure tests on tie-in piping. Flushing/cleaning/drying of tie-in piping MUST precede service introduction. Test pressures, mediums, hold times, and acceptance criteria for non-API 650 piping = TBD (project pressure-test spec not in `_REFERENCES.md`).

### R-CWP-9 — Piping Tie-Ins

The CWP MUST plan and schedule DSO inlet, DSO transfer (to DSO pumps 2 × 100 % — DBM line 577), drain, vent/blanket (if applicable), and instrument tap tie-ins. Drain headers MUST honour the 300# ANSI minimum rating where the drain connects to the hydrocarbon liquid drain system (DBM line 493). (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 493, 577.)

### R-CWP-10 — Electrical Installation

The CWP MUST install power for the DSO pumps and tank-side electrical loads (mixer if any — TBD; instrumentation; EHT; lighting; receptacles). Cable schedules, routing, terminations, and energization MUST follow the project electrical installation set (analogue artifact IDs per sibling CWPs: `ELE-014/015/016/027/028/029/030`).

### R-CWP-11 — Lighting, EHT, Grounding, Cathodic Protection

The CWP MUST include area lighting around the tank, EHT for freeze-prone piping and tank-side instrument lines (basis: DBM line 145 and line 770 — heat tracing supports winterization, freeze protection, tank and drain requirements, and process package needs), API 650 tank grounding (lightning/static), and a cathodic protection decision for buried piping and the tank bottom (TBD). (Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 145, 770.)

### R-CWP-12 — Instrumentation Installation and Loop Verification

The CWP MUST install level (high/low alarms and shutdowns), temperature, pressure (blanket, if applicable), and any analytical instrumentation; terminate; and run loops back to the facility control system. Loop check, cause-and-effect verification, and SIS function testing (if applicable) MUST be evidenced.

### R-CWP-13 — Fire & Gas / Safety

The CWP MUST install and commission F&G devices per the project F&G study; the DBM line 838 lists "tankage" and "caustic/DSO systems" among the areas governing F&G detector placement (LEL, H2S, methyl mercaptan, fire). Detector quantity, set points, and placement are project-design outputs (TBD pending detailed design per DBM).

### R-CWP-14 — Structural and Access

The CWP MUST install platform, stairs, manway access, and any external pipe supports per the vendor structural set; access compliance MUST follow project structural-access standards (TBD).

### R-CWP-15 — Spill Containment and Drainage Finish

The CWP MUST complete bunded containment, drain interceptors, and spill-routing connections per project civil/environmental design (TBD bund volume sizing; default ASSUMPTION: containment sized to 110 % of largest tank within the bund per common code practice).

### R-CWP-16 — Inspection and Test

The CWP MUST incorporate an ITP, MTRs, inspection-release certificate, and manufacturing record book (analogue artifact IDs per sibling CWPs: `QLT-003 / QLT-013 / QLT-020 / QLT-021`) and overlay site inspections (foundation acceptance, plate receipt, shell weld inspection, bottom vacuum box, hydrostatic test, settlement survey, instrument loop checks, F&G functional tests, energization).

### R-CWP-17 — Pressure Equipment Registration

If jurisdictional pressure equipment registration applies to the DSO tank or to associated pressurized piping/equipment, the CWP MUST integrate `REG-022 Pressure Equipment Registration Package` (or equivalent) activities into the site sequence prior to commissioning. Atmospheric API 650 tanks may be outside pressure-vessel jurisdictional scope — confirmation `TBD`.

### R-CWP-18 — FAT to SAT Continuity

The CWP MUST consume vendor FAT records (where applicable — many field-erected API 650 tanks have no separable FAT) and define SAT activities for instrumentation, F&G, and electrical loops at site.

### R-CWP-19 — Mechanical Completion and Turnover

The CWP MUST produce a construction interface and turnover checklist that drives mechanical completion certification of the DSO tank package and hands the package over to commissioning. Project MC procedure = TBD.

### R-CWP-20 — Spares, IOM, As-Builts

The CWP MUST ensure vendor spares, IOM, and tank/piping/electrical/instrument as-built drawings are received and registered at turnover.

## Standards

| Standard | Applies To | Location |
|---|---|---|
| API 650 (Modified) | DSO tank shell, bottom, roof, foundation interface, hydrostatic test, anchorage | `_CONTEXT.md` PackageName; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 421 (produced-water tank precedent); specific Modified clauses TBD |
| Project welding & NDE specifications | Tank shell welds and tie-in piping | TBD — not in `_REFERENCES.md` |
| Project pressure-test specification | Tie-in piping hydrotest (non-API 650) | TBD — not in `_REFERENCES.md` |
| Jurisdictional pressure equipment registration regime | Pressurized piping/equipment associated with DSO service | TBD — atmospheric tank may be out of scope; confirm |
| Site HSE / hot-work / confined-space / lift-plan procedures | All site construction activities | TBD — not in `_REFERENCES.md` |
| Coating specification governing DSO/sulphur service | Tank internals | TBD — Devchem 253 is the produced-water analogue (DBM lines 256, 421); DSO compatibility unproven |
| API 2350 or equivalent overfill protection standard (ASSUMPTION) | Tank overfill protection instrumentation | TBD — not cited in accessible source |

## Verification

| Requirement | Verification |
|---|---|
| R-CWP-1, R-CWP-2 | Trace matrix from CWP work breakdown to `SOW-0209`–`SOW-0212` and to `PKG-063` |
| R-CWP-3 | API 650 nameplate; vendor design documentation accepted |
| R-CWP-4 | Geotechnical report referenced; foundation as-built and survey; anchor-bolt survey |
| R-CWP-5 | Approved lift/erection plan; rigging inspection; plate handling records |
| R-CWP-6 | Weld map; radiograph reports; vacuum-box bottom test; weld inspection records |
| R-CWP-7 | Surface-prep DFT records; coating holiday-test; insulation installation inspection; EHT continuity |
| R-CWP-8 | API 650 hydrostatic test record with settlement survey; piping hydrotest packs |
| R-CWP-9 | Tie-in punch-list closure; weld map closure on tie-in piping |
| R-CWP-10 | Megger/continuity; energization checklist |
| R-CWP-11 | Lighting illumination survey; EHT continuity and circuit test; tank grounding resistance test; CP commissioning record if installed |
| R-CWP-12 | Loop check sheets; cause-and-effect verification |
| R-CWP-13 | F&G device functional tests |
| R-CWP-14 | Structural inspection; bolt torque; access walk-down |
| R-CWP-15 | Bund volume verification; drain functional test |
| R-CWP-16 | ITP sign-offs; inspection release certificate |
| R-CWP-17 | Pressure equipment registration acceptance evidence (if applicable) |
| R-CWP-18 | SAT records (instrumentation, F&G, electrical loops) |
| R-CWP-19 | MC certificate; turnover checklist signed |
| R-CWP-20 | Spares received register; IOM filed; as-builts issued |

## Documentation

The CWP deliverable bundle consists of:

- This Specification (`Specification.md`).
- `Datasheet.md` — package identification, attributes, conditions, interface applicability.
- `Guidance.md` — principles, considerations, trade-offs.
- `Procedure.md` — workface execution sequence and turnover.
- The three anticipated artifacts in `_CONTEXT.md`: Construction work package, Installation and tie-in workface plan, Construction interface and turnover checklist.
