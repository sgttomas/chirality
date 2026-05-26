# Package Datasheet — Tanks, Water (API 650) 4-25 (PKG-064)

> Deliverable: `DEL-064-02_package-datasheet` — EPC Integrator technical handoff datasheet for the Process Water Storage Tank package (API 650, atmospheric) serving the 04-25 (Deepcut) facility. Package equipment list and tags are taken from the accepted decomposition snapshot (GATE-07) and the Deepcut DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`).

## Identification

| Field | Value | Source |
|---|---|---|
| Package ID | `PKG-064` | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` |
| Package Name | Tanks, Water (API 650) 4-25 | `_CONTEXT.md` |
| Facility | 04-25 (Deepcut) | DBM-Deepcut tag table (line 2628) |
| Workbook Row | 96 | `_CONTEXT.md` Source Reference |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Tagged Equipment | TK-5317-1, TK-5318-1 (PROCESS WATER STORAGE TANK x2, 4-25) | DBM-Deepcut line 2628 |
| Quantity | 2 tanks | DBM-Deepcut line 2628 |
| Tank Specification | API 650, atmospheric | `_CONTEXT.md` package name; DBM-Deepcut equipment-count table (line 2560) |
| Service | Process water storage for the 04-25 Deepcut facility, including amine make-up / process-water user supply and emergency make-up water to the NGL mercaptan treating system | DBM-Deepcut lines 1132, 1183, 1556 |

ASSUMPTION: The decomposition row "Tanks, Water (API 650) 4-25" (PKG-064, workbook row 96) corresponds to the Deepcut tag table entry "Tanks, Water (API 650) 2" carrying TK-5317-1 and TK-5318-1 in the 4-25 (Deepcut) column. Confirmed by package name match ("Tanks, Water (API 650)") and 4-25 location column.

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Tank tags | TK-5317-1, TK-5318-1 | DBM-Deepcut line 2628 |
| Service description | PROCESS WATER STORAGE TANK (x2, 4-25) | DBM-Deepcut line 2560 |
| Tank construction code | API 650 (atmospheric) | `_CONTEXT.md`; DBM-Deepcut line 2560 |
| Associated transfer pumps | P-5317-1, P-5318-1 (PROCESS WATER TRANSFER PUMPS x2; Pumps radial centrifugal 2; located in Tank Farm Pump Building 2) | DBM-Deepcut lines 2555, 2621 |
| Pump building location | Tank Farm Pump Building 2 | DBM-Deepcut lines 2555, 2621 |
| Insulation | Insulated to prevent winter freezing | DBM-Deepcut line 2509 ("water tanks shall be insulated to prevent winter freezing") |
| Heat tracing | TBD (insulation explicitly stated; heat tracing not stated for process water tanks in source slice) | DBM-Deepcut line 2509 |
| Internal coating | TBD — not stated in source for process water tanks |
| Design specific gravity | TBD (process-water tank design SG not stated; for reference, produced water density = 1008 kg/m3 at 26.7 °C is given) | DBM-Deepcut line 508 (reference only) |
| Tank diameter / height | TBD — not in available source |
| Design pressure (atmospheric basis) | Atmospheric (API 650) | `_CONTEXT.md` package name; DBM-Deepcut line 518 (similar produced-water tank basis: 16 oz test pressure for modified API-650 atmospheric tank — reference only; ASSUMPTION may apply) |
| Design temperature | TBD — not in available source |
| MOC (shell / floor / roof) | TBD — not stated in source for process water tanks |
| Foundations | Equipment-specific foundation and anchorage per final geotechnical report, equipment loads, snow/wind/seismic, frost, vibration, settlement, and maintenance access (ASSUMPTION: same project-wide basis applies) |
| Nozzle schedule | TBD — not in available source |
| PVRV / EPRV | TBD — process-water tank venting not explicitly addressed (cf. produced-water tank PVRV/EPRV practice in DBM-Deepcut line 524 — reference only) |
| Truck-in / truck-out | TBD — not stated in source for process water tanks |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Process water user (downstream) — amine regeneration | Process-water storage and transfer feeds the amine regeneration module (Module 530) | DBM-Deepcut line 1132 |
| Process water user — NGL mercaptan treating system make-up | Make-up water, if required during upset operation, is supplied from the process water storage tank; final routing TBC by detailed engineering | DBM-Deepcut line 1556 |
| Process-water user rates | Remain TBD/TBC | DBM-Deepcut line 1183 |
| Winter freeze protection | Insulation required | DBM-Deepcut line 2509 |
| Atmospheric spacing — distance between atmospheric tanks | 2.35 m (7.72 ft) | DBM-Deepcut line 268 (NFPA 30, Table 22.4.2.1) |
| Spacing — pressurized bullets to nearest atmospheric tank | 30.48 m (100 ft) | DBM-Deepcut line 265 (API 2510) |
| Spacing — atmospheric tanks to nearest public road | 80 m (262.5 ft) | DBM-Deepcut line 270 (OGAOM Sec. 9.6.15, DPR 48) |
| Spacing — fired heater to atmospheric tanks | 25 m (82 ft) | DBM-Deepcut line 297 (OGAOM Sec. 9.6.15) |
| Spacing — flare to atmospheric tanks (produced-water spacing reference) | 25 m (82 ft) | DBM-Deepcut line 283 (OGAOM Sec. 9.6.15; produced-water reference, applicability to process water TBC) |
| Operating temperature / pressure | TBD — not in available source |
| Liquid level instrumentation | Level instruments shall be connected to the drain where practical (plant-wide miscellaneous requirement) | DBM-Deepcut line 2510 |

## Construction

| Item | Basis | Source |
|---|---|---|
| Tank code | API 650 atmospheric storage tank | `_CONTEXT.md` package name; DBM-Deepcut line 2560 |
| Quantity supplied | 2 tanks (TK-5317-1, TK-5318-1) | DBM-Deepcut line 2628 |
| Insulation | Insulated to prevent winter freezing | DBM-Deepcut line 2509 |
| Tank Farm pump basis | Process water transfer pumps (radial centrifugal 2, x2) installed in Tank Farm Pump Building 2 — pump scope is in a separate package (Tank Farm Pump Building 2, row 83) and is referenced here as an interface only | DBM-Deepcut lines 2555, 2621 |
| Foundations | Geotechnical-engineered foundation and anchorage; project-wide loads and environmental basis | ASSUMPTION: same project-wide basis as other tanks |
| Layout / spacing | Atmospheric tank spacing per NFPA 30 / OGAOM / API 2510 (see Conditions) | DBM-Deepcut lines 265-297 |
| Materials of construction | TBD — not stated in source for process water tanks (no caustic/sour service flags noted for process water in source slice) |
| Internal coating | TBD — not stated in source |
| Heat tracing | TBD — only insulation is explicitly required by source |
| Vent / breather / EPRV | TBD — not stated in source for process water tanks |
| Nozzle schedule, manways, anchor chairs | TBD — not in available source |
| Modular / stick-built designation | TBD — not in available source (API 650 atmospheric tanks are typically field-erected) |

## References

- `_CONTEXT.md` — deliverable identity, package mapping, scope items, supported objectives
- `_REFERENCES.md` — authoritative decomposition basis and Shared Source Root
- GATE-07 PROJECT_DECOMP snapshot — `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (DEL-064-02 row)
  - `PACKAGE_REGISTER.csv`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
- DBM-Deepcut — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - Sec. Plant Layout / Spacing tables (lines 265-297)
  - Sec. Amine Regeneration / Module 530 (lines 1132, 1183)
  - Sec. NGL Mercaptan Treating Equipment and Utilities — make-up water (line 1556)
  - Sec. Miscellaneous Plant and Mechanical Requirements — water tanks insulation (line 2509)
  - Equipment count table — Tanks, Water (API 650) 2 (line 2560)
  - Tank Farm Pump Building 2 entries (line 2555)
  - Tag table — Tank Farm Pump Building 2 process water transfer pumps (line 2621)
  - Tag table — Tanks, Water (API 650) 2 (line 2628)
- 26020-Package_Requirements.docx — package heading 19 (location TBD; native .docx not parsed in this pass)
- 26020-Packages_Interfaces_4_export.xlsx (location TBD; native .xlsx not parsed in this pass)

## Open Items / TBD

- Tank mechanical datasheet values (diameter, height, shell/floor/roof MOC, design SG, design P/T, internal coating, heat tracing, PVRV/EPRV, nozzle schedule, manways, anchor chairs): TBD — not present in accessible sources for process water tanks.
- Process-water user rates and design throughput feeding sizing of TK-5317-1 / TK-5318-1: TBD/TBC per DBM-Deepcut line 1183.
- Tank fill source (raw water supply origin, treatment train, fill rate): TBD — not in available source slice.
- Truck-in / truck-out provisions, fuel-gas blanket, vent header tie-ins: TBD — not stated for process water tanks (caustic/DSO/produced-water practices in source are not directly transferable without confirmation).
- Final make-up water routing to NGL mercaptan treating system: TBC by detailed engineering (DBM-Deepcut line 1556).
- Package interface requirements matrix (electrical, instrument air, fill line, drain, transfer pump suction tie-ins, controls, fire-water cross-connections if any): TBD — to be developed from 26020-Packages_Interfaces_4_export.xlsx once parsed.
