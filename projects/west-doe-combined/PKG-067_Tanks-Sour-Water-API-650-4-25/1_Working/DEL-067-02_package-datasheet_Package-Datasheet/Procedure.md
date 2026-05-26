# Procedure — DEL-067-02 Package Datasheet (PKG-067 Tanks, Sour Water (API 650) 4-25)

This procedure describes how to **produce** the Package Datasheet artifact for PKG-067 from the accepted upstream sources. (Procedures for **operating** the tanks in service belong to commissioning/operations turnover, not to this EPC handoff deliverable.)

## Purpose

Define the repeatable steps the EPC Integrator follows to assemble, source-anchor, and issue the Package Datasheet for the Sour/Produced Water Storage Tank package (TK-9010-1, TK-9020-1) so that the vendor handoff meets the requirements in `Specification.md` and the source-grounding rules in `Guidance.md`.

## Prerequisites

1. Accepted upstream snapshot is GATE-07 Final Published PROJECT_DECOMP at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
2. Deliverable-local truth-set files present: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md`.
3. Locally accessible authoritative source: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
4. Decomposition rows located: PACKAGE_REGISTER row 94 (PKG-067) and DELIVERABLE_REGISTER row 529 (DEL-067-02).
5. Companion package deliverables identified (DELIVERABLE_REGISTER rows 528-533) so that DEL-067-02 stays bounded to the datasheet scope and does not absorb SoW / CWP / acceptance content.
6. (Recommended, currently TBD) Local readable extraction of `_Sources/26020-Package_Requirements.docx` package heading 22 — when available, run the procedure again to fill any TBD entries that depend on that source.

## Steps

1. **Confirm scope and identity.** Read `_CONTEXT.md`. Record package ID (PKG-067), tank tags (TK-9010-1, TK-9020-1), discipline (Mechanical), responsible party (EPC Integrator), and the SOW/OBJ coverage lists. Cross-check against PACKAGE_REGISTER row 94 and DELIVERABLE_REGISTER row 529.
2. **Locate accessible sources.** Read `_REFERENCES.md`. Confirm `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` is readable. Note any cited sources that are not locally extracted (currently `26020-Package_Requirements.docx`) and flag those as TBD-producing.
3. **Extract storage-area source slice.** From the DBM, read the Process Storage Areas table (line 493), the Produced Water section (lines 504-524), the Spacing tables (lines 258-297), and the equipment-list rows for tags TK-9010-1 / TK-9020-1 (line 2627). These four slices are the authoritative source slice set for this datasheet.
4. **Populate `Datasheet.md` § Identification, Attributes, Conditions, Construction.** Use only values from the source slice set. For every non-trivial value, cite SourcePath + line number. Where the slice is silent, write `TBD` (do not insert convention defaults).
5. **Build the Interface Requirements Matrix.** Copy the interface-type list from PACKAGE_REGISTER row 94 into `Datasheet.md` § Interface Requirements Matrix. For each interface type, record (or mark TBD) the EPC vs. vendor boundary. Mark detailed tag-level resolution as downstream to INTERFACE_REGISTER for PKG-067.
6. **List member equipment tags.** Copy TK-9010-1 / TK-9020-1 from the equipment-list row (DBM line 2627) into `Datasheet.md` § Equipment List. Note adjacent-but-not-in-scope items (transfer pumps, sour water treatment pumps) for clarity.
7. **Write `Specification.md`.** For each requirement R1..Rn, anchor to a specific source slice line. Use Specification format `Source: <file> line <n>`. Carry forward any TBC/TBD qualifiers from the source rather than silently resolving them.
8. **Write `Guidance.md`.** Capture purpose, principles, considerations, trade-offs, and examples. Add the Conflict Table for any conflicts surfaced during steps 4-7 (currently: package naming, PVRV vent disposition, non-exhaustive contaminants list, missing Word source extraction).
9. **Write `Procedure.md`.** This document. Describe production steps; do not duplicate operational/commissioning content that belongs to downstream deliverables.
10. **Cross-document consistency sweep.** Verify entity names (tank tags, package ID), numeric values (capacity 2,000 bbl; storage days 8.9; design SG 1.25; spacing values), and standard citations are identical across all four documents. Resolve discrepancies from the drafts; if not resolvable, re-open the source slice; if still unresolvable, add to the Conflict Table.
11. **Update `_STATUS.md`.** If current state is `OPEN`, set to `INITIALIZED` with run-record reference. If current state is anything else, do not modify status.
12. **Write the run record.** Persist `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` capturing tools used, outputs produced, missing items, needs-human-ruling items, dependency notes, and applied changes.

## Verification

| Check | Method | Pass Criterion |
|---|---|---|
| Four documents present | File listing in `{DELIVERABLE_PATH}` | Datasheet, Specification, Guidance, Procedure all exist |
| Default sections present | Section-heading grep per document | Datasheet has Identification/Attributes/Conditions/Construction/References; Specification has Scope/Requirements/Standards/Verification/Documentation; Guidance has Purpose/Principles/Considerations/Trade-offs/Examples; Procedure has Purpose/Prerequisites/Steps/Verification/Records |
| Source citations on non-trivial values | Manual review of Datasheet and Specification | Every value either cites SourcePath+line or is marked TBD/ASSUMPTION |
| Cross-document consistency | Term/value diff across the four docs | Tank tags, capacities, spacing distances, standards consistent |
| `_STATUS.md` safe update | Read `_STATUS.md` | State == INITIALIZED if it was OPEN before the run; no regression otherwise |
| Run record persisted | File exists in `_run_records/` | Single new run-record file with PENDING -> SUCCESS lifecycle |
| No out-of-scope writes | `git status` filtered to `{DELIVERABLE_PATH}` | All modified/created files are inside the deliverable folder |

## Records

- `Datasheet.md` — primary deliverable artifact
- `Specification.md` — normative requirements set R1..R17
- `Guidance.md` — including Conflict Table for human ruling
- `Procedure.md` — this document
- `_STATUS.md` — OPEN -> INITIALIZED transition recorded
- `_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` — durable run record
- Source slice citations (DBM lines 268, 270, 283, 297, 493, 506, 508, 511-516, 518-524, 2627) embedded in Datasheet and Specification
