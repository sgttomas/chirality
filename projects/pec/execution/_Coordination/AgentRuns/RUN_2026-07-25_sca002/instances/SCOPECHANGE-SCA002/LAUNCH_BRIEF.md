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
- v4 2026-07-25 (owner Gate 3 ruling relayed): Q1 all seven per-row
  attributions AS RECOMMENDED; Q2 INDIRECT-8 affirmed OBJ-001;OBJ-002;
  Q3 drop "(best-effort)" (3b included); Q4 A008 approved + D-PEC-64
  §4.3 amendment #2 recorded (front-matter lines + DL-17 append
  admitted); Q5 complete exact text approved as drafted. Gate 3
  CLOSED. Gate 4 released: propagation plan (Propagation_Plan.md) incl.
  the _CONTEXT.md refresh-vs-defer decision materials. Write scope
  still _ScopeChange/** only until Gate 4 approval + Gate 5 release.
- v5 2026-07-25 (owner Gate 4 ruling relayed): Q1 "(i) All 64,
  P-supersede" — full pointer refresh, supersession-note text variant;
  Q2 "Approve and release" — the propagation plan v2 is APPROVED and
  Gate 5 is RELEASED. Write scope now the full D-PEC-64 §3.2 fence:
  the four amendment targets per the Gate-3-approved exact text only,
  the 64 _CONTEXT.md files (two line classes, plan v2 exact text),
  _ScopeChange/** snapshot completion + _LATEST.md repoint,
  _Evaluation/DecompCoverage/** post-change audit. No git operation;
  handoff file list + recommended message returned to Agent 0.
- v6 2026-07-25 (Agent 0 disposition — plan amendment v2.1, two-pass
  audit): Gate 5 aborted at step 12 per the abort rule (correct) on a
  plan-internal circular dependency: Check 10 requires the complete
  snapshot artifact set, but Post_Change_Coverage.json/Handoff_State/
  RUN_SUMMARY are written post-audit (one cites the audit). Amendment
  (procedural only; no new write surface — a second COV snapshot lands
  in the same §3.2 grant; no text/window change; disclosed to the
  owner at Gate 5 acceptance): TWO-PASS AUDIT — the step-12 run stands
  as interim evidence; complete steps 13–14; fill A006's audit-derived
  slots and Post_Change_Coverage's citation from the FINAL audit;
  re-run the audit (second COV snapshot) expecting Check 10 PASS;
  finalize evidence; steps 15–17 unchanged. Resume from current
  applied state (no rollback — steps 2–11 verified).
