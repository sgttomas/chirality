# Procedure — DEL-058-02 Package Datasheet (PKG-058 Medium Pressure Flash Feed Separator)

> Operational procedure to produce, review, and issue the PKG-058 Package Datasheet artifact. This procedure interprets "procedure" as the production-of-the-deliverable procedure (the artifact itself is a datasheet, not an operating manual). It is grounded in deliverable-local context and accessible source slices.

## Purpose

Produce a source-grounded, source-cited Package Datasheet that an EPC Integrator can hand to a third-party vendor (or to a downstream discipline) as the basis for engineering and design of PKG-058 Medium Pressure Flash Feed Separator equipment (V-7110-1, V-7310-1; E-7120-1, E-7320-1).

## Prerequisites

| Prerequisite | Reference | Status |
|---|---|---|
| Deliverable folder initialized | `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` present | Confirmed |
| Accepted upstream decomposition snapshot | GATE-07 PROJECT_DECOMP snapshot | Confirmed (per `_REFERENCES.md`) |
| Locally accessible source — DBM-Deepcut | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Accessible |
| Locally accessible source — 26020-Package_Requirements.docx package heading 13 | `_Sources/26020-Package_Requirements.docx` | **Not locally extracted** (binary docx; no markdown slice) — fields dependent on it marked `location TBD` |
| Locally accessible source — Packages_Interfaces export | `_Sources/26020-Packages_Interfaces_4_export.xlsx` | **Not locally extracted** — fields dependent on it marked `location TBD` |
| Declared upstream dependencies | `_DEPENDENCIES.md` | None declared during PREPARATION |
| Sibling deliverables in PKG-058 | DEL-058-01 SOW; DEL-058-03 CWP; DEL-058-04 Vendor Eng Pkg; DEL-058-05 Vendor Doc Turnover; DEL-058-06 EPC Vendor Pkg Review | Adjacent (advisory only; this procedure does not cross-edit) |

## Steps

### Step 1 — Read deliverable-local context

Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`. Confirm package identity (PKG-058) and deliverable type (EPC Package Datasheet). Confirm `_STATUS.md` Current State is `OPEN` (overwrite-permitted under the `four-documents` skill ALLOW_OVERWRITE_STATES contract).

### Step 2 — Read decomposition entry

Open the GATE-07 PROJECT_DECOMP snapshot:
- `DELIVERABLE_REGISTER.csv` row for `DEL-058-02_package-datasheet`.
- `PACKAGE_REGISTER.csv` row for `PKG-058`.
- `OBJECTIVE_DELIVERABLE_MAP.csv` rows mentioning `DEL-058-02_package-datasheet` (OBJ-001, OBJ-004 through OBJ-010 — explicit deliverable-level rows).
- `INTERFACE_REGISTER.csv` — review entries that touch PKG-058 / MPFF.

### Step 3 — Read authoritative source slices

In `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, read:
- §"MPFF and Stabilizer Train Relationship" (train pairing, sparing).
- §"MPFF Operating and Capacity Basis" (pressure, temperature, flow tables, internals, purge gas, methanol, heater bundle option).
- §"Heat Medium Users and Duties" rows E-7120-1 and E-7320-1 (heater duty basis).
- Equipment register rows 52-53 (tag confirmation).
- Module table entries for 710-1 and 730-1 modules.
- §"Relief and Blowdown" (HP flare routing context).
- §"MPFF and SOC TBDs" (source-declared open items).

### Step 4 — Draft Datasheet.md

Populate Identification, Attributes, Operating Conditions, Construction, Interfaces, and Open Items strictly from the source slices read in Step 3. Cite the source slice for every non-trivial value. Mark unknown source values `TBD`; mark unverifiable locations `location TBD`; mark inferred values `ASSUMPTION`.

### Step 5 — Draft Specification.md

Translate source content into normative requirements (R1-R9). Each requirement MUST cite its source slice. Tabulate verification approaches against requirements. Record standards including code references as `ASSUMPTION` only when not stated in the accessible source.

### Step 6 — Draft Guidance.md

Capture rationale, considerations, and trade-offs grounded in source. Build the Conflict Table for items the source itself flags as ambiguous (inlet temperature ASSUMPTION vs. post-HEX TBD; legacy 4-vessel annotation; heater-bundle supply temperature; inaccessible package-requirements doc).

### Step 7 — Cross-document consistency sweep (Pass 2)

Walk the consistency checks:
- Datasheet entities (V-7110-1, V-7310-1, E-7120-1, E-7320-1) reflected in Specification R1-R8 and Procedure prerequisites.
- Specification requirements have verification rows (R1↔V1 etc.).
- Specification verification hooks present in Procedure Steps 4-6 and Step 8.
- Terminology stable: "MPFF", "HCL heater bundle", "stabilizer flash/feed separator", "SOC third-stage suction".
- Numeric values stable across documents: 1724 kPag operating pressure design, 12.91 MMSCFD design two-phase inlet, 19.58 m3/h liquid, 4.143 MMSCFD vapour, 762 kW heater duty, 10 min residence time, 2 x 100% sparing.

### Step 8 — Verification

- Each non-trivial datasheet value either cites a source slice or is marked `TBD` / `location TBD` / `ASSUMPTION`.
- Specification requirements are each linked to a verification row.
- Conflict Table covers source ambiguities encountered.
- No edits applied outside `{DeliverablePath}` (except `_STATUS.md` safe update and `_run_records/`).

### Step 9 — Update `_STATUS.md`

If Current State is `OPEN`, run safe status update to `INITIALIZED` and stamp `TASK+four-documents`. If the current state is anything else, do not modify `_STATUS.md`.

### Step 10 — Write run record

Write `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` per AGENT_TASK structural rules with all required frontmatter and body headings populated.

## Verification (rolled up)

- Four documents (Datasheet, Specification, Guidance, Procedure) present.
- Default section headings preserved in each document.
- At least one locally accessible source from `_REFERENCES.md` was read (DBM-Deepcut).
- Non-trivial claims cite sources or are marked `TBD` / `ASSUMPTION`.
- `_STATUS.md` transitioned `OPEN → INITIALIZED` (no state regression).
- Run record written.

## Records

- `{DELIVERABLE_PATH}/Datasheet.md`
- `{DELIVERABLE_PATH}/Specification.md`
- `{DELIVERABLE_PATH}/Guidance.md`
- `{DELIVERABLE_PATH}/Procedure.md`
- `{DELIVERABLE_PATH}/_STATUS.md` (safe state update only)
- `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md`
