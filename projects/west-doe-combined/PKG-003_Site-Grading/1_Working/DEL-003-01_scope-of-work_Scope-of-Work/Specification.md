# Specification: DEL-003-01_scope-of-work — Scope of Work

## Scope

This specification governs production of the EPC Scope of Work for `DEL-003-01_scope-of-work`, the Site Grading scope-of-work deliverable for `PKG-003`.

The deliverable shall cover:

- package identity: `PKG-003`, Site Grading, Civil discipline, WBS `01`, CoA tracking number `26020-01-42-003`, Workbook Packages row 4;
- package function and integration narrative for civil site grading within the 04-25 Deepcut facility package set;
- source basis and boundaries for the Site Grading scope;
- recorded interfaces: Drain / Containment and Grading / Site Drainage / Spill Containment;
- package responsibility basis and unresolved responsibility boundary where applicable;
- open design basis items that are not closed by accessible source material.

The deliverable shall exclude:

- final detailed grading design, ditch sizing, culvert sizing, retention pond capacity, and final pond location unless supplied by later accepted design inputs;
- civil drawings, construction workface planning, or discipline production calculations owned by sibling deliverables;
- vendor-package design requirements not supported by the accessible Site Grading source slice.

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| SOW-003-REQ-001 | The Scope of Work shall identify the deliverable as `DEL-003-01_scope-of-work`, Scope of Work, for `PKG-003` Site Grading. | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-003-01_scope-of-work` |
| SOW-003-REQ-002 | The Scope of Work shall identify Civil as the discipline, EPC Integrator as the responsible party, and EPC Scope of Work as the deliverable type. | `_CONTEXT.md` Identity; Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-003-01_scope-of-work` |
| SOW-003-REQ-003 | The Scope of Work shall preserve the package source basis: Workbook Packages row 4, WBS `01`, CoA tracking number `26020-01-42-003`, package name Site Grading. | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-003`; `_Sources/26020-Packages_Interfaces_4_export.xlsx` `Packages` sheet row 4 |
| SOW-003-REQ-004 | The Scope of Work shall include the anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts; Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-003-01_scope-of-work` |
| SOW-003-REQ-005 | The Scope of Work shall record that tagged equipment is TBD unless later accepted source material identifies package-specific tagged equipment. | Gate 7 `ARTIFACT_REGISTER.csv` `Tagged equipment and package identity list` note; accessible source slice has no tagged equipment value |
| SOW-003-REQ-006 | The Scope of Work shall carry the recorded package interfaces: Drain / Containment and Grading / Site Drainage / Spill Containment. | Gate 7 `INTERFACE_REGISTER.csv` rows `IFC-CE1BC1285F`, `IFC-A9AB707D17`; `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 4 |
| SOW-003-REQ-007 | The Scope of Work shall identify package-specific exclusions as TBD because the accessible source materials state no package-specific exclusions. | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-003` |
| SOW-003-REQ-008 | The Scope of Work shall state that detailed civil implementation depends on later geotechnical, topographical, plot-plan, and detailed drainage inputs. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 Civil basis and External Inputs |
| SOW-003-REQ-009 | The Scope of Work shall preserve the DBM surface-water management intent: prevent off-site surface overflow from entering the expansion facility and direct/contain on-site overflow into a retention pond. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Site Grading and Surface Water Management |
| SOW-003-REQ-010 | The Scope of Work shall not convert objective mappings into final design requirements unless the requirement is also supported by source material. | Gate 7 `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv`; four-documents authority hierarchy |

## Standards

| Standard / basis | Applicability |
|---|---|
| Gate 7 final published PROJECT_DECOMP snapshot | Accepted decomposition truth for deliverable identity, package mapping, artifacts, interfaces, and objective association. |
| `_Sources/26020-Packages_Interfaces_4_export.xlsx` | Authoritative workbook source slice for row 4 package identity and interface marks. |
| `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 | Source basis for civil, site-grading, drainage, retention pond, surface-control, and external-input constraints. |
| Detailed geotechnical report | TBD; required future input for civil/structural work. |
| Topographical survey / existing grade surface file | TBD; required future input for grading and drainage design. |
| Plot plan, including `CIV-235633-5002-001` retention-pond reference | TBD; required future input for retention pond location and civil layout coordination. |
| Detailed engineering drainage design | TBD; required future input for final IDF duration, ditch/culvert sizing, retention pond capacity, and final pond location. |

## Verification

| Verification ID | Verifies | Method |
|---|---|---|
| VER-001 | Package identity fields are complete and source-aligned. | Compare against `_CONTEXT.md`, Gate 7 `DELIVERABLE_REGISTER.csv`, Gate 7 `PACKAGE_REGISTER.csv`, and workbook row 4. |
| VER-002 | Interface list is complete for this source slice. | Compare against workbook row 4 X-column interface marks and Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-003`. |
| VER-003 | DBM civil basis is carried without overclaiming final design values. | Confirm DBM-derived content cites SEC-11 and keeps external-input-dependent details as TBD. |
| VER-004 | Artifact content matches the scope-of-work deliverable role. | Confirm all four anticipated artifacts are represented in the Scope of Work. |
| VER-005 | Unsupported exclusions, equipment tags, and final design criteria remain TBD. | Review for invented values not present in accessible source material. |

## Documentation

The completed Scope of Work should produce or contain:

- package scope of work;
- tagged equipment and package identity list, with tagged equipment marked TBD if unsupported;
- package function and integration narrative;
- responsibility assignment record;
- source basis list and open-basis/TBD register;
- interface basis for Drain / Containment and Grading / Site Drainage / Spill Containment.
