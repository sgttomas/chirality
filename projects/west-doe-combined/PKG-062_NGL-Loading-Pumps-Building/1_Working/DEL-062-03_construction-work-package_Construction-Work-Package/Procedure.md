# Procedure — DEL-062-03 Construction Work Package (NGL Loading Pumps Building)

## Purpose

This procedure describes the steps to **produce** the Construction Work Package deliverable for PKG-062 NGL Loading Pumps Building and the high-level sequence to **use** it during construction execution. The artifact set produced is: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist (source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row 422).

## Prerequisites

- Accepted snapshot of DEL-062-01 EPC Scope of Work for PKG-062 (source: `DELIVERABLE_REGISTER.csv` row 420). (No declared upstream in `_DEPENDENCIES.md`; recorded as ASSUMPTION.)
- Accepted snapshot of DEL-062-02 Package Datasheet for PKG-062 (source: `DELIVERABLE_REGISTER.csv` row 421). (ASSUMPTION.)
- Access to the accepted decomposition snapshot `GATE-07_Final_Published_2026-05-24` (source: `_REFERENCES.md`).
- Access to `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` for package identity, equipment tags, and grounding rule (source: `_REFERENCES.md`; lines 73, 2549, 2610, 2993).
- Access to `_Sources/26020-Package_Requirements.docx` package heading 16 for package-level construction requirements (source file present; text not locally accessible — required for full source-grounding; location TBD).
- Access to `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 76 for package interface counterparts (source file present; text not locally accessible; TBD).
- Project construction specifications and ITPs (TBD — not in locally accessible sources).

## Steps

### Production of the deliverable

1. **Confirm package identity and equipment list.** Verify from `_CONTEXT.md` and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2549 and 2610 that the package is "NGL Loading Pumps Building" with pump tags P-9510-1, P-9520-1, P-9530-1, P-9540-1 (rotary vane) in LSD 4-25.
2. **Compile the construction work package narrative.** Capture the EPC Integrator description of how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems (source: `_CONTEXT.md` Scope statement).
3. **Build the installation and tie-in workface plan.** For each discipline (civil/structural, mechanical/piping, electrical, instrumentation, HVAC), state work-front packages, sequencing, and crew interfaces. Mark any discipline content as `TBD` where source data is not locally accessible.
4. **Build the construction interface and turnover checklist.** List interfaces to PKG-058 NGL Booster and Transfer Pumps Building (source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2548) and to truck-loading facilities. Include grounding interface to the facility main ground grid (source: line 2993; ASSUMPTION on extending the rule to the loading-pumps building). Mark counterpart tag IDs as `TBD` where interface workbook content is not locally accessible.
5. **Link requirements to verification.** For each REQ-CWP-NN in `Specification.md`, list the verification approach and where the evidence will be captured (inspection record, ITR, walk-down checklist, document review record).
6. **Cross-check terminology and values.** Ensure equipment tags, pump count, and package name match `Datasheet.md`, `Specification.md`, and `Guidance.md` exactly.
7. **Issue the deliverable for review.** Hand off to the EPC vendor package review and acceptance flow (DEL-062-06) as part of the Gate-5 readiness check (source: `DELIVERABLE_REGISTER.csv` row 425; ASSUMPTION on flow).

### Use of the deliverable during construction

8. **Mobilize per workface plan.** Construction supervision shall sequence civil/structural, building enclosure, equipment setting, piping tie-ins, electrical/instrumentation hook-up, and HVAC commissioning as defined in the workface plan.
9. **Execute grounding tie-in.** Connect building and equipment grounding to the facility main ground grid in accordance with the grounding requirement (REQ-CWP-05 in `Specification.md`; source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2993).
10. **Manage interfaces continuously.** Use the construction interface and turnover checklist to track interface closure with PKG-058 and truck-loading facilities through construction.
11. **Walk down and accept.** Perform mechanical completion walk-downs against the checklist; clear punchlist items; sign turnover packages.
12. **Feed turnover documentation.** Transmit construction turnover records into the vendor document turnover register (DEL-062-05) and into the EPC vendor package review and acceptance evidence (DEL-062-06).

## Verification

| Check | Method |
|---|---|
| All four pump tags present in the work package | Document review against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610 |
| Workface plan covers each named discipline scope item | Table-of-contents review of plan against `Specification.md` REQ-CWP-03 |
| Interface checklist lists PKG-058 and truck-loading interfaces | Document review against `Guidance.md` Principle 3 and source line 2548 |
| Grounding requirement traceable | Cross-reference REQ-CWP-05 to source line 2993 |
| Turnover documentation hook to DEL-062-05/DEL-062-06 is present | Cross-reference review |
| Terminology and values consistent across four documents | Cross-document scan |
| Objective coverage statement present and traceable | Cross-reference against `OBJECTIVE_SCOPE_MAP.csv` (PKG-062 rows) |

## Records

- Construction work package document (primary artifact, EPC Integrator-controlled)
- Installation and tie-in workface plan
- Construction interface and turnover checklist (signed)
- Mechanical completion walk-down records and punchlists
- Grounding continuity test records
- Turnover transmittal records to DEL-062-05 / DEL-062-06
