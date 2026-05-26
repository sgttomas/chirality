# Datasheet: DEL-075-06 — EPC Vendor Package Review and Acceptance (Cryogenic Unit / PKG-075)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-075-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-075` |
| PackageName | Cryogenic Unit ("Deepcut") — UltraTEF cryogenic recovery |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers SOW Items | `SOW-0063`, `SOW-0064`, `SOW-0065`, `SOW-0066` |
| Supports Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-heuristic mapping per `_CONTEXT.md`) |

## Attributes (subject vendor package)

| Field | Value | Source |
|---|---|---|
| Technology basis | UltraTEF cryogenic turbo-expander gas processing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L160; L1293-L1299 |
| Function | Recover propane and heavier hydrocarbons from molecular-sieve-dried gas while producing sales gas | DBM L1297 |
| Expected propane recovery (expander mode) | 99+ % | DBM L44; L1345 |
| Primary equipment | Six-pass BAHX, cold separator, J-T valve, turbo-expander/compressor, propane absorber, deethanizer, deethanizer reflux system, deethanizer reboiler, expander aftercooler, methanol injection | DBM L1297; L1320-L1339 |
| Installation form | Outdoor cryogenic modules adjacent to molecular-sieve dehydration module | DBM L1134-L1135 |
| Normal operating mode | Expander mode (summer-condition design point) | DBM L1299; L1305; L1345 |
| Off-design / start-up mode | J-T mode (minimum C3 recovery ≥27 % for sales-gas total sulphur compliance) | DBM L1346 |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Inlet temperature (design winter) | 14.2 °C | DBM L1307 |
| Inlet temperature (design summer) | 40.5 °C | DBM L1307 |
| Inlet pressure (design) | 7,129 kPag | DBM L1308 |
| Inlet pressure (low/high) | TBC | DBM L1308 |
| Sales flow at BAHX C-pass outlet (expander, winter) | 286 MMSCFD | DBM L1312 |
| Sales flow at BAHX C-pass outlet (expander, summer) | 281.2 MMSCFD | DBM L1312 |
| Sales flow (J-T, winter) | 295 < x < 300 MMSCFD TBC | DBM L1312 |
| Sales flow (J-T, summer) | 290 < x < 295 MMSCFD TBC | DBM L1312 |
| BAHX maximum design temperature | 150 °F (66 °C) | DBM L1324 |
| Methyl mercaptan in C3+ deethanizer bottoms (design summer, expander) | 1,373 ppmv | DBM L1314 |
| Ethyl mercaptan in C3+ deethanizer bottoms (design summer, expander) | 2,640 ppmv | DBM L1314 |
| Cryogenic water dewpoint limit | < -75 °C at highest operating pressure | DBM L1255 |
| BAHX over-temperature protection setpoint | 66 °C — exceedance results in facility shutdown | DBM L1257 |

## Construction / Module Configuration

| Item | Basis | Source |
|---|---|---|
| Cold separator | Receives cool two-phase gas from BAHX A-pass outlet; mesh/vane demister; overhead to J-T valve or turbo-expander; level-controlled liquids to BAHX B-pass | DBM L1320 |
| J-T valve | Pressure-controlled; sized for full hydraulic plant capacity; mechanical stop required so control-failure mass flow does not exceed cryogenic flare design flow | DBM L1321 |
| Turbo-expander / compressor | Common-shaft; expansion ratio 0.3961; IGV sized for 125 % normal design flow; single-stage open-impeller radial centrifugal compressor; typical compression ratio 1.3; anti-surge recycle | DBM L1322 |
| Turbo-expander utilities | Seal gas from downstream of sales coalescer; SCR electric seal-gas heater; 2 × 100 % duplex seal-gas filters; oil-lubricated journal bearings; 2 × 100 % lead/lag lube-oil pumps; aerial lube-oil cooler; dual bladder accumulators ≥1 min after ESD; duplex lube-oil filters; x/y bearing vibration monitoring | DBM L1323 |
| BAHX | Six-pass brazed aluminum; ALPEMA 3rd Edition + manufacturer practices with vendor exceptions; ASME U Stamp and BC CRN; minimum 10 % excess area on all passes; 0 mm corrosion allowance; mercury-tolerant features TBD; methanol injection at each pass inlet; tee strainers upstream of each pass | DBM L1324 |
| BAHX strainers | Clean ΔP < 2 psid; change at ≤ 15 psid | DBM L1325 |
| BAHX A-pass bypass | 15-20 % of max inlet flow (final TBC); controlled by cold-separator overhead temperature | DBM L1326 |
| Propane absorber | Refluxed absorber; 10 actual valve trays; jet/downcomer flood ≤ 70 %; mesh demister | DBM L1330 |
| Absorber bottoms pumps | 60 psid winter-case; 2 × 115 %; single-stage vertical inline API-610; dual mechanical seal API-682 Plan 14/52 | DBM L1331 |
| Deethanizer | 35 actual valve trays; refluxed and reboiled; flood ≤ 70 %; winter governs design | DBM L1332 |
| Deethanizer condenser | BAHX E-pass partial condenser with bypass for MDMT protection | DBM L1333 |
| Deethanizer reflux accumulator | Horizontal; mesh/vane demister; methanol boot with manual drain | DBM L1334 |
| Deethanizer reflux pumps | 50 psid winter-case; 2 × 115 %; API-610 / API-682 Plan 14/52 (or modified 13/52) | DBM L1335 |
| Deethanizer reboiler | TEMA BKU; hot-oil tube side; 350 °F heat medium; ≥ 25 °F approach (expander mode) | DBM L1336 |
| Methanol storage and pump | Atmospheric double-walled tank adjacent to expander building; pure methanol SG 1.00 TBC; triplex reciprocating pump | DBM L1329 |
| Expander aftercooler | Summer outlet 110 °F; ΔP < 4 psi summer; fan-speed / louver temperature control; winter < 95 °F operation TBD | DBM L1339 |

## References

- Authoritative basis: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-06 "Treating, Dehydration, and Cryogenic Recovery Basis" — UltraTEF Cryogenic Recovery Basis (L1098-L1396).
- Trace: `_Sources/DBM-Deepcut/Trace_Appendix.md` SEC-06 KTY-04-14 UltraTEF-Cryogenic-Unit rows.
- Decomposition row: Gate-07 snapshot `DELIVERABLE_REGISTER.csv` row for `DEL-075-06_epc-vendor-package-review-and-acceptance` (Workbook Packages row 52).
- 26020-Package_Requirements.docx heading 29 — not locally readable in this run; package-specific clause-level requirements remain `location TBD`.
