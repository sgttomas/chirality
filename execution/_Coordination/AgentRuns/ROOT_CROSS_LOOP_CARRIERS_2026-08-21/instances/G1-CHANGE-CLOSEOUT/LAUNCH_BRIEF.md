# G1 CHANGE Launch Brief — Dependency-Ordered Closeout

- **RunID:** `ROOT_CROSS_LOOP_CARRIERS_2026-08-21`
- **Parent:** `HELP_HUMAN`
- **Role:** `CHANGE` (Agent 1)
- **Purpose:** Preserve the owner-directed one-branch/one-PR closeout in dependency order.
- **Current branch:** `codex/root-cross-loop-carriers-20260821`
- **Integration target:** `main`

## Stage 1 objective

Create one scoped dependency commit containing the completed TM-ROOT-125
engineering product, G4 tranche manifest, routed change notices, and the
already-complete H1/T1 fan-in and owner decision-preparation records. Do not
push and do not open a PR at Stage 1. The governed register closeout, receipt,
and handoff follow in Stage 2 after this commit supplies immutable engineering
evidence.

## Authorized Stage 1 paths

- `agents/AGENT_HELP_HUMAN.md`
- `tools/validation/validate_agent_instructions.py`
- `tools/validation/test_validate_agent_instructions.py`
- `docs/governance_harness/tranche_manifests/ROOT-TM125-AGENT0-A2-VALIDATOR-ALIGN-20260821.yaml`
- `_DomainEngines/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md`
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md`
- `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-21_ROOT_TM125_AGENT0_A2_VALIDATOR_ALIGNMENT.md`
- `execution/_Coordination/AgentRuns/ROOT_CROSS_LOOP_CARRIERS_2026-08-21/`

## Recorded checks

- `python3 -m pytest tools/validation -q` — 319 passed.
- Live agent-instruction validator — 34 files, zero errors/warnings.
- Instruction entrypoint validation — PASS.
- Governance harness G0–G4 — PASS, including 40 manifests.
- Root live/archive register validation — PASS before closure (23 live / 102 archived).
- `git diff --check` — PASS.

## Fences

- Stage only the named tranche paths.
- No merge, rebase, reset, force push, cleanup, or history rewrite.
- Do not amend accepted snapshots or immutable derivative evidence.
- Do not select either owner decision in `OWNER_DECISION_PACKET.md`.
- Return the commit SHA and resulting status to HELP_HUMAN.

## Acceptance check

The dependency commit exists on the named branch, contains only scoped paths,
and leaves the checkout ready for the governed TM-ROOT-125 closure commit.
