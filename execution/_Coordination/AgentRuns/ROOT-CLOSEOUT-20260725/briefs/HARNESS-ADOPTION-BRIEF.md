# Sealed Brief — H1: Practitioner-harness adoption of the root adapter (ROOT-CLOSEOUT-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: ephemeral bounded
Agent 2 generalist, `opus-5`. One objective; no delegation; terminal return.

## Authorization and context

Owner direction, in-session, 2026-07-25: close out the dormant items before
per-deliverable initialization. This item was recorded as "separately
authorized" at Lane B and N2 (G1 docstring: "Adopting the root into the
practitioner-harness project table (or teaching the loader this relpath) is
a recorded open item for root Project Setup"); the owner's closeout
direction releases it. It is an M2 instruction-surface tranche (writes
under `tools/`), landing through a human-gated PR with the tranche manifest
`docs/governance_harness/tranche_manifests/ROOT-CLOSEOUT-20260725.yaml`
(Agent 0 authors the manifest — you do not).

The root working root now has: an accepted decomposition, 6 materialized
`execution/PKG-*` packages with 45 `_STATUS.md` files at OPEN
(prose-bullet-v1, all PARSED), and a G1-validated adapter at
`execution/_harness/adapter.yaml` with schema `root-harness-adapter/v1`
(baselines: status_files 45, status_mismatch 0, pinned_at `653fabc9b…`).

## Objective

Teach the practitioner harness (`tools/practitioner_harness/`) to operate
on the root working root as a first-class project, WITHOUT changing root
guard semantics or any project's existing behavior:

1. `PROJECT_ALIASES` in `harness.py`: add aliases `root` and
   `chirality-root` resolving to the repository root (`.`). Study how the
   resolver builds paths so `.` cannot produce malformed joins.
2. `adapter_loader.py`: support the root adapter — location
   `execution/_harness/adapter.yaml` (vs projects' `_harness/adapter.yaml`)
   and schema `root-harness-adapter/v1` (vs `practitioner-harness-adapter/v1`).
   Design for equivalence, not duplication: normalize the root adapter into
   the loader's internal shape (`prd` fills the role `plan` serves;
   `baselines.status_files`/`status_mismatch` map to the drift-baseline
   fields; root has no `dag_pointer` — decide and document how the
   consuming commands behave when it is absent, refusing rather than
   guessing where a command genuinely needs it). Keep both schemas
   validated strictly — no field soup, no silent fallbacks between the two
   shapes. The G1 validator (`tools/validation/validate_root_harness_adapter.py`)
   remains the root adapter's authority — do not weaken or duplicate its
   checks; the loader may be stricter about what the harness needs, never
   looser about what G1 requires.
3. Make at least `status` and `drift` work against root:
   `python3 tools/practitioner_harness/harness.py status --project root`
   and `... drift --project root` must run and report truthfully (45
   files, 0 mismatches, states OPEN). Any command that cannot meaningfully
   support root (e.g. DAG-dependent ones) must refuse with a clear
   operational message naming the reason — never a stack trace, never a
   wrong answer.
4. `self-check` must keep passing, and root must be included in whatever
   coverage `self-check` claims only if that inclusion is truthful.
5. Tests: extend `tools/practitioner_harness/` test suites with root
   coverage — alias resolution, adapter load/normalization, status/drift
   against a tmp fixture AND the live repo (pin the live baseline 45/0 the
   same way the suite pins app-dev 0/53 and piping 0/101, so root drift
   regressions are caught in CI). All existing tests must pass unchanged;
   if an existing test's premise conflicts with adoption, STOP and report
   rather than modify it.

## Constraints

- Write scope: `tools/practitioner_harness/**` only, plus your terminal
  return at
  `execution/_Coordination/AgentRuns/ROOT-CLOSEOUT-20260725/returns/H1_RETURN_RAW.md`.
  No writes to `tools/validation/`, `execution/`, `docs/`, agents, CI
  workflows, or the root adapter itself. No commits, no branches.
- Python 3 stdlib + pyyaml only. Machine-absolute paths prohibited.
- Do not change any behavior for `app-dev`, `piping`, or `pec`.
- Verification before returning (report verbatim, every exit code):
  `python3 -m pytest tools/practitioner_harness -q` (all pass, including
  your new tests); `python3 -m pytest tools/validation -q` (unchanged,
  all pass); `harness.py status --project root`, `drift --project root`,
  `self-check` (exit 0 each); `status --project app-dev` and
  `drift --project piping` unchanged vs current `main` behavior (run and
  compare); `python3 tools/validation/validate_root_harness_adapter.py`
  still PASS (you did not touch the adapter);
  `python3 tools/validation/validate_path_anchors.py` PASS;
  `git status --porcelain` exactly in scope.

## Terminal return (`H1_RETURN_RAW.md`, and return the same content)

Files created/modified; the normalization design (schema mapping table,
absent-field policy per command); refusal behaviors added; test inventory
(new test names + what each pins); full verification transcript; constraint
confirmations; open items.
