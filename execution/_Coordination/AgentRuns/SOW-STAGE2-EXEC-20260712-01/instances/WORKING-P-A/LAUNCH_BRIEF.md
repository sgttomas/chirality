# WORKING-P-A Sealed Launch Brief — v1

Role: `WORKING_ITEMS` Agent 1 manager
Package: App `PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies`
Selected deliverables: `DEL-07-01` through `DEL-07-06` (six exact P3 pilot rows)
Node: `P-A` — Stage-2 pilot preparation only

## Objective and authority

Prepare six exact single-format replacement candidates and durable verification
evidence from the already hash-bound Stage-1 SOW blobs. Do not regenerate or
semantically edit a candidate, modify the live project package, or integrate a
replacement.

Accepted authority: D-GOV-16 ruling
`7584718aa32b112e415331736d1a8e68c12ac176`; accepted Stage-2 P-A contract;
P3_MANIFEST B1/G3 PASS; synchronized main
`0d260eb024d8b8dada0df477b70ac880a6906ffa`; App project instructions and
standing loop; Stage-1 evidence commit
`fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`. This human-ratified root plan is
the owner direction for this lifecycle-neutral format-replacement preparation.
H1/H2 remain unapproved and are irrelevant to these six IN_PROGRESS members.

## Read and write scope

Read: P3/P2 accepted snapshots; the six exact current App deliverable folders;
App project instructions, current decision/register/profile/validation surfaces;
the Stage-1 commit and its PKG-07 frozen-wave evidence; active SOW tools/skill;
Git read-only state. Do not read or modify `.claude-worktrees/`.

Write only:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P4_PILOTS/APP-PKG07/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P-A/**`.

Temporary isolated verification copies may be written under `/tmp` and must be
removed or reported at handoff. No path under `projects/chirality-app-dev/**`,
Git branch/index/ref, root canon/tool/caller, lifecycle, receipt, release,
H1/H2, or retirement surface is writable.

## Work graph and child contract

Record a versioned `MIXED` package graph before child dispatch. The manager is
the serialized extraction/integration owner for the candidate package. Extract
each exact `ScopeOfWork.md` blob from the Stage-1 commit into a disjoint
deliverable candidate directory and record its expected hash:

- DEL-07-01 `9b75621a465553baf47b08b665bbbee8dc39f3d60a1d64b6610b9949c9226744`
- DEL-07-02 `80fbd86600af8516d75d2d11ccf53d304ec36426069728fbe30a8fceb846d952`
- DEL-07-03 `6fa7732954b95314176d81045edeb9492405785cf4568acf210968f903cc9ab0`
- DEL-07-04 `d456e9d29262c0cb9d0fc3350ab52b1b5a36b9c3bfab1378476c2e3ae55a9342`
- DEL-07-05 `f38b0e741949abd9a892e8fea1a93c91be7da95bda668b3c80c2fd4dac7f450e`
- DEL-07-06 `6de59e2a9d6806fb620c673b1da4822337b4c531a41de3186c9f0fde8e10b93e`

Dispatch six separate Agent 2 TASK instances, one per deliverable, using
`TaskSkill: scope-of-work`, `MODE=VERIFY`. Read the complete `AGENT_TASK.md`
and live skill package before sealing child briefs. Each child reads exactly
one P3 row, the current four source files/status/control refs, the extracted
candidate, active tools, and relevant Stage-1 evidence. Each writes only its
own child brief/return/evidence directory under `instances/WORKING-P-A/` and
temporary deterministic outputs under `/tmp`; it must not repair anything.
Children do not delegate. Because only one shared child slot may be available,
serial child dispatch is valid; do not substitute manager self-verification.

Each child independently reproduces the full twelve-part pilot gate as
applicable, subject to `PILOT-VALIDATION-001`: source and status
hashes/current-base equality; exact candidate hash; current legacy-only
`LEGACY_FOUR_DOC` and exact target SOW-only `SOW_V1` validation; claim map and
every target resolution; parity
and source-line preservation; REVIEW checklist generation; repeated HTML
render byte stability and safety; lifecycle/control containment; Stage-1
evidence identity; schema/content, preservation, and substrate verdicts; and
an exact five-path future replacement manifest (add SOW, delete four legacy
files). Any discrepancy is FAIL, never repair.

## Manager fan-in and checks

Require six terminal PASS returns. Aggregate exact source/status/candidate
hashes, mappings, source-line counts, checklist/render results, candidate and
rollback manifests, and child provenance. Run the applicable App project
checks from the current profile once at package level (at minimum typecheck,
full Vitest, production build, practitioner self-check/full harness, and
format/containment checks unless a recorded profile rule makes a check
inapplicable). Checks are read-only with respect to the package candidate.

Required outputs include package `WORK_GRAPH.md`, `PILOT_MANIFEST.tsv`,
`REPLACEMENT_MANIFEST.tsv`, `ROLLBACK_MANIFEST.tsv`, `CHECKS.md`,
`PACKAGE_HANDOFF.md`, six candidate/evidence subpackages, terminal
`RETURN.md`, and `STATUS.json`. Run schema/hash/path/diff hygiene checks.

Return `PASS`, `PARTIAL`, `BLOCKED`, or `DECISION_REQUIRED` with exact
coverage and evidence. Any source/status/candidate drift, semantic delta,
failed child/check, missing member, project write, or authority conflict blocks
P-F. On PASS next owner is HELP_HUMAN for cross-package pilot fan-in; this
manager does not release or integrate conversion.
