# Procedure — DEL-087-03 Construction Work Package (PKG-087 Incinerator)

## Purpose

Procedure to **produce** the Construction Work Package artifact set for PKG-087 Incinerator: the construction work package document, the installation and tie-in workface plan, and the construction interface and turnover checklist (`_CONTEXT.md` Anticipated Artifacts).

## Prerequisites

### Inputs (must be present before substantive drafting)

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local — present).
- GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv` (present).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (present, locally accessible).
- DEL-087-01 Scope of Work (sibling — not yet declared in `_DEPENDENCIES.md`; ASSUMPTION upstream).
- DEL-087-02 Package Datasheet (sibling — not yet declared in `_DEPENDENCIES.md`; ASSUMPTION upstream).
- `26020-Package_Requirements.docx` package heading 40 — referenced but not locally readable as text. **TBD: stage as a markdown source slice before progressing past this pass.**
- `26020-01-PT-RFQ-25-003_Incinerator.docx` — not locally accessible. **TBD.**

### Declared dependencies

`_DEPENDENCIES.md` lists no declared upstream or downstream dependencies. Per the dependency-tracking mode (DECLARED), this is not a blocker, but the sibling EPC anchor deliverables (DEL-087-01, DEL-087-02) and the Package Vendor outputs (DEL-087-04, DEL-087-05) are real upstream/downstream relationships that should be declared by the human when ready.

## Steps

### Stage A — Establish package construction basis

1. Read PACKAGE_REGISTER.csv row PKG-087 to confirm equipment list and split-of-responsibility (Package Vendor vs. EPC Integrator).
2. Read INTERFACE_REGISTER.csv rows for PKG-087 (twelve entries) and enumerate each as a discrete tie-in workstream.
3. Read accessible source slices in `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` for incinerator-relevant content (lines 56, 389-402, 547-555).
4. Record open items (service allocation, permit-final emissions) explicitly in the CWP.

### Stage B — Produce installation and tie-in workface plan

5. For each of the twelve interfaces, draft a workface plan section containing: scope of tie-in, boundary point (battery limit), prerequisite construction, sequencing relative to package erection, ITP hooks, and turnover criterion.
6. For Process Piping and Relief / Flare / Vent tie-ins, explicitly preserve the spent-caustic storage tank flame-arrestor vent path to the incinerator header (DBM line 402).
7. For Utility Piping tie-ins, coordinate with 04-25 supply (fuel gas, instrument air, electrical power — DBM line 56).
8. Mark all design values (pressures, temperatures, flows, loadings) as TBD pending DEL-087-02 Package Datasheet completion and source-slice staging of `26020-01-PT-RFQ-25-003_Incinerator.docx`.

### Stage C — Produce construction interface and turnover checklist

9. Build the turnover checklist from the twelve interface IDs (Stage A.2) and from the equipment list (knockout drum, transfer pump, LP flare stack, blower).
10. Include open-interface items (C-01 service allocation) as explicit unresolved entries.

### Stage D — Verification and human ruling routing

11. Run the cross-document consistency checks defined in `Guidance.md` Conflict Table; route C-01..C-04 to the human as `NEEDS_HUMAN_RULING`.
12. Confirm that no requirement, design value, or procedural step has been created from decomposition prose where source text is actually accessible (skill non-negotiable constraint).

### Stage E — Closeout

13. Update `_STATUS.md` only via the safe `OPEN → INITIALIZED` transition through `tools/scaffolding/write_status.sh`. (TASK shell performs this; see this run's `_run_records/` entry.)
14. Record the run in `_run_records/`.

## Verification

| Check | Method | Pass condition |
|---|---|---|
| Equipment coverage | Cross-walk equipment list against PACKAGE_REGISTER.csv PKG-087 | 4-of-4 items addressed |
| Interface coverage | Cross-walk workface plan against INTERFACE_REGISTER.csv PKG-087 (12 rows) | 12-of-12 interfaces addressed |
| SOW coverage | Cross-walk to SOW-0111..SOW-0114 | 4-of-4 SOW IDs referenced |
| Source grounding | Each non-trivial design statement cites a source slice or is marked TBD/ASSUMPTION | No unsourced design assertions |
| No invention | No permit-final emissions numbers introduced; no clause-level code requirements introduced without accessible source | Pass |
| Consistency | Terminology and equipment names consistent across Datasheet / Specification / Guidance / Procedure | Pass |

## Records

The following records result from executing this procedure:

- The Construction Work Package document (this deliverable's primary artifact, drafted from these four documents).
- Installation and tie-in workface plan (twelve interface sections).
- Construction interface and turnover checklist.
- This deliverable's `_run_records/TASK_RUN_*.md` entries (one per run of the `four-documents` skill).
- Human-ruling resolutions for Conflict Table entries C-01..C-04 (when supplied).
