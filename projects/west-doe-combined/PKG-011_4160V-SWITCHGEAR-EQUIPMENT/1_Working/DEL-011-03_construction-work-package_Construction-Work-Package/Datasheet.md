# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-011-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-011 |
| Package name | 4160V SWITCHGEAR EQUIPMENT |
| Workbook ID | 11 |
| Workbook row | 13 |
| WBS | 02 |
| Discipline | Electrical |
| Deliverable type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | SOW-0012 |
| Decomposition basis | Gate 7 final published PROJECT_DECOMP snapshot, 2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package ownership model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration. | PACKAGE_REGISTER.csv row 13 |
| EPC construction-work-package purpose | Describes how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. | DELIVERABLE_REGISTER.csv row 50 |
| Required artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | DELIVERABLE_REGISTER.csv row 50; ARTIFACT_REGISTER.csv rows 195-197 |
| Package code | 26020-02-30-002 | PACKAGE_REGISTER.csv row 13 |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row 13; INTERFACE_REGISTER.csv rows 43-48 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials. | PACKAGE_REGISTER.csv row 13 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Construction maturity basis | Initial Phase 2.2 package authored from accepted Gate 7 decomposition truth and deliverable-local context. | _CONTEXT.md; _REFERENCES.md |
| Declared upstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |
| Declared downstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |
| Blocker model | Advisory only, limited to declared dependency edges, default blocker maturity threshold INITIALIZED. | _DEPENDENCIES.md; _Coordination/_COORDINATION.md |
| Source-slice limitation | No deliverable-specific source slices were copied during PREPARATION; detailed construction values, sequence constraints, inspections, permits, and hold points remain TBD until source-supported slices are resolved. | _REFERENCES.md |

## Construction

| Construction element | Data |
|---|---|
| Physical installation scope | Install/build 4160V switchgear equipment package and coordinate tie-ins to larger facility systems; detailed methods, locations, equipment tags, lifting requirements, cable routing, energization sequence, outage requirements, and permits are TBD. |
| Tie-in focus | Electrical power, grounding/bonding, I&C/control cabling, communications/network, maintenance access, and structural/foundation/support interfaces. |
| Inspection focus | Interface readiness, installation completion, construction inspection, turnover checklist closure, and evidence needed for downstream facility handoff. Specific inspection forms and acceptance criteria are TBD. |
| Turnover focus | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. |

## References

- _CONTEXT.md for deliverable identity, scope, anticipated artifacts, and supported objectives.
- _DEPENDENCIES.md for declared dependency state.
- _REFERENCES.md for accepted upstream truth pointers and source-access limitations.
- Gate 7 PROJECT_DECOMP snapshot: DELIVERABLE_REGISTER.csv row 50.
- Gate 7 PROJECT_DECOMP snapshot: PACKAGE_REGISTER.csv row 13.
- Gate 7 PROJECT_DECOMP snapshot: ARTIFACT_REGISTER.csv rows 195-197.
- Gate 7 PROJECT_DECOMP snapshot: INTERFACE_REGISTER.csv rows 43-48.
- Gate 7 PROJECT_DECOMP snapshot: OBJECTIVE_DELIVERABLE_MAP.csv rows 382, 850, 1384, 1938, 2921, 3488, and 4033.
