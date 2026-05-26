# Procedure — DEL-063-01 Scope of Work (PKG-063 Tanks, DSO (API 650))

## Purpose

Produce the EPC Integrator's `PKG-063` Scope of Work artifact set such that the Specification requirements (SPEC-063-01-R01 through R13) are satisfied with source-grounded content, explicit `TBD` markers where source is not locally accessible, and open items captured for human ruling in the Conflict Table.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-063 row at WorkbookRow=90, CoA 26020-01-19-001)
  - `DELIVERABLE_REGISTER.csv` (DEL-063-01 row and sibling DEL-063-02 … DEL-063-06)
  - `SCOPE_LEDGER.csv` (SOW-0209 through SOW-0212)
  - `ARTIFACT_REGISTER.csv` (DEL-063-01 rows: ART-8D38072F13, ART-469823FD54, ART-B502E838FB, ART-42CDF63E00, ART-A0E63EAD7C)
  - `INTERFACE_REGISTER.csv` (nine PKG-063 rows)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-063-01 rows)
- Access to the accessible source slice `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (disulphide-oil disposition paragraph; DSO-disposal open-issue table; site/spacing tables citing API 2510 / NFPA 30 / OGAOM).
- ASSUMPTION: where deeper source extraction is needed (tag numbers, design-conditions detail text, coating-product selection, equipment heading detail), retrieve source slices from `26020-Package_Requirements.docx` package heading 18 (residing in `_Sources/`). If not locally extracted, treat as `location TBD`.
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-063-02` … `DEL-063-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-063 row and `DELIVERABLE_REGISTER.csv` DEL-063-01 row. Verify workbook row 90, WBS 01, CoA tracking 26020-01-19-001, discipline Mechanical, package name "Tanks, DSO (API 650)".
2. **Function statement.** Reproduce SOW-0210 (basic scope: supply one atmospheric DSO storage tank receiving level-controlled DSO from the DSO separator in the caustic regeneration system). Verify wording is faithful to source.
3. **Major-equipment description.** Reproduce SOW-0211 verbatim: modified API 650; 400 bbl nominal; atmospheric; design pressure 32 oz, 1.0 oz vacuum; heater at 32.2 °C (90 °F) minimum (vendor-designed); internal coating (floor, walls, roof); insulation for pour-point maintenance (minimum temperature TBD).
4. **By-others / boundary carve-out.** Reproduce SOW-0212 by-others list (foundations, on-site mounting, E&I, platforms, staircase) and the design-condition statement (atmospheric; minimum ambient TBD; design pressure 32 oz / 1.0 oz vacuum; flow rate TBD; 400 bbl; throughput TBC).
5. **Process integration narrative.** Cite the 04-25 DBM disulphide-oil paragraph: DSO is a by-product of the NGL non-regenerative caustic treating process; truck-out is the current basis; alternate C5+ mixing is an open item for detailed engineering.
6. **Interface enumeration.** Cross-reference the nine applicable interface types from `INTERFACE_REGISTER.csv` PKG-063 rows: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Note explicitly that Electrical Power and EHT are not listed even though the package contains a heater (heater is vendor-internal; on-site E&I is by-others per SOW-0212).
7. **Responsibility assignment record.** Reproduce the responsibility model from `PACKAGE_REGISTER.csv` PKG-063 (Package Vendor scope; EPC Integrator integration scope).
8. **Source basis.** List Workbook Packages row 90, `26020-Package_Requirements.docx` heading 18, `DBM-Deepcut/4-25_Deepcut_DBM.md`; label `Bid Docs/_Budgetary/26020-01-PT-RFQ-19-001_Tanks_DSO_R0.docx` as budgetary-only / informational.
9. **Objectives + scope items.** Echo `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `{SOW-0209, SOW-0210, SOW-0211, SOW-0212}` from `SCOPE_LEDGER.csv`.
10. **TBD audit.** Any design value (minimum pour-point temperature, capacity/throughput, operating flow rate, coating product, equipment tag number, alternate-disposal commitment, code/standard citations beyond modified API 650) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer.
11. **Conflict capture.** Record the five open items as Conflict Table entries in Guidance: heating system architecture (CONF-063-01-01); DSO disposal routing (CONF-063-01-02); internal coating product (CONF-063-01-03); equipment tag number (CONF-063-01-04); sour-service classification (CONF-063-01-05).
12. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-063, "Tanks, DSO (API 650)", DSO Storage Tank, 400 bbl, modified API 650, 32.2 °C / 90 °F, 32 oz / 1.0 oz vacuum), the same scope items, the same objectives, and the same nine interface types.
13. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-063 row in `PACKAGE_REGISTER.csv` (every field, including CoA 26020-01-19-001). |
| 2 | SOW-0210 text is present in the function statement (DSO separator, level-controlled, caustic regeneration system). |
| 3 | SOW-0211 numeric/textual elements all present: modified API 650, 400 bbl, atmospheric, 32 oz / 1.0 oz vacuum, heater at 32.2 °C (90 °F) minimum, internal coating, insulation for pour point. |
| 4 | By-others list per SOW-0212 enumerates foundations, mounting, E&I, platforms, staircase. |
| 5 | Process-integration narrative cites the 04-25 DBM DSO paragraph and the DSO-disposal open issue. |
| 6 | The nine `INTERFACE_REGISTER.csv` interface types for PKG-063 are listed and no extra interfaces are claimed; Electrical Power / EHT absence is acknowledged. |
| 7 | Responsibility text preserves the Package Vendor / EPC Integrator split verbatim or as a faithful paraphrase. |
| 8 | Source-basis list cites Workbook row 90, package requirements doc heading 18, and the 04-25 DBM; budgetary RFQ go-by labeled informational. |
| 9 | Objective set equals `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`; scope set equals `{SOW-0209, SOW-0210, SOW-0211, SOW-0212}`. |
| 10 | No unsourced numeric value exists outside a `TBD` cell. |
| 11 | Conflict Table present in Guidance with the five identified conflict IDs. |
| 12 | Same terms, values, and lists appear in all four documents (no aliases or numeric drift). |
| 13 | `_STATUS.md` state transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only: `OPEN → INITIALIZED`).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING items, and `NEEDS_HUMAN_RULING` items mirroring the Conflict Table.
- Conflict Table entries in `Guidance.md` (CONF-063-01-01 through CONF-063-01-05) carry forward as `NEEDS_HUMAN_RULING` items into the run record.
