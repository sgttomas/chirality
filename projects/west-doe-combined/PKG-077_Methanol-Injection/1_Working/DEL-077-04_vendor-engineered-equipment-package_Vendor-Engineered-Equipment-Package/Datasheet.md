# Datasheet — DEL-077-04 Vendor Engineered Equipment Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-077-04_vendor-engineered-equipment-package` | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row 399 |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` Identity; `DELIVERABLE_REGISTER.csv` row 399 |
| ParentPackageID | `PKG-077` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 72 |
| ParentWorkbookID | 77 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 72 |
| PackageName | Methanol Injection | `PACKAGE_REGISTER.csv` row 72 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row 72 |
| CoA Tracking Number | 26020-01-29-002 | `PACKAGE_REGISTER.csv` row 72 |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 72 |
| Type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 399 |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 399 |
| Covers Scope Items | `SOW-0143` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 399 |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 399 (ASSUMPTION: package-grouping heuristic — `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Production Unit Class | Vendor Package Production Unit | `DELIVERABLE_REGISTER.csv` row 399 |
| Authoring Entity | Package Vendor | `DELIVERABLE_REGISTER.csv` row 399; `PACKAGE_REGISTER.csv` row 72 |
| Review Entity | EPC Integrator (integration review) | `DELIVERABLE_REGISTER.csv` row 399 |
| Engineering Anchor | EPC Scope of Work (DEL-077-01) | `DELIVERABLE_REGISTER.csv` row 396 / 399 (Notes) |
| Design Basis Anchor | EPC Package Datasheet (DEL-077-02) | `DELIVERABLE_REGISTER.csv` row 397 / 399 (Notes) |
| Vendor Ownership Domains | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` row 72 |
| EPC Ownership Domains | Integration into the functional process facility; interfaces; tie-ins; constructability; procurement/construction coordination; facility-level integration | `PACKAGE_REGISTER.csv` row 72 |
| Gate 6 Disposition | Methanol Injection scope is included with the Cryogenic Unit package scope | `PACKAGE_REGISTER.csv` row 72 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Process Service | Methanol Injection (TBD: process role, flowrates, concentrations) | `PACKAGE_REGISTER.csv` row 72 (name only); deeper process conditions location TBD |
| Battery Limits | TBD — to be carried from EPC Package Datasheet (DEL-077-02) | `DELIVERABLE_REGISTER.csv` row 397 (Vendor handoff evidence) |
| Design Pressure / Temperature | TBD | location TBD (source slice not locally extracted) |
| Area Classification | TBD | location TBD |
| Site / Environmental Conditions | TBD | location TBD |
| Applicable Interface Types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row 72; `INTERFACE_REGISTER.csv` rows 574-586 |

## Construction

| Item | Value | Source |
|---|---|---|
| Physical Form | Vendor engineered physical equipment package | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row 399 |
| Major Equipment Inventory | TBD — derived from EPC Scope of Work tagged equipment list (DEL-077-01) | `DELIVERABLE_REGISTER.csv` row 396 (Tagged equipment and package identity list) |
| Fabrication / Supply Scope | Vendor-owned: engineering, design, fabrication/supply, physical equipment package | `_CONTEXT.md` Scope; `PACKAGE_REGISTER.csv` row 72 |
| Vendor Documentation Set | Vendor package design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts |
| Materials of Construction | TBD | location TBD |
| Skid / Module Definition | TBD | location TBD (ASSUMPTION: typical methanol injection packages are skid-mounted) |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `DELIVERABLE_REGISTER.csv` (Gate 7 snapshot) — row 399 (DEL-077-04), row 396 (DEL-077-01 SoW), row 397 (DEL-077-02 Package Datasheet)
- `PACKAGE_REGISTER.csv` (Gate 7 snapshot) — row 72 (PKG-077 Methanol Injection)
- `ARTIFACT_REGISTER.csv` (Gate 7 snapshot) — rows 4267-4277+ (PKG-077 artifacts)
- `INTERFACE_REGISTER.csv` (Gate 7 snapshot) — rows 574-586 (PKG-077 interfaces)
- Workbook Packages row 72 — source slice referenced by decomposition; not locally extracted (location TBD for technical detail)
