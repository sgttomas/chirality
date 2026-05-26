# Package Datasheet — Specification — PKG-075 Cryogenic Unit ("Deepcut")

DeliverableID: DEL-075-02_package-datasheet
DecompositionRef: GATE-07_Final_Published_2026-05-24

## Scope

This specification defines the normative engineering, design, fabrication, documentation, and interface basis to be carried in the PKG-075 Cryogenic Unit ("Deepcut") **Package Datasheet** for issue to the Package Vendor and to support EPC Integrator handoff. It applies to the UltraTEF cryogenic recovery unit defined as tag 26020-01-PT-28-001 (PACKAGE_REGISTER.csv PKG-075).

In scope: cold separator, J-T valve and turbo-expander/compressor train, six-pass BAHX, methanol injection system, propane absorber, absorber bottoms pumps, deethanizer with reflux system and reboiler, deethanizer condenser (BAHX E-pass), expander aftercooler, expander building utilities, and the 12 declared package interface types (DELIVERABLE_REGISTER.csv DEL-075-02; INTERFACE_REGISTER.csv PKG-075).

Out of scope (carried as interfaces only): upstream amine, TEG, molecular-sieve, MRU, and dust filtration packages; downstream sales-gas compression; NGL mercaptan treating and NGL molecular-sieve dehydration; product storage; flare/incinerator systems; whole-facility integration (owned by EPC Integrator per PACKAGE_REGISTER.csv responsibility split).

## Requirements

### R1 — Process duty
- R1.1 The package SHALL recover propane and heavier hydrocarbons from molecular-sieve-dried inlet gas while producing sales gas (SourcePath: DBM SEC-06; SectionRef: "Process Description").
- R1.2 The package SHALL achieve C3 recovery of 99+% in expander mode at design (SourcePath: DBM SEC-06; SectionRef: "UltraTEF Design Values").
- R1.3 In J-T mode the package SHALL achieve a minimum C3 recovery sufficient to support sales-gas total-sulphur compliance; ≥27% is the expected minimum (SourcePath: DBM SEC-06; SectionRef: "UltraTEF Design Values" / "Operating Modes").
- R1.4 The deethanizer bottoms C2/C3 SHALL meet the design ≤1.5 mol% (operating target read as ≤0.654 mol% — ASSUMPTION: source token "<=654 mol%" is interpreted as decimal typo; location TBD pending human ruling) (SourcePath: DBM SEC-06; SectionRef: "UltraTEF Design Values").

### R2 — Design conditions
- R2.1 Design inlet flow: 307.6 MMSCFD (winter) / 303 MMSCFD (summer) (SourcePath: DBM SEC-06; SectionRef: "UltraTEF Design Values").
- R2.2 Design inlet temperature: 14.2 °C (winter) / 40.5 °C (summer) immediately upstream of cryogenic unit inlet ESDV (SourcePath: DBM SEC-06; SectionRef: "UltraTEF Design Values").
- R2.3 Design inlet pressure: 7,129 kPag; low/high pressures TBC (SourcePath: DBM SEC-06; SectionRef: "UltraTEF Design Values").
- R2.4 BAHX and turbo-expander SHALL be designed for the summer/expander-mode single design point; winter operation is expected performance and SHALL be hydraulically verified for towers, pumps, and deethanizer reboiler (SourcePath: DBM SEC-06; SectionRef: "UltraTEF Cryogenic Recovery Basis — Process Description").
- R2.5 Site environmental loads SHALL be per DBM SEC-02 (ambient −40 / +35 °C design; snow Ss 2.5 kPa; q 1/50 wind 0.40 kPa; Sa(0.2) 0.253; elevation 673 m AMSL).

### R3 — BAHX (Brazed Aluminum Heat Exchanger)
- R3.1 BAHX SHALL be a six-pass core designed per ALPEMA 3rd Edition and manufacturer standard practices with documented vendor exceptions (SourcePath: DBM SEC-06; SectionRef: "BAHX").
- R3.2 BAHX SHALL carry ASME U Stamp and BC CRN.
- R3.3 BAHX SHALL provide ≥10% excess area on all passes with 0 mm corrosion allowance and maximum design temperature 150 °F (66 °C).
- R3.4 BAHX SHALL include methanol injection headers on each pass inlet and tee strainers upstream of each pass with start-up fine mesh and normal baskets.
- R3.5 BAHX strainers SHALL have clean ΔP < 2 psid and SHALL be changed at ≤15 psid.
- R3.6 BAHX SHALL include an automated A-pass bypass with capacity 15–20% of maximum inlet flow (TBC), controlled by cold-separator overhead temperature.
- R3.7 BAHX mercury-tolerant features SHALL be developed by the Vendor (TBD details).

### R4 — Turbo-expander/compressor and utilities
- R4.1 The turbo-expander/compressor SHALL be common-shaft with shared lube-oil and seal-gas systems (SourcePath: DBM SEC-06; SectionRef: "Turbo-expander/compressor").
- R4.2 Expander expansion ratio is approximately 0.3961; inlet guide vanes SHALL be sized for 125% of normal design flow.
- R4.3 Compressor SHALL be single-stage open-impeller radial centrifugal with typical compression ratio 1.3 and anti-surge recycle from discharge to inlet via flow control valve.
- R4.4 Seal-gas source SHALL be sweet sales gas from downstream of the sales coalescer; seal gas SHALL be available before and during lube-oil circulation.
- R4.5 Utilities SHALL include: SCR-controlled electric seal-gas heater; 2 × 100% duplex seal-gas filters; oil-lubricated journal bearings; 2 × 100% lead/lag gear lube-oil pumps; aerial lube-oil cooler within the expander building; dual bladder lube-oil accumulators sized for ≥1 minute of lube-oil flow after ESD; duplex lube-oil filters; x/y bearing vibration monitoring (SourcePath: DBM SEC-06; SectionRef: "Turbo-expander utilities").

### R5 — J-T valve and protective basis
- R5.1 The J-T valve SHALL control cold-separator backpressure and SHALL be sized for full hydraulic plant capacity so sales compressor suction can run at normal operating conditions (SourcePath: DBM SEC-06; SectionRef: "J-T valve").
- R5.2 A mechanical stop or physical stroke limit SHALL be provided such that the control-failure mass flow to the propane absorber does not exceed cryogenic flare design flow.
- R5.3 J-T valve trim capacity for condensing liquids is TBC.

### R6 — Towers and pumps
- R6.1 Propane absorber SHALL be a refluxed column with 10 actual valve trays, mesh demister, jet and downcomer flood ≤70% (SourcePath: DBM SEC-06; SectionRef: "Propane absorber").
- R6.2 Absorber bottoms pumps SHALL be 2 × 115% single-stage vertical inline API-610 light-hydrocarbon pumps with dual mechanical seals per API-682 Plan 14/52; 60 psid differential winter-case design; anti-condensation heater.
- R6.3 Deethanizer SHALL be a refluxed/reboiled fractional distillation column with 35 actual valve trays, no demister, jet/downcomer flood ≤70%; winter operation is expected to govern design (SourcePath: DBM SEC-06; SectionRef: "Deethanizer").
- R6.4 Deethanizer condenser SHALL be the BAHX E-pass partial condenser with low-ΔP temperature-control valves for E-pass inlet restriction and bypass; reflux system SHALL use low-temperature carbon steel; bypass SHALL prevent exceeding MDMT (SourcePath: DBM SEC-06; SectionRef: "Deethanizer condenser").
- R6.5 Deethanizer reflux pumps SHALL be 2 × 115% API-610 vertical inline, 50 psid winter-case, dual mechanical seal API-682 Plan 14/52 or modified 13/52; anti-condensation heater.
- R6.6 Deethanizer reboiler SHALL be TEMA BKU with hot oil on the tube side; heat medium 350 °F via mixing valves; minimum approach 25 °F (13.9 °C) in expander mode.

### R7 — Methanol system
- R7.1 The methanol injection system SHALL be designed to inject into one point at a time with injection points at: BAHX pass inlets upstream of strainers; J-T valve inlet; inlet separators upstream of PCV; inlet separators upstream of HCL and water dump valves; acid gas compressor package; design capacities TBC (SourcePath: DBM SEC-06; SectionRef: "Methanol injection").
- R7.2 Methanol storage SHALL be an atmospheric double-walled tank adjacent to the expander building; pure methanol design specific gravity 1.00 TBC; triplex reciprocating injection pump.

### R8 — Controls and protective functions
- R8.1 Controls SHALL include: J-T valve pressure control with mechanical stroke limitation for flare-flow control failure; turbo-expander anti-surge recycle; seal-gas and lube-oil permissives; lube-oil accumulators for ESD rundown; BAHX A-pass bypass temperature control; E-pass bypass for MDMT protection; methanol injection for hydrate/freezing management; low-pressure cryogenic dry-out (SourcePath: DBM SEC-06; SectionRef: "Process Controls and Protective Functions").
- R8.2 Cryogenic-service water dewpoint SHALL be maintained < −75 °C at highest operating pressure to prevent continuous freezing (governed upstream by molecular sieves) (SourcePath: DBM SEC-06; SectionRef: Molecular-sieve dehydration table).

### R9 — Interfaces
- R9.1 The Vendor SHALL coordinate with the EPC Integrator on all 12 declared package interface types (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) (SourcePath: GATE-07 INTERFACE_REGISTER.csv; SectionRef: PKG-075 rows).
- R9.2 The package SHALL deliver deethanizer bottoms to downstream NGL treating; the future bottoms exchanger/cooler provisions (R6/R-list) SHALL be retained as future interface (SourcePath: DBM SEC-06; SectionRef: "Future deethanizer bottoms exchanger" / "Future deethanizer bottoms cooler").

### R10 — Layout
- R10.1 The cryogenic area SHALL be outdoor modules adjacent to the molecular-sieve modules, with the turbo-expander/compressor in a building (SourcePath: DBM SEC-06; SectionRef: "UltraTEF cryogenic area").
- R10.2 Plot-level placement and spacing SHALL conform to DBM SEC-02 layout principles and to plot plan CIV-235633-5002 once available (TBD: plot plan not in available source package).

## Standards

| Standard / code | Application | Source |
|---|---|---|
| ALPEMA 3rd Edition | BAHX design | DBM SEC-06 "BAHX" |
| ASME (U Stamp) | BAHX code stamp | DBM SEC-06 "BAHX" |
| BC CRN | BAHX provincial registration | DBM SEC-06 "BAHX" |
| API 610 | Absorber bottoms and deethanizer reflux pumps | DBM SEC-06 "Absorber bottoms pumps" / "Deethanizer reflux pumps" |
| API 682 (Plan 14/52; or modified 13/52 for reflux pumps) | Pump mechanical seals | DBM SEC-06 "Absorber bottoms pumps" / "Deethanizer reflux pumps" |
| TEMA (Type BKU) | Deethanizer reboiler | DBM SEC-06 "Deethanizer reboiler" |
| TEMA (Type NEN) | Future deethanizer bottoms exchanger | DBM SEC-06 "Future deethanizer bottoms exchanger" |
| NBC 2020 (Dawson Creek climate data); BC Building Code 2018 site basis | Civil/structural climate loads | DBM SEC-02 "Site Data Basis" |
| BCER spacing guidelines; API 2510; NFPA 30; OGAOM Sec. 9.6.15; OGPFR Appendix 1 | Plot-spacing reference (whole-facility; package layout shall be compatible) | DBM SEC-02 "Minimum Spacing Criteria" |
| 26020-Package_Requirements.docx package heading 29 | Package-requirements addendum (location TBD: binary docx not parsed) | _REFERENCES.md |

## Verification

| Requirement | Verification approach |
|---|---|
| R1.1–R1.4 (recovery, bottoms spec) | Process simulation review (vendor model + EPC review); performance test in expander mode at design conditions; sampled lab confirmation of deethanizer bottoms C2/C3. |
| R2.x (design conditions) | Datasheet review against DBM SEC-06 table; PHA confirmation; hydraulic check of winter expected case. |
| R3.x (BAHX) | ALPEMA / ASME / CRN documentation review; FAT; strainer ΔP commissioning record; mercury-tolerant feature design review. |
| R4.x (expander/compressor + utilities) | Mechanical FAT; lube-oil accumulator timed ESD test; seal-gas availability interlock test; vibration monitoring loop check. |
| R5.x (J-T valve) | Sizing calculation review; mechanical stop verification; failure-flow check against cryogenic flare design. |
| R6.x (towers + pumps) | Tower hydraulic review (jet/downcomer flood); pump FAT (API-610/682); reboiler approach check at expander-mode design. |
| R7.x (methanol) | Injection-point P&ID review; capacity confirmation (TBC); tank/pump FAT. |
| R8.x (controls) | Loop checks; SIS/ESD validation; A-pass bypass and E-pass MDMT bypass functional tests; cryogenic dry-out procedure dry run. |
| R9.x (interfaces) | Interface matrix review with EPC Integrator; tie-in walkdown; commissioning interface checklist. |
| R10.x (layout) | Plot-plan compatibility review against CIV-235633-5002 when issued. |

## Documentation

Required documentation deliverables to be provided with the Package Datasheet handoff (per anticipated artifacts in DELIVERABLE_REGISTER.csv DEL-075-02 and DBM SEC-06 requirements):

- Package technical datasheet (this document set).
- Vendor engineering handoff basis (PFD, heat & material balance, mechanical datasheets per major equipment item, BAHX vendor design summary).
- Package interface requirements matrix (12 interface types per INTERFACE_REGISTER.csv).
- Source-supported equipment and design criteria (this Specification + Datasheet).
- ALPEMA / ASME U Stamp / BC CRN certification packages for BAHX.
- API-610 / API-682 mechanical datasheets and FAT reports for pumps.
- Turbo-expander/compressor mechanical datasheets, lube-oil and seal-gas system schematics, vibration monitoring scheme.
- Cause-and-effect matrix and SIS specification covering the protective functions in R8.
- Methanol injection P&ID and capacity calculations.
- Open-items register listing all DBM-flagged TBD/TBC items at handoff.
