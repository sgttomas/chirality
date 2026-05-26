# Datasheet — DEL-059-01_scope-of-work — Scope of Work (PKG-059 Storage Bullets)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-059-01_scope-of-work` | `_CONTEXT.md` |
| Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-059` | `_CONTEXT.md` |
| PackageName | Storage Bullets | `_CONTEXT.md`; PACKAGE_REGISTER row 83 |
| Workbook Row | 83 | PACKAGE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv |
| CoA Tracking Number | 26020-01-17-007 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Two unstable condensate storage bullets plus sixteen LPG product storage bullets for C5 condensate and LPG product storage | SCOPE_LEDGER SOW-0182 (26020-Package_Requirements.docx package heading 14) |
| Number of unstable condensate bullets | 2 | SCOPE_LEDGER SOW-0183 |
| Number of LPG product bullets | 16 | SCOPE_LEDGER SOW-0183 |
| Bullet geometry (each) | 3658 mm ID x 42494 mm seam-to-seam | SCOPE_LEDGER SOW-0183 |
| Nominal volume per bullet | 454 m3 / 120,000 US gal at 84% maximum volume | SCOPE_LEDGER SOW-0183 |
| Design pressure | 1724 kPag | SCOPE_LEDGER SOW-0183 |
| Design temperature | 66 C | SCOPE_LEDGER SOW-0183 |
| External pressure | Full vacuum | SCOPE_LEDGER SOW-0183 |
| Mounting | Outdoor, saddle, with stairs/platforms | SCOPE_LEDGER SOW-0183 |
| NGL storage basis (facility) | 16 x 120,000 USG NGL storage bullets at 04-25; production-rate basis 15,400 bbl/d; 2.5 days storage | DBM-Deepcut/4-25_Deepcut_DBM.md, "Current 04-25 NGL storage basis" (lines ~448, 492, 1627-1629) |
| Tagged Equipment Class | 26020-01-PT-17-007 — Pressure Vessels (Storage Bullets) | PACKAGE_REGISTER.csv |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service — unstable condensate bullets | Store condensate from the C5 product line, upstream of the condensate transfer pumps | SCOPE_LEDGER SOW-0184 |
| Service — LPG bullets | Store C3, C4, or C3/C4 LPG mix from the depropanizer, upstream of transfer-to-liquids-hub booster pumps | SCOPE_LEDGER SOW-0184 |
| Vapour equalization | LPG vapour equalization must avoid pockets | SCOPE_LEDGER SOW-0184 |
| Butane blanket gas | Butane storage requires blanket gas | SCOPE_LEDGER SOW-0184 |
| Location context | 04-25 Deep Cut Gas Plant, integrated with NGL/condensate product handling | DBM-Deepcut/4-25_Deepcut_DBM.md SEC NGL Storage Bullets (line ~1627) |
| Sour-service / safety regime | Sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory codes/standards apply at package interface | OBJECTIVE_REGISTER OBJ-009 |

## Construction

| Item | Provision | Source |
|---|---|---|
| Package engineering | Package Vendor scope | PACKAGE_REGISTER row 83 (Responsibility column); SCOPE_LEDGER SOW-0181 |
| Package design | Package Vendor scope | PACKAGE_REGISTER row 83; SCOPE_LEDGER SOW-0181 |
| Vendor documentation | Package Vendor scope | PACKAGE_REGISTER row 83; SCOPE_LEDGER SOW-0181 |
| Physical equipment package | Package Vendor scope | PACKAGE_REGISTER row 83; SCOPE_LEDGER SOW-0181 |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator scope | PACKAGE_REGISTER row 83; SCOPE_LEDGER SOW-0181 |
| Foundations | By others (not in Package Vendor scope) | SCOPE_LEDGER SOW-0184 |
| DCS integration | By others (not in Package Vendor scope) | SCOPE_LEDGER SOW-0184 |
| Electrical supply to MCC | By others (not in Package Vendor scope) | SCOPE_LEDGER SOW-0184 |
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | INTERFACE_REGISTER (10 PKG-059 rows); PACKAGE_REGISTER row 83 |

## Covered Scope Items

| Scope Item | Summary | Source |
|---|---|---|
| SOW-0181 | Carry the workbook-defined vendor-responsible Mechanical "Storage Bullets" package; vendor owns engineering/design/equipment; EPC owns facility integration. | SCOPE_LEDGER.csv |
| SOW-0182 | Basic scope: supply two unstable condensate storage bullets and sixteen LPG product storage bullets. | SCOPE_LEDGER.csv |
| SOW-0183 | Major included equipment, including bullet geometry, design pressure/temperature, mounting. | SCOPE_LEDGER.csv |
| SOW-0184 | Scope notes and open items, including service definition, vapour equalization, butane blanket gas, and by-others items. | SCOPE_LEDGER.csv |

## Supported Objectives (ASSUMPTION — package-grouping heuristic)

OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010.

ASSUMPTION: associations are inherited from PACKAGE_REGISTER row 83 (PKG-059) via the package-grouping heuristic. Confirm with human ruling if a deliverable-ID-explicit mapping must be authoritative.

Source: OBJECTIVE_DELIVERABLE_MAP.csv (rows mapping DEL-059-01_scope-of-work to OBJ-001, OBJ-003..OBJ-010); OBJECTIVE_REGISTER.csv.

## References

- `_CONTEXT.md` (deliverable-local)
- `_REFERENCES.md` (deliverable-local)
- GATE-07 PACKAGE_REGISTER.csv (row PKG-059, row 83)
- GATE-07 DELIVERABLE_REGISTER.csv
- GATE-07 SCOPE_LEDGER.csv (SOW-0181..SOW-0184)
- GATE-07 INTERFACE_REGISTER.csv (10 PKG-059 rows)
- GATE-07 ARTIFACT_REGISTER.csv (ART-E74992DA9A, ART-D07C763AAE, ART-07935F28C9, ART-F8F9048873, ART-3213233765)
- GATE-07 OBJECTIVE_REGISTER.csv (OBJ-001, OBJ-003..OBJ-010)
- GATE-07 OBJECTIVE_DELIVERABLE_MAP.csv
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (NGL Storage Bullets section; Pressurized Bullet Spacing tables)
- `_Sources/26020-Package_Requirements.docx` package heading 14 — `location TBD` for verbatim slices (binary not parsed in-run; content carried via SCOPE_LEDGER extraction rows)
