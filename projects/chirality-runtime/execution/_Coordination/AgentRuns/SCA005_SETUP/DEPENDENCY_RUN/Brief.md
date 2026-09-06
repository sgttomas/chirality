# TASK dependency extraction: runtime successor package

PURPOSE: Recompute deliverable-local dependency registers from approved successor scope and exact inherited ordering, without adding gating semantics.
RequestedBy: PROJECT_SETUP
TaskSkill: dependency-extract
TaskProfile: NONE
ScopePath: projects/chirality-runtime/execution/_Coordination/AgentRuns/SCA005_SETUP/DEPENDENCY_RUN
ApplyEdits: true
AllowedWriteTargets:
- projects/chirality-runtime/execution/_Coordination/AgentRuns/SCA005_SETUP/DEPENDENCY_RUN/
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/Dependencies.csv
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_DEPENDENCIES.md
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/Dependencies.csv
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/_DEPENDENCIES.md
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/Dependencies.csv
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_DEPENDENCIES.md
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/Dependencies.csv
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/_DEPENDENCIES.md
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/Dependencies.csv
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/_DEPENDENCIES.md
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/Dependencies.csv
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/_DEPENDENCIES.md
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/Dependencies.csv
- projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/_DEPENDENCIES.md

RuntimeOverrides:
- CHIRALITY_INSTRUCTION_ROOT: /Users/ryan/.codex/worktrees/341e/chirality
- RUN_ROOT: projects/chirality-runtime/execution
- SCOPE: PKG-02_Runtime_Product (exact seven registered successors)
- DECOMPOSITION_PATH: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md
- MODE: UPDATE
- STRICTNESS: CONSERVATIVE
- CONSUMER_CONTEXT: NONE
- SOURCE_DOCS: ScopeOfWork.md and explicit _CONTEXT.md/_DEPENDENCIES.md/_REFERENCES.md; exact Gate4 DEPENDENCY_DISTRIBUTION.csv and RUNTIME_METADATA_BINDINGS.csv; accepted runtime hold and authority wrappers

Read actual TASK role, skill and all companions. ScopePath is evidence anchor; RUN_ROOT and SCOPE identify the actual package. Mandatory TASK local record stays within the named evidence anchor. Exact granted effects are seven Dependencies.csv and the same seven _DEPENDENCIES.md files; no other deliverable or authority writes. All status/memory reads are paired where present.

Preserve six runtime evidence fan-in prerequisites from DEL07..12 into DEL06. Record declared upstream/downstream mirrors without double-counting six unique edges. Anchor rows are distinct from execution gates. Two Root governance edges GOV0405/GOV0502→GOV0411 remain in Root owner view, not runtime product graph; cite their distribution without inventing runtime targets. Receipt-validator-to-runtime and App/client relationships remain non-gating coordination. Do not infer inter-carrier ordering, mature satisfaction, activation or hold release. Nine holds stay; R16-B separate. Historical source no-edge wording is overridden only by explicitly approved destination distribution.

Use v3.1 canonical enums. Evidence gate does not become satisfied because status is INITIALIZED or a contract file exists. New source facts may produce nongating references conservatively; every gating addition beyond the accepted six is a conflict to report, not implement. Preserve all scoped source/production files unchanged. Current frozen contracts are under independent review; if parent later changes one, identify rerun requirement.

Run actual skill QA and applicable register validation. Return normalized unique gating edge set, original file hashes/new hashes, source pins, row counts/anchor-vs-execution distinction, all unknown maturity/satisfaction, and unresolved findings. No Git mutations, pointer, status, production, acceptance, schedule, network or delegation. Scratch /private/tmp/root-runtime-migration-20260905/gate5-dependencies. GPT6 exact serving ID unavailable; role instruction-asserted.
