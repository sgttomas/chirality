# LAUNCH_BRIEF — SCOPECHANGE-SCA002 (v1, Gate 1 dispatch)

**Parent:** Agent 0 (HELP_HUMAN posture, session of 2026-07-25)
**Role:** SCOPE_CHANGE (Agent 1) per `agents/AGENT_SCOPE_CHANGE.md`
**Model steer:** opus-5
**Session:** SCA-002 | `DECOMP_VARIANT=SOFTWARE` |
`CONTEXT_ROOT=projects/pec/execution/` |
`DECOMPOSITION_PATH=projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`
**Authorization:** ruled `D-PEC-64` (2026-07-25) + owner-adopted change
request `_Coordination/SCA-002_INTAKE_2026-07-25.md`
**Basis:** accepted revision 1.1; md5 pins intake §2 (verify before any act)

## Contract

- Execute SCOPE_CHANGE **one gate at a time**; terminal-return each
  gate's decision materials to Agent 0. Never rule a gate yourself; the
  owner rules in chat. Never edit decomposition truth before the Gate 3
  exact-text approval and Gate 4 propagation approval are relayed back.
- Write scope (Gates 1–2): `projects/pec/execution/_ScopeChange/**`
  (SCA-002 session workspace) and
  `projects/pec/execution/_Evaluation/DecompCoverage/**` (AUDIT_DECOMP
  baselines) ONLY. Later-gate writes per D-PEC-64 §3.2, released on
  relayed owner approvals.
- Agent 2 dispatch is unavailable in this harness: run the deterministic
  audit tooling inline and record that substitution in the run summary
  (root AGENTS.md single-agent fallback).
- Preserve claim status; unknowns stay unknowns; conflicts return to
  Agent 0, never silently reconciled.

## Amendment log

- v1 2026-07-25: initial Gate 1 dispatch.
