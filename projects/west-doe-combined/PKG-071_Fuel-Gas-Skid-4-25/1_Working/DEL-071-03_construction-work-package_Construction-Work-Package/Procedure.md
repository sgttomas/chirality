# Procedure — DEL-071-03 Construction Work Package (Fuel Gas Skid 4-25)

This Procedure describes how to **produce** the Construction Work Package artifact set for the Fuel Gas Skid (`26020-01-PT-23-001`, 4-25 West Doe Deepcut) and to **use** it during construction execution.

## Prerequisites

- Approved upstream deliverables:
  - DEL-071-01 Scope of Work (SOW-0099–SOW-0102) — source: `_CONTEXT.md` Covers Scope Items.
  - DEL-071-02 Package Datasheet — source: `DELIVERABLE_REGISTER.csv`.
- Vendor-released engineering set per `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables, sufficient to define foundations, tie-ins, and electrical/I&C terminations (specifically MEC-016, MEC-017, STR-005, STR-006, STR-013, PIP-004, PIP-006, PIP-007, INS-008, INS-009, INS-010, INS-011, ELE-019, ELE-029).
- Facility-level inputs (location TBD): facility piping code edition, hazardous area classification, F&G philosophy (TSF-002), grounding standard, and as-built procedure.
- Resolution of the Electrical Power applicability conflict — see `Guidance.md` Conflict Table, CONF-FGS-CWP-01.

## Steps

### Phase A — Produce the CWP artifacts (planning)

1. **Read the source slice.** Open `_Sources/26020-Package_Requirements.docx`, Heading 1 `26020-01-PT-23-001 - Fuel Gas Skid` (4-25 West Doe Deepcut instance). Capture: Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables. (Source: same.)
2. **Confirm interface applicability.** Build a working table mirroring the Physical Interface Summary. Flag every "Yes" as in-scope construction work. (Source: same.)
3. **Surface conflicts.** Cross-check Major Included Equipment against the Physical Interface Summary; record any mismatch in `Guidance.md` Conflict Table. (Source: same.)
4. **Draft the Construction Work Package narrative.** Sections at minimum: package identity; site/facility; receipt and set; foundations; piping tie-ins (process, utility, relief, drain); electrical (post-conflict ruling); I&C; F&G; grounding; lighting; structural and access; testing and FAT/SAT sequence; as-built capture; turnover.
5. **Draft the Installation and Tie-In Workface Plan.** Sequence the work scope items SOW-0099–SOW-0102 (from `_CONTEXT.md` Covers Scope Items) against each "Yes" interface row, including resource, duration, and predecessor links. Mark heater electrical tie-in as on hold pending conflict ruling.
6. **Draft the Construction Interface and Turnover Checklist.** One row per interface per Physical Interface Summary row; verification evidence column; sign-off column.
7. **Internal QA.** Confirm: every "Yes" interface row appears in at least one of the three artifacts; every vendor deliverable referenced has an inbound action; every TBD/ASSUMPTION is flagged.
8. **Issue for review.** Move the three artifacts into review per the EPC Integrator review workflow (DEL-071-06 review and acceptance precondition).

### Phase B — Use the CWP during construction (execution)

1. **Site receipt.** Off-load the skid; verify shipping damage condition; record per QLT-020 Inspection Release Certificate inputs. (Source: `_Sources/26020-Package_Requirements.docx`, Vendor Engineering Deliverables — Core vendor documents.)
2. **Foundations.** Pour and cure foundations per STR-005/STR-006; verify anchor positions per STR-013 prior to set. (Source: same — Structural.)
3. **Set skid.** Lift and set per STR-014 lifting analysis and MEC-018 lifting/handling study; survey skid position; grout/shim per vendor instructions. (Source: same — Mechanical and Structural.)
4. **Structural and access install.** Install STR-002 GA secondary steel, STR-011 platforms/ladders, STR-012 module structures. (Source: same — Structural.)
5. **Piping tie-ins (process, utility, relief, drain).** Fabricate and install per PIP-006/PIP-007/PIP-008/PIP-009 and PIP-004 Tie-In List. Hydrotest per PIP-024; flush/dry per PIP-025. Record as-builts per PIP-028. (Source: same — Process piping.)
6. **Drainage tie-ins.** Connect package drains to facility closed drain per PRO-023 / CIV-014 boundaries. (Source: same — Drainage/containment.)
7. **Grounding and bonding.** Install per ELE-019. Test earth resistance and record. (Source: same — Electrical.)
8. **Lighting at package.** Install per facility ELE-017 layout; reconcile interface file row reference per `Guidance.md` CONF-FGS-CWP-02 before quantity take-off. (Source: same — Electrical.)
9. **Electrical tie-in (heater 600 V SCR feed).** Execute only after CONF-FGS-CWP-01 ruling. Cable sizing per facility electrical engineering inputs and MEC-014 calculation outputs; terminate per ELE-028. (Sources: same — Electrical; conflict surfaced in `Guidance.md`.)
10. **I&C cabling and terminations.** Pull cable per INS-011, terminate per INS-009/INS-010, loop-check per INS-008. (Source: same — Instrumentation.)
11. **Fire & gas.** Install detectors per TSF-004; commission per TSF-003 mapping outputs; reconcile to facility TSF-002 philosophy before energization. (Source: same — Fire and gas.)
12. **Electrical FAT/SAT and energization.** Per ELE-029; record per ELE-030. (Source: same — Electrical.)
13. **Mechanical FAT.** Execute per MEC-021; record per MEC-022. (Source: same — Mechanical.)
14. **Turnover.** Complete every row of the Construction Interface and Turnover Checklist; resolve all open punch items; hand documentation to DEL-071-06 review and acceptance.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| All three CWP artifacts produced | Document inventory at the deliverable folder | Datasheet, Specification, Guidance, Procedure plus the three EPC artifacts named in `_CONTEXT.md` Anticipated Artifacts |
| All Physical Interface Summary "Yes" rows are addressed | Cross-table from interface row → workface plan task → turnover checklist row | 100% coverage |
| Conflict log resolved before fabrication | Conflict Table in `Guidance.md` shows human ruling for CONF-FGS-CWP-01 and CONF-FGS-CWP-02 | Both rows resolved |
| Vendor test/inspection deliverables fed back | PIP-024, PIP-025, ELE-029, ELE-030, MEC-021, MEC-022, INS-008 loop check records collected | Records present in turnover package |
| As-builts complete | PIP-028 and INS-029 issued; structural as-builts captured | All issued |
| Source rereads recorded | Run record `## Outputs Produced` cites which source slices were consulted | Recorded |

## Records

- Foundation inspection report (per STR-006).
- Hydrotest packages (PIP-024 outputs).
- Flushing/drying certificates (PIP-025 outputs).
- Loop check records (INS-008).
- F&G commissioning records (TSF-003/TSF-004).
- Earth resistance test records (ELE-019).
- Lighting commissioning record (ELE-017).
- Structural turnover walkdown record (STR-002/STR-011).
- Electrical energization package (ELE-029/ELE-030).
- Mechanical FAT report (MEC-022).
- Piping as-built drawings (PIP-028).
- Instrument as-built drawings (INS-029).
- Construction Interface and Turnover Checklist with sign-offs (this deliverable's artifact).
- Conflict-ruling records for CONF-FGS-CWP-01 and CONF-FGS-CWP-02.
