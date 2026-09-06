# D-APP-64 §5.3 rationale

## Judgment A
OwnerStandingApproval: D-APP-64 §3
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: Advance A1 as an App-only owner proposal after T3 serialization
JudgedBy: TASK Agent2 / pkg02_t2_proposal / APP_LOOP_SHELL_2026-09-05 iteration-04
OwnerCaseSelection: NONE
RejectedAlternatives: A2 deferred as less complete; CSS-only hiding retains markup; deleting controls loses existing behavior; concurrent T3 edits violate the shared-source fence.
RationaleArtifact: execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t2_proposal/RATIONALE.md
IndependentVerifier: PENDING — parent must dispatch fresh governed verifier; no return exists or is anticipated as COMMIT-SAFE.
EffectStatus: HELD
PreservedGates: owner case selection; Root authority and contract acceptance; product write fences; T3 serialization; independent review; lifecycle/dependency/pointer acceptance; provider/network/release boundaries.

Ontology: presentation seam is App-owned; session truth is not.
Epistemology: direct toolbar and ShellFrame reads identify the actual owners.
Praxeology: serialize after T3, preserve hooks/props, review a frozen diff.
Axiology: meet header-less intent while keeping reconnect/settings accessible.

Evidence and exact recommendation: D-APP-120 §PROPOSAL A; source hashes and frozen bytes in SOURCE_IDENTITIES.json. Draft record writing has occurred under the sealed brief; selected implementation/routing effect has not.

## Judgment B
OwnerStandingApproval: D-APP-64 §3
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: Advance B1 restriction plus separately owner-gated Root design routing proposal
JudgedBy: TASK Agent2 / pkg02_t2_proposal / APP_LOOP_SHELL_2026-09-05 iteration-04
OwnerCaseSelection: NONE
RejectedAlternatives: B2 delays resolution; B3 is a different semantic candidate needing owner acceptance; guard removal and hidden canonicalRoot fallback contradict actual contracts.
RationaleArtifact: execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t2_proposal/RATIONALE.md
IndependentVerifier: PENDING — parent must dispatch fresh governed verifier; no return exists or is anticipated as COMMIT-SAFE.
EffectStatus: HELD
PreservedGates: owner case selection; Root authority and contract acceptance; product write fences; T3 serialization; independent review; lifecycle/dependency/pointer acceptance; provider/network/release boundaries.

Ontology: absent selected folder differs from absent registered project authority.
Epistemology: required fields and fixed project binding prove current restriction, not future semantics.
Praxeology: Root accepts its own contract before App implementation; no routing message is sent here.
Axiology: truthful capability and explicit filesystem identity outweigh apparent UI completion.

Evidence and exact recommendation: D-APP-120 §PROPOSAL B; source hashes and frozen bytes in SOURCE_IDENTITIES.json. Draft record writing has occurred under the sealed brief; selected implementation/routing effect has not.

## Revision 2 factual repair

Same A/B selection and all ten fields remain unchanged; EffectStatus HELD, owner selection NONE, verifier PENDING. A candidate uses verified getRuntimeStatusBridge → window.chirality?.runtime?.daemon → bridge.status(), and one renderWorkspaceContent callback returning the complete woven layout in place of children. Original rationale retained in revision-01/. Source refresh is observation only, not T3 acceptance.
