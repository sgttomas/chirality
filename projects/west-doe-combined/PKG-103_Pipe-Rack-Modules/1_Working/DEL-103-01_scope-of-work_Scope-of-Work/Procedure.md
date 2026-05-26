# Procedure — DEL-103-01 Scope of Work (Pipe Rack Modules)

> Operational steps to **produce** the Scope of Work artifact for PKG-103 and to verify it against accessible authoritative sources. Steps are source-grounded; judgement points are marked TBD.

## Purpose

Produce a complete, source-grounded EPC Integrator Scope of Work artifact for PKG-103 that satisfies all requirements in `Specification.md`, surfaces the conflicts in `Guidance.md`, and is suitable as the Gate 5 EPC anchor record.

## Prerequisites

- **Declared upstream dependencies (per `_DEPENDENCIES.md`):** None declared during PREPARATION. Drafter SHOULD nevertheless confirm the following inputs are available in the snapshot referenced by `_REFERENCES.md`.
- **Required references (must be open before drafting):**
  - Gate-07 PROJECT_DECOMP snapshot:
    - `PACKAGE_REGISTER.csv` row 104
    - `DELIVERABLE_REGISTER.csv` row 584 (and rows 585-587 for sibling deliverables)
    - `SCOPE_LEDGER.csv` row 260 (SOW-0259)
    - `INTERFACE_REGISTER.csv` rows 909-917
    - `OBJECTIVE_REGISTER.csv` rows for OBJ-002, OBJ-005..OBJ-010
  - DBM source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (sections at lines 38, 688, 700, 722)
  - Workbook: `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 104 (binary — read via PACKAGE_REGISTER mirror; flag divergences)
  - Workbook: `_Sources/26020-Package_Requirements.docx` (binary; PKG-103 heading `location TBD`)
- **Deliverable-local files (must be reviewed, not modified):** `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- **`_STATUS.md` precondition:** Current state must be `OPEN` or `INITIALIZED` for drafting to proceed.

## Steps

1. **Verify package identity.** Confirm PKG-103 fields (workbook tracking number 26020-03-36-003, WBS 03, Structural, package name "Pipe Rack Modules") against PACKAGE_REGISTER row 104 and `_CONTEXT.md`. Resolve any mismatch in `_CONTEXT.md`'s favor only if PACKAGE_REGISTER row 104 has been re-validated; otherwise raise as a conflict.
2. **State the workbook-defined package function.** Quote or close-paraphrase SCOPE_LEDGER SOW-0259 statement and PACKAGE_REGISTER row 104 function text. Cite both rows.
3. **Assert EPC Integrator design ownership.** Insert the Gate 6 disposition verbatim from INTERFACE_REGISTER rows 909-917 ("pipe racks and pipe rack modules are designed exclusively by the EPC Integrator"). Cite at least one IFC row ID.
4. **Enumerate interfaces.** List all nine interface types from PACKAGE_REGISTER row 104 / INTERFACE_REGISTER rows 909-917 with IFC IDs alongside. Do not invent additional interface types.
5. **Draft the integration narrative.** Write the whole-facility integration narrative grounded in DBM-Comp_and_Liquids line 38 (civil and infrastructure context) and lines 688/700 (civil/foundation context). Do not add facility-integration claims unsupported by these slices; mark unsupported claims TBD.
6. **Populate anticipated artifacts.** List the four anticipated artifacts from DELIVERABLE_REGISTER row 584 verbatim. For the tagged-equipment list, insert a TBD placeholder citing PACKAGE_REGISTER row 104 note (plot plan/model confirmation pending).
7. **Build the responsibility assignment record.** Use a simple RACI-style or single-line responsibility table naming EPC Integrator as the design-owner Accountable for the rack modules. Do not assign roles not supported by the Gate 6 disposition; mark other roles TBD.
8. **Insert traceability.** Add a traceability block mapping the SoW to SOW-0259 and to OBJ-002, OBJ-005..OBJ-010 with OBJECTIVE_REGISTER row references.
9. **Surface open issues.** Reference DEC-001 against SOW-0259 from SCOPE_LEDGER row 260. If DEC-001 narrative is not locally accessible, state `location TBD` and do not fabricate a description.
10. **Surface upstream inputs.** Note the geotechnical-report dependency (DBM line 688) and foundation design considerations (DBM line 700) as required upstream inputs to rack foundation design — without consuming them in this SoW.
11. **State hazardous-area treatment.** Insert the DBM line 722 default ("outdoor pipe racks are general purpose non-hazardous areas unless detailed classification drawings identify otherwise"). Do not assert a final classification.
12. **Cross-reference sibling deliverables.** Add a section pointing to DEL-103-02, DEL-103-03, DEL-103-04 with one-line descriptors from DELIVERABLE_REGISTER rows 585-587.
13. **Run the Specification conformance pass.** Walk each requirement SPEC-103-01-R01..R14 and confirm an SoW section addresses it. Any unaddressed requirement is a defect; remediate or mark TBD with rationale.
14. **Run the Conflict Table sweep.** Re-read `Guidance.md` Conflict Table CONF-103-01-01..05 and ensure the SoW reflects the PROPOSAL position pending human ruling, with the conflict cited.
15. **Run the cross-document consistency check** against Datasheet, Specification, Guidance (Step 5 of the four-documents skill): terminology, values, and entity names must match across all four documents.

## Verification

| Check | Method | Pass condition |
|---|---|---|
| Identity correctness | Compare SoW header to PACKAGE_REGISTER row 104 | All five identity fields match |
| Interface completeness | Compare SoW interface list to INTERFACE_REGISTER rows 909-917 | All nine interface types listed, each with IFC ID |
| Design-ownership assertion | Inspect responsibility section | Gate 6 EPC-exclusive statement present and cited |
| Anticipated-artifact coverage | Inspect SoW sections | All four anticipated artifacts present; missing-data items TBD-marked |
| Traceability | Inspect traceability block | SOW-0259 and seven OBJs cited |
| Open-issue surfacing | Inspect open-issues section | DEC-001 referenced |
| Source-grounding | Spot-check non-trivial claims | Every non-trivial claim cites a source path/row or carries TBD/ASSUMPTION |
| Cross-document consistency | Diff terminology and values across the four documents | No unexplained divergence |
| `_STATUS.md` safe update | Inspect status helper invocation log | State moved OPEN → INITIALIZED only via `tools/scaffolding/write_status.sh`; no regression |

## Records

The procedure produces, within `{DELIVERABLE_PATH}`:

- The Scope of Work narrative artifact (this deliverable's primary output; embedded in this four-document set).
- The Datasheet, Specification, Guidance, and Procedure files.
- A `_run_records/TASK_RUN_<date>_<HHMM>.md` entry summarising the run, source rereads, and conflicts surfaced.
- A `_STATUS.md` safe update (OPEN → INITIALIZED) recorded via `tools/scaffolding/write_status.sh` when preconditions are met.

No file outside `{DELIVERABLE_PATH}` is written or modified by this procedure.
