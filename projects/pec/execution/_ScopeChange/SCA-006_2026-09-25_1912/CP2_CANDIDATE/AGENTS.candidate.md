---
doc_id: PEC-AGENTS
doc_kind: governance.agent_index
status: live
created: 2026-07-04
amended: 2026-09-25 (SCA-006 operational-reliance instruction tranche; earlier, shared development-loop adoption under D-PEC-94)
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

## Product Posture

PEC is the Chirality **coordination plane**: a deterministic, rebuildable
projection of governed file truth plus an ephemeral presence layer, embodying
loop Step 0 and the deterministic parts of Step 1. `docs/PRD.md` v2.4 is the
product definition of record (v2.0 adopted by `D-PEC-58`; directed-bootstrap
clarification adopted by `D-PEC-61`; exact PEC-K-03/-11 rows adopted by
`D-PEC-67`; surrounding concordance adopted by `D-PEC-68`; the v2.3 successor
adopted through SCA-005 checkpoint group 2 under `D-PEC-92`; the v2.4
successor, carrying the `D-PEC-90` operational-reliance direction, adopted
through SCA-006 checkpoint group 2).
Implementation so far consists of owner-ruled `v2/**` source slices
(`D-PEC-74`, `D-PEC-75`, `D-PEC-77`, `D-PEC-84`, `D-PEC-85`, `D-PEC-87`,
`D-PEC-89`, `D-PEC-91`); no consumer surface exists yet, and nothing in the
PRD is an implementation mandate.

Binding on every agent, now and in every future tranche:

- **Graceful absence (PEC-K-01).** No governed act may require a PEC read or
  write. The kill test is a standing release gate; any design an agent
  proposes must survive PEC being deleted.
- **Files govern (PEC-K-02).** PEC output is never citable as authority.
  Rulings and lifecycle state remain file-native (K-AUTH-1). A PEC value,
  view, or verdict is labeled non-authoritative data in that authority sense.
  Operational reliance on it (acting on a record-tier claim as true as of its
  examined-through SHA, within the pin, coverage and tier the response
  declares, with file fallback; PEC-K-03, `D-PEC-90`) applies only to a PEC
  release whose PRD §12 reliance-advertisement gate has passed. Until then,
  read the files directly. Operational reliance is distinct from the
  reliance-hold control (§Active Reliance Holds) and from professional
  reliance.
- **Observation, not participation (PEC-K-06).** PEC dispatches nothing and
  arbitrates nothing; no leases, no merge opinions. Conflicts are surfaced,
  never prevented; gate verdicts are advisory and Explain-shaped.
- **Consumer-owned use (PEC-K-03/-11).** PEC is pull-oriented, mode-capable,
  and never forced. An explicitly enabled consumer, whether a harness or an
  agent querying through tool calls under the read-only `agent` access class,
  owns whether and when it consumes and whether it injects labeled PEC data;
  no external cadence or receiving-loop duty is inferred (`D-PEC-67`,
  `D-PEC-68`, `D-PEC-90`). Injected or queried PEC data carries its reliance
  envelope (PEC-ORI-007).
- PEC is not a system of record, not a ruling surface, not an orchestrator,
  not a lock manager, not a Git actor, not a replacement for the practitioner
  harness, and not a human project-management tool (PRD v2 §4.2, permanent
  non-goals).

## Frozen Reference Corpus

`core/`, `server/`, `web/`, `agent-sidecar/`, `tools/`, `fixtures/`, and the
workspace manifests (`package.json`, `package-lock.json`, `tsconfig.base.json`)
are a **frozen reference corpus** (`D-PEC-58` behavior 6 and its 2026-07-24
fence-amendment paragraph, which names the manifests; PRD v2 §13):

- Read and cite only. No edits, no feature work, no dependency changes.
- Never run the server or any mutating CLI against a non-scratch database.
- Machinery carries into v2 **as cited patterns, never as code** (PRD v2
  §7.3/§13); a brief quarries it by citation, naming the reference module.
- Nothing is deleted; working-tree archival is a future packet (after Phase 2).
- Retired product docs live under `docs/.archive/` (SPEC, TRACEABILITY, PILOT,
  ADRs, PRD v1.0, prototype README/STATUS), indexed by
  `docs/.archive/README.md` — citable as historical basis, never updated,
  their internal notices accepted as permanently stale.
- `F-PEC-2` still binds: no invention or file-level mutation of any PEC record
  state in that corpus.

## Agent Posture

| Row | Purpose in PEC |
|---|---|
| Normative | Define runtime contracts, product boundaries, data-residency posture, validation policy, and agent workflow constraints. |
| Operative | Execute bounded PEC tranches, decomposition support, evidence updates, and coordination updates. |
| Evaluative | Review, reconcile, audit, and decide whether outputs are acceptable for the next stage. |

### Session model convention

- Subagent model assignments (owner-revised 2026-07-05; this section is the
  convention's home — a per-run steer may override): `opus` agents for
  discovery, research, summaries, running deterministic checks, and breadth
  verification; `fable` agents at `high` reasoning effort for planning, for
  adversarial verification of anything that will be recorded as fact, and for
  execution that touches governed artifacts, fences, or rulings; `fable` at
  `low` effort only for mechanical execution of fully specified changes.

Runtime hierarchy and delegation are governed by root `AGENTS.md` and the
active canonical agent instructions. Record actual model identity only when
the runtime exposes it; the convention is not evidence of the model used.

## Primary Agents

The v2 build runs through the governed pipeline (PRD v2 §12). The recurring
development procedure is `loop/LOOP_INIT.md`, entered through
`init/dev-loop-init-prompt.md`; see "Deliverable records and loop ownership"
below. Retired plans are history only.

| Role and method | Type | Role in this project |
|---|---:|---|
| `WORKING_ITEMS` with `software-decomp` (formerly `SOFTWARE_DECOMP`) | 1 | Ran the decomposition over PRD v2, Gates 1–7 per `{REPO_ROOT}/docs/DECOMPOSITION_STANDARD.md` (session and acceptance state: `D-PEC-60` and `execution/_Decomposition/_LATEST.md` — this table asserts no gate state). The accepted package at `execution/_Decomposition/` is the authoritative downstream basis; no tranche is scoped from the PRD directly; post-acceptance amendment goes through the scope-change machinery, not direct edits. |
| `WORKING_ITEMS` with `project-setup` (formerly `PROJECT_SETUP`) | 1 | Scaffolds packages/deliverables from the accepted decomposition, after acceptance and under its own packet. |
| `WORKING_ITEMS` | 1 | Per-package activations and their work graph, using the `software-repository-reconnaissance` and `software-test-planning` workflows and the `software-code-review` and `software-defect-diagnosis` skills, with implementation commissioned as a bounded TASK assignment under the implementation-node requirements of `construct-local-work-graph` (catalog: `{REPO_ROOT}/workflows/index.json`), conforming to `{REPO_ROOT}/docs/SOFTWARE_WORKFLOW_PROFILE.md`; integrates results, validates, and prepares closeout. |
| `TASK` | 2 | Executes one sealed implementation, assessment, docs, or evidence sub-scope with explicit read/write bounds. |
| `WORKING_ITEMS` with the project `chirality-change` skill (formerly `CHANGE`, whose legacy mapping is the `change` workflow) | 1 | Performs scoped Git/file-state closeout for validated tranches. The agent performing it owns Git state; PEC never will. |
| `WORKING_ITEMS` with `review` (formerly `REVIEW`) | 1 | Reviews outputs against scope, validation evidence, product invariants, and acceptance criteria. |
| `WORKING_ITEMS` with `reconciliation` (formerly `RECONCILIATION`) | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
| `WORKING_ITEMS` with `research-orchestration` (formerly `RESEARCH`) | 1 | Read-only inquiry over accepted docs, the frozen corpus, and retrieval indexes; returns cited findings without changing state. |
| `TASK` with an `audit-*` workflow (formerly `AUDIT_*`) | 2 | Bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |

The roles are Root's four (`{REPO_ROOT}/agents/registry.json`). The former
agent names map to these role and method pairs in
`{REPO_ROOT}/workflows/index.json` (`legacy.retiredRoles`).

## Write Scopes And Fences

Default writable project-local surfaces are only `execution/_Coordination/**`,
this `AGENTS.md`, and the one-time `docs/STATUS.md` governance pointer
section (F-PEC-1). Per-tranche `docs/STATUS.md` upkeep beyond that pointer
requires an explicit packet clause (as `D-PEC-58`/`D-PEC-59` supplied for
their tranches).

**Every other write under `projects/pec` — including any new v2 source tree,
scaffolding, manifest, or configuration — requires an owner-ruled `D-PEC`
packet naming the exact paths, acts, verification, and rollback.** New source
trees are named in their own packet.

`F-PEC-1..4` (`D-T0-15`, with `F-PEC-4` as extended by `D-T0-19`) remain the
outer fences and are amended only by an explicit per-tranche packet clause.
`F-PEC-1` is the outer fence over source work until a packet opens it.

Runtime/source implementation remains parked until an exact per-tranche packet
opens the applicable PEC and Root fences; PRD adoption alone opens none. The
development loop, a work graph, a Task Management outcome or a central receipt
opens no path either. These fences were formerly repeated verbatim in
`loop/LOOP_INIT.md` §3; this section is now their single loop-facing home.

## Shared Runtime Boundary

Amended under `D-GOV-43` (topology A2, supplement recorded 2026-09-12), which
supersedes `D-GOV-20` items 2–4 on the App MVP Codex path without editing
them. There is no per-user runtime daemon on that path: the App starts, owns
and stops one Runtime service child, which is the exclusive owner of the stock
`codex app-server` child together with sessions, delegation, tools, turn locks
and interruption (Root CONTRACT K-RUNTIME-1). This file reads `D-T0-23`'s convergence on the
Root-owned shared runtime as amended by that record; that is an
interpretation, since `D-GOV-43` does not cite `D-T0-23`. Agents working on PEC in another
host use that host's actual execution and delegation, recorded as Root
`AGENTS.md` and `D-GOV-35` require. In every case PEC v2 creates **no second
execution loop** and holds no session authority.

`D-PEC-56` is **partially superseded** by `D-PEC-58` (behavior 8): its ruled
behavior 1 — retaining PEC's deterministic acts, RBAC, reporting, and domain
tools as a project adapter service — does not survive the product retirement.
Its **no-dual-loop boundary (behavior 4) and human-only-act restrictions
(behavior 7) survive unchanged**. The client seam carries as a concept,
reimplemented against v2 entities (PRD v2 §13).

Runtime and user-data state is operational and non-authoritative. PEC project
truth, run evidence, decisions, and acceptance evidence remain
checkout-contained and authoritative over any PEC store.

## Data And Residency

PEC v2 is **content-minimal** (PEC-K-10): paths, counts, SHAs, states, hashes
— never file or diff content. No agent may design, brief, or implement a
surface that captures file or diff content.

`D-T0-14` and `D-T0-20` remain historical rulings for the retired product.
D-T0-27 O-A is effective through PR #459 merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; its exact PEC v2 profile is
`ADOPTED / READ_ONLY`. Its `chirality_readable_artifacts` set is
content-minimal and repo-committed only; it declares no runtime store,
service, transport, adapter-client, mutation, proposal, external-result, or
instance-content lane and creates no invocation by itself.

## Governance Pointers

- `execution/_Coordination/_DECISIONS/_REGISTER.md` — project decision
  register (`D-PEC-57` pivot, `D-PEC-58` adoption, `D-PEC-59` follow-ons,
  `D-PEC-60` decomposition acceptance, `D-PEC-61` directed bootstrap /
  SCA-001 opening, `D-PEC-62` scaffold + local dependency registers,
  `D-PEC-64` SCA-002 objective-mapping session — revision 1.2 accepted,
  `D-PEC-67` exact consumer rows / reliance control, `D-PEC-68` PRD v2.2
  concordance, and SCA-003 consumer-interface concordance — revision
  1.3 accepted; `D-PEC-92` SCA-005 checkpoint group 2 — PRD v2.3 adopted,
  with decomposition revision 1.5 accepted at checkpoint 3; `D-PEC-94`
  shared development-loop adoption; `D-PEC-90` operational reliance on PEC
  data (R-A); SCA-006 checkpoint group 2 — PRD v2.4 adopted
  (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`))
- `execution/_Decomposition/` — the accepted decomposition working package
  (`SOFTWARE_DECOMP.md` working surface + companion registers;
  `_LATEST.md` is the revision pointer and handoff state — read it first)
- `_DomainEngines/_DECISIONS/_REGISTER.md` — tier-0 register (`D-T0-*`)
- `projects/pec/plans/workplans/` — historical archive, never selection surfaces
- `execution/_Coordination/_DECISIONS/D-PEC-80_D_RULING_OWNER_INTENT_OF_RECORD_2026-09-05.md`
  — owner-intent preservation under D-PEC-80 D; verify its disposition
- `loop/LOOP_INIT.md` — the recurring development procedure;
  `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md` — an
  undertaking's current graph; `execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md`
  — its central receipt
- `projects/pec/loop/LOOP_RECEIPTS.md` — historical loop handoff ledger,
  closed by Receipt 197 at this adoption; append nothing further
- `docs/PRD.md` — adopted product definition; `docs/STATUS.md` — current state
- `_DomainEngines/profiles/pec.yaml` — D-T0-27 O-A exact PEC v2 successor
  postimage, `ADOPTED / READ_ONLY` and effective through PR #459 merge
  `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`. The frozen v0.4 profile is
  preserved as packet preimage lineage; the old L3 import lane remains
  retired.

## Project-Wide Execution Discipline

Use bounded tranches by default. A parent agent may orchestrate parallel TASK
fan-out only when subscopes are separable, briefs are explicit, and write
scopes are disjoint.

There may be other agents working in this monorepo with disjoint write scopes.
Treat unrelated dirty files outside the selected tranche as external state. Do
not fix, stage, revert, or interpret them unless the owner directs that work.

## Deliverable records and loop ownership

Under `D-PEC-94` (owner direction of 2026-09-25, recorded by HELP_HUMAN), PEC
adopts the shared development-loop method that App and Piping run.
`loop/LOOP_INIT.md` owns the recurring development procedure. Its named
workflows provide bounded methods; other historical plans and coordination
records do not supply alternate loop mechanics. The development init prompt
supplies the current human steering, including phase changes. Keep LOOP_INIT
evergreen, with no undertaking-specific graph pointer or execution state.
Recover the selected undertaking's graph from the steering and relevant
project records.

`ScopeOfWork.md` carries the deliverable's production commitments. `MEMORY.md`
indexes what each run did in this deliverable, with pointers to its PR, evidence
and central decisions or transfers. Decision authority stays at its owning
source; memory carries no future assignments. The local graph
carries execution at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`.
Keep it Git-tracked in the undertaking's PR sequence and return its path for
continuation. Preserve historical graph files. `_STATUS.md` retains
lifecycle and history.

PEC's deliverable `_STATUS.md` `## Remaining` sections stay in place as
deliverable-local records of open scope under their owning decisions (for
example `D-PEC-83`). They are no longer a work-selection surface: steering
selects the undertaking and its graph accounts for the Remaining items it
touches. A Remaining item's own gate markers still bind that item. When an
undertaking completes or changes an item, update it under the packet that
opens that `_STATUS.md`; without that grant, record the consequence in the
graph and bring it to the owner. Record new open scope in the graph and its
governing records rather than as a new Remaining entry. Retiring the sections,
as App and Piping did, is a separate owner-directed undertaking.

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

PEC's fences still apply to these records. The graph and central receipt sit
under the default-writable `execution/_Coordination/**`. A deliverable's
`MEMORY.md`, `_STATUS.md` or other file is outside the default surfaces, so a
MEMORY row needs the path grant of the undertaking's governing `D-PEC` packet
like any other write there. Name the affected `MEMORY.md` paths in that
packet. Where no packet opens a deliverable, record the run in the graph and
central receipt and bring the missing grant to the owner. The graph completes
only after that grant is given and the row written, or after the owner
decides to complete without the row; record that decision in the graph.

Preserve owner directions faithfully. A chat-only direction without another
governed home is quoted verbatim, with its date, in the graph or a linked
record under `execution/_Coordination/**`, labelled as evidence rather than
a ruling; the ruling itself stays file-native (K-AUTH-1) in the decision
register and its packets. Rely on an owner act, ruling, routed notice or
reliance-hold release only once its record is observable on `origin/main`
after `git fetch`, never on an unmerged branch's claim of it.

`D-PEC-88` item 6 leaves to this migration whether its standing
`docs/STATUS.md` and `README.md` maintenance carries into the migrated loop;
`D-PEC-94` records that disposition. While `D-PEC-88` applies, its trace
clause (item 4) is met by naming each `docs/STATUS.md` and `README.md` change
in the undertaking's work graph, carrying it into that undertaking's central
receipt at closeout, and reviewing it with the PR that carries it.

`loop/LOOP_RECEIPTS.md` is a historical ledger, closed by Receipt 197 at this
adoption. Append nothing further; handoff records go to the undertaking's
graph and central receipt. `tools/validation/validate_pec_loop_receipts.py`
still protects the existing records; that validation requires no new entries.
App and Piping stopped their ledgers without a closing receipt. PEC closes its
ledger with one because its former procedure required a receipt at every
closeout. The ledger header's rule that it is "the one place chat-only
directions become durable" is superseded by the owner-direction rule above;
its header text stays unedited.

`D-PEC-80` is not edited. This adoption reads it as follows. Item A stands: the
loop home `projects/pec/loop/`, the Task Management home and the AgentRuns
home stay where it put them. Item B's generic instruction surface is replaced
by the evergreen LOOP_INIT; its fence text, checks, evidence contract and
historical mapping move into this file. Item C's per-iteration commit and
receipt with one PR at terminus is replaced by the graph's PR sequence and one
central receipt. Item D's workplan retirement and owner-intent record stand:
retired plans stay in `plans/workplans/`, and a `WORKPLAN_*.md` appearing in
`loop/` is a defect, never loaded or selected. The former Step 0 command that
mechanically checked for such a plan is retired with the old procedure; the
rule itself stands. Item D's selection only from
deliverable `## Remaining` surfaces is replaced by steering-selected
undertakings and work graphs. The per-loop receipt ledger is
replaced as described above. The owner-intent record at
`execution/_Coordination/_DECISIONS/D-PEC-80_D_RULING_OWNER_INTENT_OF_RECORD_2026-09-05.md`
remains orientation for the loop's standing purpose, never a selection surface.

## Selection and decisions

For work within an undertaking, use the human's steering, accepted scope,
dependencies, deliverable memory and actual source/evidence under LOOP_INIT.
A dependency-register row blocks work only when it is `ACTIVE`, of type
`PREREQUISITE`, its `SatisfactionStatus` is `TBD`, `PENDING` or `IN_PROGRESS`,
and the work needs its target. `INTERFACE`, `HANDOVER`, `CONSTRAINT` and
`ENABLES` rows order work and never block; `SATISFIED`, `WAIVED` and
`NOT_APPLICABLE` never block. Separately, a matching `ACTIVE` reliance-hold
row blocks its prohibited act under the preflight below.

Recompute any hash a selected item or packet pins and stop on mismatch; a
historical preimage hash identifies history, not current bytes. A tracking
row is not its ruling source; read the packet and later owner records behind
it. Open legacy rows do not revive retired work. Material forks, source
openings, scope amendments, profile changes and owner-shaped decisions go to
the PEC decision register; ordinary method choices inside an existing grant
are attributed to the agent. Record every gate outcome and its reason,
including no-ops, in the graph. Never record a ruling that did not occur;
role assertion is not mechanical enforcement.

## Issue-Plan Rule

The undertaking's work graph records new actionable issues and deferrals that
would improve PEC's development loop, project governance, agents, or skills.
A material concern without a current or identified successor home goes to
bounded Task Management intake under LOOP_INIT Step 4. A second mandatory
issue plan or session workplan is unnecessary. Existing plans under
`execution/_Coordination/` keep their historical citations.

## Closeout And Git Discipline

When a tranche is complete and validated, use the project and root closeout
rules: inspect root git status, confirm validation evidence, stage only the
selected tranche scope, avoid unrelated dirty files, and commit/push only when
the branch can fast-forward safely. Branch, commit, push, PR and merge use
Root's standing Git authorization (Root `AGENTS.md`; `docs/PRD_ROOT.md`
§5.3.1) once required CI and independent review cover the actual candidate
with no blocking findings. Explicit holds and later owner directions prevail.

Git closeout is source-control hygiene. It is not lifecycle issuance, release
readiness, professional approval, certification, sealing, authentication, or
code-compliance acceptance.

## Active Reliance Holds

Before any PEC dispatch, production reliance, promotion, fan-in, review, or
consumption, run the PEC reliance-hold preflight against
`execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`. A matching `ACTIVE` row
blocks the prohibited act regardless of entry path. Read-only historical
inspection and exact correction preparation remain allowed only as the row
states. No runtime exception exists; override or release requires a later,
separately accepted PEC-loop amendment.

The deterministic preflight is
`execution/_Scripts/pec_reliance_hold.py`. WORKING_ITEMS must run it before
dispatch and fan-in. REVIEW and any other entry path must run the same check
before reliance or promotion. A missing, malformed, or unreadable register
fails closed.

Run the preflight from `projects/pec`, replacing the example target and
operation with the exact intended act (target paths are project-relative):

```bash
python3 execution/_Scripts/pec_reliance_hold.py \
  --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv \
  --target execution/PKG-XX_Name/1_Working/DEL-XX-YY_Name/ScopeOfWork.md \
  --operation candidate-validation
```

Operations are `historical-read-only-inspection`, `exact-correction-preparation`,
`candidate-validation`, `dispatch-for-production`, `rely-for-production`,
`consume`, and `promote`. Use the matching operation; candidate validation is
not a bypass for production. Re-verify any release against `origin/main`.
Checks constrain PEC work; they do not impose duties on a sister project.

## Development checks and evidence

Cosmetic whitespace is not a commit or merge gate; local formatting
diagnostics are optional. Every mergeable slice, including instruction and
owner-direction changes, receives fresh-context independent review of its
complete candidate diff by a reviewer who did not author it; repair
actionable findings and backcheck them. Never weaken a protected check,
tolerance or limit to obtain a pass.

| Work type | Required checks |
|---|---|
| Every PR | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check`; `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` (protects the closed ledger; requires no new entry) |
| Decomposition or dependency-register changes | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` |
| Task Management changes | `python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv` and the same command with `REGISTER_CLOSED.csv`; federation/row dispositions follow its owning role |
| Launcher/init/posture changes | `python3 tools/validation/validate_instruction_entrypoints.py .`; `python3 -m pytest -q tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py` |
| Tool changes | Focused tests for each changed tool plus practitioner-harness pytest when its code changes; record command, interpreter, and result |
| PEC v2 source/configuration | Exact packet's registered checks in `projects/pec/software-workflow.json`; run from `projects/pec` with an explicit compatible Python (registry requires 3.10+); record the selected version |
| Product release/reconciliation work | The packet's standing kill test and practitioner-harness parity diff, with rerunnable evidence; a release that advertises operational reliance also passes the PRD §12 reliance-advertisement gate (parity clean or explained, coverage statements under seeded feed failures, the reliance envelope, parser fixture suites, the kill test); absent implementations are unmet gates, never fabricated passes |
| Governance/control only | Record source-only, kill, and parity checks as not applicable when no corresponding capability changed; legacy source/demo/typecheck/build/drill checks do not authorize running the frozen product |
| Any dispatch, review, fan-in, promotion, or reliance | PEC hold preflight above for each exact target/act, plus the owning role's checks |

Evidence: follow the selected role and `docs/SOFTWARE_WORKFLOW_PROFILE.md`.
Preserve source identities, commands/cwd/interpreter, exit codes, outputs, and
a bounded rerun method for verification claims. Cite accepted upstream
snapshots; distinguish candidate artifacts, historical records, derivative
packages, and owner acts. Keep detail in the owning packet or run record and
link it from the graph and central receipt; never convert a passing check into
authority or professional reliance.

Historical references: citations of former `loop/LOOP_INIT.md` §3 (fences)
resolve to "Write Scopes And Fences" above; former §8 (checks, preflight) and
§9 (evidence contract) resolve to this section and "Active Reliance Holds";
former §§1–2 and 4–7 (bootstrap, pointers, Remaining selection, Steps 0–5,
first return, posture) are replaced by the current `loop/LOOP_INIT.md` and
survive in Git history; former §10's per-run steer is now the init steering,
and its historical mapping is this paragraph. Historical receipts refer to the old
`_DomainEngines/pec/` paths and to section numbers of the revision then in
force: in the init that predates `D-PEC-80`, §7 was the model convention now
in "Session model convention" above and §5 was the default posture. The
relocation map in
`execution/_Coordination/_DECISIONS/D-PEC-80_LOOP_HOME_2026-09-05/RELOCATION_MAP.csv`
and its `D_RETIREMENT/RELOCATION_MAP.csv` continuation, plus Git history,
resolve those references without a second live loop surface.
