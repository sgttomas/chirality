# Specification — DEL-075-04 Vendor Engineered Equipment Package (Cryogenic Unit "Deepcut")

## Scope

This deliverable specifies the engineering, design, fabrication/supply, and physical delivery of the **Vendor Engineered Equipment Package** for the West Doe Deepcut Cryogenic Unit (PKG-075). The package vendor produces this work under the EPC Scope of Work (DEL-075-01) and EPC Package Datasheet (DEL-075-02), with EPC Integrator integration review (`_CONTEXT.md`; DBM-Deepcut SEC-01).

### Included
- Vendor process and mechanical design of the UltraTEF cryogenic unit (BAHX, cold separator, J-T valve, turbo-expander/compressor, propane absorber, deethanizer, reflux/reboiler, expander aftercooler, methanol injection skid) per DBM-Deepcut SEC-06.
- Fabrication, factory assembly, factory testing, and supply of the 15 equipment line items rostered to the Cryogenic Unit ("Deepcut") package (DBM-Deepcut SEC-10 row 9).
- Vendor package design basis and datasheet set covering all rostered equipment (`_CONTEXT.md`, Anticipated Artifacts).
- Interface preparation for upstream molecular-sieve-dried gas inlet, sales-gas compression, NGL treating, heat-medium service, methanol storage interface, flare (cryo), VRU, lube-oil/seal-gas utilities (DBM-Deepcut SEC-06 Interfaces).

### Excluded
- EPC Scope of Work (DEL-075-01), Package Datasheet (DEL-075-02), Construction Work Package (DEL-075-03), Vendor Document Turnover (DEL-075-05), and EPC Vendor Package Review and Acceptance (DEL-075-06).
- Off-loading, setting on foundations, mechanical hookup at site — Tourmaline field construction scope (DBM-Deepcut SEC-01 Construction Responsibility).
- Plot plan layout authority (CIV-235633-5002) — external (DBM-Deepcut SEC-02).
- Future NGL treating/dehydration deethanizer bottoms exchanger and cooler — future interface (DBM-Deepcut SEC-06).

## Requirements

### R-1 Functional
R-1.1 The package shall recover C3+ NGL from molecular-sieve-dried inlet gas and produce sales gas (DBM-Deepcut SEC-06).
R-1.2 The package shall provide both Expander mode (normal) and J-T mode (start-up / off-design) operation (DBM-Deepcut SEC-06 UltraTEF Operating Modes).
R-1.3 Expander mode C3 recovery shall be 99+% (DBM-Deepcut SEC-06).
R-1.4 J-T mode shall achieve >=27% C3 recovery to support sales-gas total-sulphur compliance (DBM-Deepcut SEC-06; cross-ref SEC-03).

### R-2 Process Design Conditions
R-2.1 Inlet design flow: 307.6 MMSCFD winter / 303 MMSCFD summer (DBM-Deepcut SEC-06).
R-2.2 Inlet design temperature: 14.2 degC winter / 40.5 degC summer (DBM-Deepcut SEC-06).
R-2.3 Inlet design pressure: 7129 kPag; low/high pressures TBC (DBM-Deepcut SEC-06).
R-2.4 Sales pressure (expander mode): summer 3068 kPag design / winter 3289 kPag expected (DBM-Deepcut SEC-06).
R-2.5 Cryogenic water-dewpoint limit: < -75 degC at highest operating pressure (DBM-Deepcut SEC-06).

### R-3 Mechanical / Equipment
R-3.1 BAHX: six-pass; ALPEMA 3rd Edition + vendor practice with explicit exceptions; ASME U Stamp; BC CRN; minimum 10% excess area on all passes; 0 mm corrosion allowance; maximum design temperature 150 degF (66 degC) (DBM-Deepcut SEC-06).
R-3.2 BAHX strainers: tee strainers upstream of each pass; clean-condition normal dP <2 psid; change/clean at <=15 psid maximum (DBM-Deepcut SEC-06).
R-3.3 BAHX A-pass bypass: automated, 15-20% of maximum inlet flow capacity (final capacity to be reviewed); controlled by cold-separator overhead temperature (DBM-Deepcut SEC-06).
R-3.4 Cold separator: mesh/vane demister; demister sized for expander-mode liquid density with J-T mode governing actual gas volumetric flow (DBM-Deepcut SEC-06).
R-3.5 J-T valve: sized for full hydraulic plant capacity; mechanical stop/physical stroke limit so control-failure mass flow to the propane absorber does not exceed cryogenic flare design flow (DBM-Deepcut SEC-06).
R-3.6 Turbo-expander/compressor: common-shaft expander and centrifugal compressor; expansion ratio 0.3961 expected; IGVs sized for 125% normal design flow; anti-surge recycle via flow control valve (DBM-Deepcut SEC-06).
R-3.7 Turbo-expander utilities: seal-gas supply from downstream of sales coalescer with SCR-controlled electric heater and 2x100% duplex filters; oil-lubricated journal bearings; 2x100% lead/lag lube-oil pumps; aerial lube-oil cooler in expander building; dual bladder lube-oil accumulators sized for at least one minute of lube-oil flow after ESD; duplex lube-oil filters; x/y bearing vibration monitoring (DBM-Deepcut SEC-06).
R-3.8 Propane absorber: 10 actual valve trays; jet/downcomer flood <=70%; mesh demister (DBM-Deepcut SEC-06).
R-3.9 Absorber bottoms pumps: 2x115%; single-stage vertical inline API-610; dual mechanical seal API-682 Plan 14/52; 60 psid differential winter-case; space/anti-condensation heater (DBM-Deepcut SEC-06).
R-3.10 Deethanizer: 35 actual valve trays; flood <=70%; refluxed and reboiled; winter operation expected to govern design; no demister (DBM-Deepcut SEC-06).
R-3.11 Deethanizer reflux pumps: 2x115%; single-stage vertical inline API-610; dual mechanical seal API-682 Plan 14/52 or modified 13/52; 50 psid differential winter-case (DBM-Deepcut SEC-06).
R-3.12 Deethanizer reboiler: TEMA BKU; heat medium on tube side at 350 degF; minimum 25 degF (13.9 degC) approach in expander mode (DBM-Deepcut SEC-06).
R-3.13 Expander aftercooler: air cooler; summer outlet 110 degF; pressure drop <4 psi summer; fan-speed and manual louver control (DBM-Deepcut SEC-06).
R-3.14 Methanol system: atmospheric double-walled methanol tank adjacent to expander building; pure methanol tank design SG 1.00 (TBC); triplex reciprocating injection pump (DBM-Deepcut SEC-06).

### R-4 Controls and Protective Functions
R-4.1 J-T valve pressure control with mechanical stroke limitation for flare-flow control failure (DBM-Deepcut SEC-06 table 1363).
R-4.2 Turbo-expander anti-surge recycle (DBM-Deepcut SEC-06).
R-4.3 Seal-gas and lube-oil permissive interlocks; lube-oil accumulators sized for ESD rundown (DBM-Deepcut SEC-06).
R-4.4 BAHX A-pass bypass temperature control; E-pass bypass for MDMT protection (DBM-Deepcut SEC-06).
R-4.5 Methanol injection at BAHX pass inlets (upstream of strainers), J-T valve inlet, and inlet-separator points; required injection points and capacities are TBC (DBM-Deepcut SEC-06).
R-4.6 Cryogenic dry-out performed at low pressure (DBM-Deepcut SEC-06).

### R-5 Equipment Roster (binding identity)
R-5.1 The package shall comprise the 15 equipment items rostered in DBM-Deepcut SEC-10 Package Line-Item Requirements row 9: AC-6390-1, AC-6392-1, XK-6300-1, XT-6300-1, E-6210-1, E-6285-1, P-6280-1, P-6281-1, P-6250-1, P-6251-1, T-6260-1, T-6240-1, V-6275-1, V-6286-1, V-6230-1.

### R-6 Multi-Unit / Sparing
R-6.1 ASSUMPTION: Cryogenic Unit is a single-train package at 04-25 (package roster shows one entry; no "Unit 2" listing in package roster for Cryogenic Unit). Confirm in detailed engineering (DBM-Deepcut SEC-10 Package Roster).

### R-7 Site / Layout Conditions Inherited
R-7.1 Climate basis: Dawson Creek BC; NBCC 2020 IDF worst-case (DBM-Deepcut SEC-02).
R-7.2 Spacing criteria (process-equipment, electrical-equipment, fired-equipment, flare/incinerator) per DBM-Deepcut SEC-02 minimum-spacing tables shall be respected at package boundary; final placement TBD pending CIV-235633-5002.

## Standards

| Standard | Application | Location |
|---|---|---|
| ALPEMA 3rd Edition | BAHX design | DBM-Deepcut SEC-06 |
| ASME BPVC Section VIII Div 1 (U Stamp) | BAHX/pressure vessels | DBM-Deepcut SEC-06 (U Stamp); ASMEcitation `location TBD` |
| BC CRN | Pressure equipment registration | DBM-Deepcut SEC-06 |
| API 610 | Absorber bottoms & deethanizer reflux pumps | DBM-Deepcut SEC-06 |
| API 682 (Plan 14/52 or modified 13/52) | Pump mechanical seals | DBM-Deepcut SEC-06 |
| TEMA (BKU type) | Deethanizer reboiler | DBM-Deepcut SEC-06 |
| API 2510 (LPG spacing) | Spacing requirements influencing package siting | DBM-Deepcut SEC-02 |
| BCER equipment spacing | Spacing guidance | DBM-Deepcut SEC-02 |
| CEC | Electrical equipment spacing (7.5 m MCC-to-process) | DBM-Deepcut SEC-02 |
| OGAOM Sec. 9.6.15 | Fired-equipment and flare/incinerator spacing | DBM-Deepcut SEC-02 |
| NBCC 2020 | Site climate / structural loading basis | DBM-Deepcut SEC-02 |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1.x Functional / recovery | Process simulation review; expander-mode and J-T-mode performance demonstration; performance test (PTC) during commissioning |
| R-2.x Design conditions | Vendor design-basis document review against DBM-Deepcut SEC-06 values; datasheet review |
| R-3.1-3.4 BAHX | Vendor design report; ALPEMA compliance statement; ASME U Stamp + CRN registration certificates; FAT pressure test |
| R-3.5 J-T valve | Stroke-limit verification; control-failure flow calculation review |
| R-3.6-3.7 Turbo-expander | Vendor mechanical run test; lube-oil/seal-gas FAT; bearing vibration baseline; accumulator rundown duration test |
| R-3.8-3.13 Columns/pumps/exchangers | API-compliant datasheets; FAT per applicable code; hydrotests; performance curves |
| R-3.14 Methanol system | Tank construction certification; pump performance test |
| R-4.x Controls | Cause-and-effect review; SIL/SIS verification per project requirements (TBD); interlock FAT |
| R-5.1 Roster | Bill-of-materials traceability against DBM-Deepcut SEC-10 |
| R-6.1 Sparing assumption | Human ruling (Conflict Table) |
| R-7.x Site/layout | Layout review against CIV-235633-5002 once issued |

## Documentation

The package shall deliver (anticipated artifacts per `_CONTEXT.md`):
- Vendor package design basis
- Equipment datasheets for all 15 rostered items
- General arrangement and piping isometrics for the package skids
- P&IDs for the cryogenic unit boundary
- Control narrative (cause-and-effect, interlock matrix)
- Vendor inspection and test plan (ITP); FAT reports; certification packages (ASME, CRN, ALPEMA)
- Mercury-tolerance design report (BAHX) — location TBD
- Vendor turnover package handoff to DEL-075-05
