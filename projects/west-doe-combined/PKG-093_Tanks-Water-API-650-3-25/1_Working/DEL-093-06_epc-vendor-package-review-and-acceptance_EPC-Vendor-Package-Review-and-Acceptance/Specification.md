# Specification — DEL-093-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope

This specification governs the EPC-Integrator-led review, integration acceptance, and handoff readiness verification of the Package Vendor's deliverables for the Tanks, Water (API 650) 3-25 package (`PKG-093`). It defines what the EPC must verify, what evidence must be collected, and what conditions must be satisfied before the vendor package is accepted and turned over.

The acceptance set covers:

- The vendor engineered equipment package (`DEL-093-04`) — physical equipment and engineering basis;
- The vendor document turnover package (`DEL-093-05`) — vendor document register, submittals, and turnover records;
- Conformance to the EPC Scope of Work (`DEL-093-01`), EPC Package Datasheet (`DEL-093-02`), and EPC Construction Work Package (`DEL-093-03`).

### Out of scope

- Vendor-internal engineering design (owned by Package Vendor under `DEL-093-04`).
- Pipeline/installation work downstream of the facility riser/tie-in (by others; DBM SEC-04 line 216, SEC-06 line 432).
- Sales condensate LACT equipment (third-party NRM scope per DBM Facility Overview line 20).
- Final produced-water disposition agreements (subject to end-user requirements; DBM SEC-04 line 214).

## Requirements

Requirements are stated as EPC-Integrator acceptance obligations. Each requirement references a source or carries a labelled `ASSUMPTION`/`TBD`.

### R-1 — Vendor Document Review

R-1.1 The EPC SHALL maintain a vendor document review log covering each item in the vendor document register produced under `DEL-093-05`. (Source: `_CONTEXT.md` Anticipated Artifacts; `DEL-093-05` register row.)

R-1.2 The EPC SHALL record review status (Approved / Approved with Comments / Revise and Resubmit / Rejected) and disposition for each vendor document. (ASSUMPTION: status-set convention; clause-level convention `location TBD` in `26020-Package_Requirements.docx` heading 45.)

R-1.3 Vendor documents required by source (`26020-Package_Requirements.docx` vendor document tables — OBJ-010) SHALL be confirmed present and reviewed before acceptance. (Source reference; clause-level vendor document table not directly read — clause IDs `location TBD`.)

### R-2 — Conformance to EPC Anchor Deliverables

R-2.1 The EPC SHALL verify the vendor engineered equipment package (`DEL-093-04`) conforms to the EPC Package Datasheet (`DEL-093-02`) for equipment count, sizing, materials, construction class, and interface points. (Source: `DEL-093-02` register row; DBM SEC-06 lines 419-432 for current basis values.)

R-2.2 The vendor SHALL deliver seven (7) × 3,800 bbl produced-water tanks (5 sour + 2 sweet) as API-650 Modified atmospheric tanks, externally insulated and heated, with Devchem 253 internal coating, unless superseded by a controlled change. (Source: DBM SEC-06 lines 419-425.)

R-2.3 One (1) × 400 bbl H2O2 storage tank SHALL be delivered with the package as scoped. (Source: DBM SEC-06 line 428.)

R-2.4 The tank design specific gravity basis SHALL be confirmed against the resolved value (currently 1.25 TBC in source). The pump fluid SG (1.18) vs tank SG (1.25) discrepancy SHALL be closed in detailed design before acceptance. (Source: DBM SEC-06 line 421.)

### R-3 — Test and Inspection

R-3.1 The EPC SHALL verify that the vendor has executed and documented hydrotest, weld NDE, coating inspection (Devchem 253), and insulation/EHT functional checks per API 650 and the EPC Package Datasheet. (ASSUMPTION on test catalog scope; clause-level acceptance criteria `location TBD` — sourced from API 650 and `26020-Package_Requirements.docx` heading 45, not directly read.)

R-3.2 Test and inspection records SHALL be traceable to specific tank tags and SHALL include pass/fail disposition and signature. (ASSUMPTION on traceability convention.)

R-3.3 Cold-temperature applicability (-40 °C minimum ambient) SHALL be verified for any exposed package elements (heat tracing, insulation, instrumentation). (Source: DBM Site Basis line 145.)

### R-4 — Integration and Interfaces

R-4.1 The EPC SHALL verify and accept the following interfaces to facility systems:

- Produced-water transfer pumps (2 × 100%) suction/discharge ties. (Source: DBM SEC-06 line 429.)
- VRU header connection from tank vapours. (Source: DBM SEC-06 line 436.)
- Vacuum truck connection at assumed 2.75 m3/min per tank. (Source: DBM SEC-06 line 430.)
- H2O2 storage tank interfaces with treatment package. (Source: DBM SEC-06 line 428.)
- Electrical heat tracing, EHT power, and grounding/bonding (OBJ-005).
- Controls, instrumentation, fire/gas detection, alarm and shutdown signals (OBJ-006).
- Civil/structural foundations, secondary containment, and access (OBJ-008).

R-4.2 Each interface SHALL have an EPC sign-off (electrical, controls/I&C, civil/structural, mechanical) before final acceptance. (ASSUMPTION on multi-discipline sign-off convention.)

### R-5 — Safety, Regulatory, and Sour Service

R-5.1 Sour-service materials selection and corrosion allowances SHALL be confirmed against DBM SEC-15 specifications/codes/standards. (Source: OBJ-009; DBM SEC-15 referenced as governing — clause-level details `location TBD` in DBM section text.)

R-5.2 Aluminum SHALL NOT be present in caustic-adjacent locations (cross-package note). (Source: DBM SEC-06 line 402 — applies adjacent caustic package; carried as awareness only.)

### R-6 — Turnover Readiness

R-6.1 Mechanical completion, punch list resolution, commissioning records, and custody handoff documents SHALL be present and complete before acceptance. (Source: OBJ-010.)

R-6.2 Open items SHALL be tracked to closure with documented disposition; outstanding items at acceptance SHALL have explicit human-approved carry-over. (Source: OBJ-010.)

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| API 650 (latest applicable edition; specific edition `TBD`) | Welded tanks for oil storage — governing construction standard for the package | Referenced as "API-650 Modified" in DBM SEC-06 line 421; clause-level text `location TBD` (standard not in local source set) |
| `26020-Package_Requirements.docx` heading 45 | Project-issued package requirements (Tanks, Water API 650 3-25) | Path: `_Sources/26020-Package_Requirements.docx`; binary, not directly read — `location TBD` |
| DBM `3-25_Comp_and_Liquids_DBM.md` | Design Basis Memorandum — current facility basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| EPC Scope of Work (`DEL-093-01`), Package Datasheet (`DEL-093-02`), Construction Work Package (`DEL-093-03`) | EPC anchor deliverables governing this acceptance | Sibling deliverables in `PKG-093` |

## Verification

| Requirement | Verification Method | Evidence |
|---|---|---|
| R-1.1, R-1.2 | Documentation review against vendor register | Vendor document review log |
| R-1.3 | Cross-check against `26020-Package_Requirements.docx` vendor-document tables | Coverage matrix (ASSUMPTION on format) |
| R-2.1, R-2.2, R-2.3 | Comparison of vendor As-Designed vs EPC Package Datasheet | Conformance matrix |
| R-2.4 | Resolution-record review | Design change record / RFI closure |
| R-3.1, R-3.2 | Inspection record review; witness sign-off | ITR/inspection records, NDE reports, coating reports |
| R-3.3 | Cold-service compliance check | Vendor declaration + EPC review note |
| R-4.1, R-4.2 | Interface walkdown + multi-discipline sign-off | Interface acceptance form (ASSUMPTION on form name) |
| R-5.1 | Material/MTR review against DBM SEC-15 | MTR set, vendor compliance declaration |
| R-6.1, R-6.2 | Turnover package review | MC certificates, punch list, commissioning records, open-item register |

## Documentation

The deliverable produces these artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- `Vendor document review log` — per R-1
- `Package acceptance checklist` — per R-2 through R-5
- `Test and inspection evidence pack` — per R-3
- `Turnover evidence pack` — per R-6
- `Integration interface acceptance record` — per R-4
- `Open-item register and dispositions` — per R-6.2

Exact artifact formats are `TBD` pending the EPC document control convention for this project (not extracted from accessible local sources).
