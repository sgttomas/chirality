# Specification: Scope of Work

## Scope

This document specifies the required content and verification basis for the PKG-004 Site Grading scope-of-work deliverable.

The deliverable shall cover:

- Package identity for PKG-004 Site Grading, including workbook ID 4, WBS 02, CoA tracking number 26020-01-42-003, discipline Civil, and source row basis.
- Full package scope for the EPC Scope of Work, including package function, source basis, boundaries, and whole-facility integration narrative.
- The recorded package interfaces: Drain / Containment and Grading / Site Drainage / Spill Containment.
- Required artifacts listed for `DEL-004-01_scope-of-work`: package scope of work, tagged equipment and package identity list, package function and whole-facility integration narrative, and package responsibility assignment record.

The deliverable shall exclude:

- Final detailed engineering values that are identified as TBD pending geotechnical report, topographical survey, plot plan, or detailed engineering.
- Package-specific exclusions not stated in the accepted Gate 7 snapshot or accessible source slices.
- Vendor-package ownership assumptions; the accepted package register states no separate vendor-package ownership model is inferred from current sources.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, and `INTERFACE_REGISTER.csv`; `26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 5.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-001 | The scope of work shall identify PKG-004 as Site Grading, Civil discipline, WBS 02, workbook ID 4, workbook row 5, CoA tracking number 26020-01-42-003. | Check against Gate 7 `PACKAGE_REGISTER.csv` row `PKG-004` and workbook sheet `Packages`, row 5. |
| SOW-002 | The scope of work shall include the required artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Check against Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-004-01_scope-of-work`. |
| SOW-003 | The scope of work shall state that tagged equipment is TBD unless a source-supported tagged equipment list is provided. | Check that unsupported equipment tags are not invented. |
| SOW-004 | The scope of work shall carry Drain / Containment and Grading / Site Drainage / Spill Containment as recorded interfaces. | Check against Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-004` and workbook row 5 interface columns. |
| SOW-005 | The scope of work shall incorporate the site grading intent to prevent off-site surface overflow from entering the expansion facility and to direct and contain on-site overflow into a retention pond. | Check against `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| SOW-006 | The scope of work shall identify topographical survey and grade surface file inputs as required but TBD pending survey completion. | Check against `4-25_Deepcut_DBM.md`, `Geotechnical and Topographical Assumptions`. |
| SOW-007 | The scope of work shall identify geotechnical parameters and road granular pavement parameters as TBD pending the geotechnical report where they affect final grading, drainage, road, or foundation-related scope boundaries. | Check against `4-25_Deepcut_DBM.md`, `Geotechnical and Topographical Assumptions` and `Roads`. |
| SOW-008 | The scope of work shall preserve the grading and drainage design values listed in the DBM, including pad slopes, maximum grade slope, ditch slope, culvert slope, storm basis, and facility pad surface basis. | Check against `Datasheet.md` Construction table and `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| SOW-009 | The scope of work shall state that retention pond location and capacity remain tied to detailed engineering and plot plan development. | Check against `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| SOW-010 | The scope of work shall include NGL storage area surface-control considerations where applicable to site grading and spill containment. | Check against `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`. |
| SOW-011 | ASSUMPTION: The scope of work should reference the supported objectives OBJ-002, OBJ-007, OBJ-008, and OBJ-009 as directional context rather than clause-level requirements. | Check against Gate 7 `OBJECTIVE_DELIVERABLE_MAP.csv` and `OBJECTIVE_REGISTER.csv`; confirm no objective text is converted into unsupported design values. |

## Standards

| Standard / source | Applicability |
|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Accepted decomposition truth for deliverable identity, package mapping, artifacts, objectives, and interfaces. |
| `26020-Packages_Interfaces_4_export.xlsx`, sheet `Packages`, row 5 | Authoritative workbook source for package identity and interface flags. |
| `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management` | Source slice for grading, drainage, retention pond, and surface-control basis. |
| `4-25_Deepcut_DBM.md`, `Geotechnical and Topographical Assumptions` | Source slice for required survey/geotechnical inputs and TBD parameters. |
| `3-25_Comp_and_Liquids_DBM.md`, civil design slices at lines 124 and 688 | Supporting cross-facility civil/drainage context for uncertainty and civil scope coverage. |
| External civil, grading, hydrology, environmental, and regulatory standards | TBD; not listed at clause level in the accessible source slices for this deliverable. |

## Verification

The completed scope of work shall be verified by:

- Confirming every package identity field matches the accepted Gate 7 registers and workbook row 5.
- Confirming every interface named in the scope of work is present in Gate 7 `INTERFACE_REGISTER.csv` or workbook row 5.
- Confirming every numerical grading/drainage value is traceable to `4-25_Deepcut_DBM.md`, `Site Grading and Surface Water Management`.
- Confirming final-values gaps remain marked `TBD` when the DBM says the geotechnical report, topographical survey, plot plan, or detailed engineering will determine them.
- Confirming objective references are contextual and do not create requirements beyond the source-supported scope.
- Confirming no undeclared dependencies are treated as blockers under DECLARED coordination mode.

## Documentation

The scope-of-work package should produce or identify:

- Package scope of work.
- Tagged equipment and package identity list, with tagged equipment marked `TBD` unless source-supported.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.
- Source reference list tying package identity, interfaces, and grading/drainage basis to Gate 7 registers, workbook row 5, and DBM source slices.
- Open item list for geotechnical report, topographical survey/grade surface file, retention pond location/capacity, plot-plan ties, and external standards/permits.
