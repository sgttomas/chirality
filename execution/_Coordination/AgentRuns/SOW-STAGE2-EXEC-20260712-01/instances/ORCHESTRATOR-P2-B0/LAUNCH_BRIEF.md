# ORCHESTRATOR-P2-B0 Sealed Launch Brief

Parent: `HELP_HUMAN`
Role: `ORCHESTRATOR` (Agent 1)
Run: `SOW-STAGE2-EXEC-20260712-01`
Brief version: `1`
Basis: synchronized `main@eaad463c0d481f6f1654e6adb5ee718f566176e9`

## Objective and topology

Perform the fresh P2 wave preflight for the exact 29 ordinary Piping members
in PKG-05 through PKG-09, freeze current source/status/control/dependency and
method bindings, derive the minimum consecutive author/verifier batches under
the accepted limits, and emit one sealed package brief per package. Do not
convert or write project files. Execute directly as ORCHESTRATOR; no child is
needed for this single bounded preflight instance.

## Required reads and scope

Read root/Piping `AGENTS.md`, `agents/AGENT_ORCHESTRATOR.md`, the standing
workplan, accepted Stage-2 graph/plan, P3 execution manifest, W-P1/I1 accepted
handoffs, active amendments including PKG-00 exclusion, package batching,
runtime efficiency, normalization, topology clarification, and the post-I1
closure correction; current Piping decomposition/dependency truth; active
scope-of-work standard/skill/tools/tests; and live Git refs.

Selected members are exactly P3 rows for PKG-05 (5), PKG-06 (5), PKG-07 (8),
PKG-08 (6), and PKG-09 (5). Require 29/29 complete legacy-only,
`IN_PROGRESS`, non-pilot, non-ISSUED members; no live `ScopeOfWork.md`; exact
current hashes; no overlap with accepted SOW predecessors; active PKG-00
upstream-basis direction; and no unclassified drift.

Write scope is exclusively:

- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P2/preflight/**`;
- `execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/ORCHESTRATOR-P2-B0/**`, except this brief.

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
