# Specification — DEL-079-03 Construction Work Package (Instrument Air Building)

> Normative requirements the Construction Work Package (CWP) artifact for PKG-079 must satisfy.

## Scope

### In scope
- Define how the PKG-079 Instrument Air Building package will be physically installed, built, inspected, turned over, and tied into the larger facility systems (per _CONTEXT.md Scope).
- Cover SOW-0131 through SOW-0134 as the scope basis (per _CONTEXT.md and SCOPE_LEDGER).
- Specify constructability, workface execution, and turnover content for the EPC Integrator role.

### Out of scope
- Vendor engineering and equipment design (DEL-079-04 — Vendor Engineered Equipment Package).
- EPC package Scope of Work narrative (DEL-079-01).
- EPC Package Datasheet content (DEL-079-02).
- Vendor document turnover register itself (DEL-079-05).
- EPC review and acceptance evidence (DEL-079-06).
- Items explicitly marked "by others" in SOW-0134 are out of scope for performance, but the CWP MUST define the interface so those parties can execute.

## Requirements

| Req ID | Requirement | Source / Rationale |
|---|---|---|
| REQ-CWP-001 | The CWP SHALL describe the installation sequence for all major included equipment listed in SOW-0133 (2 compressors, 1 wet air receiver, 2 dryer pre-filters, 1 regenerative desiccant dryer, 1 after-filter, 1 dry air receiver or two 50%). | SCOPE_LEDGER SOW-0133 |
| REQ-CWP-002 | The CWP SHALL define the interface with the "by others" scope identified in SOW-0134: shipping to site, installation on piles, tie-in piping, electrical connections, mounting platform, and stairs. | SCOPE_LEDGER SOW-0134 |
| REQ-CWP-003 | Tie-in piping work SHALL be planned to respect the system design pressures defined in SOW-0133/0134: PSV set 948 kPag; max system design pressure 1034 kPag; min system pressure 551 kPag; facility shutdown 482 kPag; design temperature -40 °C to 38 °C. | SCOPE_LEDGER SOW-0133, SOW-0134 |
| REQ-CWP-004 | Electrical work SHALL be planned for 2 x 250 HP, 600 V / 3 PH / 60 Hz, TEFC, Non-classified motors with soft starter or VFD-ready provisions and anti-condensation space heaters. | SCOPE_LEDGER SOW-0133, SOW-0134 |
| REQ-CWP-005 | The CWP SHALL include a workface installation and tie-in plan as a discrete artifact (per _CONTEXT.md Anticipated Artifacts). | _CONTEXT.md Anticipated Artifacts |
| REQ-CWP-006 | The CWP SHALL include a construction interface and turnover checklist as a discrete artifact (per _CONTEXT.md Anticipated Artifacts). | _CONTEXT.md Anticipated Artifacts |
| REQ-CWP-007 | The CWP SHALL identify inspection and test holds covering at minimum: equipment receiving inspection, pile/foundation hold-down verification (interface with "by others"), pressure test of tie-in piping, electrical megger and motor rotation verification, and dryer regeneration cycle witnessing. | ASSUMPTION — standard EPC instrument air package practice; SOW does not enumerate hold points (location TBD) |
| REQ-CWP-008 | Delivered air quality acceptance SHALL include verification that delivered instrument air meets maximum dew point -73.3 °C at 1000 kPag, with the test method TBD. | SCOPE_LEDGER SOW-0133; test method TBD |
| REQ-CWP-009 | The CWP SHALL identify lockout/tagout boundaries for tie-in to live facility services where applicable. | ASSUMPTION — standard practice; not stated in source slice |
| REQ-CWP-010 | The CWP SHALL include a turnover package structure compatible with DEL-079-06 (EPC Vendor Package Review and Acceptance) including receipt of vendor document turnover (DEL-079-05). | DELIVERABLE_REGISTER rows DEL-079-05, DEL-079-06; ASSUMPTION on handoff structure |
| REQ-CWP-011 | The CWP SHALL define a hazardous-area boundary statement consistent with the non-classified motor selection. | SCOPE_LEDGER SOW-0134; ASSUMPTION on boundary documentation requirement |
| REQ-CWP-012 | The CWP SHALL include a constructability review record verifying that mounting platform and stairs (by others) are coordinated with equipment maintenance access, filter change-out clearances, and dryer service. | ASSUMPTION — derived from SOW-0134 "by others" mounting platform/stairs scope |

## Standards

- Workbook Packages row 69 (26020-Packages_Interfaces_4_export.xlsx) — package definition basis. Location: workbook row level (clause text TBD).
- 26020-Package_Requirements.docx package heading 32 — Basic scope; Major included equipment; Scope notes and open items. Location TBD (not opened in this run; cited via SCOPE_LEDGER extraction).
- Project mechanical and electrical construction standards — TBD (not enumerated in accessible decomposition slice).
- Applicable pressure piping code for tie-in piping (e.g., ASME B31.3) — ASSUMPTION; location TBD.
- Applicable electrical code for motor terminations and cable installation — ASSUMPTION; location TBD.

## Verification

| Req | Verification approach |
|---|---|
| REQ-CWP-001 | Review CWP installation sequence against SOW-0133 equipment list; checklist confirmation. |
| REQ-CWP-002 | Review CWP interface schedule and confirm each "by others" item from SOW-0134 has a defined interface row. |
| REQ-CWP-003 | Review pressure test plan against SOW-0133/0134 design pressures; witness pressure test. |
| REQ-CWP-004 | Review electrical scope and motor data sheet alignment; witness megger and motor rotation. |
| REQ-CWP-005 | Confirm workface installation and tie-in plan exists in the CWP folder. |
| REQ-CWP-006 | Confirm construction interface and turnover checklist exists in the CWP folder. |
| REQ-CWP-007 | Confirm CWP enumerates the listed hold points; verify each hold against execution records. |
| REQ-CWP-008 | Witness dew point test; record dew point reading at 1000 kPag. Method TBD. |
| REQ-CWP-009 | Review LOTO plan for each live-system tie-in. |
| REQ-CWP-010 | Cross-reference CWP turnover structure with DEL-079-06 acceptance checklist. |
| REQ-CWP-011 | Confirm hazardous-area boundary statement and rationale present. |
| REQ-CWP-012 | Confirm constructability review record exists and addresses maintenance access. |

## Documentation

The Construction Work Package shall include the following documents (from _CONTEXT.md Anticipated Artifacts plus derived items):

- Construction Work Package (primary artifact)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Inspection and test plan (ITP) — ASSUMPTION; derived from REQ-CWP-007
- Pressure test plan and records — ASSUMPTION; derived from REQ-CWP-003
- Electrical pre-energization and motor solo-run records — ASSUMPTION; derived from REQ-CWP-004
- Dew point acceptance test record — ASSUMPTION; derived from REQ-CWP-008
- LOTO boundary plan — ASSUMPTION; derived from REQ-CWP-009
- Constructability review record — ASSUMPTION; derived from REQ-CWP-012
