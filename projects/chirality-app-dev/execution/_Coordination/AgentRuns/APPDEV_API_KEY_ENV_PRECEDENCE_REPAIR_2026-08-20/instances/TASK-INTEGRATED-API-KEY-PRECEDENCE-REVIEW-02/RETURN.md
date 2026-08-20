# Return — TASK-INTEGRATED-API-KEY-PRECEDENCE-REVIEW-02

RUN_STATUS: FAILED

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-code-review

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: NONE

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

AllowedTools: `python3 tools/software_workflow/select_affected_checks.py`, `python3 tools/software_workflow/validate_change_scope.py`, `python3 tools/software_workflow/compare_structured.py`, `python3 tools/software_workflow/verify_generated_manifest.py`

RuntimeOverrides: none

WriteAuthorization: managed read-only run; only runtime-owned `STATUS.json` and `RETURN.md` terminalized

## Verdict

**FAIL — one actionable blocking finding.** The product implementation,
Review 01 F1-F3 remediation, raw packaged proof, and deliverable-state
calibration pass review, but the candidate cannot fan in because the frozen-v2
aggregate is false for its declared exact reconstruction.

## Exact identity and coverage

- Independently reconstructed exactly **94/94** candidate paths from repository
  root using the manifest's tracked-plus-untracked enumeration, excluding only
  `FROZEN_CANDIDATE_MANIFEST_V2.md` and this review's launch/status controls.
- Reviewed **4/4 product/test paths** and **90/90 evidence/state/control paths**.
  All 27 candidate JSON documents parsed; all Markdown/TypeScript and complete
  untracked-file bytes were included in hash, whitespace, scope, and semantic
  review. Raw proof at `/tmp/chirality-precedence-closure.pXvs6Z` was also
  parsed and backchecked.
- Expected v2 aggregate:
  `eeda6c56d07326b0c30c186627d14a8319c3f8239b497b507f314724e544b788`.
- Actual newline-delimited per-file `shasum -a 256` aggregate in the exact
  sorted 94-path order:
  `3c33705a267d938c6052869bfa064dc00ea734711ac90e755176f1ac1202d563`.
- Scope validation passed: every candidate path is under
  `projects/chirality-app-dev`; no protected root/runtime path drift exists.

## Actionable finding

### F0 — Blocking — frozen candidate manifest v2 has the wrong aggregate

`FROZEN_CANDIDATE_MANIFEST_V2.md` declares the exact 94-path reconstruction
must hash to `eeda6c56...b788`, but the declared algorithm produces
`3c33705a...d563`. The count and path set are exact. Only this review's controls
postdate the v2 manifest, and the manager independently reproduced the same
count and aggregate, so this is a frozen-manifest generation/freeze-race defect,
not reviewer-local variance. A review cannot authenticate bytes against a
non-matching freeze.

Remediation direction: regenerate a stable manifest from the exact current
candidate, exclude the replacement manifest and next review's controls
unambiguously, verify its aggregate independently before dispatch, and run a
fresh read-only integrated review.

## Review 01 F1-F3 backcheck

- **F1 PASS:** complete 94-path scan, including every untracked file, reports
  zero trailing-whitespace findings. The 15 cited locations are clean.
- **F2 PASS:** DEL-09-06 REQ015 now correctly cites compact `summary.json` for
  artifact identities, assertions, and results, and separately cites
  `_run_records/TASK_RUN_2026-08-20_1630.md` for the exact host commands.
- **F3 PASS:**
  `instances/WI-PKG09-API-KEY-PRECEDENCE-01/N3_MANAGER_REGISTERED_CHECKS.json`
  has SHA-256 `e89bf83dc90073f775b8a80a1216b9bd68a0f4157928ddd866e6b30363c175ed`
  and normalized PASS evidence for `harness-pytest` (350 passed, exit 0) and
  `harness-self-check` (exit 0), including command, cwd, duration, stdout, and
  stderr.

## Product correctness and security

- All four declared product/test hashes match v2:
  `d810b1ef...1444db`, `c9cadac3...17dac4`, `3293cbf1...ed3cb`, and
  `818b7424...74b1a6`.
- `SafeStorageCredentialStore.resolve` implements the accepted order: persisted
  safeStorage, `ANTHROPIC_API_KEY`, then
  `CHIRALITY_ANTHROPIC_API_KEY`; whitespace-only values fall through.
- Store-owned `ui | env | none` source is returned without credential material.
  Electron IPC consumes and validates that source, rejects malformed or
  inconsistent replies, does not re-infer from its own environment, and fails
  closed without disclosure.
- Provider isolation and existing unavailable/store/remove behavior are
  preserved. Focused, full Vitest, Electron/frontend typecheck, build, secret,
  scope, and registered evidence support the changed behavior.
- No additional product finding was found.

## Raw packaged-proof backcheck

- Compact proof hashes remain
  `0ec3c501c1406210b30fb32509d972e7dd8b9f0e0686aa97e1e009eb40f82df3`
  (`summary.json`) and
  `4fe82d2b2297b8665e4e2331762a78e2108e6184533cc0f365a4e8e22787ffc6`
  (`SUMMARY.md`).
- Raw summary hash is
  `016f26c486777a4354af6607a6d1202e5b4ee1eedfb76a5faa53383e293f6471`;
  final secret-scan hash is
  `7293f98c28fe214bb92e94544f6b167b364c977ebc77b1eb9fa78fc64adafa00`.
- Raw evidence confirms packaged artifact identity, encrypted owner-only
  safeStorage store/status/remove, provider isolation, blocked renderer
  diagnostic and blocked/loopback probes, five descendant snapshots, zero
  non-allowlisted outbound TCP, zero credential/metadata leaks, code-0 GUI and
  daemon shutdown with closed streams, temporary-user-data cleanup, and a
  5,868-file final secret scan with zero blocked findings.
- The retained raw and compact claims agree; no raw-proof finding was found.

## State, APP-HOLD, and boundaries

- APP-HOLD evidence records integrity PASS and ALLOW for dispatch/reliance on
  DEL-04-05, DEL-02-05, DEL-09-06, and DEL-09-04.
- DEL-02-05 and DEL-04-05 remain `IN_PROGRESS` with empty Remaining sections;
  DEL-09-06 removes only the selected packaged-security residual while keeping
  lifecycle/dependency/release fences explicit; DEL-09-04 retains login-time
  `RunAtLoad` and the owner-machine deployment act.
- Checking Approval SHAs, dependency status, F-APP-2, signing, notarization,
  distribution, publication, and release readiness are unchanged. No lifecycle
  or release act is implied.

## Residual risk and fan-in

Residual product risk is limited to the already-recorded broader lifecycle and
dependency gaps; no new implementation or proof risk was found. Nevertheless,
**fan-in is invalid** until F0 is repaired and a fresh review authenticates the
new stable freeze. Verdict: **FAIL**, not `PASS_WITH_FINDINGS`.

## Tools Used

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`
- Brief-required read-only Git, hash, JSON, whitespace, and source-inspection
  primitives

## Tool Policy Compliance

PASS. Scope validation ran first; affected-check selection audited evidence
coverage. Structured comparison/generated-manifest helpers were not relevant.
No product or host proof command was rerun.

## Outputs Produced

- This terminal review return and status only.
- One immediate manager report for F0.

## Missing

none

## Needs Human Ruling

none

## Dependency Notes

- A corrected stable candidate freeze and a fresh independent integrated review
  are required before package fan-in.

## Proposed Changes

- Replace the defective v2 manifest with a correctly calculated stable freeze;
  do not modify product/evidence/state bytes solely for this finding.

No product, evidence, deliverable state, coordination candidate, Git, host
artifact, or raw proof byte was edited. No delegation occurred.
