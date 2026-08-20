# Launch Brief — Root Governance CI Fix

- Parent: `HELP_HUMAN` via `HELPS_HUMANS`
- Executor form: ephemeral Agent 2 generalist
- Base: `219f695d348f1d83ba904ef4dd38781636b423a6`
- Objective: repair the Git 2.55 fixture-template race and bound the governance workflow's apt/zsh setup.

## Read scope

- `AGENTS.md` (`sha256:268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`)
- `agents/AGENT_HELPS_HUMANS.md` (`sha256:47a30075b4286a7352d78aae9d033d8eead8ef125e4063d0cc7c1235b3e9101a`)
- `tools/practitioner_harness/**`
- `.github/workflows/governance-harness.yml`
- `.github/workflows/piping-desktop-e2e.yml`

## Write scope

- `tools/practitioner_harness/**`
- `.github/workflows/governance-harness.yml`
- `execution/_Coordination/AgentRuns/HELP-HUMAN-ROOT-20260819-GOVERNANCE-CI-FIX/RETURN.md`

## Prohibited

- `projects/**`
- commits, pushes, PR operations, or merges
- copying around or retrying `.git/objects/maintenance.lock`

## Required implementation

1. Inventory every fixture Git initialization/commit path under `tools/practitioner_harness/`.
2. Ensure every Git subprocess used by fixture builders has effective `maintenance.auto=false`, `gc.auto=0`, and `gc.autoDetach=false`, preferably through central pytest-process environment configuration that also covers raw subprocess calls.
3. Add deterministic regression coverage that inspects effective Git config in built fixture repositories; a green full-suite rerun alone is not proof.
4. In `.github/workflows/governance-harness.yml`, add a roughly 15-minute job timeout, reuse verbatim the canonical Ubuntu source configuration step from `.github/workflows/piping-desktop-e2e.yml` before apt, and add a roughly 3-minute timeout to the zsh install step. Preserve other behavior.

## Evidence basis

- Runner Git changed `2.54.0` → `2.55.0` on 2026-08-19 between 15:05Z and 19:52Z.
- Last green main run `32267168751` used 2.54.0.
- Runs `32295433879` attempt 1 and `32304190391` attempt 2 used 2.55.0; both reported `5 failed, 655 passed`, with different tests/templates. Two of three full 2.55 runs failed, so one green rerun is insufficient proof.
- Zsh apt hung in `32295433879` attempt 2 and `32304190391` attempt 1.

## Acceptance checks

- focused deterministic regression tests
- full `tools/practitioner_harness` suite, including xdist where available
- YAML parse and static assertions for timeouts/source block ordering
- `git diff --check`
- root self-check when viable
- `RETURN.md` names exact files, inventory, checks, residual blockers, and next lawful owner (`CHANGE` for Git state)
