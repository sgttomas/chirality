# Datasheet — DEL-075-04 Vendor Engineered Equipment Package (Cryogenic Unit "Deepcut")

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-075-04_vendor-engineered-equipment-package | `_CONTEXT.md` |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | PKG-075 — Cryogenic Unit ("Deepcut") | `_CONTEXT.md` |
| Workbook Row | Packages row 52 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Source Heading | 26020-Package_Requirements.docx package heading 29 | `_CONTEXT.md` (location TBD — binary not parsed) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Facility | West Doe Deepcut Expansion, 04-25 (LSD 04-25-80-15W6, ~22.2 km N of Dawson Creek, BC) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-01 |
| Package Roster Total Equipment | 15 line items | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-10 Package Roster |
| Technology Basis | UltraTEF cryogenic turbo-expander process | DBM-Deepcut SEC-01, SEC-06 |

## Attributes (Package-Level)

| Attribute | Value | Source |
|---|---|---|
| Function | Recover propane and heavier hydrocarbons (C3+) from molecular-sieve-dried gas while producing sales gas | DBM-Deepcut SEC-06 Process Description |
| Normal operating mode | Expander mode | DBM-Deepcut SEC-06 |
| Alternate operating mode | J-T mode (start-up / off-design / expander OOS) | DBM-Deepcut SEC-06 |
| C3 recovery (expander) | 99+% | DBM-Deepcut SEC-06 UltraTEF Design Values |
| C3 recovery (J-T) | >=27% expected minimum (sales-gas total-sulphur driver) | DBM-Deepcut SEC-06 |
| C4+ recovery (expander) | 100% iC4, nC4, iC5, nC5, C6+ | DBM-Deepcut SEC-06 |
| Deethanizer bottoms C2/C3 | operating target <=6.54 mol%; design <=1.5 mol% | DBM-Deepcut SEC-06 (table value "<=654 mol%" reads as 6.54 mol%; **ASSUMPTION** decimal corrected — flagged in Conflict Table) |
| Equipment tag list (15) | AC-6390-1, AC-6392-1, XK-6300-1, XT-6300-1, E-6210-1, E-6285-1, P-6280-1, P-6281-1, P-6250-1, P-6251-1, T-6260-1, T-6240-1, V-6275-1, V-6286-1, V-6230-1 | DBM-Deepcut SEC-10 Package Line-Item Requirements row 9 |

## Design Conditions

| Parameter | Design Basis | Source |
|---|---|---|
| Inlet flow (winter design) | 307.6 MMSCFD | DBM-Deepcut SEC-06 |
| Inlet flow (summer design) | 303 MMSCFD | DBM-Deepcut SEC-06 |
| Inlet temperature (winter) | 14.2 degC | DBM-Deepcut SEC-06 |
| Inlet temperature (summer) | 40.5 degC | DBM-Deepcut SEC-06 |
| Inlet pressure (design) | 7129 kPag (low/high TBC) | DBM-Deepcut SEC-06 |
| Cryogenic water-dewpoint limit | < -75 degC at highest operating pressure | DBM-Deepcut SEC-06 |
| Maximum BAHX design temperature | 150 degF (66 degC) | DBM-Deepcut SEC-06 UltraTEF Equipment table |
| BAHX corrosion allowance | 0 mm | DBM-Deepcut SEC-06 |
| BAHX excess area | >=10% on all passes | DBM-Deepcut SEC-06 |
| Sales pressure (expander, summer) | 3068 kPag design | DBM-Deepcut SEC-06 |
| Sales pressure (expander, winter) | 3289 kPag expected | DBM-Deepcut SEC-06 |
| Expander aftercooler summer outlet | 110 degF (sales gas) | DBM-Deepcut SEC-06 |
| Deethanizer reboiler heat-medium supply | 350 degF; min 25 degF (13.9 degC) approach in expander mode | DBM-Deepcut SEC-06 |
| Methanol tank specific gravity | 1.00 (TBC) | DBM-Deepcut SEC-06 |
| Site climate-data basis | Dawson Creek, BC; NBCC 2020 IDF worst-case | DBM-Deepcut SEC-02 |

## Construction (Package Composition)

| Sub-system | Description | Source |
|---|---|---|
| BAHX | Six-pass brazed aluminum exchanger; ALPEMA 3rd Ed. + vendor practice (with exceptions); ASME U Stamp; BC CRN; mercury-tolerant features TBD | DBM-Deepcut SEC-06 |
| Cold separator | Two-phase, mesh/vane demister; overheads to J-T valve or turbo-expander inlet; level to BAHX B-pass | DBM-Deepcut SEC-06 |
| J-T valve | Cold-separator backpressure control; full hydraulic-capacity sized; mechanical stroke limit for cryo flare protection | DBM-Deepcut SEC-06 |
| Turbo-expander / compressor | Common-shaft, shared lube/seal-gas; expansion ratio ~0.3961; IGVs sized to 125% normal design flow; single-stage radial centrifugal compressor (typical ratio 1.3); anti-surge recycle | DBM-Deepcut SEC-06 |
| Expander utilities | Seal-gas filtration (2x100% duplex), SCR-controlled electric seal-gas heater, oil-lubricated journal bearings, 2x100% lead/lag lube-oil pumps, aerial lube-oil cooler, dual bladder accumulators sized for >=1 min ESD rundown, x/y bearing vibration monitoring | DBM-Deepcut SEC-06 |
| Propane absorber | Refluxed absorber, mesh demister, 10 actual valve trays, flood <=70% | DBM-Deepcut SEC-06 |
| Absorber bottoms pumps | 2x115%, vertical inline API-610, dual mech seal API-682 Plan 14/52; 60 psid differential winter-case | DBM-Deepcut SEC-06 |
| Deethanizer | Refluxed/reboiled column, 35 valve trays, flood <=70%, no demister, winter governs | DBM-Deepcut SEC-06 |
| Deethanizer condenser | BAHX E-pass partial condenser; reflux LTCS; E-pass bypass for MDMT | DBM-Deepcut SEC-06 |
| Deethanizer reflux pumps | 2x115%, vertical inline API-610, dual mech seal API-682 Plan 14/52 or modified 13/52; 50 psid differential winter-case | DBM-Deepcut SEC-06 |
| Deethanizer reboiler | TEMA BKU, heat medium on tube side, 350 degF supply | DBM-Deepcut SEC-06 |
| Methanol storage / pump | Atmospheric double-walled methanol tank; triplex reciprocating injection pump | DBM-Deepcut SEC-06 |
| Expander aftercooler | Air cooler; fan-speed + manual louvers; summer design 110 degF outlet, <4 psi dP | DBM-Deepcut SEC-06 |

## Open Items / TBDs (carried from source)

- J-T-mode C4+ recoveries, low/high inlet pressures, J-T sales flows and sales pressure — TBC (DBM-Deepcut SEC-06).
- Methanol injection points and capacities; methanol tank SG 1.00 — TBC.
- BAHX mercury-tolerant features, strainer access, two-phase strainer dP, A-pass bypass capacity, F-pass bleed concept — require detailed engineering.
- Future NGL interface (deethanizer bottoms exchanger/cooler) — TBD.
- Inlet/sales composition appendix details — external, location TBD.
- Vendor identity, vendor scope, datasheet pack, factory testing matrix — TBD (no vendor selection evidence in scope).
- Plot plan CIV-235633-5002 (drives equipment placement constraints for the package) — not available in source set (DBM-Deepcut SEC-02).

## References

- `_REFERENCES.md` (deliverable-local)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-01, SEC-02, SEC-06, SEC-10) — read for this draft
- `26020-Package_Requirements.docx` package heading 29 — listed in `_REFERENCES.md`; binary not parsed; location TBD
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot) — for SOW/OBJ associations
