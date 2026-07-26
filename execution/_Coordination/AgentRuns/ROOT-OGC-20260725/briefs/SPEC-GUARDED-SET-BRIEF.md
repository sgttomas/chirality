# Sealed Brief — S1: SPEC notes + guarded-set enumeration (ROOT-OGC-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: ephemeral bounded
Agent 2 generalist, `opus-5`. One objective; no delegation; terminal return.

## Authorization

Owner ruling 2026-07-25 (verbatim in
`docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md`,
authored this tranche): the four owner-gated issues close by following
Agent 0's recommendations. You execute R1 and R2:

- **R1 (`_Archive/` tracking):** accept the status quo — the dirs exist
  locally, the `.gitignore` `**/_Archive/` policy stands — and add a
  one-line note to `docs/SPEC.md` §1.1 that `_Archive/` subfolders are
  local working state, not tracked repo content.
- **R2 (guarded-set enumeration):** add `.github/workflows/` to the SPEC
  §0.2.2 instruction-surface enumeration (the guards already treat it as
  protected, on the workplan's named basis — this ratifies the enumeration
  in doctrine), and add `CLAUDE.md` to the guards' instruction-surface set
  (it is a live instruction pointer file importing `AGENTS.md`).

## Work

1. `docs/SPEC.md` §1.1: after the required-subfolders table (which lists
   the three `_Archive/` rows), add one sentence noting that `_Archive/`
   subfolders are local working state excluded from version control by the
   repository ignore policy ("Archives are historical/local, not canonical
   repo content") — they exist in a working checkout but are not tracked;
   nothing canonical may live only in an `_Archive/`. Keep it to the
   minimum that resolves the SPEC-vs-gitignore tension; change no
   normative requirement.
2. `docs/SPEC.md` §0.2.2: extend the instruction-surface enumeration with
   `.github/workflows/` and `CLAUDE.md`. Read the section first and place
   them so the sentence stays precise about WHY (CI workflow definitions
   gate merges; CLAUDE.md is the session-init instruction pointer). If
   §0.2.2's enumeration is repeated verbatim elsewhere in SPEC or quoted
   in other live docs, find every instance (grep) and report each —
   amend only within `docs/SPEC.md`; report (do not edit) any other file
   carrying the enumeration.
3. `tools/validation/`: add `"CLAUDE.md"` to `INSTRUCTION_SURFACE_FILES`
   in ALL validators that define it (G2 `validate_root_surface_ownership.py`,
   G3 `validate_root_work_graph_dispatch.py`, G4
   `validate_instruction_tranche_manifest.py` — verify by grep that you
   found every definition; they are deliberately identical). Update any
   comment that enumerates the set. Add regression tests in each affected
   suite pinning that a `CLAUDE.md` write target / changed path is treated
   as instruction surface (mirror the existing `.github/workflows/`
   regression-test pattern from the Lane B `normalize_target` fix).
4. Concordance check (report, do not edit): the adopted PRD
   (`docs/PRD_ROOT.md`) cites SPEC §0.2.2 by reference (O-1, O-9); confirm
   your edit does not contradict any PRD sentence that RESTATES the
   enumeration (incorporation by reference is unaffected; a verbatim
   restatement would be). Same check for `AGENTS.md` and
   `docs/DIRECTIVE.md`/`docs/TYPES.md`. List every restatement found and
   whether it now diverges — divergences are REPORTED to Agent 0, never
   silently fixed.

## Constraints

- Write scope: `docs/SPEC.md`, `tools/validation/**` (the three validators
  + their test suites only), and your terminal return at
  `execution/_Coordination/AgentRuns/ROOT-OGC-20260725/returns/S1_RETURN_RAW.md`.
  Nothing else — no CLAUDE.md edit, no `.gitignore` edit, no AGENTS.md,
  no PRD, no CI workflow files. No commits.
- A sibling agent is concurrently editing `docs/CONTRACT.md` — do not
  touch it.
- Minimal-diff discipline: prose changes only where R1/R2 require.
- Verification (verbatim, every exit code): `python3 -m pytest
  tools/validation -q` (all pass incl. your new tests); all five root
  guard validators exit 0; `python3 tools/validation/validate_path_anchors.py`
  PASS; `git status --porcelain` in scope. Also run G4 CI mode and confirm
  existing manifests still validate (adding CLAUDE.md to the set must not
  retro-invalidate any committed manifest).

## Terminal return (`S1_RETURN_RAW.md`, and return the same content)

Exact sentences added (before/after fences per edit site); every
enumeration-restatement site found with divergence verdicts; validator/test
changes; verification transcript; constraint confirmations; open items.
