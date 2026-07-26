# N2 Terminal Return — Root Project Setup, guard-state instantiation

Run: `ROOT-STEP8-DECOMP-20260725` · Node: N2 · Date: 2026-07-25
Executor: Agent 1, **PROJECT_SETUP** role, `opus-5`. No delegation.
Brief: `execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/briefs/PROJECT-SETUP-BRIEF.md`
Worktree branch: `claude/root-step8-acceptance-20260725` (no commit, no branch, no push).

**Verdict: COMPLETE.** Four guard-state files written under
`execution/_harness/`. G0–G4 all observed PASS against the state written.
`tools/validation` suite: 233 passed. Working tree left uncommitted.

---

## 1. Files written (full content inlined)

### 1.1 `execution/_harness/adapter.yaml`

```yaml
# Root harness adapter — G1 state surface (D-GOV-21 §5.3, packet §6 step 8).
#
# Instantiated by root Project Setup. Gives root `execution/` the same
# deterministic status/drift surface the project working roots have.
# Guard: tools/validation/validate_root_harness_adapter.py
#
# NOTE: this is `root-harness-adapter/v1`, NOT the projects'
# `practitioner-harness-adapter/v1`. Adoption of the root into the
# practitioner harness (PROJECT_ALIASES / loader relpath) is a separately
# authorized open item and is not claimed here.

schema: root-harness-adapter/v1
product: chirality-root

# D-GOV-21 / docs/SPEC.md §0.2.2: for the root product WORKING_ROOT == REPO_ROOT.
working_root: "."
execution_root: execution

# Declared pointers (repo-relative; all verified present at instantiation).
prd: docs/PRD_ROOT.md
coordination: execution/_Coordination/CURRENT_WORKPLAN.md
decision_register: docs/governance_harness/_DECISIONS/_REGISTER.md

# Root SPEC layout: docs/SPEC.md §1 / §2 —
# {EXECUTION_ROOT}/{PKG-ID}_{PkgLabel}/1_Working/{DEL-ID}_{DelLabel}/_STATUS.md
status_glob: execution/PKG-*/1_Working/DEL-*/_STATUS.md

# Canonical lifecycle states, docs/SPEC.md §3.2 (verbatim, in ruled order).
# SEMANTIC_READY is optional in the lifecycle but is a valid state.
states:
  - OPEN
  - INITIALIZED
  - SEMANTIC_READY
  - IN_PROGRESS
  - CHECKING
  - ISSUED

parser_dialect: prose-bullet-v1

exclude_globs:
  - ".archive/**"

baselines:
  # Pre-materialization: no PKG-*/DEL-* structure exists under root execution/,
  # so the observed status_glob count is 0. Verified against the checkout.
  status_files: 0
  status_mismatch: 0
  pinned_at: ea0ad7a566ddb51d89297bfcf491636f1fc5dd15
```

### 1.2 `execution/_harness/surface_ownership.yaml`

```yaml
# Root surface-ownership register — G2 state surface (D-GOV-21 §5.3, M1).
#
# Instantiated by root Project Setup from the accepted root decomposition.
# Guard: tools/validation/validate_root_surface_ownership.py
#
# Static facts only; no concurrency claims. `decomposition_ref` values are the
# exact package identifier strings as they appear in the declared working
# surface (G2 checks literal containment).
#
# DEL-* entries are added at materialization time (packet §6 step 9), not here.

schema: root-surface-ownership/v1
decomposition: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md

entries:
  - id: PKG-01_Product_Definition_Normative_Basis_and_Authority
    kind: package
    decomposition_ref: PKG-01_Product_Definition_Normative_Basis_and_Authority
    write_targets:
      - execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/**
    instruction_surface: false
    serialization: null

  - id: PKG-02_Operative_Instruction_Surface_and_Runtime_Layers
    kind: package
    decomposition_ref: PKG-02_Operative_Instruction_Surface_and_Runtime_Layers
    write_targets:
      - execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**
    instruction_surface: false
    serialization: null

  - id: PKG-03_Governed_Execution_Structure_and_Root_Containment
    kind: package
    decomposition_ref: PKG-03_Governed_Execution_Structure_and_Root_Containment
    write_targets:
      - execution/PKG-03_Governed_Execution_Structure_and_Root_Containment/**
    instruction_surface: false
    serialization: null

  - id: PKG-04_Developmental_Machinery_and_Change_Control
    kind: package
    decomposition_ref: PKG-04_Developmental_Machinery_and_Change_Control
    write_targets:
      - execution/PKG-04_Developmental_Machinery_and_Change_Control/**
    instruction_surface: false
    serialization: null

  - id: PKG-05_Evidence_Provenance_and_Audit
    kind: package
    decomposition_ref: PKG-05_Evidence_Provenance_and_Audit
    write_targets:
      - execution/PKG-05_Evidence_Provenance_and_Audit/**
    instruction_surface: false
    serialization: null

  - id: PKG-06_Self_Application_Variants_and_Release
    kind: package
    decomposition_ref: PKG-06_Self_Application_Variants_and_Release
    write_targets:
      - execution/PKG-06_Self_Application_Variants_and_Release/**
    instruction_surface: false
    serialization: null
```

### 1.3 `execution/_harness/work_graph.yaml`

```yaml
# Root work graph — G3 state surface (D-GOV-21 §5.3, M1/M2).
#
# The first accepted root work graph, instantiated by root Project Setup.
# Guard: tools/validation/validate_root_work_graph_dispatch.py
#
# One node per accepted package. Every node is `pending`: nothing is
# dispatched at instantiation, and materialization (packet §6 step 9) remains
# behind the D-GOV-21 §5.3 gate.
#
# No `depends_on` / `serialized_after` edges are declared. The accepted
# decomposition §8 states "Six flat work-domain packages. No nesting, no
# phases, no overlap, no gaps." and its §14 Downstream Execution Notes declare
# no inter-package ordering. Ordering is never inferred here.
#
# No `m2_marker` is declared: every node's write targets are confined to
# `execution/<package>/**`, which does not intersect the instruction surface.

schema: root-work-graph/v1

# M3 frozen instruction basis: the merge SHA of PR #347, the tranche in which
# the first root decomposition was accepted by owner ruling (D-GOV-25).
accepted_basis: ea0ad7a566ddb51d89297bfcf491636f1fc5dd15

nodes:
  - id: PKG-01_Product_Definition_Normative_Basis_and_Authority
    status: pending
    owner: PKG-01_Product_Definition_Normative_Basis_and_Authority
    write_targets:
      - execution/PKG-01_Product_Definition_Normative_Basis_and_Authority/**

  - id: PKG-02_Operative_Instruction_Surface_and_Runtime_Layers
    status: pending
    owner: PKG-02_Operative_Instruction_Surface_and_Runtime_Layers
    write_targets:
      - execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**

  - id: PKG-03_Governed_Execution_Structure_and_Root_Containment
    status: pending
    owner: PKG-03_Governed_Execution_Structure_and_Root_Containment
    write_targets:
      - execution/PKG-03_Governed_Execution_Structure_and_Root_Containment/**

  - id: PKG-04_Developmental_Machinery_and_Change_Control
    status: pending
    owner: PKG-04_Developmental_Machinery_and_Change_Control
    write_targets:
      - execution/PKG-04_Developmental_Machinery_and_Change_Control/**

  - id: PKG-05_Evidence_Provenance_and_Audit
    status: pending
    owner: PKG-05_Evidence_Provenance_and_Audit
    write_targets:
      - execution/PKG-05_Evidence_Provenance_and_Audit/**

  - id: PKG-06_Self_Application_Variants_and_Release
    status: pending
    owner: PKG-06_Self_Application_Variants_and_Release
    write_targets:
      - execution/PKG-06_Self_Application_Variants_and_Release/**
```

### 1.4 `execution/_harness/root_guards.yaml`

```yaml
# Root guard registration surface — G0's state surface (D-GOV-21 §5.3).
#
# Instantiated by root Project Setup (packet §6 step 8) after each guard was
# run against the state written in this same act and observed PASS.
# Guard: tools/validation/validate_root_materialization_fence.py
#
# G0 requires no entry for itself; it reads this file only once PKG-*/DEL-*
# structure exists under root execution/ (packet §6 step 9, still gated).
# Registration records that a guard is wired and observed passing; it holds no
# authority and confers none (K-AUTH-1).
#
# Entry shapes are verbatim from each guard's own docstring
# ("Registration entry it will assert in execution/_harness/root_guards.yaml").

guards:
  G1:
    registered: true
    status: passing
    validator: tools/validation/validate_root_harness_adapter.py
    tests: tools/validation/test_validate_root_harness_adapter.py
    state_surface: execution/_harness/adapter.yaml
    schema: root-harness-adapter/v1

  G2:
    registered: true
    status: passing
    validator: tools/validation/validate_root_surface_ownership.py
    tests: tools/validation/test_validate_root_surface_ownership.py
    state_surface: execution/_harness/surface_ownership.yaml
    schema: root-surface-ownership/v1

  G3:
    registered: true
    status: passing
    validator: tools/validation/validate_root_work_graph_dispatch.py
    tests: tools/validation/test_validate_root_work_graph_dispatch.py
    state_surface: execution/_harness/work_graph.yaml
    schema: root-work-graph/v1
    dispatch_mode: "--work-graph PATH --brief PATH [--brief PATH ...]"

  G4:
    registered: true
    status: passing
    validator: tools/validation/validate_instruction_tranche_manifest.py
    tests: tools/validation/test_validate_instruction_tranche_manifest.py
    state_surface: docs/governance_harness/tranche_manifests/
    schema: instruction-tranche-manifest/v1
    diff_mode: "--base REF --head REF [--tranche ID]"
```

---

## 2. Design choices that were mine, with sources

Everything below was left to inspection by the brief. Each choice cites the
surface it was read from; nothing was invented.

| # | Choice | Value | Source read |
|---|---|---|---|
| C-1 | `states` list | `OPEN, INITIALIZED, SEMANTIC_READY, IN_PROGRESS, CHECKING, ISSUED` | `docs/SPEC.md` §3.2 "Valid Lifecycle States" — the ruled chain `OPEN → INITIALIZED → SEMANTIC_READY → IN_PROGRESS → CHECKING → ISSUED` and its state table. Recorded in ruled order. `SEMANTIC_READY` is included though §3.2 marks it optional in the lifecycle: it is a *valid* state, and the adapter enumerates the state vocabulary, not a mandatory path. |
| C-2 | Ordering edges (`depends_on` / `serialized_after`) | **None declared** | The accepted decomposition declares no inter-package ordering. §8: "Six flat work-domain packages. **No nesting, no phases, no overlap, no gaps.**" §14 *Downstream Execution Notes* records G2 readiness, G3 readiness, materialization gating, executor and reviewer guidance — and no sequencing between packages. The package table's `Exclusions` column names other packages, but as *ownership boundaries* (what each package does not own), not as ordering. Per the brief, ordering is mirrored only where declared and never inferred; none is declared, so none is written. |
| C-3 | Package identifier strings | Full `PKG-NN_Label` forms (e.g. `PKG-01_Product_Definition_Normative_Basis_and_Authority`) | `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` §8 package table `PackageID` column, echoed by the §9 `### PKG-…` headings. These are the literal strings G2 tests for containment; §14 confirms every identifier "appears verbatim in this working surface". They also satisfy G2's `ID_RE = ^(PKG\|DEL)-[A-Za-z0-9._-]+$` (underscore is in the class). |
| C-4 | `write_targets` shape | `execution/<full-package-id>/**` | Required by G2 `covers_own_tree` (a target must cover `execution/<id>/`) and G3 `covered_by` (node targets must fall inside the owner's register targets). One target per entry/node; identical strings in register and graph, so coverage is exact rather than approximate. |
| C-5 | `instruction_surface` | `false` for all six | G2/G3 `intersects_instruction_surface`: the instruction surface is `AGENTS.md`, `agents/`, `skills/`, `tools/`, `docs/`, `init/`, `.github/workflows/`. No target begins with any of those prefixes; all are under `execution/`. Marking `true` would have been over-declaration (G2 emits a non-blocking INFO for that). |
| C-6 | `m2_marker` | Omitted on every node | G3 requires the marker only where declared targets intersect the instruction surface (C-5: none do). The brief's condition for omission holds. |
| C-7 | Node `id` | Equal to the package ID (and to `owner`) | Brief §3. G3 imposes no id format beyond uniqueness/non-blank; making node id == owner id == register id keeps the three surfaces joinable by one string. |
| C-8 | Node `status` | `pending` for all six | Brief: nothing is dispatched. Side effect: G3's active-node disjointness check has no active pair to evaluate, so no serialization declarations were needed. |
| C-9 | `serialization` | `null` for all six | No accepted predecessor or declared integration owner exists at instantiation; G2 treats overlap as an INFO-only static fact anyway, and there is no overlap (six disjoint trees). |
| C-10 | `baselines.status_files` | `0` | Verified, not assumed: `Path('.').glob('execution/PKG-*/1_Working/DEL-*/_STATUS.md')` returns 0 matches in this checkout, and G1's own cross-check confirmed it (`status_files=0` in the PASS line). |
| C-11 | `accepted_basis` provenance comment | "merge SHA of PR #347 … D-GOV-25" | Brief §"Authorization and context" (`EffectiveSHA ea0ad7a…`, merge of PR #347; decision record D-GOV-25). Recorded, not invented — consistent with the step-8 evidence note that the first graph's basis is "recorded at instantiation, not invented". |
| C-12 | Comment headers on all four files | Present | Not required by any validator; added so each state surface names its guard, its authoring act, and the reason for any omission (edges, markers). No comment makes a claim the guards do not check. |

**No file was created beyond the four.** No `INIT.md`, no scaffolding, no
`PKG-*`/`DEL-*` directory — consistent with the decomposition §14
("Materialization … is step 9 behind the D-GOV-21 §5.3 gate") and with G0
remaining lawfully idle.

---

## 3. Verification transcript (verbatim, in brief order)

```
### CMD 1: validate_root_harness_adapter.py
$ python3 tools/validation/validate_root_harness_adapter.py
G1 PASS: root harness adapter execution/_harness/adapter.yaml is schema-valid (root-harness-adapter/v1); declared pointers exist and pinned baselines match the observed tree (status_files=0, pinned_at=ea0ad7a566ddb51d89297bfcf491636f1fc5dd15).
exit=0

### CMD 2: validate_root_surface_ownership.py
$ python3 tools/validation/validate_root_surface_ownership.py
G2 PASS: surface-ownership register execution/_harness/surface_ownership.yaml is schema-valid (root-surface-ownership/v1); 6 entr(ies) declare write targets; 0 materialized PKG-*/DEL-* child(ren) all registered; decomposition='execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md'.
exit=0

### CMD 3: validate_root_work_graph_dispatch.py
$ python3 tools/validation/validate_root_work_graph_dispatch.py
G3 PASS (CI mode): work graph work_graph.yaml is schema-valid (root-work-graph/v1); 6 node(s), active: none; declared write targets, disjointness/serialization, and M2 markers check out.
exit=0

### PRE-CHECK (before writing root_guards.yaml — the brief requires G1-G4
### observed PASS before any `status: passing` is recorded)
$ python3 tools/validation/validate_instruction_tranche_manifest.py
G4 PASS (CI mode): 2 tranche manifest(s) under docs/governance_harness/tranche_manifests are schema-valid (instruction-tranche-manifest/v1); declared tranches: ['ROOT-LANE-B-20260725', 'ROOT-STEP8-ACCEPT-20260725'].
exit=0

### --- execution/_harness/root_guards.yaml written here ---

### CMD 4: validate_root_materialization_fence.py
$ python3 tools/validation/validate_root_materialization_fence.py
G0 PASS: no PKG-*/DEL-* direct children under root execution/; fence idle (D-GOV-21 gate not yet in play).
exit=0

### CMD 5: validate_instruction_tranche_manifest.py
$ python3 tools/validation/validate_instruction_tranche_manifest.py
G4 PASS (CI mode): 2 tranche manifest(s) under docs/governance_harness/tranche_manifests are schema-valid (instruction-tranche-manifest/v1); declared tranches: ['ROOT-LANE-B-20260725', 'ROOT-STEP8-ACCEPT-20260725'].
exit=0

### CMD 6: pytest tools/validation -q
$ python3 -m pytest tools/validation -q
........................................................................ [ 30%]
........................................................................ [ 61%]
........................................................................ [ 92%]
.................                                                        [100%]
233 passed in 1.78s
exit=0

### CMD 7: validate_path_anchors.py
$ python3 tools/validation/validate_path_anchors.py
PASS: no literal home-dir absolute paths found in 996 live path-anchor surfaces
exit=0

### CMD 8: git status --porcelain
$ git status --porcelain -uall
 M docs/governance_harness/_DECISIONS/_REGISTER.md
 M execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md
?? docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md
?? docs/governance_harness/tranche_manifests/ROOT-STEP8-ACCEPT-20260725.yaml
?? execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/briefs/PROJECT-SETUP-BRIEF.md
?? execution/_harness/adapter.yaml
?? execution/_harness/root_guards.yaml
?? execution/_harness/surface_ownership.yaml
?? execution/_harness/work_graph.yaml
exit=0
```

**G0's PASS is the expected code path (confirmed against source).**
`validate_root_materialization_fence.py::check` returns PASS at its first
branch when `materialized_children(root)` is empty — it never reads
`root_guards.yaml` in that condition. So this run's `root_guards.yaml` is
*written but not yet exercised* by G0; it becomes load-bearing at step 9, when
the first `execution/PKG-*` directory appears and G0's second branch reads the
`registered`/`status` fields. The `N2_RETURN` claim is therefore "G0 idle-PASS
with the registration surface in place", not "G0 verified the registration".

**No validator BLOCKed at any point.** No validator was edited, and none
appeared defective. Nothing was fixed-and-rerun; each command above is a first
and only run against the state as written.

### Note on CMD 8 — this worktree is shared

Six paths appear in `git status` that are **not** mine. Per the run brief, a
sibling agent is concurrently working in this same worktree
(ruling-application edits and the D-GOV-25 acceptance record). The four files
attributable to this node are exactly:

```
execution/_harness/adapter.yaml
execution/_harness/root_guards.yaml
execution/_harness/surface_ownership.yaml
execution/_harness/work_graph.yaml
```

The other entries — `_REGISTER.md`, the decomposition working surface,
`D-GOV-25_root_decomposition_acceptance.md`, the
`ROOT-STEP8-ACCEPT-20260725.yaml` tranche manifest, and Agent 0's own brief —
are the sibling's and Agent 0's writes. The brief's expectation of "exactly
the four files + your return" is met **for this node's write scope**; the
literal one-line `git status` cannot show that in a shared worktree, so it is
recorded here rather than glossed. (`ROOT-STEP8-ACCEPT-20260725.yaml` appeared
between my first directory listing and the G4 pre-check, which is how I know
the sibling was writing concurrently.)

---

## 4. Constraint confirmations

| Constraint (brief) | Status |
|---|---|
| Write scope = the four state files + this return | **Held.** Nothing else written or modified. |
| No `PKG-*` / `DEL-*` directories created | **Held.** `execution/` has no `PKG-*`/`DEL-*` child; G0 confirms. |
| No instruction-surface writes | **Held.** Nothing written under `AGENTS.md`, `agents/`, `skills/`, `tools/`, `docs/`, `init/`, `.github/workflows/`. No M2 tranche manifest was needed or added for this node. |
| No `INIT.md`, no scaffolding | **Held.** This was a bounded root-specific setup act, not a workspace initialization. |
| No commits, no branches, no push | **Held.** Working tree left dirty for the parent. |
| Machine-absolute paths prohibited | **Held.** All declared paths repo-relative POSIX; CMD 7 confirms across 996 surfaces. |
| YAML via plain text / safe_dump semantics | **Held.** Hand-written plain YAML; every file parses under `yaml.safe_load` (each validator did so successfully). |
| Pointer targets verified to exist before use | **Held.** `docs/PRD_ROOT.md`, `execution/_Coordination/CURRENT_WORKPLAN.md`, `docs/governance_harness/_DECISIONS/_REGISTER.md`, `execution/`, and the decomposition file were each checked on disk before being declared; none were missing, so the STOP-and-report path was not taken. |
| `baselines.status_files` equals actual glob count | **Held.** Independently counted (0) and cross-checked by G1. |
| `root_guards.yaml` written only after G1–G4 observed PASS | **Held.** See the pre-check placement in §3. |
| No writes under `execution/_Decomposition/` | **Held.** Read-only. The sibling's concurrent edits there did not change any PKG identifier string; G2's literal-containment check passed against the file as it stood at CMD 2. |
| Fix state, never validators | **Held vacuously** — no BLOCK occurred; `tools/` untouched. |

---

## 5. Open items and hand-back notes

1. **Practitioner-harness adoption of the root adapter remains separately
   gated.** `tools/practitioner_harness/harness.py` resolves projects through a
   hardcoded alias table that does not contain the root, and
   `adapter_loader.py` does not know the `execution/_harness/` relpath. G1's
   own docstring records this as "a recorded open item for root Project Setup,
   not a claim this guard makes". This run did **not** touch it: the alias
   table is instruction surface (`tools/`) and outside this brief's write
   scope. Consequence: the root adapter is schema-valid and CI-checked, but
   `harness.py drift` cannot yet be run against the root product. Requires its
   own M2-gated tranche.
2. **`root_guards.yaml` is written but not yet exercised** (see §3). Its first
   real evaluation is at step 9. Whoever performs materialization should re-run
   G0 immediately after the first `execution/PKG-*` directory exists — that is
   the first moment the registration is load-bearing, and the first moment G1's
   and G2's "absent while structure exists → BLOCK" branches could fire.
3. **G2/G3 state is package-level only.** DEL-level register entries and any
   deliverable-level work-graph nodes are added at materialization, per the
   brief. Until then, a dispatch-mode G3 run naming a deliverable brief will
   BLOCK with "node … is not a node of the accepted work graph" — correct
   behavior, not a defect.
4. **The work graph declares no ordering** (C-2). If the owner intends any
   inter-package sequencing, it must be added to the accepted decomposition
   first and then mirrored here; it must not be introduced by editing
   `work_graph.yaml` alone, since G3's basis pin would then no longer describe
   the graph's provenance.
5. **`accepted_basis` pins `ea0ad7a…`.** The guards do not verify SHA
   reachability (offline / shallow-clone-safe by design), so the pin's
   correctness rests on the brief's record of the D-GOV-25 acceptance, which
   this node accepted as given rather than independently confirmed against git
   history.
6. **Shared-worktree caveat** (§3 note). If the parent expects a clean
   attribution boundary at commit time, the four `execution/_harness/` files
   should be staged explicitly rather than by `git add -A`.
