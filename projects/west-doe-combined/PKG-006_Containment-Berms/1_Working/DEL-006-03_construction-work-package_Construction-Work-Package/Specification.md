# Specification: Construction Work Package

## Scope

This specification governs the deliverable-local Construction Work Package for `PKG-006` Containment Berms. The package is a Civil WBS 03 scope item and is an EPC Integrator deliverable for physical installation, construction, inspection, turnover, and tie-in to larger facility systems.

The Construction Work Package shall cover:

- construction work package content;
- installation and tie-in workface planning;
- construction interface and turnover checklist content;
- Drain / Containment interface controls;
- Grading / Site Drainage / Spill Containment interface controls.

Exclusions:

- Detailed berm geometry, material, liner, coating, and acceptance criteria are `TBD` unless confirmed by IFC civil drawings, project civil specifications, geotechnical reports, environmental requirements, or other accepted source material.
- No separate vendor-package ownership model is inferred for this Civil package from current sources.

Sources: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-006-03_construction-work-package`; `PACKAGE_REGISTER.csv` row `PKG-006`; `INTERFACE_REGISTER.csv` rows for `PKG-006`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| CWP-REQ-001 | The Construction Work Package shall identify `PKG-006` Containment Berms, workbook row 7, WBS 03, CoA tracking number `26020-03-42-006`, Civil discipline, and responsible party. | Confirm against `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| CWP-REQ-002 | The package shall include a construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. | Confirm required artifacts are present in the package index and turnover records. |
| CWP-REQ-003 | The workface plan shall address the source-recorded interfaces: Drain / Containment and Grading / Site Drainage / Spill Containment. | Check interface checklist against `INTERFACE_REGISTER.csv` rows `IFC-62ACD644F9` and `IFC-2A535A882C`. |
| CWP-REQ-004 | Surface-water management provisions shall prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | Review CWP drainage controls against `3-25_Comp_and_Liquids_DBM.md` SEC-11 Surface Water and Drainage. |
| CWP-REQ-005 | Process-contaminated drainage shall be routed to the appropriate drain or containment system rather than surface-water discharge. | Inspect drainage/containment tie-in details and turnover checklist against DBM SEC-11. |
| CWP-REQ-006 | Drainage, retention pond sizing, and surface-water-management criteria shall identify current hydrology uncertainty until final hydrology inputs are confirmed. | Confirm open-item/TBD register cites DBM SEC-02 rainfall basis. |
| CWP-REQ-007 | Foundation, site preparation, frost protection, settlement, and structural support criteria shall not be closed until the final geotechnical report is accepted. | Confirm construction readiness gate includes final geotechnical report or a `TBD` exception. |
| CWP-REQ-008 | The Construction Work Package shall preserve civil, electrical, controls, instrumentation, safety, environmental, and turnover interfaces where they affect construction. | Confirm interface/turnover checklist includes applicable discipline reviews and signoffs. |
| CWP-REQ-009 | Standards and code references unavailable in the workspace shall be treated as verification requirements, not closed requirements. | Confirm standards register marks unavailable source locations as `location TBD` or verification-required. |
| CWP-REQ-010 | ASSUMPTION: Before issue for construction, the Construction Work Package shall be aligned with the plot plan, equipment list, civil drawings, and any construction work package register. | Confirm against DBM SEC-10 final miscellaneous facilities alignment statement and project IFC deliverables when available. |

## Standards

| Standard / authority | Status |
|---|---|
| NBCC 2020 Dawson Creek IDF rainfall proxy | Referenced as current rainfall basis in DBM SEC-02; site-specific update pending. |
| Final geotechnical report | Required before foundation design closure; not accessible in current deliverable source set. |
| BC environmental and water regulatory requirements | Detailed act, permit, trigger, and deliverable register remains TBD in current source set per DBM SEC-15. |
| Civil/structural governing content | NBCC, geotechnical report, site data, civil drawings, and surface-water management per DBM SEC-15; detailed project specification index verification required. |
| Project specifications and standards register | `location TBD`; DBM SEC-15 states unavailable citations must be verified before final issue. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Package identity | Document review | Matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Interface coverage | Checklist review | Includes Drain / Containment and Grading / Site Drainage / Spill Containment. |
| Drainage and containment routing | Engineering review and field inspection hold point | No process-contaminated drainage routed to surface-water discharge unless approved by environmental/regulatory authority. |
| Hydrology/geotechnical readiness | Design readiness review | Final hydrology and geotechnical inputs accepted, or exceptions explicitly carried as `TBD`. |
| Construction turnover | Turnover package review | Construction records, inspections, exceptions, and interface signoffs complete. |
| Standards verification | Standards register check | Unavailable standards are not represented as closed. |

## Documentation

The deliverable shall include or reference:

- construction work package;
- installation and tie-in workface plan;
- construction interface and turnover checklist;
- interface checklist for Drain / Containment;
- interface checklist for Grading / Site Drainage / Spill Containment;
- construction inspection and turnover records;
- unresolved criteria register for hydrology, geotechnical, IFC drawing, civil specification, and regulatory items.
