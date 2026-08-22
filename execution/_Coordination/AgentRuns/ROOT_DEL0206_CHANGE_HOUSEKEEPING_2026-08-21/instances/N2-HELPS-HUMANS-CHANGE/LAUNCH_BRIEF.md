# Launch brief — N2 HELPS_HUMANS TM-ROOT-124 instruction tranche

RequestedBy: `HELP_HUMAN`
RunID: `ROOT_DEL0206_CHANGE_HOUSEKEEPING_2026-08-21`
ParentInstanceID: `HELP-HUMAN-ROOT`
ChildInstanceID: `N2-HELPS-HUMANS-CHANGE`
Objective: implement the owner-directed TM-ROOT-124 disposition on the Root
CHANGE instruction surface: clean-basis branch/worktree-lane creation is
routine; dirty-basis lanes remain non-routine; ship the required G4 manifest
and App/Piping/domain-engine coordination notices.
AcceptedBasis: repository/branch base
`1b375af4f1219ecfc00fc2755854aa7fd4220901`; exact live TM-ROOT-124 row;
owner direction transcribed in the parent run.
Dependencies: none.
EXCLUSIONS: Root Task Management register writes/closure; changes to any other
agent instruction; historical pin rewrites; App/Piping/domain-engine content
or register changes; merge; silent sync.
DeclaredReads: root `AGENTS.md`; `agents/AGENT_HELPS_HUMANS.md`;
`agents/AGENT_CHANGE.md`; exact TM-ROOT-124 row and cited sources; applicable
D-GOV authority row/record, G4 schema and validator/tests, precedent manifests,
and the pin/mirror surfaces required by the agent-index change-notice rule.
AllowedTools: read, search, deterministic local validators/tests, apply_patch.
AllowedWriteTargets: `agents/AGENT_CHANGE.md`; one new Root G4 manifest; the
three exact coordination-notice paths frozen in the parent work graph; this
instance directory only.
ExpectedOutputs: smallest coherent instruction change; G4 manifest whose
`basis:` is the full real branch-base SHA and resolves as a commit via
`git cat-file -t`; routed notices stating change and loop-owned follow-on;
pin/mirror inventory; validation and fresh review result; manager return.
AcceptanceCriteria: exact clean/dirty distinction; applicable D-GOV authority
identified without invention; manifest and instruction validators pass;
notices satisfy the agent-index change-notice rule; no register write.
Escalation: if the row's D-GOV assignment cannot be resolved unambiguously,
return the named blocker and do not invent a decision identity.
