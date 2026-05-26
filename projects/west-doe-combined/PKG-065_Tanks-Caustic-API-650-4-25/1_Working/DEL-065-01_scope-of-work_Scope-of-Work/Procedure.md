# Procedure — DEL-065-01 Scope of Work — Tanks, Caustic (API 650) 4-25 (PKG-065)

## Purpose

Operational procedure for producing and maintaining the EPC Scope of Work artifact for PKG-065. This procedure is for the EPC Integrator authoring team and reviewers; it is not an equipment operating procedure.

## Prerequisites

- Read deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` (placeholder).
- Read GATE-07 PROJECT_DECOMP snapshot rows: `DELIVERABLE_REGISTER.csv` row DEL-065-01_scope-of-work; `PACKAGE_REGISTER.csv` row PKG-065; `SCOPE_LEDGER.csv` rows SOW-0197, SOW-0198, SOW-0199, SOW-0200.
- Read accessible source slices: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (NGL mercaptan treating unit, caustic tanks subsections).
- Note inaccessible sources (relay-only basis): `26020-Package_Requirements.docx` heading 20 (`.docx`); Workbook Packages row 87 (`.xlsx`); Bid Docs `26020-01-PT-RFQ-19-003_Tanks_Caust_2_R0.docx` (`TBD` — not locally present in `_Sources`).
- Confirm `_STATUS.md` Current State is in `ALLOW_OVERWRITE_STATES` (OPEN, INITIALIZED) per brief.
- Declared upstream/downstream dependencies in `_DEPENDENCIES.md`: none declared during PREPARATION (treat as advisory; cross-package interface to PKG containing the pressurized caustic drain drum is `TBD`).

## Steps

1. **Identity confirmation.** Confirm package identity from PACKAGE_REGISTER row PKG-065 (Workbook row 87; Mechanical; WBS 01; Vendor Tracking 26020-01-PT-19-003; package name). Reflect in Datasheet Identification table.
2. **Tagged equipment enumeration.** List `TK-6780-1` (spent caustic, per SOW-0199) and one fresh caustic tank (tag `TBD`, per SOW-0198 + DBM-Deepcut). Do NOT add equipment that is not asserted in SOW rows for PKG-065 (e.g., `V-6940-1`).
3. **Responsibility split.** Reflect the PACKAGE_REGISTER Responsibility field: Package Vendor owns engineering/design/equipment/documentation; EPC Integrator owns facility integration and interfaces. Carry the applicable interface types verbatim.
4. **Requirements derivation.** For each requirement, cite the source slice (SOW row and/or DBM-Deepcut section). Mark inferences as `ASSUMPTION` and missing values as `TBD`. Do NOT derive requirements from decomposition prose when the source slice does not support them.
5. **By-others enumeration.** Carry the SOW-0200 by-others list verbatim into the Specification Scope (out-of-scope subsection).
6. **Integration narrative.** Summarize the package's role in the 4-25 NGL mercaptan treating loop using only DBM-Deepcut text. Avoid asserting plant-wide claims beyond DBM coverage.
7. **Cross-document consistency sweep.** Confirm tags, quantities, capacities, design conditions, and material requirements match across Datasheet, Specification, Guidance, and this Procedure. Capture unresolved items in the Guidance Conflict Table.
8. **Status update.** If `_STATUS.md` is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` to transition to `INITIALIZED`. Do not regress state.
9. **Run record.** Write `_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved state, tools used, outputs, missing items, and human-ruling needs.

## Verification

| Check | Pass criterion |
|---|---|
| Four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present in deliverable folder. |
| Default sections present | Each document carries its default schema sections per skill SKILL.md. |
| Source grounding | Each substantive requirement/value cites a source (SOW row, PACKAGE_REGISTER, or DBM section); inferred items labeled `ASSUMPTION`; unknowns marked `TBD`. |
| Cross-document consistency | Tag list, capacities, design pressure, material requirements, vent routing, and by-others list agree across all four documents. |
| Scope discipline | No requirements asserted from binary sources that were not surfaced via extraction; `.docx`/`.xlsx`-only items recorded as `TBD` with provenance. |
| Status discipline | `_STATUS.md` transitions only from `OPEN` to `INITIALIZED`; no regression. |
| Metadata immutability | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` unchanged. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated `OPEN → INITIALIZED` (TASK+four-documents).
- `_run_records/TASK_RUN_2026-05-25_0437.md`.
- Guidance Conflict Table entries (CFT-065-01-01 fresh-tank tag; CFT-065-01-02 V-6940-1 assignment; CFT-065-01-03 binary-source extraction completeness) pending human ruling.
