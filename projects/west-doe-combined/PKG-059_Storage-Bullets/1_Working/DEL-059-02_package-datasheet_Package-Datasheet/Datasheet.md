# Package Datasheet — Storage Bullets (PKG-059)

> Deliverable: `DEL-059-02_package-datasheet` — EPC Integrator technical handoff datasheet for the Storage Bullets package (two unstable condensate storage bullets and sixteen LPG product storage bullets). Package identity, scope, and major equipment values are taken from the GATE-07 PROJECT_DECOMP snapshot (`SCOPE_LEDGER.csv` rows SOW-0181..SOW-0184, extracted from `26020-Package_Requirements.docx` package heading 14) and from the locally accessible Deepcut DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).

## Identification

| Field | Value | Source |
|---|---|---|
| Package ID | `PKG-059` | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` |
| Package Name | Storage Bullets | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Workbook Row | 83 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv |
| Source RFQ Tag | `26020-01-PT-RFQ-17-007` (Pressure Vessels — Storage Bullets) | PACKAGE_REGISTER.csv (Source Basis); GATE-07 register row |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Package Vendor scope | Engineering, design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv responsibility split |
| EPC Integrator scope | Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | PACKAGE_REGISTER.csv responsibility split |
| Facility | 04-25 Deep Cut Gas Plant (NGL/LPG product storage) | DBM-Deepcut lines 73, 448, 1627-1629 (ASSUMPTION: facility located at 04-25 per Deepcut NGL/product storage basis; see Open Items / Conflicts) |
| Service | Storage of C5 unstable condensate (two bullets) and LPG product (sixteen bullets) | SCOPE_LEDGER SOW-0182, SOW-0184 |

ASSUMPTION (facility-of-record): The decomposition row text speaks of LPG product storage bullets and C5 condensate storage bullets. The Deepcut DBM (line 1627-1629; line 448; line 492) carries 16 x 120,000 USG NGL storage bullets at 04-25, with the C3/C4 LPG depropanizer concept retired in the current DBM scope. The numeric inventory (16 x 120,000 USG bullets) matches the SCOPE_LEDGER row. The C3/C4 vs NGL composition difference is recorded as CONF-01 in `Guidance.md`. Facility-of-record is assumed to be 04-25 because product storage in the DBM resides at 04-25.

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Unstable condensate bullets — count | 2 | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| LPG product bullets — count | 16 | SCOPE_LEDGER SOW-0183 (26020 package heading 14); cross-check DBM-Deepcut line 492 (16 x 120,000 USG bullets) |
| Bullet — inside diameter (ID) | 3658 mm | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| Bullet — seam-to-seam length (S/S) | 42494 mm | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| Bullet — nominal volume | 454 m3 / 120,000 US gal | SCOPE_LEDGER SOW-0183; cross-check DBM-Deepcut line 492 ("120,000 USG bullets") |
| Bullet — maximum fill volume | 84% of nominal | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| Bullet — design pressure | 1724 kPag (full vacuum also required) | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| Bullet — design temperature | 66 C | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| Bullet — external design | Full vacuum | SCOPE_LEDGER SOW-0183 |
| Mounting | Outdoor saddle mounting | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| Access | Stairs and platforms | SCOPE_LEDGER SOW-0183 (26020 package heading 14) |
| Unstable condensate bullet service | Stores condensate from the C5 product line before the condensate transfer pumps | SCOPE_LEDGER SOW-0184 |
| LPG bullet service | Stores C3, C4, or C3/C4 LPG mix from the depropanizer before transfer to the off-site liquids hub via booster pumps | SCOPE_LEDGER SOW-0184 |
| LPG vapour equalization | Required; piping must avoid pockets | SCOPE_LEDGER SOW-0184 |
| Butane storage blanket | Blanket gas required for butane storage | SCOPE_LEDGER SOW-0184 |
| Excluded vendor scope (by others) | Foundations; DCS integration; electrical supply to MCC | SCOPE_LEDGER SOW-0184 |
| NGL storage duration (project basis) | 2.5 days at 15,400 bbl/d production rate | DBM-Deepcut lines 448, 492 (ASSUMPTION: NGL/LPG correspondence per CONF-01) |
| Material of construction (shell) | TBD | Not stated in available source slice (package heading 14 extract); RFQ source `26020-01-PT-RFQ-17-007` likely contains MOC but native .docx not parsed |
| MAWP / hydrotest | TBD | Not stated in available source slice |
| Internals (boot, vortex breaker, nozzles) | TBD | Not stated in available source slice |
| Insulation / heat tracing (EHT) | TBD (EHT interface is declared; specific bullet insulation not in source slice) | INTERFACE_REGISTER IFC-150A5B72C1 (EHT interface YES) |
| Relief / vent disposition | TBD; relief routed to Relief / Flare / Vent interface | INTERFACE_REGISTER IFC-B6B084C01D (Relief / Flare / Vent YES) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Design pressure (internal) | 1724 kPag | SCOPE_LEDGER SOW-0183 |
| Design pressure (external) | Full vacuum | SCOPE_LEDGER SOW-0183 |
| Design temperature | 66 C | SCOPE_LEDGER SOW-0183 |
| Maximum fill | 84% of nominal (454 m3 / 120,000 USG) | SCOPE_LEDGER SOW-0183 |
| Stored fluid — unstable condensate bullets | C5 product line condensate, upstream of condensate transfer pumps | SCOPE_LEDGER SOW-0184 |
| Stored fluid — LPG bullets | C3, C4, or C3/C4 LPG mix, downstream of the depropanizer | SCOPE_LEDGER SOW-0184 |
| Downstream disposition — LPG | Transfer to off-site liquids hub via booster pumps | SCOPE_LEDGER SOW-0184 |
| Spacing — pressurized bullets, maximum per cluster | <=6 | DBM-Deepcut line 249 (API 2510) |
| Spacing — between pressurized bullet clusters | 15.24 m (50 ft) | DBM-Deepcut line 250 (API 2510) |
| Spacing — between butane and propane bullets | 2.804 m (9.2 ft) | DBM-Deepcut line 251 (API 2510) |
| Spacing — bullets to pump skid taking suction from bullets | 3.05 m (10 ft) | DBM-Deepcut line 252 (API 2510) |
| Spacing — bullets to unrelated rotating equipment | 15.24 m (50 ft) | DBM-Deepcut line 253 (API 2510) |
| Spacing — bullets to control building / process building / control room | 15.24 m (50 ft) | DBM-Deepcut line 254 (API 2510) |
| Spacing — bullets to unrelated occupied buildings (e.g., warehouse) | 30.48 m (100 ft) | DBM-Deepcut line 255 (API 2510) |
| Spacing — bullets to process vessels | 15.24 m (50 ft) | DBM-Deepcut line 256 (API 2510) |
| Spacing — bullets to truck loading station | 15.24 m (50 ft) | DBM-Deepcut line 257 (API 2510) |
| Spacing — bullet loading connection to ignition / process / storage / occupied | 15.24 m (50 ft) | DBM-Deepcut line 258 (API 2510) |
| Spacing — bullets to property line | 38.1 m (125 ft) | DBM-Deepcut line 259 (API 2510 Table 1) |
| Spacing — bullets to nearest atmospheric tank | 30.48 m (100 ft) | DBM-Deepcut line 265 (API 2510) |
| Spacing — bullets to nearest spill containment area | 3.05 m (10 ft) | DBM-Deepcut line 266 (API 2510) |
| Spacing — LPG process equipment to ignition / property line / occupied | 15.24 m (50 ft) | DBM-Deepcut line 267 (API 2510) |
| Spacing — flare to pressurized bullets | 30.48 m (100 ft) | DBM-Deepcut line 284 (API 2510) |
| Spacing — fired heater to pressurized bullets | 15.24 m (50 ft) | DBM-Deepcut line 299 (API 2510) |
| Vapour-equalization piping | Must avoid pockets | SCOPE_LEDGER SOW-0184 |
| Butane blanket gas | Required | SCOPE_LEDGER SOW-0184 |

## Construction

| Item | Basis | Source |
|---|---|---|
| Mounting | Outdoor, saddle-mounted pressure vessels | SCOPE_LEDGER SOW-0183 |
| Access | Stairs and platforms | SCOPE_LEDGER SOW-0183 |
| Foundations | By others (EPC Integrator / civil discipline) | SCOPE_LEDGER SOW-0184 |
| DCS integration | By others (EPC Integrator / I&C) | SCOPE_LEDGER SOW-0184 |
| Electrical supply to MCC | By others (EPC Integrator / electrical) | SCOPE_LEDGER SOW-0184 |
| Vessel code | TBD (ASSUMPTION: ASME BPVC Sec. VIII Div. 1 typical for LPG pressure vessels) | Not in available source slice; assumption per industry practice |
| Pressure-vessel jurisdiction | TBD (ASSUMPTION: BC PV registration applicable in British Columbia) | Not in available source slice |
| MOC (vessel shell) | TBD | Not in available source slice (native RFQ .docx not parsed) |
| Nozzle schedule | TBD | Not in available source slice |
| Internals (boot, vortex breaker, demister, instrument nozzles) | TBD | Not in available source slice |
| Insulation / heat tracing | TBD (EHT interface declared; specifics deferred to detailed design) | INTERFACE_REGISTER IFC-150A5B72C1 |
| Surface preparation / paint | TBD | Not in available source slice |
| Cluster layout | Per API 2510 spacing constraints (above); cluster size <=6 | DBM-Deepcut lines 249-259 |
| Spill containment / drainage | Per Drain / Containment and Grading / Site Drainage / Spill Containment interfaces | INTERFACE_REGISTER IFC-8B00B00EF5, IFC-256D0B008C |

## Interface Requirements Matrix

Per `_CONTEXT.md` Notes, interface facts are intentionally carried in this datasheet rather than as a standalone deliverable. Interface types come from `INTERFACE_REGISTER.csv` (GATE-07).

| Interface ID | Interface Type | Applicability | EPC / Vendor split (PROPOSAL) | Source |
|---|---|---|---|---|
| IFC-E24F2509B2 | Process Piping | YES | EPC owns tie-ins outside vendor skid edge; vendor owns package piping inside skid envelope | INTERFACE_REGISTER (Workbook Packages row 83); PACKAGE_REGISTER scope split |
| IFC-B6B084C01D | Relief / Flare / Vent | YES | EPC owns relief/vent header routing; vendor owns PSV sizing on each bullet and connection to the relief/vent stub | INTERFACE_REGISTER; SCOPE_LEDGER SOW-0184 (vapour equalization & blanket) |
| IFC-8B00B00EF5 | Drain / Containment | YES | EPC owns drainage system and spill containment; vendor provides bullet drain nozzles | INTERFACE_REGISTER; DBM-Deepcut line 266 (API 2510 containment spacing) |
| IFC-150A5B72C1 | EHT (Electric Heat Tracing) | YES | EPC owns EHT supply and controls; vendor designs vessel/nozzles to accept EHT and provides insulation supports | INTERFACE_REGISTER |
| IFC-C98C663233 | Grounding / Bonding | YES | EPC owns site grounding grid; vendor provides bonding lugs on bullets and platforms | INTERFACE_REGISTER |
| IFC-D1A0DB0DE5 | Area / Exterior Lighting | YES | EPC scope (lighting for outdoor cluster, platforms, stairs) | INTERFACE_REGISTER |
| IFC-22BB35F0F9 | I&C / Control Cabling | YES | EPC owns DCS integration and control cabling; vendor provides instrument nozzles, JBs, and local instrument schedule | INTERFACE_REGISTER; SCOPE_LEDGER SOW-0184 (DCS integration by others) |
| IFC-164A2BFF9D | Maintenance Access | YES | EPC plot plan owns spacing for maintenance access; vendor provides stairs/platforms on bullets | INTERFACE_REGISTER; SCOPE_LEDGER SOW-0183 |
| IFC-256D0B008C | Grading / Site Drainage / Spill Containment | YES | EPC scope; spacing per API 2510 (3.05 m bullet-to-containment) | INTERFACE_REGISTER; DBM-Deepcut line 266 |
| IFC-FF66D2BF62 | Structural / Foundations / Supports | YES | EPC scope; vendor delivers saddle reactions, anchor loads, and pier requirements | INTERFACE_REGISTER; SCOPE_LEDGER SOW-0184 (foundations by others) |

ASSUMPTION: The EPC/Vendor split rows are PROPOSALs framed by the package responsibility split in `PACKAGE_REGISTER.csv` and standard EPC convention. They are not extracted verbatim from `26020-Packages_Interfaces_4_export.xlsx` (native .xlsx not parsed in this pass).

## References

- `_CONTEXT.md` — deliverable identity, scope items, supported objectives, interface note
- `_REFERENCES.md` — authoritative decomposition basis and Shared Source Root
- GATE-07 PROJECT_DECOMP snapshot — `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (DEL-059-02 row)
  - `PACKAGE_REGISTER.csv` (PKG-059 row, including responsibility split and interface list)
  - `SCOPE_LEDGER.csv` (SOW-0181..SOW-0184, source-extracted package heading 14 text)
  - `INTERFACE_REGISTER.csv` (10 interface rows for PKG-059)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- DBM-Deepcut — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - Sec. Pressurized Bullet Spacing (lines 245-259, API 2510)
  - Sec. Atmospheric Tank and General Plant Spacing (lines 261-268, API 2510 / NFPA 30)
  - Sec. Flare and Incinerator Spacing (line 284, API 2510)
  - Sec. Fired Heater Spacing (line 299, API 2510)
  - Sec. Storage and Disposition tables (lines 448, 492)
  - Sec. NGL Storage Bullets (lines 1627-1629)
- DBM-Comp_and_Liquids — `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (context only; condensate/LPG disposition narrative)
- `26020-Package_Requirements.docx` package heading 14 (location TBD; native .docx not parsed — values used here are the SCOPE_LEDGER source extractions)
- `26020-Packages_Interfaces_4_export.xlsx` (location TBD; native .xlsx not parsed)
- RFQ tag `26020-01-PT-RFQ-17-007` Pressure Vessels — Storage Bullets (not locally accessible; bullet detail design parameters likely contained here)

## Open Items / TBD

- Vessel MOC, MAWP, hydrotest, internals, nozzle schedule, surface prep/paint: TBD — not in available source slice; need RFQ document or vendor data.
- LPG composition mix per bullet (C3, C4, C3/C4 mix), per-cluster allocation, vapour-equalization piping topology: TBD — package heading 14 carries the general statement but not the per-bullet schedule.
- Bullet relief device set and discharge routing: TBD — to be sized by vendor and tied to relief/flare/vent interface.
- Detailed interface allocation (e.g., EHT power, instrument JB count) per `26020-Packages_Interfaces_4_export.xlsx`: TBD — native .xlsx not parsed.
- Facility-of-record reconciliation between "two unstable condensate storage bullets and sixteen LPG product storage bullets" (SCOPE_LEDGER) and "16 x 120,000 USG NGL storage bullets" (DBM-Deepcut, with C3/C4 LPG depropanizer scope retired): see CONF-01 in `Guidance.md`.
- Foundation, DCS, MCC supply scopes are explicitly "by others" per SCOPE_LEDGER SOW-0184; coordination interface lives in PKG-059 interface matrix but specific design parameters are deferred to the receiving EPC discipline packages.
