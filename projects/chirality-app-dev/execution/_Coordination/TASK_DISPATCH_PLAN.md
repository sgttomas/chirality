# TASK Dispatch Plan

**Generated:** 2026-05-20
**Variant:** SOFTWARE_DECOMP
**Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`

## Phase Order

1. `TASK + four-documents`, `RUN_PASSES=P1_P2`
2. Validate four-document kit presence and status transition
3. `TASK + semantic-matrix-build`
4. Validate `_SEMANTIC.md`
5. `TASK + lens-register`
6. Validate `_SEMANTIC_LENSING.md`
7. `TASK + four-documents`, `RUN_PASSES=P3_ONLY`
8. Validate P3 disposition and `SEMANTIC_READY` state
9. `TASK + dependency-extract`
10. Validate `Dependencies.csv` v3.1 and merged graph acyclicity

## Dispatch Queue

| DeliverableID | PackageID | ScopePath | CurrentState | FourDocs | Semantic | Lens | P3 | Dependencies |
|---|---|---|---|---|---|---|---|---|
| DEL-01-01 | PKG-01 | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-01_Governance_Alignment_Human_Authority_and_Project_Truth` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-01-02 | PKG-01 | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-02_Reliance_Boundary_Register` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-01-03 | PKG-01 | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-03_Product_Identity_and_Professional_Boundary_Copy` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-01-04 | PKG-01 | `execution/PKG-01_Product_Governance_and_Reliance_Boundaries/1_Working/DEL-01-04_Scope_Boundary_and_Retired_Scope_Register` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-02-01 | PKG-02 | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-01_Desktop_Shell_and_Matrix_Navigation` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-02-02 | PKG-02 | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-02-03 | PKG-02 | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-03_Working_Root_File_Tree_and_Scope_Scan_UI` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-02-04 | PKG-02 | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-02-05 | PKG-02 | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-03-01 | PKG-03 | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-03-02 | PKG-03 | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-02_Thin_TurnEngine_and_Session_Locking` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-03-03 | PKG-03 | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-03_Harness_API_and_SSE_Compatibility_Adapter` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-03-04 | PKG-03 | `execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-04_Interrupt_Cancel_and_Terminal_Outcome_Handling` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-04-01 | PKG-04 | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-04-02 | PKG-04 | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-04-03 | PKG-04 | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-03_SdkMessageMapper_and_Provider_Neutral_Translation` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-04-04 | PKG-04 | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-04_PersonaComposer_from_Instruction_Root` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-04-05 | PKG-04 | `execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-05-01 | PKG-05 | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-05-02 | PKG-05 | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-05-03 | PKG-05 | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-03_Redacted_RunLogger_and_Secret_Hygiene` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-05-04 | PKG-05 | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-05-05 | PKG-05 | `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-05_ToolResultStore_and_Session_Artifacts` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-06-01 | PKG-06 | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-01_ChiralityPermissionOverlay_and_Mode_Mapping` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-06-02 | PKG-06 | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-06-03 | PKG-06 | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-06-04 | PKG-06 | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-04_Write_Edit_Surface_and_Path_Hooks` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-06-05 | PKG-06 | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-05_Bash_Governance_and_Timeout_Policy` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-06-06 | PKG-06 | `execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-06_Hook_Lifecycle_and_Compaction_Mirror` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-07-01 | PKG-07 | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-07-02 | PKG-07 | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-02_Execution_Root_Scaffolding_from_Decomposition` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-07-03 | PKG-07 | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-07-04 | PKG-07 | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-04_Status_Transition_API_and_MCP_Tool` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-07-05 | PKG-07 | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-05_Dependencies_csv_v3_1_Reader_Writer_and_Linter` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-07-06 | PKG-07 | `execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-08-01 | PKG-08 | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-01_Instruction_Root_Packaging_and_Agent_Conformance` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-08-02 | PKG-08 | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-08-03 | PKG-08 | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-08-04 | PKG-08 | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-08-05 | PKG-08 | `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-09-01 | PKG-09 | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-01_Section_8_Harness_Validation_Preservation` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-09-02 | PKG-09 | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-02_Section_9_Runtime_Validation_Additions` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-09-03 | PKG-09 | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-03_Unit_and_Integration_Test_Expansion` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-09-04 | PKG-09 | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-09-05 | PKG-09 | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-09-06 | PKG-09 | `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-10-01 | PKG-10 | `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-10-02 | PKG-10 | `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-10-03 | PKG-10 | `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-10-04 | PKG-10 | `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
| DEL-10-05 | PKG-10 | `execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation` | INITIALIZED | P1_P2 complete | semantic pending | lens pending | P3 pending | dependency-extract pending |
