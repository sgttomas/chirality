# Specification — DEL-086-03 Construction Work Package (Flare Stack, Low Pressure)

> Normative content for the EPC Integrator Construction Work Package (CWP). Requirements are derived from locally accessible source slices in the project DBMs and the accepted PROJECT_DECOMP Gate-07 snapshot. Inferences are labeled **ASSUMPTION**; missing source-specific values are labeled `TBD`.

## Scope

### In scope

- Construction Work Package (CWP) defining how PKG-086 Flare Stack (Low Pressure) will be physically installed, built, inspected, turned over, and tied into the larger facility (`_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv row `DEL-086-03_construction-work-package`).
- Installation and tie-in workface plan for the LP flare element (piggy-back on the common HP/Cryo stack physically at 03-25 shared with 04-25) (DBM-Deepcut `4-25_Deepcut_DBM.md` line 2030-2031; DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` line 497).
- Construction interface and turnover checklist covering the eight package interface classes declared for PKG-086 (Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports) (INTERFACE_REGISTER.csv PKG-086 rows).
- Construction-side coverage of SOW-0091, SOW-0092, SOW-0093, SOW-0094 (OBJECTIVE_SCOPE_MAP.csv PKG-086 rows).

### Out of scope (carried by other PKG-086 deliverables)

- Package vendor engineering, design, fabrication, and equipment supply — DEL-086-04 (DELIVERABLE_REGISTER.csv).
- Vendor document register and turnover documentation — DEL-086-05.
- EPC vendor package review and acceptance — DEL-086-06.
- Package scope of work and package datasheet definition — DEL-086-01 and DEL-086-02.

## Requirements

> R-IDs are local to this deliverable. Each requirement cites the source slice from which it is derived.

| R-ID | Requirement | Source |
|---|---|---|
| R-CWP-01 | The CWP shall describe physical installation, build, inspection, turnover, and facility tie-in of PKG-086. | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv DEL-086-03 description |
| R-CWP-02 | Installation shall accommodate the LP flare element installed as a piggy-back element on the common HP/Cryo flare stack physically at 03-25 and shared with 04-25. | DBM-Deepcut line 2030, line 2031; DBM-Comp_and_Liquids line 497 |
| R-CWP-03 | LP relief header tie-ins shall be sized DN 500 / 20 in (508 mm) at the package interface unless overridden by detailed design. | DBM-Deepcut line 2029; DBM-Comp_and_Liquids line 499 |
| R-CWP-04 | The CWP shall provide for installation of the LP flare KO drum and its transfer/truck-out pump, with hydrocarbon liquids transferable to slop. | DBM-Deepcut line 2029; DBM-Comp_and_Liquids lines 499, 584 |
| R-CWP-05 | VRU-suction-to-LP-flare header tie-in shall be free-draining without traps and shall slope toward the LP flare knock-out. | DBM-Deepcut line 1787 |
| R-CWP-06 | The installation shall route LP flare services received from TEG regeneration, VRU, compressor seal pots, and (on Deepcut side) amine regeneration to the LP flare KO drum and onward to the LP stack element. | DBM-Comp_and_Liquids line 499; DBM-Deepcut line 2029 |
| R-CWP-07 | The CWP shall implement supplemental fuel gas supply to the LP flare stack such that any blended gas mixture directed to flare has LHV >= 20 MJ/Sm^3. | DBM-Deepcut line 2033 |
| R-CWP-08 | The CWP shall provide pilot, pilot proving, auto-ignition, and smokeless air-assist installation provisions for the LP element. | DBM-Deepcut line 2030, line 2031 |
| R-CWP-09 | The installation shall demonstrate flare radiation at grade meeting OGPFR Appendix 1, Schedule 1: <= 9 kW/m^2 inside the facility boundary blackened area and <= 5 kW/m^2 outside the facility boundary, including a 0.7888 kW/m^2 solar radiation allowance. | DBM-Deepcut lines 285-286, 2050, 2057 |
| R-CWP-10 | Smokeless performance acceptance shall target Ringelmann 1 at approximately 5% (TBC) of the emergency design case flare load. | DBM-Deepcut line 2031 |
| R-CWP-11 | HP flare headers outside heated buildings shall be electrically heat-traced and insulated for freeze protection except for PSV outlets that free-drain into the flare header. **ASSUMPTION:** the same freeze-protection rule applies to LP wet-service headers — confirm at detailed design (LP-specific statement: location TBD). | DBM-Deepcut line 2033 |
| R-CWP-12 | Construction interfaces shall be planned for the eight declared PKG-086 interface classes: Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports. | INTERFACE_REGISTER.csv PKG-086 rows |
| R-CWP-13 | The CWP shall include a construction interface and turnover checklist exit gate before package acceptance (DEL-086-06). | DELIVERABLE_REGISTER.csv DEL-086-03 (anticipated artifacts); DEL-086-06 (downstream EPC acceptance) |
| R-CWP-14 | LP-element-specific dimensions (LP element OD and final stack height) shall be confirmed before fabrication/erection planning is frozen. **TBD in source** — DBM records "LP stack OD remains TBD" / "LP element OD TBD". | DBM-Comp_and_Liquids line 499; DBM-Deepcut line 2031 |
| R-CWP-15 | LP flare stack pilot and purge gas rate shall be confirmed (source: "TBC"). | DBM-Deepcut line 1892 |
| R-CWP-16 | Staggered blowdown shall be considered during detailed engineering to limit the maximum simultaneous relief rate to the common HP/Cryo flare stack (LP element shares the stack structure). | DBM-Deepcut line 2046 |

## Standards

| Standard / Code | Use | Source slice |
|---|---|---|
| BCER Oil and Gas Processing Facility Regulation (OGPFR), Appendix 1, Schedule 1, Sections 2 and 7(4) | Flare thermal radiation limits at grade | DBM-Deepcut lines 285-286, 2050 |
| SA-106 (LP flare piping material) | LP flare header material basis (324 mm reference example) | DBM-Deepcut line 2042 (location TBD for full applicability statement) |
| Aspen Flare System Analyzer | Header sizing/backpressure modeling tool referenced in DBM | DBM-Deepcut line 2021 |
| Detailed welding, NDE, hydrotest, painting, insulation, scaffolding, and lifting standards | Construction execution | `location TBD` — not enumerated in accessible source slices |

## Verification

| R-ID | Verification approach |
|---|---|
| R-CWP-01..R-CWP-02 | Document review of CWP narrative against DELIVERABLE_REGISTER and DBM stack architecture. |
| R-CWP-03..R-CWP-06 | Isometric/P&ID/3D model walk-down against header size, KO drum tag, slope, and service-list source slices. |
| R-CWP-07..R-CWP-08, R-CWP-15 | Pilot light test, pilot proving signal test, auto-ignition test, fuel gas LHV verification at commissioning. |
| R-CWP-09..R-CWP-10 | Radiation calculation re-check against installed geometry; smokeless visual observation at design test load (Ringelmann 1 target). |
| R-CWP-11 | Heat-tracing/insulation inspection record; confirm LP wet-header coverage (assumption to resolve). |
| R-CWP-12..R-CWP-13 | Interface punch-list closure and turnover checklist sign-off prior to DEL-086-06 acceptance. |
| R-CWP-14 | Dimensional check vs vendor-issued LP element drawing once OD/height frozen. |
| R-CWP-16 | Detailed-engineering blowdown logic review evidence cited in CWP. |

## Documentation

The CWP shall produce / reference, at minimum:

- Construction work package (narrative + index) — `_CONTEXT.md` Anticipated Artifacts.
- Installation and tie-in workface plan — `_CONTEXT.md` Anticipated Artifacts.
- Construction interface and turnover checklist — `_CONTEXT.md` Anticipated Artifacts; INTERFACE_REGISTER.csv PKG-086 rows.
- Discipline drawings sufficient to install LP element, KO drum, pilot/ignition/air-assist, tie-ins (drawing register **TBD** at detailed design).
- Weld map, NDE log, hydrotest pack, pressure-test record — **ASSUMPTION** (typical EPC content; explicit enumeration: location TBD).
- Mechanical completion certificates, instrument loop check sheets, F&G loop tests — **ASSUMPTION** (typical; location TBD).
- Punch-list closure record feeding DEL-086-06 (EPC Vendor Package Review and Acceptance).
