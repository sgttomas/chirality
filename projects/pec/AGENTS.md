---
doc_id: PEC-AGENTS
doc_kind: governance.agent_index
status: draft
created: 2026-07-04
---

# AGENTS - PEC Agent Index

This file maps the root Chirality agent framework onto PEC work. It does not
redefine canonical agents; it records how agents should behave inside
`projects/pec`.

## Path Anchors

Prompts and TASK briefs must derive paths from the active checkout:

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
- Set `WORKING_ROOT` to `{REPO_ROOT}/projects/pec`.
- Use `{REPO_ROOT}` and `{WORKING_ROOT}` in project-local instructions and
  briefs instead of machine-specific absolute paths.

## Agent Posture

| Row | Purpose in PEC |
|---|---|
| Normative | Define runtime contracts, product boundaries, data-residency posture, validation policy, and agent workflow constraints. |
| Operative | Execute bounded PEC implementation tranches, tests, evidence updates, and coordination updates. |
| Evaluative | Review, reconcile, audit, and decide whether outputs are acceptable for the next stage. |

## Primary Agents

| Agent | Type | Role in this project |
|---|---:|---|
| `WORKING_ITEMS` | 1 | Primary parent for bounded PEC tranches; selects scope, integrates results, validates, updates coordination state, and prepares closeout. |
| `TASK` | 2 | Executes one sealed implementation, assessment, docs, or evidence sub-scope with explicit read/write bounds. |
| `CHANGE` | 1 | Performs scoped Git/file-state closeout for validated tranches. |
| `RECONCILIATION` | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
| `REVIEW` | 1 | Reviews outputs against scope, validation evidence, product boundaries, and acceptance criteria. |
| `RESEARCH` | 1 | Performs read-only inquiry over accepted docs, source files, and retrieval indexes; returns cited findings without changing state. |
| `AUDIT_*` | 2 | Runs bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |

## Domain-Engine Boundary

PEC is registered as an ADOPTED domain engine under `_DomainEngines/pec/`
(profile Gate 2 adopted by owner ruling 2026-07-05; D-T0-12 adoption note).
Agents must read the tier-0 profile, loop, and decision register before making
claims about PEC harness integration:

- `_DomainEngines/profiles/pec.yaml`
- `_DomainEngines/pec/WORKPLAN_2026-07-04_pec_loop.md`
- `_DomainEngines/_DECISIONS/_REGISTER.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`

Agents must not write `pec.db*`, `backups/**`, `core/**`, `server/**`,
`web/**`, `tools/**`, `fixtures/**`, root manifests, or source-owned docs
unless a PEC implementation brief explicitly grants that project-local scope.
The PEC loop's default writable project-local surfaces are only
`execution/_Coordination/**`, this `AGENTS.md`, and the one-time governance
pointer already added to `docs/STATUS.md`.

PEC record lifecycles are app-owned truth. Approvals, decisions, checks,
comments, holds, issue events, and state transitions are changed only through
PEC's RBAC API and append-only history/audit mechanisms, or by cited owner
statements in governed coordination records. Agents must not edit files or SQL
to manufacture those states.

Do not run the PEC server or a mutating CLI against a non-scratch database.
`npm run drill` is acceptable only because it creates and destroys a scratch DB;
commands such as `npm run seed`, restore, imports with `force=true`, or any
server-backed instance-data capture require explicit owner authority and the
applicable data-residency ruling.

## Project-Wide Execution Discipline

Use bounded tranches by default. A parent agent may orchestrate parallel TASK
fan-out only when subscopes are separable, briefs are explicit, and write
scopes are disjoint.

There may be other agents working in this monorepo with disjoint write scopes.
Treat unrelated dirty files outside the selected tranche as external state. Do
not fix, stage, revert, or interpret them unless the owner directs that work.

## Closeout And Git Discipline

When a tranche is complete and validated, use the project and root closeout
rules: inspect root git status, confirm validation evidence, stage only the
selected tranche scope, avoid unrelated dirty files, and commit/push only when
the branch can fast-forward safely.

Git closeout is source-control hygiene. It is not lifecycle issuance, release
readiness, professional approval, certification, sealing, authentication, or
code-compliance acceptance.

## Issue-Plan Rule

If concrete, actionable issues are discovered that would improve PEC's agentic
development loop, project governance, agents, or skills, record them in at most
one timestamped plan under `{WORKING_ROOT}/plans/` for the session. Do not
create a plan merely to satisfy this instruction when no actionable issue was
found.
