# Specification: EPC / Civil Discipline Production Package

## Scope

This specification covers the DEL-005-04 civil discipline production package for PKG-005 Site Grading. The deliverable is a non-vendor civil production unit for SOW-0005, grounded in the accepted Gate 7 decomposition snapshot and the accessible civil/site grading source basis.

Included scope:

- Civil production package basis for Site Grading.
- Drain / Containment interface incorporation.
- Grading / Site Drainage / Spill Containment interface incorporation.
- Source-limited requirements closure record.
- Discipline deliverable register placeholder until detailed discipline deliverable requirements are ruled or sourced.

Excluded or not established:

- Package-specific exclusions are TBD; no package-specific exclusions are stated in the accepted source materials.
- Final geotechnical, topographical, plot-plan, and detailed drainage inputs are not closed in the accessible source set.
- Vendor package engineering is not inferred for this deliverable.

Sources: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-005`; `DELIVERABLE_REGISTER.csv` row `DEL-005-04_epc-civil-discipline-production-package`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-001 | The production package shall identify PKG-005 as Site Grading, discipline Civil, WBS 03, CoA tracking number 26020-01-42-003. | Check Datasheet Identification against `PACKAGE_REGISTER.csv` row `PKG-005` and workbook row 6. |
| REQ-002 | The production package shall carry Drain / Containment and Grading / Site Drainage / Spill Containment as applicable interfaces. | Check interface matrix against `INTERFACE_REGISTER.csv` rows `IFC-590C44EF2F`, `IFC-F6589335A4`, and workbook row 6. |
| REQ-003 | The production package shall preserve the artifact set: discipline production package basis, TBD discipline deliverable register, and source-limited requirements closure record. | Check artifact list against `ARTIFACT_REGISTER.csv` rows `ART-84267B95AF` and `ART-3BB0AFBF4A` plus `_CONTEXT.md`. |
| REQ-004 | Civil grading and drainage content shall account for grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security where applicable to the Site Grading scope. | Review civil scope table against `3-25_Comp_and_Liquids_DBM.md` `Civil and infrastructure` and `Civil Scope` sections. |
| REQ-005 | Surface-water management content shall prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | Review drainage basis against `3-25_Comp_and_Liquids_DBM.md` `Surface Water and Drainage`. |
| REQ-006 | Process-contaminated drainage shall be routed to the appropriate drain or containment system rather than surface-water discharge. | Review drain/containment provisions against `3-25_Comp_and_Liquids_DBM.md` `Surface Water and Drainage`. |
| REQ-007 | Site grading criteria shall preserve source-stated grading principles: high equal-elevation ridges along main pipe racks, pad slopes down from pipe racks at 1.5% to each side, possible reduction to 1.0%, equal elevation around tank farms with exterior slope/swale as required, and 3H:1V maximum grade slope unless engineered or geotechnical requirements dictate otherwise. | Check grading criteria against `4-25_Deepcut_DBM.md` `Site Grading and Surface Water Management`. |
| REQ-008 | The requirements closure record shall identify final geotechnical report, topographical survey/grade surface file, plot plan/retention-pond reference, and detailed engineering drainage design as open inputs where not available. | Check closure record against `4-25_Deepcut_DBM.md` `External Inputs` and `Open Assumptions and Unresolved Items`. |
| REQ-009 | ASSUMPTION: Until a responsible party is assigned, production responsibility may be EPC Integrator or civil discipline subcontractor; the package shall not assign a separate vendor-package ownership model. | Confirm human assignment or preserve TBD; source is `PACKAGE_REGISTER.csv` row `PKG-005`. |

## Standards

| Standard / basis | Status |
|---|---|
| Accepted Gate 7 PROJECT_DECOMP snapshot | Governing decomposition truth for package, deliverable, artifact, objective, and interface identity. |
| 3-25 Comp and Liquids DBM civil/site sections | Accessible civil source basis for 3-25 WBS 03 civil and site work. |
| 4-25 Deepcut DBM civil/site grading sections | Accessible civil/site grading source basis used only for source-supported grading and surface-water criteria that are applicable by civil scope; package-specific applicability remains source-limited. |
| NFPA 30-2023 | Mentioned in DBM standards list as secondary containment basis; clause-level application to PKG-005 is TBD. |
| Geotechnical report | Required input; not available in current source set. |
| Topographical survey and grade surface file | Required input; not available in current source set. |

## Verification

- Confirm all package identity fields match the Gate 7 registers and workbook row 6.
- Confirm the two applicable interfaces are present and no unsupported interface types are added.
- Confirm all grading/drainage criteria are cited to an accessible DBM section or marked TBD.
- Confirm final design inputs unavailable in the source set remain in the closure record as TBD/open.
- Confirm no detailed design values are introduced without a cited source.

## Documentation

The completed production package should contain or reference:

- Discipline production package basis.
- Discipline deliverable register: TBD pending human/source ruling.
- Source-limited requirements closure record.
- Interface basis covering Drain / Containment and Grading / Site Drainage / Spill Containment.
- Evidence links to Gate 7 registers, workbook row 6, and DBM civil/site grading sections.
