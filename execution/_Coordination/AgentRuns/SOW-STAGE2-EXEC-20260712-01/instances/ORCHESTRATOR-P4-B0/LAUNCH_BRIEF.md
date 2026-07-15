# ORCHESTRATOR-P4-B0 Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `ORCHESTRATOR` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@e8f59a63372f38d9e788ac39b39995558f5aba73`

## Objective and topology

Perform the fresh P4 wave preflight for the exact 22 ordinary Piping members
in PKG-14 through PKG-17, freeze current source/status/control/dependency and
method bindings, derive the minimum consecutive author/verifier batches under
the accepted limits, and emit one sealed package brief per package. Do not
convert or write project files. Execute directly as ORCHESTRATOR; no child is
needed for this single bounded preflight instance.

## Required reads and scope

Read root/Piping `AGENTS.md`, `agents/AGENT_ORCHESTRATOR.md`, standing
workplan, accepted Stage-2 graph/plan, P3 execution manifest, W-P3 postmerge
handoff, earlier accepted predecessors, active amendments including PKG-00
exclusion, package batching, runtime efficiency, normalization, topology
clarification, and post-I1 closure correction; current Piping decomposition/
dependency truth; active scope-of-work standard/skill/tools/tests; and live
Git refs.

Selected members are exactly P4 rows for PKG-14 (5), PKG-15 (4), PKG-16 (4),
and PKG-17 (9). Require 22/22 complete legacy-only, `IN_PROGRESS`, non-pilot,
non-ISSUED members; no live `ScopeOfWork.md`; exact current hashes; no overlap
with accepted SOW predecessors; active PKG-00 upstream-basis direction; and no
unclassified drift.

Write scope is exclusively:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P4/preflight/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/ORCHESTRATOR-P4-B0/**`, except this brief.

No project, candidate, prior snapshot, graph/plan/receipt, Git, lifecycle,
release, reliance, rollback, retirement, or H2 write is permitted.

For each package compute physical source-line totals and partition by ascending
numeric DeliverableID into the minimum consecutive batches containing at most
five members and at most 2,053 frozen legacy source lines. Freeze one package
manager brief that requires a fresh package manager, one fresh author then one
fresh evidence-only verifier per batch, complete per-member evidence, safe
mechanical repair/attempt retention/rebinding, no live project writes, and
later direct RECON fan-in without a redundant child layer.

Run all applicable census, hash, format, lifecycle, dependency-direction,
method/tool, containment, JSON, and check-profile validations. Return `PASS`,
`BLOCKED`, or `DECISION_REQUIRED` with immutable self-bound snapshot, exact
package/batch plan, briefs, blockers/unknowns/waivers, derivative status,
rerun triggers, and next dependency-valid releases.
