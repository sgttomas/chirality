# Sealed Brief — N2: Root Project Setup — guard-state instantiation (ROOT-STEP8-DECOMP-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: Agent 1 instance in
the **PROJECT_SETUP** role, `opus-5`. One objective; no delegation; terminal
return.

## Authorization and context

The first root decomposition is ACCEPTED by owner ruling (2026-07-25;
AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`; EffectiveSHA
`ea0ad7a566ddb51d89297bfcf491636f1fc5dd15`, merge of PR #347; decision record
D-GOV-25, authored in this tranche). D-GOV-21 §6 step 8's second act is
released: root Project Setup instantiates guard STATE so guards G0–G4 flip
from idle to PASS-with-state. Read first:

- `../evidence/GUARD_STATE_SPEC.md` (extracted schemas — but the validator
  sources govern; read each validator docstring yourself:
  `tools/validation/validate_root_materialization_fence.py` (G0),
  `validate_root_harness_adapter.py` (G1),
  `validate_root_surface_ownership.py` (G2),
  `validate_root_work_graph_dispatch.py` (G3),
  `validate_instruction_tranche_manifest.py` (G4))
- The accepted decomposition:
  `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
  (6 packages PKG-01..PKG-06, 45 deliverables)
- `agents/AGENT_PROJECT_SETUP.md` (your role file; this brief is a bounded
  root-specific setup act, not a full project workspace initialization —
  no INIT.md, no scaffolding, no PKG/DEL folders)

## Objective — write exactly four files under `execution/_harness/` (new dir)

1. `execution/_harness/adapter.yaml` — schema `root-harness-adapter/v1`,
   all required keys per G1. Values: product `chirality-root`;
   working_root `.`; execution_root `execution`; prd `docs/PRD_ROOT.md`;
   coordination `execution/_Coordination/CURRENT_WORKPLAN.md`;
   decision_register `docs/governance_harness/_DECISIONS/_REGISTER.md`
   (root decisions live there — verify paths exist; if a pointer target is
   missing, STOP and report rather than substituting);
   status_glob `execution/PKG-*/1_Working/DEL-*/_STATUS.md`; states — use
   the canonical lifecycle states from `docs/SPEC.md` §3 (read them; do
   not invent); parser_dialect `prose-bullet-v1`; exclude_globs
   `[".archive/**"]`; baselines: status_files 0 (must equal the actual
   on-disk glob count — verify), status_mismatch 0, pinned_at
   `ea0ad7a566ddb51d89297bfcf491636f1fc5dd15`.
2. `execution/_harness/surface_ownership.yaml` — schema
   `root-surface-ownership/v1`; decomposition:
   `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`; six
   entries, one per accepted package PKG-01..PKG-06 (kind `package`;
   decomposition_ref = the exact package ID string as it appears in the
   working surface — G2 checks literal containment; write_targets
   `execution/<full-package-id>/**` covering each entry's own tree;
   instruction_surface false — no package's write target intersects the
   instruction surface at instantiation; serialization null). DEL-level
   entries are added at materialization time, not now.
3. `execution/_harness/work_graph.yaml` — schema `root-work-graph/v1`;
   accepted_basis `ea0ad7a566ddb51d89297bfcf491636f1fc5dd15`; the first
   accepted work graph: six nodes, one per package (id = the package ID;
   status `pending` — nothing is dispatched; owner = the matching G2
   register entry id; write_targets identical to that entry's targets;
   no depends_on unless the accepted decomposition's downstream execution
   notes state ordering — read them and mirror only what is declared,
   never infer; no m2_marker needed while no node's targets intersect the
   instruction surface).
4. `execution/_harness/root_guards.yaml` — `guards:` mapping with the FULL
   registration entries G1–G4 exactly as each validator's docstring
   specifies (validator, tests, state_surface, schema, plus G3's
   dispatch_mode and G4's diff_mode strings), each `registered: true`,
   `status: passing` — written ONLY after you have run G1–G4 and observed
   PASS against the state you wrote.

## Constraints

- Write scope: the four files above + your terminal return at
  `execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/returns/N2_RETURN_RAW.md`.
  Nothing else. No PKG-*/DEL-* directories, no instruction-surface writes,
  no INIT.md, no commits, no branches.
- Machine-absolute paths prohibited. YAML via plain text or safe_dump
  semantics; keys and values exactly as the validators require.
- Verification (run in this order, report every command + exit code +
  output verbatim):
  1. `python3 tools/validation/validate_root_harness_adapter.py` → PASS
  2. `python3 tools/validation/validate_root_surface_ownership.py` → PASS
  3. `python3 tools/validation/validate_root_work_graph_dispatch.py` → PASS
  4. then write `root_guards.yaml`, then
     `python3 tools/validation/validate_root_materialization_fence.py`
     → PASS (idle — no PKG/DEL structure exists; confirm that is the
     expected code path)
  5. `python3 tools/validation/validate_instruction_tranche_manifest.py`
     → PASS
  6. `python3 -m pytest tools/validation -q` → all pass
  7. `python3 tools/validation/validate_path_anchors.py` → PASS
  8. `git status --porcelain` → exactly the four files + your return
- If ANY validator BLOCKs on your state, fix the state (never the
  validator) and re-run; if a validator appears defective against ruled
  content, STOP and report — do not modify tools.

## Terminal return (`N2_RETURN_RAW.md`, and return the same content)

Files written with their full content inlined; every design choice that
was yours (states list, ordering edges, anything the brief left to
inspection) with its source cited; the full verification transcript;
constraint confirmations; open items (e.g., practitioner-harness adoption
of the root adapter remains separately gated).
