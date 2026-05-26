# Specification — DEL-051-03 Construction Work Package (PKG-051 Process Heat Medium Unit)

## Scope

This specification governs the EPC Integrator Construction Work Package (CWP) that describes how the Process Heat Medium Unit (PKG-051) is physically installed, built, inspected, turned over, and tied into adjacent facility systems (reboilers, heaters, drains, electrical, controls, fire & gas, fuel gas).

**In scope** (per `_CONTEXT.md` and DBM-Deepcut 4-25 §"Heat Medium Basis"):
- The single unified heat medium loop equipment: API-560 direct-fired thermal-fluid heater, expansion tank, single-loop circulation pumps, pop tank (~600 bbl), associated piping, instrumentation, and electrical.
- Field installation, mechanical hookups, shipped-loose item installation, tie-ins to user reboilers/heaters and to the fuel gas, flare, drain, electrical, and controls systems.
- Construction inspection, testing, and turnover documentation for the package.

**Excluded** (deliverable scope boundary):
- Process and mechanical design of the HM equipment (carried in DEL-051-02 Package Datasheet and DEL-051-04 Vendor Engineered Equipment Package).
- Vendor document turnover register (carried in DEL-051-05).
- EPC review/acceptance evidence (carried in DEL-051-06).
- Heat-medium users themselves (reboilers, TEG regenerator, amine reboiler, deethanizer reboiler); the CWP terminates at the HM supply/return interface flanges to user packages.

## Requirements

### R-051-03-01 Workface installation plan
The CWP shall include a workface installation plan for HM heater, pump module, expansion tank, pop tank, and unit piping, sequenced to support module offload/setting and mechanical hookup as defined by the project execution plan.
Source: DBM-Comp_and_Liquids 3-25 §"Construction Scope Summary" (line 73). ASSUMPTION: sequencing details are project-execution-plan dependent.

### R-051-03-02 Foundations, civil, and structural install
Foundations for the fired heater, pump module, and pop tank shall be designed and installed in conformance with the accepted geotechnical report and DBM frost-protection basis; until the geotechnical report is accepted, the CWP shall identify geotechnical values as placeholders.
Source: DBM-Comp_and_Liquids 3-25 line 141.

### R-051-03-03 Heat-medium piping mechanical and pressure integrity
All heat-medium fluid-containing components installed under this CWP shall meet a minimum design pressure of 350 psig (2413 kPag). Hydrostatic / pressure-test plans shall reflect this basis.
Source: DBM-Deepcut 4-25 line 1983.

### R-051-03-04 Seal-welded exchanger tubes (HM service)
All heat-exchanger users in heat-medium service installed or interfaced under this CWP shall have seal-welded tubes; the CWP construction inspection plan shall verify seal-weld evidence at field tie-in for shipped-loose bundles.
Source: DBM-Deepcut 4-25 line 2503; reboiler-tube seal-weld basis at line 706.

### R-051-03-05 PSV and pop tank installation
The HM heater PSV(s) shall be installed to discharge to the pop tank (approx. 600 bbl, normally empty), and the pop tank level switch validating empty status during normal operation shall be installed and loop-checked prior to turnover.
Source: DBM-Deepcut 4-25 line 2002.

### R-051-03-06 No block valves on ASME Section I PSV piping
The CWP installation and inspection plan shall prohibit installation of block valves on PSV inlet or outlet piping for equipment certified under ASME Section I, including the heat medium heater.
Source: DBM-Deepcut 4-25 line 2435.

### R-051-03-07 Cold-start commissioning
The construction turnover and commissioning interface shall confirm that circulation pump motors can be started at a 15 deg C ambient cold-start condition.
Source: DBM-Deepcut 4-25 line 1996.

### R-051-03-08 Fire and gas detector install
At minimum one fire detector shall be installed in every building containing heat-medium service; detector install and loop-check shall be on the turnover checklist.
Source: DBM-Deepcut 4-25 line 3256.

### R-051-03-09 Field tie-in list
The CWP shall publish a field tie-in list covering HM supply and return laterals to all HM users (reboilers, heaters), fuel-gas supply to the HM heater, flare/vent connections, drain connections, electrical feeds (pump motors, heater BMS), and control system connections.
Source: DBM-Deepcut 4-25 line 617 (package deliverable expectations); line 1822 (utility systems section scope).

### R-051-03-10 Construction interface and turnover checklist
A construction interface and turnover checklist shall be produced and used to record mechanical completion and to evidence handoff to commissioning, including PSV witness, hydrostatic test, electrical megger, instrumentation loop check, fire/gas loop check, and pop-tank empty validation.
Source: `_CONTEXT.md` anticipated artifact; DBM-Deepcut 4-25 lines 2002, 3256.

### R-051-03-11 Cross-facility tie-in coordination
Installation shall coordinate with package buildings, MCC/RIO interfaces, heat tracing, HVAC, and drain/vent tie-ins per the DBM cross-discipline coordination requirement.
Source: DBM-Deepcut 4-25 line 619.

## Standards

- API-560 (direct-fired thermal-fluid heater design and construction reference) — location TBD; cited via DBM-Deepcut 4-25 line 1998.
- ASME Boiler and Pressure Vessel Code, Section I (heat medium heater certification) — location TBD; cited via DBM-Deepcut 4-25 line 2435.
- ASME B31.3 process piping (assumed applicable to HM piping in Canadian provincial jurisdiction): ASSUMPTION; not explicitly cited in available DBM source slices.
- Provincial pressure-equipment registration and inspection regime: ASSUMPTION; specific regulator and registration workflow are TBD in the current locally accessible source set.

## Verification

| Req | Verification approach |
|---|---|
| R-051-03-01 | Document review of workface plan against project execution plan. |
| R-051-03-02 | Inspection of foundation As-built against accepted geotechnical report; if geotechnical report unavailable, raise as TBD on the turnover checklist. |
| R-051-03-03 | Hydrostatic test records at >= 350 psig design basis; ITP sign-off. |
| R-051-03-04 | Visual / NDE inspection of seal-welded tubes per exchanger ITP. |
| R-051-03-05 | PSV witness + pop tank level-switch loop check. |
| R-051-03-06 | Walk-down inspection of PSV inlet/outlet piping; redline if any block valve installed. |
| R-051-03-07 | Cold-start motor demonstration during commissioning interface. |
| R-051-03-08 | Fire/gas detector install verification and loop check per building. |
| R-051-03-09 | Tie-in list completeness review against P&IDs and adjacent package interface registers. |
| R-051-03-10 | Turnover checklist sign-off, item by item, before package handoff. |
| R-051-03-11 | Interdiscipline walk-down sign-off (mechanical, electrical, controls, civil). |

## Documentation

- Construction work package document (this CWP set).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- ITPs, NDE records, hydrostatic test records, PSV witness records.
- Loop check records for instrumentation, fire/gas, and pop-tank level switch.
- Field tie-in list with as-built redlines.
