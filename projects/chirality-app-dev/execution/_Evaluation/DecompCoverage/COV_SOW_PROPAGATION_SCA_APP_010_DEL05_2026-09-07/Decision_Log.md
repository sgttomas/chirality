# Decision log

| ID | Decision | Basis |
| --- | --- | --- |
| APP-POST-001 | Audit only the exact DEL-02-05 carrier propagation poststate. | Sealed brief; manager direction to avoid broad unchanged-corpus checks. |
| APP-POST-002 | Treat the active SCA-APP-010 semantic snapshot as accepted upstream truth and the new addendum as an immutable application record. | App `_ScopeChange/_LATEST.md`, addendum `APPLICATION_JOURNAL.md`, and `Handoff_State.md`. |
| APP-POST-003 | Classify Runtime modifications as authorized excluded sibling state. | Sealed brief and lane status; Runtime paths are outside the App path set. |
| APP-POST-004 | Preserve existing open derivative/closure blockers without converting them into findings against this exact SOW propagation. | Active SCA-APP-010 handoff and addendum handoff both keep `ReadyForNextPhase = NO` and enumerate the carried work. |
| APP-POST-005 | Do not update `_Evaluation/DecompCoverage/_LATEST.md`. | The sealed brief authorizes one immutable snapshot, not an evaluation pointer mutation. |
