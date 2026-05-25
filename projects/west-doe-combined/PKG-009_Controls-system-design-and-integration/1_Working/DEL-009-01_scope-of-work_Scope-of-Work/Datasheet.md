# Datasheet: DEL-009-01_scope-of-work - Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-009-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-009 - Controls system design and integration |
| Workbook ID / row | 9 / 10 |
| WBS | 02 |
| CoA tracking number | 26020-01-32-001 |
| Discipline | Controls |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Covers scope item | SOW-0009 |
| Source basis | Gate 7 final published PROJECT_DECOMP snapshot; Workbook Packages row 10 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package name | Controls system design and integration | DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv |
| Scope description | Workbook-defined Controls package under WBS 02 with recorded physical interfaces. | PACKAGE_REGISTER.csv |
| Mandatory deliverable role | EPC Integrator deliverable for the full package scope, including tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative. | DELIVERABLE_REGISTER.csv |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | DELIVERABLE_REGISTER.csv; ARTIFACT_REGISTER.csv |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. | PACKAGE_REGISTER.csv |
| Package exclusions | TBD; no package-specific exclusions stated in source materials. | PACKAGE_REGISTER.csv |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Included source row | Workbook Packages row 10. | SCOPE_LEDGER.csv; PACKAGE_REGISTER.csv |
| Objective support | OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, OBJ-010. | OBJECTIVE_DELIVERABLE_MAP.csv |
| Declared upstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |
| Declared downstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |
| Blocker mode | DECLARED critical dependencies; default maturity threshold INITIALIZED. | _DEPENDENCIES.md; _COORDINATION.md |
| Raw-source detail limits | No deliverable-specific source slices were copied during PREPARATION; detailed design values not present in the deliverable-local context remain TBD. | _REFERENCES.md |

## Construction

The scope-of-work package should be constructed as an EPC Integrator-authored control document that records:

- Package scope, function, tagged-equipment basis, source rows, WBS, discipline, and boundaries.
- Tagged equipment and package identity list, including package name, workbook ID, CoA tracking number, WBS, and detailed major-equipment text where source-supported.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.

ASSUMPTION: Because the Gate 7 snapshot carries this as an EPC Scope of Work and no separate template is provided in the deliverable folder, the scope-of-work document should be organized as a controlled narrative plus tables for identity, boundaries, artifacts, responsibilities, and source references.

## References

- `_CONTEXT.md` for deliverable identity and assigned scope.
- `_DEPENDENCIES.md` for declared dependency state.
- `_REFERENCES.md` for accepted upstream reference pointers.
- Gate 7 final published PROJECT_DECOMP snapshot:
  - `DELIVERABLE_REGISTER.csv`
  - `PACKAGE_REGISTER.csv`
  - `SCOPE_LEDGER.csv`
  - `ARTIFACT_REGISTER.csv`
  - `INTERFACE_REGISTER.csv`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
  - `OBJECTIVE_REGISTER.csv`
