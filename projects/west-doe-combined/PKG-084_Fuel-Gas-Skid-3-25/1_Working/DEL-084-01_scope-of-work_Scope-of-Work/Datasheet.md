# Datasheet — DEL-084-01 Scope of Work (PKG-084 Fuel Gas Skid 3-25)

Pass directive: P1_P2 (Pass 1 + Pass 2). Source-grounded per `_REFERENCES.md` authority hierarchy.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-084-01_scope-of-work` | `_CONTEXT.md` |
| Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-084` | `_CONTEXT.md` |
| Package Name | Fuel Gas Skid 3-25 | `_CONTEXT.md` |
| Workbook Row | Packages row 60 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Source Heading | `26020-Package_Requirements.docx` package heading 37 (`26020-02-PT-23-001 - Fuel Gas Skid`) | `_REFERENCES.md`; 26020-Package_Requirements.docx |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Location / Status | 3-25 West Doe Compressor Station; vetted package scope basis | 26020-Package_Requirements.docx, `26020-02-PT-23-001` Location/Status |
| Source Basis Document | `Bid Docs/Budgetary/26020-02-PT-RFQ-23-001_FG_Skid_1.docx` | 26020-Package_Requirements.docx, `26020-02-PT-23-001` Source Basis |
| Covers Scope Items | SOW-0095; SOW-0096; SOW-0097; SOW-0098 | `_CONTEXT.md`; OBJECTIVE_SCOPE_MAP.csv |
| Supports Objectives (ASSUMPTION — package-grouping heuristic) | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | DELIVERABLE_REGISTER.csv (PACKAGE_HEURISTIC) |

## Attributes — Package Identity

| Attribute | Value | Source |
|---|---|---|
| Tagged equipment item | `26020-02-PT-23-001 - Fuel Gas Skid` | 26020-Package_Requirements.docx package heading 37 |
| Skid count | 1 skid-mounted Low Pressure Fuel Gas Package | 26020-Package_Requirements.docx, Basic Scope |
| Major equipment item 1 | 1 LP fuel gas heater (capacity TBD; SCR control at 600 V; skin-temperature thermocouple override on heater) | 26020-Package_Requirements.docx, Major Included Equipment |
| Major equipment item 2 | 1 LP fuel gas scrubber (sized using K = 0.35 imperial maximum plus de-ration factor for operating pressure; vendor to design) | 26020-Package_Requirements.docx, Major Included Equipment |
| Skid type | Mounting skid for the system equipment | 26020-Package_Requirements.docx, Major Included Equipment |
| Process function | Serves the low-pressure fuel gas system for the West Doe Deep Cut Facility | 26020-Package_Requirements.docx, Basic Scope |

## Conditions — Design and Operating Basis

| Parameter | Value | Source |
|---|---|---|
| Design flow required | > 1.5 MMSCFD (42.5 e3m3/day) | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Final flow | TBD | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Heated outlet temperature | 95 °F (35 °C) | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Operating pressure | 150 psig | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Design pressure | 150 psig | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Design temperature | −40 °C to 35 °C | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Ambient temperature | −19 °C to 22.2 °C | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| MAWP | TBD | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Heating value | 1040 BTU/SCF | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| Heater driver | SCR control panels, 600 V, located in electrical building | 26020-Package_Requirements.docx, Scope Notes / Open Items |
| LP fuel-gas system facility context (normal total) | 1.382 MMSCFD (39.13 e3m3/d); design > 1.5 MMSCFD (42.5 e3m3/d) — facility-wide LP fuel-gas basis | `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas" |
| LP fuel-gas users (facility) | TEG stripping, caustic treating overhead dilution, maintenance purge, drive gas, blanket gas | `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas" |
| Related downstream LP scrubber (facility-side, not the same as skid scrubber) | `V-3210-2` LP fuel-gas scrubber, K = 0.35, downstream of heater, liquids to slop tank `TK-9130-2` | `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas" |
| Facility utility-sharing context | Fuel gas and instrument air shared with 04-25 Deep Cut Gas Plant; fuel-gas building associated with 04-25 | `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas"; §Utilities |
| Emergency buyback fuel gas | CONFLICT — W242510 indicates not required; Process_DBM_fixed includes it in 04-25 utility package. Human ruling required. | `3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas" |

## Construction — Package Composition

| Element | Value | Source |
|---|---|---|
| Skid | Mounting skid supplied with package | 26020-Package_Requirements.docx, Major Included Equipment |
| Heater | Fuel gas heater, SCR-controlled, with skin-temperature thermocouple override; capacity TBD | 26020-Package_Requirements.docx, Major Included Equipment |
| Scrubber | LP fuel gas scrubber, sized per K = 0.35 plus pressure de-ration; vendor design | 26020-Package_Requirements.docx, Major Included Equipment |
| By Others (excluded from package) | Shipping packages to site; installation; tie-in piping; electrical tie-in | 26020-Package_Requirements.docx, Scope Notes / Open Items |

## Physical Interface Summary (from package heading 37 interface table)

| Interface Type | Applicability | Source |
|---|---|---|
| Process Piping | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Utility Piping | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Relief / Flare / Vent | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Drain / Containment | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Electrical Power | No (heater control via SCR panels in electrical building — ASSUMPTION: vendor scope ends at panel; tie-in by others) | 26020-Package_Requirements.docx, Physical Interface Summary; Scope Notes |
| Area / Exterior Lighting | Yes (interface source: `26020-Packages_Interfaces.3.xlsx` column M row 60) | 26020-Package_Requirements.docx, Physical Interface Summary |
| EHT | No | 26020-Package_Requirements.docx, Physical Interface Summary |
| Grounding / Bonding | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Cathodic Protection | No | 26020-Package_Requirements.docx, Physical Interface Summary |
| I&C / Control Cabling | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Communications / Network | No | 26020-Package_Requirements.docx, Physical Interface Summary |
| Building HVAC / Services | No | 26020-Package_Requirements.docx, Physical Interface Summary |
| Fire & Gas / Safety Systems | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Maintenance Access | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Grading / Site Drainage / Spill Containment | No | 26020-Package_Requirements.docx, Physical Interface Summary |
| Structural / Foundations / Supports | Yes | 26020-Package_Requirements.docx, Physical Interface Summary |
| Product Loading | No | 26020-Package_Requirements.docx, Physical Interface Summary |
| Pipeline / Pigging | No | 26020-Package_Requirements.docx, Physical Interface Summary |

## References

- `_CONTEXT.md` (deliverable identity)
- `_REFERENCES.md` (authoritative source pointer table)
- `26020-Package_Requirements.docx`, package heading 37: `26020-02-PT-23-001 - Fuel Gas Skid` (Location/Status, Source Basis, Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"## Fuel Gas", §Utilities (facility LP fuel-gas system context)
- `GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row 324 — DEL-084-01)
- `GATE-07_Final_Published_2026-05-24/OBJECTIVE_SCOPE_MAP.csv` (SOW-0095..0098 / PKG-084 rows)
- Source vendor RFQ basis: `Bid Docs/Budgetary/26020-02-PT-RFQ-23-001_FG_Skid_1.docx` — `location TBD` (not locally accessible)
- `26020-Packages_Interfaces_4_export.xlsx` — referenced by source as `26020-Packages_Interfaces.3.xlsx` row 60 (`location TBD` for the exact field set)
