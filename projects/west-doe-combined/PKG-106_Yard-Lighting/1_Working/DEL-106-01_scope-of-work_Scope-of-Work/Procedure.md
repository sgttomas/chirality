# Procedure — DEL-106-01 Scope of Work (PKG-106 Yard Lighting)

## Purpose

Produce the EPC Integrator's `PKG-106` Scope of Work artifact set such that the Specification requirements (SPEC-106-01-R01 through R12) are satisfied with source-grounded content and explicit `TBD` markers where source is not locally accessible.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-106 row)
  - `DELIVERABLE_REGISTER.csv` (DEL-106-01 row and sibling DEL-106-02 … DEL-106-06)
  - `SCOPE_LEDGER.csv` (SOW-0011)
  - `ARTIFACT_REGISTER.csv` (DEL-106-01 rows: ART-1D00D7FAE6, ART-508A45C565, ART-C1764AFD92, ART-27C44AFC19)
  - `INTERFACE_REGISTER.csv` (3 PKG-106 rows: IFC-6FCF1B30D6, IFC-DA0D60681B, IFC-ED86F51087)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-106-01 mappings); `OBJECTIVE_SCOPE_MAP.csv` for PKG-106 corroboration.
- ASSUMPTION: where deeper source extraction is needed, retrieve source slices from `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` row 12 (residing in `_Sources/`). If not locally extracted, treat as `location TBD`.
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-106-02` … `DEL-106-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-106 row and `DELIVERABLE_REGISTER.csv` DEL-106-01 row. Verify workbook row 12, WBS TBD (blank in source — do not infer), CoA tracking 26020-01-30-001, discipline Electrical, package name "Yard Lighting".
2. **Function and equipment.** Compose the package function narrative from the workbook description and DBM-Deepcut SEC-12 (lines 3027-3035) and DBM-Comp_and_Liquids SEC-12 (lines 764-770). List major equipment categories (LED yard/area luminaires; mast poles; downcast floodlights; photocell/switch controls; supply circuits; grounding/bonding to facility earth grid). Mark fixture catalog, wattages, pole heights, and counts explicitly `TBD` (vendor design).
3. **Conditions and integration narrative.** Reproduce the SEC-12 design conditions (LED only; suitable for area classification; downward illumination; no horizontally aimed floodlights; photocell/switch control; mast placement away from pad edge) and the -40 deg C ambient (DBM-Comp_and_Liquids SEC-04 line 145) governing outdoor electrical equipment. State explicitly that illuminance targets, photometric basis, and pole/mast counts are `TBD`.
4. **Interface enumeration.** List the 3 PKG-106 interface types from `INTERFACE_REGISTER.csv`: Electrical Power; Grounding / Bonding; Area / Exterior Lighting.
5. **Responsibility assignment record.** Reproduce the responsibility model verbatim from `PACKAGE_REGISTER.csv` PKG-106 (Package Vendor scope; EPC Integrator integration scope). Surface CONF-106-01-01 (workbook vendor-owned vs. SEC-04 field-construction-scope) for human ruling; do not silently reconcile.
6. **Source basis.** List Workbook Packages row 12, DBM-Deepcut SEC-12 (Lighting and Receptacles), DBM-Comp_and_Liquids SEC-12 (Electrical Buildings, Raceways, Lighting, and Heat Tracing); label `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` row 12 as `location TBD` until extracted.
7. **Objectives + scope items.** Echo `{OBJ-001, OBJ-004, OBJ-005, OBJ-009, OBJ-010}` and `{SOW-0011}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `SCOPE_LEDGER.csv`. Mark the objective association as ASSUMPTION at deliverable-ID granularity (PACKAGE_HEURISTIC).
8. **TBD audit.** Any design value (illuminance, pole height, mast count, fixture catalog, wattage, photometric basis, specific fixture/lighting standards beyond CEC, specific regulatory light-pollution citation) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer.
9. **Conflict capture.** Record open conflicts in the Guidance Conflict Table (CONF-106-01-01 vendor-owned vs. field construction; CONF-106-01-02 emergency-egress vs. yard-lighting boundary; CONF-106-01-03 design-values extraction; CONF-106-01-04 regulatory citation; CONF-106-01-05 WBS assignment) with proposed authority and `TBD` human ruling.
10. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-106, Yard Lighting, LED luminaire, mast pole, downcast floodlight, Electrical Power / Grounding / Bonding / Area / Exterior Lighting interfaces), the same scope items, the same objectives, and the same 3 interface types.
11. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-106 row in `PACKAGE_REGISTER.csv` (every field; WBS marked `TBD`). |
| 2 | Package function statement reflects SEC-12 lighting narrative; vendor-to-design quantities flagged. |
| 3 | Conditions appear verbatim or as exact paraphrase from SEC-12 lines 3029, 3031, 3035 and SEC-04 line 145; lux/pole/photometric values marked `TBD`. |
| 4 | The 3 interface types match `INTERFACE_REGISTER.csv` for PKG-106 exactly (set equality with `{Electrical Power, Grounding / Bonding, Area / Exterior Lighting}`). |
| 5 | Responsibility text preserves Vendor/EPC split per `PACKAGE_REGISTER.csv` ResponsibilityModel; CONF-106-01-01 surfaced. |
| 6 | Source basis list cites Workbook row 12, DBM-Deepcut SEC-12, DBM-Comp_and_Liquids SEC-12; package requirements doc and interface xlsx labeled `location TBD`. |
| 7 | Objective set equals `{OBJ-001, OBJ-004, OBJ-005, OBJ-009, OBJ-010}`; scope set equals `{SOW-0011}`. |
| 8 | No unsourced numeric value or material exists outside a `TBD` cell. |
| 9 | Conflict Table present in Guidance with at least the five CONF-106-01-0x items, or explicit "resolved" if resolved. |
| 10 | Same terms, equipment categories, and lists appear in all four documents (no aliases). |
| 11 | `_STATUS.md` State transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING, and any NEEDS_HUMAN_RULING items.
- Conflict Table entries in `Guidance.md` carry forward as `NEEDS_HUMAN_RULING` items into the run record.
