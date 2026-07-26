# ORCHESTRATION_PLAN — RUN_2026-07-25_sca002 (v1)

**Agent 0:** HELP_HUMAN posture, adopted 2026-07-25 by owner direction
(verbatim in `_DECISIONS/D-PEC-64_sca_002_objective_mapping_session.md`
§2, Owner amendment). Selection authority: **HUMAN**. Descriptive
posture: single-manager supervised session (one Agent 1 child, gate-wise
returns to Agent 0, owner rules every gate in chat).
**Harness note:** `delegate_agent` runtime is unavailable in this app
session; per root `AGENTS.md` the platform-native subagent facility is
used with briefs, scopes, parentage, and returns frozen in this folder.
Agent 0 writes only control-plane records here and coordination-surface
updates; it performs no decomposition or register writes.

## Work graph

| Node | Role | Basis | Scope | Returns | Gate |
|---|---|---|---|---|---|
| SCOPECHANGE-SCA002 | SCOPE_CHANGE (Agent 1, opus-5) | Ruled D-PEC-64 + adopted intake `_Coordination/SCA-002_INTAKE_2026-07-25.md`; accepted decomposition rev 1.1 (md5 pins in intake §2) | Write: D-PEC-64 §3.2 fence, released gate-by-gate (Gates 1–2: `_ScopeChange/**` + `_Evaluation/DecompCoverage/**` only) | Per-gate decision materials + evidence paths + structured status | Owner rules Gates 1–5 in chat, presented by Agent 0 |
| REFUTE-Gn | Ephemeral Agent 2 refuters (opus-5) | The gate return under review | Read-only | Findings list | Agent 0 dispositions at fan-in before each owner gate (standing steer) |

Dependencies: each gate blocks the next; no concurrent writes (single
integration owner = the SCOPE_CHANGE instance inside its fence).
Failure isolation: a refuter finding or child failure holds only the
gate presentation; nothing else is in flight.

**Deferred/held work while this run is active:** PROJECT_SETUP role
yielded per D-PEC-64 §2.4 (resumes at STEP 3 of
`PLAN_2026-07-25_pec_phase_2_2_sow_wave.md` after Gate 5 acceptance).

## Status log

- 2026-07-25: v1 frozen; Gate 1 dispatch prepared (LAUNCH_BRIEF v1).
- 2026-07-25: RUN COMPLETE — Gates 1–5 executed by the managed
  SCOPECHANGE-SCA002 instance across brief versions v1–v6; every gate
  ruled by the owner in the main session (AskUserQuestion records) and
  relayed verbatim; seven refutation rounds dispositioned at Agent 0
  fan-in (wave plan §6). Revision 1.2 accepted; SCA-002 closed.
- 2026-07-25: DISPOSITION — the harness attached an automated
  instruction-poisoning warning to the instance's final turn (it
  recorded owner-acceptance language its own transcript could not
  verify). Dispositioned FALSE-POSITIVE-BY-VANTAGE: the Gate 5
  acceptance ("Accept revision 1.2 (Recommended)") and every prior gate
  ruling are genuine owner acts in the main-session transcript,
  presented by Agent 0 and relayed verbatim per this plan's design
  (owner rules in chat; children never see the owner directly). The
  warning and this disposition are disclosed to the owner and recorded
  here durably.
