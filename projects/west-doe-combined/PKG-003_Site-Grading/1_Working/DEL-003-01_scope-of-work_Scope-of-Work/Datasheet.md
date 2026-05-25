# Datasheet: DEL-003-01_scope-of-work — Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-003-01_scope-of-work` |
| Deliverable name | Scope of Work |
| Parent package | `PKG-003` |
| Package name | Site Grading |
| Parent workbook ID | 3 |
| Workbook row | 4 |
| WBS | `01` |
| CoA tracking number | `26020-01-42-003` |
| Discipline | Civil |
| Deliverable type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Covered scope item | `SOW-0003` |
| Supported objectives | `OBJ-001`, `OBJ-007`, `OBJ-008`, `OBJ-009` |

## Attributes

| Attribute | Source-grounded value |
|---|---|
| Package role | Site grading package for the 04-25 Deepcut facility package set. |
| Source package row | Workbook Packages row 4. |
| Package description | Workbook-defined Civil package for Site Grading under WBS 01 with recorded physical interfaces. |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources. |
| Scope-of-work artifact set | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. |
| Tagged equipment basis | No tagged equipment is identified in the accessible source slice for this scope-of-work deliverable. TBD if later source material defines tagged grading or drainage assets. |
| Interface types recorded for package | Drain / Containment; Grading / Site Drainage / Spill Containment. |
| Exclusions | TBD; no package-specific exclusions stated in the accessible source materials. |

## Conditions

| Condition | Source-grounded value |
|---|---|
| Civil DBM basis | Civil scope includes site grading, ditching, culvert, retention-pond, and surface-control requirements. |
| Surface-water management intent | Site grading and drainage shall prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond. |
| Main pipe rack grading principle | High equal-elevation ridges along main pipe racks. |
| Facility pad grading principle | Pad slopes down from pipe racks at 1.5% to each side. |
| Road drainage principle | Only access roads will be defined by ditches on either side. |
| Retention pond basis | On-site retention pond with berm to capture natural runoff; location and capacity remain detailed-engineering items. |
| Existing grade input | Existing grade surface file from topographical survey is expected as an input; format, data model, and final contents are TBD. |
| Plot plan dependency | Approximate retention pond location and civil layout coordination depend on the plot plan, including the `CIV-235633-5002-001` retention-pond reference. |

## Construction

| Construction / production element | Source-grounded value |
|---|---|
| Scope-of-work purpose | Define package function, source basis, boundaries, and whole-facility integration narrative for the Site Grading package. |
| Required package identity content | Package name, workbook ID, CoA tracking number, WBS, discipline, and source row. |
| Required interface content | Record and route Drain / Containment and Grading / Site Drainage / Spill Containment interfaces for downstream package datasheet and construction work package development. |
| Required responsibility content | Identify EPC Integrator responsibility and preserve TBD responsibility boundary where civil discipline subcontractor assignment is unresolved. |
| Required open-basis content | Preserve TBD items for final exclusions, detailed drainage sizing, retention pond capacity, final pond location, survey input, and plot-plan-dependent layout. |

## References

| Source | SectionRef / slice used |
|---|---|
| `_CONTEXT.md` | Identity, Scope, Anticipated Artifacts, Covers Scope Items, Supports Objectives |
| `_REFERENCES.md` | Authoritative decomposition basis and shared source root |
| Gate 7 `DELIVERABLE_REGISTER.csv` | `DEL-003-01_scope-of-work` row |
| Gate 7 `PACKAGE_REGISTER.csv` | `PKG-003` row |
| Gate 7 `ARTIFACT_REGISTER.csv` | `DEL-003-01_scope-of-work` rows |
| Gate 7 `INTERFACE_REGISTER.csv` | `IFC-CE1BC1285F`, `IFC-A9AB707D17` rows |
| Gate 7 `OBJECTIVE_REGISTER.csv` | `OBJ-001`, `OBJ-007`, `OBJ-008`, `OBJ-009` rows |
| `_Sources/26020-Packages_Interfaces_4_export.xlsx` | `Packages` sheet row 4 |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | SEC-11 Civil, Buildings, and Miscellaneous Facilities Basis; Site Grading and Surface Water Management; External Inputs |
