# Specification — DEL-094-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope

This specification governs the EPC-Integrator-led review, integration acceptance, and handoff readiness verification of the Package Vendor's deliverables for the Tanks, Caustic (API 650) 3-25 package (`PKG-094`). It defines what the EPC must verify, what evidence must be collected, and what conditions must be satisfied before the vendor caustic-service tank package is accepted and turned over.

The acceptance set covers:

- The vendor engineered equipment package (`DEL-094-04`) — physical equipment and engineering basis;
- The vendor document turnover package (`DEL-094-05`) — vendor document register, submittals, and turnover records;
- Conformance to the EPC Scope of Work (`DEL-094-01`), EPC Package Datasheet (`DEL-094-02`), and EPC Construction Work Package (`DEL-094-03`).

### Out of scope

- Vendor-internal engineering design (owned by Package Vendor under `DEL-094-04`).
- The non-regenerative caustic mercaptan treating unit's process equipment outside the tank scope (contactor, pre-heater, filter, water wash) — interface only (DBM line 400).
- Incinerator package design — interface only (DBM line 402).
- Pipeline/installation work downstream of the facility riser/tie-in (by others; DBM SEC-04 line 216).
- Caustic regeneration (explicitly not part of 03-25 basis — DBM line 389).

## Requirements

Requirements are stated as EPC-Integrator acceptance obligations. Each requirement references a source or carries a labelled `ASSUMPTION`/`TBD`.

### R-1 — Vendor Document Review

R-1.1 The EPC SHALL maintain a vendor document review log covering each item in the vendor document register produced under `DEL-094-05`. (Source: `_CONTEXT.md` Anticipated Artifacts; `DEL-094-05` register row.)

R-1.2 The EPC SHALL record review status (Approved / Approved with Comments / Revise and Resubmit / Rejected) and disposition for each vendor document. (ASSUMPTION: status-set convention; clause-level convention `location TBD` in `26020-Package_Requirements.docx` heading 46.)

R-1.3 Vendor documents required by source (`26020-Package_Requirements.docx` vendor document tables — OBJ-010) SHALL be confirmed present and reviewed before acceptance. (Source reference; clause-level vendor document table not directly read — clause IDs `location TBD`.)

### R-2 — Conformance to EPC Anchor Deliverables

R-2.1 The EPC SHALL verify the vendor engineered equipment package (`DEL-094-04`) conforms to the EPC Package Datasheet (`DEL-094-02`) for equipment count, sizing, materials, construction class, vapour-space rating, and interface points. (Source: `DEL-094-02` register row; DBM lines 389-402 for current basis values.)

R-2.2 The vendor SHALL deliver the caustic-service tank set comprising 400 bbl caustic process-water, fresh-caustic, spent-caustic, and H2O2 tanks per the EPC Package Datasheet. (Source: DBM line 40; line 400. ASSUMPTION on unit count per service — one each, pending Datasheet confirmation.)

R-2.3 Fresh-caustic and spent-caustic tanks SHALL be atmospheric 32 oz vapour-space tanks with LP fuel-gas blanket, heating, and insulation. (Source: DBM line 402.)

R-2.4 The caustic solution design basis SHALL be 50 wt% NaOH/H2O with SG 1.75 (TBC in source; vendor SHALL confirm or propose a controlled change). (Source: DBM line 402.)

R-2.5 Caustic tank material selection and internal coating SHALL be confirmed against detailed design closure; DBM line 402 explicitly carries this as TBC. Aluminum SHALL NOT be used in the caustic building. (Source: DBM line 402.)

### R-3 — Test and Inspection

R-3.1 The EPC SHALL verify that the vendor has executed and documented hydrotest, weld NDE, coating/lining inspection, insulation/EHT functional checks, vapour-blanket system functional check, and flame-arrestor verification on the spent-caustic vent per API 650 and the EPC Package Datasheet. (ASSUMPTION on test catalog scope; clause-level acceptance criteria `location TBD` — sourced from API 650 and `26020-Package_Requirements.docx` heading 46, neither directly read.)

R-3.2 Test and inspection records SHALL be traceable to specific tank tags and SHALL include pass/fail disposition and signature. (ASSUMPTION on traceability convention.)

R-3.3 Cold-temperature applicability (-40 °C minimum ambient) SHALL be verified for any exposed package elements (heat tracing, insulation, instrumentation). (Source: DBM Site Basis line 145.)

R-3.4 Caustic-drain interface conditions SHALL be verified: 300# flange at the spent-caustic tank, max temp 121 °C / 250 °F TBC, min drain tank temp 80 °F, heat tracing per detailed-design closure. (Source: DBM line 493.)

### R-4 — Integration and Interfaces

R-4.1 The EPC SHALL verify and accept the following interfaces to facility systems:

- Caustic treating package process tie-ins (contactor, pre-heater, water wash, filter). (Source: DBM line 400.)
- LP fuel-gas blanket supply to fresh/spent caustic tanks. (Source: DBM line 402.)
- Spent-caustic vent path through flame arrestor to incinerator header. (Source: DBM line 402.)
- Truck-out connection at spent-caustic tank. (Source: DBM line 402.)
- Confirmation that fresh-caustic tank is NOT connected to the VRU. (Source: DBM line 402.)
- Caustic drain tie-in at 300# flange (DBM line 493).
- H2O2 tank tie-ins to the H2O2 treatment package (cross-package interface). (Source: DBM line 216.)
- Electrical heat tracing, EHT power, grounding/bonding (OBJ-005).
- Controls, instrumentation, fire/gas detection, alarm and shutdown signals (OBJ-006).
- Civil/structural foundations, secondary containment, and access — including caustic-spill containment (OBJ-008).

R-4.2 Each interface SHALL have an EPC sign-off (electrical, controls/I&C, civil/structural, mechanical) before final acceptance. (ASSUMPTION on multi-discipline sign-off convention.)

### R-5 — Safety, Regulatory, and Caustic-Service

R-5.1 Caustic-service materials selection, coating, and corrosion allowances SHALL be confirmed against DBM SEC-15 specifications/codes/standards and the embrittlement review noted at DBM line 493. (Source: OBJ-009; DBM SEC-15; line 493 — clause-level details `location TBD` in DBM section text.)

R-5.2 The aluminum exclusion (DBM line 402) SHALL be verified across vendor materials lists, including fasteners, gratings, ladders, platforms, and ancillary items in the caustic building. (Source: DBM line 402.)

R-5.3 Vapour-blanket and flame-arrestor controls SHALL be verified against the incinerator-header interface; loss-of-blanket and high-temperature scenarios SHALL be addressed in the package safety case. (Source: DBM line 402; ASSUMPTION on safety-case format — `location TBD`.)

### R-6 — Turnover Readiness

R-6.1 Mechanical completion, punch list resolution, commissioning records, and custody handoff documents SHALL be present and complete before acceptance. (Source: OBJ-010.)

R-6.2 Open items SHALL be tracked to closure with documented disposition; outstanding items at acceptance SHALL have explicit human-approved carry-over. (Source: OBJ-010.)

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| API 650 (latest applicable edition; specific edition `TBD`) | Welded tanks for oil storage — governing construction standard cited by package title; caustic-service applicability via project specifications | Referenced via package name "API 650"; clause-level text `location TBD` (standard not in local source set) |
| `26020-Package_Requirements.docx` heading 46 | Project-issued package requirements (Tanks, Caustic API 650 3-25) | Path: `_Sources/26020-Package_Requirements.docx`; binary, not directly read — `location TBD` |
| DBM `3-25_Comp_and_Liquids_DBM.md` | Design Basis Memorandum — current facility basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| EPC Scope of Work (`DEL-094-01`), Package Datasheet (`DEL-094-02`), Construction Work Package (`DEL-094-03`) | EPC anchor deliverables governing this acceptance | Sibling deliverables in `PKG-094` |

## Verification

| Requirement | Verification Method | Evidence |
|---|---|---|
| R-1.1, R-1.2 | Documentation review against vendor register | Vendor document review log |
| R-1.3 | Cross-check against `26020-Package_Requirements.docx` vendor-document tables (when retrieved) | Coverage matrix (ASSUMPTION on format) |
| R-2.1, R-2.2, R-2.3 | Comparison of vendor As-Designed vs EPC Package Datasheet | Conformance matrix |
| R-2.4, R-2.5 | Resolution-record review (SG TBC, material/coating TBC) | Design change record / RFI closure; vendor material declaration |
| R-3.1, R-3.2 | Inspection record review; witness sign-off | ITR/inspection records, NDE reports, coating reports, blanket-gas/flame-arrestor function check |
| R-3.3 | Cold-service compliance check | Vendor declaration + EPC review note |
| R-3.4 | Caustic-drain interface check | Drain interface acceptance form, temperature/heat-tracing record |
| R-4.1, R-4.2 | Interface walkdown + multi-discipline sign-off | Interface acceptance form (ASSUMPTION on form name) |
| R-5.1 | Material/MTR review against DBM SEC-15 and embrittlement guidance | MTR set, vendor compliance declaration |
| R-5.2 | Aluminum-exclusion sweep across vendor BOM and ancillary items | Materials review record |
| R-5.3 | Safety-case review for vapour blanket/flame arrestor | Vendor safety/HAZOP closure record (ASSUMPTION on format) |
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
