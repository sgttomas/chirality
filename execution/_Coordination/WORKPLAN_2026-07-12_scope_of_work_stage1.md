# Scope-of-Work Stage 1 — root governance standing workplan

> **Epistemic status: agent-authored plan — not authority.** This standing
> workplan implements the owner-directed Stage-1 course recorded in
> `plans/deliverable_scope_of_work_stage1_plan_2026-07-12.md`. It records the
> loop protocol, fences, and source pointers only. Live decisions, accepted
> snapshots, Git state, and current human direction govern on disagreement.

## Goal

Establish the root governance loop, design and validate a candidate
`chirality-deliverable-sow/v1` contract, and—only after an explicit ruling
authorizes its variance—supervise bounded App Dev and Piping pilots that can
support or reject a separately ruled Stage 2.

Stage 1 does not ratify exact TYPES/SPEC amendments, replace the live
four-document contract, merge converted pilot deliverables, or authorize the
remaining corpus conversion.

## Step 0 — Discover every iteration

1. Resolve the repository, branch, worktree, remote divergence, and dirty
   paths. Treat unrelated changes as external state.
2. Read root `AGENTS.md`, the latest receipt in this directory, and the live
   governance decision register. Verify every relied-on plan statement against
   its cited source.
3. Inspect the latest App Dev and Piping loop receipts and their live Git state
   before proposing any project-local activation.
4. Determine whether the prerequisite governance ruling, exact pilot variance,
   source-state snapshot, and execution posture are accepted. If any is absent,
   prepare only the evidence or decision slate that live authority permits.
5. Derive the current work graph from accepted dependencies and write fences.
   Do not copy a prior graph as current state.
6. Return the live orientation required by `LOOP_INIT.md` before execution.

## Standing lanes

| Lane | Agent owner | Purpose | Release condition |
|---|---|---|---|
| Machinery | HELPS_HUMANS | Candidate schema, skill, tools, validators, registries, compatibility, and deprecation design | Explicit human authorization for candidate implementation |
| Pilot supervision | HELP_HUMAN | Cross-project activation, dependencies, notices, amendments, and validated fan-in | Accepted path-scoped variance and frozen source basis |
| Preservation audit | RECONCILIATION | Claim mapping, parity, source-state binding, and pilot closure evidence | Candidate outputs plus independent audit brief |

WORKING_ITEMS is never the root-loop persona. One WORKING_ITEMS instance may be
activated per authorized project package, through HELP_HUMAN or direct human
entry, and remains bounded to that package.

## Dependency order

1. Repair the root loop entry and root coordination home.
2. Produce commit-bound sizing and consumer-inventory reports.
3. Present the Stage-1 decision slate, including the variance, lifecycle
   neutrality, execution posture, abort posture, and Stage-2 gates.
4. Stop for the owner ruling.
5. If authorized, build and validate the candidate machinery while preserving
   the legacy path as authoritative.
6. Freeze the accepted pilot source-state basis and candidate schema revision.
7. Activate one calibration deliverable in each project through its project
   loop and explicit per-run variance steer.
8. Audit calibration results; revise only within live authority; freeze the
   schema used for steady-state measurement.
9. Run the frozen-schema package pilots, then RECONCILIATION fan-in.
10. Close Stage 1 with a PASS/FAIL handoff and stop for Stage-2 direction.

## Root write fences

Before a Stage-1 ruling, write only planning, evidence, candidate decision, and
root loop surfaces explicitly directed by the human.

After an authorizing ruling, the maximum candidate write surface is:

- root candidate governance documents and the exact agents, skills, tools,
  tests, registries, and exports named by that ruling;
- root `execution/_Coordination/**` runtime records;
- the exact App Dev PKG-07 and Piping PKG-13 pilot paths named by the accepted
  variance, only inside isolated pilot worktrees;
- project-local run records produced by real child execution.

Always denied in Stage 1:

- non-pilot deliverables and the remaining corpus;
- DOMAIN/KTY, archived, template, fixture, export-source, or generated trees
  unless a specific component test fixture is expressly authorized;
- Piping's ISSUED deliverable;
- historical receipts, concordance artifacts, briefs, and accepted snapshots;
- `_STATUS.md` or lifecycle changes in pilot deliverables;
- direct edits to generated HTML or treating it as authority;
- merge of dual-format pilot deliverables to `main`;
- Stage-2 implementation without a new human ruling.

Git closeout is CHANGE-owned. The owner merges.

## Pilot contract

- Canonical candidate: `ScopeOfWork.md` with schema marker
  `chirality-deliverable-sow/v1`.
- HTML: deterministic, on-demand, non-authoritative, untracked derivative.
- Legacy four production documents: authoritative throughout Stage 1.
- `_STATUS.md` and other underscore control/generated surfaces: separate and
  unchanged by conversion.
- Dual format: permitted only under the exact accepted pilot variance.
- Content change: classify as `CONFLICT`; route to SCOPE_CHANGE or the human.
- Lifecycle: neutral. REVIEW may test deterministic checklist derivation but
  performs no transition.

Calibration targets and full Stage-2 entry gates are defined in
`plans/deliverable_scope_of_work_stage1_plan_2026-07-12.md`; verify them against
the live project trees and ruling before use.

## Orchestration records

Real root runs persist under:

```text
execution/_Coordination/AgentRuns/<RunID>/
```

Do not pre-create `<RunID>`. The first executing parent creates it with a work
graph and launch evidence. Project-local child runs persist under their owning
project's corresponding `AgentRuns` root. Root stores the cross-project graph,
notices, dispositions, and fan-in.

Use native hierarchical agents only after demonstrating equivalent sealed
briefs, scopes, parentage, status, returns, and durable evidence. If the
accepted ruling permits sequential fallback, record native-substrate failure
separately and continue sequentially. Never relabel a substrate failure as a
schema or project-content failure.

## Check and receipt discipline

- Root changes: run agent, skill, instruction-entrypoint, path-anchor, public
  export/staging, and practitioner-harness checks applicable to changed paths.
- App Dev pilot waves: run the project-registered frontend/harness checks once
  per commit-shaped wave.
- Piping pilot waves: run `harness-pytest` and `harness-self-check` once per
  commit-shaped wave, plus any registered changed-path checks.
- Conversion: prove source hashes, claim disposition completeness, parity,
  byte-identical `_STATUS.md`, deterministic HTML, and unchanged historical
  evidence.

Append only a minimal pointer receipt after each lawful tranche. Detailed
reports and run evidence live in their governed artifact packages, not in the
receipt ledger.

## Terminal conditions

**PASS:** all ruled Stage-1 gates pass; root and both project handoffs identify
the frozen basis, derivative status, validation evidence, blockers, and a
Stage-2 recommendation. Stop for a new ruling.

**FAIL:** preserve a failed handoff with cause classification and rerun
requirements; do not merge pilot deliverables; retire failed pilot branches or
worktrees only after evidence capture. Stop for disposition.

**PARKED:** only a human ruling, scope decision, lifecycle act, authority
change, shared-write resolution, or Stage-2 authorization can advance the
remaining work. Present the decision slate and stop.
