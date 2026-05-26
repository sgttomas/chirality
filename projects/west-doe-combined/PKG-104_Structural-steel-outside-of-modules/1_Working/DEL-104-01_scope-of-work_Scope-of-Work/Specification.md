# Specification: DEL-104-01_scope-of-work — Scope of Work

> Normative scope-of-work specification for `PKG-104` "Structural steel -
> outside of modules". Requirements derive from accessible sources. Inferred
> requirements are marked **ASSUMPTION**. Missing values are marked `TBD`.

## Scope

### In Scope

- Carry the workbook-defined Structural package "Structural steel - outside of
  modules" under WBS 01 as a distinct flat project package
  (Source: `SCOPE_LEDGER.csv` row `SOW-0260` IN; `PACKAGE_REGISTER.csv` row
  `PKG-104`).
- Author the package scope-of-work narrative covering: package function,
  source basis, boundaries, tagged equipment basis, WBS, discipline, and
  whole-facility integration (Source: `_CONTEXT.md` Scope; `ARTIFACT_REGISTER.csv`
  artifacts `ART-1667AE1F32`, `ART-6192616307`, `ART-4288CE535A`, `ART-FE5EE5E445`).
- Define the package boundary with respect to module-internal structural steel
  (which is out of scope of `PKG-104`) and adjacent disciplines via the two
  recorded physical interfaces (Source: `INTERFACE_REGISTER.csv`
  `IFC-CCDE4B56CA`, `IFC-ECDD4D3A15`).
- Record package responsibility assignment consistent with the workbook (Source:
  `PACKAGE_REGISTER.csv` Responsibility column for `PKG-104`).

### Out of Scope

- Module-internal structural steel (carried in the relevant module packages,
  not in `PKG-104`) — **ASSUMPTION** based on the package title
  "Structural steel - outside of modules".
- Pipe racks and pipe rack modules — designed exclusively by the EPC Integrator
  under `PKG-103` per the Gate 6 disposition recorded in
  `INTERFACE_REGISTER.csv` notes for `PKG-103` interfaces.
- Detailed discipline production deliverables (carried under
  `DEL-104-04_epc-structural-discipline-production-package`, which remains
  source-limited per `DELIVERABLE_REGISTER.csv`).
- Package datasheet content (carried under `DEL-104-02_package-datasheet`).
- Construction work package content (carried under
  `DEL-104-03_construction-work-package`).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-104-01-01 | The scope-of-work narrative shall identify `PKG-104` by Workbook ID 104, CoA tracking `26020-01-36-004`, discipline Structural, and WBS 01. | `PACKAGE_REGISTER.csv` row `PKG-104` |
| REQ-104-01-02 | The scope-of-work narrative shall state the workbook source row (Workbook Packages row 105). | `PACKAGE_REGISTER.csv` row `PKG-104`; `_CONTEXT.md` Source Reference |
| REQ-104-01-03 | The scope-of-work narrative shall list the applicable physical interfaces: "Grading / Site Drainage / Spill Containment" and "Structural / Foundations / Supports". | `INTERFACE_REGISTER.csv` `IFC-CCDE4B56CA`, `IFC-ECDD4D3A15`; `PACKAGE_REGISTER.csv` Applicable interface types |
| REQ-104-01-04 | The scope-of-work narrative shall apply the project structural basis (CAN/CSA-S16 design; CSA G40.20/G40.21 350W W-flange/HSS, 300W channels/plates/angles; National Building Code of Canada loading basis). | DBM-Deepcut SEC-11 lines 2672-2676; line 2753 |
| REQ-104-01-05 | The scope-of-work narrative shall state that foundation support is driven steel piles as default unless detailed engineering establishes a different basis. | DBM-Deepcut SEC-11 "Piles and Foundations" lines 2738-2749 |
| REQ-104-01-06 | The scope-of-work narrative shall record responsibility per the workbook, noting that EPC Integrator vs discipline-subcontractor responsibility is source-dependent and that no separate vendor-package ownership model is inferred. | `PACKAGE_REGISTER.csv` Responsibility note for `PKG-104` |
| REQ-104-01-07 | The scope-of-work narrative shall list package-specific exclusions as `TBD` until source materials state otherwise. | `PACKAGE_REGISTER.csv` row `PKG-104` exclusion field |
| REQ-104-01-08 | The scope-of-work narrative shall enumerate tagged major equipment for `PKG-104` or explicitly mark it `TBD` when not source-supported. | `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` `ART-6192616307`; **TBD** (no tagged equipment list in available source slices) |
| REQ-104-01-09 | The scope-of-work narrative shall describe how `PKG-104` integrates into the whole facility, citing supported objectives `OBJ-001` and `OBJ-008` and the SEC-11 civil/structural basis. | `_CONTEXT.md` Supports Objectives; `OBJECTIVE_REGISTER.csv`; DBM-Deepcut SEC-11 |
| REQ-104-01-10 | All non-trivial values shall be source-cited; un-cited assertions shall be marked `TBD` or `ASSUMPTION` (K-PROV-1). | Governing invariant; not a source claim |

## Standards

| Standard | Applicability | Source slice |
|---|---|---|
| National Building Code of Canada | Loading basis (snow, rain, wind, seismic); building egress | DBM-Deepcut SEC-11 line 2672; line 2753 |
| CAN/CSA-S16 (Design of Steel Structures); CSA S16:19 | Steel design basis | DBM-Deepcut SEC-11 line 2673; line 3412 |
| CSA G40.20/G40.21 | Structural steel material specification | DBM-Deepcut SEC-11 line 2676 |
| CAN/CSA A23.3 | Concrete design (where foundations engage) | DBM-Deepcut SEC-11 line 2674 |
| CSA A23.1/A23.2 | Concrete materials, construction, testing | DBM-Deepcut SEC-11 line 2677 |
| Canadian Foundation Engineering Manual | Foundation engineering | DBM-Deepcut SEC-11 line 2675 |

## Verification

| Req ID | Verification approach |
|---|---|
| REQ-104-01-01..02 | Inspect the issued scope-of-work narrative for the identification block and workbook source citation. |
| REQ-104-01-03 | Cross-check listed interfaces against `INTERFACE_REGISTER.csv` rows whose `PackageID = PKG-104`. |
| REQ-104-01-04..05 | Cross-check standards/materials citations against DBM-Deepcut SEC-11 source slice; foundation default against SEC-11 "Piles and Foundations". |
| REQ-104-01-06 | Confirm responsibility assignment record matches `PACKAGE_REGISTER.csv` Responsibility column verbatim or with a recorded human ruling. |
| REQ-104-01-07 | Confirm exclusions section explicitly carries `TBD` where source does not support specific exclusions. |
| REQ-104-01-08 | Confirm tagged-equipment list either enumerates source-supported tags or is explicitly `TBD`. |
| REQ-104-01-09 | Confirm integration narrative references `OBJ-001`, `OBJ-008`, and DBM-Deepcut SEC-11. |
| REQ-104-01-10 | Run quality review: every non-trivial value cited; un-cited items flagged. |

## Documentation

Required artifacts to be produced under this deliverable (per
`ARTIFACT_REGISTER.csv`):

- `ART-1667AE1F32` — Package scope of work
- `ART-6192616307` — Tagged equipment and package identity list
- `ART-4288CE535A` — Package function and whole-facility integration narrative
- `ART-FE5EE5E445` — Package responsibility assignment record

A `_STATUS.md` lifecycle file is maintained per K-STATUS-1; no other file
determines deliverable state.
