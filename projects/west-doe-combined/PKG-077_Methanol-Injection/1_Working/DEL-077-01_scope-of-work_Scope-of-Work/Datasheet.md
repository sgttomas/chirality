# Datasheet — DEL-077-01_scope-of-work (PKG-077 Methanol Injection)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-077-01_scope-of-work` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-077-01_scope-of-work` |
| Name | Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-077` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-077` |
| ParentWorkbookID | 77 | `PACKAGE_REGISTER.csv` row `PKG-077` |
| Workbook Row | 72 | `PACKAGE_REGISTER.csv` (`SourceRef`: Workbook Packages row 72) |
| PackageName | Methanol Injection | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Type | EPC Scope of Work | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| CoA / Tracking Number | 26020-01-29-002 | `PACKAGE_REGISTER.csv` (CoA tracking number) |
| Covers Scope Items | `SOW-0143` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` row `SOW-0143` |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Methanol Injection — vendor-owned Mechanical package on WBS 01 of the 04-25 Deepcut facility | `PACKAGE_REGISTER.csv` row `PKG-077`; `OBJ-001` (`OBJECTIVE_REGISTER.csv`) |
| Procurement model | Vendor-owned package (Package Vendor engineering/design/equipment) integrated by EPC Integrator | `PACKAGE_REGISTER.csv` row `PKG-077` (ResponsibilityNote); `OBJ-004` |
| Tagged major equipment | TBD — workbook major-equipment text not extracted into the snapshot registers | `PACKAGE_REGISTER.csv` references workbook row 72 detailed major-equipment text; not surfaced locally |
| Anticipated artifact set | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record | `DELIVERABLE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` rows ART-319578C39E, ART-F30A41723D, ART-7A3F23A6BA, ART-1230D957BE |
| Gate 6 disposition note | Methanol Injection scope is included with the Cryogenic Unit package scope | `PACKAGE_REGISTER.csv` row `PKG-077` Notes |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service environment | Sour raw gas inlet/stabilization facility (04-25 Deepcut) — ASSUMPTION based on parent project objective | `OBJ-001` (`OBJECTIVE_REGISTER.csv`); facility-level inference |
| Sour service requirement | Carry sour-service safety per OBJ-009 | `OBJ-009` (`OBJECTIVE_REGISTER.csv`) |
| Operability requirement | Maintain operability per OBJ-010 | `OBJ-010` (`OBJECTIVE_REGISTER.csv`) |
| Design conditions (pressure, temperature, fluid composition) | TBD — not present in locally accessible registers | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Vendor-supplied package scope | Engineering, design, vendor documentation, and the physical equipment package | `PACKAGE_REGISTER.csv` ResponsibilityNote |
| EPC Integrator scope | Interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` ResponsibilityNote |
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` rows for `PKG-077` (13 IFC rows) |
| Package boundary exclusions | TBD — no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` row `PKG-077` Exclusions field (TBD) |

## References

- `PACKAGE_REGISTER.csv` row `PKG-077` (Workbook Packages row 72)
- `DELIVERABLE_REGISTER.csv` row `DEL-077-01_scope-of-work`
- `SCOPE_LEDGER.csv` row `SOW-0143`
- `ARTIFACT_REGISTER.csv` rows ART-319578C39E, ART-F30A41723D, ART-7A3F23A6BA, ART-1230D957BE
- `INTERFACE_REGISTER.csv` rows for PKG-077 (13)
- `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010
- Snapshot root: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
