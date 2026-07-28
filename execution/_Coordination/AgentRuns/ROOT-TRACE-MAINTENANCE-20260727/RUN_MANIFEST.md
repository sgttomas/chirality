# Run Manifest — ROOT-TRACE-MAINTENANCE-20260727

Status: `REFRESHED EXACT APPLICATION CANDIDATE — OWNER GATE REQUIRED`
Parent: HELP_HUMAN (Agent 0)
Manager: PROJECT_SETUP (Agent 1)
Accepted Git basis:
`7b0be4d8772a16e5a4774a17988479587d00acca`

## Objective

Refresh the previously prepared RT-A Root trace-maintenance candidate against
current main after W-A became durable, preserving W-A and every unrelated
governed state surface.

## Predecessor package

The frozen predecessor is
`ROOT_TRACE_MAINTENANCE_DECISION_PACKET_2026-07-27_A6B106832`, whose
`ARTIFACT_HASHES.sha256` has SHA-256
`303479841bacdd7206c6adeb58e7119b1b9a00526802c3f9c1e847e64c8948fb`.
Its 83-path `CANDIDATE_PATHS_AND_HASHES.csv` has SHA-256
`82bc6074a77117a75126c6c7acffd5ab7498c038ac015ece2535ce1a43b78a23`.

## Current-basis refresh

All 83 predecessor preimages match immutable current main exactly: 38
`ScopeOfWork.md` paths and 45 `_CONTEXT.md` paths. Zero are stale or missing.
Regeneration produces the same 83 candidate postimages and replacement
cardinalities: 42 Scope-of-Work responsibility assertions, 45 context-tail
assertions, 19 closed-conflict current-state replacements, and eight lifecycle
trace replacements.

## Exact live write scope

- replace the 83 exact execution-tree paths enumerated by the package
  `CANDIDATE_PATHS_AND_HASHES.csv`;
- append only the supplied Receipt 56 block to
  `execution/_Coordination/LOOP_RECEIPTS.md`;
- add
  `execution/_Coordination/AgentRuns/ROOT-TRACE-MAINTENANCE-20260727/RUN_MANIFEST.md`;
- add
  `execution/_Coordination/AgentRuns/ROOT-TRACE-MAINTENANCE-20260727/HANDOFF_STATE.md`; and
- add
  `execution/_Coordination/AgentRuns/ROOT-TRACE-MAINTENANCE-20260727/VALIDATION.md`.

The package `WRITE_SURFACES.csv` is the exact 87-row application inventory.

## Preserved W-A state

- `execution/_Coordination/CURRENT_WORKPLAN.md` remains byte-identical at
  SHA-256
  `efaea5b88a58e9fe408efffde3ac92ae3c4ec55fdde43b6c61f8add7d3913776`.
- `execution/_Coordination/HANDOFF_STATE.md` remains byte-identical at
  SHA-256
  `46364cc4711682ef1916bc3ebf3c01cce534d5dad45b27d86fcab29d5ffa164d`.
- Receipt 55 remains the immediate predecessor of candidate Receipt 56.
- No successor production phase is selected.

## Prohibitions

- No application before exact owner approval.
- No candidate adaptation, silent receipt renumbering, or partial apply.
- No PRD, decomposition, register, scope, acceptance-criteria,
  verification-method, lifecycle, dependency, estimate, schedule, pin,
  implementation, runtime, client, resource-governance, PEC, App, Piping,
  release, reliance, notice, W-A pointer, or unrelated state change.
- No Git closeout without its own authorization.

## Engine identity

Provider: OpenAI
Engine: Codex
Model/build: unknown exact runtime build
