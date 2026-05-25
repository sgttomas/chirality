# Specification: DEL-006-01_scope-of-work — Scope of Work

## Scope

This deliverable specifies the EPC scope-of-work content for `PKG-006 — Containment Berms`, a Civil WBS 03 package. It covers the package identity, source basis, boundaries, applicable interfaces, package function, whole-facility integration narrative, and responsibility assignment record for the Containment Berms package.

Included scope:

- Carry SOW-0006: workbook-defined Civil package "Containment Berms" as a distinct flat project package for WBS 03 (`SCOPE_LEDGER.csv`, SOW-0006).
- Document the applicable interface types: Drain / Containment and Grading / Site Drainage / Spill Containment (`INTERFACE_REGISTER.csv`, PKG-006).
- Align the scope narrative with the 03-25 civil and drainage basis (`3-25_Comp_and_Liquids_DBM.md`, SEC-11).
- Identify missing package-specific design values as `TBD` instead of deriving them from general civil language.

Excluded or deferred scope:

- Package-specific exclusions are `TBD`; no source-specific exclusions are stated for PKG-006 (`PACKAGE_REGISTER.csv`, PKG-006).
- Berm geometry, containment volume, materials, liner details, detailed grading, and construction coordinates are `TBD` until detailed civil design, hydrology, geotechnical, and layout inputs are accepted.
- Vendor engineered equipment scope is not inferred for this Civil package.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-006-01 | The scope of work shall identify `PKG-006 — Containment Berms` as a Civil package under WBS 03 with CoA tracking number `26020-03-42-006`. | `PACKAGE_REGISTER.csv`, PKG-006 |
| REQ-006-02 | The scope of work shall identify SOW-0006 as the covered scope item and retain the package as a distinct flat project package. | `SCOPE_LEDGER.csv`, SOW-0006 |
| REQ-006-03 | The scope of work shall include the mandatory EPC scope-of-work artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | `DELIVERABLE_REGISTER.csv`, DEL-006-01_scope-of-work |
| REQ-006-04 | The scope of work shall include the declared interface types `Drain / Containment` and `Grading / Site Drainage / Spill Containment`. | `INTERFACE_REGISTER.csv`, PKG-006 |
| REQ-006-05 | The scope of work shall require surface-water management to prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | `3-25_Comp_and_Liquids_DBM.md`, SEC-11 Surface Water and Drainage |
| REQ-006-06 | The scope of work shall route process-contaminated drainage to the appropriate drain or containment system rather than surface-water discharge. | `3-25_Comp_and_Liquids_DBM.md`, SEC-11 Surface Water and Drainage |
| REQ-006-07 | The scope of work shall carry the current rainfall and storm basis as provisional until hydrology is updated. | `3-25_Comp_and_Liquids_DBM.md`, SEC-02 Site-Specific Design Data; SEC-11 Surface Water and Drainage |
| REQ-006-08 | The scope of work shall require final geotechnical confirmation before foundation or civil design closure where berm construction depends on soil, settlement, frost, or support assumptions. | `3-25_Comp_and_Liquids_DBM.md`, SEC-02 Geotechnical and Seismic Basis; SEC-11 Site and Civil Conditions |
| REQ-006-09 | The scope of work shall cite applicable civil/structural governing content as NBCC, geotechnical report, site data, civil drawings, and surface-water management, with unavailable standards treated as verification requirements. | `3-25_Comp_and_Liquids_DBM.md`, SEC-15 Specifications, Codes, and Standards |
| REQ-006-10 | ASSUMPTION: The responsibility assignment should identify EPC Integrator or civil discipline subcontractor ownership and flag final assignment as source-dependent. | `PACKAGE_REGISTER.csv`, PKG-006 |

## Standards

| Standard or governing content | Status | Source |
|---|---|---|
| NBCC | Applicable to civil/structural governing content; clause location TBD | `3-25_Comp_and_Liquids_DBM.md`, SEC-15 Specifications, Codes, and Standards |
| Final geotechnical report | Required before foundation/civil design closure; report not available in current source set | `3-25_Comp_and_Liquids_DBM.md`, SEC-02 and SEC-11 |
| Site data and civil drawings | Required for final layout, drainage, and civil design verification; detailed drawings not available in current source set | `3-25_Comp_and_Liquids_DBM.md`, SEC-11 |
| Surface-water management basis | Required for drainage/containment design | `3-25_Comp_and_Liquids_DBM.md`, SEC-11 Surface Water and Drainage |
| Environmental/regulatory governing content | BCER permits, water regulations, consultation/notification, waste management permit; location TBD | `3-25_Comp_and_Liquids_DBM.md`, SEC-15 Specifications, Codes, and Standards |

## Verification

| Requirement IDs | Verification approach |
|---|---|
| REQ-006-01 through REQ-006-04 | Check scope-of-work identity, deliverable contents, and interface tables against Gate 7 registers and workbook row 7. |
| REQ-006-05 through REQ-006-06 | Check drainage and containment narrative against SEC-11 Surface Water and Drainage and the detailed civil drainage design when available. |
| REQ-006-07 | Confirm the hydrology basis and update any provisional rainfall/storm assumptions before final issue. |
| REQ-006-08 | Confirm final geotechnical report acceptance before closing berm construction criteria. |
| REQ-006-09 | Check standards/codes list against the latest project specification index and civil drawing register. |
| REQ-006-10 | Obtain project responsibility assignment or human ruling for EPC Integrator vs civil discipline subcontractor ownership. |

## Documentation

The scope-of-work package shall produce or reference:

- Package scope of work.
- Tagged equipment and package identity list, with `TBD` if no tagged equipment applies.
- Package function and integration narrative.
- Responsibility assignment record.
- Interface summary for Drain / Containment and Grading / Site Drainage / Spill Containment.
- Source basis and open/TBD item list.
