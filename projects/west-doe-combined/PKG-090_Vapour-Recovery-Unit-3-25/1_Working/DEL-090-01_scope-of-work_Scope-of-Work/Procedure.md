# Procedure — DEL-090-01 Scope of Work (PKG-090 Vapour Recovery Unit 3-25)

> Operational document. Steps describe how to **produce** the Scope of Work deliverable artifact. Source-grounded; `TBD` where source information is missing.

## Purpose

Produce the EPC Integrator Scope of Work for PKG-090 covering package scope, tagged equipment and package identity, package function and integration narrative, and responsibility assignment, to support Gate 5 EPC anchoring and downstream PKG-090 deliverables (DEL-090-02..06).

## Prerequisites

- Read deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`.
- Confirm accepted upstream snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Open the PACKAGE_REGISTER.csv row 100 (PKG-090) and DELIVERABLE_REGISTER.csv row 564 (DEL-090-01).
- Open the project DBM at `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`: SEC-01 (supersession), SEC-06 (§Vapour Recovery), SEC-07 (Fuel Gas / Utilities).
- Locate/obtain access to `_Sources/26020-Package_Requirements.docx` package heading 43 (extract to text form if practicable).
- Locate/obtain access to vendor RFQ `Bid Docs/Budgetary/26020-03-PT-RFQ-12-001_VRU_1_R0.docx` (NOT currently in `_Sources/` — flag as missing reference).
- No declared upstream/downstream dependencies in `_DEPENDENCIES.md` at the time of authoring; coordination via PACKAGE_REGISTER interface types.

## Steps

### Step 1 — Confirm package identity

1. Copy identity fields from `_CONTEXT.md` and PACKAGE_REGISTER row 100 into the Datasheet §Identification table.
2. Confirm Workbook row 100, tag `26020-03-12-001`, doc number `26020-03-PT-12-001 - Vapour Recovery Unit`, discipline Mechanical, WBS 03.
   Source: PACKAGE_REGISTER row 100; `_CONTEXT.md`.

### Step 2 — Establish package function and integration narrative

1. Draft the package-function narrative from DBM SEC-06 §Vapour Recovery and PACKAGE_REGISTER row 100 Description.
2. State 2 x 100% lead-lag configuration, single building, Ro-Flo 12S/212M two-stage rotary-vane compressors, 200 HP VFD motors, sour service.
3. State discharge routing to 04-25 SOC suction per SCA-002 (cite DBM SEC-01 supersession).
4. Describe VRU recycle, LP fuel-gas blanket, and LP flare bypass behaviours (DBM SEC-06).

### Step 3 — Produce tagged equipment and package identity list

1. List the two VRU compressor packages, the single shared building, per-train recycle valves, the LP-flare bypass V-ball valve, and the LP fuel-gas make-up/blanket regulator.
2. Where individual tag numbers are not located in accessible sources, set value to `TBD` and cite "location TBD — `26020-Package_Requirements.docx` heading 43 and vendor RFQ `26020-03-PT-RFQ-12-001_VRU_1_R0.docx`".
3. Do NOT invent equipment tags; defer detailed sub-component list to DEL-090-04.

### Step 4 — Document responsibility assignment

1. Copy the ownership statement from PACKAGE_REGISTER row 100 §Ownership.
2. State Package Vendor scope (engineering, design, vendor documentation, physical equipment package).
3. State EPC Integrator scope (integration into the functional process facility; interfaces; tie-ins; constructability; procurement/construction coordination; facility-level integration).

### Step 5 — Map facility-side interfaces

1. List the thirteen interface types from PACKAGE_REGISTER row 100.
2. For each, briefly cross-reference what the EPC Integrator must coordinate (free-text narrative; defer detailed interface specs to INTERFACE_REGISTER and DEL-090-02 Package Datasheet).
3. Where detailed values are not in accessible sources, mark `TBD`.

### Step 6 — Map covered SOW items and supported objectives

1. Reproduce SOW-0249, SOW-0250, SOW-0251, SOW-0252 from `_CONTEXT.md` and DELIVERABLE_REGISTER row 564.
2. Reproduce OBJ-002…OBJ-010 mapping from PACKAGE_REGISTER row 100 / DELIVERABLE_REGISTER row 564.
3. Label the objective association as `ASSUMPTION (PACKAGE_HEURISTIC)` per `OBJECTIVE_ASSOCIATION_MODE` in the brief.
4. If detailed SOW item text is not locally accessible, leave the per-item description as `TBD`.

### Step 7 — Flag missing source slices

1. Record explicit `TBD` markers in Datasheet §Conditions and Specification R-090-11 where capacity / sizing / pressures cannot be sourced.
2. Record the missing/unextracted sources in Guidance §Conflict Table (C-090-01, C-090-02, C-090-03).

### Step 8 — Cross-document consistency sweep

1. Verify identical terminology (PKG-090, DEL-090-01, "2 x 100% lead-lag", "Ro-Flo 12S/212M", "200 HP VFD", "04-25 SOC suction") across all four documents.
2. Verify each Specification requirement has a corresponding §Verification row.
3. Verify Datasheet attributes align with Specification requirements and Guidance principles.

### Step 9 — Update `_STATUS.md`

If `_STATUS.md` Current State is `OPEN`, advance to `INITIALIZED` using `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Otherwise do not modify (no state regression).

## Verification

| Check | Pass condition |
|---|---|
| Identity fields populated | All Datasheet §Identification rows match `_CONTEXT.md` and PACKAGE_REGISTER row 100 |
| Source citations present | Every non-TBD requirement, value, and attribute cites a source path + section reference |
| TBD markers preserved | Capacity, pressures, equipment tags, SOW item details, and `26020-Package_Requirements.docx` heading 43 specifics carry `TBD` or `location TBD` |
| Cross-document consistency | Specification requirements ↔ Datasheet attributes ↔ Guidance principles ↔ Procedure steps use identical terms and values |
| Conflict Table issued | Guidance §Conflict Table captures source-access gaps and heuristic mappings |
| Scope boundary preserved | Out-of-scope items (DEL-090-02..06) explicitly excluded |
| Status update | `_STATUS.md` advances OPEN → INITIALIZED only if state was OPEN |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` produced in `{DELIVERABLE_PATH}`.
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_{timestamp}.md`.
- `_STATUS.md` updated to `INITIALIZED` (history entry added) when authorised by safe-update rule.
- Conflict Table entries in `Guidance.md` for human ruling.
