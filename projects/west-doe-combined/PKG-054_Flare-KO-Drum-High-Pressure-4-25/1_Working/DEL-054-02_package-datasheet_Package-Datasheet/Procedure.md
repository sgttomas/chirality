# Procedure — Producing the Package Datasheet for Flare KO Drum (High Pressure) 4-25 (PKG-054)

> Operational steps for the EPC Integrator (or delegated TASK) to produce, review, and turn over the `DEL-054-02_package-datasheet` deliverable. Interpretation per skill convention: this procedure addresses how to **produce** the datasheet artifact. Steps for vendor *use* of the package are out of scope (covered by `DEL-054-04` and `DEL-054-06`).

## Purpose

Produce a source-grounded EPC Package Datasheet for PKG-054 that satisfies the requirements in `Specification.md`, captures the design basis from the Deepcut DBM, and surfaces interface facts and open items for downstream vendor engineering.

## Prerequisites

### Inputs / references

- `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- GATE-07 PROJECT_DECOMP snapshot at `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- DBM-Deepcut source file at `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (especially Sec. Flare Systems Basis and the tag tables).
- DBM-Comp_and_Liquids source file at `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` for project-wide pump-sparing and shared-stack basis.
- Native source files (to be parsed in a follow-up pass): `26020-Package_Requirements.docx` (package heading 9), `26020-Packages_Interfaces_4_export.xlsx`.

### Declared dependencies

- Per `_DEPENDENCIES.md`: no upstream or downstream dependencies are declared during PREPARATION. Coordination mode is DECLARED. Treat extracted info-flow summaries as context only.

### State precondition

- `_STATUS.md` must be in `OPEN` or `INITIALIZED` (within `ALLOW_OVERWRITE_STATES`) for the four-document kit to be overwritten by the four-documents skill.

## Steps

1. **Read deliverable-local context.** Open `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, and the placeholder `_SEMANTIC.md`. Extract identity (PKG-054, DEL-054-02), discipline (Mechanical), responsible party (EPC Integrator), scope items (`SOW-0075`-`SOW-0078`), and supported objectives.
2. **Locate the decomposition row.** In the GATE-07 `DELIVERABLE_REGISTER.csv`, find the `DEL-054-02_package-datasheet` row and confirm the package name "Flare KO Drum (High Pressure) 4-25", workbook row 55, and the Source Reference (Workbook Packages row 55; 26020-Package_Requirements.docx package heading 9).
3. **Open accessible source slices.**
   - DBM-Deepcut Sec. Flare and Incinerator Spacing (around line 276) for spacing constraints.
   - DBM-Deepcut Sec. Flare Systems Basis → Flare Equipment and Routing (lines 2019-2034) for service envelope, header sizes, KO drum tags, pump tags, and routing.
   - DBM-Deepcut Sec. Flare Header and Backpressure Basis (lines 2035-2046) for material, sizing, and backpressure values.
   - DBM-Deepcut tag tables and module table (lines 2533-2585, 2783-2786) for V-4100-1 / P-4100-1 / Module 410-1.
   - DBM-Comp_and_Liquids Sec. Flare and Blowdown (lines 495-499) and Pump sparing table (line 583) for cross-facility context.
4. **Identify Conflicts.** Compare DBM line 2028 (truck-out) against DBM line 1665 (flare KO drum pumps to condensate slop tank). Record as CONF-01 in `Guidance.md`. Add the naming reconciliation (CONF-02) and pump-sparing inference (CONF-03).
5. **Draft `Datasheet.md`** using the default schema (Identification, Attributes, Conditions, Construction, References). Populate Identification entirely from `_CONTEXT.md` and the DBM tag table. Populate Attributes / Conditions / Construction from the cited DBM lines. Mark missing values (vessel dimensions, design P/T, MOC, pump curve, relief load set) as TBD with a brief note on which source would supply them.
6. **Draft `Specification.md`** with normative requirements (REQ-DS-01..REQ-DS-15) traceable to the cited DBM slices and `_CONTEXT.md`. Populate Standards (OGAOM, BCER, API 2510, ASME BPVC Sec. VIII Div. 1 ASSUMPTION, ASME B31.3 ASSUMPTION) with `location TBD` where the full standard text is not locally accessible. Define Verification and Documentation accordingly.
7. **Draft `Guidance.md`** with Purpose, Principles, Considerations, Trade-offs, Examples, and the Conflict Table.
8. **Draft this `Procedure.md`** (covering production of the datasheet artifact and its review/turnover steps).
9. **Run Pass 2 cross-reference consistency checks** as specified in `skills/four-documents/SKILL.md` Step 5:
   - Datasheet ↔ Specification: V-4100-1, P-4100-1, Module 410-1, 508 mm relief header, 695 kPag backpressure, 1172 kPag PSV-flange limit, 10 m spacing all consistent.
   - Specification ↔ Guidance: every REQ has rationale in Principles or Considerations.
   - Specification ↔ Procedure: every REQ has a verification hook (datasheet review or cross-reference check).
   - Terminology: "V-4100-1", "HP flare KO drum", "Module 410-1", "P-4100-1", "HP flare", "HP/cryo stack" used consistently.
   - Values: 508 mm, 762 mm, 695 kPag, 1172 kPag, 10 m, 20 MJ/Sm3 are quoted identically across documents.
10. **Update `_STATUS.md`** from `OPEN` to `INITIALIZED` using `tools/scaffolding/write_status.sh` with the `TASK+four-documents` reason token.
11. **Write the run record** at `_run_records/TASK_RUN_<timestamp>.md` with full input echo, resolved state, tools used, outputs produced, missing items, and TBD/conflict surfacing.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| All four documents exist | Directory listing | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present |
| Default schema sections present | Heading scan in each doc | All default sections from the skill schema table present |
| At least one accessible source was read | Citations in `Datasheet.md` / `Specification.md` | DBM-Deepcut line citations present |
| Non-trivial values are cited or marked TBD/ASSUMPTION | Manual review | No bare numeric values without a source or label |
| Cross-document consistency | Manual sweep using Step 9 checklist | All checks pass; otherwise Conflict Table entry exists |
| `_STATUS.md` lifecycle | Read updated `_STATUS.md` | Current state = `INITIALIZED`; History entry appended |
| Run record written | List `_run_records/` | `TASK_RUN_<timestamp>.md` exists with run-status `SUCCESS` |
| No out-of-scope writes | Review changed paths | All writes confined to this deliverable folder |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this file).
- Updated `_STATUS.md` (`OPEN` → `INITIALIZED`).
- Run record at `_run_records/TASK_RUN_2026-05-25_0424.md`.
- Conflict Table entries (CONF-01, CONF-02, CONF-03) in `Guidance.md` awaiting human ruling.
- Open items / TBDs surfaced in `Datasheet.md` Open Items section, to be resolved during Pass 3 semantic lensing (`RUN_PASSES: P3_ONLY` after `_SEMANTIC_LENSING.md` is produced) and during detailed design.
