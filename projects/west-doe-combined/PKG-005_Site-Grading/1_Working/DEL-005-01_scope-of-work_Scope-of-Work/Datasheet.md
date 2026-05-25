# Datasheet: DEL-005-01_scope-of-work - Scope of Work

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-005-01_scope-of-work |
| Deliverable name | Scope of Work |
| Parent package | PKG-005 - Site Grading |
| Workbook ID / row | 5 / row 6 |
| WBS | 03 |
| CoA tracking number | 26020-01-42-003 |
| Discipline | Civil |
| Type | EPC Scope of Work |
| Responsible party | EPC Integrator |
| Scope item | SOW-0005 |
| Supported objectives | OBJ-002; OBJ-007; OBJ-008; OBJ-009 |

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row for `DEL-005-01_scope-of-work`; Gate 7 `PACKAGE_REGISTER.csv` row for `PKG-005`; Gate 7 `SCOPE_LEDGER.csv` row for `SOW-0005`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package name | Site Grading | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005` |
| Package discipline | Civil | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005` |
| Package basis | Workbook-defined Civil package for Site Grading under WBS 03 with recorded physical interfaces | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005` |
| Responsibility model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005` |
| Scope-of-work purpose | Mandatory EPC Integrator deliverable for full package scope, tagged equipment where source-supported, package function, source basis, boundaries, and whole-facility integration narrative | Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-005-01_scope-of-work`; Gate 7 `VOCABULARY_MAP.csv`, Scope of Work |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record | Gate 7 `DELIVERABLE_REGISTER.csv`, `DEL-005-01_scope-of-work`; Gate 7 `ARTIFACT_REGISTER.csv`, rows for `DEL-005-01_scope-of-work` |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility context | 03-25 compressor station and liquids hub scope | Gate 7 `PROJECT_DECOMP.md`, `OBJ-002`; DBM 03-25 `SEC-11 - Plant Layout, Spacing, Civil, and Buildings` |
| Layout dependencies | Plot plan and spacing information must be verified against current civil drawings and equipment layout before final issue | DBM 03-25 `SEC-11 - Layout Basis` |
| Interface types | Drain / Containment; Grading / Site Drainage / Spill Containment | Gate 7 `INTERFACE_REGISTER.csv`, `PKG-005` |
| Civil design coverage relevant to package | Grading, drainage, roads, surface-water management, retention pond, foundations/supports, building foundations, fencing, and security | DBM 03-25 `SEC-11 - Site and Civil Conditions` |
| Surface-water management basis | Prevent uncontrolled offsite discharge, protect process areas, support construction and operations access | DBM 03-25 `SEC-11 - Surface Water and Drainage` |
| Hydrology uncertainty | Rainfall basis uses NBCC 2020 Dawson Creek IDF data as a proxy pending site-specific update; drainage, retention pond sizing, and surface-water management carry this uncertainty until final hydrology inputs are confirmed | DBM 03-25 `SEC-02 - Design Implications / rainfall basis` |
| Geotechnical maturity | Final geotechnical report is required before foundation design closure; current geotechnical basis remains preliminary | DBM 03-25 `SEC-11 - Site and Civil Conditions`; `SEC-02 - Geotechnical and Seismic Basis` |
| Regulatory basis | Stormwater management and related activities must comply with applicable BC water legislation and regulator requirements; detailed regulatory review remains required | DBM 03-25 `SEC-15 - BC Water Regulations` |

## Construction

This deliverable is a scope-definition artifact, not a construction work package. It must define the package work boundaries and integration basis needed by downstream package datasheet, construction work package, and EPC/Civil discipline production package deliverables.

| Construction-related item | Datasheet value | Source |
|---|---|---|
| Work package relationship | Construction work package for `PKG-005` is a sibling deliverable (`DEL-005-03`) and not replaced by this Scope of Work | Gate 7 `DELIVERABLE_REGISTER.csv`, `PKG-005` rows |
| Construction support context | Construction scope includes grading and related construction management activities | DBM 03-25 introductory construction-scope text, line-referenced source slice around construction scope |
| Physical interface evidence | Drain / Containment and Grading / Site Drainage / Spill Containment are interface facts carried as evidence, not separate deliverables | Gate 7 `ARTIFACT_REGISTER.csv`, rows `ART-6F70DBF7E2` and `ART-3CBE544E73` |
| Package exclusions | TBD; no package-specific exclusions stated in source materials | Gate 7 `PACKAGE_REGISTER.csv`, `PKG-005` |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-005_Site-Grading/1_Working/DEL-005-01_scope-of-work_Scope-of-Work/_CONTEXT.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/PKG-005_Site-Grading/1_Working/DEL-005-01_scope-of-work_Scope-of-Work/_DEPENDENCIES.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PROJECT_DECOMP.md`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
