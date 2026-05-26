# Datasheet — DEL-096-03 Construction Work Package (PKG-096 Tanks, Sour Condensate API 650)

> Descriptive document. Values are quoted from authoritative source slices. Missing values are marked `TBD`; inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-096-03_construction-work-package` | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-096` | `_CONTEXT.md` |
| Package Name | Tanks, Sour Condensate (API 650) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-096 |
| Workbook Row | 92 | `DELIVERABLE_REGISTER.csv` row DEL-096-03 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Equipment Tags Covered | TK-9110-2; TK-9120-2 | `26020-Package_Requirements.docx` H1 #48 "26020-03-PT-19-005 - Tanks, Sour Condensate", Basic Scope |

## Attributes (Subject Equipment Being Constructed)

| Attribute | Value | Source |
|---|---|---|
| Process Function | Sour C5+ Condensate Storage Tanks | `26020-Package_Requirements.docx` H1 #48, Basic Scope |
| Number of Tanks | Two (2) | `26020-Package_Requirements.docx` H1 #48, Basic Scope |
| Nominal Capacity (each) | 3800 bbl | `26020-Package_Requirements.docx` H1 #48, Basic Scope / Major Included Equipment |
| Design & Fabrication Code | Modified API 650 | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment |
| Insulation | Non-insulated | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment |
| Blanket Gas System | Per API 2000 | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment |
| Service Class | Sour service (H2S present), NACE compliant | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment |
| Internal Coating (floors, walls, roofs) | Devchem 253 | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment |
| Relief Devices (each tank) | PVRV (vacuum / modulating pressure relief); EPRV (emergency relief); VRU header connection | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment |
| Maximum Fill Limit | 90% shutdown | `26020-Package_Requirements.docx` H1 #48, Major Included Equipment |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating Pressure | Atmospheric | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Operating Temperature (Item No. 1) | Ambient | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Operating Temperature (Item No. 2) | 5 °C (min) – 40 °C (max) | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Design Pressure | 32 oz test pressure | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Design Temperature | -40 °C (min) – 60 °C (max) | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Design Flow (Item No. 1) | 27,606 kg/h / 919 Am3/d | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Design Flow (Item No. 2) | 94,940 kg/h / 3187 Am3/d | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |

## Construction (EPC Integrator Scope Surface)

> The package vendor delivers the engineered tank package. The EPC Integrator's Construction Work Package covers physical installation, tie-ins, inspection, and turnover. Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase etc. are explicitly "By Others" in the vendor scope (source-stated) and are therefore EPC-Integrator construction scope.

| Construction Element | Disposition | Source |
|---|---|---|
| Foundations | By Others (EPC scope) | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Site mounting of tanks | By Others (EPC scope) | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Electrical / instrumentation | By Others (EPC scope) | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Platforms, staircase | By Others (EPC scope) | `26020-Package_Requirements.docx` H1 #48, Scope Notes / Open Items |
| Process Piping interface | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| Relief / Flare / Vent interface | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| Drain / Containment interface | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| Area / Exterior Lighting interface | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary (row 92, col M) |
| Grounding / Bonding interface | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| Cathodic Protection interface | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| I&C / Control Cabling interface | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| Grading / Site Drainage / Spill Containment | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| Structural / Foundations / Supports | Applicable | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |
| Utility Piping, Electrical Power, EHT, Communications, HVAC, F&G, Maintenance Access, Product Loading, Pipeline/Pigging | Not applicable per source | `26020-Package_Requirements.docx` H1 #48, Physical Interface Summary |

## Anticipated Artifacts (this deliverable)

- Construction work package
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-096-03.

## References

- `26020-Package_Requirements.docx` — package heading 48 "26020-03-PT-19-005 - Tanks, Sour Condensate" (located at `_Sources/26020-Package_Requirements.docx`).
- `DELIVERABLE_REGISTER.csv` (GATE-07_Final_Published_2026-05-24).
- `PACKAGE_REGISTER.csv` (GATE-07_Final_Published_2026-05-24), row PKG-096.
- `26020-Packages_Interfaces_4_export.xlsx` — interface details for row 92 — **location TBD** (not yet read).
- DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` — design basis context — **location TBD** (not yet read for this deliverable).
- API 650 — **location TBD** (not locally accessible).
- API 2000 — **location TBD** (not locally accessible).
- NACE (sour service compliance standards, e.g. MR0175 family) — **ASSUMPTION: likely applicable**; **location TBD**.
