# Datasheet — DEL-051-03 Construction Work Package (PKG-051 Process Heat Medium Unit)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-051-03_construction-work-package |
| Name | Construction Work Package |
| ParentPackageID | PKG-051 |
| ParentWorkbookID | 51 |
| PackageName | Process Heat Medium Unit |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Decomposition Basis | GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP snapshot |

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Package function | Single unified process heat medium loop supplying hot oil to reboilers, heaters, and auxiliaries | DBM-Deepcut 4-25 §"Heat Medium Basis" (line 1945) |
| Heat medium fluid | Brenntag Petrotherm | DBM-Deepcut 4-25 line 1951 |
| Loop supply temperature | 220 deg C (428 deg F) | DBM-Deepcut 4-25 line 1832, 1951 |
| Heater type | API-560 natural-draft cabin-style direct-fired thermal-fluid heater | DBM-Deepcut 4-25 line 1998 |
| Heater design duty basis | 1.25 x winter steady-state design duty | DBM-Deepcut 4-25 line 1998 |
| Heater sparing basis | 1 x 125% (multi-heater options 2 x 62.5% / 3 x 41.7% under review) | DBM-Deepcut 4-25 line 1998 |
| Circulation pumps | Single-stage vertical inline; sparing TBC | DBM-Deepcut 4-25 line 1996 |
| Minimum component design pressure | 350 psig (2413 kPag) | DBM-Deepcut 4-25 line 1983 |
| PSV discharge | Pop tank, ~600 bbl, normally empty, with level switch | DBM-Deepcut 4-25 line 2002 |
| Cold-start ambient assumption | 15 deg C; pump motors must start at this condition | DBM-Deepcut 4-25 line 1996 |
| Pop tank fluid SG | 1.00 (TBC) | DBM-Deepcut 4-25 line 2002 |
| Scope SOW items covered | SOW-0165, SOW-0166, SOW-0167, SOW-0168 | _CONTEXT.md |
| Supported objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | _CONTEXT.md (PACKAGE_HEURISTIC ASSUMPTION) |

## Conditions

| Condition | Value | Note |
|---|---|---|
| Minimum design ambient | -40 deg C | DBM-Comp_and_Liquids 3-25 (winter design basis, line 696) |
| Bulk temperature service | Up to 220 deg C, vendor to confirm fluid rating to maximum bulk temperature | DBM-Deepcut 4-25 line 1951 |
| Minimum circulation basis | Assumed 85% of design flow for fired-heater operation, TBC | DBM-Deepcut 4-25 line 1961 |
| Tube construction (heat-exchanger users) | All HM-service exchangers shall have seal-welded tubes | DBM-Deepcut 4-25 line 2503 |
| Block-valve restriction | No block valves on PSV inlet/outlet for ASME Section I-certified equipment, including the HM heater | DBM-Deepcut 4-25 line 2435 |

## Construction (CWP composition)

| Element | Description | Source / Note |
|---|---|---|
| Construction work package document | Workface plan and installation narrative for the HM unit module(s) | _CONTEXT.md anticipated artifact |
| Installation and tie-in workface plan | Foundation, piping, electrical, controls install sequence with tie-ins to reboilers/heaters/auxiliaries | _CONTEXT.md anticipated artifact; DBM-Deepcut 4-25 §"Utility Systems and Plant Support" (line 1822) |
| Construction interface and turnover checklist | Field tie-in verification and mechanical-completion turnover register | _CONTEXT.md anticipated artifact |
| Field tie-in list inputs | Heat-medium supply/return laterals to reboilers, heaters, pop tank vent, and pump module connections | DBM-Deepcut 4-25 line 617 (package deliverable expectations) |
| Civil / structural scope | Pump module foundations, heater foundation and stack support, pop tank foundation, pipe-rack supports | DBM-Comp_and_Liquids 3-25 line 38 (civil scope summary) |
| Fire/gas detection install | At minimum one fire detector in every building containing heat-medium service | DBM-Deepcut 4-25 line 3256 |

## References

- _CONTEXT.md (this deliverable)
- _REFERENCES.md (this deliverable)
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md
- /Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md
- 26020-Package_Requirements.docx (binary; package heading 6 — location TBD, not locally machine-readable)
- 26020-Packages_Interfaces_4_export.xlsx (binary; Packages row 79 — location TBD, not locally machine-readable)

## Missing / TBD

- Final heater sparing arrangement: TBD (1 x 125% vs 2 x 62.5% vs 3 x 41.7%).
- Single-loop circulation rates and pump sparing: TBD pending detailed engineering simulation.
- Pop tank fluid SG confirmation: TBC.
- Final fluid vendor rating for sustained 220 deg C bulk service: TBC.
- 26020-Package_Requirements.docx package heading 6 detail: location TBD (binary not extracted).
