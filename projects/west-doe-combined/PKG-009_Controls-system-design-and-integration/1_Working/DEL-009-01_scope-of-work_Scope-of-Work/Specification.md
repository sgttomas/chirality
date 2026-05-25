# Specification: DEL-009-01_scope-of-work - Scope of Work

## Scope

This specification defines the required content and verification basis for the EPC Scope of Work deliverable for PKG-009, Controls system design and integration, WBS 02.

The deliverable covers SOW-0009 and must describe the full package scope, tagged equipment and package identity, package function, source basis, boundaries, whole-facility integration narrative, and responsibility assignment record.

Exclusions are TBD because the accepted Gate 7 package register states that no package-specific exclusions are stated in source materials.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-001 | The Scope of Work must identify DEL-009-01_scope-of-work, PKG-009, workbook ID 9, workbook row 10, WBS 02, CoA tracking number 26020-01-32-001, discipline Controls, and responsible party EPC Integrator. | _CONTEXT.md; DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv |
| REQ-002 | The Scope of Work must carry SOW-0009 as the covered scope item for the workbook-defined Controls package under WBS 02. | _CONTEXT.md; SCOPE_LEDGER.csv |
| REQ-003 | The Scope of Work must include the anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | DELIVERABLE_REGISTER.csv; ARTIFACT_REGISTER.csv |
| REQ-004 | The Scope of Work must state that responsibility is source-dependent where applicable and must not infer a separate vendor-package ownership model from the current sources. | PACKAGE_REGISTER.csv; ARTIFACT_REGISTER.csv |
| REQ-005 | The Scope of Work must preserve the package's applicable interface types as context: Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, and Fire & Gas / Safety Systems. | PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv |
| REQ-006 | The Scope of Work must reference the supported objectives OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, and OBJ-010 as directional context and not as unstated design values. | OBJECTIVE_DELIVERABLE_MAP.csv; OBJECTIVE_REGISTER.csv |
| REQ-007 | The Scope of Work must keep design details, equipment counts, performance values, code clauses, and package-specific exclusions as TBD unless they are supported by the accepted snapshot or an accessible source slice. | _REFERENCES.md; PACKAGE_REGISTER.csv |
| REQ-008 | The Scope of Work must include a source-basis section identifying the Gate 7 final published PROJECT_DECOMP snapshot and Workbook Packages row 10. | _REFERENCES.md; DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv |

## Standards

| Standard / authority | Application | Status |
|---|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Accepted decomposition truth for package, deliverable, artifact, interface, objective, and scope mapping. | Available locally |
| Workbook Packages row 10 | Source row for the PKG-009 package basis. | Available through accepted snapshot registers; raw workbook slice not copied into deliverable folder |
| DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md | Source reference named by PKG-009 package register and objectives. | Location referenced in Gate 7 snapshot; not reinterpreted in this Phase 2.2 run |
| Detailed codes, standards, and design clauses | TBD until accessible source slices are resolved by a later workflow. | TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-001 | Check identity table against `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| REQ-002 | Check SOW-0009 against `_CONTEXT.md` and `SCOPE_LEDGER.csv`. |
| REQ-003 | Check artifact list against `DELIVERABLE_REGISTER.csv` and `ARTIFACT_REGISTER.csv`. |
| REQ-004 | Check responsibility wording against `PACKAGE_REGISTER.csv` and `ARTIFACT_REGISTER.csv`. |
| REQ-005 | Check interface type list against `PACKAGE_REGISTER.csv` and `INTERFACE_REGISTER.csv`; confirm no separate power-panel deliverable is created from the interface note. |
| REQ-006 | Check objective list against `OBJECTIVE_DELIVERABLE_MAP.csv`. |
| REQ-007 | Review all numeric values, design details, and clause references for explicit source support; replace unsupported items with TBD. |
| REQ-008 | Confirm source-basis section names the Gate 7 snapshot and Workbook Packages row 10. |

## Documentation

The Scope of Work should produce or contain the following records:

- Package scope of work.
- Tagged equipment and package identity list.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.
- Source-basis and boundary record.
- Interface context record for applicable package interfaces.
- TBD/open-item list for missing design values, exclusions, or source slices.
