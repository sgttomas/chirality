# Return — TASK-INTEGRATED-API-KEY-PRECEDENCE-REVIEW-01

RUN_STATUS: FAILED

ReviewVerdict: **FAIL**

ControlSurface: FILE

TaskProfile: NONE

TaskSkill: software-code-review

ScopePath: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev`

ResolvedSkillPath: `/Users/ryan/.codex/worktrees/ef5e/chirality/skills/software-code-review`

ResolvedSkillVersion: `1`

ResolvedTaskProfileRequirement: NONE

CompanionFiles: `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`

WriteAuthorization: runtime-owned review `STATUS.json` and `RETURN.md` only

## Frozen identity and 100% coverage

- Independently reconstructed exactly **86** frozen candidate paths, excluding
  only `FROZEN_CANDIDATE_MANIFEST.md` and this review instance's controls.
- Independently recomputed aggregate SHA-256
  `ee2623a620af684ed6b67a678466d46db186b4e590c9dd606f61542ff322acec`:
  exact match.
- All four product/test identities matched the manifest:
  `d810b1ef…1444db`, `c9cadac3…17dac4`, `3293cbf1…ed3cb`, and
  `818b7424…74b1a6`.
- Read 100% of all four product/test files and semantically inspected all 82
  frozen evidence/state/control paths. All candidate JSON and all raw host
  JSON/NDJSON parsed. All candidate paths are contained under
  `projects/chirality-app-dev`; no protected root instruction, skill, tool,
  decomposition, decision, receipt, completion-log, dependency, or lockfile
  path is changed.
- Package ownership is contained: N1 owns PKG-04 plus storage source/test, N2
  owns PKG-02 plus IPC source/test, N3 owns only the named PKG-09 evidence and
  state. Shared graph/plan files are Agent-0 controls.

## Actionable findings

### F1 — Blocking — candidate-wide whitespace gate fails on untracked files

The frozen brief requires candidate-wide whitespace checking, including
untracked paths. Ordinary `git diff --check` passes only because the affected
control files are untracked. An exact 86-path trailing-blank scan finds 15
occurrences:

- `WORK_GRAPH.md:5-7`;
- `WORK_GRAPH_V2.md:5-8`;
- `instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_MANAGER_VALIDATION_V2.md:3-4`;
- `instances/WI-PKG04-API-KEY-PRECEDENCE-01/RETURN_V2.md:5-7,71-72,75`.

Impact: N3 acceptance item 9 and the integrated review brief's explicit
candidate-wide whitespace gate are not satisfied. The frozen candidate also
contains assertions that whitespace passed, so the evidence is inconsistent
with the actual untracked bytes.

Remediation: remove the trailing blanks (use paragraphs or explicit markup if
hard line breaks are intended), rerun the exact tracked-plus-untracked scan,
refreeze the aggregate, and dispatch a fresh review.

### F2 — Blocking — DEL-09-06 REQ015 cites a field absent from compact evidence

`DEL-09-06.../Assessment_INSP-03_DEL-09-06.md:38` says compact
`summary.json` identity-binds the artifacts, **commands**, assertions, and
results. The compact JSON has no `commands` field. Exact host commands exist
only in `_run_records/TASK_RUN_2026-08-20_1630.md`; they are not subjects of an
identity relation declared by `summary.json`.

Impact: the assessment's PASS evidence statement is factually broader than
the cited artifact, violating the review requirement that packaged proof
support every calibrated assessment/state claim.

Remediation: either cite the run record separately for commands and narrow the
`summary.json` statement, or add command identities to compact evidence;
refreeze and re-review. No product or host-proof rerun is required if only the
claim/evidence bytes change and the underlying artifact identity stays fixed.

### F3 — Blocking — passing host harness/self-check evidence is not normalized or retained

`WI-PKG09-API-KEY-PRECEDENCE-01/LAUNCH_BRIEF.md:55-57` requires the
practitioner harness and root self-check to pass with normalized evidence;
lines 68-70 require raw host output and exact command/results retention.

The retained raw evidence shows:

- `registered-checks-sandbox.json`: `harness-pytest` FAIL (system Python lacks
  pytest) and `harness-self-check` FAIL (system Python lacks PyYAML);
- `registered-host-checks.json`: passing entries only for `frontend-test`,
  `frontend-typecheck`, `frontend-build`, and `app-hold-integrity`;
- no other raw file contains normalized passing results for the required
  mise-Python practitioner harness or root self-check reruns.

The compact summary and run prose assert 350 harness tests and self-check PASS,
but the reviewer cannot backcheck those assertions to a normalized command,
cwd, exit code, duration, and output. This is the same evidence class that the
earlier N1/N2 review loops correctly required before fan-in.

Remediation: persist a normalized host/mise evidence bundle for the passing
`harness-pytest` and `harness-self-check` reruns, update any affected compact
references, refreeze, and dispatch a fresh review. No product change is
requested.

## Product correctness and security

No actionable product defect was found.

- `SafeStorageCredentialStore` resolves non-whitespace persisted safeStorage
  first, `ANTHROPIC_API_KEY` second, and
  `CHIRALITY_ANTHROPIC_API_KEY` third; oMLX remains isolated.
- Status exposes only `{ configured, source }`; source is `ui | env | none`
  and no credential material crosses the status boundary.
- Electron IPC treats daemon status as untrusted, requires a valid and
  internally consistent configured/source pair, projects only non-secret
  status, and fails malformed replies closed. Thrown/unreachable behavior
  remains the prior structured `unavailable` result.
- Store/remove, unsupported-provider, provider isolation, and settings
  consumers remain compatible. Focused tests cover coexistence, canonical and
  compatibility fallbacks, none, whitespace, malformed replies, and
  non-disclosure.
- The root runtime static `CredentialStatusResponse` and
  `ProviderCredentialPort` types still omit the additive source field. The
  current daemon serializes the store's full enumerable status and the local
  IPC boundary validates `unknown`, so current behavior works. This remains a
  documented residual contract risk, not a defect in the frozen authorized
  app slice.

## Raw packaged-proof backcheck

The packaged proof itself backchecks successfully:

- raw `summary.json` SHA-256
  `016f26c486777a4354af6607a6d1202e5b4ee1eedfb76a5faa53383e293f6471`
  and final secret-scan SHA-256
  `7293f98c28fe214bb92e94544f6b167b364c977ebc77b1eb9fa78fc64adafa00`
  match compact evidence;
- executable, `app.asar`, CLI, packaged-subject, and DMG identities match;
- independently extracted `dist-electron/main.js` is 1,375,977 bytes at
  SHA-256 `aebac27f…90120` and contains the accepted resolver order, source
  discriminator, and IPC fail-closed consumer;
- safeStorage before/store/status/remove, encrypted owner-only non-plaintext
  blob, provider isolation, zero retained credential/metadata findings,
  blocked renderer diagnostic and both probes all match raw evidence;
- all five TCP snapshots parse and contain zero non-loopback endpoints;
- GUI and daemon terminated code 0 with stream closure, and temporary userData
  cleanup passed;
- the final scan covers 5,868 files with zero blocked findings and no real
  credential environment input.

The initial sandbox failures are correctly classified as execution-surface
calibration only where exact host reruns are retained. F3 concerns the two
host reruns whose normalized evidence is absent, not the packaged proof.

## State and boundary calibration

- DEL-02-05 and DEL-04-05 remain `IN_PROGRESS`, their Remaining sections stay
  empty, and Checking Approval SHA remains
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.
- DEL-09-06 removes only the selected D-APP-97 packaged-security residual and
  remains `IN_PROGRESS`; dependency and release closure stay separate.
- DEL-09-04 removes only the coordinated REQ-009/R4-P49 packaged-network item.
  Login-time `RunAtLoad` and owner-machine deployment remain explicit.
- Dependencies, lifecycle, signing, notarization, distribution, publication,
  and release fences are unchanged.

Apart from F2, no further state/claim calibration defect was found.

## Verdict and fan-in

- Blocking findings: **3**.
- Non-blocking findings: **0**.
- Product-source findings: **0**.
- Raw packaged-proof findings: **0**.
- Verdict: **FAIL**.
- Fan-in recommendation: **REJECT** the current frozen candidate. Remediate
  F1-F3, generate a new frozen identity, and dispatch a fresh independent
  integrated review. Product and packaged-host proof need not rerun if their
  identities remain byte-identical and the replacement evidence truthfully
  binds the existing proof.

## Tool policy and confirmation

ToolsUsed:

- `python3 tools/software_workflow/validate_change_scope.py`
- `python3 tools/software_workflow/select_affected_checks.py`
- brief-required repository reads, Git/hash reconstruction, JSON/NDJSON
  parsing, artifact extraction, and whitespace inspection

ToolPolicyCompliance: PASS

No candidate, product, evidence, state, graph, manager, Git, lifecycle,
dependency, release, commit, push, PR, merge, or publication edit was made. No
delegation occurred. Writes are limited to this instance's runtime-owned
`STATUS.json` and `RETURN.md`.

MISSING:

- normalized passing host evidence for N3 practitioner harness and root
  self-check.

NEEDS_HUMAN_RULING: none

DEPENDENCY_NOTES: N3 remains gated behind remediation and a fresh integrated
PASS with zero actionable findings.
