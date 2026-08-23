# Fresh Review — N1 D-GOV-35 Decision and DEL-02-03 M2 Application, Cycle 1

Verdict: `FAIL — ONE ACTIONABLE FINDING; REPAIR AND FRESH RE-REVIEW REQUIRED`

Review basis: `origin/main@b143444bd497eae1b1b638670a33e6df756d9084`

Subject: N1 governed content, application evidence, manager return/status, and
the child attempt/repair evidence under `N1_DGOV35_M2_APPLICATION/`.

This is fresh read-only review evidence. It is not publication, merge,
lifecycle acceptance, release, reliance authority, or a hold lift.

## Actionable finding

### 1. MEDIUM — The application evidence does not preserve required validator exit codes and exact outputs

The controlling preparation plan states in
`DEL-02-03-M2-PREP-001/VALIDATION_PLAN.md`:

> Exact outputs and exit codes must be preserved in the application tranche's
> durable evidence and Root receipt.

The application package's `DEL-02-03-M2-APPLY-001/VALIDATION_RESULTS.md`
records concise PASS summaries, but it does not record an exit code for any of
the listed validators. It also does not preserve the exact output of several
commands. For example, the full manifest validator currently emits its
44-manifest declaration plus nine INFO lines, while the evidence records only
`PASS — 44 live manifests schema-valid in CI mode`; the CI-form invocation is
also summarized rather than preserved with its complete output and exit.

This is an evidence-contract defect, not a governed-content defect. The
reviewer's independent rerun confirms every current validator exits `0`, but
the review cannot substitute its own transient observation for the durable
application evidence expressly required by the validation plan.

Bounded repair:

1. Amend only `DEL-02-03-M2-APPLY-001/VALIDATION_RESULTS.md` to preserve the
   exact stdout/stderr and exit code for every command required by
   `DEL-02-03-M2-PREP-001/VALIDATION_PLAN.md`. Clearly retain the CI-form G4
   pre-commit limitation: it currently sees zero committed changed paths and
   must be rerun after the serialized N1 commit.
2. Update only the corresponding `VALIDATION_RESULTS.md` SHA row in
   `DEL-02-03-M2-APPLY-001/HASHES.sha256`.
3. Update the N1 manager return/status only if necessary to describe this
   repair accurately, then submit the repaired N1 package to a new fresh
   review cycle.

Do not change the ruled content, manifest, notices, proposal packet, live
instruction surfaces, lifecycle state, or any path outside N1's existing write
set.

## Checks that passed

- The Phase-0b steer and R1 record reproduce their declared SHA-256 values
  `c4b674327b78434561a42f93b8bb34e50921281459ec00ca6c8afaaa9ebb80e2`
  and `a9879a87faaeb4cd4d5f16b2b4b0364543dff117e1b51c7e17d1efdcb20f377d`.
- `origin/main` and the uncommitted branch basis both resolve to
  `b143444bd497eae1b1b638670a33e6df756d9084`; PR #620 merge
  `abf3c1bf5996cd9333ad706df14e62df32fbbf0f` is an ancestor.
- Literal scratch reconstruction from basis `AGENTS.md` plus
  `AGENTS.proposed.patch` succeeds and is byte-identical to live `AGENTS.md` at
  SHA-256
  `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`.
- Each concordance file has exactly one removed line and one added line. The
  added sentence is the R1-A ruled hierarchy verbatim; no other byte in those
  files changed.
- D-GOV-35 has the required pre-publication header, accepted basis,
  supersession boundary, `TBD` Git identities, complete byte-identical R1-A
  body, all eight proposal items byte-identical to the proposal, concordance
  disposition, and no-authority/no-hold boundaries.
- The D-GOV register adds exactly one row and removes none.
- The proposal is exactly its basis bytes plus the required ruled-status line.
  The README is exactly its basis bytes plus the two authorized SHA-table
  replacements and ruled-status line. Proposal SHA-256 is
  `cf992fe4a01956c5df4ecec6bdbd386c3c2c084cd323ab8f7361a611800a27b3`;
  README exact SHA-256 is
  `10947e324d5a68664b8d9ba44d5281a2fd5361ee638be7e64222be66cf25c414`;
  its normalized self-hash independently reproduces as
  `0eafd816f7da5252a6439b58fec21f2ef22295871629912715c276dd8a27ba86`.
- Direct validation of the finalized live manifest returns `failures=[]` and
  `notes=[]`. Its basis is the branch-time `main`; its protected path list is
  exact; its R1-B authorization is byte-identical to the owner record; its M2
  gate is `human-gated-pr` with `self_merge: false`; its two notices are
  `routed`; and public export disposition is `deferred`.
- Both routed notices exist, contain the pre/post `AGENTS.md` hashes, two-class
  rule, instruction-asserted boundary, calibrated pinned/mirrored surfaces,
  receiving-loop follow-ons, and the `coordination, not authority` boundary.
  `projects/**` changes are exactly those two notice files.
- The application evidence otherwise records the pre-gates, exact patch and
  concordance application, hashes, notice paths, lifecycle/non-hold posture,
  public-export deferral, and lawful handoff. Every current row of
  `HASHES.sha256` verifies.
- DEL-02-03 `ScopeOfWork.md` is unchanged at
  `e3d4a4c862919acf00c777cb024f0c4f9456df25fa14448862830241d607460f`;
  `_STATUS.md` changes by one History line only and keeps `Current State:
  INITIALIZED`; `_ScopeChange/_LATEST.md` remains
  `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.
- No `agents/**` path changes. No unlisted `projects/**`, runtime, export,
  pointer, pin, DEL-02-06, or other protected-path write was found in N1.
- Independent validator reruns all returned exit `0`:
  `validate_agent_instructions.py` (34/0/0),
  `validate_instruction_entrypoints.py`, full manifest validation,
  pre-commit CI-form G4, candidate whitespace, Task Management register
  validation (21 rows), and `git diff --check`.
- The exact CI-form G4 invocation currently reports zero changed paths because
  N1 is uncommitted. Its mandatory post-commit rerun remains correctly open.

N1 must not enter serialized CHANGE fan-in until the bounded evidence repair
and a fresh independent re-review return zero actionable findings.
