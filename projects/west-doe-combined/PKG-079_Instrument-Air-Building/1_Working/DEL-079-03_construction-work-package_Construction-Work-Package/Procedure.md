# Procedure — DEL-079-03 Construction Work Package (Instrument Air Building)

> Operational procedure for producing the Construction Work Package artifact for PKG-079 and for using it at the field workface.

## Purpose

Produce the Construction Work Package, its workface installation/tie-in plan, and its construction interface and turnover checklist, so the PKG-079 Instrument Air Building skid can be received, installed on piles (by others), tied in, electrically connected (by others), inspected, tested, and turned over to acceptance (DEL-079-06).

## Prerequisites

| Item | Status | Source / Note |
|---|---|---|
| DEL-079-01 Scope of Work issued | Required upstream (ASSUMPTION) | DELIVERABLE_REGISTER row DEL-079-01; _DEPENDENCIES.md declares no edges |
| DEL-079-02 Package Datasheet issued | Required upstream (ASSUMPTION) | DELIVERABLE_REGISTER row DEL-079-02 |
| DEL-079-04 Vendor Engineered Equipment Package general arrangement available | Required for tie-in elevations and pile loads (ASSUMPTION) | DELIVERABLE_REGISTER row DEL-079-04; SCOPE_LEDGER SOW-0133 "sized by vendor" items |
| Pile design and schedule from foundation party | Required for set sequencing | SCOPE_LEDGER SOW-0134 ("installation on piles" by others); ASSUMPTION |
| Facility tie-in points identified | Required for piping and electrical scope | SCOPE_LEDGER SOW-0134; ASSUMPTION on availability |
| Site access, lay-down, and lift plan basis | Required | TBD |
| Project mechanical, piping, and electrical construction standards | Required | TBD |
| _REFERENCES.md source materials locally accessible | Partial — decomposition snapshot accessible; 26020-Package_Requirements.docx not opened in this run | _REFERENCES.md |

## Steps

### Phase A — Produce the CWP artifact

1. **Confirm package scope basis.** Read SCOPE_LEDGER SOW-0131 through SOW-0134 and _CONTEXT.md. Reproduce equipment list, design pressures, and "by others" interface list verbatim in the CWP.
2. **Establish package boundary diagram.** Draft a single-page boundary diagram showing: vendor package boundary, EPC scope boundary, "by others" boundary for piles/piping/electrical/platform. (Source basis: SOW-0131, SOW-0134.)
3. **Define interface schedule.** For each "by others" line in SOW-0134, create one interface row with: owner, predecessor activity, successor activity, acceptance criterion, document evidence.
4. **Develop installation sequence.** Order: receive -> inspect -> set on piles -> grout -> mechanical tie-in -> electrical tie-in -> pre-commissioning -> commissioning -> acceptance.
5. **Develop workface installation and tie-in plan.** Per _CONTEXT.md Anticipated Artifacts. Include lift plan reference, isolation plan, hot/cold cut-in decisions, and test boundaries.
6. **Develop construction interface and turnover checklist.** Per _CONTEXT.md Anticipated Artifacts. Map every requirement REQ-CWP-001 through REQ-CWP-012 to one or more checklist rows.
7. **Define Inspection and Test Plan (ITP).** Include the hold points listed in REQ-CWP-007. (ASSUMPTION on hold point list; SOW does not enumerate.)
8. **Define pressure test plan.** Choose test medium, pressure, and duration consistent with system design max 1034 kPag and the governing piping code (TBD; ASSUMPTION ASME B31.3).
9. **Define electrical pre-energization plan.** Include cable megger, motor rotation bump, soft starter/VFD function check, and anti-condensation heater verification.
10. **Define delivered air quality verification.** Specify dew point test at 1000 kPag confirming -73.3 °C maximum (SOW-0133). Method TBD.
11. **Define LOTO boundary plan.** Identify every live-service tie-in and its isolation, bleed, and lockout point. (ASSUMPTION — not enumerated in source.)
12. **Issue constructability review record.** Confirm mounting platform and stairs (by others) preserve maintenance access for filter change-out, dryer service, and PSV access (ASSUMPTION).
13. **Internal review and issue.** EPC Integrator internal review; issue CWP package; move _STATUS.md to next gate when downstream review completes.

### Phase B — Use the CWP at the workface

14. **Pre-mobilization.** Confirm prerequisites (piles complete, vendor GA issued, lift plan approved).
15. **Receiving inspection.** Inspect compressors, receivers, dryer, filters per receiving checklist.
16. **Equipment set.** Set skid(s) on piles per lift plan; verify hold-down and grout.
17. **Mechanical tie-in.** Execute tie-in piping per workface plan and isolation plan.
18. **Electrical tie-in.** Pull and terminate cables; complete megger and rotation checks.
19. **Pre-commissioning.** Execute ITP hold points; energize anti-condensation heaters as soon as cables are terminated.
20. **Commissioning.** Run single-train, then dual-train; cycle dryer towers; verify dew point.
21. **Turnover.** Complete construction interface and turnover checklist; package evidence for DEL-079-06 acceptance.

## Verification

| Verification | Confirms |
|---|---|
| All requirements REQ-CWP-001..012 mapped to one or more procedural steps and one or more checklist rows | Spec/Procedure traceability |
| Pressure test record exists and pressure >= designated test pressure | REQ-CWP-003 |
| Megger, rotation, and heater verification records exist | REQ-CWP-004 |
| Dew point test record shows <= -73.3 °C at 1000 kPag | REQ-CWP-008 |
| LOTO plan signed off for each live tie-in | REQ-CWP-009 |
| Constructability review record signed | REQ-CWP-012 |
| Turnover package structure matches DEL-079-06 acceptance checklist | REQ-CWP-010 |

## Records

Records produced by execution of this procedure:

- Receiving inspection records (per equipment item)
- Pile hold-down and grout records (interface with foundation party)
- Pressure test record (tie-in piping)
- Welder qualifications and weld records for tie-in piping (ASSUMPTION — driven by piping code TBD)
- Electrical megger, continuity, and motor rotation records
- Anti-condensation heater energization log
- Dryer regeneration cycle witness record
- Delivered air dew point acceptance record
- LOTO boundary plan and execution records
- Completed construction interface and turnover checklist
- Constructability review record
- Final turnover package submitted to DEL-079-06 review
