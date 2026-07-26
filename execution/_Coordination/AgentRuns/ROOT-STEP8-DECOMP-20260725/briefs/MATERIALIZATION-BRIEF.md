# Sealed Brief — M1: Step-9 materialization (ROOT-STEP8-DECOMP-20260725 continuation)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: the N2 PROJECT_SETUP
Agent 1 instance (continuation — guard-state context intact), `opus-5`. One
objective; no delegation; terminal return.

## Authorization

Owner direction, in-session, 2026-07-25: "Merge PR #348 then proceed with
Step 9." PR #348 is merged; EffectiveSHA of the acceptance-application
tranche is `653fabc9b3e8abf369f5e776a7d3ee24bf235e7a` (current
`origin/main`, this branch's base). D-GOV-21 §6 step 9: "Materialize
`PKG-*`/`DEL-*` under root `execution/` from that accepted decomposition
only, with G0–G4 passing." The accepted decomposition is
`execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
(D-GOV-25): 6 packages, 45 deliverables. This is the first time G0's fence
becomes load-bearing — your verification is the evidence that it works with
real structure.

## Objective

Materialize ALL 6 packages and ALL 45 deliverables under root `execution/`,
exactly as named in the accepted decomposition (IDs verbatim — no renames,
no additions, no omissions), per `docs/SPEC.md` §1:

1. Per package `execution/<PKG-ID>_{Label}/` (the accepted full IDs already
   include the label): subfolder set per SPEC §1 — `0_References/` (+
   `_Archive/`), `1_Working/` (+ `_Archive/`), `2_Checking/From/`,
   `2_Checking/To/`, `3_Issued/` (+ `_Archive/`). Inspect how the existing
   project working roots keep empty folders tracked (e.g. `.gitkeep` under
   `projects/chirality-app-dev/execution/`) and match that convention
   exactly.
2. Per deliverable `1_Working/<DEL-ID>_{Label}/` with the four SPEC-required
   files, at lifecycle state **OPEN** (scaffolded, not initialized):
   - `_STATUS.md` — canonical state file, `prose-bullet-v1`-parseable
     (match the field/heading shape of the app-dev precedent:
     `# Status: DEL-XX-YY`, `**Current State:** OPEN`,
     `**Last Updated:** 2026-07-25`, an Authorization Basis line citing
     D-GOV-25 + the owner's step-9 direction, empty `## Remaining`, and a
     `## History` line `2026-07-25 - State set to OPEN (PROJECT_SETUP,
     step-9 materialization, D-GOV-25)`).
   - `_CONTEXT.md` — header fields matching the accepted decomposition for
     that deliverable (read `agents/AGENT_PREPARATION.md` and SPEC §2 for
     the required fields; populate from the deliverable register:
     DeliverableID, name, parent package, Type, ContextEnvelope,
     CoversScopeItems, SupportsObjectives, AnticipatedArtifacts; mark
     anything the decomposition leaves TBD as TBD — never invent).
   - `_DEPENDENCIES.md` — deliverable-local dependency register skeleton
     (K-DEP-1) per PREPARATION/SPEC conventions; no dependencies invented —
     the accepted decomposition declares no inter-package ordering; leave
     declared-empty with the schema in place.
   - `_REFERENCES.md` — skeleton pointing at the accepted decomposition
     (path + working-surface section) as the deliverable's source of scope.
3. Update `execution/_harness/adapter.yaml` **baselines only**:
   `status_files: 45` (must equal the actual post-materialization glob
   count — verify), `pinned_at: 653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`.
   Touch nothing else in `execution/_harness/` — the ownership register
   already covers the package trees (G2 registers direct children only;
   DEL-level entries were deliberately deferred, and materialization does
   not require them — confirm against the validator, and report rather
   than modify the register if you find otherwise).

## Constraints

- Write scope: NEW `execution/PKG-*` trees exactly as specified; the
  baselines edit in `execution/_harness/adapter.yaml`; terminal return at
  `execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/returns/M1_RETURN_RAW.md`.
  Nothing else. No instruction-surface writes, no `_Decomposition/` edits,
  no work-graph changes (nodes stay `pending` — materialization dispatches
  no work), no commits, no branches.
- IDs and labels byte-identical to the accepted decomposition's
  `PKG-XX_{Label}` / `DEL-XX-YY_{Label}` strings.
- Machine-absolute paths prohibited in all written files.
- State OPEN only. No SOW_V1 production documents, no INITIALIZED claims —
  initialization is later, per-deliverable, gated work.

## Verification (run all; report verbatim; every exit code)

1. `python3 tools/validation/validate_root_materialization_fence.py` —
   G0's **second branch** now executes (children exist → registration
   read). Confirm from output/source that the registration was actually
   read and satisfied — this is the fence's first real exercise.
2. G1 (adapter: recount must match 45), G2 (6 direct children all
   registered), G3 (CI mode), G4 (CI mode) — all PASS.
3. `python3 -m pytest tools/validation -q` and
   `python3 -m pytest tools/practitioner_harness -q` — all pass. NOTE:
   G0's test suite includes `test_live_repo_state_is_clean`, which asserts
   the live repo has no materialized children — with step 9 executed that
   test's premise changes. If it fails, STOP, do not modify the test, and
   report the failure with the test's source lines — Agent 0 will
   disposition it (a test asserting a pre-step-9 world is expected to need
   a governed update in this tranche; that update is Agent 0's to stage,
   not yours).
4. `python3 tools/validation/validate_path_anchors.py` — PASS.
5. `ls` count checks: 6 `execution/PKG-*` dirs; 45 `_STATUS.md` files
   matching the adapter glob; per-package DEL counts 8/5/6/10/8/8.
6. `git status --porcelain` — writes exactly in scope.

## Terminal return (`M1_RETURN_RAW.md`, and return the same content)

Tree summary (per package: DEL count, files per DEL); the exact `_STATUS.md`
/ `_CONTEXT.md` template instantiated (one example inlined); adapter diff;
full verification transcript including the G0 second-branch evidence and
the disposition-needed test result if any; constraint confirmations; open
items.
