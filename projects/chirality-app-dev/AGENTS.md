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

## Active Roles

New App work uses exactly four roles. Role identity is distinct from the
Agent 0/1/2 type and from the engine or model that supplies an instance.

| Role | Type | App use |
|---|---:|---|
| `HELP_HUMAN` | 0 | Default new-chat role. Maintains human alignment and continuity and coordinates the managers needed for the undertaking. |
| `HELPS_HUMANS` | 1 | Direct-entry design manager for roles, skills, workflows, tools, briefs, projects, and their governing contracts. |
| `WORKING_ITEMS` | 1 | Direct-entry implementation manager. Organizes bounded work, dispatches TASK instances, validates fan-in, and returns the undertaking as a whole. |
| `TASK` | 2 | Delegated bounded executor. Applies selected skills or workflows within its brief and returns work plus evidence; it is not a direct chat entry. |

Historical session identifiers and references to retired agents remain
readable through Runtime compatibility records. They do not add roles to the
active registry. Reusable methods such as research, review, decomposition,
change, and reconciliation are selected as skills or workflows when applicable.

## Skills, Workflows, and Context

Runtime owns the effective role and method catalog. The App consumes its typed
list, inspection, selection, context-resolution, and replay results; App code
does not maintain a second Markdown parser or infer method completion from a
loaded instruction body.

Ordinary App skill discovery follows Codex's native project, user and bundled
sources under D-GOV-43. Preserve each skill's actual origin. Skill browsing is
hidden for v3.0.0; native background skill use remains available. Read-only replay
preserves historical bytes and source-qualified identity without activating a
skill for a new turn or silently binding a same-named definition elsewhere.

Project workflows live under `.chirality/workflows/<name>/WORKFLOW.md`, user
workflows under `~/.chirality/workflows/<name>/WORKFLOW.md`, and reviewed
bundled workflows are the third source. Unqualified workflow lookup prefers
project, then user, then bundled definitions, while an actual selection retains
its source-qualified identity. Old flat project workflow Markdown files remain
ordinary documents and historical navigation targets.

The central workflows are workflow creation, project setup, project
decomposition, software decomposition, domain decomposition, research
orchestration, and scope change.
They receive immediate placement in selection UI because they are broadly
useful. Before authoring or revising a reusable workflow, agents load and follow
the core `create-workflow` method from the selected library basis. Other central
methods remain optional unless applicable instructions require them. Skills and workflows can
be combined, stopped, and replaced within one conversation. Selection does not
change a role, launch a manager, expand tools, or grant permissions.

Users create, save, and revise workflows through the active chat. An authorized
agent writes a valid canonical project or user workflow package with ordinary
file tools, validates its metadata and contained resources, and refreshes the
Runtime catalog. The App has no separate workflow editor.

New conversation context contains the App product `AGENTS.md`, native global
and project instructions, the full active-role instructions, and available skill descriptions.
Selected or needed method bodies and contained resources load through Runtime.
The recorded basis preserves each supplied item's origin and hash for replay.
Interaction mode and permission mode are independent. Native Plan Mode is
available only when Runtime reports admitted adapter evidence; plan revisions
remain in conversation history and are exported to a project file only through
an explicit user-selected save action.

The product default lives in `instructions/AGENTS.md` in this project and is
seeded into the App's user-data instructions folder. Settings opens that copy
for editing and can restore the default while retaining a backup. Runtime
supplies common guidance and the selected full role automatically to primary
chats and fresh named native children. Native user/project discovery is not
duplicated by Runtime. Edits apply at a confirmed safe boundary; running agents
and historical basis retain the content they received. These files are open
source and the distinction from repository development guidance is applicability.

## Execution attribution

Codex is the sole App MVP engine qualification and release target. Runtime
registers Codex as the only MVP engine, new chats default to it, and the UI
exposes only supported release engines. Selecting a Codex model changes model
configuration within that engine. Historical sessions, standalone compatibility
records, and retained compatibility surfaces preserve their original engine and
provider attribution without establishing qualified MVP support or substituting
for required Codex capability.

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

The recurrent discovery, planning, delegation, checking and integration procedure
lives in `loop/LOOP_INIT.md`. The thin `init/dev-loop-init-prompt.md` launcher
selects it. Current state belongs in the owning run and its work graph; priorities
and phase transitions come from owner steering. Do not copy run-specific lane
names, model assignments or next actions into these standing instructions.

Choose agent types by responsibility and delegation needs, not task complexity
or reasoning effort. Root role instructions govern delegation. No package-per-
manager roster or separate closeout agent is compulsory. HELP_HUMAN owns
cross-undertaking dependencies and shared-surface integration; each manager or
direct specialist has an explicit bounded assignment. Children return to their
parent; Type 2 instances do not delegate.

Concurrent writes must be disjoint or serialized under an identified integration
owner. Shared reads are allowed. Honour cross-package verification ownership
named in deliverable contracts through the existing notice route; it does not
by itself require another manager. Software activations use
`software-workflow.json` under `../../docs/SOFTWARE_WORKFLOW_PROFILE.md` and
its applicable checks. A profile does not expand authority or waive a gate.

Every slice requires fresh-context independent review of its complete frozen
diff before merge, with actionable findings repaired and backchecked. This
includes instruction and owner-direction changes; proportionate review and
affected-correction backchecks are described in `loop/LOOP_INIT.md`. For
product source (`frontend/src/**` outside `__tests__/**`, `frontend/electron/**`,
`frontend/packages/**`, `frontend/scripts/**`, build/packaging configuration),
retain the fresh read-only `TASK + software-code-review` path before final
registered checks and push. The reviewer did not implement the change and has
no write scope. Registered checks remain additional requirements.

Never weaken a test or move a tolerance, oracle or limit to obtain a pass.
Preserve a protected check that conflicts with the design, bring the owner the
measured conflict and recommendation, and block the affected acceptance or
merge. Check delegated changes for this failure mode. Observed test results,
agent review, Git integration and owner acceptance are distinct. Explicit holds
remain until their owning authority lifts them.

Write only inside the authorised undertaking and its required evidence and
coordination scope. Root governance, roles, skills and tools require explicit
owner direction. Preserve unrelated dirty files and parked work: do not fix,
stage or revert them as part of ordinary closeout.

Host-capability execution uses the current host's actual tools and permissions.
Use its supported approval mechanism when a required command needs additional
permission. If execution is unavailable or declined, retain the exact command,
reason and outstanding verification as `HOST_RERUN_REQUIRED`; never claim a
pass or silently waive the check. A missing build/profile binding is a distinct
failure, not a sandbox denial. CI does not replace a required native witness
unless the owning criterion permits it. D-APP-127's affected-check rule replaces
the retired A1 re-stage requirement and daemon/LaunchAgent proof subjects;
applicable production packaging and native checks remain required.

## APP-HOLD-1 Reliance Preflight

Before relying on, dispatching, promoting to `CHECKING`, or consuming an
accepted dependency for any App deliverable, every session, agent, and
workflow must run:

`python3 execution/_Scripts/app_hold.py check --operation <operation> --entry-path <declared-entry-path> --target <DEL-ID> [--target <DEL-ID> ...]`

from the App working root. `operation` is exactly one of `reliance`,
`dispatch`, `checking-promotion`, or `accepted-dependency-consumption`.
The execution-time scan and `execution/_Coordination/APP_HOLD_REGISTER.csv`
must agree. Register rows distinguish `HOLD`, `STRUCTURAL_BOOTSTRAP`, and
`SOW_INITIALIZATION`; a held target always fails closed and no admission can override a
hold. APP-HOLD-1 has no generic runtime exception input and does not infer
exceptions from owner prose.

The DEL-09-07 structural-bootstrap admission from D-APP-104 expired and was
retired by D-APP-107. D-APP-127 subsequently superseded D-APP-107 in whole and
removed its initialization admission with the retired LaunchAgent installer.
Those records and guard compatibility code remain historical evidence; they
are not active dispatch instructions. The generic APP-HOLD-1 check above
continues to govern live targets. No other override is inferred: a new
exception requires a separately accepted and applied amendment to the live
register, tool and instruction surfaces before the prohibited act.

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

Use the project-scoped `chirality-change` skill or the same checklist inline,
within existing role and write authority. Inspect Git state, validation and
review coverage; stage only the authorised diff and evidence; verify upstream
and the actual candidate before publishing. Branch creation, commit, push, PR
and merge use standing owner Git authority when its conditions hold, without
new per-run approval tokens. Explicit holds and later owner directions prevail.

Preserve other contributors' changes when integrating upstream. Re-review the
resulting candidate and repeat checks invalidated by the change. Escalate
substantive conflicts beyond existing authority; do not discard unrelated work
or force-push another contributor's branch. Record branch and basis identities
in the owning run. A dirty checkout is not permission to carry unrelated changes
into a new branch.

Git closeout is source-control hygiene. It is not lifecycle issuance, release
readiness, professional approval, certification, sealing, authentication, or
code-compliance acceptance. The loop's work graph records new actionable issues
and deferrals; a second mandatory issue plan or session workplan is unnecessary.
Preserve existing plans and their historical citations.

## Shared Runtime Boundary

Amended under D-GOV-43 (topology A2, 2026-09-12; D-APP-127). The Runtime is
an application-owned service: the App starts, owns and stops one Runtime
service child, which owns the pinned stock `codex app-server` child and the
effective Codex home. The Runtime service owns engines, sessions, delegation,
tools, turn ownership and interruption; the Desktop renderer and the app-dev
HTTP routes are clients of that service over its Unix socket with a
per-launch token and must not construct an independent runtime. There is no
per-user daemon, LaunchAgent, second socket or model residency on the App
path (D-GOV-20 and D-APP-73 are read as amended; D-APP-107's preflight is
retired).

Runtime user-data state is operational and non-authoritative. This checkout
retains authority for project identity, instructions, execution records,
AgentRuns, permissions, approvals, and acceptance evidence. The tracked
`chirality.project.json` manifest contains no secret or machine-specific
absolute path; authority-affecting changes require explicit re-registration.

Agent roles remain authority contracts independent of engines and models.
Every governed run records the actual engine, provider, and model, including
substitutions, without establishing a durable model-to-role preference.
