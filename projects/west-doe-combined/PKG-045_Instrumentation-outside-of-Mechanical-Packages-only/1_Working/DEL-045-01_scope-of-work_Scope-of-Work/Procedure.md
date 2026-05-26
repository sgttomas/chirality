# Procedure: DEL-045-01_scope-of-work — Scope of Work

**Interpretation:** This Procedure describes how to *produce* the Scope of Work artifact set for PKG-045. The artifact set, once produced, is itself input to downstream production work (DEL-045-02, DEL-045-03, DEL-045-04).

## Purpose

To produce a source-grounded EPC Scope of Work for PKG-045 covering the four required artifacts (ART-E7B3409573, ART-F40323895F, ART-F820619A3E, ART-34E643FBEB) within the bounds of the active interface set and the accepted decomposition basis.

## Prerequisites

- Accepted upstream decomposition snapshot accessible: GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP (registers and PROJECT_DECOMP.md). [Source: _REFERENCES.md]
- DBM source `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` accessible.
- Workbook Packages row 47 source slice — TBD (not currently locally copied). Procedure can run with TBDs flagged where this slice is the only source.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`. [Source: _DEPENDENCIES.md]
- `_STATUS.md` current state is OPEN or INITIALIZED (otherwise this Procedure does not run; the deliverable belongs to the human reviewer).

## Steps

1. **Confirm package identity.** Read PACKAGE_REGISTER.csv for PKG-045. Record name, workbook ID (45), workbook row (47), CoA tracking number (26020-01-32-002), WBS (03), and discipline (Instrumentation) into the Scope of Work header. Verify against `_CONTEXT.md`.
2. **Pull artifact set.** Read ARTIFACT_REGISTER.csv for `DEL-045-01_scope-of-work`. Record the four artifacts (ART-E7B3409573, ART-F40323895F, ART-F820619A3E, ART-34E643FBEB) and their descriptions as the deliverable's required outputs.
3. **Build the package function and integration narrative (ART-F820619A3E).** From `3-25_Comp_and_Liquids_DBM.md`, extract the role of 03-25 instrumentation outside vendor packages (utility interfaces — instrument air from 04-25, electrical, controls — and the field-installed instrument scope coordinated under DBM construction scope). Write the narrative section. Cite each statement to the DBM section it came from.
4. **Build the tagged equipment and package identity list (ART-F40323895F).** Enumerate only source-supported instrument tags. If the workbook row 47 source slice is not locally accessible, record the list as TBD with a note that population requires the workbook slice. Do not invent tags from generic instrumentation convention.
5. **Define package boundaries against each active interface.** Read INTERFACE_REGISTER.csv rows for PKG-045. For each of IFC-33F8A9F366, IFC-AE76B11E50, IFC-2D030CA850, IFC-210F46B073, IFC-9DAC4D3C4D, record a boundary statement that names the counterpart discipline, what crosses the boundary, and the Gate 6 plug-n-play disposition.
6. **Record exclusions explicitly.** Include: instrumentation inside vendor mechanical packages (from the package title); local 03-25 instrument-air compressor scope superseded by SCA-006 (from DBM). Mark "additional package-specific exclusions: TBD" with the PACKAGE_REGISTER.csv note as basis.
7. **Record the responsibility assignment (ART-34E643FBEB).** Default to EPC Integrator per DELIVERABLE_REGISTER.csv. Flag any discipline-subcontractor assignment only when source-supported. Record the source-dependence note from PACKAGE_REGISTER.csv.
8. **Record the environmental, instrument-air, and electrical/control-separation conditions** from the DBM, with citations.
9. **Cite the accepted upstream snapshot** (GATE-07_Final_Published_2026-05-24) and all source paths used.
10. **Run the cross-document consistency check (Pass 2):** terminology, identifiers, interface IDs, and values must match between Datasheet, Specification, Guidance, and Procedure. Resolve from drafts where possible; otherwise add a Conflict Table row in `Guidance.md`.
11. **Mark labels.** Apply `ASSUMPTION`, `TBD`, or `CONFLICT` per the deliverable-local epistemic contract. Do not silently resolve unknowns.
12. **Update `_STATUS.md`** via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` if and only if current state is `OPEN`. Otherwise do not modify state.

## Verification

| Check | Pass criterion |
|---|---|
| Four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all present in the deliverable folder. |
| Default schema sections present | Each document contains its default section headings (Datasheet: Identification/Attributes/Conditions/Construction/References; Specification: Scope/Requirements/Standards/Verification/Documentation; Guidance: Purpose/Principles/Considerations/Trade-offs/Examples; Procedure: Purpose/Prerequisites/Steps/Verification/Records). |
| Source grounding | Every non-trivial value/requirement either cites a source (SourcePath + SectionRef) or carries `location TBD`/`TBD`/`ASSUMPTION`. |
| Identifiers consistent | DeliverableID, ParentPackageID, interface IDs, artifact IDs are spelled identically across all four documents. |
| Interface set complete | All five active interfaces from INTERFACE_REGISTER.csv appear in Datasheet, Specification, and Procedure. |
| No metadata files modified | `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md` unchanged. `_STATUS.md` only changed when OPEN -> INITIALIZED safe update applies. |
| Conflict Table present | Any unresolved source/decomposition disagreement is recorded with Conflict ID, sources, impacted sections, proposal, and human ruling TBD. |
| Run record written | `_run_records/TASK_RUN_*.md` exists for this invocation, finalized to SUCCESS/FAILED/FAILED_INPUTS. |

## Records

The following records result from this Procedure:

- `Datasheet.md` — package identification, attributes, conditions, construction, interfaces.
- `Specification.md` — normative requirements, standards, verification mapping, documentation list.
- `Guidance.md` — purpose, principles, considerations, trade-offs, examples, Conflict Table.
- `Procedure.md` — this document.
- `_STATUS.md` — state transition record (OPEN -> INITIALIZED) when applicable.
- `_run_records/TASK_RUN_<timestamp>.md` — durable execution record for this Procedure run.
- Conflict Table entries in `Guidance.md` for items requiring human ruling.
