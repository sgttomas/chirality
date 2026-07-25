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
- v2 2026-07-25 (owner Gate 1 ruling relayed): scope width **O-A**;
  actions A001–A006 confirmed + **A007** added (W-1 §5 envelope-prose
  fix; D-PEC-64 §4.3 window amended same day to admit it); SOW-021
  constrained ⊆ {OBJ-005}. R-2b-g1 dispositions relayed: derivative-
  package status table (intake §6.5) is a mandatory Gate 2 output;
  record snapshot-artifact deferrals (Amendment_Actions.csv at Gate 3;
  Pre_Change_Coverage.json copy pre-Gate-5); W-1 characterization
  corrected (MODIFY-legal, window-excluded). Gate 2 released; write
  scope unchanged (Gates 1–2 surfaces only).
- v3 2026-07-25 (owner Gate 2 ruling relayed): impact assessment
  ACCEPTED — Q1 "Accept": no Supersession_Delta.csv owed under O-A,
  conditional on Gate 3 attributions remaining PRD-consumptive
  (re-affirmed at Gate 3); Q2 "Record as deferred": OI-B (64
  _REFERENCES.md rev-1.1 pointers) recorded in Handoff_State as a
  deferred obligation owned by resumed PROJECT_SETUP; no fence change.
  Gate 3 released: draft exact amendment text A001–A007 + the 9
  attribution candidates with per-row PRD warrants; write
  Amendment_Preview.md + Amendment_Actions.csv (deferred artifact now
  due). Write scope still _ScopeChange/** only — no decomposition
  edits until the Gate 3 approval and Gate 4 plan are relayed.
