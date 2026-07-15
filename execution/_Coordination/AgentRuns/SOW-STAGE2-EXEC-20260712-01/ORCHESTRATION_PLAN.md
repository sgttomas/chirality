# D-GOV-16 Stage-2 Execution Run — Orchestration Plan

Status: `P4 INTEGRATED — CORPUS CLOSURE FAN-IN RELEASED`
RunID: `SOW-STAGE2-EXEC-20260712-01`
Parent: `HELP_HUMAN`
Selection authority: `HUMAN`
Posture: `MIXED`
Graph version: `v77`

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
required checks. Fresh live-census reproduction then corrected the derivative
closure-release label: only 80/146 conversion members are `SOW_V1`; 66 exact
ordinary Piping members remain legacy-only across accepted P2–P4, with zero
dual/invalid. P2 preflight for PKG-05–09 is released. Conversion closure and
legacy retirement remain parked.

All five W-P2 package managers and their fresh author/verifier executions
returned PASS for 29 members. Direct fresh `RECON-P2` then reproduced the
entire wave because every package retained at least one closed mechanical
exception: 919 mappings, 8,203 source lines, 87 candidates, exact 145-row
replacement/inverse manifests, 29 simulations, 58 negatives, 261 live
bindings, 29 dependency schemas, focused and 264 practitioner tests, and all
27 accepted predecessors pass with zero project writes or unresolved finding.
HELP_HUMAN reproduced and accepted the immutable 334-row snapshot at SHA-256
`a42918b012864c245082837dc8abf5d0d403b3453edb56bd2484b9b139e5fe9b`.
One parent-brief terminal-LF defect was normalized and its six-row instance
manifest rebound to
`1c9a9b2d3547ccc09403dd0d615af1d86f23c2af3a1c383cbca7b87f20cd9055`.
Fresh `CHANGE-P2` is released for only the exact 29-member atomic integration,
required checks, merge under active blanket approval, and postmerge handoff.

`CHANGE-P2` integrated the 29 ordered atomic five-path replacement commits
through ready PR #231 after `governance-harness / harness` passed on exact
source head `3ea904a6e6228a93f8b0dd9c5ff84c235fa194b3`; the merge commit is
`7b5f27c17f425c1e1f8e47f4e81200b070227f69`. Fresh postmerge reproduction
passes the exact 145-row project delta, all target/control hashes and formats,
inverse rollback simulation, 264 practitioner tests, 20 root export/Scope-of-
Work tests, dependency schemas, root validators, and whole-diff hygiene. W-P2
integration is closed and P3 is dependency-released.

All three W-P3 package managers returned PASS for the 15 PKG-10–12 members.
PKG-11's two stale ignored-residue bindings were repaired and transitively
rebound under its versioned brief; PKG-12's contaminated initial verifier
remains terminal BLOCKED and excluded, while its single authorized fresh
replacement passed with zero prohibited reads. Direct fresh `RECON-P3` then
reproduced the complete wave: 493 mappings, 4,919 source lines, 45 candidates,
exact 75-row replacement/inverse manifests, 15 simulations, 105 negatives,
135 live bindings, 15 dependency schemas, focused and 264 practitioner tests,
56 predecessors, and 88 valid PKG-00 upstream edges. HELP_HUMAN reproduced
and accepted the immutable 154-row snapshot at SHA-256
`9bd3fbc04be6ed07a5123cc26da0119dbb4a3c835b38b73a949c09bdf72963c7`.

`CHANGE-P3` integrated the 15 ordered atomic five-path replacement commits
through ready PR #233 after `governance-harness / harness` passed on exact
source head `2628c4ec68d65c7fa422c202d12f95d11b9e456b`; the merge commit is
`b999fbd24852aa6acee36a61c2f049c7a2e6fa36`. Fresh isolated postmerge
reproduction passes the exact 75-row project delta, all target/control hashes
and formats, inverse rollback simulation without execution, 264 practitioner
tests, 20 root export/Scope-of-Work tests, dependency schemas, root validators,
and project diff hygiene. The immutable postmerge manifest SHA-256 is
`15affcebf7c766a27879e90f39891b0d9035268475a0ae35452f2a1d2ca5918f`.
The fresh worktree also exposed three ignored compiled-residue rows in the
current PKG-10 author and PKG-12 verifier manifests. CHANGE removed only those
untracked residue bindings, transitively rebuilt the two package manifests,
and revalidated all ten package/child manifests without changing candidates,
project state, semantic evidence, or the immutable accepted snapshot. W-P3
integration is closed and W-P4 is dependency-released.

`WORKING-I0-PKG01` returned PASS after a fresh author and fresh independent
verifier. The exact ISSUED source/status/authority basis is preserved; the
clean candidate binds 27 mappings and 272/272 physical source lines; exact
replacement/inverse manifests, simulation, negative behavior, containment,
and required tests pass. I0 RECONCILIATION is released for direct single-
manager full reproduction. H1 remains unapproved and integration prohibited.

W-P4 is released behind accepted W-P3. Corpus closure remains parked behind
W-P4 and the already integrated H1 replacement; H2 remains a fresh human gate.
CHANGE is the sole integration owner for every Git mutation. Root `execution/`
remains control-plane-only and may not acquire `PKG-*` or `DEL-*` structure.

Fresh conversion-closure fan-in found a bounded implementation defect in the
already-authorized corpus: 57 live production contracts (all 53 App members
and four Piping pilots) retain evidence-candidate metadata prohibited by
`CLEAN-SOW-PRODUCTION-001`. This is not a scope or lifecycle change. Direct
`WORKING-CLEAN-REPAIR` is released without a child to apply only the registered
deterministic finalizer, preserve the externalized metadata in repair evidence,
and return the exact project delta for independent RECONCILIATION and
EVALUATION reruns. Integration remains reserved to a fresh CHANGE manager;
H2 and legacy retirement remain parked.

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

Final post-repair fan-in passes on exact
`origin/main@79de30d83b91a2ab468a3f17536a5233c2f85fe7`. Fresh direct
RECONCILIATION independently closes the 154-member census, 146 clean
conversions, eight PKG-00 exemptions, lifecycle 153+1, 57 finalizer bridges,
730 rollback rows, 146 simulations, callers, compatibility, and all root/App/
Piping checks. Fresh direct EVALUATION independently passes the same material
state and produces the exact H2 slate. HELP_HUMAN accepts the fan-in and
releases `CONVERSION_CLOSED — LEGACY_RETIREMENT_RULING_REQUIRED`. H2 remains
unapproved; compatibility and legacy retirement remain unchanged and parked.
