# TASK Run: four-documents Pass 3

| Field | Value |
|---|---|
| TaskSkill | four-documents |
| RUN_PASSES | P3_ONLY |
| DECOMP_VARIANT | SOFTWARE |
| Deliverable | DEL-06-05 Bash Governance and Timeout Policy |
| Scope | `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy` |
| DecompositionRef | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| StatusPolicy | NO_STATUS_TOUCH preserved; `_STATUS.md` not modified |
| RunStatus | PASS |

## Inputs Read

- `skills/four-documents/SKILL.md`
- `skills/four-documents/QA_CHECKS.md`
- `skills/four-documents/TOOL_POLICY.md`
- `tools/validation/validate_p3_disposition.py`
- `tools/validation/validate_semantic_pipeline_scope.py`
- `_STATUS.md`
- `_CONTEXT.md`
- `_REFERENCES.md`
- `_SEMANTIC_LENSING.md`
- `_DEPENDENCIES.md`
- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `docs/CONTRACT.md` Section 1.5 and Section 1.6
- `docs/SPEC.md` Sections 9, 10, 14, and 15
- `docs/TYPES.md` Sections 8 and 9
- `docs/PLAN.md` R4
- `docs/PRD.md` R4 and session artifact policy, with REF-006 HASH_MISMATCH warning from `_REFERENCES.md`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-062 / DEL-06-05 context

## Files Changed

- `Specification.md`
- `Procedure.md`
- `_run_records/TASK_RUN_2026-05-23_W28_four-documents-p3.md`

`Datasheet.md`, `Guidance.md`, `_STATUS.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` were not modified.

## Pass 3 Disposition

| ItemID | Disposition | Evidence and source reread |
|---|---|---|
| C-001 | Incorporated as unresolved contract slot. | Re-read `Procedure.md#Steps`, `Specification.md#Requirements`, `docs/PRD.md#R4`, and `docs/CONTRACT.md#1.6`. Added `DEL-06-05-REQ-016` and revised Procedure Step 3 to keep command metadata fields and network posture checks unresolved unless accepted or assigned out of scope. |
| F-001 | Already covered as blocker. | Re-read `Datasheet.md#Conditions`, `Specification.md#Requirements`, `Guidance.md#Conflict Table`, `Procedure.md#Prerequisites`, `docs/CONTRACT.md#K-BASH-1`, and `docs/PLAN.md#R4`. Existing documents preserve numeric timeout default and maximum as `TBD`; no source supplied a number. |
| F-002 | Incorporated as evidence requirement. | Re-read `Specification.md#Scope`, `Specification.md#Documentation`, `Procedure.md#Records`, `docs/CONTRACT.md#K-HOOK-1`, `docs/CONTRACT.md#K-PATH-2`, `docs/CONTRACT.md#K-PATH-3`, and `docs/SPEC.md#15.2`. Added hook/path interface evidence to Specification documentation and Procedure records. |
| D-001 | Incorporated as controlled-release evidence slots. | Re-read `Procedure.md#Records`, `docs/PLAN.md#R4`, and `docs/SPEC.md#14-15`. Procedure records now name hook/path composition evidence and concrete DEL-06-05 test names/fixtures/harness paths as `TBD`. Existing records already kept policy slice, preflight enforcement point, timeout, capture, artifact fixture, and terminal outcome evidence as `TBD`. |
| D-002 | Incorporated as current-state dependency wording. | Re-read `Procedure.md#Prerequisites` and `_DEPENDENCIES.md#Extracted Dependency Register`. Procedure no longer says no accepted upstream edges exist; it now records extracted ACTIVE upstream rows while keeping declared upstream and satisfaction acceptance as `TBD`. |
| X-001 | Already covered as source-state warning. | Re-read `_REFERENCES.md#Authoritative Source Corpus`, `Guidance.md#PRD Hash Warning`, `Guidance.md#Conflict Table`, and `Specification.md#Documentation`. Existing guidance and documentation require a residual-risk note for REF-006 HASH_MISMATCH before PRD-derived details are accepted as closure evidence. |
| X-002 | Incorporated as concrete-test-path gap. | Re-read `Specification.md#Verification`, `Procedure.md#Records`, and `docs/PLAN.md#R4 Acceptance`. Specification verification now explicitly keeps concrete test names, fixtures, and harness paths as `TBD` until assigned. |
| E-001 | Incorporated as warning-qualified metadata schema. | Re-read `Specification.md#Requirements`, `Procedure.md#Steps`, `docs/TYPES.md#8.3`, `docs/TYPES.md#HarnessSubagentRun`, and `docs/PRD.md#Session artifact policy`. Specification and Procedure now cite PRD artifact-policy fields while preserving Bash channel labels and terminal-outcome linkage as `TBD`. |
| E-002 | Incorporated as interrupt fallback boundary. | Re-read `Datasheet.md#Conditions`, `Specification.md#Requirements`, `Procedure.md#Steps`, `docs/SPEC.md#10.1`, `docs/CONTRACT.md#K-EVENT-3`, and `docs/PLAN.md#R4`. Specification and Procedure now require persistence of actual failure/cancellation/residual-risk outcome when interruption is unsupported. |

## Mini Consistency Sweep

| Check | Result |
|---|---|
| Datasheet to Specification | PASS - timeout and interrupt remain aligned as required/TBD where source evidence is incomplete. |
| Specification to Guidance | PASS - PRD HASH_MISMATCH warning remains visible in Guidance and is not relaxed by P3 edits. |
| Specification to Procedure | PASS - new preflight, metadata, interrupt, hook/path, and concrete-test gaps are reflected in Procedure steps/records. |
| Terminology | PASS - retained Bash, Chirality events, ToolResultStore, `readOnly`, `dontAsk`, and HASH_MISMATCH terminology. |
| Values | PASS - no numeric timeout or output threshold invented. |

## Validation

Planned commands:

```sh
python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_p3_disposition.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy
python3 /Users/ryan/ai-env/projects/chirality/tools/validation/validate_semantic_pipeline_scope.py /Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy --step p3
```

## Blockers

- Numeric Bash timeout default and maximum remain `TBD`; no accepted source slice supplies values.
- REF-006 `docs/PRD.md` remains HASH_MISMATCH in `_REFERENCES.md`, so PRD-derived Bash, artifact, and interrupt details remain warning-qualified.
- Concrete implementation paths, fixture paths, and accepted hook/path interface evidence remain `TBD`.
