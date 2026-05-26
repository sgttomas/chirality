# Datasheet — DEL-043-03 Construction Work Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-043-03_construction-work-package` | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row 242 |
| Name | Construction Work Package | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row 242 |
| ParentPackageID | `PKG-043` | `_CONTEXT.md` |
| ParentWorkbookID | 43 | `_CONTEXT.md` |
| PackageName | Instrumentation (outside of Mechanical Packages only) | `_CONTEXT.md` |
| WBS | 01 | GATE-07 `PACKAGE_REGISTER.csv` row 45 |
| Discipline | Instrumentation | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 45 |
| ArtifactType | EPC Construction Work Package | GATE-07 `DELIVERABLE_REGISTER.csv` row 242 |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 242 |
| CoversScopeItems | `SOW-0044` | `_CONTEXT.md`; `SCOPE_LEDGER.csv` row 45 |
| SupportsObjectives | OBJ-001; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-010 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 242 |
| SourceRow | Workbook Packages row 45 | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package physical interface types | Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network | `PACKAGE_REGISTER.csv` row 45 |
| Field supports / power / comms inclusion | Not marked unless confirmed by package scope | `PACKAGE_REGISTER.csv` row 45 |
| Tagged equipment list (instruments in scope) | TBD — not enumerated in accessible decomposition rows; expected to be carried by `DEL-043-01_scope-of-work` and `DEL-043-02_package-datasheet` (location TBD) | `_CONTEXT.md` (anticipated artifacts); cross-deliverable scope |
| Vendor / discipline subcontractor ownership model | Source-dependent; no separate vendor-package ownership model inferred | `PACKAGE_REGISTER.csv` row 45 |
| Package-specific exclusions | TBD — none stated in source materials | `PACKAGE_REGISTER.csv` row 45 |
| Duplicate workbook tracking number handling | Workbook package row authoritative; duplicate tracking numbers not merged | `PACKAGE_REGISTER.csv` row 45 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / facility | West DOE combined facility (project workspace) | Project root `west-doe-combined` |
| Environmental design conditions | TBD — design basis values not present in accessible decomposition slices | `_REFERENCES.md` (Missing/Deferred); ASSUMPTION pending DBM access |
| Hazardous-area classification | TBD — not stated in accessible source slices | TBD |
| Construction season / climate constraints | TBD | TBD |
| Pre-commissioning / commissioning interlocks | TBD; coordinated through facility turnover system (location TBD) | ASSUMPTION |

## Construction

| Aspect | Value | Source |
|---|---|---|
| Physical installation expectations | Package will be physically installed, built, inspected, turned over, and tied into larger facility systems | `DELIVERABLE_REGISTER.csv` row 242 (description) |
| Anticipated artifacts produced | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 242 (artifacts column) |
| Tie-in interface set | Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network | `PACKAGE_REGISTER.csv` row 45 |
| Construction sequencing / workfaces | TBD — workface plan structure to be developed against site CWP/IWP convention (ASSUMPTION) | TBD |
| Materials / spares / consumables list | TBD | TBD |
| Inspection and test plan (ITP) | TBD — referenced under verification; clause-level content not derivable from accessible sources | TBD |
| Turnover documentation set | TBD; turnover checklist is an anticipated artifact | `_CONTEXT.md` |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- GATE-07 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` row 242 (this deliverable)
  - `PACKAGE_REGISTER.csv` row 45 (PKG-043)
  - `SCOPE_LEDGER.csv` row 45 (SOW-0044)
  - `OBJECTIVE_SCOPE_MAP.csv` rows 24, 266, 697, 945, 1177, 1932 (objective associations)
- Inaccessible (source slices not copied during PREPARATION): Workbook Packages row 45 raw cells; DBM-Deepcut and DBM-Comp_and_Liquids design-basis content. Content dependent on these sources is marked `TBD`.
