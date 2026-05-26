# Procedure — DEL-066-02 Package Datasheet (PKG-066 Tanks, Condensate (API 650) 4-25)

## Purpose

This Procedure documents how the EPC Integrator produces and maintains the PKG-066 Package Datasheet, and how a vendor or discipline engineer uses it for package engineering. Per the four-document interpretation rule, both production and use steps are included.

## Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Confirm DEL-066-01_scope-of-work is at INITIALIZED or later (upstream context). Note: `_DEPENDENCIES.md` declares no formal upstream/downstream edges; this is a recommended coordination dependency, not a declared blocker.
- Accessible source materials:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (04-25 plant DBM).
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (03-25 Liquids Hub DBM).
  - Decomposition snapshot: GATE-07_Final_Published_2026-05-24.
- Inaccessible/deferred source: `26020-Package_Requirements.docx` package heading 21 (recover access before final issue).
- Decomposition row for DEL-066-02 in `DELIVERABLE_REGISTER.csv`.

## Steps

### A. Production of the Package Datasheet (EPC Integrator)

1. Read all deliverable-local files (`_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` placeholder).
2. Extract package identity (PKG-066, Tanks, Condensate (API 650) 4-25, mechanical, EPC Package Datasheet, EPC Integrator) from `_CONTEXT.md` and the decomposition row.
3. Open `26020-Package_Requirements.docx` package heading 21 (when accessible) and extract: tank list with tags, service, sizing basis, MOC, coating, nozzle schedule, foundation/anchorage basis, inspection/NDE basis, civil/I&C/electrical interface basis. Until accessible, mark TBD.
4. Extract atmospheric-tank inventory and storage-duration basis from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-04 Product Storage Summary, and the produced-water API-650 Modified analog from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Produced-Water section.
5. Populate the Datasheet sections (Identification, Attributes, Conditions, Construction, Interface Requirements, References) using only source-grounded values or explicit TBD/ASSUMPTION markers.
6. Populate the Specification (Scope, Requirements, Standards, Verification, Documentation) with the requirement table; map each requirement to a verification method.
7. Populate the Guidance (Purpose, Principles, Considerations, Trade-offs, Examples, Conflict Table) and record any conflicts that the human owner must rule on.
8. Populate this Procedure (production + use steps; verification; records).
9. Run the Cross-Reference Consistency Check (Specification REQ ↔ Datasheet attributes; Specification REQ ↔ Procedure verification; terminology and units consistent).
10. Update `_STATUS.md` per safe-update rule (OPEN → INITIALIZED via `tools/scaffolding/write_status.sh`).
11. Write run record at `_run_records/TASK_RUN_<timestamp>.md`.

### B. Use of the Package Datasheet (downstream vendor / discipline engineer)

1. Read Identification and confirm package identity matches the work order.
2. Use Attributes table to confirm tank count, size, and service against the vendor RFQ.
3. Apply Conditions table for design SG, density, temperature, and spacing constraints when sizing and laying out the package.
4. Confirm Construction basis (code, coating, insulation, heating) against vendor's proposed datasheet; raise an interface query if the vendor proposes deviation.
5. Use the Interface Requirements table to align tie-in P&IDs and the package interface matrix.
6. Track all TBD rows and Conflict Table items; close them out via interface queries to the EPC Integrator before fabrication release.

## Verification

| Check | How | Pass Criterion |
|---|---|---|
| All requirements cite a source or are explicitly marked TBD/ASSUMPTION | Document review | No unsourced positive claim |
| Each spacing requirement matches the 04-25 SEC-03 atmospheric-tank-spacing table | Cross-check | Numeric match |
| Vapour interface aligns with VRU post-SCA-002 routing | Cross-check with `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Vapour Recovery | Match |
| Tank inventory consistent with selected scope of CONF-066-02-01 ruling | Cross-check after human ruling | Match |
| Each Specification REQ has a Verification row | Table review | Every REQ ID present |
| Each TBD has either a "source not accessible" note or an action to close | Table review | Every TBD has either |
| `_STATUS.md` updated only if state was OPEN; new state INITIALIZED | File review | State change recorded only when permitted |
| Run record present in `_run_records/` with timestamp and PASS or VIOLATION | File review | Run record exists; required headings present |

## Records

- This deliverable's four documents: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- `_STATUS.md` updated state line and History entry.
- `_run_records/TASK_RUN_<timestamp>.md` for each TASK invocation.
- Vendor RFI/IFC submittals (downstream, outside this deliverable's write scope).
- Interface queries raised against Conflict Table rows (recorded against `_Coordination/` or successor controls; outside this deliverable's write scope).
