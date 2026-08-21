# DEL-09-04 actual login-session LaunchAgent proof preparation

- Date: 2026-08-21
- Run: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- Authority: owner `PREPARE-THEN-OWNER` ruling plus superseding owner direction
  **“Push through failures.”** This record documents completed implementation
  preparation under active integrated remediation; it does not perform or claim
  proof or publication.
- Product hashes: script
  `980e2e710ab66006baeefc14d400584bc8837f3ea3b35390db94b879413e2c20`;
  focused test
  `f168e7d18326a536ff07b4e3a82019904bc43753fa3999acd439b8353171f01a`.

> **ACTIVE INTEGRATED REMEDIATION.** The owner immediately superseded the stop
> disposition with **“Push through failures.”** Exact reviewed frozen diff 04
> bytes are restored to the live candidate paths. Agent 0 owns routing of the
> App-side `RUNTIME_INSTRUCTION_ROOT_ENV` alignment; root runtime writes,
> unrelated App mocks, and `node_modules` remain forbidden here. The owner
> procedure below remains non-executable until mandatory integrated
> Vitest/typecheck/build and a fresh full-diff review pass. Those local gates
> now pass; final review and later Git/packaged identity remain.

## What the preserved candidate implements

The reusable harness has two phases. `prepare` validates the GUI account,
packaged app, unique proof label, absent proof job/plist, and disjoint new
session root. It installs through the packaged CLI into the canonical
`~/Library/LaunchAgents` with exact packaged daemon argv, `RunAtLoad=true`,
proof-only persistent runtime data, and `CHIRALITY_SKIP_CLI_LAUNCHER=1`. It
never bootstraps, kickstarts, logs out, logs in, or claims proof.

After a later owner logout/login, one `capture` command requires a distinct GUI
login-session identity and validates the prepared plist, source revision,
loaded job state, exact program/argv/PID/process executable, and unchanged
default job/plist posture. The public evidence package contains only the three
redacted files `prepared.json`, `summary.json`, and `evidence-package.json`.
Separately, prepare writes private one-shot `.capture-state.json`, which contains
local absolute identity paths; capture atomically renames it to private
`.capture-state.consumed.json`. Both private state names are retained only in
the restrictive local proof-session directory and are excluded from the public
evidence package. Identity-gated cleanup removes only proof-owned
job/plist/runtime state. Missing, stale, ambiguous, unsafe, or incomplete
evidence fails closed and records cleanup residuals.

## Minimal owner procedure — future owner act, pending integrated acceptance

Do not run these commands yet. Although the exact reviewed script is restored
and local integrated gates pass, final integrated review, Git integration, and
an exact accepted source revision and packaged app remain prerequisites.
Only then choose a new nonexistent session-root path and unique label beginning
`com.chirality.ci.runatload.login.`. Never use `com.chirality.runtime`.

1. From the repository root, set task-specific shell variables to explicit
   values (shown as placeholders), then run preparation once:

   ```sh
   PROOF_APP="/absolute/path/to/Chirality.app"
   PROOF_ROOT="/absolute/new/nonexistent/chirality-login-proof-<unique>"
   PROOF_LABEL="com.chirality.ci.runatload.login.owner.<unique>"
   PROOF_REVISION="<exact-40-character-source-commit>"
   node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs prepare --app-path "$PROOF_APP" --session-root "$PROOF_ROOT" --label "$PROOF_LABEL" --source-revision "$PROOF_REVISION"
   ```

   Require `status: PREPARED` and `proofClaimed: false`. Stop on any error. Do
   not bootstrap or kickstart the proof label.

2. The owner performs one ordinary logout and later login on the same GUI
   account. This is the sole owner act; the harness does not automate it.

3. After login, restore only the same explicit `PROOF_ROOT` value and run the
   single capture command:

   ```sh
   PROOF_ROOT="/absolute/new/nonexistent/chirality-login-proof-<unique>"
   node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs capture --session-root "$PROOF_ROOT"
   ```

4. Treat proof as passing only if the command exits zero and both
   `summary.json` and `evidence-package.json` report `PASS`. Preserve the three
   public redacted JSON files as the evidence package. Do not package or publish
   private `.capture-state.json` or `.capture-state.consumed.json`; keep the
   proof-session directory access-restricted until its governed local cleanup.
   Any nonzero exit, missing file, cleanup residual, default-protection failure,
   unchanged login-session identity, or inconsistent source/job/process
   identity is a failed proof and must not be manually upgraded.

No action against the operator/default LaunchAgent or CLI launcher is part of
this procedure. The owner-machine daemon deployment act remains separate.

## Validation and current gate state

- Focused syntax and Vitest: PASS, 15/15.
- Exact two-path scope: PASS.
- Final fresh full-file review: PASS, zero findings, 100% coverage.
- Practitioner harness: PASS, 350 tests.
- Root harness self-check and APP-HOLD integrity: PASS.
- Host-capability full Vitest: 1,210 passed / 4 skipped / 4 failed. All four
  failures are the concurrent `RUNTIME_INSTRUCTION_ROOT_ENV` export/mock gap.
- Typecheck and build: FAIL on the same external missing export. Rerun these
  integrated gates after that root/DEL-08 dependency is aligned. **Superseded:**
  Agent 0 rebuilt current runtime only under ignored frontend dependencies;
  final registered typecheck and build now PASS.
- Host full Vitest: PASS, 152 files + 1 skipped; 1,214 tests + 4 skipped.
- Focused affected trio: PASS, 35/35.
- Registered premerge local attempt: managed Next service READY; check FAIL only
  because the shared runtime daemon/project registration lifecycle was absent
  (`HTTP 503`). No local product defect was identified. Treat premerge as
  PR-CI-owned and rerun it after PR using the workflow's full runtime
  build/start/register lifecycle.
- Current decision: `PREPARATION_COMPLETE`. Final integrated review/fan-in and
  later PR-CI premerge remain mandatory before owner execution.

This is implementation-preparation evidence under active remediation, not
actual login-session proof, publication, release evidence, reliance, lifecycle
acceptance, signing, notarization, or distribution.
