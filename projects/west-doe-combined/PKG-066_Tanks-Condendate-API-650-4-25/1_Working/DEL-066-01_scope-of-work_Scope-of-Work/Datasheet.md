# Datasheet — DEL-066-01 Scope of Work (PKG-066 Tanks, Condendate (API 650) 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-066-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-066` — Tanks, Condendate (API 650) 4-25 | `PACKAGE_REGISTER.csv` row 89 |
| Workbook Row | 89 | `PACKAGE_REGISTER.csv` (WorkbookRow=89) |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-19-004 (also reported as 26020-01-PT-19-004) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (basic scope) | Supply condensate product storage tanks for 4-25 on-spec C5+ condensate product storage, using the 3-25 condensate tank package as the nearest analog. | `SCOPE_LEDGER.csv` SOW-0206; `26020-Package_Requirements.docx` package heading 21 (Basic scope) — location TBD for clause text |
| Major Equipment | Likely API 650 modified atmospheric condensate product storage tanks with blanket gas, PVRV/EPRV protection, VRU header connection, grounding/cathodic protection provisions, tank instrumentation, and standard tank appurtenances. Final 4-25 tank count, tags, capacity, and dimensions require confirmation; the Deepcut package roster indicates five condensate tanks, while the 3-25 analog uses four 3,800 bbl tanks. | `SCOPE_LEDGER.csv` SOW-0207; `26020-Package_Requirements.docx` package heading 21 (Major included equipment) — location TBD for clause text |
| Scope Notes (process integration) | Analog 3-25 condensate service is on-spec C5+ condensate product storage downstream of treating or bypass paths before condensate export. For 4-25, confirm the tank count, tags, capacity, inlet/outlet sources, whether mercaptan treating bypass/recycle paths apply, VRU/blanket gas requirements, and whether design conditions match the 3-25 3,800 bbl tank basis. | `SCOPE_LEDGER.csv` SOW-0208; `26020-Package_Requirements.docx` package heading 21 (Scope notes and open items) — location TBD for clause text |
| Package Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` PKG-066 ResponsibilityModel; ART-E0DD04C3E9 |
| Product Disposition (facility context) | Sales condensate, C5+ — delivered to the NorthRiver Midstream NEBC Connector via LACT (facility-level context from `DBM-Deepcut/4-25_Deepcut_DBM.md`). | `DBM-Deepcut/4-25_Deepcut_DBM.md` Process and Commercial Basis |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Atmospheric on-spec C5+ condensate product storage (sour-service handling context inferred from facility basis). | `SCOPE_LEDGER.csv` SOW-0206/0208; `OBJ-009`; ASSUMPTION on sour-service classification at the package level. |
| Operating regime | Continuous product storage between condensate stabilization and condensate export to the 03-25 Liquids Hub / NEBC Connector via LACT. | `DBM-Deepcut/4-25_Deepcut_DBM.md` Process and Commercial Basis |
| Tank count, tags, capacity | TBD — Deepcut roster indicates five condensate tanks; 3-25 analog uses four 3,800 bbl tanks. Final 4-25 values require confirmation. | `SCOPE_LEDGER.csv` SOW-0207/0208 — location TBD for design selection |
| Design pressures/temperatures | TBD (atmospheric per API 650 implied; specific design values not in locally accessible source slices; reside in `26020-Package_Requirements.docx` package heading 21 detail text and/or analog `26020-03-PT-RFQ-19-006 - Conde Tanks.docx` — location TBD) | `PACKAGE_REGISTER.csv` SourceRefRaw |
| VRU / blanket gas | Blanket gas and VRU header connection identified as likely equipment; specific configuration TBD pending confirmation. | `SCOPE_LEDGER.csv` SOW-0207/0208 — location TBD |
| Materials of construction | TBD | location TBD |
| Spacing constraints (facility) | Atmospheric condensate tanks: ≥30.48 m (100 ft) from pressurized bullets (API 2510); 2.35 m (7.72 ft) between atmospheric tanks (NFPA 30 Tbl 22.4.2.1); ≥50 m (164 ft) from flare (OGAOM Sec. 9.6.15); ≥80 m (262.5 ft) from public road (OGAOM Sec. 9.6.15, DPR 48). | `DBM-Deepcut/4-25_Deepcut_DBM.md` Site / Spacing section |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | Mechanical equipment package supplied by Package Vendor; integrated into facility by EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Applicable interface types (package boundary integration) | Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-066 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| Cathodic protection / grounding | Grounding/cathodic protection provisions identified as part of tank package scope. | `SCOPE_LEDGER.csv` SOW-0207 |
| Drains/containment | Atmospheric tank containment, grading, and site drainage are package-boundary interfaces (no in-tank slop routing stated in accessible slices). | `INTERFACE_REGISTER.csv` PKG-066 rows |

## Scope Items Covered

| Scope Item | Statement |
|---|---|
| `SOW-0205` | Carry workbook-defined vendor-responsible Mechanical package "Tanks, Condendate (API 650) 4-25" as a distinct flat project package for WBS 01; Package Vendor owns engineering/design/equipment, EPC Integrator owns facility integration. |
| `SOW-0206` | Basic scope: Supply condensate product storage tanks for 4-25 on-spec C5+ condensate product storage, using the 3-25 condensate tank package as the nearest analog. |
| `SOW-0207` | Major included equipment: API 650 modified atmospheric condensate product storage tanks with blanket gas, PVRV/EPRV protection, VRU header connection, grounding/cathodic protection provisions, tank instrumentation, and standard tank appurtenances. Final count/tags/capacity TBD. |
| `SOW-0208` | Scope notes and open items: confirm tank count, tags, capacity, inlet/outlet sources, mercaptan treating bypass/recycle applicability, VRU/blanket gas requirements, and design-condition match to the 3-25 3,800 bbl tank basis. |

Source: `SCOPE_LEDGER.csv`.

## Objectives Supported

| Objective | Statement (short) | Source |
|---|---|---|
| `OBJ-001` | Provide the 04-25 Deepcut facility scope (sour gas processing through inlet separation, stabilization, treating, dehydration, cryogenic recovery, product handling, acid-gas, and supporting systems). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-003` | Preserve commercial stream disposition, metering accountability, and facility boundary interfaces for sales gas, NGL, condensate, acid gas, produced water, LACT/tie-in limits, truck loading, and 03-25/04-25 exchanges. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-004` | Execute each electrical/mechanical equipment package with vendor and EPC responsibilities preserved. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-005` | Provide and integrate facility electrical power basis and interfaces to vendor packages (grounding, lighting, cathodic protection). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-006` | Provide and integrate controls, instrumentation, package control interfaces, fire/gas detection, and shutdown interfaces. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-007` | Provide and integrate shared utilities and ancillary support systems (flare/blowdown/vent, drains, containment, blanket gas, VRU). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-008` | Provide civil, structural, site, foundations, grading, containment, and construction-support scope. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-009` | Carry sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, regulatory, codes, and standards requirements. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-010` | Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and open-item closure. | `OBJECTIVE_REGISTER.csv` |

Objective association mode: PACKAGE_HEURISTIC (objectives are mapped at the deliverable-ID level in `OBJECTIVE_DELIVERABLE_MAP.csv` for this deliverable; therefore an explicit mapping rather than heuristic-only).

## References

- `_CONTEXT.md`; `_REFERENCES.md`; `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 snapshot: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Source basis (per `PACKAGE_REGISTER.csv` SourceRefRaw): Workbook Packages row 89; `26020-Package_Requirements.docx` package heading 21; analog basis `26020-03-PT-19-006_Tanks_Cond/Bid Docs/Budgetary/26020-03-PT-RFQ-19-006 - Conde Tanks.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md`. No direct package-folder brief.md, DOCX, or PDF scope source found for 4-25. Deliverable-specific source slices were NOT copied into the deliverable folder during PREPARATION; clause-level extraction beyond the SCOPE_LEDGER entries marked `location TBD` above.
