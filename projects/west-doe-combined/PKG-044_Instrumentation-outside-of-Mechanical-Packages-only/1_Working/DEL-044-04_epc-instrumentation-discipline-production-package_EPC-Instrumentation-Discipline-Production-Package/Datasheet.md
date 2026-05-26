# Datasheet — DEL-044-04 EPC / Instrumentation Discipline Production Package

> Pass 1/2 draft from `four-documents` skill. Deliverable is source-limited per decomposition; substantive technical values remain `TBD` pending Gate 5 disposition and resolution of additional source slices.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-044-04_epc-instrumentation-discipline-production-package` |
| Name | EPC / Instrumentation Discipline Production Package |
| ParentPackageID | `PKG-044` |
| ParentWorkbookID | 44 |
| PackageName | Instrumentation (outside of Mechanical Packages only) |
| Discipline | Instrumentation |
| Type | EPC/Discipline Production Unit |
| ResponsibleParty | TBD; EPC Integrator or discipline subcontractor as assigned (decomposition row, Workbook Packages row 46) |
| CoA / WBS | `26020-01-32-002` (PACKAGE_REGISTER row PKG-044) |
| Scope-of-work coverage | `SOW-0045` |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-010 (ASSUMPTION: package-grouping heuristic from `_CONTEXT.md`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Production unit role | Non-vendor (discipline-led) production unit for the package scope | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER row DEL-044-04 |
| Discipline | Instrumentation | PACKAGE_REGISTER PKG-044 Discipline column |
| Ownership model | No separate vendor-package ownership inferred; source-dependent EPC Integrator or discipline subcontractor | PACKAGE_REGISTER PKG-044 ResponsibilityNote |
| Maturity at this gate | Source-limited; carried conservatively from workbook + DBM support | DELIVERABLE_REGISTER DEL-044-04 Notes |
| Production package basis | Workbook Packages row 46; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | PACKAGE_REGISTER PKG-044 SourceReference |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating envelope | TBD (no source slice locally accessible for this deliverable) | `_REFERENCES.md` Missing/Deferred References |
| Environmental / area classification | TBD | `_REFERENCES.md` Missing/Deferred References |
| Utility requirements (power, air, signal) | TBD | `_REFERENCES.md` Missing/Deferred References |
| Interface conditions | Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network (ASSUMPTION: inherited from package-level interface types in PACKAGE_REGISTER PKG-044 `ApplicableInterfaceTypes`) | PACKAGE_REGISTER PKG-044 ApplicableInterfaceTypes |

## Construction

| Field | Value | Source |
|---|---|---|
| Discipline deliverable register | TBD (decomposition Notes: "TBD discipline deliverable register") | DELIVERABLE_REGISTER DEL-044-04 AnticipatedArtifacts |
| Production package basis document set | TBD; to be assembled from workbook + DBM support material | DELIVERABLE_REGISTER DEL-044-04 AnticipatedArtifacts |
| Source-limited requirements closure record | TBD; required as part of closure evidence | DELIVERABLE_REGISTER DEL-044-04 AnticipatedArtifacts |
| Equipment list / tagged scope | TBD; defer to DEL-044-01 (Scope of Work) and DEL-044-02 (Package Datasheet) when populated | ASSUMPTION (sibling-deliverable handoff convention) |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- DELIVERABLE_REGISTER row `DEL-044-04_epc-instrumentation-discipline-production-package` (GATE-07 snapshot)
- PACKAGE_REGISTER row `PKG-044` (GATE-07 snapshot)
- ARTIFACT_REGISTER rows for `DEL-044-01` and `DEL-044-02` (interface-fact context)
- OBJECTIVE_DELIVERABLE_MAP rows for `DEL-044-04` (objective associations)
- Workbook Packages row 46 (`26020-Packages_Interfaces_4_export.xlsx`) — referenced but not parsed in this run
- `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — referenced but not opened in this run (location TBD relative to `_REFERENCES.md` Shared Source Root)
