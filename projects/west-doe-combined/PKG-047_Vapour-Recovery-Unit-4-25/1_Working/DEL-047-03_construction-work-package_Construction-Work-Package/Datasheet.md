# Datasheet — Construction Work Package (VRU 4-25)

DeliverableID: `DEL-047-03_construction-work-package`
ParentPackageID: `PKG-047` (Vapour Recovery Unit 4-25)
Discipline: Mechanical (Construction execution by EPC Integrator)
Type: EPC Construction Work Package
ResponsibleParty: EPC Integrator

## Identification

| Field | Value | Source |
|---|---|---|
| Workbook row | Packages row 101 | DELIVERABLE_REGISTER.csv (DEL-047-03) |
| SOW coverage | SOW-0253, SOW-0254, SOW-0255, SOW-0256 | SCOPE_LEDGER.csv |
| Package vendor scope (engineering/design/equipment) | Vendor-owned | SOW-0253; OBJ-004 |
| Facility integration scope | EPC Integrator | SOW-0253; OBJ-004 |
| Construction interface scope ("by others") | Shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs | SOW-0256 (Scope notes and open items) |
| Facility | West Doe Deepcut expansion, LSD 04-25-80-15W6 | 4-25_Deepcut_DBM.md SEC-01 (lines 5-7, 16-17) |

## Attributes (As-Installed Configuration the Construction Package Must Realize)

| Attribute | Value | Source |
|---|---|---|
| Quantity / sparing | 2 x 100% VRU compressor packages, lead-lag, both in one building | SOW-0254; 4-25_Deepcut_DBM.md VRU Configuration table |
| Compressor model | Ro-Flo 17S / 217M two-stage rotary vane, positive displacement | SOW-0254/0255; DBM VRU table |
| Service | Sour service (H2S 0.3557 mol%, CO2 0.9434 mol%), NACE designation applies | SOW-0255; DBM VRU Inlet Composition table |
| Seal system | Dual mechanical pressurized barrier seal (Plan 53 type) using fuel gas; primary vent to LP flare | SOW-0255; DBM VRU table |
| Motors | 2 total (1 per train; drives both stages); 200 HP, 600 V, 3-phase, 60 Hz, VFD-ready | SOW-0256 |
| Cooler motors | VFD-ready, 600 V | SOW-0256 |
| Motor voltage (DBM body) | 4,000 V, 3 phase | DBM VRU table — **CONFLICT** with SOW-0256 (600 V); see Guidance Conflict Table |
| Motor power (DBM body) | TBD; 200 hp TBC and 300 hp conflict requires ruling | DBM VRU table — **CONFLICT** noted in source; SOW-0256 states 200 HP |
| Housing | Each VRU installed in an individual building with associated utilities (DBM) / both in one building (SOW-0254) | DBM VRU section / SOW-0254 — **CONFLICT** see Guidance |
| Capacity control | Speed control plus automated recycle valve | DBM VRU table |
| Design capacity | 1.5 MMSCFD / 42 e3m3/d (TBC) | DBM VRU table; SOW-0256 |
| Design suction pressure | 0.9 kPag / 2 oz/in2 | DBM VRU table; SOW-0256 |
| Design discharge pressure | 483 kPag / 70 psig | DBM VRU table; SOW-0256 |
| Design temperature | 102 C | SOW-0256 |
| 1st-stage discharge MAWP (minimum) | 552 kPag | DBM VRU MAWP table |
| 2nd-stage discharge MAWP (minimum) | 1034 kPag | DBM VRU MAWP table |
| 1st-stage intercooler outlet (operating) | 48.9 C | SOW-0256; DBM cooler table |
| 2nd-stage aftercooler outlet (operating) | 60.0 C | SOW-0256; DBM cooler table |
| 1st-stage dewpoint | 45.6 C (SOW-0256); 52.7 C (DBM) | **CONFLICT** — see Guidance |
| 2nd-stage dewpoint | 53.2 C (SOW-0256); 55.8 C (DBM) | **CONFLICT** — see Guidance |
| Driver speed | 310 to 760 rpm (TBC) | DBM VRU table |
| Driver turndown | 3:1 on inverter duty | DBM VRU table |

## Site / Tie-In Conditions

| Item | Value | Source |
|---|---|---|
| Discharge routing | VRU discharge to 04-25 stabilizer overheads compressor (SOC) first-stage suction (both 04-25 and 03-25 VRUs) | DBM Vapour Recovery Unit section |
| Primary seal vent | LP flare | DBM VRU table |
| Foundations | Piles (per SOW "installation on piles") | SOW-0256 |
| Electrical interface | EPC connections to VFD-ready motors, 600 V (SOW) | SOW-0256 |
| Building utilities | Each VRU building with associated utilities (DBM) | DBM VRU Configuration paragraph |

## Construction Scope (As Anticipated Per `_CONTEXT.md`)

- Construction work package narrative.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

## References

- `_CONTEXT.md` (identity, anticipated artifacts).
- `_REFERENCES.md` (decomposition basis; shared source root).
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-047-03.
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` rows SOW-0253..SOW-0256.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Vapour Recovery Unit" section (lines 1681-1780) and SEC-04 stabilizer overheads context (lines 569-612).
- `_Sources/26020-Package_Requirements.docx` package heading 2 — **binary source; only the SOW-0254..SOW-0256 extracts in SCOPE_LEDGER.csv are locally accessible as text**.

## TBD / Open Items

- Field installation contractor identity: TBD (decomposition assigns to EPC Integrator; specific contractor not in accessible sources).
- Pile design (diameter, length, count): TBD; civil DEL/package not referenced in accessible sources.
- Tie-in P&ID isometrics: TBD (mechanical/piping deliverable; not in accessible sources for this deliverable).
- Construction schedule, sequencing, and milestone dates: TBD.
- Crane/lift study, rigging plan, heavy-lift requirements: TBD.
- Hot/cold work permit regime at site: TBD.
- Pre-commissioning, mechanical completion, and turnover boundary list: TBD; coordination with DEL-047-06 (EPC vendor package review and acceptance).
