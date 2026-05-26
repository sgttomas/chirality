# Specification — Package Datasheet (DEL-064-02), PKG-064 Tanks, Water (API 650) 4-25

> Normative requirements for the EPC Integrator Package Datasheet covering the Process Water Storage Tanks (TK-5317-1, TK-5318-1) at the 04-25 (Deepcut) facility. Requirements are grounded in the GATE-07 decomposition snapshot and the Deepcut DBM. Inferred items are labeled ASSUMPTION; missing values are TBD.

## Scope

**In scope of the Package Datasheet:**
- Two atmospheric API 650 process water storage tanks: TK-5317-1 and TK-5318-1 located at 04-25 (Deepcut). (DBM-Deepcut lines 2560, 2628)
- All tank mechanical attributes, design conditions, materials, coatings, insulation/freeze protection, and nozzle/vent provisions required for third-party vendor or discipline package engineering and design. (`_CONTEXT.md` Scope; deliverable description)
- Package interface requirements matrix supporting EPC-to-vendor handoff: fill source tie-in, transfer-pump suction tie-in (to Tank Farm Pump Building 2 — P-5317-1 / P-5318-1), drains, instrumentation/controls, electrical, freeze protection. (DBM-Deepcut lines 2555, 2621)

**Out of scope of this datasheet:**
- The Process Water Transfer Pumps P-5317-1 / P-5318-1 themselves are part of Tank Farm Pump Building 2 (Workbook row 83; tag-table row 2621) and are not equipment items of PKG-064; only the tank-side interface is in scope here.
- Other water-service tanks: produced-water tanks (PKG separately, TK-9010-1 / TK-9020-1; DBM-Deepcut line 2627) and condensate/caustic/DSO/sour-water tanks.
- Downstream water-using systems (amine regeneration Module 530, NGL mercaptan treating make-up).

## Requirements

| Req ID | Requirement | Source / Status |
|---|---|---|
| REQ-064-02-001 | The package shall comprise two (2) atmospheric storage tanks designed and constructed to API 650, tagged TK-5317-1 and TK-5318-1, located at the 04-25 (Deepcut) facility. | DBM-Deepcut lines 2560, 2628 |
| REQ-064-02-002 | The tanks shall be insulated to prevent winter freezing. | DBM-Deepcut line 2509 (plant-wide miscellaneous requirement: "water tanks shall be insulated to prevent winter freezing") |
| REQ-064-02-003 | Level instruments on each tank shall be connected to the drain where practical. | DBM-Deepcut line 2510 (plant-wide miscellaneous requirement) |
| REQ-064-02-004 | The tank package shall accommodate withdrawal by the Process Water Transfer Pumps (P-5317-1, P-5318-1) installed in Tank Farm Pump Building 2 (interface boundary at tank suction nozzles). | DBM-Deepcut lines 2555, 2621 |
| REQ-064-02-005 | The tank package shall be capable of supplying process water to (a) the amine regeneration module (Module 530) for process-water user demand and (b) the NGL mercaptan treating system for upset-case caustic-train make-up water. Final routing to the mercaptan treating system is to be confirmed in detailed engineering. | DBM-Deepcut lines 1132, 1183, 1556 |
| REQ-064-02-006 | Atmospheric tank spacing shall meet: 2.35 m (7.72 ft) between atmospheric tanks (NFPA 30 Table 22.4.2.1); 30.48 m (100 ft) from pressurized bullets (API 2510); 80 m (262.5 ft) to nearest public road (OGAOM Sec. 9.6.15 / DPR 48); 25 m (82 ft) from fired heaters (OGAOM Sec. 9.6.15). | DBM-Deepcut lines 265, 268, 270, 297 |
| REQ-064-02-007 | The Package Datasheet shall populate all mandatory fields required for third-party vendor or discipline package engineering and design (per deliverable description). Where the accepted source basis does not yet specify a value, the field shall carry TBD with a named owner for resolution in detailed engineering. | `_CONTEXT.md` Scope; GATE-07 DELIVERABLE_REGISTER DEL-064-02 description |
| REQ-064-02-008 (ASSUMPTION) | Tanks shall be designed for an atmospheric (low-pressure) basis consistent with API 650 (e.g., 16 oz test pressure has been applied to other modified-API-650 atmospheric tanks at this facility — produced-water tank reference, DBM-Deepcut line 518). The exact internal-pressure / vacuum basis for process-water tanks is TBC in detailed engineering. | ASSUMPTION; DBM-Deepcut line 518 (reference only) |
| REQ-064-02-009 | Tank foundations and anchorage shall be designed per final geotechnical report, equipment loads, snow/wind/seismic, frost, vibration, settlement, and maintenance access (project-wide basis). | ASSUMPTION (project-wide basis applies); not stated explicitly for process water tanks in available slice |
| REQ-064-02-010 | Design specific gravity, design pressure, design temperature, MOC (shell/floor/roof), internal coating, heat tracing, PVRV/EPRV sizing, venting routing, and nozzle/manway schedule shall be specified in the issued datasheet. Values are TBD pending detailed engineering and source-document parsing (26020-Package_Requirements.docx heading 19; 26020-Packages_Interfaces_4_export.xlsx). | TBD |

## Standards

| Standard | Applies To | Local Slice / Status |
|---|---|---|
| API 650 — Welded Tanks for Oil Storage | Tank construction (atmospheric) | Identified by package name and DBM-Deepcut line 2560; clause-level text not locally accessible — location TBD |
| API 2510 — Design and Construction of LPG Installations | Spacing between pressurized bullets and atmospheric tanks (30.48 m / 100 ft) | DBM-Deepcut line 265 |
| NFPA 30 — Flammable and Combustible Liquids Code | Atmospheric-tank-to-atmospheric-tank spacing (Table 22.4.2.1) | DBM-Deepcut line 268 |
| OGAOM Sec. 9.6.15 | Tank-to-public-road and fired-heater spacing | DBM-Deepcut lines 270, 297 |
| DPR 48 | Tank-to-public-road spacing reference | DBM-Deepcut line 270 |
| 26020 Package Requirements (heading 19) | Mandatory package datasheet content per project | location TBD; native .docx not parsed in this pass |

## Verification

| Req ID | Verification Method |
|---|---|
| REQ-064-02-001 | Vendor documentation review against API 650 (Manufacturer's Data Report); tag confirmation against GATE-07 PACKAGE_REGISTER and DBM-Deepcut tag table |
| REQ-064-02-002 | Vendor design review; insulation thickness calculation against site winter design temperature (TBD) |
| REQ-064-02-003 | Drawing/P&ID review of level instrument tie-ins; field walkdown |
| REQ-064-02-004 | Interface drawing review (tank suction nozzles vs. P-5317-1 / P-5318-1 suction headers); hydraulic check by detailed engineering |
| REQ-064-02-005 | P&ID review of process-water distribution headers to Module 530 and to mercaptan-treating make-up tie-in |
| REQ-064-02-006 | Plot plan review against quoted spacing tables; site inspection |
| REQ-064-02-007 | Datasheet completeness audit by EPC Integrator before vendor RFQ issue |
| REQ-064-02-008 | Vendor design pressure / vacuum basis confirmation against API 650 venting calculation |
| REQ-064-02-009 | Geotechnical sign-off; foundation calculation review |
| REQ-064-02-010 | EPC Integrator close-out of TBDs prior to package datasheet IFC issue |

## Documentation

Per the deliverable's anticipated artifacts (`_CONTEXT.md`):

- Package technical datasheet (this deliverable's primary artifact)
- Vendor engineering handoff basis
- Package interface requirements matrix
- Source-supported equipment and design criteria

Supporting and feeder documents:

- GATE-07 PROJECT_DECOMP snapshot (DELIVERABLE_REGISTER, PACKAGE_REGISTER, OBJECTIVE_DELIVERABLE_MAP)
- DBM-Deepcut (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`)
- 26020-Package_Requirements.docx package heading 19 (location TBD — to be parsed)
- 26020-Packages_Interfaces_4_export.xlsx (location TBD — to be parsed)
