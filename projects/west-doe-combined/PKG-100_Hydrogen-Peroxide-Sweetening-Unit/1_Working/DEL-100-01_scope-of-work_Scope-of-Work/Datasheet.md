# Datasheet — DEL-100-01 Scope of Work (PKG-100 Hydrogen Peroxide Sweetening Unit)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-100-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-100` — Hydrogen Peroxide Sweetening Unit | `PACKAGE_REGISTER.csv` (WorkbookID=100, WorkbookRow=63) |
| Workbook Row | 63 | `PACKAGE_REGISTER.csv` |
| WBS | 03 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-03-27-001 (also reported as 26020-03-PT-27-001) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function (basic scope) | Supply 1 sour-water hydrogen peroxide treatment package consisting of: Hydrogen Peroxide Pumps (chemical injection pumps); Hydrogen Peroxide Reactors; Static Mixer. Sour water is sent to the static mixer and then to the Hydrogen Peroxide Reactors for treatment. Hydrogen peroxide is pumped in from the hydrogen peroxide tank by the hydrogen peroxide pumps; treated water is sent to produced water storage tanks (see attached PFD). | `SCOPE_LEDGER.csv` SOW-0108; `26020-Package_Requirements.docx` package heading 52 (Basic scope) |
| Major Equipment | 400 BBL Hydrogen Peroxide Storage Tank; Hydrogen Peroxide Pumps – chemical injection pumps (Vendor to design); Static Mixer (Vendor to design); Hydrogen Peroxide Reactors (Vendor to design); additional equipment shown in PFD; self-framing building to be erected at site. | `SCOPE_LEDGER.csv` SOW-0109; `26020-Package_Requirements.docx` package heading 52 (Major included equipment) |
| Scope Notes (process integration) | By others: interconnecting piping, DCS integration, foundations, electrical supply to MCC. Hydrogen peroxide supplied from onsite tanks. | `SCOPE_LEDGER.csv` SOW-0110; `26020-Package_Requirements.docx` package heading 52 (Scope notes and open items) |
| Package Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration). | `PACKAGE_REGISTER.csv` PKG-100 ResponsibilityModel; `ARTIFACT_REGISTER.csv` ART-5BA6AFE0FD |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour-water treatment via hydrogen peroxide injection/reaction (oxidative sweetening of sour water before transfer to produced water storage). | `SCOPE_LEDGER.csv` SOW-0108 |
| Capacity / Design throughput | 24,154 BBL/D (treatment package capacity); Tank capacity 400 BBL; Pump capacity TBC (Vendor to design). | `SCOPE_LEDGER.csv` SOW-0110 |
| Sour-water operating temperature | 9 °C | `SCOPE_LEDGER.csv` SOW-0110 |
| Sour-water operating pressure | 340.54 kPag | `SCOPE_LEDGER.csv` SOW-0110 |
| Sour-water operating flow rate | 160 m³/h (24,154 BBL/D) | `SCOPE_LEDGER.csv` SOW-0110 |
| Ambient temperature (design) | −40 °C min., +35 °C max. | `SCOPE_LEDGER.csv` SOW-0110 |
| Other design conditions (P, T, sizing) | TBC (Vendor to design); not in locally accessible source slices beyond what is captured above. | location TBD — `26020-Package_Requirements.docx` package heading 52 detail text and/or `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` |
| Materials of construction | TBD | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | Mechanical equipment package supplied by Package Vendor; integrated into facility by EPC Integrator. Includes self-framing building to be erected at site. | `PACKAGE_REGISTER.csv` ResponsibilityModel; `SCOPE_LEDGER.csv` SOW-0109 |
| Applicable interface types (package boundary integration) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` PKG-100 rows (13 entries); `PACKAGE_REGISTER.csv` InterfaceTypes |
| Drivers / Electrical | All pumps driven by 575 V / 3 PH / 60 Hz motors; starting method DOL or VFD; local control (H-O-A or On-Off switch); electric motors fed from 600 V MCC. | `SCOPE_LEDGER.csv` SOW-0110 |
| EPC-scope exclusions from vendor package | Interconnecting piping, DCS integration, foundations, and electrical supply to the MCC are "by others" (i.e., EPC Integrator scope or other facility deliverables). | `SCOPE_LEDGER.csv` SOW-0110 |
| Hydrogen peroxide supply | Supplied from onsite tanks (400 BBL Hydrogen Peroxide Storage Tank within package). | `SCOPE_LEDGER.csv` SOW-0109, SOW-0110 |

## Scope Items Covered

| Scope Item | Statement |
|---|---|
| `SOW-0107` | Carry workbook-defined vendor-responsible Mechanical package "Hydrogen Peroxide Sweetening Unit" as a distinct flat project package for WBS 03; Package Vendor owns engineering/design/equipment, EPC Integrator owns facility integration. |
| `SOW-0108` | Basic scope: Supply 1 sour-water hydrogen peroxide treatment package (Hydrogen Peroxide Pumps; Hydrogen Peroxide Reactors; Static Mixer); process function per SOW-0108. |
| `SOW-0109` | Major included equipment: 400 BBL Hydrogen Peroxide Storage Tank; Hydrogen Peroxide Pumps (Vendor to design); Static Mixer (Vendor to design); Hydrogen Peroxide Reactors (Vendor to design); additional equipment per PFD; self-framing building at site. |
| `SOW-0110` | Scope notes/open items: by-others list; capacity 24,154 BBL/D; tank 400 BBL; pump capacity TBC; drivers 575 V/3PH/60Hz, DOL or VFD, fed from 600 V MCC; sour-water T=9 °C, P=340.54 kPag, Q=160 m³/h; ambient −40 to +35 °C; H₂O₂ from onsite tanks. |

Source: `SCOPE_LEDGER.csv`.

## Objectives Supported

| Objective | Statement (short) | Source |
|---|---|---|
| `OBJ-002` | (Per `OBJECTIVE_REGISTER.csv`) — supported by PKG-100 per `OBJECTIVE_DELIVERABLE_MAP.csv`. | `OBJECTIVE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| `OBJ-004` | Execute each electrical/mechanical equipment package with vendor and EPC responsibilities preserved. | `OBJECTIVE_REGISTER.csv` (per project-wide objective set) |
| `OBJ-005` | Provide and integrate facility electrical power basis and interfaces to vendor packages. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-006` | Provide and integrate controls, instrumentation, and package control interfaces. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-007` | Provide and integrate shared utilities and ancillary support systems (flare/blowdown/vent, drains, etc.). | `OBJECTIVE_REGISTER.csv` |
| `OBJ-008` | Provide civil, structural, site, foundations, access, and construction-support scope. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-009` | Carry sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, regulatory, codes, and standards requirements. | `OBJECTIVE_REGISTER.csv` |
| `OBJ-010` | Maintain operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and open-item closure. | `OBJECTIVE_REGISTER.csv` |

Objective association mode: PACKAGE_HEURISTIC (per brief). The objectives above are explicitly listed at the deliverable-ID level in `DELIVERABLE_REGISTER.csv` (DEL-100-01 row, SupportsObjectives column) and corroborated for `PKG-100` by `OBJECTIVE_SCOPE_MAP.csv`; this association is therefore explicit, not heuristic-only. Short statements for OBJ-002 are ASSUMPTION pending direct extraction of the `OBJECTIVE_REGISTER.csv` row text.

## References

- `_CONTEXT.md`; `_REFERENCES.md`; `_DEPENDENCIES.md` (deliverable-local).
- GATE-07 snapshot: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_SCOPE_MAP.csv`.
- Source basis (per `PACKAGE_REGISTER.csv` SourceRefRaw): Workbook Packages row 63; `26020-Package_Requirements.docx` package heading 52; `Bid Docs/Budgetary/26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` (budgetary go-by); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. Deliverable-specific source slices were NOT copied into the deliverable folder during PREPARATION; clause-level extraction beyond the `SCOPE_LEDGER.csv` entries marked `location TBD` above.
