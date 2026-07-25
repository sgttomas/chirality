# N1 Terminal Return (raw) — Guard capability G1–G4 (ROOT-LANE-B-20260725)

Executor: ephemeral bounded Agent 2 generalist, `opus-5`. Sealed brief:
`briefs/GUARD-CAPABILITY-BRIEF.md`. Basis: `main@ba2b80bf25b6`, branch
`claude/root-lane-b-guards`. Status: **COMPLETE as a candidate; not committed**
— all changes left in the working tree for Agent 0 fan-in (V1).

## 1. Files created / modified

Created (new, under `tools/validation/`):

| Path | Purpose |
|---|---|
| `tools/validation/validate_root_harness_adapter.py` | G1 validator |
| `tools/validation/test_validate_root_harness_adapter.py` | G1 tests (18) |
| `tools/validation/validate_root_surface_ownership.py` | G2 validator |
| `tools/validation/test_validate_root_surface_ownership.py` | G2 tests (21) |
| `tools/validation/validate_root_work_graph_dispatch.py` | G3 validator |
| `tools/validation/test_validate_root_work_graph_dispatch.py` | G3 tests (34) |
| `tools/validation/validate_instruction_tranche_manifest.py` | G4 validator |
| `tools/validation/test_validate_instruction_tranche_manifest.py` | G4 tests (27) |

Created (tranche manifest, at the location G4 defines):

- `docs/governance_harness/tranche_manifests/ROOT-LANE-B-20260725.yaml`

Modified:

- `.github/workflows/governance-harness.yml` — four steps appended after the
  G0 step, same style (test suite then validator; BLOCK fails the run per
  D-GOV-02). Workflow now has 11 steps and parses as YAML.

Nothing else was written. `git status --porcelain` shows exactly these plus the
pre-existing untracked `execution/_Coordination/AgentRuns/ROOT-LANE-B-20260725/`
run-record directory (this return file).

## 2. Per-guard design decisions

Conventions common to all four (matched to G0,
`validate_root_materialization_fence.py`): stdlib-only import surface with
PyYAML imported lazily and only when a state surface actually exists; a
module-level `check(root, ...) -> (exit_code, lines)` for tmp-tree testability;
`repo_root()` via `git rev-parse --show-toplevel`; message prefixes naming the
guard (`G1 PASS:` / `G2 BLOCK:` / …); exit 0 PASS, exit 1 BLOCK. Each guard is
self-contained (no shared helper module) so each is independently runnable and
independently registrable, matching how `tools/validation/` is written.

**Deviation from G0 to record:** exit **2** is used for genuine operational
errors — PyYAML unimportable while a state surface exists, an unresolvable git
ref, a missing named file in an explicit-argument mode, or half-specified CLI
arguments — per D-GOV-02's newest-validator-class convention (exit 0/1/2) and
its "the tool asserts nothing when it cannot observe" posture. G0 uses only
0/1 because it never needs the distinction. Exit 2 still fails CI, so the gate
semantics are unchanged. Malformed-but-readable YAML is BLOCK (exit 1), not
operational: the surface exists and is objectively invalid.

### G1 — `validate_root_harness_adapter.py`

- **State surface:** `execution/_harness/adapter.yaml`. **Schema:**
  `root-harness-adapter/v1`.
- **Why there, not `{REPO_ROOT}/_harness/adapter.yaml`** (the literal project
  convention, since the root product's `WORKING_ROOT` == `REPO_ROOT`): it
  co-locates with G0's `execution/_harness/root_guards.yaml` so the root
  working root has one harness control directory; root `execution/` is outside
  the public-export boundary (packet §4) whereas a new top-level `_harness/`
  would sit beside the exported instruction surface; and the practitioner
  harness resolves projects through a hardcoded alias table in
  `tools/practitioner_harness/harness.py` that the root is not in — editing it
  is outside this tranche's write scope. Full rationale is in the file's
  docstring ("Design of record").
- **Schema shape:** key-compatible with `practitioner-harness-adapter/v1` where
  the keys carry the same meaning (`coordination`, `decision_register`,
  `status_glob`, `states`, `parser_dialect`, `exclude_globs`) and different
  where root reality differs — `prd` replaces `plan`; `working_root` (must be
  `.`) and `execution_root` (must be `execution`) are declared explicitly;
  pinned baselines are nested under `baselines` with `status_files`,
  `status_mismatch`, `pinned_at` (7–40 hex SHA), and an optional
  `mismatch_disposition`.
- **Pinned-baseline verification:** `baselines.status_files` must equal the
  observed count of files matching `status_glob` under the checkout after
  `exclude_globs` — a declared baseline that does not match the tree is
  reported as `pinned baseline drift` and BLOCKs. A nonzero
  `status_mismatch` requires a recorded `mismatch_disposition`. Mismatch
  *counting* is explicitly out of the observation boundary (that is the
  practitioner harness's `_STATUS.md` parse), and so is SHA reachability
  (offline / shallow-clone-safe).
- **Idle semantics:** adapter absent **and** no `PKG-*`/`DEL-*` under root
  `execution/` → PASS idle.
- **Scope choice beyond the brief's literal text, flagged for review:** the
  brief says "Absent → PASS idle". Implemented as absent → PASS idle *unless*
  `PKG-*`/`DEL-*` structure exists, in which case absent → BLOCK. Rationale:
  materialized root structure with no adapter has no status/drift surface at
  all, which is exactly the condition §5.3 has G1 prevent; it mirrors G2's
  ruled idle rule ("structure exists without register → BLOCK"); and it cannot
  fire before materialization, which G0 independently gates. Agent 0 may
  direct removal if this reads as over-reach.

### G2 — `validate_root_surface_ownership.py`

- **State surface:** `execution/_harness/surface_ownership.yaml`. **Schema:**
  `root-surface-ownership/v1`. Top-level `decomposition` (a repo-relative path
  or `TBD`) plus `entries[]` of `{id, kind, decomposition_ref, write_targets,
  instruction_surface, serialization}`.
- **Idle semantics (as ruled in the brief):** no `PKG-*`/`DEL-*` and no
  register → PASS idle; structure exists without register → BLOCK; register
  present → validated even with no structure.
- **BLOCK conditions:** unknown/malformed schema; non-`PKG-*`/`DEL-*` id;
  unknown `kind`; duplicate entry; absolute or `..`-escaping write target;
  **undeclared write target** (no declared target covers the entry's own
  `execution/<id>/` tree); **unregistered materialized package** (an
  `execution/PKG-*`/`DEL-*` child with no entry); an instruction-surface
  intersecting target without `instruction_surface: true`;
  **register/decomposition mismatch**.
- **Register/decomposition mismatch, validated only as declared:** while
  `decomposition: TBD`, `decomposition_ref: TBD` is lawful. Once
  `decomposition` names a path, the path must exist, every entry must carry a
  non-TBD ref, and each ref must appear **literally** in that surface. No
  structural parse of a decomposition format that does not yet exist — deeper
  cross-checking is a recorded open item, not a silent claim.
- **Static facts only:** overlapping write targets between entries are
  reported as INFO with an explicit statement that the guard makes **no
  concurrency claim** (serialization is G3's question). This is tested
  (`test_overlapping_targets_are_info_not_block`).

### G3 — `validate_root_work_graph_dispatch.py`

- **State surface:** `execution/_harness/work_graph.yaml`. **Schema:**
  `root-work-graph/v1`, with `accepted_basis` (M3 frozen instruction basis, a
  7–40 hex SHA) and `nodes[]` of `{id, status, owner?, write_targets,
  depends_on?, serialized_after?, integration_owner?, m2_marker?}`.
- **M2 marker convention (defined by this guard, documented in its
  docstring):** the string field `m2_marker`, value `M2:<repo-relative path>`
  naming the G4 tranche manifest that records the M2 gate. Required on any
  node — and any run brief — whose declared write targets intersect the
  instruction surface; the named path must exist. The marker records that a
  gate was taken and grants nothing (K-AUTH-1), stated in the message text.
- **CI mode** (no args): absent surface → PASS idle. Present → internal
  consistency: schema, `accepted_basis`, unique ids, known statuses,
  resolvable `depends_on`/`serialized_after`, **no dependency cycle**,
  declared repo-relative write targets on every non-`complete` node,
  active-node pairwise disjointness-or-serialization, and M2 markers. A cycle
  BLOCKs with a message pointing at the `AGENTS.md` cycle-resolution rule
  (recorded move required); the guard never linearizes a cycle.
- **M1 serialization test:** an overlap between two `active` nodes is
  permitted when either declares the other in `serialized_after`/`depends_on`,
  or both declare the same non-empty `integration_owner` (the "one declared
  integration owner" limb). Overlap is computed conservatively on literal path
  prefixes with path-boundary awareness.
- **Register tie-in:** when the G2 register exists, a node declaring `owner`
  must name a register entry and its targets must be covered by that entry.
  When the register is absent the cross-check is reported
  `NOT_APPLICABLE (skipped, not assumed)` — never assumed satisfied.
- **Dispatch mode:** `--work-graph PATH --brief PATH [--brief PATH ...]`.
  Adds, per brief: node exists and is `active`; every brief write target is
  covered by the node's declared targets (else `undeclared write target`);
  instruction-surface intersection carries an M2 marker matching the node's. A
  brief is a `.yaml`/`.yml` mapping or a Markdown file whose first block is
  YAML front matter delimited by `---`; a brief with no machine-readable
  dispatch block BLOCKs rather than being guessed at.

### G4 — `validate_instruction_tranche_manifest.py`

- **Manifest format and location (defined by this guard):**
  `docs/governance_harness/tranche_manifests/<TRANCHE_ID>.yaml`, one file per
  tranche, filename stem == `tranche_id`. **Schema:**
  `instruction-tranche-manifest/v1` with `schema`, `tranche_id`, `title`,
  `date`, optional `basis`, `instruction_surface_paths[]`, `m2_gate`
  (`authorization`, `authorized_by`, `authorization_date`,
  `integration_owner`, `merge_gate` — must be `human-gated-pr`, `self_merge` —
  must be `false`), and `m6_notice` (`disposition` ∈ {`pending`, `routed`,
  `none-required`}, `routed_to[]`, `rationale`).
- **CI mode:** the manifest directory must exist and hold at least one
  manifest (an absent or emptied directory BLOCKs — the discipline must not be
  silently emptied), and every manifest present must be schema-valid. This
  tranche's own manifest lives there, so the G4-applied-to-itself requirement
  is enforced by every CI run, and additionally by a live-repo test that
  asserts `ROOT-LANE-B-20260725.yaml` exists and validates.
- **Diff mode:** `--base REF --head REF [--tranche ID]` → `git diff
  --name-only base..head`, filtered to instruction-surface paths, each of which
  must be covered by a declared manifest path.
- **Never infers origin:** `m2_gate` and `m6_notice` are read as recorded
  fields; a diff is used only for coverage, never to attribute authorship or
  to infer authorization. Stated in the docstring and enforced by there being
  no code path from diff content to gate fields.
- **`disposition: pending` PASSes with an INFO note** — the M6 routing decision
  belongs to the accepting agent at fan-in, and the guard records rather than
  pre-empts it. Declared paths are not required to exist (a tranche may delete
  a path). Paths that do not intersect the instruction surface are INFO
  over-declaration, not BLOCK. Unquoted YAML dates (`date: 2026-07-25`, which
  PyYAML parses to a `date` object) and quoted strings are both accepted.

### Instruction-surface definition used by G2/G3/G4

`docs/SPEC.md` §0.2.2's enumeration — `AGENTS.md`, `agents/`, `skills/`,
`tools/`, root `docs/`, `init/` — **plus `.github/workflows/`**, on the named
basis of the Lane B characterization in
`execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`
("G1–G4 touch `tools/`, `.github/workflows/`, and possibly root `docs/` — the
protected instruction surface"). No other additions were made: `CLAUDE.md` is
raised as an open item rather than silently included, because it has no named
basis in the enumeration.

### Registration entries (G0 compatibility)

Guard IDs are exactly `G1`–`G4`, matching `REQUIRED_GUARDS` in
`validate_root_materialization_fence.py`. Each validator's docstring states
verbatim the `execution/_harness/root_guards.yaml` entry it will assert —
`registered: true`, `status: passing` (the two fields G0 checks), plus
`validator`, `tests`, `state_surface`, `schema`, and mode strings as
informational fields G0 ignores. **`root_guards.yaml` was not created**: that
is root Project Setup's act.

## 3. Verification results (every command, honestly reported)

Run in the worktree at `main@ba2b80bf25b6` with the working-tree changes.

| # | Command | Result |
|---|---|---|
| 1 | `pytest tools/validation/test_validate_root_harness_adapter.py -q` | **18 passed**, exit 0 |
| 2 | `pytest tools/validation/test_validate_root_surface_ownership.py -q` | **21 passed**, exit 0 |
| 3 | `pytest tools/validation/test_validate_root_work_graph_dispatch.py -q` | **34 passed**, exit 0 |
| 4 | `pytest tools/validation/test_validate_instruction_tranche_manifest.py -q` | **27 passed**, exit 0 |
| 5 | `python3 tools/validation/validate_root_harness_adapter.py` | **PASS idle**, exit 0 |
| 6 | `python3 tools/validation/validate_root_surface_ownership.py` | **PASS idle**, exit 0 |
| 7 | `python3 tools/validation/validate_root_work_graph_dispatch.py` | **PASS idle**, exit 0 |
| 8 | `python3 tools/validation/validate_instruction_tranche_manifest.py` | **PASS (CI mode)**, exit 0 — 1 manifest, `ROOT-LANE-B-20260725`, + INFO note on `pending` M6 disposition |
| 9 | `python3 -m pytest tools/validation -q` | **233 passed**, exit 0 (was 133 before this tranche) |
| 10 | `python3 -m pytest tools/practitioner_harness -q` | **311 passed**, exit 0 |
| 11 | `python3 tools/validation/validate_path_anchors.py` | **PASS**, exit 0 — 996 live path-anchor surfaces, no home-dir paths |
| 12 | `python3 tools/validation/validate_root_materialization_fence.py` | **G0 PASS**, fence idle, exit 0 |

Additional runs not required by the brief:

| # | Command | Result |
|---|---|---|
| 13 | `python3 tools/practitioner_harness/harness.py self-check` | exit 0; **0 BLOCK** findings (INFO=15, NOT_APPLICABLE=1, REVIEW=3, WARN=22 — the standing baseline) |
| 14 | `validate_skill_metadata.py`, `validate_agent_instructions.py`, `validate_instruction_entrypoints.py` | all exit 0 |
| 15 | `py_compile` on the four validators | OK |
| 16 | G3 dispatch mode, CLI, valid brief (scratchpad fixtures, absolute args) | **PASS (dispatch mode)**, exit 0 |
| 17 | G3 dispatch mode, CLI, brief declaring `tools/validation/sneaky.py` | **BLOCK**, exit 1 — reported both `undeclared write target` and the missing M2 marker |
| 18 | `validate_instruction_tranche_manifest.py --base HEAD~1 --head HEAD` | **BLOCK**, exit 1 (see note below) |

**Note on #18 — read this before wiring diff mode anywhere.** Diff mode
BLOCKs on historical commits (`docs/CONTRACT.md` and the D-GOV-24 decision
record changed in `HEAD~1..HEAD` and are not covered by any manifest) simply
because the manifest discipline begins with this tranche; every earlier
tranche predates it. **Diff mode is therefore deliberately NOT wired into CI**
— only CI mode is. Diff mode is a tool for the integration owner to run
against a specific `base..head` for a tranche that carries a manifest. CI
remains green on the clean tree.

**Nothing in the battery failed.** No result is unreported and no command
could not be run.

### One real bug found and fixed during verification

The first implementation normalized targets with `target.lstrip("./")`, which
strips *every* leading `.` and `/` character and therefore turned
`.github/workflows/...` into `github/workflows/...` — CI wiring silently read
as **not** instruction surface. Caught by the live G4 CI-mode run reporting
`.github/workflows/governance-harness.yml` as over-declaration. Fixed in all
three affected guards with a `normalize_target()` helper that strips only
leading `./` segments, and pinned by a regression test in each of the G2, G3,
and G4 suites.

## 4. Constraint confirmations

- **Write scope held.** Only: eight new files under `tools/validation/`, the
  `.github/workflows/governance-harness.yml` edit, the tranche manifest at
  `docs/governance_harness/tranche_manifests/ROOT-LANE-B-20260725.yaml`, and
  this return. No `execution/` writes outside this run-record directory, no
  `PKG-*`/`DEL-*`, no other instruction file, no `root_guards.yaml`, no
  `tools/REGISTRY.md` edit.
- **Dependencies:** Python 3 stdlib + PyYAML only. PyYAML is imported lazily
  and only when a state surface exists, so all four guards run idle-PASS on a
  stdlib-only interpreter.
- **No machine-absolute paths** in any created or modified file (verified by
  direct grep for `/Users/…`, `/home/…`, `C:\Users\…` across all ten paths,
  and by `validate_path_anchors.py`).
- **Not committed.** All changes left in the working tree on
  `claude/root-lane-b-guards` for Agent 0 fan-in.
- **Capability, not state.** No guard state surface was instantiated.

## 5. Open items for root Project Setup / Agent 0

1. **Instantiate guard state** (Project Setup, packet §6 step 8):
   `execution/_harness/adapter.yaml`, `surface_ownership.yaml`,
   `work_graph.yaml`, and `root_guards.yaml` with the G1–G4 entries each
   validator's docstring specifies. G0 gates materialization on that file.
2. **Practitioner-harness adoption of the root adapter.** The root is not in
   `PROJECT_ALIASES` in `tools/practitioner_harness/harness.py`, and
   `adapter_loader.ADAPTER_RELPATH` is `_harness/adapter.yaml` relative to a
   project root. Giving root `execution/` a *live* `status`/`drift` command
   (rather than only a validated adapter surface) requires a separate,
   separately-authorized change to those two surfaces. G1 asserts nothing
   about this today.
3. **M6 disposition for this tranche.** The manifest records
   `m6_notice.disposition: pending`. Agent 0's pin survey at V1 must set it to
   `routed` (naming each notice path) or `none-required` (with its basis) —
   G4 accepts `pending` but the disposition is not closed until then.
4. **`CLAUDE.md` and the instruction-surface set.** `CLAUDE.md` is the root
   instruction entrypoint (it imports `AGENTS.md`) but is not in the
   `docs/SPEC.md` §0.2.2 enumeration, so it was deliberately excluded from
   G2/G3/G4's surface set. Owner/Agent 0 decision whether to add it (and
   whether `.github/workflows/` should be added to the SPEC enumeration
   itself, rather than resting on the workplan's characterization).
5. **Decomposition cross-check depth (G2).** Once an accepted root
   decomposition format exists, the current literal-string presence test for
   `decomposition_ref` should be upgraded to a structural check.
6. **Tool registry.** `tools/REGISTRY.md` was not updated (outside write
   scope); the four new validators should be registered there in the same
   tranche or an immediately following one.
7. **Diff-mode usage policy (G4).** Decide whether the integration owner runs
   `--base/--head` manually per tranche or whether a future PR-scoped CI job
   should run it against the PR merge base (which would require every future
   instruction-surface PR to carry a manifest — a real policy commitment, not
   made here).
