HandoffID,OwnerWorkflow,TriggerCondition,PayloadPath,ExpectedOutput,Status
HOFF-SCC-001-001,WORKING_ITEMS,"Need deliverable-local evidence review across runtime, SDK, session, audit, permission, tooling, hook, and MCP concerns.",Task_Findings.csv,"Additional findings and evidence rows.",OPEN
HOFF-SCC-001-002,SCOPE_CHANGE,"Human rules that a decomposition or scope amendment is needed for one bounded concern.",Candidate_Remedies.csv,"Possible SCA snapshot if SCOPE_CHANGE accepts an amendment.",DEFERRED
HOFF-SCC-001-003,DEPENDENCY_WORKFLOW,"Accepted owner workflow changes require dependency register regeneration or extraction.",Candidate_Remedies.csv,"Regenerated dependency registers or derivative evidence as authorized by the owning workflow.",DEFERRED
HOFF-SCC-001-004,RECONCILIATION,"Dependency workflow outputs are current and need coherence review before closure scan.",Evidence_Register.csv,"Updated reconciliation evidence for follow-up DepClosure.",DEFERRED
HOFF-SCC-001-005,DEPCLOSURE,"Reconciliation evidence is current after owner workflow work.",Case_QA.md,"Accepted closure snapshot that determines whether SCC-001 remains.",DEFERRED
