# TASK_MANAGEMENT launch brief — App v3 G0 triage preparation

RunID: `APP_TM_TRIAGE_2026-08-24`

Parent: `HELP_HUMAN` (Agent 0)

Executor: canonical `TASK_MANAGEMENT` Agent 1 under
`agents/AGENT_TASK_MANAGEMENT.md`.

## Purpose

Prepare the owner-facing G0 v3 release triage packet authorized by A10-A.
Make no disposition, register mutation, notice adoption/routing, lifecycle
change, or implementation act.

## Basis and instruments

- Branch: `codex/app-tm-triage-2026-08-24`.
- Git basis: `8884b143f3d8dbca49756e981e4e20299d55875d`.
- Steer SHA-256:
  `8b7319421ddb09568fc02a2e5c0750ac725a81fafb6491951f396509e897373b`.
- A10 SHA-256:
  `0908fee812919291979dd486dd9748fda21b9fb4b20afb13604a1a3e02bd8aa2`.
- App register required identity:
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`.

## Read scope

Repository tracked bytes needed to verify the five triage rows, both notices,
the Root TM-ROOT-122 closure echo, DEL-02-06 acceptance/held bindings,
SCA-APP-008 application/audit, Electron decision/manifests/governed mirrors,
and the seven remaining OPEN-row sources. Invocation-local federation reads
all four canonical registers.

## Write scope

Exactly:

1. new files under
   `execution/_Coordination/_TaskManagement/TRIAGE_2026-08-24_G0_V3_RELEASE/`;
2. new files under
   `execution/_Coordination/AgentRuns/APP_TM_TRIAGE_2026-08-24/`; and
3. one Receipt-201 append to `loop/LOOP_RECEIPTS.md`.

No live/closed register, existing notice, scope-change, contract,
decomposition, corpus, dependency, status, lifecycle, frontend, Root-loop,
agent, tool, or plan write is permitted.

## Required output checks

- mandatory federation preflight `COMPLETE`, limitations disclosed, zero
  register writes;
- packet contains the five-row triage, Electron candidate, both notice
  adoption assessments, seven-row staleness/closure echo, and exact unapplied
  CSV post-image/diff;
- live register remains exact at basis and validates;
- Receipt 201 has parent Receipt-200;
- candidate whitespace against the exact basis, receipt validator,
  `git diff --check`, and exact containment pass.

If any identity or claim disagrees, stop fail-closed without widening.
