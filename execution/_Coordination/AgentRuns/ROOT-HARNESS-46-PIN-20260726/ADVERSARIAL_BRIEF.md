# Sealed Brief — Read-only Live-Root Pin Adversarial Review

## Parent and construction

- Parent: `HELPS_HUMANS` (Agent 1)
- Child form: one ephemeral generalist Agent 2
- Delegation: prohibited
- Writes: prohibited

## Objective

Adversarially inspect the proposed bounded M2 refresh for the three stale
live-root static tests exposed by PR #369. Determine the exact static
assertions, names, and comments required to bind:

1. 46 total status files;
2. zero mismatches;
3. lifecycle distribution 45 `INITIALIZED` plus one `OPEN`;
4. unchanged absence of a Root DAG pointer; and
5. the state-plus-pin atomic SCC.

Also review G4 manifest sufficiency, downstream pin/mirror routing, public
export derivatives, prohibited scope, and acceptance checks.

## Read scope

- `agents/AGENT_HELPS_HUMANS.md`
- `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`
- `docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md`
- `tools/practitioner_harness/test_root_adoption.py`
- `tools/validation/validate_instruction_tranche_manifest.py`
- `execution/_harness/adapter.yaml`
- relevant project/domain pin manifests and public-export derivative records
- Git history at `ff04694`, `dd28d201b`, and the PR #369 failure log

## Constraints

- No writes, Git actions, authority claims, or delegation.
- No dynamic assertions and no production harness change.
- No edits outside the three failing tests, their names/comments/assertions,
  the directly coupled module-level LIVE-tree summary authorized by amendment
  01, the one G4 manifest, and this run-record directory.
- No Project Setup, audit, scaffold, adapter, decomposition, or runtime state
  change.

## Acceptance

The return must identify any omitted static assertion, scope expansion,
incorrect SCC claim, missing downstream notice, undeclared export derivative,
or check too weak to support closure. It must state a final bounded verdict.
