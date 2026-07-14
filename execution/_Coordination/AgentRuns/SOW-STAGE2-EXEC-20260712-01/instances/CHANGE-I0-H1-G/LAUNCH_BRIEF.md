# CHANGE-I0-H1-G Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `CHANGE` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@c5abf91b717c0b3901d2a27c578e63976853f8de`

## Objective

Bind the completed W-P1 acceptance, I0 derivative preparation, independent
RECON snapshot, HELP_HUMAN H1 evidence acceptance/decision slate, graph/plan,
and Receipt 18 in one evidence-only closeout commit, then fast-forward push it
to remote `main`. Do not create or integrate the prepared project replacement.

## Required reads and validation

Read root `AGENTS.md`, `agents/AGENT_CHANGE.md`, the standing workplan, graph
v50, W-P1 acceptance/handoff, WORKING-I0 and RECON-I0 terminal packages, the
29-row RECON snapshot manifest at
`a8c36925daaba4595d8f9a8017bedb840293c54f0ab078e85c9154b5b149eefe`,
the three-row H1 evidence manifest at
`b28fc08be9a40cdb9d913ad31bbd75323308f5c890a23add6cbe48ab2676b081`,
and Receipt 18.

Before commit, require local HEAD and `origin/main` both equal the basis,
rehash every upstream/self-excluding manifest, parse all JSON, run whole-diff
hygiene and applicable root governance checks, and prove changed-path
containment. Confirm the exact live `DEL-01-01` path is unchanged, remains
legacy-only, `ScopeOfWork.md`-absent, exact source/status hashes, and `ISSUED`.
Confirm no project path appears in the commit delta.

## Write scope and fences

Write scope is the exact currently modified/untracked root control-plane and
derivative-evidence paths under:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/{ORCHESTRATION_PLAN.md,WORK_GRAPH.json}`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/I0/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/{WORKING-I0-PKG01,RECON-I0-PKG01,CHANGE-I0-H1-G}/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/{I0,W_P1/ACCEPTANCE.md,W_P1/HANDOFF_STATE.md}`;
- `execution/_Coordination/LOOP_RECEIPTS.md`;
- the exact Git commit and fast-forward push required to bind those paths.

Do not write any project path, candidate content, prior evidence, canon/tool/
instruction path, lifecycle, H1/H2 ruling, issuance/reissue, authentication,
integration, release, reliance, or retirement state. Do not include unrelated
primary-checkout equation-audit or worktree state. The source branch/worktree
is `/Users/ryan/ai-env/projects/chirality-sow-p1-pkg04-closeout`; it is isolated
and clean at the basis except the declared closeout scope.

Fix safe mechanical defects inside the declared closeout evidence, retain
before/after hashes and attempts, rebuild affected bindings, and continue. Any
project delta, source/status/lifecycle drift, semantic evidence conflict,
manifest mismatch not safely repairable in owned evidence, non-fast-forward,
or failed required check blocks publication.

## Return

Return `PASS`, `BLOCKED`, or `DECISION_REQUIRED` with exact commit/push state,
changed-path inventory, manifest/check results, live-project non-change proof,
and terminal handoff. PASS must leave remote `main` synchronized to the new
evidence-binding commit and explicitly record
`H1_EVIDENCE_PREPARED — AWAITING_ISSUED_ADMINISTRATIVE_APPROVAL`; H1 remains
unapproved and I1 prohibited.
