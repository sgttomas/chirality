# Launch brief — N3 TASK_MANAGEMENT federation and housekeeping

RequestedBy: `HELP_HUMAN`
RunID: `ROOT_DEL0206_CHANGE_HOUSEKEEPING_2026-08-21`
ParentInstanceID: `HELP-HUMAN-ROOT`
ChildInstanceID: `N3-TASK-MANAGEMENT-HOUSEKEEPING`
Objective: after N1/N2 land, run mandatory Root federation and perform only the
owner-directed Root register housekeeping: close TM-ROOT-116 and TM-ROOT-124;
add the two named attention rows for owner triage; assess whether N1's REM-001
disposition fires TM-ROOT-035 or TM-ROOT-042 and prepare, but do not rule, any
promotion.
AcceptedBasis: repository base `1b375af4f1219ecfc00fc2755854aa7fd4220901`,
plus the landed N1 and N2 commits supplied by HELP_HUMAN before activation.
Dependencies: N1 and N2 landed in order.
EXCLUSIONS: implementation; edits to the three concordance docs; edits to the
G4 validator/tests; other OPEN/DEFERRED rows unless exact N1 trigger fired;
foreign register writes; acceptance; lifecycle/release/publication/reliance;
Git commit/push/PR/merge.
DeclaredReads: root `AGENTS.md`; `agents/AGENT_TASK_MANAGEMENT.md`; all four
canonical Task Management register pairs; the exact target rows; N1/N2 returns
and landed bytes; cited workplan/docs/validator sources.
AllowedTools: read, deterministic Task Management helpers and validators,
apply_patch inside allowed writes. No implementation dispatch.
AllowedWriteTargets: Root Task Management register home, Root receipt/handoff,
and this instance directory only.
ExpectedOutputs: COMPLETE/PARTIAL federation report with zero foreign register
writes; exact archived closures for TM-ROOT-116 and TM-ROOT-124; two new live
attention rows; trigger assessment and owner-only promotion slate if fired;
validated counts/hashes/staleness/closure echo; manager return.
AcceptanceCriteria: K-TM-1..6; each closure cites owner direction and exact
evidence bytes/SHA; new rows create attention only; no forbidden implementation.
Escalation: any incomplete federation, ambiguous next ID, invalid register,
or trigger uncertainty stops dependent global claims and returns the blocker.
