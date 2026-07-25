# Sealed Brief — N1: Guard capability G1–G4 (ROOT-LANE-B-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: ephemeral bounded
Agent 2 generalist, `opus-5`. One objective; no delegation; terminal return.

## Objective

Implement and validate the deterministic guard **capability** — validator
code, tests, and CI wiring — for guards G1–G4 exactly as specified in
D-GOV-21 packet §5.3 (`docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md`,
read §5.2–§5.3 and §6–§7 first), per D-GOV-21 §6 step 6 and the Lane B
section of `execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`.

**Capability vs state (critical).** Lane B ships capability only. Guard
*state* — the G1 adapter registration, the G2 ownership register, the first
accepted work graph G3 checks, and `execution/_harness/root_guards.yaml`
registration entries — is instantiated later by root Project Setup (gated
downstream). Every guard must therefore be **PASS-idle** on the current
clean tree: absent state surfaces are the lawful pre-instantiation
condition, reported as idle PASS with a clear message, following the G0
bootstrap-semantics precedent (`tools/validation/validate_root_materialization_fence.py`
— study it and match its conventions: stdlib-only if achievable, exit 0
PASS / exit 1 BLOCK per D-GOV-02, message prefixes naming the guard).

## The four guards (packet §5.3 verbatim scope)

1. **G1 — Root harness adapter** (`validate_root_harness_adapter.py`).
   Validates root `execution/_harness/adapter.yaml` (or equivalent — study
   how project working roots register harness adapters and pinned
   baselines under `projects/*/execution/_harness/` or the practitioner
   harness's adapter model, and design the root registration to give root
   `execution/` the same deterministic status/drift surface; record your
   design in the file's docstring). Absent → PASS idle. Present →
   schema-valid with pinned baselines, BLOCK on malformation or baseline
   drift claims that fail verification.
2. **G2 — Static surface-ownership validator**
   (`validate_root_surface_ownership.py`). Register instantiated later by
   Project Setup; you define its schema and location (recommend
   `execution/_harness/surface_ownership.yaml`) in the validator docstring.
   Idle rules: no `PKG-*`/`DEL-*` and no register → PASS idle; structure
   exists without register → BLOCK; register present → BLOCK on undeclared
   write targets, unregistered materialized packages, or
   register/decomposition mismatch (decomposition pointer field may be
   `TBD` until an accepted root decomposition exists — validate what is
   declared, never infer). Static facts only; no concurrency claims.
3. **G3 — Pre-dispatch work-graph check**
   (`validate_root_work_graph_dispatch.py`). Two modes: CI mode (no
   dispatch state → PASS idle; if a work-graph surface you define exists,
   validate its internal consistency) and dispatch mode (explicit
   arguments naming the work graph and run briefs) verifying: each active
   node's write targets declared; concurrently active nodes' targets
   disjoint or serialized per M1; instruction-surface intersection carries
   the M2 marker (you define the marker convention; document it).
4. **G4 — Instruction-surface tranche manifest check**
   (`validate_instruction_tranche_manifest.py`). Define the tranche
   manifest format and location (recommend
   `docs/governance_harness/tranche_manifests/`). CI mode: every manifest
   present is schema-valid; **the manifest for THIS Lane B tranche must
   exist and pass** (the G4 discipline applied to itself — author it:
   touched instruction-surface paths, the M2 gate record naming the
   owner's "proceed with Lane B" direction and the human-gated PR, and the
   M6 notice disposition, which Agent 0 will complete at fan-in). Diff
   mode (explicit base..head): verify manifest path coverage of the actual
   instruction-surface diff. Checks recorded provenance; **never infers
   origin from diffs**.

## Also required

- **Tests** per guard (`test_validate_*.py`, pytest, tmp-tree fixtures
  like G0's suite): idle-PASS, BLOCK, and PASS-with-state cases; plus a
  live-repo-clean test only where G0's suite has one (its scratch
  sensitivity is intended — see the preflight report).
- **CI wiring**: append steps to `.github/workflows/governance-harness.yml`
  after the G0 step, same style (test suite then validator; BLOCK fails
  the run). CI must stay green on the clean tree.
- **Registration-surface consistency**: G0 reads
  `execution/_harness/root_guards.yaml` expecting G1–G4
  `registered: true` + `status: passing`. Your guards' names/IDs must
  match what G0 expects, and each validator must state in its docstring
  what its registration entry will assert. Do not create
  `root_guards.yaml` — that is Project Setup's act.

## Inputs

- Preflight evidence: `../evidence/PREFLIGHT_REPORT.md` (the §5.1 finding:
  only G0 detects root materialization; your guards close the rest).
- G0 source + tests (conventions to match); D-GOV-02 severity semantics;
  `AGENTS.md` §Governance Integration Rules; the adopted PRD
  `docs/PRD_ROOT.md` §5.2 O-9 and §6.2 for context.

## Constraints

- Write scope: NEW files under `tools/validation/`, edits to
  `.github/workflows/governance-harness.yml`, the Lane B tranche manifest
  at your defined location, and your terminal return. Nothing else — no
  `execution/` writes, no `PKG-*`/`DEL-*`, no other instruction files.
- Python 3 stdlib + pyyaml only (CI installs pyyaml; G0 precedent).
- Machine-absolute paths prohibited in all files.
- Run before returning: your four test suites; all four validators
  (expect PASS idle); `python3 -m pytest tools/validation -q`;
  `python3 -m pytest tools/practitioner_harness -q`;
  `python3 tools/validation/validate_path_anchors.py`;
  `python3 tools/validation/validate_root_materialization_fence.py`.
  Report every result honestly; flag any you cannot run.
- Do not commit; leave changes in the working tree for Agent 0 fan-in.

## Terminal return (write to `../returns/N1_RETURN_RAW.md` and return the same content)

Files created/modified; per-guard design decisions (state surface, schema,
idle semantics, registration entry, marker/manifest conventions);
verification results (every command + outcome); constraint confirmations;
open items for Project Setup instantiation.
