# Procedure — DEL-085-01 Scope of Work (PKG-085 Flare Stack (High Pressure))

This Procedure describes the steps to **produce** the EPC Integrator Scope of Work artifact for PKG-085 from the accepted upstream GATE-07 decomposition and the locally accessible source materials. Operational/use procedures for the physical HP flare stack belong to vendor documentation (DEL-085-04/05) and the Construction Work Package (DEL-085-03), not to this SoW deliverable.

## Purpose

Produce the four anticipated artifacts named in DELIVERABLE_REGISTER row 312 — (1) package scope of work, (2) tagged equipment and package identity list, (3) package function and integration narrative, (4) responsibility assignment record — in a form that is source-grounded, internally consistent across this deliverable's four documents, and ready to anchor DEL-085-02 through DEL-085-06.

## Prerequisites

| # | Prerequisite | Status / Source |
|---|---|---|
| P1 | `_CONTEXT.md` populated with deliverable identity, package, discipline, type, responsible party, anticipated artifacts | Present |
| P2 | `_REFERENCES.md` populated with decomposition pointers and shared source root | Present |
| P3 | `_DEPENDENCIES.md` initialized (DECLARED mode, no upstream/downstream declared during PREPARATION) | Present; no declared dependencies |
| P4 | Accepted GATE-07 PROJECT_DECOMP snapshot accessible | Present |
| P5 | At least one locally accessible authoritative source slice for the HP flare stack | Present: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Active Flare Basis (lines ~497-501); contributing context in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| P6 | 26020-Package_Requirements.docx package heading 38 rendered to a readable form | TBD — source-binary; clause-level renderings not located in the local workspace |
| P7 | W242510-PRC-REP-000003-001 Plant Shutdown and Blowdown Philosophy available locally | TBD — not locally accessible |
| P8 | `_STATUS.md` current state in `ALLOW_OVERWRITE_STATES` (OPEN, INITIALIZED) | OPEN — overwrite permitted |

## Steps

| # | Step | Inputs | Output |
|---|---|---|---|
| S1 | Read `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_SEMANTIC.md` to fix deliverable identity and overwrite eligibility. | Deliverable-local metadata | Confirmed identity (DEL-085-01, PKG-085, FL-4120-1), confirmed OPEN state |
| S2 | Read the decomposition entries for PKG-085 and DEL-085-01 in the GATE-07 snapshot (PACKAGE_REGISTER row 58, DELIVERABLE_REGISTER row 312, SCOPE_LEDGER rows 88-91, OBJECTIVE_REGISTER for OBJ-002 and OBJ-004 through OBJ-010). | GATE-07 snapshot CSVs | Decomposition context (package function, responsibility model, interfaces, anticipated artifacts, scope ledger entries) |
| S3 | Read accessible source slices for the HP flare stack: 3-25 DBM Facility Overview (line ~56), Active Flare Basis (lines ~497-501), Emissions table row (line ~548); 4-25 DBM HP-flare-served service descriptions (lines ~585, 704, 813, 838-842). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Source-supported values (tag, OD, height, header size, KO drums, served loads, staggered-blowdown rule) |
| S4 | Generate `Datasheet.md` — populate Identification from `_CONTEXT.md`/registers; populate Attributes/Conditions/Construction from source slices; mark unsupported values `TBD`. | S1-S3 outputs | `Datasheet.md` |
| S5 | Generate `Specification.md` — Scope, Requirements (R-085-01-01 through R-085-01-14), Standards, Verification, Documentation. Cite source for every non-trivial requirement; mark TBD where source is unavailable. | S1-S3 outputs; Datasheet identity | `Specification.md` |
| S6 | Generate `Guidance.md` — Purpose, Principles, Considerations, Trade-offs, Examples, Conflict Table (CT-085-01-01 through CT-085-01-03). | S1-S5 outputs | `Guidance.md` |
| S7 | Generate `Procedure.md` (this file) — Prerequisites, Steps, Verification, Records. | S1-S6 outputs | `Procedure.md` |
| S8 | Cross-document consistency check: tag IDs (FL-4120-1, V-4100-2, V-4150-2, P-4100-2, P-4150-2), values (660 mm OD; 60,957 mm; 508 mm), terminology (HP/Cryo flare stack; reference/interface package), responsibility wording, and Objective list all consistent across the four documents. | S4-S7 outputs | Pass 2 consistency confirmed; conflicts moved to Guidance Conflict Table |
| S9 | Update `_STATUS.md` from OPEN to INITIALIZED via `tools/scaffolding/write_status.sh` operational invocation, recording `TASK+four-documents`. | `_STATUS.md`; this skill | `_STATUS.md` updated |
| S10 | Write the run record at `_run_records/TASK_RUN_<timestamp>.md` with all input echo, resolved state, tools used, outputs, missing items, dependency notes, and applied changes. | All preceding outputs | Run record |

## Verification

| Check | Method |
|---|---|
| Four documents exist in the deliverable folder | Directory listing |
| Default schema sections present in each document | Heading scan |
| Tag IDs and numeric values consistent across all four documents | Manual cross-check during S8 |
| Every non-trivial value cites a source or is explicitly `TBD` | Specification §Requirements, Datasheet tables |
| No metadata files other than `_STATUS.md` modified | `git status` against deliverable folder |
| `_STATUS.md` state transition is OPEN -> INITIALIZED only when permitted | Read `_STATUS.md` history |
| Conflict Table captures unresolved source/decomposition disagreements | Guidance §Conflict Table review |
| Run record contains all required headings and frontmatter | Open `_run_records/TASK_RUN_*.md` |

## Records

- `_run_records/TASK_RUN_<timestamp>.md` — durable run record
- `_STATUS.md` — state transition history line for OPEN -> INITIALIZED
- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four artifacts that collectively constitute the SoW deliverable's working draft

## Notes / TBD

- Procedure steps that depend on the binary `26020-Package_Requirements.docx package heading 38` source remain partially `TBD` until a markdown/text rendering of that heading is staged into `_Sources/` or `0_References/`.
- Blowdown sequencing detail required by R-085-01-07 depends on external document W242510-PRC-REP-000003-001 which is not locally accessible (`TBD`).
