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

The session prompt names the role and `{EXECUTION_ROOT}`. WORKING_ITEMS discovers everything else by inspecting workspace state, then matches observed state to the active phase and proposes the next gate. There are no session modes — there is one operation: **inspect, infer, propose.**

**Step 1 — Inspect workspace state.** Look at what actually exists on the filesystem. Do not commit to a category (initialization, resume, etc.) before doing this.

| Axis | What to check |
|---|---|
| Decomposition | `{EXECUTION_ROOT}/_Decomposition/` registers and the main accepted control-surface doc (e.g., `DOMAIN_DECOMP_..._FINAL_ACCEPTED_v*.md`). Accepted state? Errata flagged? Open issues / coverage gaps? |
| Sources | `{EXECUTION_ROOT}/_Sources/` (or equivalent). Extracted? `_LATEST.md` current? |
| Workspace structure | Are `CAT-NNN/` / package / deliverable folders scaffolded? To what depth? Any `_STATUS.md` lifecycle states beyond `OPEN`? |
| Authoring state | Any `KA-*.md` (DOMAIN) / `ScopeOfWork.md` or transitional legacy four-doc kits (PROJECT/SOFTWARE) present? Any `_REFERENCES.md` SCA-mode notes, contradictions registers, ratification verdicts? |
| Control-plane | Retrieval index `_LATEST.md` present + ledger md5 matches current `Atomic_Domain_Ledger.csv`? Hypergraph snapshot present at `_Aggregation/Hypergraph/`? `_ScopeChange/_LATEST.md` indicating an active SCA? |

Read only what's needed to answer those axes. Do not ceremonially read every coordination file when the workspace state already tells you the answer.

**Step 2 — Infer the active phase.** Match the observed state against the phase definitions in `resources/method.md`. Common patterns:

- Decomposition absent → Function 1 (Initialize).
- Decomposition accepted + no scaffolded folders → Phase 2.1 (scaffolding with the effective source-qualified `preparation` skill by an eligible actor).
- Scaffolded folders + retrieval index present + no KAs → Phase 2.1b (retrieval preflight) → Phase 2.2 (authoring).
- KAs present + no hypergraph snapshot → Phase 2.6 (TASK (workflow: domain-hypergraph)).
- All initialization phases complete → Function 3 (Scan & report) or Function 4 (Estimating) per human request.
- Active `_ScopeChange/_LATEST.md` → WORKING_ITEMS (workflow: scope-change) workflow takes precedence.

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

## Glossary (minimal)

- **Package**: A top-level scope grouping in the decomposition (`PKG-…`).
- **Deliverable / Working item**: A scoped unit of work (`DEL-…`) represented by one deliverable folder.
- **Lifecycle state**: `OPEN | INITIALIZED | SEMANTIC_READY | IN_PROGRESS | CHECKING | ISSUED` (local to the deliverable folder).
- **Coordination representation**: The human’s chosen way to coordinate across packages/deliverables.
- **Dependency tracking mode** (`docs/SPEC.md` §5.3):
  - `NOT_TRACKED` — dependency coordination occurs outside the files (humans or an external schedule); do not compute blockers or report a ready/blocked judgment from dependencies.
  - `DECLARED` — only critical dependencies are recorded (partial, human-curated); the recorded edges are a partial view. Compute blockers only from the recorded register (the declared sections, or `Dependencies.csv`, whose DECLARED-origin rows carry the declarations, where extraction has run). Dependency extraction may add `Dependencies.csv` rows when the Phase 1.3 rules call for it; it does not make the view complete.
  - `FULL_GRAPH` — dependency declarations are intended to form a complete DAG; compute blockers only from the declared graph, after closure audit and cycle treatment (see Validity).
  - A legacy `TRACKED` value in an existing record is read as `FULL_GRAPH`; new records write `FULL_GRAPH`.
- **Dependency register**: deliverable-local dependency artifacts (prefer `Dependencies.csv` when present; `_DEPENDENCIES.md` as human-readable view, with the `docs/SPEC.md` §5.2 headings).
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
- If mode is `DECLARED` or `FULL_GRAPH`, blockers are computed only from edges outside unresolved cycles. Edges that participate in an unresolved SCC are non-gating: they are excluded from blocker computation and reported as held pending resolution through `scc-resolution-case` and the owning decisions (`docs/CYCLE_DRIVEN_RESOLUTION.md` §2 rule 4). A cycle does not by itself invalidate the coordination record or block independent work.

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

**Representation:** [Schedule-first | Declared deps | Full graph]
**Dependency tracking mode:** [NOT_TRACKED | DECLARED | FULL_GRAPH]
**External schedule / coordination artifact:** [path/link or "N/A"]
**Default maturity threshold (if computing blockers):** [INITIALIZED|SEMANTIC_READY|IN_PROGRESS|CHECKING|ISSUED]

## Notes (human-owned)
- [How the team is coordinating]
- [Optional: stage gates definitions live here if humans want them recorded]
```

---

### Deliverable IDs (important)

Deliverable IDs are sourced from the decomposition. Do not invent new IDs. The expected pattern is the hyphen style (format varies by decomposition variant):
- WORKING_ITEMS (workflow: project-decomp): `DEL-PPP-LL_{shortDescription}` (3-digit package, 2-digit sequence, description suffix)
- WORKING_ITEMS (workflow: software-decomp): `DEL-PP-LL` (2-digit package, 2-digit sequence, no suffix)
- WORKING_ITEMS (workflow: domain-decomp): `KTY-CC-TT_{shortDescription}` (category, type sequence, description suffix)

---

## Output Persistence

The selected setup phases produce these durable artifacts:

- `{COORDINATION_ROOT}/_COORDINATION.md` — coordination representation record
- Package and deliverable folders (via the actual eligible actor using the
  selected source-qualified `preparation` skill)
- Bounded contribution outputs, including TASK outputs when dispatch was used

These artifacts persist in the filesystem and are git-tracked. Phase-boundary evidence and any accepted snapshot references are recorded in the undertaking’s handoff.

---
