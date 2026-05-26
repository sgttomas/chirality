# Datasheet — DEL-066-04 Vendor Engineered Equipment Package

> Deliverable: Vendor Engineered Equipment Package for PKG-066 "Tanks, Condendate (API 650) 4-25" (Condensate Storage Tanks at the 04-25 West Doe Deepcut expansion).
> Variant: PROJECT_DECOMP. Decomposition snapshot: GATE-07_Final_Published_2026-05-24.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-066-04_vendor-engineered-equipment-package | `_CONTEXT.md` Identity |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | PKG-066 | `_CONTEXT.md` |
| ParentWorkbookID | 66 | `_CONTEXT.md` |
| Package Name | Tanks, Condendate (API 650) 4-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Facility | West Doe Deepcut expansion, 04-25 (LSD 04-25-80-15W6) | `4-25_Deepcut_DBM.md` SEC-01 / Facility Identity |
| Owner | Tourmaline Oil Corporation | `4-25_Deepcut_DBM.md` SEC-01 / Facility Identity |
| Covered Scope Items | SOW-0205, SOW-0206, SOW-0207, SOW-0208 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives (ASSUMPTION; PACKAGE_HEURISTIC) | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `DELIVERABLE_REGISTER.csv` package-grouped mapping |

## Attributes — Tagged Equipment In Package

Per the workbook package roster (Packages row 90, package "Tanks, Condendate (API 650) 2", 4-25 / Deepcut), this vendor package covers five (5) condensate storage tanks:

| Tag | Service | Source |
|---|---|---|
| TK-9110-1 | Condensate Storage Tank | `4-25_Deepcut_DBM.md` package roster row 90 |
| TK-9120-1 | Condensate Storage Tank | `4-25_Deepcut_DBM.md` package roster row 90 |
| TK-9130-1 | Condensate Storage Tank | `4-25_Deepcut_DBM.md` package roster row 90 |
| TK-9140-1 | Condensate Storage Tank | `4-25_Deepcut_DBM.md` package roster row 90 |
| TK-9150-1 | Condensate Storage Tank | `4-25_Deepcut_DBM.md` package roster row 90 |

CONFLICT C-01: The DBM Product Storage narrative (§ Condensate Product Storage) states "four 3,800 bbl condensate product storage tanks" while the package roster row 90 lists five tagged tanks. See `Guidance.md` Conflict Table; vendor scope must clarify final tank count with the EPC Integrator before fabrication.

## Conditions — Design Basis Values (Per Source)

| Parameter | Basis | Source |
|---|---|---|
| Tank specification | Modified API 650 | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Design pressure | Atmospheric tank with 16 oz test pressure | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Maximum fill shutdown limit | 90% of tank volume | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Individual tank nominal volume | 3,800 bbl (per DBM narrative; tank count per roster row 90 — see C-01) | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Local storage duration | ~4.5 days for liquids-hub upset | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Service fluid | Stabilized C5+ condensate (stabilizer bottoms) | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Condensate product tank design SG | 1.0 | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Insulation, product condensate tanks | Non-insulated; recycle may be required for winter temperature maintenance | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Blanket gas | Provided for winter vacuum prevention; rates per API 2000 | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Vapour disposition | Connected to VRU suction header (Module 930 C5+ storage tanks) | `4-25_Deepcut_DBM.md` § Condensate Product Storage; § VRU Configuration |
| Tank arrangement | Two tanks designated as inlet tanks with internal pipe stand cascade to downstream tanks; common truck-out connection | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| EPRV sizing | TBD — detailed-engineering review item | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Off-spec condensate overhead vent sizing | TBD — detailed-engineering review item | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Tank isolation philosophy (possible sour vapours) | TBD — detailed-engineering review item | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Thermal expansion review across ambient range | TBD — detailed-engineering review item | `4-25_Deepcut_DBM.md` § Condensate Product Storage |

### Stored Fluid Density Basis (kg/m3)

| Temperature, deg C | Combined / stabilizer-only C5+ density | Stabilizer C5+ density |
|---:|---:|---:|
| -40 | 709.8 | 732.2 |
| 15 | 658.6 | 682.7 |
| 35 | 638.8 | 663.6 |
| 43.3 | 630.3 | 655.4 |
| 48 | 624.5 | 649.9 |
| 60 | 612.6 | 638.6 |

Source: `4-25_Deepcut_DBM.md` § Condensate Product Storage. Per the same source, combined-flow and stabilizer C5+ density values are the operative storage-design values; depropanizer-density rows in the historical record are not active.

## Construction

| Parameter | Basis | Source |
|---|---|---|
| Code of construction | Modified API 650 (atmospheric, low-pressure) | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Tank-to-tank spacing | 2.35 m (7.72 ft) per NFPA 30 Table 22.4.2.1 (applies to atmospheric tanks at facility) | `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing |
| Tank-to-public-road | 80 m (262.5 ft) per OGAOM § 9.6.15, DPR 48 | `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing |
| Flare to atmospheric condensate tanks | 50 m (164 ft) per OGAOM § 9.6.15 | `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing |
| Fired heater to atmospheric tanks | 25 m (82 ft) per OGAOM § 9.6.15 | `4-25_Deepcut_DBM.md` § Atmospheric Tank and General Plant Spacing |
| Internal pipe stand | Required to cascade condensate from inlet tanks to downstream tanks | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Truck-out connections | Common truck-out connection across inlet and outlet condensate tanks | `4-25_Deepcut_DBM.md` § Condensate Product Storage |
| Foundations, anchorage, seismic, wind | TBD — site-specific civil/structural basis not present in accessible sources |
| Coatings, corrosion allowance, materials of construction | TBD — not specified in accessible sources for product condensate tanks (produced-water tank Devchem 253 coating is for a different service) |
| Plot plan coordinates | TBD — governing drawing CIV-235633-5002 is not in the accessible publication input package per DBM | `4-25_Deepcut_DBM.md` § Existing-Facility Interfaces and Metering / Plot plan |

## References

- `_CONTEXT.md` (deliverable identity, scope, supports/covers)
- `_REFERENCES.md` (authoritative basis pointers)
- `_DEPENDENCIES.md` (declared upstream/downstream; none declared at PREPARATION)
- `4-25_Deepcut_DBM.md` — accessible at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
  - § Product Storage and Pumps / Condensate Product Storage
  - § Atmospheric Tank and General Plant Spacing
  - § Vapour Recovery Unit / VRU Configuration and Design Parameters (Module 930 C5+ storage tanks)
  - § package roster row 90 (PKG ID "Tanks, Condendate (API 650) 2", 5 tanks, TK-9110/20/30/40/50-1)
- `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot), rows DEL-066-01 through DEL-066-06
- `26020-Package_Requirements.docx` package heading 21 — referenced by decomposition row; **not directly readable** from this run (.docx). Relevant package-requirements clause-level requirements are therefore `location TBD`.
- `26020-Packages_Interfaces_4_export.xlsx` — referenced by decomposition row; **not directly readable** from this run (.xlsx).
