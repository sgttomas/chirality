# Specification — DEL-097-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope

This specification governs the EPC-Integrator-led review, integration acceptance, and handoff readiness verification of the Package Vendor's deliverables for the Tanks, Condensate (API 650) 3-25 package (`PKG-097`). It defines what the EPC must verify, what evidence must be collected, and what conditions must be satisfied before the vendor package is accepted and turned over.

The acceptance set covers:

- The vendor engineered equipment package (`DEL-097-04`) — physical equipment and engineering basis;
- The vendor document turnover package (`DEL-097-05`) — vendor document register, submittals, and turnover records;
- Conformance to the EPC Scope of Work (`DEL-097-01`), EPC Package Datasheet (`DEL-097-02`), and EPC Construction Work Package (`DEL-097-03`).

### Out of scope

- Vendor-internal engineering design (owned by Package Vendor under `DEL-097-04`).
- Foundations, mounting of tanks at site, electrical/instrumentation install, platforms, staircases — explicitly "By others" per `26020-Package_Requirements.docx` heading 49 Scope Notes.
- Sales condensate LACT equipment (third-party NRM scope; facility provides tie-in only — DBM line 417).
- Pipeline scope downstream of the facility tie-in (by others, where applicable).

## Requirements

Requirements are stated as EPC-Integrator acceptance obligations. Each requirement references a source or carries a labelled `ASSUMPTION`/`TBD`.

### R-1 — Vendor Document Review

R-1.1 The EPC SHALL maintain a vendor document review log covering each item in the vendor document register produced under `DEL-097-05` and each item listed in `26020-Package_Requirements.docx` heading 49 "Vendor Engineering Deliverables". (Source: `_CONTEXT.md` Anticipated Artifacts; heading 49 Vendor Engineering Deliverables; `DEL-097-05` register row.)

R-1.2 The EPC SHALL record review status (Approved / Approved with Comments / Revise and Resubmit / Rejected) and disposition for each vendor document. (ASSUMPTION: status-set convention; clause-level convention `location TBD`.)

R-1.3 Vendor documents listed under heading 49 Vendor Engineering Deliverables SHALL be confirmed present, reviewed, and dispositioned before acceptance. The full list includes (non-exhaustively): PRQ-009 Vendor Document Index; DOC-008 Vendor Document Control Procedure; QLT-006 Supplier Quality Plan; QLT-003 Inspection and Test Plan (ITP); QLT-013 Material Test Reports / Certificates; QLT-020 Inspection Release Certificate; QLT-021 Manufacturing Record Book / Vendor Data Book; PRQ-013 Logistics / Shipping Plan; PRQ-015 SPIR; PRQ-016 Vendor Data Book / Final Supplier Documentation; MEC-001 through MEC-025 (core package engineering plus storage-tank specifics MEC-005, MEC-011); PRO-014 through PRO-018 (relief/flare/vent); PIP-003 through PIP-028 (piping interfaces); PRO-023, CIV-014 (drainage / containment); ELE-012, ELE-017, ELE-019 (electrical/lighting/grounding); PLN-015, PLN-016 (cathodic protection); INS-002 through INS-029, CTL-003, CTL-005, CTL-006, CTL-026 (instrumentation and controls); STR-001 through STR-020 (structural); CIV-003, CIV-004, CIV-015, CIV-019 (civil grading / spill containment). (Source: `26020-Package_Requirements.docx` heading 49 Vendor Engineering Deliverables.)

### R-2 — Conformance to EPC Anchor Deliverables

R-2.1 The EPC SHALL verify the vendor engineered equipment package (`DEL-097-04`) conforms to the EPC Package Datasheet (`DEL-097-02`) for equipment count, sizing, materials, construction class, and interface points. (Source: `DEL-097-02` register row; heading 49 Basic Scope and Major Included Equipment.)

R-2.2 The vendor SHALL deliver four (4) × 3,800 bbl C5+ Condensate Product Storage Tanks built to Modified API 650 as non-insulated atmospheric tanks with internal coating (Devchem 253) on floors, walls, and roof, blanket gas system per API 2000, and each tank fitted with PVRV (vacuum or modulating pressure relief), EPRV (single worst-case relief), VRU header connection, and blanket gas connection, unless superseded by a controlled change. (Source: heading 49 Basic Scope; Major Included Equipment.)

R-2.3 Tank nozzles SHALL be sized so that plant design capacity can fill a single tank; maximum fill SHALL be limited to 90 % shutdown. (Source: heading 49 Major Included Equipment.)

R-2.4 Preliminary design throughput (94,940 kg/h / 3,187 Am3/d) and operating envelope (Atmospheric ambient pressure; 0 °C to 40 °C operating; 32 oz design test pressure; -40 °C to 60 °C design temperature) SHALL be verified for the as-built/as-designed equipment. (Source: heading 49 Scope Notes / Open Items.)

R-2.5 If a winter recycle is required to maintain a minimum temperature, the vendor SHALL describe the provision and the EPC SHALL verify it. (Source: heading 49 Major Included Equipment — "a recycle may be required to maintain a certain temperature during winter".)

### R-3 — Test and Inspection

R-3.1 The EPC SHALL verify that the vendor has executed and documented hydrotest, weld NDE, coating inspection (Devchem 253), pressure/vacuum-relief device (PVRV/EPRV) function tests, and blanket-gas system function tests per API 650, API 2000, and the EPC Package Datasheet. (ASSUMPTION on test catalog scope; clause-level acceptance criteria `location TBD` — API 650 and API 2000 standards not in local source set.)

R-3.2 Test and inspection records SHALL be traceable to specific tank tags and SHALL include pass/fail disposition and signature. (ASSUMPTION on traceability convention.)

R-3.3 Cold-temperature applicability (-40 °C minimum ambient and -40 °C minimum design) SHALL be verified for any exposed package elements (instrumentation, relief devices, valves, blanket-gas controls). (Source: heading 49 Scope Notes — design temperature -40 °C min; DBM Site Basis.)

### R-4 — Integration and Interfaces

R-4.1 The EPC SHALL verify and accept the following interfaces per heading 49 Physical Interface Summary (only interfaces marked **Yes** in the source slice are in scope for active acceptance):

- Process Piping;
- Relief / Flare / Vent (PVRV/EPRV discharge routing, VRU header tie-in);
- Drain / Containment;
- Area / Exterior Lighting;
- Grounding / Bonding;
- Cathodic Protection;
- I&C / Control Cabling;
- Grading / Site Drainage / Spill Containment;
- Structural / Foundations / Supports.

Interfaces marked **No** in the source slice (Utility Piping; Electrical Power; EHT; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Product Loading; Pipeline / Pigging) are not active acceptance items for this package and SHALL be confirmed as non-applicable in the acceptance record. (Source: heading 49 Physical Interface Summary.)

R-4.2 Each in-scope interface SHALL have an EPC discipline sign-off (mechanical, electrical, controls/I&C, civil/structural) before final acceptance. (ASSUMPTION on multi-discipline sign-off convention.)

R-4.3 The "Interface Coordination Notes" item is marked **TBD** in the source slice; the EPC SHALL resolve and record coordination notes prior to acceptance, or capture an explicit human-approved carry-over. (Source: heading 49 Interface Coordination Notes.)

### R-5 — Safety, Regulatory, and Service-Specific Items

R-5.1 Material selection and corrosion allowances for sweet C5+ condensate service with residual H2S exposure pathways SHALL be confirmed against project material specifications. (Source: DBM Liquids Hub material basis; clause-level details `location TBD`.)

R-5.2 Blanket gas system design SHALL be confirmed against API 2000 (clause-level details `location TBD` — standard not in local source set). (Source: heading 49 Major Included Equipment.)

R-5.3 Internal coating (Devchem 253) SHALL be confirmed by vendor coating reports against the coating specification. (Source: heading 49 Major Included Equipment.)

### R-6 — Turnover Readiness

R-6.1 Mechanical completion, punch list resolution, commissioning records, and custody handoff documents SHALL be present and complete before acceptance. (Source: OBJ-010.)

R-6.2 Open items SHALL be tracked to closure with documented disposition; outstanding items at acceptance SHALL have explicit human-approved carry-over. (Source: OBJ-010.)

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| API 650 (Modified; specific edition `TBD`) | Welded tanks for oil storage — governing construction standard | Referenced as "modified API 650" in `26020-Package_Requirements.docx` heading 49 Major Included Equipment; clause-level text `location TBD` (standard not in local source set) |
| API 2000 (specific edition `TBD`) | Pressure/vacuum venting and blanket gas system basis | Referenced in heading 49 Major Included Equipment; clause-level text `location TBD` (standard not in local source set) |
| `26020-Package_Requirements.docx` heading 49 | Project-issued package requirements (Tanks, Condensate — `26020-03-PT-19-006`) | Path: `_Sources/26020-Package_Requirements.docx`; source slice extracted |
| DBM `3-25_Comp_and_Liquids_DBM.md` | Design Basis Memorandum — current facility basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| EPC Scope of Work (`DEL-097-01`), Package Datasheet (`DEL-097-02`), Construction Work Package (`DEL-097-03`) | EPC anchor deliverables governing this acceptance | Sibling deliverables in `PKG-097` |
| Coating spec — Devchem 253 | Internal coating basis (floors, walls, roof) | Named in heading 49 Major Included Equipment; product datasheet not in local source set — `location TBD` |

## Verification

| Requirement | Verification Method | Evidence |
|---|---|---|
| R-1.1, R-1.2, R-1.3 | Documentation review against vendor register and against heading 49 Vendor Engineering Deliverables list | Vendor document review log; coverage matrix |
| R-2.1, R-2.2, R-2.3 | Comparison of vendor As-Designed vs EPC Package Datasheet | Conformance matrix |
| R-2.4 | Operating-envelope verification against vendor data sheets / calculation package | Vendor calculation package (MEC-014); Storage Tank Data Sheets (MEC-011) |
| R-2.5 | Winter recycle provision design review | Vendor design narrative / P&IDs (PRO-008) |
| R-3.1, R-3.2 | Inspection record review; witness sign-off at hold points | Hydrotest report; NDE reports; coating reports; relief-device function test reports; blanket-gas function test reports |
| R-3.3 | Cold-service compliance check | Vendor declaration + EPC review note |
| R-4.1, R-4.2 | Interface walkdown + multi-discipline sign-off; non-applicable interfaces confirmed | Interface acceptance form (ASSUMPTION on form name) |
| R-4.3 | Coordination-note resolution review | Updated coordination note record or carry-over approval |
| R-5.1 | Material/MTR review against project material specs | MTR set (QLT-013); vendor compliance declaration |
| R-5.2 | Blanket gas system design review against API 2000 | Vendor calc / data sheets; reviewer note on clause coverage (clauses `location TBD`) |
| R-5.3 | Coating report review | Coating QC reports |
| R-6.1, R-6.2 | Turnover package review | MC certificates; punch list; commissioning records; open-item register |

## Documentation

The deliverable produces these artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- `Vendor document review log` — per R-1
- `Package acceptance checklist` — per R-2 through R-5
- `Test and inspection evidence pack` — per R-3
- `Turnover evidence pack` — per R-6
- `Integration interface acceptance record` — per R-4
- `Open-item register and dispositions` — per R-4.3, R-6.2

Exact artifact formats are `TBD` pending the EPC document control convention for this project (not extracted from accessible local sources).
