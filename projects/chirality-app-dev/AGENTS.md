---
doc_id: APP-AGENTS
doc_kind: governance.agent_index
status: draft
created: 2026-06-15
---

# AGENTS - Chirality App Dev Agent Index

This file maps the general Chirality agent framework onto Chirality App
development. It does not redefine the canonical agent framework; it specifies
how the existing agent roles should be used for this project.

## Path Anchors

Executable prompts and TASK briefs must derive paths from the active checkout:

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
- Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.
- Use `{REPO_ROOT}` and `{WORKING_ROOT}` in project-local instructions and
  briefs instead of machine-specific absolute paths.

## Agent Posture

| Row | Purpose in Chirality App Dev |
|---|---|
| Normative | Define runtime contracts, product boundaries, validation policy, and agent workflow constraints. |
| Operative | Execute bounded app-integration tranches, implementation slices, tests, evidence updates, and docs updates. |
| Evaluative | Review, reconcile, audit, and decide whether outputs are acceptable for the next stage. |

## Primary Agents

| Agent | Type | Role in this project |
|---|---:|---|
| `WORKING_ITEMS` | 1 | Primary parent for bounded app-integration tranches; selects scope, integrates results, validates, updates coordination state, and prepares closeout. |
| `TASK` | 2 | Executes one sealed implementation, assessment, docs, or evidence sub-scope with explicit read/write bounds. |
| `CHANGE` | 1 | Performs final Git/file-state closeout for validated tranches: scoped status review, staging, commit, and fast-forward-safe push. |
| `RECONCILIATION` | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
| `REVIEW` | 1 | Reviews project outputs against scope, validation evidence, product boundaries, and acceptance criteria. |
| `RESEARCH` | 1 | Evidence-grounded, read-only inquiry over accepted decompositions, governance/source docs, and retrieval indexes; returns cited findings without changing project state. |
| `AUDIT_*` | 2 | Runs bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |

## Project-Wide Execution Discipline

Use bounded app-integration tranches by default. A parent `WORKING_ITEMS`
agent may orchestrate parallel `TASK` fan-out only when subscopes are
separable, briefs are explicit, and write scopes are disjoint.

Agents may write inside the selected tranche scope, required evidence and
coordination artifacts, and project-local plans created under the issue-plan
rule below. Do not write root governance files, root agent instructions, root
skills, or root tools unless the human explicitly directs that governance
work.

There may be other agents working in this monorepo with disjoint write scopes.
Treat unrelated dirty files outside the selected tranche scope as external
state. Do not fix, stage, revert, or interpret them unless the human directs
that work.

## Closeout And Git Discipline

When a tranche is complete, validated, and project closeout rules allow it,
the parent `WORKING_ITEMS` agent hands off to a `CHANGE` agent/subagent for
final Git/file-state review. `CHANGE` should commit and push the validated
tranche as the ordinary terminal action when git state allows closeout;
per-run `APPROVE:` tokens are not required for scoped closeout commit/push.

If a `CHANGE` agent/subagent is unavailable, perform the `CHANGE` closeout
checklist inline:

- inspect root git status;
- confirm validation evidence and skipped-check notes;
- stage only files in the selected tranche write scope, required
  evidence/coordination artifacts, and any explicitly created governance-issue
  plan;
- do not stage unrelated dirty files;
- commit the scoped tranche when validation and staging are clean;
- fetch or otherwise verify upstream state before pushing;
- push only when the upstream branch can be fast-forwarded to the local scoped
  commit.

If the remote branch has advanced and local `HEAD` does not already include
it, stop and surface the conflict. Do not merge, rebase, force push, or judge
another agent's work during ordinary closeout.

Git closeout is source-control hygiene. It is not lifecycle issuance, release
readiness, professional approval, certification, sealing, authentication, or
code-compliance acceptance.

## Issue-Plan Rule

If concrete, actionable issues are discovered that would improve the agentic
development loop, project governance, agents, or skills, record them in at
most one timestamped plan under `{WORKING_ROOT}/plans/` for the session. Do
not create a plan merely to satisfy this instruction when no actionable issue
was found.
