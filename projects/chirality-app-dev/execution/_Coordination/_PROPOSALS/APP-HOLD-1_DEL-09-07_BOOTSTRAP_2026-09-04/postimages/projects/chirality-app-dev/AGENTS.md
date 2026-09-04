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

## Execution attribution

- Capability and model direction is supplied per-session by the owner's
  steering (D-GOV-17 M1-D, ruled 2026-07-18,
  `../../docs/governance_harness/_DECISIONS/D-GOV-17_model_capability_doctrine.md`):
  no durable surface in this project prescribes canonical models or model
  capability types. The owner-revised 2026-07-12 capability-tier convention
  formerly in this section is rescinded going forward and survives as
  historical record (verbatim in D-APP-61 Appendix Q2 and Git history),
  alongside the earlier named-model steers it had itself rescinded.
- Two model-agnostic evidence rules survive under the same ruling: record
  which model actually ran each dispatched role in the governed AgentRuns
  record and point to it from the receipt (when no AgentRuns record exists,
  the receipt may carry the minimum model attribution directly); and record
  any mid-wave substitution where the wave's execution is recorded — never
  substitute silently.

## Project-Wide Execution Discipline

Use a recorded work graph for every multi-agent tranche. The human may
prescribe the graph or delegate selection to HELP_HUMAN or a directly invoked
WORKING_ITEMS instance. Terminal fan-out/fan-in is appropriate for independent
children; supervised many-to-many agency is appropriate when active findings
may affect siblings. Mixed sequential/concurrent stages are allowed.

**Delegation posture (work-type conditioned).** "Every multi-agent tranche"
does not mean every tranche is multi-agent. The package `WORKING_ITEMS`
instance sizes delegation to the target:

- *Independent-review path (default for product source).* Any tranche that
  changes product source — `frontend/src/**` outside `__tests__/**`,
  `frontend/electron/**`, `frontend/packages/**`, `frontend/scripts/**`, or
  build/packaging configuration — dispatches at least one **fresh, read-only**
  `TASK + software-code-review` child over 100% of the frozen diff before the
  registered checks are treated as final and before push. The reviewer has no
  write target and is not the implementer's context. A `PASS` with no
  actionable finding is required to publish; findings are remediated and
  re-reviewed. Registered checks (typecheck, Vitest, build/premerge, D-APP-36
  render bar) remain the deterministic gates; review is additional, not a
  substitute.
- *Single-manager path (permitted).* Tranches confined to one deliverable that
  change only automated tests, evidence, `_run_records`, deliverable state,
  coordination, docs, or governance/control-plane surfaces — no product source
  — may be executed directly by the `WORKING_ITEMS` instance under the
  registered checks and APP-HOLD-1 preflight; the receipt plus deliverable-local
  state are the record and no AgentRuns package is owed. The manager may still
  choose the review path when a tests-only tranche asserts a product invariant
  for the first time or its correctness is not self-evident from the checks.
- *Multi-agent path (record contract).* Whenever children are dispatched, the
  tranche uses the recorded work graph and freezes, under
  `execution/_Coordination/AgentRuns/<RUN_ID>/`: activation or plan, work graph,
  one sealed launch brief per child, each child's return and status, the manager
  return, and a handoff state — the existing App convention, unchanged.
  Registered-check JSON, runtime events, and summaries are written once per run,
  not per child, unless a child's own return contract requires them.

Cross-package verification ownership named in a deliverable's `Remaining` (for
example DEL-09-03 for test-expansion claims) is honoured on either path by the
existing notice route; it does not by itself require the multi-agent path.

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

Host-capability execution. Some registered checks and evidence surfaces cannot run inside the session's sandbox because the sandbox denies process spawning, Mach bootstrap, network, or keychain access — packaged Electron launches, browser-driven proofs, LaunchAgent drills, and keychain-backed probes are the standing examples. For such a surface, the executing agent requests sandbox escalation for the exact command and runs it itself in the session; the human approves or declines per command. A sandbox denial is not an environment class to record and move past, and it is not a reason to park, hand off, waive, or infer a pass. Park with HOST_RERUN_REQUIRED only when the escalation request itself is declined, and record the exact command that was declined. Escalated runs are recorded once per run in the run record with the command, the reason escalation was required, and the result. A failure whose cause is a missing local profile or binding (for example the registered premerge's absent runtime-daemon bindings) is a different class: record it as such and defer to PR CI as today. Root harness CI is additional evidence where it exists; it does not replace a required host surface unless the owning decision says so.

There may be other agents working in this monorepo with disjoint write scopes.
Treat unrelated dirty files outside the selected tranche scope as external
state. Do not fix, stage, revert, or interpret them unless the human directs
that work.

## APP-HOLD-1 Reliance Preflight

Before relying on, dispatching, promoting to `CHECKING`, or consuming an
accepted dependency for any App deliverable, every session, agent, and
workflow must run:

`python3 execution/_Scripts/app_hold.py check --operation <operation> --entry-path <declared-entry-path> --target <DEL-ID> [--target <DEL-ID> ...]`

from the App working root. `operation` is exactly one of `reliance`,
`dispatch`, `checking-promotion`, or `accepted-dependency-consumption`.
The execution-time scan and `execution/_Coordination/APP_HOLD_REGISTER.csv`
must agree. Register rows distinguish `HOLD` from `STRUCTURAL_BOOTSTRAP`; a
held target always fails closed and no structural-bootstrap row can override a
hold. APP-HOLD-1 has no generic runtime exception input and does not infer
exceptions from owner prose.

D-APP-104 adds one mechanically bounded structural admission for the
not-yet-contracted `DEL-09-07`. It applies only to `operation=dispatch`, only
to package `PKG-09`, and only to these two stable entry-path tokens:

- `SCA-APP-009:GATE5:PREPARATION:CANDIDATE_MIRROR`
- `SCA-APP-009:GATE5:PREPARATION:ACTUAL_WORKTREE`

The guard returns `admission_kind=STRUCTURAL_BOOTSTRAP` only while the live
decomposition and companion-register SHA-256 values equal the exact approved
SCA-APP-009 postimages, `_ScopeChange/_LATEST.md` still equals its exact old
preimage, `ScopeOfWork.md` is absent, and the exact DEL-09-07 folder is absent
or contains only regular, non-symlink instances of the five authorized
PREPARATION files. Pointer movement, contract appearance, authority drift, an
unexpected or nested path, or a symlink expires the admission automatically.
The row authorizes no PREPARATION act, scope amendment, repin, audit waiver,
or sixth Scope of Work; it only allows the separately owner-authorized
preflight for those two dispatch contexts. Row retirement after expiry is a
separate maintenance act. Any other override still requires a separately
accepted and applied App-loop amendment to the live register, tool, and
instruction surfaces before the prohibited act begins.

The prohibition binds held contracts regardless of entry path. WORKING_ITEMS
preflight is the primary enforcement mechanism, not the source or limit of
the prohibition. Direct entry, resumed sessions, API paths, other agents, and
other workflows remain bound. A fan-in that observes work or dependency use
without a passing preflight must reject the return and keep dependants held.

APP-HOLD-1 never authorizes repinning. A register/scan mismatch, malformed
contract basis, malformed admission row, missing preflight, held target, or
failed structural-admission condition is blocking and returns to the human
through the active manager.

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

Branch creation is routine. Creating the tranche's task branch (and, when
isolation is warranted, its worktree lane) from a verified clean basis on the
integration branch — clean status, no in-progress Git operation, base SHA
recorded — is an ordinary Step 0/Step 4 act and requires no `APPROVE:` token,
whether performed by the loop session or by a dispatched CHANGE instance.
CHANGE reports the branch name and base SHA and proceeds. Basing a lane on a
dirty worktree, or any switch that would discard or carry uncommitted work,
remains non-routine under root `AGENT_CHANGE.md`. Owner direction 2026-07-19
(recorded in App `loop/LOOP_RECEIPTS.md` Receipt-74), applied to this loop by
owner direction 2026-08-15; scoped commit/push closeout follows the checklist
above and likewise needs no per-run `APPROVE:` token.

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

## Shared Runtime Boundary

D-GOV-20 and D-APP-73 authorize migration of the executable harness into the
root-owned `runtime/` workspace. After migration, the per-user runtime daemon
is the sole owner of engines, credentials, sessions, delegation, tools, turn
locks, interruption, and model residency. The normal Desktop process, CLI,
and app-dev HTTP routes are clients of that daemon and must not construct an
independent runtime.

Daemon user-data state is operational and non-authoritative. This checkout
retains authority for project identity, instructions, execution records,
AgentRuns, permissions, approvals, and acceptance evidence. The tracked
`chirality.project.json` manifest contains no secret or machine-specific
absolute path; authority-affecting changes require explicit re-registration.

Agent roles remain authority contracts independent of engines and models.
Every governed run records the actual engine, provider, and model, including
substitutions, without establishing a durable model-to-role preference.
