# Guard-state instantiation spec (Agent 0 context assembly, step 8)

Run: ROOT-STEP8-DECOMP-20260725 · Date: 2026-07-25
Source: read-only survey of `tools/validation/validate_root_*.py`,
`validate_instruction_tranche_manifest.py`, their test suites, and the
practitioner-harness loader, at basis `24726a73c` (post-PR-#346 `main`).
This file is derivative evidence; on any disagreement the validator sources
govern.

## What root Project Setup must instantiate (packet §6 step 8, §5.3)

All four state files are attributed to root Project Setup by the validator
docstrings ("written by root Project Setup, never by this tranche"), even
though the packet's step-8 sentence names only the G2 register and the work
graph explicitly. Recorded as a textual gap, not a conflict: G0's and G1's
docstrings each attribute their surface to root Project Setup as well.

1. `execution/_harness/root_guards.yaml` — G0's registration surface.
   Top-level `guards:` mapping with entries `G1`–`G4`, each at minimum
   `registered: true` + `status: passing` (G0 checks exactly those two
   fields; G0 requires no entry for itself). Each guard's docstring
   specifies the fuller entry it expects (validator, tests, state_surface,
   schema, and for G3/G4 the dispatch/diff mode strings) — write the full
   entries.
2. `execution/_harness/adapter.yaml` — schema `root-harness-adapter/v1`.
   Required keys: schema, product, working_root ("." required),
   execution_root ("execution" required), prd, coordination,
   decision_register, status_glob, states, parser_dialect, baselines
   {status_files, status_mismatch, pinned_at (7–40 hex SHA)}; optional
   exclude_globs. Pointer paths must exist on disk. `baselines.status_files`
   is cross-checked against the actual on-disk glob count (0 before
   materialization). NOTE: root's `_STATUS.md` pointer paths — pick
   status_glob to match root SPEC layout `execution/PKG-*/1_Working/DEL-*/_STATUS.md`.
3. `execution/_harness/surface_ownership.yaml` — schema
   `root-surface-ownership/v1`. `decomposition:` must point at the accepted
   root decomposition (repo-relative, must exist); once non-TBD, EVERY
   entry's `decomposition_ref` must be non-TBD and appear **literally as a
   substring** of the decomposition file text. Entries: id (PKG-*/DEL-*),
   kind, write_targets (must cover `execution/<id>/`), instruction_surface
   flag (true iff targets intersect AGENTS.md, agents/, skills/, tools/,
   docs/, init/, .github/workflows/ — M2), serialization.
4. `execution/_harness/work_graph.yaml` — schema `root-work-graph/v1`.
   `accepted_basis:` = the M3 frozen instruction basis SHA. Nodes: id,
   status ∈ {active,pending,complete,blocked}, write_targets (required for
   non-complete nodes), depends_on / serialized_after (no cycles — BLOCK),
   owner (must be a G2 entry id with covering targets once the register
   exists), m2_marker `M2:<manifest path>` required where targets intersect
   the instruction surface (path must exist).

## Lawfulness of pre-materialization instantiation

Confirmed lawful under every guard: G0 passes idle whenever no `PKG-*`/`DEL-*`
children exist (never reads the registration in that case); G1/G2 full-validate
a present state file regardless of materialization (G2 has an explicit test:
register present, no structure, PASS); G3 CI mode keys only on file presence;
G4 keys on neither. Step 8 (state) strictly before step 9 (materialization) is
the intended order.

## Implications adopted for this lane

- The decomposition surface must be a stable, committed, repo-relative file
  whose entry identifiers appear verbatim (G2 literal-containment check).
- The first accepted work graph's `accepted_basis` is the merge SHA of the
  tranche that accepts the decomposition (recorded at instantiation, not
  invented).
- Practitioner-harness adoption of the root adapter (PROJECT_ALIASES /
  loader relpath) remains a separately-authorized open item — NOT part of
  step 8. `execution/_harness/adapter.yaml` uses `root-harness-adapter/v1`,
  not the projects' `practitioner-harness-adapter/v1`.
- G4's manifest directory already passes CI-mode (Lane B manifest present);
  the step-8 tranche adds its own manifest only if it touches instruction
  surfaces (root `docs/` is instruction surface — a decomposition candidate
  under `execution/_Coordination/` is NOT; the later decision record under
  `docs/governance_harness/` IS).
