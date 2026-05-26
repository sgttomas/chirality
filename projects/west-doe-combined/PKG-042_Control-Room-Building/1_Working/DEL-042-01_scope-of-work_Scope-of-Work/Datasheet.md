# Datasheet: DEL-042-01_scope-of-work — Scope of Work (PKG-042 Control Room Building)

Descriptive datasheet for the EPC Integrator-authored Scope of Work for the vendor-owned Electrical package "Control Room Building" (PKG-042, Workbook row 44, WBS 03).

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-042-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-042` — Control Room Building | `PACKAGE_REGISTER.csv` |
| Workbook Package ID | 42 | `PACKAGE_REGISTER.csv` |
| Workbook Row | 44 | `PACKAGE_REGISTER.csv` |
| WBS | 03 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-03-39-010 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Covered Scope Item | `SOW-0043` (IN) | `SCOPE_LEDGER.csv` |
| Supported Objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `DELIVERABLE_REGISTER.csv` (ASSUMPTION — best-effort PACKAGE_HEURISTIC mapping) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Vendor-owned Electrical package for "Control Room Building" under WBS 03 | `PACKAGE_REGISTER.csv` Description |
| Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` ResponsibilityModel; ART-93D323D241 |
| Exclusions | TBD — no package-specific exclusions stated in source materials. | `PACKAGE_REGISTER.csv` Exclusions |
| Anticipated Artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source basis | Workbook Packages row 44; DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | `PACKAGE_REGISTER.csv` SourceReference (ASSUMPTION on DBM relevance — location TBD; the DBM slice for the Control Room Building has not been opened in this pass) |
| Decomposition gate basis | GATE-07 Final Published 2026-05-24 (PROJECT_DECOMP) | `_CONTEXT.md`; `_REFERENCES.md` |
| Lifecycle gate | Gate 5 (EPC anchor deliverable) | `DELIVERABLE_REGISTER.csv` Notes |

## Construction (Tagged Equipment and Identity)

The workbook package row for PKG-042 names the package as "Control Room Building" with tracking number 26020-03-39-010 under WBS 03; no detailed major-equipment list text is carried in the accessible GATE-07 registers. Detailed tagged-equipment text is `TBD — location TBD` until the workbook row 44 detailed equipment cells or the relevant DBM section are opened.

| Item | Value | Source |
|---|---|---|
| Package Name | Control Room Building | `PACKAGE_REGISTER.csv` |
| Tracking Number | 26020-03-39-010 | `PACKAGE_REGISTER.csv` |
| WBS | 03 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv` |
| Detailed Major Equipment | TBD — extract from Workbook row 44 equipment text (location TBD) | ASSUMPTION |

## Interface Conditions (Workbook X-Column Facts)

The following interface types are flagged YES for PKG-042 in `INTERFACE_REGISTER.csv` and frame the EPC integration boundary the Scope of Work must describe:

| InterfaceID | Interface Type | Source |
|---|---|---|
| IFC-BE3458FDB4 | Utility Piping | `INTERFACE_REGISTER.csv` |
| IFC-24C34638A3 | Drain / Containment | `INTERFACE_REGISTER.csv` |
| IFC-DC78111478 | Electrical Power | `INTERFACE_REGISTER.csv` |
| IFC-DA72344D63 | Grounding / Bonding | `INTERFACE_REGISTER.csv` |
| IFC-0DCC239AB3 | Area / Exterior Lighting | `INTERFACE_REGISTER.csv` |
| IFC-F360E6EC35 | I&C / Control Cabling | `INTERFACE_REGISTER.csv` |
| IFC-66A84D947D | Communications / Network | `INTERFACE_REGISTER.csv` |
| IFC-681FD52C78 | Building HVAC / Services | `INTERFACE_REGISTER.csv` |
| IFC-E549CF5FDE | Fire & Gas / Safety Systems | `INTERFACE_REGISTER.csv` |
| IFC-732E8E4246 | Grading / Site Drainage / Spill Containment | `INTERFACE_REGISTER.csv` |
| (additional) | Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` (applicable interface types list) |

Note: detailed interface fact text (battery limits, tie-in points) is carried as evidence on the **Package Datasheet** deliverable (DEL-042-02), not on this Scope of Work. The Scope of Work references the interfaces by type only.

## References

- `_REFERENCES.md` (authoritative reference index for this deliverable)
- `PACKAGE_REGISTER.csv` row PKG-042 (GATE-07)
- `DELIVERABLE_REGISTER.csv` row `DEL-042-01_scope-of-work` (GATE-07)
- `SCOPE_LEDGER.csv` row `SOW-0043` (GATE-07)
- `INTERFACE_REGISTER.csv` rows for `PKG-042` (GATE-07)
- `ARTIFACT_REGISTER.csv` rows for `DEL-042-01_scope-of-work` (GATE-07)
- Workbook Packages row 44 (location TBD — source slice not opened in this pass)
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (ASSUMPTION — relevance per PACKAGE_REGISTER source reference; specific section TBD)
