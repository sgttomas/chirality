# Procedure: DEL-100-03_construction-work-package — Construction Work Package

## Purpose

Produce the Construction Work Package for PKG-100 (Hydrogen Peroxide Sweetening Unit): the construction-facing plan that describes how the vendor-supplied H2O2 sweetening package and self-framing building will be physically installed, built, inspected, turned over, and tied into the 03-25 facility, with all PKG-100 interfaces carried into the workface plan and turnover checklist.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot: `GATE-07_Final_Published_2026-05-24`.
- DEL-100-01_scope-of-work (EPC Scope of Work for PKG-100): no declared upstream in `_DEPENDENCIES.md`; treat as context-only until human-declared.
- DEL-100-02_package-datasheet (Package Datasheet): no declared upstream in `_DEPENDENCIES.md`; treat as context-only until human-declared.
- DEL-100-04_vendor-engineered-equipment-package: needed for vendor engineering, anchor loads, electrical loads, dynamic data, materials, P&IDs, and GA drawings — TBC; treat as required vendor input.
- Locally accessible reference materials in `_REFERENCES.md`, including DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md.
- Workbook Packages row 63 facts (interfaces, discipline, WBS, CoA tracking number).
- SCOPE_LEDGER.csv SOW-0107 through SOW-0110 extractions.

(Note: `_DEPENDENCIES.md` lists no declared upstream/downstream dependencies. The dependencies above are necessary-input ASSUMPTIONS pending human declaration via `TASK + dependency-extract`.)

## Steps

1. **Establish identity.** Populate the work package header with PKG-100, Hydrogen Peroxide Sweetening Unit, WBS 03, CoA 26020-03-27-001, Mechanical, Workbook Packages row 63.
2. **Carry the responsibility split.** Insert a responsibility matrix that records: Package Vendor — engineering/design/documentation/equipment; EPC Integrator — integration/interfaces/tie-ins/constructability/coordination; Field construction contractor — TBD pending 03-25 assignment (see Guidance Conflict Table CFL-100-03-01).
3. **List vendor-supplied scope verbatim.** Carry SOW-0108 (basic scope) and SOW-0109 (major included equipment) into the package as the equipment list the contractor will offload, set, and connect.
4. **List "by others" / EPC-Integrator construction scope verbatim.** Carry SOW-0110 "by others" items as construction scope sections: interconnecting piping; DCS integration tie-ins; foundations (package + self-framing building); electrical supply to MCC.
5. **Foundations workface plan.** Document foundation design dependency on vendor anchor loads and dynamic data (TBC). Include excavation, rebar, pours, cure, anchor-bolt template setting, and inspection holdpoints. Mark detailed quantities/coordinates `TBD`.
6. **Building erection workface plan.** Document the self-framing building (SOW-0109) erection — sequencing, crane lifts, anchorage to foundation, wall/roof closure, weather protection for winter erection (consistent with -40 °C ambient design). Mark vendor drawing references `location TBD`.
7. **Module/skid offloading and setting plan.** Plan offloading of H2O2 reactors, static mixer, H2O2 pumps, 400 BBL H2O2 tank, and additional PFD equipment; rigging plan; setting tolerances per vendor GA (location TBD).
8. **Mechanical hookup workface plan.** Process piping tie-ins (sour water in to static mixer; treated water out to produced-water tanks); utility piping; relief/flare/vent routing; drain/containment routing. Cite each PKG-100 interface from INTERFACE_REGISTER.csv.
9. **Electrical hookup workface plan.** 600V MCC feeder pulls and terminations to 575V / 3PH / 60 Hz motors (DOL or VFD start per package detail TBC); local H-O-A or On-Off control station adjacent to each motor, hard-wired back to MCC starter circuit by the field construction contractor (DBM-Comp_and_Liquids SEC-12). Grounding/bonding per facility grounding plan. EHT per insulation/EHT plan (winterization).
10. **Lighting / building services / HVAC plan.** Area/exterior lighting; building HVAC and services for the self-framing building; potable/septic provisions if applicable.
11. **I&C / control cabling and DCS integration plan.** Home-run cabling from package to facility DCS marshalling; terminations; loop checks; SAT scope. DCS integration is "by others" relative to the vendor package per SOW-0110, so coordinate with the controls/I&C deliverable owner.
12. **Fire & gas / safety systems plan.** Fire/gas detection devices in and around the package and building; alarm and shutdown interface wiring to facility F&G; sour-service handling per OBJ-009.
13. **Maintenance access plan.** Access for pump maintenance, reactor servicing, tank inspection, building access, and crane lift requirements; carry from interface IFC-FC62996C71.
14. **Structural / supports plan.** Pipe supports, equipment supports, platforms, and grating in accordance with workbook interface fact IFC-B76BAF7A9C.
15. **Construction interface checklist.** Build the checklist with one row per PKG-100 interface (13 interfaces). Each row cites the IFC-* ID, source fact, action, and verification.
16. **Inspection and turnover register.** List the inspection and turnover records (e.g., foundation pour record, anchor torque record, cable test, loop check, hydrotest, energization, F&G commissioning, mechanical run-in). Final form templates `TBD`.
17. **Open input / TBD register.** List: pump capacity TBC; package design conditions TBC; vendor design of pumps/reactors/static mixer; DCS integration detail; foundation design (pending vendor loads); MCC loads; standards clauses (location TBD per Guidance Conflict Table CFL-100-03-03); field contractor identity (CFL-100-03-01); building erection party (Guidance Trade-offs).
18. **Handoff record (OBJ-010).** Index the items required for handoff: sparing list, isolation list, winterization (EHT, building heat, drain heat trace), vendor documents (linked to DEL-100-05), commissioning records, turnover punchlist, and closure evidence for open items.

## Verification

| Check | Method |
|---|---|
| Identity matches Gate 7 and workbook row 63. | Compare against DELIVERABLE_REGISTER.csv DEL-100-03 and PACKAGE_REGISTER.csv PKG-100. |
| All 13 PKG-100 interfaces appear in the construction interface checklist. | Cross-check checklist against INTERFACE_REGISTER.csv rows for PKG-100. |
| Vendor / EPC-Integrator / field-contractor responsibility matrix present. | Document review. |
| SOW-0107 through SOW-0110 facts carried verbatim into the package. | Source diff against SCOPE_LEDGER.csv. |
| Self-framing building erection workface section present. | Document review against SOW-0109. |
| Open-item register lists every TBC/TBD item identified above. | Register review. |
| Inspection and turnover records named for foundations, structural, mechanical, electrical, I&C, F&G, and commissioning. | Register review. |

## Records

- Construction Work Package document (this deliverable's primary artifact).
- Installation and tie-in workface plan (artifact ART-* TBD; named in DELIVERABLE_REGISTER.csv anticipated artifacts).
- Construction interface and turnover checklist (artifact ART-* TBD; named in DELIVERABLE_REGISTER.csv anticipated artifacts).
- Responsibility matrix.
- Open-item / TBD register.
- Inspection and turnover record index (final forms TBD).
- Foundation, structural, mechanical, electrical, I&C, F&G, and commissioning records produced during execution (forms TBD).
- Cross-reference index to DEL-100-04 (vendor equipment package) and DEL-100-05 (vendor document turnover package).
