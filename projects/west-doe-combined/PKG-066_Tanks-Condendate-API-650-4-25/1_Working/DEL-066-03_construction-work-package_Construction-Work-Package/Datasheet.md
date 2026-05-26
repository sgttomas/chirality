# Datasheet — DEL-066-03 Construction Work Package (PKG-066 Tanks, Condensate (API 650) 4-25)

> Descriptive document. The Construction Work Package (CWP) is itself the construction-execution dossier for the package; this datasheet identifies and describes the CWP-relevant attributes of the equipment package being installed.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-066-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| Parent Package ID | `PKG-066` | `_CONTEXT.md` |
| Package Name | Tanks, Condensate (API 650) 4-25 | `_CONTEXT.md` (workbook label uses "Condendate") |
| Facility | 04-25 Deepcut Gas Plant (West Doe) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"This DBM is the governing basis-of-design document …" |
| Equipment Type | Modified API 650 atmospheric storage tanks, condensate service | DBM-Deepcut line 1646 ("Condensate tank specification: Modified API 650"); line 2557 ("Tanks, Condendate (API 650) 2 — Condensate Storage Tanks") |
| Tag Set | TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1 (5 tanks) | DBM-Deepcut line 2625 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Responsible Party (EPC) | EPC Integrator | `_CONTEXT.md` |
| Field Construction Responsibility | Tourmaline Oil Corporation (owner-managed field construction) | DBM-Deepcut §"Construction Responsibility", lines 101-127 |
| Covered SOW Items | SOW-0205, SOW-0206, SOW-0207, SOW-0208 | `_CONTEXT.md` |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION: package-grouped objective heuristic per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |

## Attributes (package equipment as it pertains to construction)

| Attribute | Value | Source |
|---|---|---|
| Number of tanks installed under this package (4-25) | 5 | DBM-Deepcut line 2625 |
| Nominal capacity per tank | 3,800 bbl | DBM-Deepcut line 1640 ("4 x 3,800 bbl tanks" local storage; line 495 sister 03-25 6 x 3,800 bbl). Quantity CONFLICT — see Conflict Table in Guidance. |
| Specification basis | Modified API 650 atmospheric tank, 16 oz test pressure | DBM-Deepcut lines 1646-1647; line 518 |
| Maximum fill | 90% of tank volume | DBM-Deepcut line 1648 |
| Service classification | Two inlet condensate tanks (sediment/water collection) cascading by elevation to product tanks; one slop tank with dedicated envirobox truck-in/out | DBM-Deepcut line 1661; line 1665 |
| Insulation | Slop tank fully insulated; product condensate tanks non-insulated (winter recycle may be required) | DBM-Deepcut lines 1644-1645 |
| Blanket gas | Required (winter vacuum prevention; API 2000 basis) | DBM-Deepcut line 1663 |
| Vent collection | Connected to VRU suction header | DBM-Deepcut line 1663 |
| Tank-farm interfaces (CWP relevance) | Stabilizer outlet header; LP condensate pump header; hydrocarbon drain header; common truck-out connection; VRU suction header | DBM-Deepcut lines 1661-1665 |
| Tank-farm pump module (adjacent install) | Product recycle pump (1x100%); condensate skim pump (1x100%); condensate transfer pumps P-9210-1 / P-9220-1 (2x150%) | DBM-Deepcut lines 1669-1674 |

## Conditions (site/environmental that govern construction)

| Condition | Value | Source |
|---|---|---|
| Minimum ambient design temperature | -40 deg C | DBM-Comp_and_Liquids line 145 (cross-facility West Doe basis); DBM-Deepcut line 1679 (transfer pump motor startup at -40 deg C) |
| Tank winterization | External insulation + heating where required (per service); product tanks non-insulated with recycle option | DBM-Deepcut line 1645; line 524 (sour-water tank externally insulated/heated reference comparator) |
| Foundation basis | Final geotechnical report required before foundation design closure | DBM-Comp_and_Liquids lines 141, 688, 700 |
| Plot/layout drawing | CIV-235633-5002 not available in source package — coordinates TBD | DBM-Deepcut line 323 |

## Construction (CWP-defining attributes)

| Item | Value | Source |
|---|---|---|
| Construction method | Field-erected (consistent with API 650 modified atmospheric tank service); tank-farm pump module shop-fabricated/site-set per DBM module philosophy | ASSUMPTION (API 650 tanks are field-erected by industry convention); DBM-Deepcut lines 1671-1673 (pump module) |
| Construction manager | Tourmaline field construction scope | DBM-Deepcut line 107 |
| Grading / piling / foundation | Tourmaline field construction scope | DBM-Deepcut lines 108-109 |
| Mechanical hookup | Tourmaline field construction scope | DBM-Deepcut line 114 |
| Shipped-loose instruments & valves install | Tourmaline field construction scope | DBM-Deepcut line 115 |
| ISBL/OSBL tie-in piping responsibility | External interface marker — responsibility to be confirmed per tie-in | DBM-Deepcut lines 117, 174 |
| Cabling, terminations, area lighting | Tourmaline field construction scope | DBM-Deepcut lines 118-120 |
| Fence/security | Tourmaline field construction scope | DBM-Deepcut line 121 |
| Tie-in joint planning | Required; timing established as project progresses | DBM-Deepcut line 127 |
| Construction work package register alignment | Required against plot plan and equipment list before issue for construction | DBM-Comp_and_Liquids line 661 |

## References

- `_REFERENCES.md` (this deliverable)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (authoritative 04-25 facility basis)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (cross-facility tank-design comparator and construction-scope summary)
- `26020-Package_Requirements.docx`, package heading 21 — referenced by `_CONTEXT.md`; text not locally accessible. `location TBD`.
- `26020-Packages_Interfaces_4_export.xlsx`, workbook Packages row 89 — referenced by `_CONTEXT.md`; tabular content not locally extracted. `location TBD`.
- Decomposition snapshot `GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (deliverable narrative).
