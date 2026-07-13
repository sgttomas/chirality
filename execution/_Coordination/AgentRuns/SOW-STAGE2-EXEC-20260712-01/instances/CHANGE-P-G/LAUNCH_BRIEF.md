# CHANGE-P-G Sealed Launch Brief — v1

Parent: `HELP_HUMAN`  
Role: `CHANGE` Agent 1  
Run: `SOW-STAGE2-EXEC-20260712-01`  
Dependency: `P-F-R1 ACCEPTED`

## Objective and standing approval

Integrate the accepted ten-pilot release set through ten serial atomic
single-format replacement commits, bind the integration evidence, open one
run-scoped PR, merge it under `amendments/HUMAN-STEER-001.md`, synchronize
main, and record an immutable postintegration handoff.

Approval covers the PR merge throughout this goal. It does not cover a failed
gate, extra path, pilot-branch merge, semantic reinterpretation, status/control
or lifecycle edit, force/history rewrite, destructive cleanup, H1/H2, action
on the ISSUED member, product release, or legacy retirement.

## Required basis and accepted release set

- Exact synchronized local main, origin/main, and remote main:
  `0d260eb024d8b8dada0df477b70ac880a6906ffa`.
- P4 acceptance:
  `snapshots/P4_PILOTS/preintegration-r1/ACCEPTANCE.md`, SHA-256
  `8e5d453f98e7be40256c200f15e80eb05df02f0167b037b90d1f59332ff10224`.
- P4 acceptance manifest SHA-256:
  `84e11ec2c8268aafd3297e95f45cfc5463ca0d1f09563c8bf454172b8ba4c9b0`.
- Exact integration manifest:
  `snapshots/P4_PILOTS/preintegration-r1/REPLACEMENT_MANIFEST.tsv`, 50
  unique rows, ten SOW additions and 40 legacy deletions.
- Exact inverse:
  `snapshots/P4_PILOTS/preintegration-r1/ROLLBACK_MANIFEST.tsv`.
- Candidate bytes only from
  `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P4_PILOTS/**`.
- All ten members are IN_PROGRESS. H1/H2 remain unapproved. Piping DEL-01-01
  is outside this tranche.

Read root and both project `AGENTS.md` files plus the complete `AGENT_CHANGE`
package before acting. Do not inspect or modify `.claude-worktrees/`.

## Branch and exact commit architecture

Require no in-progress Git operation and no project-tree change before branch
creation. Preserve the declared dirty pilot evidence while creating
`codex/sow-stage2-pilots` from the exact basis. Stop on an unexplained branch
or remote collision.

1. First make one evidence-only binding commit containing all and only the
   current authorized P4 pilot preparation, failed-attempt preservation,
   repair, reconciliation, acceptance, candidate, amendment, work-graph, and
   CHANGE-P-G launch/readiness evidence under this root run. Do not stage
   `.claude-worktrees/` or a project path in this commit.
2. Then make exactly ten serial deliverable commits in this order:
   App `DEL-07-01` through `DEL-07-06`, then Piping `DEL-13-01` through
   `DEL-13-04`.
3. Each deliverable commit must contain exactly five paths for its one
   manifest member: add the exact accepted `ScopeOfWork.md`; delete
   `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
   It must contain no `_STATUS.md`, control, evidence, or other path.
4. After the ten replacements, make an evidence-only integration binding
   commit for the exact integration snapshot, receipts, checks, return, and
   status. Do not amend the ten deliverable commits.

Never merge either Stage-1 pilot branch and never cherry-pick its commits.
Obtain only the already accepted candidate blobs. Do not regenerate,
normalize, or insert a marker.

## Mandatory preimage, per-commit, and post-state gates

1. Reproduce all hashes in `ACCEPTANCE_MANIFEST.tsv`; require terminal PASS
   manager contracts, zero findings/blockers/unknowns/waivers, exact
   candidate hashes, exact 40 live source hashes, ten exact `_STATUS.md`
   hashes, ten `LEGACY_FOUR_DOC` pre-states, and zero live SOW.
2. Verify the 50 replacement paths are unique, are grouped into ten disjoint
   five-path sets, match current preimages, contain no control/status path,
   and have an exact operation/hash inverse in the rollback manifest.
3. Before and after every deliverable commit, verify current HEAD parentage,
   exact five-path diff, exact candidate byte, absent four legacy files,
   byte-identical `_STATUS.md`, unchanged lifecycle `IN_PROGRESS`, and resolver
   result exactly `SOW_V1` with no legacy/dual/partial/invalid state. Record the
   commit SHA, tree/preimage/postimage hashes, status hash, path inventory,
   candidate hash, and non-history-rewriting rollback instruction.
4. Stop remaining integration on any mismatch or failed check. Preserve
   already created branch evidence; do not force, rewrite, reset, clean, or
   automatically revert. Main must remain unchanged unless the entire PR
   passes and merges.
5. After ten commits, require 10/10 `SOW_V1`, zero pilot legacy/dual/invalid,
   all ten statuses byte-identical, all ten IN_PROGRESS, and no other governed
   deliverable or project path changed from the PR base.
6. Rerun proportionate current checks: SOW resolver/tool tests; App focused
   consumer tests and typecheck/build/profile checks required by App
   instructions; Piping four-document/dependency/profile checks required by
   Piping instructions; applicable root self-check/governance harness; exact
   manifests, portability, JSON/CSV/TSV structure, path containment, and
   `git diff --check`. A required failure blocks the PR.

## Integration evidence and remote closeout

Write CHANGE records only under `instances/CHANGE-P-G/**` and a new immutable
integration derivative under `snapshots/P4_PILOTS/integration/**`. Include at
least `INTEGRATION_READINESS.md`, one receipt per deliverable, a ten-row commit
ledger, exact post-state/status ledger, copied/bound rollback manifest,
checks, an internal hash manifest, handoff, terminal return, and source-bound
status. Each receipt must cite the accepted preintegration snapshot and make
no lifecycle or reliance claim.

Push the branch, open one non-draft PR to main, verify remote changed paths and
commit architecture, wait for every required check, and merge only on PASS
under HUMAN-STEER-001 using the repository-permitted merge method. No force or
history rewrite.

After merge, synchronize local main, origin/main, and remote main; require
divergence 0/0 and tracked-clean state except untouched `.claude-worktrees/`.
Reverify the ten live post-states and unchanged statuses. Record the PR,
merge/final-main identities, required checks, exact path/commit inventories,
rollback obligations, derivative status, rerun rules, and next owner
HELP_HUMAN. Bind postmerge records with an ordinary evidence-only commit/push
if needed, then resynchronize and reverify refs.

Return `PASS`, `PARTIAL`, `BLOCKED`, or `DECISION_REQUIRED` with branch,
evidence and ten deliverable commit SHAs, PR URL/number, check results, merge
and final-main SHAs, exact accepted counts, remaining state, blockers,
unknowns, waivers, rerun/rollback rules, and handoff. P-G PASS releases only
the A1 ordinary-wave preflight; it does not authorize H1, H2, ISSUED action,
release, or retirement.
