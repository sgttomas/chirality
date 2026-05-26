# Package Datasheet — PKG-075 Cryogenic Unit ("Deepcut")

DeliverableID: DEL-075-02_package-datasheet
ParentPackageID: PKG-075
PackageTag: 26020-01-PT-28-001 — Cryogenic Deep Cut Package
Discipline: Mechanical
ResponsibleParty: EPC Integrator
DecompositionRef: GATE-07_Final_Published_2026-05-24

## Identification

| Field | Value | Source |
|---|---|---|
| Package name | Cryogenic Unit ("Deepcut") | PACKAGE_REGISTER.csv (PKG-075) |
| Package tag | 26020-01-PT-28-001 | PACKAGE_REGISTER.csv (PKG-075) |
| WBS | 01 | PACKAGE_REGISTER.csv (PKG-075) |
| Workbook row | 52 | PACKAGE_REGISTER.csv (PKG-075) |
| Discipline | Mechanical | PACKAGE_REGISTER.csv (PKG-075) |
| Technology basis | UltraTEF cryogenic turbo-expander gas processing | DBM SEC-01 "Terminology Basis"; SEC-06 "UltraTEF Cryogenic Recovery Basis" |
| Facility | West Doe Deepcut expansion (04-25), 22.2 km N of Dawson Creek, BC | DBM SEC-01 "Facility Identity" |
| Owner / proponent | Tourmaline Oil Corporation | DBM SEC-01 "Facility Identity" |
| Field construction responsibility | Tourmaline Oil Corporation | DBM SEC-01 "Construction Responsibility" |
| Package vendor / EPC split | Package Vendor: package engineering, design, vendor documentation, physical equipment. EPC Integrator: facility integration, interfaces, tie-ins, constructability. | PACKAGE_REGISTER.csv (PKG-075); DELIVERABLE_REGISTER.csv (DEL-075-02) |

## Attributes (Service and Capacity)

| Attribute | Value | Source |
|---|---|---|
| Function | Recover propane and heavier hydrocarbons (C3+) from molecular-sieve-dried sour gas while producing sales gas | DBM SEC-06 "UltraTEF Cryogenic Recovery Basis — Process Description" |
| Design inlet flow — winter | 307.6 MMSCFD | DBM SEC-06 "UltraTEF Design Values" |
| Design inlet flow — summer | 303 MMSCFD | DBM SEC-06 "UltraTEF Design Values" |
| Design inlet temperature — winter | 14.2 °C (upstream of cryogenic unit inlet ESDV) | DBM SEC-06 "UltraTEF Design Values" |
| Design inlet temperature — summer | 40.5 °C (upstream of cryogenic unit inlet ESDV) | DBM SEC-06 "UltraTEF Design Values" |
| Design inlet pressure | 7,129 kPag (low/high TBC) | DBM SEC-06 "UltraTEF Design Values" |
| Propane (C3) recovery — expander mode | 99+% | DBM SEC-06 "UltraTEF Design Values" |
| Propane (C3) recovery — J-T mode | >27% expected minimum (for sales-gas total sulphur compliance) | DBM SEC-06 "UltraTEF Design Values"; SEC-06 "UltraTEF Operating Modes" |
| C4+ recovery — expander mode | 100% for iC4, nC4, iC5, nC5, C6+; J-T mode values TBC | DBM SEC-06 "UltraTEF Design Values" |
| Deethanizer bottoms C2/C3 design | ≤1.5 mol% (operating target ≤0.654 mol% — value cited as "<=654 mol%" in source; corrected reading) | DBM SEC-06 "UltraTEF Design Values" (CONFLICT: source string "<=654 mol%" appears typographic; treated as ASSUMPTION pending human ruling) |
| Sales flow at BAHX C-pass outlet — expander mode | Winter 286 MMSCFD; summer 281.2 MMSCFD | DBM SEC-06 "UltraTEF Design Values" |
| Sales pressure — expander mode | Summer 3,068 kPag (design); winter 3,289 kPag (expected) | DBM SEC-06 "UltraTEF Design Values" |
| Operating modes | Expander mode (normal); J-T mode (start-up / off-design); Dry-out / start-up | DBM SEC-06 "UltraTEF Operating Modes" |

## Conditions and Service

| Condition | Value | Source |
|---|---|---|
| Service | Sour, dehydrated, mercury-protected hydrocarbon gas (post amine, TEG, mol-sieve, MRU) | DBM SEC-06 "Process Description" |
| Upstream inlet protection | Molecular-sieve dehydration with MRU and dust filter upstream of cryogenic inlet ESDV | DBM SEC-06 "Process Description"; "Process Controls and Protective Functions" |
| Water-dewpoint limit (cryogenic unit) | < −75 °C at highest operating pressure (continuous-freezing prevention) | DBM SEC-06 (Molecular-Sieve table) |
| Methanol injection (hydrate/freeze management) | Required at: BAHX pass inlets upstream of strainers; J-T valve inlet; inlet separators upstream of PCV; inlet separators upstream of HCL and water dump valves; acid gas compressor package. Capacities TBC. | DBM SEC-06 "UltraTEF Equipment and Design Requirements — Methanol injection" |
| Methanol storage | Atmospheric double-walled tank adjacent to expander building; triplex reciprocating injection pump; design SG 1.00 TBC | DBM SEC-06 "Methanol storage and pump" |
| Ambient design | −40 °C min / +35 °C max (DBM site basis) | DBM SEC-02 "Site Data Basis" |
| Plant elevation | 673 m AMSL | DBM SEC-02 "Site Data Basis" |
| Atmospheric pressure | 93.3 kPa(a) | DBM SEC-02 "Site Data Basis" |
| Snow load Ss / Sr | 2.5 kPa / 0.2 kPa | DBM SEC-02 "Site Data Basis" |
| Wind pressure q 1/50 | 0.40 kPa | DBM SEC-02 "Site Data Basis" |
| Seismic Sa(0.2) | 0.253 | DBM SEC-02 "Site Data Basis" |

## Construction (Equipment List)

| Tag / Equipment | Description | Key design requirement | Source |
|---|---|---|---|
| Cold separator | Two-phase separator on BAHX A-pass outlet; mesh/vane demister | Demister sized on expander-mode liquid density; J-T mode governs gas volumetric flow | DBM SEC-06 "UltraTEF Equipment and Design Requirements — Cold separator" |
| J-T valve | Backpressure control of cold separator | Sized for full hydraulic plant capacity; mechanical/stroke limit so failure flow ≤ cryogenic flare design flow; trim capacity TBC | DBM SEC-06 "J-T valve" |
| Turbo-expander/compressor | Common-shaft expander–compressor with shared lube oil and seal-gas | Expander expansion ratio ~0.3961; IGVs sized for 125% normal design flow; single-stage open-impeller centrifugal compressor, compression ratio ~1.3; anti-surge recycle via FCV | DBM SEC-06 "Turbo-expander/compressor" |
| Turbo-expander utilities | Seal-gas (from sales coalescer downstream), SCR electric seal-gas heater, 2×100% duplex seal-gas filters, 2×100% lube-oil pumps, aerial lube-oil cooler in expander building, dual bladder lube-oil accumulators (≥1 min ESD rundown), duplex lube-oil filters, x/y vibration monitoring | Seal gas available before and during lube-oil circulation | DBM SEC-06 "Turbo-expander utilities" |
| BAHX (Brazed Aluminum Heat Exchanger) | Six-pass core | ALPEMA 3rd Ed. + mfr practice; ASME U Stamp; BC CRN; ≥10% excess area all passes; 0 mm CA; max design 150 °F (66 °C); methanol injection on each pass inlet header; tee strainers (start-up fine, normal baskets) upstream of each pass; mercury-tolerant features TBD | DBM SEC-06 "BAHX" |
| BAHX strainers | Per-pass inlet protection | Clean ΔP < 2 psid; service at ≤15 psid | DBM SEC-06 "BAHX strainers" |
| BAHX A-pass bypass | Automated bypass | 15–20% of max inlet flow (TBC); controlled by cold-separator overhead temperature | DBM SEC-06 "BAHX A-pass bypass" |
| BAHX F-pass bleed | Automated bleed valve + flow meter (F-pass inlet ↔ C-pass outlet) | For light-end recycle management; concept stage | DBM SEC-06 "BAHX F-pass bleed" |
| Methanol injection system | Single-point at-a-time injection | Capacities TBC | DBM SEC-06 "Methanol injection" |
| Propane absorber | Refluxed absorber column | 10 actual valve trays; jet and downcomer flood ≤70%; mesh demister; J-T or expander two-phase feed enters lower feed; overhead vapour to BAHX C-pass; bottoms pumped to BAHX D-pass | DBM SEC-06 "Propane absorber" |
| Absorber bottoms pumps | Light-HC pumps to BAHX D-pass and deethanizer intermediate feed | 2×115%; 60 psid winter-case design; single-stage vertical inline API-610; dual mech seal API-682 Plan 14/52; anti-condensation heater | DBM SEC-06 "Absorber bottoms pumps" |
| Deethanizer | Refluxed/reboiled fractional distillation column | 35 actual valve trays; jet/downcomer flood ≤70%; no demister; bottoms level controlled to downstream NGL treating (or future bottoms cooler); winter operation expected to govern; co-current trays may be evaluated | DBM SEC-06 "Deethanizer" |
| Deethanizer condenser | BAHX E-pass partial condenser | Low-ΔP temperature-control valves for E-pass restriction and bypass; reflux system in low-temperature carbon steel; bypass prevents exceeding MDMT | DBM SEC-06 "Deethanizer condenser" |
| Deethanizer reflux accumulator | Horizontal mesh/vane demister; methanol boot with manual drain to cryogenic drain header; LSH for boot | — | DBM SEC-06 "Deethanizer reflux accumulator" |
| Deethanizer reflux pumps | 2×115%; 50 psid winter-case; single-stage vertical inline API-610; dual mech seal API-682 Plan 14/52 or modified 13/52; anti-condensation heater | — | DBM SEC-06 "Deethanizer reflux pumps" |
| Deethanizer reboiler | TEMA BKU; hot oil tube side | Heat medium 350 °F via mixing valves; min approach 25 °F (13.9 °C) in expander mode | DBM SEC-06 "Deethanizer reboiler" |
| Future deethanizer bottoms exchanger | NEN shell-and-tube; future NGL-treating provision | 10 °F (5.56 °C) min approach; initial outlet target 48.8 °C | DBM SEC-06 "Future deethanizer bottoms exchanger" |
| Future deethanizer bottoms cooler | Future air cooler to downstream NGL mercaptan treating | Outlet 110 °F (38 °C); downstream caustic min 80 °F (26.7 °C); plenum/recirculation basis to be reviewed | DBM SEC-06 "Future deethanizer bottoms cooler" |
| Expander aftercooler | Air cooler on hot sales gas from expander-compressor discharge | Outlet 110 °F summer; ΔP < 4 psi summer; fan speed + manual louver control; winter <95 °F (35 °C) operation TBC | DBM SEC-06 "Expander aftercooler" |
| Package layout | Outdoor cryogenic modules: cold separator, J-T valve, turbo-expander/compressor building, six-pass BAHX, methanol injection, propane absorber, absorber bottoms pumps, deethanizer, reflux system, reboiler, future bottoms exchanger/cooler provisions, expander aftercooler | Adjacent to molecular-sieve modules | DBM SEC-06 "UltraTEF cryogenic area" |

## Interfaces (Package Boundaries)

| Interface type | Direction / role | Source |
|---|---|---|
| Process Piping | Mol-sieve-dried gas inlet from MRU/dust filter; sales gas to expander aftercooler then sales-gas compression header; deethanizer bottoms to downstream NGL treating | DBM SEC-06 "Process Description", "Interfaces"; INTERFACE_REGISTER.csv IFC-381FAF28BD |
| Utility Piping | Heat medium 350 °F to deethanizer reboiler; methanol supply; instrument air | DBM SEC-06 "Interfaces"; INTERFACE_REGISTER.csv IFC-434C7B5D15 |
| Relief / Flare / Vent | Cryogenic flare per J-T valve failure-flow basis; deethanizer/absorber reliefs; PSV protection | DBM SEC-06 "J-T valve"; INTERFACE_REGISTER.csv IFC-0704DE742B |
| Drain / Containment | Cryogenic drain header (deethanizer reflux accumulator methanol boot drain); package drain to plant drain system | DBM SEC-06 "Deethanizer reflux accumulator"; INTERFACE_REGISTER.csv IFC-353D0A224C |
| Electrical Power | Electric-driven expander seal-gas heater (SCR), lube-oil pumps, methanol pumps, motor-operated valves, building services | DBM SEC-06 "Turbo-expander utilities"; DBM SEC-01 (electrification basis); INTERFACE_REGISTER.csv IFC-281256F5AB |
| Grounding / Bonding | Standard facility basis | INTERFACE_REGISTER.csv IFC-F0848E5D35 (location TBD in source slices) |
| Area / Exterior Lighting | Standard facility basis | INTERFACE_REGISTER.csv IFC-F1FF9386E9 (location TBD in source slices) |
| I&C / Control Cabling | Plant PID/SIS for cold-separator overhead temperature (A-pass bypass), J-T valve PC, anti-surge FCV, ESD permissives, vibration monitoring | DBM SEC-06 "UltraTEF cryogenic unit" controls row |
| Building HVAC / Services | Expander building (lube-oil cooling); methanol storage adjacency | DBM SEC-06 "UltraTEF cryogenic area"; "Methanol storage" |
| Fire & Gas / Safety Systems | F&G coverage of expander building and outdoor cryogenic modules; ESD network | INTERFACE_REGISTER.csv IFC-9F39AF939C; DBM SEC-06 controls row (ESD rundown) |
| Maintenance Access | BAHX strainer access; pump and motor maintenance envelopes | DBM SEC-06 "BAHX" / "BAHX strainers"; DBM SEC-02 layout principles |
| Structural / Foundations / Supports | Multilevel modules; pipe rack adjacency to molecular-sieve modules | DBM SEC-06 "UltraTEF cryogenic area"; DBM SEC-02 "General Layout Basis" |

## References

- Source slice (authoritative): `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01, SEC-02, SEC-05, SEC-06, SEC-07.
- Package register row: GATE-07 PACKAGE_REGISTER.csv (PKG-075).
- Deliverable register row: GATE-07 DELIVERABLE_REGISTER.csv (DEL-075-02).
- Interface register: GATE-07 INTERFACE_REGISTER.csv (12 declared interface types for PKG-075).
- 26020-Package_Requirements.docx (package heading 29) — TBD location: binary .docx not parsed locally; package-requirements text not consulted.
- 26020-Packages_Interfaces_4_export.xlsx — TBD location: binary .xlsx not parsed locally.
