# Stage-2 Governed Orchestration Plan Brief

Status: `SEALED — PLAN AUTHORING ONLY`
Parent: `HELP_HUMAN`
Manager: `ORCHESTRATOR` (Agent 1)
Date: 2026-07-12

## Objective

Create and present the next governed orchestration plan for D-GOV-16 Stage 2
from synchronized `main`. Do not dispatch or implement any Stage-2 node.

## Accepted basis

- Local `main`, local `origin/main`, and remote `refs/heads/main` are
  synchronized at
  `c9af689118e4e87f329e1ab4c6e71fea331b2674`.
- D-GOV-16 ruling publication:
  `7584718aa32b112e415331736d1a8e68c12ac176`.
- D-GOV-16 proposal snapshot:
  `31e5efd985db4cc7b25543e11a65933979e07e4f`.
- Planning branch: `codex/sow-stage2-plan`, created directly from synchronized
  main at the basis above.
- Exact ruled artifacts and hashes are those in D-GOV-16 items 1–2 and its
  evidence-package index.

## Required inspection

Read the full applicable authority and current state, including:

- D-GOV-16 and D-GOV-15;
- the exact ruled standard and TYPES/SPEC patches;
- the current canonical standard, TYPES, SPEC, affected agents, skills, tools,
  exports, and App Dev runtime consumers;
- Stage-1 sizing/caller inventories and terminal evidence/handoffs;
- the live App Dev and Piping decompositions, coordination states, lifecycle
  records, and package topology needed to form bounded waves; and
- root AGENTS.md plus `agents/AGENT_ORCHESTRATOR.md`.

## Planning work

1. Reproduce the D-GOV-16 tracked census read-only on the synchronized basis:
   counts by project and package, four-file completeness, lifecycle
   distribution, the sole ISSUED member, pilot membership, remaining-member
   count, and sorted path-list digest. A changed membership, lifecycle
   population, conflict, or unclassified active caller is a decision request,
   not silent scope expansion.
2. Refresh the active caller classification sufficiently to define the
   canon/consumer activation tranche. Preserve historical evidence and
   independent DOMAIN/KTY or packet/case schemas.
3. Write an executable, dependency-valid work graph with explicit managers,
   bounded children, read/write scopes, inputs, outputs, checks, immutable
   snapshots, fan-in gates, failure isolation, handoffs, and human decisions.
4. Sequence at least these governed boundaries:
   - exact canon and consumer/tool activation;
   - refreshed census/manifest freeze;
   - atomic integration of the ten verified pilots without merging the
     dual-format pilot branches as-is;
   - bounded package waves for the authorized remaining population;
   - isolated ISSUED `DEL-01-01` representation-replacement preparation and
     explicit human administrative approval;
   - cross-wave RECONCILIATION, rollback window, closure evidence, and a
     separate legacy-retirement decision request.
5. Select and justify terminal fan-out/fan-in, supervised many-to-many, or a
   mixed graph at each boundary. Concurrent writes must be disjoint; any
   Bash-bearing project-root child becomes the serialized integration owner
   for that stage.
6. Make every D-GOV-16 item 1–10 traceable to plan nodes and acceptance gates.

## Required outputs

Under `execution/_Coordination/AgentRuns/SOW-STAGE2-PLAN-20260712/`:

- `ORCHESTRATION_PLAN.md` — authoritative proposed execution plan;
- `WORK_GRAPH.v1.md` — node/dependency/scope/gate graph;
- `CENSUS_REFRESH.md` — synchronized-main census evidence;
- `CALLER_REFRESH.md` — active/retained/historical/independent disposition;
- `D_GOV_16_TRACEABILITY.md` — items 1–10 to nodes/gates;
- `HANDOFF_STATE.md` — plan-presented stop, blockers, rerun rules, next owner;
- `instances/ORCHESTRATOR-PLAN/RETURN.md` and `STATUS.json`.

## Acceptance criteria

- Basis synchronization and D-GOV-16 hashes verified.
- Census result is reproducible and compared with 154 total / 10 pilot / 144
  remaining / one ISSUED; any delta is surfaced.
- No plan node can integrate dual formats or mutate lifecycle during format
  migration.
- Exact canon activation precedes conversion; pilot and corpus integration
  use atomic replacement commits.
- Every wave has independent verification and RECONCILIATION fan-in.
- Failed nodes block only declared dependants; evidence and handoffs persist.
- Legacy retirement remains a later explicit owner act.
- The planning branch contains no changes to canon, projects, agents, skills,
  tools, exports, pilots, or lifecycle records.
- Terminal state is `PLAN_PRESENTED — NO_STAGE2_DISPATCH`.

## Prohibitions

No application of TYPES/SPEC patches, standard copying, tool/consumer change,
census pointer update, conversion, candidate generation, pilot integration,
ISSUED act, lifecycle edit, legacy retirement, execution brief dispatch, Git
merge, or push to `main`.
