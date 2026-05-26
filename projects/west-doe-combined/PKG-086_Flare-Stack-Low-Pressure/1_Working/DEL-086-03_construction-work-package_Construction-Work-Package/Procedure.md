# Procedure — DEL-086-03 Construction Work Package (Flare Stack, Low Pressure)

> Operational procedure for **producing** the Construction Work Package (CWP) deliverable artifact and the supporting installation/tie-in workface plan and construction interface and turnover checklist. The deliverable is a document set; the produce-the-document procedure is primary, with the use-the-document procedure (install/turnover) summarized in Step 4-6.

## Purpose

Produce the CWP artifact set (CWP narrative, installation and tie-in workface plan, construction interface and turnover checklist) that meets the requirements in `Specification.md` and is grounded in the source slices identified in `Datasheet.md`.

## Prerequisites

- `_CONTEXT.md` present and current (DeliverableID, Package, Discipline, Anticipated Artifacts).
- `_REFERENCES.md` resolved against the accepted GATE-07 PROJECT_DECOMP snapshot; source slices in DBM-Deepcut and DBM-Comp_and_Liquids accessible. (`_REFERENCES.md`)
- DBM source slices read for: LP flare service list, header size, KO drum tag, stack basis, radiation limits, smokeless target, supplemental fuel rule, freeze protection, header drainage rule, pilot/purge basis. (Datasheet "References" section)
- Declared interface set from INTERFACE_REGISTER.csv for PKG-086 (eight interface classes).
- Pre-conditions on declared upstream deliverables:
  - Sibling DEL-086-01 (Scope of Work) — directional context.
  - Sibling DEL-086-02 (Package Datasheet) — vendor handoff basis; LP element dimensional data flows from this datasheet once frozen.
  - PKG-085 (HP) construction package coordination — shared stack; joint sequencing required.
- Required references for closure: extracted text slices of `26020-Package_Requirements.docx` heading 39 and `26020-Packages_Interfaces_4_export.xlsx` row 59 (currently TBD, see Guidance Conflict C-3).

## Steps

### Phase A — Produce the CWP artifact set

1. **Confirm scope and exclusions** against `Specification.md` Scope; tag any out-of-scope items as carried by DEL-086-01, -02, -04, -05, -06.
2. **Lift the requirement set** (R-CWP-01..R-CWP-16) into the CWP narrative table of contents; map each requirement to a CWP section.
3. **Populate construction interface coverage** for each of the eight PKG-086 interface classes (INTERFACE_REGISTER.csv) with: interface description, responsible discipline, isolation/tie-in approach, witness/inspection hold points.
4. **Build the installation and tie-in workface plan**:
   - LP element installation on the common HP/Cryo stack (coordinate with PKG-085).
   - LP relief header (DN 500 / 20 in) routing and tie-ins.
   - LP KO drum (V-3900-x — resolve C-1) and transfer/truck-out pump installation.
   - VRU-suction-to-flare V-ball bypass installation with free-drain slope toward LP KO.
   - Pilot, pilot proving, auto-ignition, smokeless air-assist installation.
   - Supplemental fuel-gas tie-in and metering.
   - Electrical/grounding/F&G/I&C cable installation per interface IFCs.
5. **Build the construction interface and turnover checklist** with one section per IFC ID for PKG-086 plus mechanical completion, hydrotest, NDE, instrument loop check, F&G loop test, commissioning walkdown, and punch-list close-out.
6. **Mark all TBDs explicitly**: LP element OD, final LP stack height contribution, LP pilot/purge gas rate, weld/NDE class enumeration, LP-specific heat-trace authority, KO drum tag resolution.
7. **Cross-check against Datasheet** for consistent values (header size, KO drum tag once resolved, radiation limits, fuel-gas LHV, Ringelmann smokeless target).
8. **Cross-check against Guidance Conflict Table** to ensure every open conflict is surfaced (not silently resolved) in the CWP narrative.

### Phase B — Use the CWP for installation (summary)

9. Execute the workface plan in coordination with PKG-085 (joint lift plan for the common stack).
10. Run inspection holds for: weld/NDE (basis TBD), hydrotest, instrument loop, F&G loop, heat-tracing continuity, header slope, pilot/ignition function, smokeless blower function.
11. Demonstrate radiation compliance (<= 9 kW/m^2 inside boundary; <= 5 kW/m^2 outside; OGPFR App. 1 Sched. 1) and smokeless performance (Ringelmann 1 at ~5% emergency case, TBC) at commissioning.
12. Close construction interface and turnover checklist; hand off to DEL-086-06 (EPC Vendor Package Review and Acceptance).

## Verification

| Check | What it confirms | Tied to R-ID |
|---|---|---|
| Document review of CWP TOC vs Specification | All R-CWP-01..R-CWP-16 mapped to a CWP section | All |
| Isometric/P&ID walk-down record | LP header size, KO drum tag, slope, services list match Datasheet/Spec | R-CWP-03..R-CWP-06 |
| Heat-trace and insulation inspection record | Freeze protection on LP wet headers per Spec R-CWP-11 (assumption pending C-2) | R-CWP-11 |
| Pilot test, pilot proving, auto-ignition test | LP element ignition system functions per Spec | R-CWP-08, R-CWP-15 |
| Fuel-gas LHV verification | Blended gas to flare >= 20 MJ/Sm^3 | R-CWP-07 |
| Radiation calculation re-check | Installed geometry meets OGPFR limits plus solar allowance | R-CWP-09 |
| Smokeless visual observation at test load | Ringelmann 1 at ~5% emergency design case (TBC) | R-CWP-10 |
| Interface punch-list close-out per IFC ID | All eight PKG-086 interfaces closed | R-CWP-12 |
| Turnover checklist sign-off | Pre-acceptance gate before DEL-086-06 | R-CWP-13 |
| LP element dimensional check | OD and height match vendor-issued data once frozen | R-CWP-14 |
| Blowdown logic test record | Staggered blowdown logic per detailed engineering | R-CWP-16 |

## Records

- CWP narrative document (issued for construction).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist (one row per IFC + completion gate).
- Weld map, NDE log, hydrotest pack, pressure-test record (typical EPC turnover content — explicit list TBD; ASSUMPTION).
- Mechanical completion certificates, instrument loop check sheets, F&G loop test records (typical — TBD/ASSUMPTION).
- Pilot light/proving and auto-ignition test record; smokeless air-assist test record.
- Radiation re-check report.
- Punch-list closure record fed forward to DEL-086-06.
- Conflict-resolution memo for items C-1, C-2, C-3 from `Guidance.md` Conflict Table.
