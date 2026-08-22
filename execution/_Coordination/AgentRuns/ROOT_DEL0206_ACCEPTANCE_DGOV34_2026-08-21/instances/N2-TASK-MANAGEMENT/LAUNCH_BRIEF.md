# Launch brief — N2 TASK_MANAGEMENT promotions and dependent TM-ROOT-124 closure

RequestedBy: `HELP_HUMAN`

RunID: `ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21`

InstanceID: `N2-TASK-MANAGEMENT`

Role: `TASK_MANAGEMENT`

AcceptedBasis: `33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0`

Objective V1: Run mandatory invocation-local federation, transcribe D2 and D3 verbatim in a Root ruling file, and promote only TM-ROOT-035 and TM-ROOT-042 from DEFERRED to OPEN exactly as ruled: clear the spent Trigger, append firing evidence, and create no disposition. Leave TM-ROOT-126/127 OPEN and unassigned and every other row unchanged.

DependentObjective V2: After HELP_HUMAN confirms the N3 commit, record TM-ROOT-124's D-GOV-34 authority pointer and close/archive it `RESOLVED_WITH_CHANGE` citing D-GOV-34 and the landed instruction bytes; rerun federation and validation. Do not begin V2 before the explicit follow-up.

RequiredReads: root `AGENTS.md`, `agents/AGENT_TASK_MANAGEMENT.md`, D-GOV-32/K-TM-1..6 instruments, the owner transcript, live Root register/archive, and federation helper contract.

AllowedWriteTargets:

- `execution/_Coordination/_TaskManagement/**`;
- this instance directory.

AcceptanceContract V1:

- mandatory federation COMPLETE before mode work;
- ruling file contains D2/D3 verbatim;
- TM-ROOT-035/042 become OPEN, Trigger empty, firing evidence appended, Disposition empty;
- TM-ROOT-126/127 and all other rows byte-semantically unchanged;
- register validators PASS; return exact deltas/hashes/counts and federation results.

Exclusions: any foreign register write, triage of TM-ROOT-126/127 or nine other OPEN rows, unruled disposition, implementation, instruction/decision edit, receipt, Git commit/push/PR/merge.
