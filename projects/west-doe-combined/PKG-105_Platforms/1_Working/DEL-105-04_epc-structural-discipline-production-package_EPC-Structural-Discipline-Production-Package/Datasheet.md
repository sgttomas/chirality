# Datasheet: DEL-105-04 — EPC / Structural Discipline Production Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-105-04_epc-structural-discipline-production-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (GATE-07) |
| Name | EPC / Structural Discipline Production Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| ParentPackageID | `PKG-105` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Workbook Package ID | `26020-01-36-005` | `PACKAGE_REGISTER.csv` row PKG-105 |
| Package Name | Platforms | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| WBS | `01` | `PACKAGE_REGISTER.csv` row PKG-105 |
| Discipline | Structural | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC/Discipline Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible Party | TBD; EPC Integrator or discipline subcontractor as assigned | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0261` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-001`, `OBJ-005`, `OBJ-008`, `OBJ-010` | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (explicit deliverable-ID mapping — FACT, not heuristic) |
| Source Reference | Workbook Packages row 106 | `_CONTEXT.md`; `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject of production | Non-vendor package scope for the Platforms structural package | `DELIVERABLE_REGISTER.csv` row `DEL-105-04` |
| Production unit character | Carried conservatively from workbook and DBM support | `DELIVERABLE_REGISTER.csv` row `DEL-105-04` |
| Source-limitation status | Detailed non-vendor package deliverable requirements are source-limited and remain open for Gate 5 disposition | `DELIVERABLE_REGISTER.csv` Notes column |
| Workbook discipline description | "Platforms" (structural steel platforms class for WBS 01) | `PACKAGE_REGISTER.csv` row PKG-105 |
| Recorded interface types (PKG-105) | Area / Exterior Lighting; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv` rows IFC-26E3DCAD56, IFC-07C472C58B, IFC-B7C0A01E38 |
| Recorded interface guidance | Platform-to-equipment tie-ins should be confirmed by layout/model. Gate 6 disposition: platform-to-equipment tie-ins are the EPC Integrator's responsibility through the overall 3D model and integrated P&ID set. | `INTERFACE_REGISTER.csv` PKG-105 rows |
| Package-level exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` row PKG-105 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Discipline production package basis (anticipated artifact) | Workbook and DBM-supported production package evidence | `ARTIFACT_REGISTER.csv` row ART-16D83D7454 |
| TBD discipline deliverable register (anticipated artifact) | Not present in source; to be produced under this deliverable | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` |
| Source-limited requirements closure record (anticipated artifact) | Detailed discipline requirements are not present in the current source set and remain open | `ARTIFACT_REGISTER.csv` row ART-10C0D579FC |
| Design loads / load combinations | TBD — not present in accessible source slices | `_REFERENCES.md` (source slices not copied during PREPARATION) |
| Governing structural codes/standards | TBD — not named in accessible source slices; ASSUMPTION: project-level structural code basis will be inherited from the EPC Integrator package basis (DEL-105-01 / DEL-105-02) | ASSUMPTION |
| Material specifications | TBD — not present in accessible source slices | `_REFERENCES.md` |
| Environmental/site conditions | TBD — not present in accessible source slices for this deliverable | `_REFERENCES.md` |

## Construction

| Item | Value | Source |
|---|---|---|
| Production unit elements | Discipline (Structural) production deliverables for the non-vendor Platforms scope | `DELIVERABLE_REGISTER.csv` row `DEL-105-04` |
| Interfaces to other disciplines | Area / Exterior Lighting (Electrical); Grading / Site Drainage / Spill Containment (Civil); Structural / Foundations / Supports (Structural/Civil) | `INTERFACE_REGISTER.csv` PKG-105 rows |
| Companion EPC anchor deliverables | DEL-105-01 (Scope of Work), DEL-105-02 (Package Datasheet), DEL-105-03 (Construction Work Package) | `DELIVERABLE_REGISTER.csv` PKG-105 rows |
| Detailed structural elements (members, connections, weldments) | TBD — not present in accessible source slices | `_REFERENCES.md` |
| Fabrication / shop drawing requirements | TBD — not present in accessible source slices | `_REFERENCES.md` |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- `_DEPENDENCIES.md` (this deliverable)
- GATE-07 `DELIVERABLE_REGISTER.csv` — row `DEL-105-04_epc-structural-discipline-production-package`
- GATE-07 `PACKAGE_REGISTER.csv` — row `PKG-105` (Platforms; 26020-01-36-005)
- GATE-07 `ARTIFACT_REGISTER.csv` — rows ART-16D83D7454, ART-10C0D579FC
- GATE-07 `INTERFACE_REGISTER.csv` — rows IFC-26E3DCAD56, IFC-07C472C58B, IFC-B7C0A01E38
- GATE-07 `OBJECTIVE_DELIVERABLE_MAP.csv` — OBJ-001/005/008/010 mappings
- Workbook source: `_Sources/26020-Package_Requirements.docx`; `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; not slice-extracted during PREPARATION — location TBD for clause-level claims)
- DBM source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no Platforms-specific slice identified)
