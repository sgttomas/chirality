# Datasheet — Construction Work Package (DEL-059-03)

> Deliverable: `DEL-059-03_construction-work-package` — EPC Integrator Construction Work Package datasheet for the Storage Bullets package (PKG-059). The deliverable describes how the storage bullet package will be physically installed, built, inspected, turned over, and tied into the larger 04-25 facility. Source-grounded primarily in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` and the accepted GATE-07 decomposition snapshot. The cited workbook (`Workbook Packages row 83`) and the package requirements Word document (`26020-Package_Requirements.docx` package heading 14) are referenced by the decomposition but were not available as locally readable text slices at drafting time; rows that depend solely on those sources are marked `location TBD` or `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-059-03_construction-work-package` | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-059` | `_CONTEXT.md` |
| ParentWorkbookID | 59 | `_CONTEXT.md` |
| PackageName | Storage Bullets | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` |
| Facility | 04-25 (Deepcut) | DBM-Deepcut line 32 (04-25 expansion basis) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Decomposition Basis | PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |
| Primary Source Slice | DBM-Deepcut Sec. "NGL Storage Bullets" (lines 1627-1629), Product Storage table (line 492), Pressurized Bullet Spacing (lines 245-266), NGL storage area grading (line 2722) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |

ASSUMPTION: The PKG-059 package register name ("Storage Bullets") and `_CONTEXT.md` scope text ("two unstable condensate storage bullets and sixteen LPG product storage bullets for C5 condensate and LPG product storage") describe the workbook-era scope. The accepted current-state DBM basis (DBM-Deepcut lines 448, 492, 1627-1629) re-bases storage to **16 x 120,000 USG NGL storage bullets** and explicitly notes the C3/C4 LPG storage concept was retired with the depropanizer. See `Guidance.md` Conflict Table.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Bullet count (current DBM basis) | 16 storage bullets | DBM-Deepcut line 448, 492, 1629 |
| Bullet capacity (each) | 120,000 USG | DBM-Deepcut lines 448, 492, 1629 |
| Storage service | C3+ NGL product storage | DBM-Deepcut line 492 |
| Production-rate basis | 15,400 bbl/d | DBM-Deepcut lines 448, 492 |
| Storage duration basis | 2.5 days | DBM-Deepcut lines 448, 492 |
| Downstream disposition | NRM NEBC Connector via LACT | DBM-Deepcut line 492 |
| Bullet tags | TBD | Tags for storage bullets not enumerated in available source slice (DBM-Deepcut equipment tag tables at lines 2557-2627 list condensate (API 650) tanks `TK-9110-1...TK-9150-1` and produced-water tanks `TK-9010-1, TK-9020-1`, not bullets). `location TBD` |
| Bullet design pressure | TBD | Not in available source slice |
| Bullet design temperature | TBD | Not in available source slice |
| MOC | TBD | Not in available source slice |
| Detailed bullet design parameters | Required design-development item | DBM-Deepcut line 1629 ("not fully developed in the available product-storage basis and remain a required design-development item") |
| Module/skid identifier | TBD (no bullet module entry found in DBM modularization table) | location TBD |
| Cluster arrangement | <=6 bullets per cluster | DBM-Deepcut line 249 (API 2510) |
| Bullet-to-bullet (butane to propane) | 2.804 m (9.2 ft) | DBM-Deepcut line 251 (API 2510) — ASSUMPTION: applies to mixed NGL bullets; verify against final product slate |
| Bullet cluster-to-cluster spacing | 15.24 m (50 ft) | DBM-Deepcut line 250 (API 2510) |
| Bullet-to-pump skid (related) | 3.05 m (10 ft) | DBM-Deepcut line 252 (API 2510) |
| Bullet-to-unrelated rotating equipment | 15.24 m (50 ft) | DBM-Deepcut line 253 (API 2510) |
| Bullet-to-facility-control building | 15.24 m (50 ft) | DBM-Deepcut line 254 (API 2510) |
| Bullet-to-non-control building | 30.48 m (100 ft) | DBM-Deepcut line 255 (API 2510) |
| Bullet-to-process-vessel | 15.24 m (50 ft) | DBM-Deepcut line 256 (API 2510) |
| Bullet-to-truck-loading-station | 15.24 m (50 ft) | DBM-Deepcut line 257 (API 2510) |
| Bullet-to-property-line | 38.1 m (125 ft) | DBM-Deepcut line 259 (API 2510 Table 1) |
| Bullet-to-nearest atmospheric tank | 30.48 m (100 ft) | DBM-Deepcut line 265 (API 2510) |
| Bullet-to-nearest spill containment area | 3.05 m (10 ft) | DBM-Deepcut line 266 (API 2510) |
| Bullet-to-flare | 30.48 m (100 ft) | DBM-Deepcut line 284 (API 2510) |
| Bullet-to-fired-heater | 15.24 m (50 ft) | DBM-Deepcut line 299 (API 2510) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site grading under bullets | Sloped (potentially southbound) to redirect NGL away from pipe rack and process areas | DBM-Deepcut line 2722 |
| Spill / leak surface control | Berm, elevation decline, or other surface-control feature for accidental leak/spill containment | DBM-Deepcut line 2722 |
| Pool-fire exposure mitigation | Achieved via grading and surface-control features above | DBM-Deepcut line 2722 |
| Facility alarm beacon presence | Beacon group near the NGL Storage Area | DBM-Deepcut line 3262 |
| Adjacent storage interface | Atmospheric storage tank area for produced water and condensate tanks; separate beacon group provided there | DBM-Deepcut line 3262 |
| Co-located packages requiring tie-in coordination | NGL loading, NGL product pumps, NGL product booster pumps | DBM-Deepcut line 73 |
| Local condensate storage interface | 4 x 3,800 bbl condensate product storage tanks at 04-25 (separate package; located in adjacent tank area) | DBM-Deepcut line 1639 |
| Construction sequencing constraint to product storage downstream system | LACT/NRM NEBC connector tie-in required for product run-down | DBM-Deepcut line 492 |
| Spacing-code retained terminology note | Existing LPG terminology in spacing tables is retained as an API 2510 application descriptor; does not alter current NGL product-handling scope | DBM-Deepcut lines (LPG spacing retention note near spacing table) |

## Construction

| Item | Basis | Source |
|---|---|---|
| Civil / foundations scope | Bullet foundations, grading per slope basis, berm / surface-control structure under bullets, pipe-rack/process-area isolation grading | DBM-Deepcut line 2722; ASSUMPTION for civil discipline package boundaries |
| Mechanical erection scope | Set 16 x 120,000 USG bullets per layout meeting API 2510 spacing | DBM-Deepcut lines 245-299, 1629 |
| Piping tie-ins | NGL inlet from upstream NGL dehydration / treating; NGL outlet to NGL product / booster pumps and onward to LACT and NRM NEBC connector | DBM-Deepcut lines 73, 492, 1408 |
| Relief / flare tie-ins | Pressurized vessel relief routing to applicable flare header (HP/cryo or LP per detailed design) | DBM-Deepcut lines 245-299 (spacing implies adjacency to flare system); detailed routing TBD — location TBD |
| Drainage / spill containment tie-ins | NGL storage area grading and containment per design; routing TBD | DBM-Deepcut line 2722 |
| Electrical / instrumentation tie-ins | Beacon group near NGL Storage Area; remaining E&I tie-ins (power, grounding, EHT where applicable, controls) per package interface matrix | DBM-Deepcut line 3262; remaining items `TBD` from `26020-Package_Requirements.docx` package heading 14 (not locally available) |
| Cathodic protection | TBD | Not in available source slice |
| Insulation / EHT | TBD (bullets are pressurized vessels; specific tracing/insulation philosophy not stated for bullets in available source) | location TBD |
| Inspections (vessel) | Hydrotest, NDE, code-stamp verification per applicable vessel code | ASSUMPTION (standard EPC inspection scope); 26020-Package_Requirements.docx package heading 14 likely governs — location TBD |
| Inspections (interfaces) | Tie-in line walk-down; piping radiography to package boundary as per facility ITP | ASSUMPTION (standard EPC inspection scope) — location TBD |
| Pre-commissioning | Hydrotest / pneumatic test of new piping, line flushes, leak tests, dryness/inert purge | ASSUMPTION (standard EPC pre-commissioning) — location TBD |
| Turnover scope | Mechanical completion of bullet field, ITP/inspection records, vendor documentation, system handover to commissioning | ASSUMPTION (standard EPC turnover) — location TBD |
| Modularization status | No specific bullet shop-module entry identified in DBM modularization table; field-set assumed for large NGL bullets | ASSUMPTION; verify against bullet vendor scope |

## References

- `_CONTEXT.md` — deliverable identity, scope, and decomposition pointer
- `_REFERENCES.md` — reference inventory
- `_DEPENDENCIES.md` — declared dependencies (none yet declared)
- GATE-07 `PACKAGE_REGISTER.csv` row PKG-059 — package definition, interfaces, source basis
- GATE-07 `DELIVERABLE_REGISTER.csv` row DEL-059-03 — deliverable definition, anticipated artifacts, SOW IDs (SOW-0181..SOW-0184), supports objectives
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - Lines 32, 40 — 04-25 expansion / facility basis
  - Line 73 — NGL package list including NGL storage bullets, NGL loading, NGL product pumps, NGL product booster pumps
  - Lines 245-266, 284, 299 — Pressurized bullet spacing (API 2510)
  - Lines 448, 492 — Current 04-25 NGL storage basis (16 x 120,000 USG, 15,400 bbl/d, 2.5 days)
  - Line 1408 — Storage area scope summary
  - Lines 1627-1629 — NGL Storage Bullets section, replacement of retired C3/C4 LPG concept, design-development gap acknowledgement
  - Line 1639 — Local 04-25 condensate storage (4 x 3,800 bbl tanks; separate package)
  - Line 1814 — Identified design-development item to develop detailed basis for 16 x 120,000 USG NGL storage bullets
  - Line 2722 — NGL storage area grading and containment guidance
  - Line 3262 — Facility alarm beacon location near NGL Storage Area
- `26020-Package_Requirements.docx` package heading 14 — package requirements document referenced by decomposition; not available as readable text at drafting time (location TBD for clause-level citations)
- `Workbook Packages row 83` — workbook entry referenced by decomposition; package definition is reproduced into the accepted GATE-07 `PACKAGE_REGISTER.csv`
