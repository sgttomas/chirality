# Datasheet: Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-022-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-022 |
| Package name | 5kV SWITCHGEAR EQUIPMENT |
| Workbook ID | 22 |
| Workbook row | 24 |
| WBS | 01 |
| Package code | 26020-01-30-013 |
| Discipline | Electrical |
| Deliverable type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | SOW-0023 |
| Decomposition basis | Gate 7 final published PROJECT_DECOMP snapshot, 2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package ownership model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv row `PKG-022` |
| EPC construction-work-package purpose | Describes how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems. | DELIVERABLE_REGISTER.csv row `DEL-022-03_construction-work-package` |
| Required artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | DELIVERABLE_REGISTER.csv row `DEL-022-03_construction-work-package`; ARTIFACT_REGISTER.csv rows `ART-31BD60C810`, `ART-474069A619`, `ART-686B185A30` |
| Package code | 26020-01-30-013 | PACKAGE_REGISTER.csv row `PKG-022` |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row `PKG-022`; INTERFACE_REGISTER.csv rows `IFC-FAD0C5C924`, `IFC-291807A33B`, `IFC-FFD6E87354`, `IFC-652BE03197`, `IFC-53BEFBC3CA`, `IFC-ED54C3FD1A` |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials. | PACKAGE_REGISTER.csv row `PKG-022` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Construction maturity basis | Initial Phase 2.2 package authored from accepted Gate 7 decomposition truth and deliverable-local context. | _CONTEXT.md; _REFERENCES.md |
| Declared upstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |
| Declared downstream dependencies | None declared during PREPARATION. | _DEPENDENCIES.md |
| Blocker model | Advisory only, limited to declared dependency edges; default blocker maturity threshold INITIALIZED. | _DEPENDENCIES.md; _Coordination/_COORDINATION.md |
| Source-slice limitation | No deliverable-specific source slices were copied during PREPARATION; detailed construction values, sequence constraints, inspections, permits, and hold points remain TBD until source-supported slices are resolved. | _REFERENCES.md |

## Construction

| Construction element | Data |
|---|---|
| Physical installation scope | Install/build the 5kV switchgear equipment package and coordinate tie-ins to larger facility systems; detailed methods, locations, equipment tags, lifting requirements, cable routing, energization sequence, outage requirements, and permits are TBD. |
| Tie-in focus | Electrical power, grounding/bonding, I&C/control cabling, communications/network, maintenance access, and structural/foundation/support interfaces. |
| Inspection focus | Interface readiness, installation completion, construction inspection, turnover checklist closure, and evidence needed for downstream facility handoff. Specific inspection forms and acceptance criteria are TBD. |
| Turnover focus | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. |

## References

- _CONTEXT.md for deliverable identity, scope, anticipated artifacts, and supported objectives.
- _DEPENDENCIES.md for declared dependency state.
- _REFERENCES.md for accepted upstream truth pointers and source-access limitations.
- Gate 7 PROJECT_DECOMP snapshot: DELIVERABLE_REGISTER.csv row `DEL-022-03_construction-work-package`.
- Gate 7 PROJECT_DECOMP snapshot: PACKAGE_REGISTER.csv row `PKG-022`.
- Gate 7 PROJECT_DECOMP snapshot: ARTIFACT_REGISTER.csv rows `ART-31BD60C810`, `ART-474069A619`, `ART-686B185A30`.
- Gate 7 PROJECT_DECOMP snapshot: INTERFACE_REGISTER.csv rows `IFC-FAD0C5C924`, `IFC-291807A33B`, `IFC-FFD6E87354`, `IFC-652BE03197`, `IFC-53BEFBC3CA`, `IFC-ED54C3FD1A`.
- Gate 7 PROJECT_DECOMP snapshot: OBJECTIVE_DELIVERABLE_MAP.csv rows for `DEL-022-03_construction-work-package` (objectives OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- _Sources/DBM-Deepcut/4-25_Deepcut_DBM.md referenced by Gate 7 PACKAGE_REGISTER.csv row `PKG-022`; not reinterpreted in this bounded task.
