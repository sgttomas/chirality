# project-setup — contract

## Runtime variables and defaults

This file is **project-generic**. Do not embed project-specific absolute paths in this workflow resource. Resolve instance paths from the human’s prompt and/or a recorded coordination record.

Defaults (only when not otherwise specified):
- `PROJECT_ROOT` = repo/project root (context-dependent)
- `EXECUTION_ROOT = execution/` (relative to `PROJECT_ROOT`)
- `COORDINATION_ROOT = {EXECUTION_ROOT}/_Coordination/`
- `DECOMP_ROOT = {EXECUTION_ROOT}/_Decomposition/`
- `SOURCES_ROOT = {EXECUTION_ROOT}/_Sources/` (optional; project may instead use `{PKG}/0_References/`)
- `AGENTS_ROOT = agents/` (relative; may vary by repo)

When this document refers to `execution/`, it means `{EXECUTION_ROOT}`.

---

## Session entry: state inspection

The session prompt names the role and `{EXECUTION_ROOT}`. WORKING_ITEMS discovers everything else by inspecting workspace state, then matches observed state to the active phase and proposes the next gate. There are no separate session categories — there is one operation: **inspect, infer, propose.** The setup mode (`INITIAL` or `INCREMENTAL`, see [Setup modes](#setup-modes)) is itself inferred from that state and confirmed in the proposal.

**Step 1 — Inspect workspace state.** Look at what actually exists on the filesystem. Do not commit to a category (initialization, resume, etc.) before doing this.

| Axis | What to check |
|---|---|
| Decomposition | `{EXECUTION_ROOT}/_Decomposition/` registers and the main accepted control-surface doc (e.g., `DOMAIN_DECOMP_..._FINAL_ACCEPTED_v*.md`). Accepted state? Errata flagged? Open issues / coverage gaps? |
| Sources | `{EXECUTION_ROOT}/_Sources/` (or equivalent). Extracted? `_LATEST.md` current? |
| Workspace structure | Are `CAT-NNN/` / package / deliverable folders scaffolded? To what depth? Any `_STATUS.md` lifecycle states beyond `OPEN`? |
| Authoring state | Any `KA-*.md` (DOMAIN) / `ScopeOfWork.md` or transitional legacy four-doc kits (PROJECT/SOFTWARE) present? Any `_REFERENCES.md` SCA-mode notes, contradictions registers, ratification verdicts? |
| Control-plane | Retrieval index `_LATEST.md` present + ledger md5 matches current `Atomic_Domain_Ledger.csv`? Hypergraph snapshot present at `_Aggregation/Hypergraph/`? |
| Scope change | Under `_ScopeChange/`: an amendment in progress (a group-1 or group-2 authorized pointer or candidate `SCA-*` folder not yet accepted at checkpoint group 3)? Accepted amendments (the `_LATEST.md` target and earlier accepted `SCA-*` snapshots) whose `Handoff_State.md` hands setup back to this workflow, that are not covered by the adoption baseline in `_Coordination/SETUP_LOG.md`, and that have no `COMPLETE` entry there? |

Read only what's needed to answer those axes. Do not ceremonially read every coordination file when the workspace state already tells you the answer.

**Step 2 — Infer the active phase.** Match the observed state against the phase definitions in `resources/method.md`. Common patterns:

- Decomposition absent → Function 1 (Initialize).
- Decomposition accepted + no scaffolded folders → Phase 2.1 (scaffolding with the effective source-qualified `preparation` skill by an eligible actor).
- Scaffolded folders + retrieval index present + no KAs → Phase 2.1b (retrieval preflight) → Phase 2.2 (authoring).
- KAs present + no hypergraph snapshot → Phase 2.6 (TASK (workflow: domain-hypergraph)).
- All initialization phases complete → Function 3 (Scan & report) or Function 4 (Estimating) per human request.
- Amendment in progress under `_ScopeChange/` → WORKING_ITEMS (workflow: scope-change) takes precedence; setup of the amended scope waits for its checkpoint group 3 acceptance.
- Accepted amendment with setup handed back and not yet recorded complete → Function 5 (Incremental setup) against that accepted snapshot.
- No `SETUP_LOG.md` baseline yet while accepted amendments exist (a project set up before incremental setup existed) → propose the Function 5 adoption step (Phase 5.0) first. Its baseline never covers an amendment whose `Handoff_State.md` hands setup to `project-setup` `INCREMENTAL`, so the amendment that prompted adoption is set up next.

If the observed state doesn't match a phase cleanly (e.g., partial scaffolding from an interrupted run, mismatched accepted-doc references, errata pending in registers), surface the discrepancy to the human before acting.

**Step 3 — Propose the next gate.** Report observed state + inferred phase + proposed next action. Apply documented defaults autonomously. Do NOT re-ask the human about decisions the coordination files already specify; surface only genuinely-novel decisions for human ruling.

---

## Non-negotiable invariants

- **Setup and delegated production.** The setup stage establishes the environment and visibility. WORKING_ITEMS assigns deliverable/domain production to bounded TASK stages with their selected methods, source basis, and output scope.
- **Filesystem is the state.** Project truth is in the folder structure + files. Do not maintain a separate hidden database.
- **Evidence-first reporting.** Report only what can be justified from files you actually read (with paths; best-effort anchors; or `location TBD`).
- **Human authority is the halting condition.** Confirmation gates are mandatory.
- **Coordination representation is human-owned.** WORKING_ITEMS records the representation the human chooses; it does not impose one.
- **No forced false precision.** If the human chooses not to track dependencies in-file, do not compute “blocked/available” as if a complete graph exists.
- **Bounded sub-agents only.** Spawn sub-agents only for clearly bounded work with explicit scope. When a deterministic tool exists for a structural or query operation, route that operation through the tool and reserve language-model work for reading, summarizing, or populating source-grounded text.
- **Bounded workflow stages use TASK.** Reusable method work such as `semantic-matrix-build`, `lens-register`, `dependency-extract`, `estimate-snapshot`, and `content-digest` is dispatched as `TASK + Workflow`, not by minting a new persona agent. WORKING_ITEMS writes or resolves the bounded brief; TASK normalizes scope, loads the selected workflow resources, follows its effective write boundary, supplies run evidence, and returns the auditable report.
- **Accepted work selection.** The human establishes the undertaking’s scope. WORKING_ITEMS assigns bounded contributions within that accepted scope and reports proposed scope changes for human decision.
- **Human-owned schedule basis.** Dependency evidence is not automatically a schedule constraint. Before schedule work, the human selects `PRECEDENCE | CONSTRAINT | HYBRID`, scope, hard-versus-soft edge rules, duration posture, calendars, and milestones.
- **No invented schedule facts.** Structure traces to accepted decomposition IDs; constraints trace to accepted dependency rows or explicit human rulings. Durations remain blank unless proposals are explicitly enabled and labeled.
- **Schedule cycle discipline.** PRECEDENCE cycles require a recorded human-approved resolution. CONSTRAINT/HYBRID cycles are represented as concurrency/risk patterns unless the human rules otherwise.
- **Schedule quarantine.** Each schedule run writes an immutable snapshot under `{EXECUTION_ROOT}/_Schedule/{RunID}/`; it never modifies decomposition or deliverable truth.
- **Incremental setup preserves existing work.** In `INCREMENTAL` mode, existing folders, IDs, file content and lifecycle state are kept. Added entities are scaffolded; retired entities are never deleted; modified deliverables go to their production contract's update path, never to re-scaffolding.
- **Lifecycle state recording follows the selected stage.** The authorized workflow and accepted project policy determine when state may advance. Record the actual decision actor separately from the executing recorder: human-gated CHECKING/ISSUED transitions require the human ruling and applicable approval evidence; WORKING_ITEMS or TASK records only transitions its brief and the guarded tool permit.

Recommended lifecycle ownership (may vary by project):
- **The actual eligible actor using the selected `preparation` skill** may set
  `OPEN` when creating deliverable folders within its existing role, brief, and
  write boundary. Record that actor rather than a former method identity.
- **`scope-of-work`, `MODE=INIT`** is the new PROJECT/SOFTWARE production
  initialization route and may support `INITIALIZED` only after validated
  `SOW_V1` exists under the human-confirmed lifecycle policy.
- **`four-documents`** remains compatibility-only for an existing complete
  `LEGACY_FOUR_DOC`; it does not initialize new production or advance state.
- **Semantic matrix generation** (`TASK + semantic-matrix-build`, Phase 2.3) produces the `_SEMANTIC.md` lens scaffold under `STATUS_POLICY=PRESERVE_CURRENT` and may append `_STATUS.md` history, but must not advance the lifecycle state to `SEMANTIC_READY` unless the human-confirmed project policy explicitly makes semantic-matrix validation the readiness gate (`STATUS_POLICY=ADVANCE_ON_PASS` with `_STATUS.md` write authorization).
- **Semantic enrichment completion:** for an existing `LEGACY_FOUR_DOC` kit,
  `four-documents` with `RUN_PASSES: P3_ONLY` applies `_SEMANTIC_LENSING.md`
  and may set `SEMANTIC_READY` when the semantic artifacts exist and the
  human-confirmed policy authorizes it. For `SOW_V1`, no bundled workflow
  currently applies `_SEMANTIC_LENSING.md` to `ScopeOfWork.md`, and
  `scope-of-work` never edits `_STATUS.md`; `SEMANTIC_READY` then requires a
  separately authorized status act under the recorded project policy.
- Humans decide whether/when to set `IN_PROGRESS`, `CHECKING`, `ISSUED` (or delegate via a dedicated state manager).

---

## Setup modes

| Mode | Applies when | Functions | Human checkpoints |
|---|---|---|---|
| `INITIAL` | An accepted decomposition has not yet been set up | 1 (Initialize), 2 (Scaffold + setup pipelines) | The phase gates of Functions 1–2 |
| `INCREMENTAL` | An accepted `scope-change` amendment, not covered by the project's adoption baseline, has been applied and its `Handoff_State.md` hands setup back to this workflow | 5 (Incremental setup) | Confirm the adoption baseline once per project where `INITIAL` setup did not record it; confirm the incremental plan; then report. Other gates only for decisions the stages reserve (for example accepting a `project-dag` successor or rejecting the change for `DAG pending` deliverables, SCC resolution, a lifecycle act such as reopening an `ISSUED` deliverable) |

Functions 3 (Scan & report) and 4 (Estimating) apply in either mode on request.

### `INCREMENTAL` inputs

| Input | Source | Requirement |
|---|---|---|
| `AMENDMENT_SNAPSHOT` | `{EXECUTION_ROOT}/_ScopeChange/_LATEST.md` target, or an earlier accepted `SCA-*` snapshot still awaiting setup | Accepted at checkpoint group 3 and not covered by the adoption baseline. A candidate or returned snapshot is not an input; an amendment covered by the baseline is never reprocessed. |
| Accepted action register | `Amendment_Actions.csv` in the snapshot, or the distinct register its group-2 `ACCEPTED_MANIFEST.csv` names (for example `Amendment_Actions_CP2.csv`) | Resolve through the accepted manifest; `Intake_Actions.csv` is group-1 evidence only. Verify the recorded hash. |
| `Propagation_Plan.md`, `Handoff_State.md` | The same snapshot | Name the hand-back, derivative state, deferred items and blockers. |
| Amended decomposition | `{DECOMP_ROOT}/`, as applied by the amendment | Source of IDs, names, parent bindings and metadata for added entities. |
| Coordination record | `{COORDINATION_ROOT}/_COORDINATION.md` | Representation, dependency tracking mode (`docs/SPEC.md` §5.3) and threshold are reused, not re-asked. Read only; this workflow does not write the human-owned record in `INCREMENTAL` mode. |
| Setup log | `{COORDINATION_ROOT}/SETUP_LOG.md` | Agent-owned and append-only (see [Setup log](#setup_logmd-project-level-agent-owned-append-only)). Holds the adoption baseline and one line per incremental run. Created at the end of `INITIAL` setup (method Phase 2.7), or by the adoption step (Phase 5.0) in a project set up before incremental setup existed. |
| Production format | Each affected deliverable, resolved per `docs/SPEC.md` §2.2 | Selects the update path for `MODIFY`. |

If any input is missing, unaccepted or inconsistent with the workspace (for example a `REMOVE` without its decomposition annotation), report the discrepancy and return it to `scope-change` rather than repairing decomposition truth here.

### `INCREMENTAL` action treatment

| Accepted action | Setup treatment |
|---|---|
| `ADD` (and successor entities of `MERGE`/`SPLIT`) | Scaffold only the new package, deliverable, category or knowledge type with the source-qualified `preparation` skill (Phase 2.1 rules), then initialize production with the project's contract (`SOW_V1` via `scope-of-work`, `MODE=INIT`; DOMAIN via `domain-documents` with `AUTHORITY_MODE: SCA_DRIVEN` as the amendment's hand-off) and create its dependency and status records. |
| `REMOVE` (and sources retired by `MERGE`/`SPLIT`) | No deletion of folders or files. Confirm the `scope-change` retirement rule was applied: the `[RETIRED — {AMENDMENT_ID}]` decomposition annotation and one appended `_STATUS.md` history line, lifecycle state unchanged, `write_status.sh` not used. Append the history line only where the accepted poststate lacks it. |
| `MODIFY` | No re-scaffolding. Route the deliverable to its production contract's update path (Function 5, Phase 5.5): for `SOW_V1`, `scope-of-work` `MODE=REVISE` ending in `MODE=VERIFY`. A `CHECKING` or `ISSUED` deliverable is held for the human; an `ISSUED` deliverable reopens only as `docs/SPEC.md` §3.3 allows. `_CONTEXT.md` edits belong to the amendment itself. |
| `RECLASSIFY` | Routed as `MODIFY` (Phase 5.5). An `ISSUED` deliverable reopens only for a scope-changing `RECLASSIFY` (`docs/SPEC.md` §3.3). Move a folder only when the accepted propagation plan names the relocation and the human confirms it in the incremental plan; move it whole, keeping content and `_STATUS.md`. |

The affected set is the deliverables named by the accepted actions. Their
neighbours are the deliverables with a recorded edge to or from an affected
deliverable (declared sections, `Dependencies.csv`) and any the accepted
impact assessment names for dependency review.

Where the project has an accepted project DAG (`docs/SPEC.md` §5.4), the
incremental dependency stage ends with a `project-dag` currency audit. The
deliverables a departure affects are `DAG pending` until the human accepts the
candidate successor or rejects the change; unaffected work continues on the
accepted version. This workflow reports the flag and does not clear it.

---

## Glossary (minimal)

- **Package**: A top-level scope grouping in the decomposition (`PKG-…`).
- **Deliverable / Working item**: A scoped unit of work (`DEL-…`) represented by one deliverable folder.
- **Lifecycle state**: `OPEN | INITIALIZED | SEMANTIC_READY | IN_PROGRESS | CHECKING | ISSUED` (local to the deliverable folder).
- **Coordination representation** (`docs/TYPES.md` §6, `docs/SPEC.md` §13): The human’s chosen way to coordinate across packages/deliverables, recorded separately from the dependency tracking mode:
  - `SCHEDULE_FIRST` — a schedule (Gantt) drives sequencing; recorded dependencies, unless the mode is `NOT_TRACKED`, support blocker detection and audit.
  - `DEPENDENCY_TRACKED` — the dependency graph drives sequencing.
  - `HYBRID` — a combination of schedule-first and dependency-tracked.
  - Earlier records may carry the former option labels (`Schedule-first`; `Declared deps` or `Declared critical dependencies`; `Full graph` or `Full dependency graph (DAG)`); they remain readable as written. `Schedule-first` corresponds to `SCHEDULE_FIRST`; the declared and full-graph labels named a tracking mode (`DECLARED`, `FULL_GRAPH`) rather than a representation, so confirm the representation with the human when the record is next updated.
- **Dependency tracking mode** (`docs/SPEC.md` §5.3):
  - `NOT_TRACKED` — dependency coordination occurs outside the files (humans or an external schedule); do not compute blockers or report a ready/blocked judgment from dependencies.
  - `DECLARED` — only critical dependencies are recorded (partial, human-curated); the recorded edges are a partial view. Compute blockers only from the recorded register (see **Dependency register**). Dependency extraction may add `Dependencies.csv` rows when the Phase 1.3 rules call for it; it does not make the view complete.
  - `FULL_GRAPH` — dependency declarations are intended to form a complete DAG; compute blockers only from the declared graph in the recorded register, after closure audit and cycle treatment (see Validity).
  - A legacy `TRACKED` value in an existing record is read as `FULL_GRAPH`; new records write `FULL_GRAPH`.
- **Dependency register**: deliverable-local dependency artifacts: `_DEPENDENCIES.md`, with the `docs/SPEC.md` §5.2 headings, and `Dependencies.csv` when present. They are the dependency evidence (`docs/SPEC.md` §5.4). In a project without an accepted project DAG, the recorded register used for blockers is the union of the declared entries in `_DEPENDENCIES.md` and the CSV rows (`docs/SPEC.md` §5.3). `dependency-extract` mirrors each declared entry into the CSV as an `Origin=DECLARED` row, but a file not yet refreshed may hold a declaration only in the markdown, so never compute blockers from the CSV alone. A declared entry and a row for the same direction and target are one edge, counted once; where they disagree, the declared section governs and the disagreement is reported. In a project with an accepted project DAG, blockers come instead from the accepted current version named by `_DAG/_LATEST.md`, and a deliverable whose local evidence departs from it is `DAG pending` until the human decides (`docs/SPEC.md` §5.4; `project-dag`).
- **Semantic lens artifacts**:
  - `_SEMANTIC.md` is a lens scaffold (question-shaping), not an authority.
  - `_SEMANTIC_LENSING.md` is an enrichment register, not an authority.

---

## Validity

### Workspace validity

A workspace is valid when:
- Every package from the decomposition has a folder with `0_References/`, `1_Working/`, `2_Checking/`, `3_Issued/`.
- Every deliverable from the decomposition has a folder in the appropriate package `1_Working/`.
- Every deliverable folder contains the minimum viable fileset (see STRUCTURE).
- `{COORDINATION_ROOT}/_COORDINATION.md` exists and reflects the human-confirmed coordination representation.

### Coordination representation validity

- Representation and dependency mode were explicitly confirmed by the human.
- If mode is `NOT_TRACKED`, reports must not label deliverables as blocked/available based on dependencies.
- If mode is `DECLARED` or `FULL_GRAPH`, blockers are computed, in a project without an accepted project DAG, from the recorded register, which is the union of the declared entries in `_DEPENDENCIES.md` and `Dependencies.csv` (see **Dependency register**); in a project with one, from its accepted current version, with `DAG pending` deliverables given no verdict. In either case they are computed only from edges outside unresolved cycles. Edges that participate in an unresolved SCC are non-gating: they are excluded from blocker computation and reported as held pending resolution through `scc-resolution-case` and the owning decisions (`docs/CYCLE_DRIVEN_RESOLUTION.md` §2 rule 4). A cycle does not by itself invalidate the coordination record or block independent work.

### S-EST — Estimating pipeline validity

The estimating pipeline (Function 4) may only proceed when:
- `{EXECUTION_ROOT}/INIT.md` exists and contains both a `Basis of Estimate` path and a `Price Sources` path.
- The BOE document at the referenced path exists and contains at minimum: Section 3 (Estimation Strategy), Section 4 (Per-Deliverable Estimation Plan), and Section 5 (Run Sequence).
- `_PriceSources/INDEX.md` exists at the referenced path and contains a per-package file mapping.
- Each deliverable targeted for estimation has a resolvable `BASIS_OF_ESTIMATE` entry in BOE Section 4.

If any of these conditions are not met, WORKING_ITEMS must report the specific missing prerequisite and halt the pipeline (do not attempt partial runs without human authorization).

### Invalid states (examples)

- Deliverable folder missing minimum viable fileset (downstream agents cannot operate).
- Coordination mode unspecified (WORKING_ITEMS cannot know whether to compute blockers).
- Reporting blockers in `NOT_TRACKED` mode (false precision).
- Running semantic lensing steps out of order (no `_SEMANTIC.md` or `_SEMANTIC_LENSING.md`).
- Running estimating pipeline without a BOE or INDEX.md (`estimate-snapshot` cannot operate).
- Spawning `estimate-snapshot` for a deliverable excluded in BOE Section 4 (contradicts human strategy).
- Executing a later tier before all runs in the preceding tier have reported status (breaks tier sequencing).

---

## Artifacts and schemas

### Folder hierarchy (conceptual)

```
{PROJECT_ROOT}/
  agents/                      # agent instructions (repo-specific)
  {EXECUTION_ROOT}/             # runtime workspace
    _Coordination/
      _COORDINATION.md
      _Archive/
    _Decomposition/            # decomposition document(s)
    _Sources/                  # optional reference staging area
    {PKG-ID}_{PkgLabel}/       # one per package
      0_References/
        _Archive/
      1_Working/
        _Archive/
        {DEL-ID}_{DelLabel}/   # one per deliverable (flat)
          _CONTEXT.md
          _STATUS.md
          _REFERENCES.md
          _DEPENDENCIES.md
          Dependencies.csv         # optional; produced by TASK+dependency-extract
          _SEMANTIC.md             # required placeholder; lens scaffold content optional
          _SEMANTIC_LENSING.md     # enrichment register (optional)
          ScopeOfWork.md           # SOW_V1 production contract (scope-of-work, MODE=INIT)
          # Datasheet.md, Specification.md, Guidance.md, Procedure.md:
          # transitional LEGACY_FOUR_DOC kit only where it already exists
      2_Checking/
        From/
        To/
      3_Issued/
        _Archive/
```

**Filesystem-safe labels:** `{PkgLabel}` and `{DelLabel}` are sanitized derivatives of names. Canonical names remain in `_CONTEXT.md`. Where the project has a recorded folder-label rule (for example in its decomposition or coordination record, or evidenced by its existing accepted folders), that rule governs; the `preparation` skill's sanitization rule is the default for new workspaces.

---

### Minimum viable fileset (deliverable-local)

Every deliverable folder should be seeded with:

| File | Purpose | Notes |
|---|---|---|
| `_CONTEXT.md` | Identity and scope | Must contain stable IDs from decomposition |
| `_STATUS.md` | Lifecycle state | Authoritative lifecycle indicator |
| `_REFERENCES.md` | Sources index | Pointers to package references and other materials |
| `_DEPENDENCIES.md` | Human-readable dependency view | Created with the `docs/SPEC.md` §5.2 skeleton; TASK+dependency-extract refreshes only its agent-owned sections |
| `Dependencies.csv` | Structured dependency edges | Optional; created by TASK+dependency-extract when run |
| `_SEMANTIC.md` | Semantic lens scaffold | Required placeholder at scaffold time; lens content optional and created/overwritten by TASK+semantic-matrix-build |
| `_SEMANTIC_LENSING.md` | Enrichment register | Optional; created by TASK+lens-register |

---

### `_COORDINATION.md` (project-level; human-owned)

```markdown
# Coordination Record

**Representation:** [SCHEDULE_FIRST | DEPENDENCY_TRACKED | HYBRID]
**Dependency tracking mode:** [NOT_TRACKED | DECLARED | FULL_GRAPH]
**External schedule / coordination artifact:** [path/link or "N/A"]
**Default maturity threshold (if computing blockers):** [INITIALIZED|SEMANTIC_READY|IN_PROGRESS|CHECKING|ISSUED]

## Notes (human-owned)
- [How the team is coordinating]
- [Optional: stage gates definitions live here if humans want them recorded]
```

This workflow does not add agent-written sections to `_COORDINATION.md`. Setup
evidence goes to `SETUP_LOG.md` below.

---

### `SETUP_LOG.md` (project-level; agent-owned, append-only)

`{COORDINATION_ROOT}/SETUP_LOG.md` records incremental setup. WORKING_ITEMS
creates it when `INITIAL` setup completes (method Phase 2.7), or at the
adoption step (Phase 5.0) in a project set up before incremental setup
existed, and appends lines; it never edits or deletes an earlier line. A correction is a new line that names the line it corrects.

```markdown
# Setup Log

Agent-owned and append-only. Written by WORKING_ITEMS (workflow: project-setup).

- [YYYY-MM-DD] — BASELINE: incremental setup adopted; amendments accepted up to [YYYY-MM-DD] (latest [AMENDMENT_ID or "none"]) are already set up and are not reprocessed; confirmed by [human]
- [YYYY-MM-DD] — INCREMENTAL [AMENDMENT_ID] setup [COMPLETE | PARTIAL | BLOCKED]; run record [path]
```

The `BASELINE` line is written once per project, with the human's
confirmation. `INITIAL` setup writes it with `latest none` (or the latest
accepted amendment already included in the decomposition it set up). At
adoption in an existing project, the proposed baseline names the latest
accepted amendment whose `Handoff_State.md` does not hand setup to
`project-setup` `INCREMENTAL`, or `none`, and its acceptance date. It covers
the amendment it names and those accepted before it; those are never
reprocessed in `INCREMENTAL` mode. An amendment whose `Handoff_State.md` hands
setup to `project-setup` `INCREMENTAL` is never covered by the baseline. An `INCREMENTAL` line marked `COMPLETE` is the record that
an accepted amendment's setup hand-back has been carried out.

---

### Deliverable IDs (important)

Deliverable IDs are sourced from the decomposition. Do not invent new IDs. The expected pattern is the hyphen style (format varies by decomposition variant):
- WORKING_ITEMS (workflow: project-decomp): `DEL-PPP-LL_{shortDescription}` (3-digit package, 2-digit sequence, description suffix)
- WORKING_ITEMS (workflow: software-decomp): `DEL-PP-LL` (2-digit package, 2-digit sequence, no suffix)
- WORKING_ITEMS (workflow: domain-decomp): `KTY-CC-TT_{shortDescription}` (category, type sequence, description suffix)

---

## Output Persistence

The selected setup phases produce these durable artifacts:

- `{COORDINATION_ROOT}/_COORDINATION.md` — coordination representation record (human-owned)
- `{COORDINATION_ROOT}/SETUP_LOG.md` — for `INCREMENTAL` mode, the agent-owned, append-only setup log with its adoption baseline
- Package and deliverable folders (via the actual eligible actor using the
  selected source-qualified `preparation` skill)
- Bounded contribution outputs, including TASK outputs when dispatch was used
- For `INCREMENTAL` mode, a run record under `{COORDINATION_ROOT}/AgentRuns/<RunID>/` (`docs/SPEC.md` §9.8) holding the confirmed incremental plan, the amendment snapshot path and register hash, briefs, returns, created and skipped paths, dependency-stage evidence and the final report

These artifacts persist in the filesystem and are git-tracked. Phase-boundary evidence and any accepted snapshot references are recorded in the undertaking’s handoff.

---
