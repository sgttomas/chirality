# Specification — DEL-075-01 Scope of Work (PKG-075 Cryogenic Unit "Deepcut")

## Scope

### In scope

The EPC Integrator Scope of Work for PKG-075 covers the package boundary, tagged-equipment identity list, package function and integration narrative, and responsibility assignments for the UltraTEF cryogenic recovery unit of the West Doe Deepcut expansion (`_CONTEXT.md`; DBM-Deepcut SEC-06 "UltraTEF Cryogenic Recovery Basis", lines 1293-1396).

Functionally, the package recovers propane and heavier hydrocarbons from molecular-sieve-dried inlet gas and produces sales gas (DBM-Deepcut line 1297). Equipment within the package boundary includes the cold separator, J-T valve path, turbo-expander/compressor and its seal/lube utilities, six-pass BAHX with strainers, A-pass bypass and F-pass bleed provisions, methanol injection system (storage, pump, distribution to listed injection points), propane absorber and bottoms pumps, deethanizer, deethanizer condenser (BAHX E-pass), reflux accumulator, reflux pumps, reboiler, and expander aftercooler (DBM-Deepcut lines 1320-1340).

### Out of scope (interfaces, not package equipment)

- Upstream amine treating, TEG dehydration, molecular-sieve dehydration, mercury removal (MRU), and dust filtration (DBM-Deepcut SEC-06 functional configuration paragraph, lines 1098-1106).
- Downstream sales-gas compression beyond the expander-compressor outlet (DBM-Deepcut "Interfaces", line 1376).
- Downstream NGL treating and dehydration (DBM-Deepcut line 1377; future-NGL exchanger/cooler are interface provisions only).
- Acid-gas compression / disposal (DBM-Deepcut line 1371).
- VRU, fuel-gas, heat-medium, produced-water/drain systems (DBM-Deepcut lines 1372-1375), except for the cryogenic drain header connection and methanol drain boot routing (DBM-Deepcut line 1334).
- External composition/specification appendices and any sulphur distribution basis dependent on them (DBM-Deepcut line 1378).

## Requirements

### R-01 Package process function

The package SHALL recover propane and heavier hydrocarbons from molecular-sieve-dried gas while producing sales gas, sized to the design point in R-02 (DBM-Deepcut line 1297).

### R-02 Design point

Design SHALL be set to summer ambient, expander mode for BAHX and turbo-expander sizing (DBM-Deepcut lines 1299, 1305). Winter performance SHALL be verified for tower, pump, and deethanizer reboiler hydraulics (DBM-Deepcut line 1299).

### R-03 Design inlet conditions

The package boundary SHALL be designed for: inlet flow 307.6 MMSCFD winter / 303 MMSCFD summer; inlet temperature 14.2 degC winter / 40.5 degC summer; inlet pressure 7129 kPag, all measured immediately upstream of the cryogenic unit inlet ESDV (DBM-Deepcut lines 1306-1308). Low/high inlet pressure: TBC (DBM-Deepcut line 1308).

### R-04 Recovery performance

Expander-mode C3 recovery SHALL be 99+% (DBM-Deepcut line 1309). Expander-mode C4+ recovery for iC4, nC4, iC5, nC5, and C6+ SHALL be 100% (DBM-Deepcut line 1310). J-T-mode minimum C3 recovery SHALL be >27% to support sales-gas total sulphur compliance (DBM-Deepcut lines 1309, 1346). J-T-mode C4+ recovery values: TBC (DBM-Deepcut line 1310).

### R-05 Sales delivery

Sales gas at BAHX C-pass outlet SHALL meet: expander mode winter 286 MMSCFD / summer 281.2 MMSCFD; sales pressure expander summer 3068 kPag design, expander winter 3289 kPag expected (DBM-Deepcut lines 1312-1313). J-T-mode sales flow and pressure: TBC.

### R-06 Operating modes

The package SHALL operate in two normal modes: expander mode (normal design) and J-T mode (start-up / off-design) (DBM-Deepcut lines 1297, 1345-1346). A documented dry-out / start-up plan SHALL be performed at low pressure to avoid freezing and overcooling (DBM-Deepcut line 1347).

### R-07 BAHX construction

The BAHX SHALL be a six-pass brazed aluminum exchanger designed to ALPEMA 3rd Edition plus manufacturer standard practice (with vendor exceptions), ASME U Stamp, and BC CRN; minimum 10% excess area on all passes; 0 mm corrosion allowance; maximum design temperature 150 degF (66 degC); mercury-tolerant features (TBD); per-pass methanol injection on each pass inlet header; per-pass tee strainers upstream of each pass with start-up fine mesh and normal baskets (DBM-Deepcut line 1324).

### R-08 BAHX strainer differential-pressure limits

Clean normal-operation pressure drop SHALL be <2 psid; strainers SHALL be cleaned/changed at a maximum 15 psid, with operations permitted to change earlier for capacity or efficiency (DBM-Deepcut line 1325).

### R-09 BAHX A-pass bypass and F-pass bleed

An automated A-pass bypass SHALL be provided with capacity 15-20% of maximum inlet flow (final capacity TBC), controlled by cold-separator overhead temperature (DBM-Deepcut line 1326). An automated F-pass bleed valve and flow meter between F-pass inlet and C-pass outlet SHALL be considered for light-end recycle management (DBM-Deepcut line 1327).

### R-10 J-T valve sizing and protection

The J-T valve SHALL maintain cold-separator backpressure by pressure control, be sized for full hydraulic plant capacity so sales-compressor suction pressure can run at normal operating conditions, and include a mechanical stop or physical stroke limit so that control-failure mass flow to the propane absorber does not exceed cryogenic flare design flow (DBM-Deepcut line 1321). Trim capacity for condensing liquids: TBC.

### R-11 Turbo-expander / compressor

The unit SHALL be a common-shaft expander and compressor with shared lube oil and seal-gas systems; expander expected expansion ratio 0.3961; inlet guide vanes sized for 125% of normal design flow; compressor single-stage open-impeller radial centrifugal with typical compression ratio 1.3; anti-surge recycle from discharge to inlet via flow control valve (DBM-Deepcut line 1322).

### R-12 Expander seal-gas and lube-oil utilities

Seal gas SHALL be taken from downstream of the sales coalescer, be available before and during lube-oil circulation, and pass through an SCR-controlled electric heater and 2 x 100% duplex seal-gas filters. Lubrication SHALL use oil-lubricated journal bearings with 2 x 100% lead/lag gear lube-oil pumps, aerial lube-oil cooler in the expander building, dual bladder lube-oil accumulators sized for at least one minute of lube-oil flow after ESD, duplex lube-oil filters, and x/y bearing vibration monitoring (DBM-Deepcut line 1323).

### R-13 Methanol injection

Methanol injection SHALL be system-designed to inject into one point at a time; injection points SHALL include BAHX pass inlets upstream of strainers, J-T valve inlet, inlet separators upstream of PCV, inlet separators upstream of HCL and water dump valves, and acid-gas compressor package (DBM-Deepcut line 1328). All design injection capacities: TBC. Methanol storage SHALL be an atmospheric double-walled tank adjacent to the expander building; pure methanol tank design specific gravity 1.00 (TBC); injection pump shall be triplex reciprocating (DBM-Deepcut line 1329).

### R-14 Propane absorber

The propane absorber SHALL be a refluxed absorber column with 10 actual valve trays, jet and downcomer flood <=70%, and a mesh demister. The J-T or turbo-expander two-phase stream enters the lower feed; overhead vapour is sales gas to BAHX C-pass; recovered liquids are pumped and level-controlled to BAHX D-pass (DBM-Deepcut line 1330).

### R-15 Absorber bottoms pumps

Absorber bottoms pumps SHALL be 2 x 115%, 60 psid differential, winter-case design, single-stage vertical inline API-610 light-hydrocarbon pumps with API-682 Plan 14/52 dual mechanical seals and space / anti-condensation heaters (DBM-Deepcut line 1331).

### R-16 Deethanizer

The deethanizer SHALL be a refluxed and reboiled fractional distillation column for C3+ recovery with 35 actual valve trays, jet/downcomer flood <=70%, and no demister; winter operation is expected to govern design; co-current trays may be evaluated (DBM-Deepcut line 1332). Deethanizer bottoms product C2/C3 expected/operating target <=0.654 mol%; design <=1.5 mol% (DBM-Deepcut line 1311 — NOTE: source uses "<=654 mol%" which is reproduced verbatim above; intended numeric value `TBD - source-text appears typographically inconsistent (likely 0.654 mol%)`; see Guidance.md Conflict Table CONFL-01).

### R-17 Deethanizer condenser, reflux, reboiler

The deethanizer condenser SHALL be a BAHX E-pass partial condenser with low-pressure-drop temperature-control valves for E-pass inlet restriction and bypass; reflux system shall use low-temperature carbon steel; bypass prevents exceeding MDMT (DBM-Deepcut line 1333). The reflux accumulator SHALL be horizontal-flow with mesh/vane demister and a methanol boot with manual drain to the cryogenic drain header (DBM-Deepcut line 1334). Reflux pumps SHALL be 2 x 115%, 50 psid differential, winter-case design, API-610 / API-682 Plan 14/52 or modified 13/52 (DBM-Deepcut line 1335). The reboiler SHALL be a TEMA BKU type with hot oil on tube side, 350 degF heat medium via mixing valves, minimum approach 25 degF (13.9 degC) in expander mode (DBM-Deepcut line 1336).

### R-18 Expander aftercooler

The aftercooler SHALL cool hot sales gas from expander-compressor discharge to 110 degF in summer, with pressure drop <4 psi in summer; temperature control by fan speed and manual bundle louvers; winter operation below 95 degF (35 degC) to be studied (DBM-Deepcut line 1339).

### R-19 Mercaptan handling concern

The design SHALL account for mercaptan concentration in cryogenic liquids; design summer expander-mode C3+ deethanizer bottoms may contain methyl mercaptan 1373 ppmv and ethyl mercaptan 2640 ppmv (DBM-Deepcut line 1314).

### R-20 Future NGL interface provisions

Future deethanizer bottoms exchanger (NEN shell-and-tube, 10 degF (5.56 degC) min approach, initial target outlet 48.8 degC) and future deethanizer bottoms cooler (design outlet 110 degF (38 degC); downstream caustic solution minimum 80 degF (26.7 degC)) SHALL be provided as future interface provisions for downstream NGL mercaptan treating; final basis TBD (DBM-Deepcut lines 1337-1338).

### R-21 Package interfaces

The EPC Scope of Work SHALL define and document the package's external interfaces consistent with DBM-Deepcut "Interfaces" (lines 1365-1378): upstream molecular-sieve dehydration / MRU / dust filtration (gas to BAHX); downstream sales-gas compression; downstream NGL treating and future-NGL interface provisions; cryogenic drain header connections; methanol supply; heat medium (350 degF) supply; and required utilities.

### R-22 Tagged equipment list

The EPC Scope of Work SHALL include a tagged equipment list of all package equipment with tag numbers, equipment names, and design-basis references (per `_CONTEXT.md` Anticipated Artifacts). Individual tag numbers are not present in the locally accessible source slice and are `TBD` until P&IDs and the package datasheet (DEL-075-02) are issued.

### R-23 Responsibility assignment record

The EPC Scope of Work SHALL contain a responsibility assignment record covering EPC Integrator, Package Vendor, and other-discipline responsibilities for engineering, design, fabrication/supply, installation, integration, inspection, and turnover. Detailed RACI/RAM content: TBD (no responsibility matrix is present in the locally accessible source slice; `_CONTEXT.md` declares the deliverable but does not enumerate the matrix rows).

## Standards

| Standard | Applicability | Source / Status |
|---|---|---|
| ALPEMA 3rd Edition + manufacturer standard practice (with vendor exceptions) | BAHX design | DBM-Deepcut line 1324 |
| ASME U Stamp | BAHX certification | DBM-Deepcut line 1324 |
| BC CRN | BAHX BC jurisdiction | DBM-Deepcut line 1324 |
| ASME Section VIII (DIV 1) | Pressure vessels (absorber, deethanizer, separator, accumulators) | ASSUMPTION (industry default); location TBD in source |
| API-610 | Vertical inline single-stage light-hydrocarbon pumps (absorber bottoms; reflux) | DBM-Deepcut lines 1331, 1335 |
| API-682 Plan 14/52 (or modified 13/52 for reflux) | Dual mechanical seals on absorber bottoms and reflux pumps | DBM-Deepcut lines 1331, 1335 |
| TEMA BKU | Deethanizer reboiler | DBM-Deepcut line 1336 |
| TEMA NEN | Future deethanizer bottoms exchanger | DBM-Deepcut line 1337 |
| Package Requirements (26020-Package_Requirements.docx, heading 29) | Mandatory contractual basis for this scope of work | Referenced in `_REFERENCES.md`; locally machine-readable text `TBD` — content depending solely on this source is marked `TBD` |

## Verification

| Requirement | Verification approach |
|---|---|
| R-01, R-02 | Process simulation (winter and summer cases); design review against DBM SEC-06 |
| R-03 | Heat & material balance review; inlet boundary instrument selection / loop check |
| R-04 | Vendor simulation / performance test data; commissioning C3 recovery measurement |
| R-05 | Sales-gas custody-transfer metering; commissioning pressure/flow verification at BAHX C-pass outlet |
| R-06 | Operating procedures (Procedure.md) including expander-to-J-T transition test |
| R-07, R-08 | BAHX vendor data report (U Stamp, CRN), excess-area calculation, strainer dP datasheet; commissioning baseline dP measurement |
| R-09 | A-pass bypass and F-pass bleed control narrative; FAT/SAT for control loops |
| R-10 | J-T valve sizing review; stroke-limit setting and verification; flare load study |
| R-11, R-12 | API mechanical run test, lube-oil and seal-gas system FAT, vibration baseline; ESD rundown demonstration |
| R-13 | Methanol injection system FAT; single-point interlock test; SG check of methanol on receipt |
| R-14, R-15, R-16, R-17 | Tower hydraulic check; pump performance test (API-610 PTC); reboiler thermal performance test |
| R-18 | Aftercooler performance test in summer; engineering study for winter <95 degF operation |
| R-19 | Mercaptan concentration measurement in deethanizer bottoms during commissioning |
| R-20 | Future interface drawings and tie-in stub verification |
| R-21 | Interface matrix review with adjacent packages (PKG inventory of dehydration, MRU, sales-gas compression, NGL treating) |
| R-22 | Tag list cross-check against P&IDs and package datasheet (DEL-075-02) at issue |
| R-23 | RACI/RAM review and acceptance |

## Documentation

The EPC Scope of Work deliverable consists of the artifacts named in `_CONTEXT.md`:

- Package scope of work (this document and the four-document set in this folder)
- Tagged equipment and package identity list (Datasheet.md)
- Package function and integration narrative (Guidance.md and Specification.md scope)
- Responsibility assignment record (TBD — to be authored alongside this set)

Companion downstream deliverables in PKG-075: DEL-075-02 Package Datasheet; DEL-075-03 Construction Work Package; DEL-075-04 Vendor Engineered Equipment Package; DEL-075-05 Vendor Document Turnover Package; DEL-075-06 EPC Vendor Package Review and Acceptance.
