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
| `HELP_HUMAN` | 0 | Default supervising entry for the open-ended standing development loop; aligns the human and workflow, supervises discovery and the selected Agent 1 managers, and validates cross-manager fan-in. Direct Agent 1 entry remains lawful for a matter already bounded to one manager. |
| `WORKING_ITEMS` | 1 | One package-scoped instance per activated package; derives the intra-package graph, dispatches Agent 2 work across deliverables, validates fan-in, and returns package closure evidence. |
| `TASK` | 2 | Executes one sealed implementation, assessment, docs, or evidence sub-scope with explicit read/write bounds. |
| `CHANGE` | 1 | Performs final Git/file-state closeout for validated tranches: scoped status review, staging, commit, and fast-forward-safe push. |
| `RECONCILIATION` | 1 | Runs activated deliverable-corpus concordance through claim-level discovery, package waves, synthesis, decision routing, repair, and backcheck. |
| `EVALUATION` | 1 | Orchestrates generic read-only audits and cross-surface assessment outside deliverable-corpus concordance. |
| `REVIEW` | 1 | Reviews project outputs against scope, validation evidence, product boundaries, and acceptance criteria. |
| `RESEARCH` | 1 | Evidence-grounded, read-only inquiry over accepted decompositions, governance/source docs, and retrieval indexes; returns cited findings without changing project state. |
| `AUDIT_*` | 2 | Runs bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |

## Runtime capability convention

- Subagent capability assignments (owner-revised 2026-07-12: MODEL-AGNOSTIC —
  no named-model conventions; this section is the convention's home and a
  per-run steer may override; earlier named-model steers, including the
  2026-07-05 convention and loop Receipt 18, are rescinded going forward and
  survive only as historical record): use the session's available models by
  capability tier, not by name. Standard-capability agents for discovery,
  research, summaries, running deterministic checks, and breadth
  verification; highest-capability agents (at high reasoning effort where the
  harness supports it) for planning, for adversarial verification of anything
  that will be recorded as fact, and for execution that touches governed
  artifacts, fences, or rulings; reduced effort only for mechanical execution
  of fully specified changes. Record which model actually ran each dispatched
  role in the governed AgentRuns record and point to it from the receipt;
  when no AgentRuns record exists, the receipt may carry the minimum model
  attribution directly. Never silently substitute mid-wave — a capability-
  tier change within a wave is a receipt-worthy event.

## Project-Wide Execution Discipline

Use a recorded work graph for every multi-agent tranche. The human may
prescribe the graph or delegate selection to HELP_HUMAN or a directly invoked
WORKING_ITEMS instance. Terminal fan-out/fan-in is appropriate for independent
children; supervised many-to-many agency is appropriate when active findings
may affect siblings. Mixed sequential/concurrent stages are allowed.

HELP_HUMAN owns cross-package dependencies and shared-surface ownership. Each
WORKING_ITEMS instance owns exactly one package and coordinates its
deliverable-scoped Agent 2 children. Shared reads are allowed. Concurrent
writes must be disjoint; overlapping writes are serialized against an
accepted predecessor or assigned to one integration owner. Agent 1 and Agent 2
siblings do not message or delegate directly; coordination flows through the
parent and preserves claim status and evidence.

Software package activations use `software-workflow.json` under the root
`../../docs/SOFTWARE_WORKFLOW_PROFILE.md` contract. WORKING_ITEMS selects the
appropriate `software-*` TASK skill and registered checks; the profile does not
expand project authority or replace the validation and owner gates below.

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
the package `WORKING_ITEMS` instance returns a closeout handoff to HELP_HUMAN
or the human, which invokes `CHANGE` as a separate Agent 1 for final
Git/file-state review. `CHANGE` should commit and push the validated
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
