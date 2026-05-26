# Procedure — DEL-073-03 Construction Work Package (PKG-073 Amine Treating Unit)

## Purpose

This procedure describes how the EPC Integrator **produces** the Construction Work Package (CWP) deliverable for PKG-073 — including the workface plan and the construction interface/turnover checklist — and how the CWP is then **used** during field execution to install, inspect, and turn over the Amine Treating Unit. (Interpretation: per skill `four-documents` interpretation rule, this Procedure covers both production and use, given deliverable type and source availability.)

## Prerequisites

- **Upstream deliverables (declared):** none in `_DEPENDENCIES.md` at PREPARATION. The CWP nonetheless depends in practice on:
  - DEL-073-01 Scope of Work (SoW) — sufficient maturity to define package boundaries and SOW items SOW-0051..SOW-0054.
  - DEL-073-02 Package Datasheet — vendor handoff datasheet defining technical interfaces.
  - DEL-073-04 Vendor Engineered Equipment Package — at minimum, vendor general arrangement, P&IDs, and equipment list available for tie-in planning.
  (Source: DELIVERABLE_REGISTER rows 258–261. ASSUMPTION: practical sequencing requirement; specific maturity gate TBD.)
- **References available:** `_REFERENCES.md` source set, including `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (locally accessible) and `_Sources/26020-Package_Requirements.docx` package heading 27 (binary; clause-level extraction TBD).
- **Decomposition snapshot:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (PACKAGE_REGISTER PKG-073, DELIVERABLE_REGISTER row 260).
- **Site / facility basis:** 04-25 Deepcut Gas Plant; design ambient -40 °C to +35 °C; cold-climate constructability constraints. (Source: DBM-Deepcut Sec. 2.)
- **Roles:** EPC Integrator (lead authoring and field execution); Package Vendor (information provider; supports vendor-internal scope queries); Owner / facility operations (turnover acceptor).

## Steps

### Part A — Produce the CWP deliverable set

1. **Confirm scope.** Read `_CONTEXT.md` and PROJECT_DECOMP PKG-073 row; confirm SoW items SOW-0051..SOW-0054 and interface-type list are still current.
2. **Assemble engineering basis.** Collect the latest vendor general arrangement, P&IDs, equipment list, and interface drawings from DEL-073-04 (and EPC piping/electrical/I&C/structural specifications). Cross-reference the equipment tag list against the DBM-Deepcut "Amine Treating Unit" equipment row.
3. **Draft the CWP body.** Populate scope, equipment register, tie-in register (by interface type), construction methods, inspection plan, NDE plan, testing plan, and turnover-evidence plan against REQ-CWP-01..13 in `Specification.md`.
4. **Draft the workface plan.** Sequence crews, lay-down, crane plans, hot-work and SIMOPS coordination, and constraint sign-off log. (Detailed contents per REQ-CWP-09; specific format TBD against EPC execution standards.)
5. **Draft the construction interface and turnover checklist.** Build the mechanical completion punch-list template, NDE/PWHT record list, instrument loop-check record list, electrical record list, interface signoff list, and turnover witness sign-off form. (Per REQ-CWP-10.)
6. **Cross-check against vendor responsibilities.** Confirm that no field-rework provision encroaches on vendor design ownership (DEL-073-04) or vendor turnover documentation ownership (DEL-073-05) without going through a documented change record. (Source: PROJECT_DECOMP PKG-073 ownership split.)
7. **Internal review and human approval.** EPC Integrator reviewers approve the CWP, workface plan, and checklist. Approval is human-author only per `K-AUTH-1`.

### Part B — Use the CWP during field execution

8. **Mobilize per approved workface plan.** Issue work packs in sequence; verify lay-down, crane access, hot-work coordination, and SIMOPS constraints are met before each work pack opens.
9. **Install vendor package and tie-ins.** Set equipment per drawings; complete tie-ins per interface type (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). (Source: PROJECT_DECOMP PKG-073.)
10. **Inspect and test.** Execute ITPs, NDE, PWHT where required, hydrotest/leak-test per pressure-test plan (test pressures/media TBD), megger/continuity electrical checks, and instrument loop checks.
11. **Cold-weather and EHT readiness.** Confirm cold-weather welding qualifications, hydrotest freeze management, and EHT installation acceptance per REQ-CWP-11 before exposing assets to ambient extremes.
12. **Close punch list.** Walkdown by EPC integrator and (where required) owner/operations; close A-list items before mechanical completion (MC); document B-list items with closure plans.
13. **Mechanical completion (MC) sign-off.** Issue MC certificate when the turnover checklist is closed out and all turnover evidence is collected.
14. **Handoff to commissioning.** Transfer the turnover dossier (mechanical, electrical, instrumentation, NDE, test records) to commissioning, with reference to the vendor turnover dossier produced under DEL-073-05 and accepted under DEL-073-06. (Source: DELIVERABLE_REGISTER rows 262–263.)

## Verification

| Step | Verification Check | Evidence |
|---|---|---|
| 1 | Scope confirmation aligns with current PROJECT_DECOMP PKG-073 row and `_CONTEXT.md`. | Scope confirmation memo. |
| 2 | Vendor engineering basis collected from DEL-073-04 is at the required maturity. | Document register snapshot. |
| 3 | Each REQ-CWP-01..13 traced in CWP body. | REQ traceability matrix. |
| 4 | Workface plan covers crew, lay-down, crane, hot-work, SIMOPS, sign-off. | Approved workface plan. |
| 5 | Turnover checklist covers all evidence categories. | Approved turnover checklist. |
| 6 | No CWP item infringes on vendor design ownership. | Reviewer sign-off. |
| 7 | Approval signed by an authorized human reviewer. | Signed approval. |
| 8 | Each work pack release authorized before issue. | Work-pack release log. |
| 9 | Tie-ins complete per interface-type checklist. | Tie-in completion records. |
| 10 | ITP/NDE/PWHT/pressure-test/electrical/loop records collected. | Test packs and ITP records. |
| 11 | Cold-weather, freeze, and EHT records collected per environmental envelope. | WPS/PQR, freeze-management log, EHT acceptance record. |
| 12 | A-list items closed before MC; B-list items have closure plans. | Punch-list register. |
| 13 | MC certificate issued and signed. | MC certificate. |
| 14 | Turnover dossier accepted by commissioning; coordinated with DEL-073-05 / DEL-073-06. | Turnover acceptance record (DEL-073-06 evidence). |

## Records

The Procedure produces or consumes the following records (which are also the deliverable's anticipated artifacts and supporting evidence):

- **Deliverable artifacts (carried in DEL-073-03):**
  - Construction work package (the body document).
  - Installation and tie-in workface plan.
  - Construction interface and turnover checklist.
- **Supporting execution records (carried as evidence; managed under EPC document control):**
  - Equipment tag and tie-in register; REQ-CWP traceability matrix.
  - ITP records, NDE/PWHT records, weld registers, WPS/PQR.
  - Pressure / leak-test packs.
  - Electrical megger/continuity records.
  - Instrument loop-check records.
  - Cold-weather welding and EHT installation acceptance records.
  - Punch-list register (A/B lists).
  - Mechanical completion (MC) certificate.
  - Turnover dossier transmittal record to commissioning (cross-referenced to DEL-073-05 / DEL-073-06).

Approvals on this deliverable and on each MC/turnover record are **human-author only**; this Procedure must not assign agent-authored approvals (per `K-AUTH-1`).
