# Procedure — DEL-069-01 Scope of Work (PKG-069 Mole Sieve Drier Unit (Gas))

## Purpose

Produce the EPC Integrator's `PKG-069` Scope of Work artifact set such that the Specification requirements (SPEC-069-01-R01 through R14) are satisfied with source-grounded content and explicit `TBD` markers where source is not locally accessible.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-069 row, WorkbookRow=73)
  - `DELIVERABLE_REGISTER.csv` (DEL-069-01 row and siblings DEL-069-02 … DEL-069-06)
  - `SCOPE_LEDGER.csv` (SOW-0144)
  - `ARTIFACT_REGISTER.csv` (DEL-069-01 rows: ART-CA6ACF97B8, ART-E3BAD449B0, ART-ED8784A9C5, ART-875349E7C7)
  - `INTERFACE_REGISTER.csv` (PKG-069 rows: 12 interface types)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-069-01 rows)
- Access to source materials in `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/`:
  - `DBM-Deepcut/4-25_Deepcut_DBM.md` — mole sieve narrative (~line 1243), adsorber configuration (~line 1263), equipment inventory row 56 (~line 2607), spares table (~line 2362), regeneration heat narrative (~line 1947), moisture analyzers (~line 2134), isolation philosophy (~line 2408).
  - `26020-Package_Requirements.docx` — row-73 heading (clause-level design conditions; not locally extracted as Markdown — treat as `location TBD`).
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-069-02` … `DEL-069-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-069 row and `DELIVERABLE_REGISTER.csv` DEL-069-01 row. Verify workbook row 73, WBS 01, CoA tracking 26020-01-22-002, discipline Mechanical, package name "Mole Sieve Drier Unit (Gas)".
2. **Function and configuration.** Reproduce the mole sieve narrative (DBM line ~1243): TEG dehydration upstream, two 100% inlet filter/coalescers, three driers in adsorption/standby/regeneration/cooling cycle, dust filtration + mercury recovery downstream to cryogenic unit. Reproduce the adsorber-configuration row (DBM line ~1263, downflow adsorption).
3. **Tagged equipment list.** Reproduce the DBM row-56 equipment inventory verbatim by tag: `AC-6180-1`, `K-6190-1`, `K-6195-1`, `F-5910-1`, `F-5920-1`, `F-6151-1`, `F-6155-1`, `E-6170-1`, `V-6160-1`, `V-6130-1`, `V-6140-1`, `V-6150-1`, `V-6185-1`.
4. **Regeneration heating.** Reproduce DBM line ~1947 statement that mole sieve regeneration gas heating is removed from the unified heat medium loop and is served by a separate direct-fired heater. Flag the heater scope-split as `CONF-069-01-02` in the Guidance Conflict Table.
5. **Interface enumeration.** Reproduce the twelve `INTERFACE_REGISTER.csv` interface types for PKG-069 in the Construction section: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
6. **Responsibility assignment record.** Reproduce the responsibility model from `PACKAGE_REGISTER.csv` PKG-069 (Package Vendor scope; EPC Integrator integration scope).
7. **Source basis.** List Workbook Packages row 73, `26020-Package_Requirements.docx` row-73 heading (location TBD for clause-level extraction), `DBM-Deepcut/4-25_Deepcut_DBM.md` (mole sieve narrative line ~1243; equipment inventory row 56 line ~2607; sparing line ~2362; regeneration heat line ~1947; moisture analyzers line ~2134; isolation philosophy line ~2408).
8. **Objectives + scope items.** Echo `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}` and `{SOW-0144}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `SCOPE_LEDGER.csv`.
9. **Gate-6 disposition.** Reproduce the Gate-6 disposition note from `PACKAGE_REGISTER.csv` PKG-069 NotesRaw and flag `CONF-069-01-01` (package-boundary disposition vs. cryogenic-unit consolidation) in the Guidance Conflict Table.
10. **Moisture analyzer + isolation context.** Carry DBM moisture-analyzer narrative (line ~2134) and unit-isolation philosophy (line ~2408) where they bear on package boundary. Flag `CONF-069-01-03` (analyzer scope-split) in the Guidance Conflict Table.
11. **TBD audit.** Any design value (P, T, bed sizing, cycle time, regeneration heater duty, materials, code citations) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer. Capture as `CONF-069-01-04`.
12. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-069, the 13 equipment tags, the 12 interface types, the 9 objectives, SOW-0144), the same Gate-6 disposition statement, and the same regeneration-heat narrative.
13. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-069 row in `PACKAGE_REGISTER.csv` (every field). |
| 2 | Mole sieve narrative (DBM line ~1243) and adsorber-configuration row (~line 1263) are present and verbatim or faithfully paraphrased. |
| 3 | Tagged-equipment list contains all 13 tags from DBM row 56 exactly. |
| 4 | Regeneration heating statement preserves the "removed from unified heat medium loop / separate direct-fired heater" fact. |
| 5 | Declared interface types equal the 12 entries in `INTERFACE_REGISTER.csv` for PKG-069. |
| 6 | Responsibility text preserves vendor/EPC split. |
| 7 | Source basis list cites Workbook row 73, package requirements doc heading (location TBD), and DBM line references. |
| 8 | Objective set equals `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`; scope set equals `{SOW-0144}`. |
| 9 | Gate-6 disposition statement present in Datasheet and Specification; CONF-069-01-01 captured in Guidance. |
| 10 | Moisture-analysis and isolation statements present in Datasheet; CONF-069-01-03 captured. |
| 11 | No unsourced numeric value exists outside a `TBD` cell; CONF-069-01-04 captured. |
| 12 | Same terms, tags, lists, and dispositions appear in all four documents (no aliases). |
| 13 | `_STATUS.md` State transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only): `OPEN → INITIALIZED`.
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING items, and NEEDS_HUMAN_RULING items (the four Conflict Table entries CONF-069-01-01 through CONF-069-01-04 carry forward).
