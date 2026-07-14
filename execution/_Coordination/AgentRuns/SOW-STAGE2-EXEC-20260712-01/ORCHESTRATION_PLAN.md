# D-GOV-16 Stage-2 Execution Run — Orchestration Plan

Status: `ACTIVE — PKG-04 LOCAL INTEGRATION GATES PASS; PR PENDING`
RunID: `SOW-STAGE2-EXEC-20260712-01`
Parent: `HELP_HUMAN`
Selection authority: `HUMAN`
Posture: `MIXED`
Graph version: `v46`

## Objective and accepted basis

Execute the owner-accepted D-GOV-16 Stage-2 plan through preparation and
independent acceptance of the H1 evidence package, then stop before ISSUED
integration. The accepted plan snapshot is
`27f03730c956447b9a9696422cc9c63b8f061939`, bound at
`b22a24fda994a8387a9bf2e04a2826dc311a36dd`. D-GOV-16 items 1–10 were
approved exactly as proposed and published at
`7584718aa32b112e415331736d1a8e68c12ac176`.

The human amended this execution plan on 2026-07-13 through
`amendments/HUMAN-STEER-PKG00-EXCLUSION-001.md`: the eight Piping PKG-00
members remain tracked governance/architecture-basis context but are outside
the Stage-2 conversion population. The conversion population is therefore
146 members: ten pilots, 135 ordinary members, and isolated ISSUED
`DEL-01-01`. P1 begins at PKG-01 and contains 22 ordinary members. PKG-01
through PKG-17 must consume applicable PKG-00 context, while PKG-00 must have
no dependency on another package or deliverable.

The execution basis at entry is synchronized `main`, local `origin/main`, and
remote `refs/heads/main` at
`c5f5bbd6e636916a76c34a04295f6ddd2a3d0983`. The tracked tree is clean and
the only porcelain entry is the pre-existing untracked `.claude-worktrees/`
container, which is outside all run write scopes and tracked-census inputs.

## Current release

Canon/consumer activation, manifest freeze, ten pilots, and ordinary waves
A1 through A3 are accepted predecessors. The original `W-P1-B0` returned
`DECISION_REQUIRED` because its superseded 30-member contract expected eight
PKG-00 dependency registers that do not exist. That terminal evidence remains
immutable.

`W-P1-B0-R1` is accepted at
`snapshots/W_P1/preflight-r1/ACCEPTANCE.md`: 22/22 members, 198/198 live
bindings, exact ISSUED exclusion, and the human's one-way PKG-00 dependency
rule all pass without project-truth edits. The package-batch method is accepted
through `amendments/PACKAGE-BATCH-ADOPTION-001.md`; PKG-01 and PKG-02 were
integrated through PR #227 and bound on main at
`5f124ad80fe84357f6dc33072dc4fbdbeb05d545`. The fresh-session basis and stale
graph delta are recorded in `amendments/SESSION-CONTINUATION-PKG03-001.md`.
`WORKING-P1-PKG03` returned manager-validated `PASS` in two consecutive
batches: 8/8 members, 234 mappings, 1,966 source lines, exact 40-row
replacement/inverse manifests, and 8/8 simulations. `RECON-P1-PKG03` completed
a passing Agent-1 full-package reproduction. Human clarification
`amendments/MANAGER-CHILD-TOPOLOGY-CLARIFICATION-001.md` confirms that RECON
itself is the independent third layer and the orchestrator-added single-child
fourth layer is not required. RECON minted the accepted rebound snapshot.
CHANGE integrated the exact replacement through PR #228 after its required
check passed on head `413c7765c7df85a8a9ad6ef4e424f896f801e065`;
the merge commit is `2826a12ba3f53720312737bd6e1480dc62d57a37`.
Postmerge project, hash, control, format, and registered checks pass. PKG-04 is
therefore dependency-released.

`WORKING-P1-PKG04` and direct `RECON-P1-PKG04` both returned `PASS`; HELP_HUMAN
reproduced and accepted the 84-row reconciliation snapshot at SHA-256
`c30cacfbf26ceb9daa691cedf7688aba5e390d979c76c16142d67961084b94c4`.
`CHANGE-P1-PKG04` created six ordered atomic five-path replacement commits on
`codex/sow-p1-pkg04`. Exact replacement/inverse manifests, six rollback
simulations, 178 mappings, 1,368 source lines, 264 practitioner tests, 20 root
export/Scope-of-Work tests, root validators, and whole-diff hygiene pass. Two
terminal-LF findings were mechanically normalized before evidence freeze with
before/after hashes retained. The branch is ready for a PR; merge still
requires every required remote check to pass on the exact final head.

All later nodes remain parked behind the accepted graph edges. H1 and H2
remain fresh human gates. CHANGE is the sole integration owner for every Git
mutation. Root `execution/` remains control-plane-only and may not acquire
`PKG-*` or `DEL-*` structure.

## Coordination and fan-in

Direct children are Agent 1 managers only. Each child receives a sealed brief
with basis, read scope, write targets, tools, return contract, dependencies,
fan-in gate, and escalation conditions. Manager returns are accepted only
after HELP_HUMAN verifies scope, provenance, schema, blockers, and required
reruns. Contract-changing amendments are versioned; consequential amendments
return to the human.

The accepted plan package at
`execution/_Coordination/AgentRuns/SOW-STAGE2-PLAN-20260712/` remains the full
graph contract. This execution record is derivative coordination evidence and
does not replace D-GOV-16, decomposition truth, deliverable truth, or accepted
snapshots.
