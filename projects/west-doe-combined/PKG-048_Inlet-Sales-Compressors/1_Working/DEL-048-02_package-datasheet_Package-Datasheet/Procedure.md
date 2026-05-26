# Procedure: DEL-048-02 — PKG-048 Inlet / Sales Compressors Package Datasheet

## Purpose

Operational steps to **produce, verify, and maintain** the PKG-048 Inlet / Sales Compressors Package Datasheet (`Datasheet.md`) so it satisfies the requirements in `Specification.md` and is fit for use as the Gate 5 EPC handoff document.

This procedure describes how to author the datasheet within the deliverable folder. It is not the procedure for operating the field compressor packages.

## Prerequisites

1. Deliverable-local truth set is initialized in `{DELIVERABLE_PATH}`:
   - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` are present (PREPARATION seeded fileset).
2. Accepted decomposition snapshot is reachable at the path recorded in `_REFERENCES.md` (Gate 7 final published PROJECT_DECOMP snapshot 2026-05-24).
3. Authoritative source `DBM-Deepcut/4-25_Deepcut_DBM.md` is locally accessible under `_Sources/`.
4. Companion sources `26020-Package_Requirements.docx` heading 3 and `Bid Docs/Budgetary/RFQ/Bid Docs/26020-01-PT-RFQ-12-003-Inlet Sales Comp.docx` are either (a) locally accessible as Markdown or (b) explicitly known to be inaccessible — in which case dependent fields will be carried as `location TBD`.
5. `_STATUS.md` Current State is in `ALLOW_OVERWRITE_STATES` (per brief: `OPEN, INITIALIZED`). If not, abort and return `SKIPPED_PROTECT_HUMAN_WORK`.
6. No declared upstream dependencies block this work (`_DEPENDENCIES.md` declares none).

## Steps

### S1 — Load context and source set (Step 1 of `four-documents`)

1. Read `_CONTEXT.md` and extract Identification fields verbatim.
2. Read the deliverable row in `DELIVERABLE_REGISTER.csv` (DEL-048-02) and the package row in `PACKAGE_REGISTER.csv` (PKG-048) from the Gate 7 snapshot.
3. Read `_REFERENCES.md` to enumerate authoritative source materials.
4. Open the DBM source slice for inlet/sales compression: `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-05 "Compression and Acid Gas Handling Basis" in full; SEC-04 for upstream pipeline basis as needed; SEC-08 for buildings/foundations basis as needed.
5. If `26020-Package_Requirements.docx` heading 3 or the RFQ document is available as Markdown, open it; otherwise record it as inaccessible.

### S2 — Draft Identification table (Datasheet)

Populate from `_CONTEXT.md` and PACKAGE_REGISTER.csv row PKG-048. Every cell cites its source.

### S3 — Draft Attributes table (Datasheet)

For each row, copy the value from DBM-Deepcut SEC-05 with the cited subsection ("Compression Configuration" / "Inlet / Sales Compressor Basis" / "Inlet / Sales Compressor Design Conditions" / "Open Items / TBC Items"). Carry TBC labels through. Where the PACKAGE_REGISTER row disagrees with the DBM on engineering substance (start method), record the DBM value and add a Conflict Table row.

### S4 — Draft Conditions tables (Datasheet)

Carry inlet-service and sales-service pressure/temperature tables, the per-stage air-cooler outlet and dP basis, and the scrubber sizing basis from DBM-Deepcut SEC-05 verbatim, preserving units and TBC markers.

### S5 — Draft Construction table and Interface list (Datasheet)

1. Per-package equipment rows from DBM-Deepcut SEC-05 (scrubbers, cooler frame, control valves, blowdown, recycle, lube-oil heater, sweet-gas purge, seal pot, distance-piece sweep purge, clearance pockets, start basis).
2. Copy the applicable interface types verbatim from PACKAGE_REGISTER.csv row PKG-048.
3. For each interface type, attach a DBM-cited counterpart where the DBM supports it (inlet/TEG HEX, amine inlet, J-T/expander, sales-gas booster, fuel-gas purge, VRU suction header, packing drain seal pot, electrical/MCC). Do not invent counterparts.

### S6 — Draft References (Datasheet)

List authoritative sources actually consulted and explicitly enumerate inaccessible sources as TBD.

### S7 — Cross-reference consistency check (Pass 2)

Run the following checks; resolve from drafts where possible, else open the DBM source slice; else mark TBD or add to the Conflict Table in `Guidance.md`:

| Check | What to verify |
|---|---|
| Datasheet ↔ Specification | Each Specification requirement (R1-R17) has a corresponding Datasheet row or section. |
| Specification ↔ Guidance | Each Specification requirement has a directional principle/consideration in Guidance. |
| Specification ↔ Procedure | Each Specification requirement has a verification or production step in this Procedure. |
| Terminology | "inlet/sales multi-service compressor package", "package", "inlet service", "sales service", "starting VFD", "common compressor frame", "common air-cooler frame", "Ariel KBC/6" used consistently across all four documents. |
| Values | 5 packages, 5 x 20 percent sparing, 62.4 MMSCFD per package inlet (TBC vs 60), 57.6 MMSCFD per package sales, 1,130 psig inlet discharge, 1,500 psig sales 2nd-stage discharge (TBC vs 1,700), 6,700 hp (TBC vs 7,000), 4,000 V, NEMA MG1 — consistent across all four documents. |

### S8 — Update status (Step 7 of `four-documents`)

1. Read `_STATUS.md` Current State.
2. If Current State = `OPEN`, update to `INITIALIZED` and append a history line citing `TASK+four-documents`. Use `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` when available; otherwise apply the equivalent safe edit directly.
3. If Current State is not `OPEN`, do not modify `_STATUS.md`. Report the skip in the run record.

### S9 — Persist run record

Write `_run_records/TASK_RUN_{YYYY-MM-DD}_{HHmm}.md` with YAML frontmatter and the standard body headings (Requested Tasks, Expected Outputs, Tools Used, Tool Policy Compliance, Outputs Produced, Missing, Needs Human Ruling, Dependency Notes, Applied Changes).

### S10 — Optional — Pass 3 (semantic lensing) when invoked separately

When `_SEMANTIC_LENSING.md` is later produced by `skills/lens-register/`, dispatch a separate TASK run with `RUN_PASSES: P3_ONLY`. For each warranted item: reread the relevant source slice, incorporate only when supported, record disposition (incorporated / already covered / converted to TBD / surfaced as conflict / rejected with reason). Do not invent.

## Verification

| Verification ID | Check | Pass criterion |
|---|---|---|
| V1 | Every non-trivial Datasheet cell cites a source path and section reference, or is marked `TBD` / `location TBD`. | 100 percent compliance on inspection. |
| V2 | Identification table matches `_CONTEXT.md` and PACKAGE_REGISTER.csv row PKG-048. | No discrepancies. |
| V3 | Attributes, Conditions, Construction values match DBM-Deepcut SEC-05 verbatim (subject to TBC carry-through). | No discrepancies. |
| V4 | Applicable interface types list is verbatim from PACKAGE_REGISTER.csv row PKG-048. | No discrepancies. |
| V5 | Cross-document terminology and values are consistent (per S7). | No mismatch detected. |
| V6 | Each Conflict Table row has a Conflict ID, both source pointers (or `none` when single-source), impacted sections, a PROPOSAL, and `TBD` for human ruling. | All rows complete. |
| V7 | `_STATUS.md` change (when applied) is a safe forward transition (`OPEN` -> `INITIALIZED`) and is appended to history with a dated line. | Single safe transition with history line. |
| V8 | Run record YAML frontmatter and body headings are complete (per `four-documents/QA_CHECKS.md` and `AGENT_TASK.md`). | All required fields/headings present. |
| V9 | No files outside `{DELIVERABLE_PATH}` were modified. | Confirmed via git scope check. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — produced/updated.
- `_STATUS.md` — updated only under the safe transition rule (`OPEN` -> `INITIALIZED`).
- `_run_records/TASK_RUN_2026-05-24_2359.md` — auditable run evidence for this run.
- Future Pass 3 runs produce additional run records under `_run_records/`.
- Open conflict entries in `Guidance.md` "Conflict Table (for human ruling)" remain `TBD` until a human rules.
