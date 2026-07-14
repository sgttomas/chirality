# D-GOV-16 Stage-2 Execution Run — Orchestration Plan

Status: `I1 INTEGRATED — CONVERSION CLOSURE RELEASED`
RunID: `SOW-STAGE2-EXEC-20260712-01`
Parent: `HELP_HUMAN`
Selection authority: `HUMAN`
Posture: `MIXED`
Graph version: `v53`

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
before/after hashes retained. Ready PR #229 passed its required governance
harness on exact head `f2b1d22bd4c84298ba5b9eb4f133a82904086f79` and merged as
`4c945be4c049b3ea04205f5de047d2c14d055754`. Postmerge project, format,
hash, control, evidence-binding, practitioner, and root tests pass. PKG-04 is
integrated and the P1 postmerge handoff is ready for HELP_HUMAN fan-in.

HELP_HUMAN reproduced the 22-member ordinary P1 post-state and accepted the
phase boundary at `snapshots/W_P1/ACCEPTANCE.md`: every ordinary member is
single-format `SOW_V1`, status and `IN_PROGRESS` lifecycle are preserved,
PKG-00 remains excluded upstream-only context, and `DEL-01-01` remains exact
legacy-only `ISSUED`. I0 is released for isolated derivative preparation and
independent verification only. H1 remains unapproved and integration remains
prohibited.

Direct `RECON-I0-PKG01` completed full 1-of-1 reproduction and HELP_HUMAN
accepted the normalized, rebound 29-row snapshot at SHA-256
`802656d604adcaed53bdfd6789a79d852da77dc252382387954f369fe603bc74`.
The explicit H1 evidence acceptance, decision slate, and handoff are frozen at
`snapshots/I0/H1_EVIDENCE/`. The inherent workplan goal is substantively
complete; CHANGE is released only to bind this derivative evidence and receipt
to synchronized main. H1 remains unapproved and I1 remains parked.

The human explicitly approved H1 for the exact `DEL-01-01` representation
replacement bound at evidence commit
`054ef5dd2de62f0803569573e162d613258b1b40`, agreed with the governed pause for
the ISSUED deliverable, and directed the goal to resume. The exact ruling is
recorded at `amendments/H1-APPROVAL-001.md`. CHANGE is released first to bind
that ruling on synchronized main; I1 remains parked until that binding passes.
The ruling does not authorize reissue, reauthentication, lifecycle change,
release, reliance, retirement, or H2.

`CHANGE-H1-G` bound the exact human ruling on synchronized main at
`b776813d57124df94e9ba1b66a8a63e89487b388`; the evidence-only publication
contained zero project paths and passed all manifest, hash, validator, test,
and diff-hygiene checks. I1 is now released to fresh CHANGE for only the exact
five-row `DEL-01-01` representation replacement, required PR checks, merge,
and postmerge verification. All non-H1 fences remain in force.

`CHANGE-I1` integrated that exact replacement through ready PR #230 after the
required governance harness passed on source head `41c65bd1f862701314b9c98df216cd8dbdcfe0a5`.
The clean merge commit is `6d56a1b6f391d21618f3328179d5a48654aec422`.
Fresh postmerge reproduction confirms the exact five paths, clean `SOW_V1`,
byte-identical status, unchanged `ISSUED` lifecycle, inverse rollback, and all
required checks. Cross-wave conversion/rollback closure is released. Legacy
retirement remains prohibited pending the separate fresh H2 human ruling.

`WORKING-I0-PKG01` returned PASS after a fresh author and fresh independent
verifier. The exact ISSUED source/status/authority basis is preserved; the
clean candidate binds 27 mappings and 272/272 physical source lines; exact
replacement/inverse manifests, simulation, negative behavior, containment,
and required tests pass. I0 RECONCILIATION is released for direct single-
manager full reproduction. H1 remains unapproved and integration prohibited.

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
