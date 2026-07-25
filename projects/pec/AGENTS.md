---
doc_id: PEC-AGENTS
doc_kind: governance.agent_index
status: live
created: 2026-07-04
amended: 2026-07-25 (D-PEC-64; SCA-002 closed — decomposition revision 1.2 accepted)
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
loop Step 0 and the deterministic parts of Step 1. `docs/PRD.md` v2.1 is the
product definition of record (v2.0 adopted by `D-PEC-58`; directed-bootstrap
clarification adopted by `D-PEC-61`). Implementation does not exist yet;
nothing in the PRD is an implementation mandate.

Binding on every agent, now and in every future tranche:

- **Graceful absence (PEC-K-01).** No governed act may require a PEC read or
  write. The kill test is a standing release gate; any design an agent
  proposes must survive PEC being deleted.
- **Files govern (PEC-K-02).** PEC output is never citable as authority.
  Rulings and lifecycle state remain file-native (K-AUTH-1). A PEC value,
  view, or verdict is labeled non-authoritative data, verified against its
  cited source before reliance.
- **Observation, not participation (PEC-K-06).** PEC dispatches nothing and
  arbitrates nothing; no leases, no merge opinions. Conflicts are surfaced,
  never prevented; gate verdicts are advisory and Explain-shaped.
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

## Primary Agents

The v2 build runs through the governed pipeline (PRD v2 §12; standing plan
target sequence).

| Agent | Type | Role in this project |
|---|---:|---|
| `SOFTWARE_DECOMP` | 1 | Ran the decomposition over PRD v2, Gates 1–7 per `{REPO_ROOT}/docs/DECOMPOSITION_STANDARD.md` (session and acceptance state: `D-PEC-60` and `execution/_Decomposition/_LATEST.md` — this table asserts no gate state). The accepted package at `execution/_Decomposition/` is the authoritative downstream basis; no tranche is scoped from the PRD directly; post-acceptance amendment goes through the scope-change machinery, not direct edits. |
| `PROJECT_SETUP` | 1 | Scaffolds packages/deliverables from the accepted decomposition, after acceptance and under its own packet. |
| `WORKING_ITEMS` | 1 | Per-package activations and their work graph, using the five `software-*` TASK skills (roster: root `AGENTS.md` agent index and `{REPO_ROOT}/skills/software-*`), conforming to `{REPO_ROOT}/docs/SOFTWARE_WORKFLOW_PROFILE.md`; integrates results, validates, and prepares closeout. |
| `TASK` | 2 | Executes one sealed implementation, assessment, docs, or evidence sub-scope with explicit read/write bounds. |
| `CHANGE` | 1 | Performs scoped Git/file-state closeout for validated tranches. CHANGE owns Git state; PEC never will. |
| `REVIEW` | 1 | Reviews outputs against scope, validation evidence, product invariants, and acceptance criteria. |
| `RECONCILIATION` | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
| `RESEARCH` | 1 | Read-only inquiry over accepted docs, the frozen corpus, and retrieval indexes; returns cited findings without changing state. |
| `AUDIT_*` | 2 | Bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |

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

## Shared Runtime Boundary

`D-GOV-20` and `D-T0-23` place PEC agent execution on the root-owned shared
runtime. The runtime daemon remains the **sole owner** of sessions,
delegation, turn locks, credentials, interruption, and model residency. PEC v2
creates **no second execution loop** and holds no session authority.

`D-PEC-56` is **partially superseded** by `D-PEC-58` (behavior 8): its ruled
behavior 1 — retaining PEC's deterministic acts, RBAC, reporting, and domain
tools as a project adapter service — does not survive the product retirement.
Its **no-dual-loop boundary (behavior 4) and human-only-act restrictions
(behavior 7) survive unchanged**. The client seam carries as a concept,
reimplemented against v2 entities (PRD v2 §13).

Daemon and user-data state is operational and non-authoritative. PEC project
truth, run evidence, decisions, and acceptance evidence remain
checkout-contained and authoritative over any PEC store.

## Data And Residency

PEC v2 is **content-minimal** (PEC-K-10): paths, counts, SHAs, states, hashes
— never file or diff content. No agent may design, brief, or implement a
surface that captures file or diff content.

`D-T0-14` and `D-T0-20` are unchanged as rulings; item (iii) of the D-T0-20
enumeration tracks the profile's `chirality_readable_artifacts` set,
re-pointed 2026-07-24 for the docs archive (`D-PEC-59`). Mutation basis for any real (non-scratch) database remains an
unopened future row. Agent validation stays scratch/demo-only.

## Governance Pointers

- `execution/_Coordination/_DECISIONS/_REGISTER.md` — project decision
  register (`D-PEC-57` pivot, `D-PEC-58` adoption, `D-PEC-59` follow-ons,
  `D-PEC-60` decomposition acceptance, `D-PEC-61` directed bootstrap /
  SCA-001 opening, `D-PEC-62` scaffold + local dependency registers,
  `D-PEC-64` SCA-002 objective-mapping session — revision 1.2 accepted)
- `execution/_Decomposition/` — the accepted decomposition working package
  (`SOFTWARE_DECOMP.md` working surface + companion registers;
  `_LATEST.md` is the revision pointer and handoff state — read it first)
- `_DomainEngines/_DECISIONS/_REGISTER.md` — tier-0 register (`D-T0-*`)
- `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` — the
  standing plan (loop protocol, target sequence, parked work, fences)
- `_DomainEngines/pec/LOOP_RECEIPTS.md` — loop handoff ledger
- `docs/PRD.md` — adopted product definition; `docs/STATUS.md` — current state
- `_DomainEngines/profiles/pec.yaml` — amended 2026-07-24 (`D-PEC-59`) for the
  docs-archive paths and pivot notes; it binds the frozen engine instance
  only. Full supersession is pending v2 implementation shape. The L3
  operation-proposal (import) lane sunset with the old product and is not an
  agent lane.

## Project-Wide Execution Discipline

Use bounded tranches by default. A parent agent may orchestrate parallel TASK
fan-out only when subscopes are separable, briefs are explicit, and write
scopes are disjoint.

There may be other agents working in this monorepo with disjoint write scopes.
Treat unrelated dirty files outside the selected tranche as external state. Do
not fix, stage, revert, or interpret them unless the owner directs that work.

## Issue-Plan Rule

If concrete, actionable issues are discovered that would improve PEC's agentic
development loop, project governance, agents, or skills, record them in at most
one timestamped plan under `{WORKING_ROOT}/execution/_Coordination/` for the
session (in-fence; the legacy `plans/` target is outside the default
writable surfaces). Do not
create a plan merely to satisfy this instruction when no actionable issue was
found.

## Closeout And Git Discipline

When a tranche is complete and validated, use the project and root closeout
rules: inspect root git status, confirm validation evidence, stage only the
selected tranche scope, avoid unrelated dirty files, and commit/push only when
the branch can fast-forward safely.

Git closeout is source-control hygiene. It is not lifecycle issuance, release
readiness, professional approval, certification, sealing, authentication, or
code-compliance acceptance.
