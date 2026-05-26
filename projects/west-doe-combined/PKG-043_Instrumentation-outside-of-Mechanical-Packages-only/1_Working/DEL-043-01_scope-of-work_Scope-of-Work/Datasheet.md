# Datasheet — DEL-043-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-043-01_scope-of-work | _CONTEXT.md |
| Name | Scope of Work | _CONTEXT.md |
| ParentPackageID | PKG-043 | _CONTEXT.md |
| WorkbookID / Row | 43 / row 45 | _CONTEXT.md; PACKAGE_REGISTER.csv |
| CoA Tracking | 26020-01-32-002 | PACKAGE_REGISTER.csv row PKG-043 |
| PackageName | Instrumentation (outside of Mechanical Packages only) | _CONTEXT.md |
| Discipline | Instrumentation | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Type | EPC Scope of Work | _CONTEXT.md |
| ResponsibleParty | EPC Integrator | _CONTEXT.md |
| WBS | 01 | PACKAGE_REGISTER.csv |
| ResponsibilityModel | EPC Integrator or discipline subcontractor (source-dependent; no separate vendor-package ownership inferred) | PACKAGE_REGISTER.csv row PKG-043 |
| PackageRole | authoritative companion register row | PACKAGE_REGISTER.csv row PKG-043 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope description | Workbook-defined Instrumentation package for "Instrumentation (outside of Mechanical Packages only)" under WBS 01 with recorded physical interfaces. | PACKAGE_REGISTER.csv row PKG-043 |
| Inclusion criteria | Workbook row 45; discipline Instrumentation; WBS 01. Applicable interface types: Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network. | PACKAGE_REGISTER.csv row PKG-043 |
| Exclusions | TBD; no package-specific exclusions stated in source materials. | PACKAGE_REGISTER.csv row PKG-043 |
| Interface review note | Field supports, power, and comms not marked unless confirmed by package scope. | PACKAGE_REGISTER.csv row PKG-043 |
| Covered scope items | SOW-0044 | _CONTEXT.md; DELIVERABLE_REGISTER.csv |
| Supported objectives (ASSUMPTION — package-grouped) | OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 | _CONTEXT.md; DELIVERABLE_REGISTER.csv |

## Conditions (Boundary and Applicability)

| Item | Value | Source |
|---|---|---|
| Package boundary | Instrumentation scope outside of Mechanical Packages only (i.e., instrumentation not already owned by a mechanical vendor package). | PACKAGE_REGISTER.csv row PKG-043 (Name + ResponsibilityModel) |
| Cross-facility applicability | DBM identifies instrumentation as shared between 03-25 and 04-25 for instrument air and analyzers; cross-facility applicability of this package is TBD pending boundary disposition. | DBM-Deepcut/4-25_Deepcut_DBM.md L74-75, L1822, L1906-1925 |
| Reserved-volume condition (related shared utility) | Instrument air system reserve: 15 minutes usable reserve after shutdown (DBM utility basis, informational; not a direct PKG-043 requirement). | DBM-Deepcut/4-25_Deepcut_DBM.md L1941 |
| Project specification anchor | ELC-QAS-000014-001 "Instrumentation General" (project Electrical & Instrumentation specifications govern). | DBM-Deepcut/4-25_Deepcut_DBM.md L2870, L2887 |

## Construction / Tagged Equipment

| Item | Value | Source |
|---|---|---|
| Tagged equipment list at PKG-043 scope | TBD — not enumerated in extracted sources for row 45 specifically. | _Sources/26020-Package_Requirements.docx (binary; not extracted); PACKAGE_REGISTER.csv (no equipment list field) |
| Related equipment evidence (informational, not PKG-043 ownership) | Instrument Air Building equipment seen at 4-25: K-4210-1, K-4220-1, F-4220-1, F-4230-1, F-4225-1, F-4215-1, V-4240-1, V-4210-1 — owned by the consolidated 04-25 Instrument Air package, not by PKG-043. | DBM-Deepcut/4-25_Deepcut_DBM.md L2601 |
| Implementation note | Installation of shipped-loose instruments, valves, and components is Tourmaline field construction scope. (ASSUMPTION: directionally applicable to PKG-043; confirm at detailed engineering.) | DBM-Deepcut/4-25_Deepcut_DBM.md L115 |

## References

- `_CONTEXT.md` (deliverable identity, scope, objectives)
- `_REFERENCES.md` (deliverable reference index)
- `_DEPENDENCIES.md` (declared dependencies — none at PREPARATION)
- PACKAGE_REGISTER.csv, row PKG-043 — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- DELIVERABLE_REGISTER.csv, row DEL-043-01_scope-of-work — same snapshot folder
- Workbook Packages row 45 — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` (binary; location TBD for clause-level extraction)
- DBM Deepcut basis — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
