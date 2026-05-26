# Datasheet — DEL-075-01 Scope of Work (PKG-075 Cryogenic Unit "Deepcut")

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-075-01_scope-of-work` | `_CONTEXT.md` |
| Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-075` | `_CONTEXT.md` |
| Package Name | Cryogenic Unit ("Deepcut") | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | SOW-0063, SOW-0064, SOW-0065, SOW-0066 | `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION: package-grouping heuristic) |
| Source Reference | Workbook Packages row 52; 26020-Package_Requirements.docx package heading 29 | `_CONTEXT.md` |
| Anchor Source (locally accessible) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-06 "UltraTEF Cryogenic Recovery Basis", lines 1293-1396) | this run |

## Attributes (Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Process function | NGL recovery (propane and heavier) from molecular-sieve-dried gas while producing sales gas | DBM-Deepcut SEC-06 / "UltraTEF Cryogenic Recovery Basis / Process Description" (line 1297) |
| Technology | UltraTEF cryogenic recovery | DBM-Deepcut SEC-06 (line 1293) |
| Recovery basis (design point) | Summer ambient, expander-mode design point governs BAHX and turbo-expander; winter is expected performance and must be checked for hydraulics | DBM-Deepcut SEC-06 (lines 1299, 1305) |
| Normal operating mode | Expander mode | DBM-Deepcut SEC-06 / "UltraTEF Operating Modes" (line 1345) |
| Off-design mode | J-T mode (start-up / when turbo-expander is down) | DBM-Deepcut SEC-06 (lines 1297, 1346) |
| Vendor package model | UltraTEF cryogenic unit (vendor-supplied) | DBM-Deepcut SEC-06 (line 1293) — vendor identity location TBD |

## Conditions (Inlet / Sales Boundary Conditions)

| Parameter | Value | Source |
|---|---|---|
| Inlet flow (design winter) | 307.6 MMSCFD | DBM-Deepcut SEC-06 / UltraTEF Design Values (line 1306) |
| Inlet flow (design summer) | 303 MMSCFD | DBM-Deepcut SEC-06 (line 1306) |
| Inlet temperature (design winter) | 14.2 degC | DBM-Deepcut SEC-06 (line 1307) |
| Inlet temperature (design summer) | 40.5 degC | DBM-Deepcut SEC-06 (line 1307) |
| Inlet pressure (design) | 7129 kPag | DBM-Deepcut SEC-06 (line 1308) |
| Inlet measurement boundary | Immediately upstream of the cryogenic unit inlet ESDV | DBM-Deepcut SEC-06 (lines 1307-1308) |
| C3 recovery (expander mode) | 99+% | DBM-Deepcut SEC-06 (line 1309) |
| C3 recovery (J-T mode minimum) | >27% (to support total sulphur compliance) | DBM-Deepcut SEC-06 (line 1309) |
| Sales flow at BAHX C-pass outlet (expander, winter) | 286 MMSCFD | DBM-Deepcut SEC-06 (line 1312) |
| Sales flow at BAHX C-pass outlet (expander, summer) | 281.2 MMSCFD | DBM-Deepcut SEC-06 (line 1312) |
| Sales pressure (expander summer, design) | 3068 kPag | DBM-Deepcut SEC-06 (line 1313) |
| Sales pressure (expander winter, expected) | 3289 kPag | DBM-Deepcut SEC-06 (line 1313) |
| J-T-mode sales flow and pressure | TBC | DBM-Deepcut SEC-06 (lines 1312-1313) |
| Low/high inlet pressure | TBC | DBM-Deepcut SEC-06 (line 1308) |

## Construction (Package Tagged-Equipment List)

Tagged-equipment functional list (per DBM-Deepcut SEC-06 UltraTEF Equipment and Design Requirements, lines 1316-1340). Individual tag numbers (e.g., V-, E-, P-, K-, T- numbers) are not enumerated in the locally accessible source slice and are `TBD` pending package datasheet / P&IDs.

| Function / Equipment | Notable Source-Anchored Basis | Tag Number |
|---|---|---|
| Cold separator | Mesh/vane demister; expander-mode density sizing; J-T-mode actual gas volume governs | TBD |
| J-T valve | Pressure control on cold-separator backpressure; mechanical stroke limit for flare-flow protection | TBD |
| Turbo-expander / compressor | Common-shaft; expander ratio 0.3961; IGV sized 125% normal flow; compressor single-stage open-impeller radial centrifugal, ratio ~1.3; anti-surge recycle | TBD |
| Turbo-expander seal/lube utilities | Seal gas from sales coalescer; SCR-controlled electric heater; 2x100% duplex seal-gas filters; 2x100% lead/lag gear lube-oil pumps; aerial cooler; dual bladder accumulators; duplex lube-oil filters; x/y vibration monitoring | TBD |
| BAHX (six-pass brazed aluminum) | ALPEMA 3rd Ed. + manufacturer practice with exceptions; ASME U Stamp + BC CRN; min 10% excess area; max design 150 degF (66 degC); 0 mm CA; mercury-tolerant features TBD; per-pass methanol injection; per-pass tee strainers | TBD |
| BAHX strainers | Clean dP <2 psid; clean/change at max 15 psid | TBD |
| BAHX A-pass bypass | 15-20% of max inlet flow capacity (TBC); controlled by cold-separator overhead temperature | TBD |
| BAHX F-pass bleed | Automated bleed + flow meter (consideration) | TBD |
| Methanol injection system | Single-point-at-a-time; injection points enumerated (BAHX passes, J-T inlet, inlet separators upstream of PCV/HCL/water dump, acid-gas compressor) | TBD |
| Methanol storage and pump | Atmospheric double-walled tank; design SG 1.00 (TBC); triplex reciprocating injection pump | TBD |
| Propane absorber | Refluxed absorber; 10 actual valve trays; jet/downcomer flood <=70%; mesh demister | TBD |
| Absorber bottoms pumps | 2x115%; 60 psid winter-case; single-stage vertical inline API-610; API-682 Plan 14/52 dual mech seal | TBD |
| Deethanizer | 35 actual valve trays; refluxed + reboiled; jet/downcomer flood <=70%; co-current trays may be evaluated | TBD |
| Deethanizer condenser | BAHX E-pass partial condenser; LP-dP bypass for MDMT protection | TBD |
| Deethanizer reflux accumulator | Horizontal mesh/vane demister; methanol boot with manual drain to cryogenic drain | TBD |
| Deethanizer reflux pumps | 2x115%; 50 psid winter-case; API-610 / API-682 Plan 14/52 (or modified 13/52) | TBD |
| Deethanizer reboiler | TEMA BKU; hot oil tube-side; 350 degF heat medium; >=25 degF (13.9 degC) min approach in expander mode | TBD |
| Future deethanizer bottoms exchanger | NEN shell-and-tube; 10 degF (5.56 degC) min approach; target outlet 48.8 degC (future NGL interface provision) | TBD (future) |
| Future deethanizer bottoms cooler | Air cooler; design outlet 110 degF (38 degC); plenum heat basis TBD | TBD (future) |
| Expander aftercooler | Air cooler; 110 degF summer outlet; <4 psi dP summer; fan-speed + manual louver control; winter below 95 degF (35 degC) to be studied | TBD |

## References

- Authoritative source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-06 "Treating, Dehydration, and Cryogenic Recovery Basis" (lines 1098-1396), with primary anchor in "UltraTEF Cryogenic Recovery Basis" (lines 1293-1396).
- Decomposition row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 276.
- Referenced but not locally machine-readable: `_Sources/26020-Package_Requirements.docx` (heading 29). Content depending solely on this source is marked `TBD`.
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
