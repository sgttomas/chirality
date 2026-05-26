# Specification: DEL-068-03 — Construction Work Package (TEG Dehydration Unit)

## Scope

### In scope
This Construction Work Package (CWP) defines the EPC Integrator construction, installation, inspection, tie-in, and turnover activities required to physically install the vendor-supplied **TEG Dehydration Unit (PKG-068)** into the 04-25 Deepcut facility, including all interfaces flagged YES for PKG-068 in the Gate-07 Interface Register (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). [Source: `INTERFACE_REGISTER.csv` rows for PKG-068; `PACKAGE_REGISTER.csv` row 97]

The CWP also defines:
- Vendor module/skid receipt, set, alignment, and grouting (Modules 520 and 570 contents per the DBM module table). [Source: `4-25_Deepcut_DBM.md` lines 1131, 1133]
- Foundations, supports, pipe-rack, platforms, and maintenance access provisions for the TEG dehydration train. [Source: SOW-0240 "by others"; OBJ-008; IFC-0B65AE534B; IFC-7286F463F5]
- Interconnecting process and utility piping, including tie-ins to amine treating, molecular sieve dehydration, inlet/TEG cross-exchanger, heat medium loop, HP flare, LP flare, and drain headers. [Source: `4-25_Deepcut_DBM.md` SEC-06, lines 1131–1133, 2029; ASSUMPTION: tie-in list scoped to interfaces identified in PROJECT_DECOMP for PKG-068]
- Electrical power, EHT, grounding, lighting, and burner-control-panel power supply (excluded from vendor scope). [Source: SOW-0240; OBJ-005]
- Inspection, NDE, hydrotest, mechanical completion, pre-commissioning, and turnover activities. [ASSUMPTION: standard EPC construction practice; specific NDE and test extents TBD]
- Construction interface and turnover checklist and installation/tie-in workface plan. [Source: DELIVERABLE_REGISTER.csv row 548 anticipated artifacts]

### Out of scope
- Vendor package engineering, package design, vendor documentation, and physical equipment supply — owned by Package Vendor. [Source: PACKAGE_REGISTER.csv row 97; OBJ-004]
- Process simulation, P&ID design, or detailed engineering of TEG dehydration internals (vendor-led). [Source: PACKAGE_REGISTER.csv row 97]
- Items the source explicitly labels "by others" beyond EPC scope. [Source: SOW-0240]

## Requirements

### R-CWP-068-03-01 — Responsibility split
The CWP SHALL be developed and executed by the EPC Integrator and SHALL preserve the vendor/EPC responsibility split: vendor owns engineering/design/vendor documentation/equipment; EPC owns installation, integration, interface execution, and turnover. [Source: PACKAGE_REGISTER.csv row 97; OBJ-004]

### R-CWP-068-03-02 — Interfaces addressed
The CWP SHALL include workface execution coverage for every interface row flagged `YES` against PKG-068 in `INTERFACE_REGISTER.csv` (13 interface types listed in the Datasheet). [Source: `INTERFACE_REGISTER.csv` PKG-068 rows]

### R-CWP-068-03-03 — By-others items explicit
The CWP SHALL explicitly include construction execution of the items the source labels "By others / NOT in vendor scope": interconnecting piping, foundations, and electrical supply to the burner control panel. [Source: SOW-0240]

### R-CWP-068-03-04 — Module receipt and setting
The CWP SHALL define receipt, rigging, set, alignment, grout, and integrity-restoration requirements for the vendor-fabricated Module 520 contents (TEG inlet air cooler, TEG inlet filter coalescer, TEG contactor, TEG cooler, TEG level pot, and other Module 520 items) and Module 570 contents (TEG regeneration module/building items: flash drum, solids filters, charcoal filter, lean/rich exchanger, pumps, still and stripping columns, reflux condenser, reboiler, surge tank, regen cooler, overheads scrubber/pumps, make-up tank, make-up pump). [Source: `4-25_Deepcut_DBM.md` lines 1131, 1133; line 2795 (570-1 fabrication = Shop)]

### R-CWP-068-03-05 — Tie-ins to facility systems
The CWP SHALL define tie-in execution to: (a) sweet gas from amine absorbers feeding the TEG inlet cooler; (b) dehydrated gas to inlet/TEG cross-exchanger and onward to mol-sieve dehydration; (c) heat-medium supply at 425 °F to the TEG reboiler via mixing valves; (d) HP flare (TEG contactor automated blowdown); (e) LP flare (TEG regeneration overheads, flash drum LP blowdown); (f) VRU (still overheads recovery, flash gas); (g) drain/containment headers. [Source: `4-25_Deepcut_DBM.md` lines 1113, 1191, 1193, 1214, 1360, 1375, 2029]

### R-CWP-068-03-06 — Common-equipment isolation
Because the TEG Dehydration Unit is **common equipment** (one train serves the facility), the CWP SHALL provide installation provisions for safe isolation, draining, blinding, and maintenance access without facility shutdown beyond declared common-equipment outage limits. [Source: `4-25_Deepcut_DBM.md` line 2429; IFC-7286F463F5]

### R-CWP-068-03-07 — Design-condition compliance
Installed piping, supports, tie-in flanges, valves, and instrumentation interfaced to the package SHALL be rated for the SOW-stated design conditions: 1,480 psig design pressure and 150 °F design temperature on the process side. [Source: SOW-0240]

### R-CWP-068-03-08 — Workface plan
The CWP SHALL produce an **installation and tie-in workface plan** as an anticipated artifact. [Source: DELIVERABLE_REGISTER.csv row 548]

### R-CWP-068-03-09 — Turnover artifact
The CWP SHALL produce a **construction interface and turnover checklist** as an anticipated artifact, traceable to DEL-068-05 (vendor-document turnover) and DEL-068-06 (EPC vendor package review and acceptance). [Source: DELIVERABLE_REGISTER.csv row 548; SCOPE_LEDGER siblings]

### R-CWP-068-03-10 — Vendor reference set
The CWP SHALL reference the vendor package definition document `26020-Package_Requirements.docx` package heading 23 as the controlling vendor-scope document. [Source: PACKAGE_REGISTER.csv row 97; `_CONTEXT.md`]

### R-CWP-068-03-11 — Safety/regulatory carryover
The CWP SHALL carry sour-service, fire/gas, shutdown, and relief/flare/drain/containment requirements from the DBM into installation and pre-commissioning checks. [Source: OBJ-009; `4-25_Deepcut_DBM.md` SEC-09, SEC-14]

## Standards

| Standard / Source | Application | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 23 | Vendor scope and vendor-document tables for TEG Dehydration Unit | location TBD (binary source not extracted) |
| 4-25 Deepcut DBM (`4-25_Deepcut_DBM.md`) | Process basis, module assignments, heat-medium and flare interfaces, common-equipment treatment | SEC-06 (lines 1098–1386), modules table (lines 1131–1133), SEC-08, SEC-09, SEC-15 |
| ASME B31.3 (process piping) | Process piping construction (1,480 psig service) | location TBD (not in extracted source) — ASSUMPTION based on discipline norms; confirm in detailed engineering |
| ASME Sec VIII Div 1 (pressure vessels) | Vessel acceptance for TEG contactor, flash drum, scrubbers | location TBD — ASSUMPTION |
| CSA/Provincial electrical code | Electrical tie-in to burner control panel and package power | location TBD — ASSUMPTION |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-CWP-068-03-01 | RACI / responsibility matrix review against PACKAGE_REGISTER.csv row 97 and DEL-068-06 acceptance package |
| R-CWP-068-03-02 | Cross-walk of CWP work packages to INTERFACE_REGISTER.csv PKG-068 rows; gap log resolved |
| R-CWP-068-03-03 | Inspection of CWP scope sheet for explicit inclusion of by-others items |
| R-CWP-068-03-04 | Receiving inspection, alignment records, grout certification |
| R-CWP-068-03-05 | Tie-in punchlist closed against P&IDs; test-pack reconciliation |
| R-CWP-068-03-06 | Isolation list and maintenance-access walkdown signed off |
| R-CWP-068-03-07 | Material test reports + hydrotest records vs. design-pressure tag |
| R-CWP-068-03-08 | Workface plan issued and accepted |
| R-CWP-068-03-09 | Turnover checklist completed and signed by EPC Integrator and Owner |
| R-CWP-068-03-10 | Reference traceability matrix |
| R-CWP-068-03-11 | Pre-commissioning safety checks completed; F&G loop checks executed |

## Documentation

Required artifacts produced by this deliverable:

- Construction Work Package (master document) — TBD final outline
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Related artifacts (other deliverables, not produced here):

- DEL-068-01 Scope of Work — EPC scope reference
- DEL-068-02 Package Datasheet — process/mechanical parameters
- DEL-068-04 Vendor-Engineered Equipment Package — vendor design
- DEL-068-05 Vendor-Document Turnover Package — vendor doc set
- DEL-068-06 EPC Vendor Package Review and Acceptance — acceptance gate
