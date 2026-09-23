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
- Preserve actual model attribution and substitutions in the available
  execution record. Where host records do not retain the required facts,
  keep a compact execution note linked from the graph. The undertaking receipt
  points to those facts; do not create a second receipt solely for attribution.
  This changes record placement, not the duty of truthful attribution.

## Project-Wide Execution Discipline

The recurrent discovery, planning, delegation, checking and integration procedure
lives in `loop/LOOP_INIT.md`. The thin `init/dev-loop-init-prompt.md` launcher
selects it. Its current-graph pointer locates the undertaking; work state and
recovery facts belong in that graph. Priorities and phase transitions come from
owner steering. Do not copy node state or next actions into these instructions.

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
includes instruction and owner-direction changes. Scale review to what the
change can break and backcheck affected corrections and their consequences;
later candidate changes need review coverage. A read-only assignment is not
itself a mergeable slice. For
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

## Deliverable records and loop ownership

`loop/LOOP_INIT.md` owns the recurring development procedure. Its named
workflows provide bounded methods; other historical plans and coordination
records do not supply alternate loop mechanics. The development init prompt
supplies the current human steering, including phase changes.

`ScopeOfWork.md` carries the deliverable's production commitments. `MEMORY.md`
indexes what each run did in this deliverable, with pointers to its PR, evidence
and central decisions or transfers. Decision authority stays at its owning
source; memory carries no future assignments. The local graph
carries execution at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`.
Keep it Git-tracked in the undertaking's PR sequence and set LOOP_INIT's current
pointer to its actual path. Preserve historical graph files. `_STATUS.md` retains
lifecycle and history. The App's former `Remaining` sections were retired through
the finite Task Management account at
`execution/_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/`.
Their absence does not prove completion or prevent work within the human's
authorized undertaking. Select current work from the steering, governing Scope
of Work, accepted decisions, dependencies and identified work graph; the
historical census and account are migration evidence, not a work list.

Each substantive PR includes the documentary, reconciliation and conditional
Task Management consequences needed for that slice. Perform one final bounded
documentation/governance closeout after the undertaking's
intended implementation and evidence integration (normally the penultimate
merge), before the final PR. Record one central loop receipt and terse MEMORY
run rows near final PR preparation under LOOP_INIT. The final PR description
uses the receipt's result/checks/limits account; MEMORY links the receipt.
Detailed evidence and decisions stay at their sources. Required execution
provenance stays recoverable. The loop ends when its completed graph's final PR
merges after required checks, review and human decisions. In-flight method bases retain their
own authority until explicitly transitioned.

## Development boundaries

- **F-APP-1 (provider/network):** Codex remains the sole current MVP engine.
  Apply the current Runtime-owned network, tool and credential contracts as
  amended by D-GOV-43/A2 and D-APP-127. Retired hosted admission, per-root
  consent and supplier containment are not current proof prerequisites. Codex
  owns login/logout and its credentials in the App's effective Codex home;
  the App must not read, copy or relay those credentials or affect other
  clients' credentials. This development loop grants no provider expansion, remote MCP,
  plugin or broad tool-search enablement beyond separately accepted scope.
- **F-APP-2 (release/distribution):** no signing, notarization, publication,
  external distribution, or release-readiness / professional / certification
  claims.
- **F-APP-3 (domain-engine boundary):** domain-engine work happens only
  inside what the tier-0 bridge loop's ruled decisions grant (the `D-APP-4x`
  F-series rows); this development loop never writes `_DomainEngines/**` or piping
  surfaces, and never advances integration level, live binding, or
  apply-class tool exposure on its own authority.
- **F-APP-4 (issuance):** no `CHECKING -> ISSUED` lifecycle issuance.
- **F-APP-5 (truth and planning surfaces):** authoritative deliverable scope,
  lifecycle and dependencies remain in their governed sources; owner decisions
  remain in the decision register and applicable owner-direction records.
  The session work graph is the executable plan, not a replacement for those
  sources. It neither issues deliverables nor silently changes the phase DAG.
  Historical plans remain readable; do not select new work from them.
- **Fresh-ruling stops** (carried from the pre-consolidation coordination
  record): provider execution outside the current Codex MVP direction and
  its current accepted Runtime/network/credential scope; write/edit/bash/
  tool-execution exposure beyond the current approved item; changes to the
  project-truth model for sessions, transcripts, chats, runtime logs, or
  completion logs; professional-boundary or release-readiness posture.

Changing a fence requires owner authority. This development loop grants no new release
act; later specific owner rulings retain their effects and historical releases
are not undone by F-APP-2. Do not infer another release from a prior one.


## Development checks and evidence

Use `software-workflow.json` and `docs/VALIDATION_STRATEGY.md`,
`docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` for the work.
Before push, every tranche needs a passing repo-wide practitioner-harness
self-check and practitioner-harness pytest at closeout. Product source also
needs typecheck, vitest, build/premerge gates and the independent review path
above; run product checks on a clean candidate. Stop the dev server before
build/package/premerge commands. UI work additionally follows the D-APP-36
render bar in `docs/ISSUE_READINESS_PROFILES.md` §4 and the evidence rules in
`docs/ui/UI_POLISH_EXECUTION_PLAN.md`. Authority-corpus edits require D-APP-38
reconciliation via `execution/_Reconciliation/References/reconcile_authority_corpus.py`.
Record why frontend gates are inapplicable to a records-only change. Cosmetic
whitespace is not a merge gate. CI and review must cover the merging candidate;
rerun checks invalidated by later edits under D-APP-127.

Exercise affected user journeys as they become operable, alongside code tests.
Use native application evidence for native-host behavior; browser evidence alone
does not establish it. Include relevant interruption, recovery, keyboard and
window-size behavior. Record expected and observed outcomes, candidate and
limitations; repair defects and repeat affected checks. These checks do not
establish owner or usability acceptance. An unavailable required witness remains
outstanding, as described in the host-capability rule above.

For empirical, fixture, conformance and gate-evidence claims (A12; Root R17 N3),
retain enough non-secret bytes to independently recompute the claim: identified
inputs and candidate; fixture, evaluator and validator bytes; commands, arguments,
working directory, effective environment, versions and exit status; canonical
stdout/stderr and machine-readable results; sorted manifests with independent
hash recomputation; and a bounded rerun method. Preserve secrets neither in
commands nor outputs. If required evidence is unavailable, withhold the claim.
Retain one canonical copy and reference it from the graph or deliverable.

Historical citations to the LOOP_INIT evidence contract (including former
sections 7 and 9) now resolve to the evidence contract above; dated verdicts
retain their original basis. Historical section 8 check citations resolve to
this section and its owning check documents.

## Selection and decisions

For work selection, use the human's steering, accepted scope, dependencies,
deliverable memory and actual source/evidence under LOOP_INIT. Verify the
selected work's required inputs at the point of consumption from the dependency
records and their owning contracts. Preserve
named gates and APP-HOLD-1. INTERFACE/HANDOVER/CONSTRAINT/ENABLES do not become
blanket whole-deliverable blockers; their actual obligations still apply.
Apply K-ENGINE-6: standalone-harness or feature-parity work remains off-strategy.

D-APP-64 §5, refining D-APP-60, governs judgment-shaped forks. Prepare a proposal
for material or hard-to-reverse choices and acts reserved to the owner; decide
ordinary choices within authority. Disclose implementation departures, their
rationale and reversal method. An explicit ruling, adopted requirement or
protected criterion needs its owning decision before reversal. Owner suggestions
and agent recommendations are not rulings. Preserve material owner directions
faithfully in the graph or a linked decision record; distinguish transcription
from a governed ruling. In-session directions do not pretend a required merge
has occurred.

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
in the work graph or its linked evidence. A dirty checkout is not permission to
carry unrelated changes into a new branch.

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
