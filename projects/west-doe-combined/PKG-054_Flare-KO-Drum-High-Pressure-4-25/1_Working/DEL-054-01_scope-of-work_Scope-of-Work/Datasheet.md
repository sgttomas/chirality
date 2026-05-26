# Datasheet — DEL-054-01 Scope of Work (PKG-054 Flare KO Drum (High Pressure) 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-054-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-054` — Flare KO Drum (High Pressure) 4-25 | `PACKAGE_REGISTER.csv` row 55 |
| Workbook Row | 55 | `PACKAGE_REGISTER.csv` (WorkbookRow=55) |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-17-002 (also reported as 26020-01-PT-17-002) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (basic scope) | Supply one HP flare knock-out drum and one HP flare KO drum transfer pump. | `SCOPE_LEDGER.csv` SOW-0076; `26020-Package_Requirements.docx` package heading 9 (Basic scope) |
| Major Equipment | HP flare KO drum `V-4100-1`; transfer pump `P-4100-1`; liquid handling to condensate slop tank; truck-out provision; related package connections. | `SCOPE_LEDGER.csv` SOW-0077; `26020-Package_Requirements.docx` package heading 9 (Major included equipment) |
| Scope Notes (process integration) | HP flare header ties into the cryogenic flare header downstream of the drum before the common HP/Cryo flare stack. Outdoor HP flare headers are electrically heat traced and insulated. | `SCOPE_LEDGER.csv` SOW-0078; `26020-Package_Requirements.docx` package heading 9 (Scope notes and open items) |
| Package Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration). | `PACKAGE_REGISTER.csv` PKG-054 ResponsibilityModel; ART-BBEC99B699 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | High-pressure flare relief liquid knock-out (sour service inferred from project basis) | `SCOPE_LEDGER.csv` SOW-0076/0077; OBJ-009 (sour-service safety/relief) — ASSUMPTION on sour-service classification at the package level |
| Operating regime | Continuous availability for relief events; transfer pump returns collected liquids to condensate slop tank | `SCOPE_LEDGER.csv` SOW-0077 — location TBD for design conditions (pressures, temperatures, flow rates) |
| Design pressures/temperatures | TBD (not in locally accessible source slices; resides in `26020-Package_Requirements.docx` package heading 9 detail text and/or budgetary go-by `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` — location TBD) | `PACKAGE_REGISTER.csv` SourceRefRaw |
| Sizing/Capacity | TBD | location TBD |
| Materials of construction | TBD | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | Mechanical equipment package supplied by Package Vendor; integrated into facility by EPC Integrator. | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Applicable interface types (package boundary integration) | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-054 rows; `PACKAGE_REGISTER.csv` InterfaceTypes |
| Heat tracing / insulation | Outdoor HP flare headers electrically heat traced and insulated (per SOW-0078). | `SCOPE_LEDGER.csv` SOW-0078 |
| Drains/containment | Liquid handling to condensate slop tank; truck-out provision. | `SCOPE_LEDGER.csv` SOW-0077 |

## Scope Items Covered

| Scope Item | Statement |
|---|---|
| `SOW-0075` | Carry workbook-defined vendor-responsible Mechanical package "Flare KO Drum (High Pressure) 4-25" as a distinct flat project package for WBS 01. |
| `SOW-0076` | Basic scope: Supply one HP flare knock-out drum and one HP flare KO drum transfer pump. |
| `SOW-0077` | Major included equipment: V-4100-1, P-4100-1, liquid handling to condensate slop tank, truck-out provision, related package connections. |
| `SOW-0078` | Scope notes/open items: HP flare header ties into cryogenic flare header downstream of drum before common HP/Cryo flare stack; outdoor HP flare headers EHT-traced and insulated. |

Source: `SCOPE_LEDGER.csv`.

## Objectives Supported

| Objective | Statement (short) | Source |
|---|---|---|
| `OBJ-001` | Provide the 04-25 Deepcut facility scope (sour gas processing). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-004` | Execute each electrical/mechanical equipment package with vendor and EPC responsibilities preserved. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-005` | Provide and integrate facility electrical power basis and interfaces to vendor packages. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-006` | Provide and integrate controls, instrumentation, and package control interfaces. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-007` | Provide and integrate shared utilities and ancillary support systems (including flare/blowdown/vent, drains). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-008` | Provide civil, structural, site, foundations, access, and construction-support scope. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-009` | Carry sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, regulatory, codes, and standards requirements. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-010` | Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and open-item closure. | `OBJECTIVE_REGISTER.csv` |

Objective association mode: PACKAGE_HEURISTIC (objectives are mapped at the deliverable-ID level in `OBJECTIVE_DELIVERABLE_MAP.csv` for this deliverable; this is therefore an explicit mapping, not a heuristic-only association).

## References

- `_CONTEXT.md`; `_REFERENCES.md`; `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 snapshot: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Source basis (per `PACKAGE_REGISTER.csv` SourceRefRaw): Workbook Packages row 55; `26020-Package_Requirements.docx` package heading 9; `Bid Docs/Budgetary/brief.md` (Word source basis); `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` (budgetary go-by); `DBM-Deepcut/4-25_Deepcut_DBM.md`. Deliverable-specific source slices were NOT copied into the deliverable folder during PREPARATION; clause-level extraction beyond the SCOPE_LEDGER entries marked `location TBD` above.
