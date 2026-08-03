# HELP_HUMAN orchestration plan — Root four-lane owner steer

Run ID: `ROOT_FOUR_LANES_2026-08-02`
Plan version: `3`
Selection authority: `HUMAN`
Descriptive posture: `MIXED`
Repository basis: `origin/main@97678a841ef58345c73d3470ed8de57c9b1405d2`
Working root: repository root
Supervising role: `HELP_HUMAN`

## Alignment

The owner opened four separately authorized Root lanes on 2026-08-02:

1. open the Root SCOPE_CHANGE intake carried by `TM-ROOT-107` with the two
   exact named inputs;
2. take the `TM-ROOT-108` accepted-turn recovery defect through the
   `DEL-02-06` amendment/activation lane, with restart/replay idempotence as
   the eventual closure evidence;
3. wire the existing G4 diff-mode manifest check into CI under `TM-ROOT-110`;
4. commission the `TM-ROOT-106` Pi `0.82.0` concordance and supply-chain
   validation, preserving the human decision gate and the rule that present
   bytes are not approval.

The owner retains the merge gate. Task Management register-row closure is
excluded from this run. The standing idle workplan remains the general loop
posture; these four distinct owner acts do not silently select a broader Root
production phase.

## Accepted basis and authoritative inputs

- `execution/_Coordination/_TaskManagement/RULING_2026-08-02_ROOT_HARVEST_SLATE.md`
  at SHA-256
  `9fde04e411f1839c6b37ae09e7fba0e8b60a6dd54e434b2bbf2d570e854520d8`.
- `execution/_Coordination/_TaskManagement/SCOPE_CHANGE_INTAKE_TM-ROOT-107_2026-08-02.md`.
- `execution/_Coordination/_TaskManagement/DEL-02-06_HANDOFF_TM-ROOT-108_2026-08-02.md`.
- `execution/_Coordination/_TaskManagement/G4_CI_HANDOFF_TM-ROOT-110_2026-08-02.md`.
- D-APP-84 REV2 Root route at SHA-256
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`.
- Product-delivery owner-intent record at SHA-256
  `9bbb67556765c6c83d6a35a1ace297e4d693d5169281c620dc9b2673229c7e03`.
- D-APP-85 C06 Root route at SHA-256
  `0b34cefdc9abd5927db1b6bdda07225c37c42806ff5b3f946bb182227f08dc41`.
- Accepted Root decomposition revision 1.2 and the initialized, unactivated
  `DEL-02-06` package state.

## Nodes, ownership, dependencies, and returns

| Node | Agent 1 | Objective | Write ownership | Dependencies / holds | Required return |
|---|---|---|---|---|---|
| C0 | CHANGE | Verify and retain the synchronized current `codex/` branch as the task branch; no branch mutation is required. | Read-only Git state | Runs first | Branch identity, base SHA, known run-record-only dirty state |
| S1 | SCOPE_CHANGE | Process the human-initiated Root SOFTWARE decomposition intake from TM-ROOT-107 through every currently authorized SCOPE_CHANGE gate. | New SCA-owned snapshot/control files under `execution/_ScopeChange/`; authoritative decomposition or metadata only after the applicable explicit human gate | May inspect E1 evidence; any authoritative amendment remains human-gated | Gate state, impact assessment, exact proposed action set, affected derivatives, blockers, next human decision |
| W1 | WORKING_ITEMS | Open the first bounded DEL-02-06 activation for the TM-ROOT-108 recovery concern, respecting the accepted first-activation limit to specification, census, evidence-matrix design, and change planning; do not infer implementation authority. | DEL-02-06-local run records only until a later sealed implementation activation exists | Discovery may proceed; amendment/implementation is held on applicable S1 and activation gates | Validated manager return, work graph, exact recovery requirements, implementation/evidence plan, gate required for executable change |
| H1 | HELPS_HUMANS | Implement and verify the already-ruled G4 diff-mode CI wiring without weakening schema checks. | Exact G4 validator/test and CI workflow surfaces; H1 run return | Independent of S1/W1/E1 | Changed paths, positive and missing-manifest negative proof, local validation, CI rerun requirements |
| E1 | EVALUATION | Produce a read-only Pi 0.82.0 authority/executable/supply-chain concordance assessment and decision-ready recommendation. | Quarantined Root `execution/_Evaluation/` output plus E1 return only | Independent discovery; its recommendation informs S1 and the human Pi decision | Evidence-linked findings, supply-chain validation results, exact conflict map, decision options, reruns/blockers |
| C1 | CHANGE | Integrate validated fan-in, commit and push the scoped tranche, and open or update the human-gated PR; do not merge. | Git/file-state closeout plus `_Change/` evidence if needed | All accepted manager returns and required checks | Commit, push, PR URL/head, changed paths, checks, unresolved human gates |

## Concurrency and integration ownership

- `S1`, `W1`, `H1`, and `E1` have disjoint primary write scopes and may run
  concurrently after C0.
- `S1` and `E1` are read dependencies for later semantic decisions; neither
  may silently amend the other's basis.
- `W1` may produce only the accepted first-activation planning/evidence
  package until a later explicit implementation activation is granted.
- `H1` is the only writer to CI/G4 implementation surfaces during the
  parallel stage.
- `C1` is the sole Git integration owner.

## Fan-in gates and human decisions

1. Refuse a SCOPE_CHANGE return that skips any required human gate or treats
   an impact assessment as an accepted amendment.
2. Refuse a DEL-02-06 return that treats the first activation as runtime
   implementation authority or claims closure without restart/replay proof.
3. Refuse a G4 return without both positive proof and a missing-manifest
   negative case.
4. Refuse a Pi return that treats installed/executable `0.82.0` bytes as
   approval, lacks supply-chain evidence, or omits the explicit decision
   required to reconcile the `0.80.10` authority conflict.
5. Return consequential SCOPE_CHANGE, runtime-implementation, Pi-version,
   lifecycle, release, and acceptance choices to the human.
6. Git closeout may create a candidate PR only; merge remains the owner's
   gate.

## Parked work

- TM-ROOT-105 and TM-ROOT-109 remain parked until the Piping loop records the
  requested runtime-surface-needs response.
- Task Management row closure and archival are outside this run.
- No general Root production phase, release, reliance, or professional act is
  selected.

## Amendment 1 — plan version 2

C0 found the newly persisted, untracked run record after the synchronized
preflight. Rather than request a human exception to create a new branch from a
technically dirty checkout, HELP_HUMAN retains the existing
`codex/task-management-federation-closeout` branch as this run's candidate
branch. Its pre-run HEAD is exactly `origin/main@97678a841...`; its old remote
branch is behind only because the owner-directed fast-forward brought this
worktree to current `origin/main`. No rebase, force operation, publication, or
semantic scope change results. C0 is reclassified as read-only verification.

## Amendment 2 — plan version 3

All four manager returns have completed and HELP_HUMAN has validated their
truthful stop states. Three semantic lanes require owner decisions, while H1
is locally ready for hosted CI. Under the loop's standing PR closeout policy
and the owner's express reservation of the merge gate, C1 may now publish the
coherent current tranche to an open PR without merging. The PR is a candidate
container for later ruled follow-up commits; publication does not accept the
SCA, activate DEL-02-06 for implementation, approve Pi `0.82.0`, close any
Task Management row, or change lifecycle/release state.
