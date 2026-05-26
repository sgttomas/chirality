# Procedure — DEL-058-01 Scope of Work (PKG-058 Medium Pressure Flash Feed Separator)

## Purpose

Produce the EPC Integrator's `PKG-058` Scope of Work artifact set such that the Specification requirements (SPEC-058-01-R01 through R13) are satisfied with source-grounded content and explicit `TBD` markers where source is not locally accessible.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-058 row)
  - `DELIVERABLE_REGISTER.csv` (DEL-058-01 row and sibling DEL-058-02 … DEL-058-06)
  - `SCOPE_LEDGER.csv` (SOW-0139, SOW-0140, SOW-0141, SOW-0142)
  - `ARTIFACT_REGISTER.csv` (DEL-058-01 rows: ART-060CD62000, ART-D3168A53CC, ART-5F228F6180, ART-2F011685B1, ART-4F926E1593)
  - `INTERFACE_REGISTER.csv` (PKG-058 rows — nine interface types)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-058-01 rows)
- Locally accessible source materials in `_Sources/`:
  - `DBM-Deepcut/4-25_Deepcut_DBM.md` (read MPFF section, MPFF and Stabilizer Train Relationship, MPFF Operating and Capacity Basis, interface descriptions).
  - `26020-Package_Requirements.docx` package heading 13 — binary; not locally extracted; treat as `location TBD` beyond what is reproduced in `SCOPE_LEDGER.csv` SOW-0139..SOW-0142.
  - `Bid Docs/Budgetary/26020-01-PT-RFQ-17-006_MPFF Separator_R0.docx` — budgetary Word source; label informational.
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-058-02` … `DEL-058-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-058 row and `DELIVERABLE_REGISTER.csv` DEL-058-01 row. Verify workbook row 71, WBS 01, CoA tracking 26020-01-17-006, discipline Mechanical.
2. **Function and equipment.** Reproduce SOW-0140 (basic scope) and SOW-0141 (major included equipment — mistex mist extractor, building module, 2 PITs, 1 TIT, 2 LTs, 1 inlet LCV) as the package function and tagged-equipment artifacts. Add facility-DBM vessel tags `V-7110-1` and `V-7310-1` as ASSUMPTION.
3. **Conditions block.** Populate operating and design conditions from SOW-0142 verbatim: Normal Throughput 7,883 m³/h; Maximum Throughput 15,223 m³/h; Operating Pressure 1,724 kPag; Operating Inlet Flow 7,883 m³/h; Operating Inlet Temperature −9.55 °C; Design Pressure TBD; Flange Rating ASME Class 300; Design Inlet Flow Rate 15,223 m³/h; Design Temperature −40 °C. Surface the DBM 40 °C assumed value as a CONFLICT entry (CONF-058-01-01).
4. **By-others enumeration.** Reproduce SOW-0142 by-others list: interconnecting piping at skid edge; DCS integration; foundations; electrical power supply from plant MCC; installation/erection. Cross-walk to the nine declared interface types and the Electrical Power gap (CONF-058-01-03).
5. **Integration narrative.** Compose an integration narrative grounded in `DBM-Deepcut/4-25_Deepcut_DBM.md` MPFF section: upstream inlet-separator liquid outlet heater feed; level-controlled inlet LCV; overhead vapour pressure-regulated to SOC 3rd-stage suction; bottoms condensate level-controlled to the downstream stabilizer flash/feed separator; LP fuel gas purge from downstream of fuel-gas scrubber; automated blowdown to HP flare; 2 x 100% normal operating sparing with one MPFF-per-stabilizer train pairing.
6. **Responsibility assignment record.** Reproduce the responsibility model verbatim from `PACKAGE_REGISTER.csv` PKG-058 (Package Vendor scope; EPC Integrator integration scope).
7. **Source basis.** List Workbook Packages row 71, `26020-Package_Requirements.docx` heading 13, `DBM-Deepcut/4-25_Deepcut_DBM.md`; label `Bid Docs/Budgetary/26020-01-PT-RFQ-17-006_MPFF Separator_R0.docx` as budgetary informational only.
8. **Objectives + scope items.** Echo `{OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}` and `{SOW-0139, SOW-0140, SOW-0141, SOW-0142}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `SCOPE_LEDGER.csv`.
9. **TBD audit.** Any design value (Design Pressure, materials, vessel geometry, code citations) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer.
10. **Conflict capture.** Record open ownership/extraction/temperature/tag conflicts in the Guidance Conflict Table with proposed authority and `TBD` human ruling.
11. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-058, MPFF, mistex mist extractor, SOC 3rd-stage suction, inlet separator liquid outlet heater), the same scope items, the same objectives, the same nine interface types, and the same condition values.
12. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-058 row in `PACKAGE_REGISTER.csv` (every field). |
| 2 | SOW-0140 and SOW-0141 text is present; mist extractor named "mistex"; instrument counts exact. |
| 3 | Operating/design conditions reproduce SOW-0142 numerics verbatim; Design Pressure shown as TBD; DBM 40 °C surfaced as CONFLICT. |
| 4 | By-others list reproduces SOW-0142; cross-walk to interface set explicit; Electrical Power gap surfaced as CONFLICT. |
| 5 | Integration narrative explicitly names upstream inlet-separator liquid outlet heater, downstream stabilizer flash/feed separator, and SOC 3rd-stage suction; train pairing and 2 x 100% sparing referenced. |
| 6 | Responsibility text preserves vendor/EPC split verbatim. |
| 7 | Source basis list cites all required sources; Word budgetary source labeled informational. |
| 8 | Objective set equals `{OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`; scope set equals `{SOW-0139, SOW-0140, SOW-0141, SOW-0142}`. |
| 9 | No unsourced numeric value exists outside a `TBD` cell. |
| 10 | Conflict Table present in Guidance with at least the temperature, EHT/methanol, Electrical-Power-gap, Design-Pressure-extraction, and tag-binding items. |
| 11 | Same terms, tags, and lists appear in all four documents (no aliases). |
| 12 | `_STATUS.md` State transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING, and any NEEDS_HUMAN_RULING items.
- Conflict Table entries in `Guidance.md` carry forward as `NEEDS_HUMAN_RULING` items into the run record.
