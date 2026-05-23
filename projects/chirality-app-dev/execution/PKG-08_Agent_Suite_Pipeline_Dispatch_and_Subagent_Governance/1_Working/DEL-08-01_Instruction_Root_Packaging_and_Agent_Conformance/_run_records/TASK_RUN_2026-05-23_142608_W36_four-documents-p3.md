# TASK RUN: W36 four-documents P3

**Run:** TASK + four-documents  
**RUN_PASSES:** P3_ONLY  
**DECOMP_VARIANT:** SOFTWARE  
**Deliverable:** DEL-08-01 Instruction Root Packaging and Agent Conformance  
**StatusPolicy:** NO_STATUS_TOUCH; `_STATUS.md` was read and not modified.  
**Result:** PASS

## Inputs Read

- `_CONTEXT.md`
- `_STATUS.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `_SEMANTIC_LENSING.md`
- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- Source slices: `docs/DIRECTIVE.md` section 2.7; `docs/CONTRACT.md` K-ROOT, K-INVENT, K-CONFLICT, K-WRITE, K-SEAL, K-GHOST, K-SUBAGENT; `docs/SPEC.md` sections 1.1 and 7; `docs/TYPES.md` Agent classification and Type 2 vocabulary; `docs/PRD.md` sections 8.10 and 15 with REF-006 hash warning.

## Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| C-001 | Surfaced as conflict and already covered; strengthened references. | `Guidance.md` keeps CT-001 and now points impacted Specification requirements to `DEL0801-REQ004`, `DEL0801-REQ005`, `DEL0801-REQ012`, and `DEL0801-REQ013` without stale shorthand IDs. Source reread: `_REFERENCES.md` REF-006 and `docs/CONTRACT.md` K-CONFLICT-1. |
| F-001 | Converted to explicit TBD implementation-decision slot. | `Specification.md` Documentation now requires the later coding task to record validator implementation path, fixture path, test framework, local command, CI location, and output artifact directory. `Procedure.md` Step 5 mirrors the same required decision fields. Source reread: Procedure Step 5, Specification Documentation, `_DEPENDENCIES.md` unresolved implementation notes. |
| F-002 | Incorporated as pass/fail evidence capture requirement. | `Procedure.md` Step 6 now requires command, worktree or commit identifier when available, fixture summary, warning/failure counts, and output artifact location once the validator command exists. Source reread: Procedure Verification and Records. |
| D-001 | Converted to TBD ownership question with bounded records. | `Procedure.md` Prerequisites, Step 5, and Records now keep framework, command, fixture path, CI command, and artifact directory as explicit TBD fields to be resolved by the coding task before verification is executable. Source reread: Procedure Prerequisites, Step 5, and Records. |
| X-001 | Incorporated using dependency-register status without inventing edges. | `Datasheet.md` Conditions and `Procedure.md` Prerequisites now state that declared upstream/downstream lists remain TBD, while `_DEPENDENCIES.md` contains extracted upstream source prerequisites and no populated downstream handoff edges under `CONSUMER_CONTEXT=NONE`. Source reread: `_DEPENDENCIES.md` Dependency Tracking, Extracted Dependency Register, and Downstream Handoff Notes. |
| E-001 | Incorporated as human ruling path. | `Guidance.md` now adds Human Ruling Path: PRD-only checks stay warnings until REF-006 is reconciled or the source basis is amended, with SPEC/CONTRACT/TYPES retained as governing authority. Source reread: `_REFERENCES.md` REF-006 and `docs/CONTRACT.md` K-CONFLICT-1. |

## Cross-Document Sweep

- Terminology remains aligned around instruction root, working root, agent instruction conformance, Type 2 candidates, and source-warning handling.
- Requirement labels were normalized from local shorthand to `DEL0801-REQ###` so semantic-lensing validators do not confuse requirement labels with warranted item IDs.
- Unsupported implementation choices remain `TBD`; no validator path, fixture path, framework, command, CI location, or artifact directory was invented.
- `_STATUS.md` was not changed because this was P3_ONLY and the deliverable carries NO_STATUS_TOUCH.

## Validation

- `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_p3_disposition.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-01_Instruction_Root_Packaging_and_Agent_Conformance`
- `python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_semantic_pipeline_scope.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-01_Instruction_Root_Packaging_and_Agent_Conformance --step p3`
