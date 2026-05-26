# Specification: DEL-051-01_scope-of-work — Scope of Work

> Normative requirements for the EPC Integrator Scope of Work for PKG-051 Process Heat Medium Unit. Each requirement cites its source slice. Where source slices conflict (Workbook hot/cold-loop vs. DBM single-loop, expansion-tank pressure, maximum bulk temperature), requirements are stated `TBD pending human ruling` and the conflict is captured in `Guidance.md` Conflict Table.

## Scope

### In scope (this Scope of Work document)

- SR-01: The Scope of Work shall describe the full package scope of PKG-051 Process Heat Medium Unit including tagged equipment, package function, source basis, and whole-facility integration narrative. [`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-051-01]
- SR-02: The Scope of Work shall identify the responsibility split: Package Vendor owns package engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination. [`PACKAGE_REGISTER.csv` PKG-051 responsibility model; OBJ-004]
- SR-03: The Scope of Work shall list the four anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. [`_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row DEL-051-01]
- SR-04: The Scope of Work shall declare coverage of SOW-0165, SOW-0166, SOW-0167, SOW-0168 and support of OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010. ASSUMPTION on objective association (package-grouping heuristic). [`_CONTEXT.md`; `SCOPE_LEDGER.csv`; `OBJECTIVE_REGISTER.csv`]

### Out of scope (this Scope of Work document)

- Vendor package engineering deliverables (carried by DEL-051-04). [`DELIVERABLE_REGISTER.csv` row DEL-051-04]
- Package datasheet content (carried by DEL-051-02). [`DELIVERABLE_REGISTER.csv` row DEL-051-02]
- Construction work package content (carried by DEL-051-03). [`DELIVERABLE_REGISTER.csv` row DEL-051-03]
- Vendor document turnover register (carried by DEL-051-05). [`DELIVERABLE_REGISTER.csv` row DEL-051-05]

## Requirements (Package Scope Content)

### Package identity and function

- REQ-01: The SoW shall identify PKG-051 by Workbook Tracking Number 26020-01-15-001, Workbook Packages row 79, discipline Mechanical, WBS 01. [`PACKAGE_REGISTER.csv` PKG-051]
- REQ-02: The SoW shall state the package function as a closed-loop hot oil / heat medium system supplying heat to multiple process users in the facility. [SOW-0166]
- REQ-03: The SoW shall record the package architecture as stated in the workbook scope (hot/cold loop with mixing) and the architecture as stated in the Deepcut DBM (single unified loop at 220 °C/428 °F). Final architecture is `TBD pending human ruling` — see Conflict Table in `Guidance.md`. [SOW-0166; `4-25_Deepcut_DBM.md` lines 1945-1947]

### Tagged equipment list (minimum content)

- REQ-04: The SoW shall list the following tagged or named equipment derived from accessible source slices:
  - Pump Module: expansion tank; circulation pumps (count per Workbook = 3 × 66 %; DBM consolidated sparing TBC). [SOW-0167; `4-25_Deepcut_DBM.md` line 1996]
  - Medium Heater Module: one medium heater (API-560 natural-draft cabin-style direct-fired thermal-fluid heater per DBM; tagged `H-5170-1` per DBM duty table), one heater blower, one air intake pre-heater. [SOW-0166; `4-25_Deepcut_DBM.md` lines 1977, 1998]
  - Pop tank associated with heater PSV discharge (~600 bbl). ASSUMPTION (DBM-aligned): vendor-package vs. EPC scope boundary TBD. [`4-25_Deepcut_DBM.md` line 2002]
- REQ-05: The SoW shall list known downstream users supplied by the loop, drawn from the DBM duty table: stabilizer reboilers `E-7230-1`, `E-7430-1`; TEG reboiler `E-5790-1`; amine reboiler `E-5360-1`; deethanizer reboiler `E-6285-1`; MPFF HCL heaters `E-7120-1`, `E-7320-1`. [`4-25_Deepcut_DBM.md` lines 1967-1976]

### Design and operating envelope

- REQ-06: The SoW shall record the heat medium components minimum design pressure of 350 psig (2413 kPag). [`4-25_Deepcut_DBM.md` line 1983; SOW-0167]
- REQ-07: The SoW shall record the maximum normal operating temperature as 428 °F (220 °C) per DBM. [`4-25_Deepcut_DBM.md` line 1957]
- REQ-08: The SoW shall record the maximum bulk fluid temperature. Value is `TBD pending human ruling` because DBM states 599 °F (315 °C) while Workbook SOW-0167 states 500 °F (260 °C). [Conflict Table item C-01]
- REQ-09: The SoW shall record the heat medium fluid as Petrotherm (Brenntag per DBM; Petro-Canada per Workbook) with vendor confirmation of fluid rating required. [`4-25_Deepcut_DBM.md` line 1951; SOW-0167]
- REQ-10: The SoW shall record total post-VE design loop duty of approximately 21,913 kW (~74.8 MM BTU/h) at winter design as the basis for heater resizing. [`4-25_Deepcut_DBM.md` line 1976]
- REQ-11: The SoW shall record heater sparing basis of 1 × 125 %, pending review of multi-heater options (2 × 62.5 % or 3 × 41.7 %). [`4-25_Deepcut_DBM.md` line 1998]
- REQ-12: The SoW shall record expansion-tank operating pressure as `TBD pending human ruling` because Workbook SOW-0167 states 125–240 kPag (18–35 psig) while SOW-0168 states 695 kPag (100 psig). [Conflict Table item C-02]

### Boundaries (by others)

- REQ-13: The SoW shall list interconnecting piping, DCS integration, foundations, mounting buildings at site, electrical supply from MCC, and platforms/stairs as scope by others. [SOW-0168]
- REQ-14: The SoW shall list applicable interface types: Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports. [`PACKAGE_REGISTER.csv` PKG-051 applicable interface types]

### Whole-facility integration narrative

- REQ-15: The SoW shall describe the heat medium system as a shared utility serving multiple disciplines/areas at 04-25, with mole sieve regeneration gas heating removed from the loop (separate direct-fired heater). [`4-25_Deepcut_DBM.md` lines 1832, 1947]
- REQ-16: The SoW shall describe the responsibility-handoff path: vendor package handoff to EPC via DEL-051-02 (Package Datasheet); installation/integration via DEL-051-03 (Construction Work Package); EPC review and acceptance via DEL-051-06. [`DELIVERABLE_REGISTER.csv` rows DEL-051-02, DEL-051-03, DEL-051-06]

### Open items to be carried forward

- REQ-17: The SoW shall carry the following open items into downstream deliverables:
  - Single-loop circulation rates (TBD pending simulation). [`4-25_Deepcut_DBM.md` line 1961]
  - Pump sparing consolidation (TBC). [`4-25_Deepcut_DBM.md` line 1996]
  - Heater resizing for 220 °C single-loop duty basis. [`4-25_Deepcut_DBM.md` line 1979]
  - Heater minimum-flow assumption (85 % of design, TBC by vendor). [`4-25_Deepcut_DBM.md` line 2000]
  - Sour tube-rupture venting review including dispersion modeling. [`4-25_Deepcut_DBM.md` line 2002]
  - Fluid vendor rating to maximum bulk temperature. [`4-25_Deepcut_DBM.md` line 1951]
  - Pop-tank specific gravity (TBC), pour point (TBC), maximum tubeskin/film temperature (TBC). [`4-25_Deepcut_DBM.md` lines 1955, 1959, 2002]
  - Architecture reconciliation: workbook hot/cold-loop vs. DBM single-loop (Conflict Table C-03).

## Standards

- STD-01: API-560 (Fired Heaters for General Refinery Service) — heater type basis. [`4-25_Deepcut_DBM.md` line 1998] Location of governing edition/clauses: TBD (standard text not locally accessible).
- STD-02: ASME Section I — referenced for the heat medium heater (no block valves on PSV inlet/outlet for ASME Section I-certified equipment). [`4-25_Deepcut_DBM.md` line 2435] Location of governing edition/clauses: TBD.
- STD-03: ANSI flange ratings (300 #) — drain header related; not directly governing this SoW but cited in the surrounding utility basis. [`4-25_Deepcut_DBM.md` line 2010] Location TBD.
- STD-04: Project-wide DBM-Deepcut design basis (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) is authoritative for facility-side parameters cited in this SoW.

## Verification

| Requirement | Verification approach |
|---|---|
| SR-01..SR-04 | Document review against `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, and `OBJECTIVE_REGISTER.csv`. |
| REQ-01, REQ-02 | Trace check against `PACKAGE_REGISTER.csv` PKG-051 and SOW-0166. |
| REQ-03 | Conflict Table review and recorded human ruling resolving C-03. |
| REQ-04, REQ-05 | Equipment list reconciled against SOW-0166/0167 and DBM duty table lines 1967-1976. |
| REQ-06, REQ-07, REQ-10, REQ-11 | Numeric trace to DBM `## Heat Medium Basis` slice. |
| REQ-08, REQ-12 | Recorded human ruling resolving C-01 and C-02 prior to package issuance. |
| REQ-09 | Fluid vendor confirmation document at detailed engineering. |
| REQ-13, REQ-14 | Interface register cross-check against PKG-051 row. |
| REQ-15, REQ-16 | Narrative review against DBM SEC-08 utilities entry and downstream deliverable records. |
| REQ-17 | Open-item carry-forward into DEL-051-02 datasheet and DEL-051-03 work package; closure tracked in `OPEN_ISSUES.csv`. |

## Documentation

Required artifacts produced by this deliverable (matching `_CONTEXT.md` Anticipated Artifacts):

- Package scope of work (the narrative SoW document itself, anchored by this Specification, Guidance, and Procedure)
- Tagged equipment and package identity list (REQ-04, REQ-05)
- Package function and integration narrative (REQ-02, REQ-15)
- Responsibility assignment record (SR-02, REQ-16)
