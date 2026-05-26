# Procedure — DEL-062-02 Package Datasheet (NGL Loading Pumps Building, PKG-062)

> Pass 1 + Pass 2 draft. Operational steps to **produce** the Package Datasheet for `PKG-062`, then to **use** it as the EPC handoff to the Package Vendor. Steps are grounded in `_CONTEXT.md`, `26020-Package_Requirements.docx` (`26020-01-PT-18-003`), the Gate-07 PROJECT_DECOMP snapshot, and the skill `four-documents/SKILL.md`. Inferences are labeled `ASSUMPTION`; unknowns are `TBD`.

## Purpose

Establish a reproducible procedure for (a) producing this Package Datasheet from source materials and decomposition registers and (b) using the Datasheet as the handoff to the Package Vendor and as the interface evidence basis for EPC discipline engineering.

## Prerequisites

### Required references (must be locally accessible)

- `26020-Package_Requirements.docx`, section `26020-01-PT-18-003 - LPG Loading Pumps` (locally accessible: yes).
- Gate-07 snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` row `PKG-062` (yes).
  - `DELIVERABLE_REGISTER.csv` row `DEL-062-02_package-datasheet` (yes).
  - `SCOPE_LEDGER.csv` rows `SOW-0153..0156` (yes).
- Deliverable-local metadata: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` (yes).

### Conditionally required references

- `Bid Docs/Budgetary/26020-01-PT-RFQ-18-003-LPG_Loading_Pumps.docx` — cited by source row but **not** locally accessible (CONFLICT-3). Required only if NPSH, casing pressure rating, or materials of construction must be filled before vendor confirmation.
- `26020-Packages_Interfaces_4_export.xlsx` — corroborating interface matrix (present locally; version differs from source citation — CONFLICT-2).
- `DBM-Deepcut/4-25_Deepcut_DBM.md` — basis-of-design reference (present locally).

### Declared dependencies (per `_DEPENDENCIES.md`)

- Upstream: none declared during PREPARATION.
- Downstream: none declared during PREPARATION.

The package's other deliverables (`DEL-062-01`, `DEL-062-03..06`) are co-package siblings; they are not declared dependencies but are obvious downstream consumers of the Datasheet.

### Status precondition

- `_STATUS.md` `Current State` must be `OPEN` or `INITIALIZED` (per brief `ALLOW_OVERWRITE_STATES = OPEN,INITIALIZED`). If not, this procedure does not overwrite documents and returns `SKIPPED_PROTECT_HUMAN_WORK`.

## Steps — Production of the Datasheet

### Step 1 — Read deliverable-local context

Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md`. Extract identity, scope, anticipated artifacts, scope items covered (`SOW-0153..0156`), and objectives (`OBJ-001`, `OBJ-003..010`).

### Step 2 — Read decomposition entries (Gate-07)

Read the `PKG-062` row in `PACKAGE_REGISTER.csv`, the `DEL-062-02_package-datasheet` row in `DELIVERABLE_REGISTER.csv`, and `SOW-0153..0156` in `SCOPE_LEDGER.csv`. Extract package equipment tag (`26020-01-PT-18-003`), WBS (`01`), workbook row (`76`), applicable interface types, and scope-item statements.

### Step 3 — Read source slices

Read the `26020-01-PT-18-003 - LPG Loading Pumps` section of `26020-Package_Requirements.docx`, including subsections: Location / Status; Source Basis; Basic Scope; Major Included Equipment; Scope Notes / Open Items; Physical Interface Summary; Vendor Engineering Deliverables (full list, including the Structural / foundations / supports group; the Pass 1 extraction was truncated and must be re-extracted for closeout — see Step 5).

### Step 4 — Populate the Datasheet

Populate `Datasheet.md` per `Specification.md` requirements R-DEL-062-02-001 through R-DEL-062-02-014. Apply the source-citation discipline of R-DEL-062-02-015 (every non-trivial value cites `SourcePath` + `SectionRef`; unknown locations are "location TBD"; inferred values are labeled `ASSUMPTION`).

### Step 5 — Resolve the Structural-group truncation (closeout step)

Re-extract the "Vendor Engineering Deliverables — Structural / foundations / supports" subgroup from `26020-Package_Requirements.docx` (`26020-01-PT-18-003`). Insert the IDs into `Datasheet.md` under that subheading, replacing the `TBD` placeholder.

### Step 6 — Cross-check internal consistency (Pass 2)

Run the consistency checks from `four-documents/SKILL.md` Step 5:
- Datasheet entities ↔ Specification requirements: every named pump, capacity, driver, building, and by-others item has a requirement ID.
- Specification ↔ Guidance: each requirement has a rationale entry or considerations note.
- Specification ↔ Procedure: each requirement has a production-step or verification linkage.
- Terminology: "Blackmer LGL4B," "rotary vane," "parallel," "MCC," "TBC," "by others" used consistently.
- Values: 68 m³/hr / 345 kPad / 300 USGPM / 50 psid / 575 V / 3 PH / 60 Hz / 600 V MCC / −40 °C identical across documents.

### Step 7 — Apply the Conflict Table

For CONFLICT-1, CONFLICT-2, CONFLICT-3 in `Guidance.md`, confirm the Datasheet and Specification reflect the documented PROPOSAL (use decomposition identity; rely on source-row interface matrix; mark bid-doc citation as location TBD). Do not silently resolve to one side without a human ruling.

### Step 8 — Update `_STATUS.md` (safe update only)

Per `four-documents/SKILL.md` Step 7 and brief `ALLOW_OVERWRITE_STATES`: if and only if `Current State` is `OPEN`, transition to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. If state is not `OPEN`, do not modify `_STATUS.md` (no state regression).

### Step 9 — Persist the run record

Write the run record at `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` per `AGENT_TASK.md` Run-record file format. The run record is the durable record of input, resolved state, tools used, outputs, conflicts surfaced, and human rulings needed.

## Steps — Use of the Datasheet (handoff)

### Step U-1 — EPC Integrator transmits the Datasheet

EPC Integrator transmits `Datasheet.md` (and the supporting `Specification.md`, `Guidance.md`, `Procedure.md`) to the Package Vendor as the Package Datasheet handoff. The handoff includes the Vendor Engineering Deliverables list as the basis of the Vendor Document Index (`PRQ-009`).

### Step U-2 — Package Vendor confirm-back

Package Vendor returns confirmation/rejection of each `TBC` value (TDH, operating conditions, design conditions) via `MEC-003 Mechanical Equipment Data Sheets`, `MEC-007 Pump Data Sheets`, `PRO-013 Pump Hydraulic / NPSH Calculations`, and `ELE-011 Motor Starting Study`.

### Step U-3 — EPC discipline engineering uses interface matrix

Discipline leads (Process, Mechanical, Electrical, I&C, Civil, Structural, F&G) consume the Physical Interface Applicability matrix to plan tie-ins. Each "Yes" interface triggers the corresponding vendor deliverable category and an EPC tie-in scope sheet via `PIP-004 Tie-In List / Tie-In Scope Sheets`.

### Step U-4 — Change control on by-others list

Any proposed change to "DCS integration, foundations, electrical supply to MCC by others" is treated as a scope change and routed through the EPC-vendor review (DEL-062-06).

## Verification

| Verification | How |
|---|---|
| All four documents exist after the run | Filesystem check in `{DELIVERABLE_PATH}` |
| Default schema sections present in each document | Manual / QA pass per `four-documents/QA_CHECKS.md` |
| At least one locally accessible source was read from `_REFERENCES.md` | Confirmed in run record: `26020-Package_Requirements.docx` |
| Every non-trivial Datasheet value cites a source (or "location TBD") | Review `Datasheet.md` Identification, Attributes, Conditions, Interface, Vendor-deliverables sections |
| Cross-document terminology and value consistency | Step 6 above |
| Conflicts captured in `Guidance.md` Conflict Table | CONFLICT-1, CONFLICT-2, CONFLICT-3 recorded |
| `_STATUS.md` only modified per safe-update rule | `OPEN` → `INITIALIZED` via `write_status.sh` (Step 8) |
| Run record written with all frontmatter and headings | `_run_records/TASK_RUN_<…>.md` per AGENT_TASK contract |

## Records

The following records are produced and shall be retained:

- `{DELIVERABLE_PATH}/Datasheet.md` — the deliverable artifact.
- `{DELIVERABLE_PATH}/Specification.md` — normative requirements.
- `{DELIVERABLE_PATH}/Guidance.md` — directional rationale and Conflict Table.
- `{DELIVERABLE_PATH}/Procedure.md` — this file.
- `{DELIVERABLE_PATH}/_STATUS.md` — updated to `INITIALIZED` (when precondition met).
- `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` — durable run evidence.
- Post-handoff (downstream of this skill): vendor confirm-back responses (`MEC-003`, `MEC-007`, `PRO-013`, `ELE-011`), Vendor Document Index (`PRQ-009`), Tie-In List (`PIP-004`).
