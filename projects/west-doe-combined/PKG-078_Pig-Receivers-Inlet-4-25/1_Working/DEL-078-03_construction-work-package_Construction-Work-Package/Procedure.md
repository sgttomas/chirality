# Procedure: Construction Work Package

## Purpose

This Procedure describes the sequence of activities required to produce, execute, and close out the Construction Work Package (CWP) for `PKG-078` Pig Receivers (Inlet) 4-25, covering both (a) the EPC Integrator drafting and issuance of the CWP package and (b) the field execution and turnover steps that the CWP governs. It is the operational complement to `Specification.md` and `Guidance.md` for this deliverable.

## Prerequisites

| Item | Required for |
|---|---|
| Accepted upstream PROJECT_DECOMP snapshot `GATE-07_Final_Published_2026-05-24` | Drafting authority and source references |
| `DEL-078-01_scope-of-work` issued | Scope baseline for CWP boundary |
| `DEL-078-02_package-datasheet` issued | Technical handoff data feeding CWP equipment-context |
| Vendor package design (`DEL-078-04_vendor-engineered-equipment-package`) sufficiently advanced to confirm tag list, skid geometry, and HIPPS configuration | CWP construction sequencing, interface drawings, and turnover checklist |
| Project piping specification (sour-service class) issued for construction | R-08, R-09 acceptance |
| Project EHT design issued for construction | R-11 acceptance |
| Project I&C wiring/loop design issued for construction; DCS-integration responsibility confirmed | R-12 acceptance |
| Foundation IFC drawings issued (EPC civil scope, "by others" per SOW-0164) | R-02 acceptance |
| Geotechnical report final (per DBM SEC-11 basis) - status TBD | Foundation acceptance |
| HIPPS SIL allocation / proof-test interval from detailed engineering - status TBD | R-07 acceptance |
| Set pressure / sizing for HP flare vent connection - status TBD | R-06 acceptance |

Declared upstream dependencies in `_DEPENDENCIES.md`: none declared during PREPARATION (`_DEPENDENCIES.md`). Treat the above prerequisites as practical inputs the CWP author must confirm or mark TBD.

## Steps

### A. CWP drafting and issuance (EPC Integrator engineering)

1. Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `SCOPE_LEDGER.csv` rows `SOW-0161`-`SOW-0164`, `PACKAGE_REGISTER.csv` row `PKG-078`, and `INTERFACE_REGISTER.csv` rows for `PKG-078` to baseline the CWP scope and interfaces.
2. Read `4-25_Deepcut_DBM.md` slices for inlet pig receiver (line 585), Inlet Pipeline Pressure table (line 626), Plant ESDV / HIPPS (line 809), and Package Line-Item Requirements row 61 to confirm equipment identity, pressure framing, and HIPPS context.
3. Resolve the equipment-count narrative ambiguity (C-01 in `Guidance.md` Conflict Table): confirm three receivers (PR-1010-1, PR-1020-1, PR-1030-1) per package basic scope. Surface for human ruling if not yet confirmed at gate.
4. Coordinate with the Package Vendor for vendor equipment outline drawings, HIPPS package P&IDs, and vendor maintenance-access requirements (status TBD until vendor design advances).
5. Coordinate with EPC civil/structural for foundation IFC drawings and grading/spill-containment design (interface `IFC-3894C2DC14`, `IFC-6798D96AAF`).
6. Coordinate with EPC electrical for MCC supply route and energization plan (interface `IFC-F2CC0221E0`).
7. Coordinate with EPC I&C / DCS for marshalling-termination handoff and loop-test responsibility (interface `IFC-99C4B8C9E0`; DCS integration "by others" per SOW-0164).
8. Coordinate with EPC pipeline / pigging interface (`IFC-65EDB92369`) for first-pig receipt sequencing.
9. Draft the workface plan: installation sequence for three skids, lay-down, lifts, foundation pre-set acceptance, tie-in checkpoints, barred-tee installation, full-port pig-handling isolation verification, sweet-gas purge tie-in, HP flare vent tie-in, HIPPS hookup, EHT installation, I&C cabling, drain tie-in, grading acceptance, maintenance-access walk-down.
10. Draft the construction interface and turnover checklist per the minimum contents listed in `Datasheet.md` (Construction section) and the requirements in `Specification.md`.
11. Mark each unresolved item as `TBD` with source reference; do not invent acceptance criteria where source data is absent.
12. Internal review against `Specification.md` requirements R-01 through R-16; close out checklist gaps.
13. Issue CWP IFC (Issued For Construction). Record issue in `_run_records/`.

### B. Field execution (Construction contractor under EPC Integrator)

14. Site receipt of three receiver/HIPPS skids; preservation check; vendor punch from shipping inspection captured.
15. Foundation acceptance walk-down for each skid (interface `IFC-6798D96AAF`); civil sign-off.
16. Skid setting (PR-1010-1, then PR-1020-1, then PR-1030-1 - actual sequence per workface plan); grouting per civil spec; level/alignment confirmed.
17. Install upstream full-port isolation / ESDVs and barred tees per IFC drawings; inspect bore for pig-passage clearance prior to install (R-03, R-04).
18. Tie-in inlet piping (pipeline side) - by EPC interconnecting piping scope per SOW-0164; coordinate weld procedures and sour-service hardness checks (R-08).
19. Tie-in downstream piping to inlet separator system (by EPC interconnecting piping scope).
20. Install low-pressure sweet fuel-gas purge connection downstream of each receiver manual isolation valve (R-05).
21. Install HP flare vent tie-in for each receiver (R-06); slope and pocket inspection.
22. Install HIPPS package mechanical and instrument hookups (R-07); coordinate with vendor commissioning representative.
23. Install Drain / Containment tie-ins per facility drain design (R-13).
24. Install EHT per design (R-11); continuity, megger, and as-installed coverage records.
25. Install electrical power tie-ins for skid loads (R-10) and I&C cabling to marshalling cabinet (R-12); loop checks to marshalling termination.
26. Pressure test per project piping spec (R-09); record results.
27. Sour-service hardness survey on representative welds (R-08); record results.
28. Grading and spill-containment as-built check around each skid (R-14).
29. Maintenance-access walk-down with operations (R-15).
30. Execute and close construction interface and turnover checklist per skid (R-16).
31. HIPPS loop and function test (with vendor and operations); upstream ESDV stroke tests; PT calibration; PCV stroke test; PID interaction with inlet separator pressure simulated. SIL proof-test per detailed-engineering output - TBD.
32. Punch list and mechanical-completion walk-down with EPC Integrator and Operations.
33. Turnover package issued to commissioning team.

## Verification

| Check | How verified | Linked requirement |
|---|---|---|
| Three skids set and tagged correctly | Installation log + nameplate verification | R-01 |
| Foundation acceptance per civil IFC | Civil sign-off record | R-02 |
| Full-port pig-handling isolation | Bore inspection + valve datasheet | R-03 |
| Barred tees installed | Visual inspection + ITP sign-off | R-04 |
| Sweet-gas purge tie-in operable | Pressure / isolation function test | R-05 |
| HP flare vent tie-in clear | Pressure test + slope check | R-06 |
| HIPPS function | Loop test + trip time + PT/PCV stroke | R-07 |
| Sour-service welds qualified | WPS/PQR review + hardness survey | R-08 |
| Pressure test passed | Hydrostatic / pneumatic record | R-09 |
| Electrical energization | Megger / continuity tests + MCC coordination | R-10 |
| EHT installed and continuous | Continuity / insulation record | R-11 |
| I&C cabling loop-checked to marshalling | Loop-check record + DCS-integration sign-off | R-12 |
| Drain tie-in operable | Drain pressure / function test | R-13 |
| Grading / spill containment as-built | Civil as-built check | R-14 |
| Maintenance access preserved | Operations walk-down record | R-15 |
| Turnover checklist closed per skid | Signed construction interface and turnover checklist | R-16 |

## Records

Records to be produced and turned over:
- CWP IFC package (this deliverable, issued)
- Installation and tie-in workface plan (issued and as-executed)
- Construction interface and turnover checklist per skid (signed)
- Inspection-test plan (ITP) records (welding, NDE, pressure test, sour-service hardness)
- HIPPS loop-test and function-test records
- EHT continuity and insulation records
- Loop-check records (I&C) acknowledged by DCS-integration party
- Foundation acceptance records (interface with EPC civil scope)
- Grading / spill-containment as-built check
- Maintenance-access walk-down record
- Punch list and mechanical-completion record
- First-pig-receipt coordination record (operational handoff)
