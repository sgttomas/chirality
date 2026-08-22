# DEL-09-04 post-Root login-proof enablement and owner-procedure staging

- Date: `2026-08-21` (`2026-08-22` UTC build evidence)
- Run: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- Node / manager: `N3` / `WI-PKG09-LOGIN-STAGING-01`
- Authority: owner standing direction transcribed in the run root; owner act
  adopting the routed Root notices after PR #602
- Exact build commit: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Branch: `codex/app-post-root-login-proof`
- Result: `PASS — UNSIGNED PACKAGE REBUILT; OWNER PROCEDURE STAGED ONLY`
- Deliverable state: `IN_PROGRESS`

This record enables the owner to perform the already-reviewed two-phase R12
login-session proof later. It does not execute preparation, logout/login,
capture, deployment, proof, publication, signing, notarization, distribution,
release readiness, issuance, or reliance.

## Current unsigned package

The exact command below ran from `projects/chirality-app-dev/frontend`:

```sh
npm run desktop:pack
```

The initial sandboxed attempt compiled Next, Electron, and the CLI, then stopped
when Electron Builder could not resolve GitHub for the pinned, uncached Electron
`43.2.0` arm64 artifact. A fresh executor reran the same tracked command with
narrow network permission only for that locked artifact retrieval. No
dependency version, package manifest, lockfile, or product source changed. The
retry exited `0` and completed the command's embedded
`desktop:verify-dependencies` and `instruction-root:integrity` stages.

Current packaged app:

```text
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app
```

- app identity: `com.chirality.app`, version `2.0.0`
- minimum macOS: `15.0.0`
- executable: thin arm64 Mach-O
- posture: Electron Builder skipped application signing because
  `CSC_IDENTITY_AUTO_DISCOVERY=false`; the executable carries only its
  linker-produced ad-hoc signature, with no team identifier
- main executable SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`

This is a local unsigned/adhoc `--dir` package. No DMG, artifact-proof label,
signing, notarization, distribution, publication, or release claim is in scope.

## Dependency and instruction-root evidence

The packaged dependency-boundary verifier returned `PASS`: no monorepo-local
package entries or forbidden development packages were present; required SDK,
Pi coding-agent, and Next packages were present; and the packaged desktop/CLI
runtime-source proof passed.

Current instruction-root summary:

```text
/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/summary.json
```

- summary SHA-256:
  `1028e49effe50da36cef27e7d2e05a5fcf1dc0369bc418f3c05e683c4d61cd82`
- generated: `2026-08-22T03:25:09.387Z`
- status: `pass`
- Git SHA: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- checked files: `43`
- missing, mismatched, or unexpected bundle-agent files: none
- instruction-root `latest/manifest.json` SHA-256:
  `d3ce01d5172ce1c0dbe23ff091ce74f397bef9b87da887361e615a06b3762d45`

The regenerated current-byte evidence records both source and bundled
`agents/AGENT_HELP_HUMAN.md` at SHA-256
`0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`,
10,073 bytes, with `match: true`; an independent byte comparison also passed.
The summary separately preserves its existing
`sourceCompleteness.status: needs_remediation` for the absent candidate
`examples` source asset. That calibrated derivative field is not upgraded and
does not alter the explicit integrity comparison status `pass`.

## Exact build-revision and frontend-tree proof

The app was built while `HEAD` was the exact 40-character commit:

```text
1b375af4f1219ecfc00fc2755854aa7fd4220901
```

The required proof command returned no output:

```sh
git diff --stat 1b375af4f1219ecfc00fc2755854aa7fd4220901..HEAD -- projects/chirality-app-dev/frontend
```

Scoped staged, unstaged, and porcelain checks also found no tracked frontend
change. The app therefore remains bound to a frontend tree identical to the
current branch tip at this record's fan-in. The command must be rerun at final
PR fan-in; any later frontend change invalidates this staged package identity
and requires a rebuild.

## Staged minimal owner procedure — do not run in this agent tranche

The following concrete values were selected and checked at staging time:

- `PROOF_APP` exists and is the current app above.
- `PROOF_REVISION` is the exact build commit above.
- `PROOF_ROOT` is nonexistent:
  `/private/tmp/chirality-login-proof-owner-2a38b15f-07de-48c4-87ef-ccd246bd92fa`.
- `PROOF_LABEL` begins the required owner prefix, is not loaded, and has no
  plist:
  `com.chirality.ci.runatload.login.owner.2a38b15f-07de-48c4-87ef-ccd246bd92fa`.

### Phase 1 — owner preparation before logout

Copy and run this block only when the owner chooses to begin the proof:

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
PROOF_APP="/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-2a38b15f-07de-48c4-87ef-ccd246bd92fa"
PROOF_LABEL="com.chirality.ci.runatload.login.owner.2a38b15f-07de-48c4-87ef-ccd246bd92fa"
PROOF_REVISION="1b375af4f1219ecfc00fc2755854aa7fd4220901"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs prepare --app-path "$PROOF_APP" --session-root "$PROOF_ROOT" --label "$PROOF_LABEL" --source-revision "$PROOF_REVISION"
```

Require `status: PREPARED` and `proofClaimed: false`. Stop on any error. Do not
bootstrap or kickstart the proof label.

The owner then performs one ordinary logout and later login on the same GUI
account. The harness does not automate this owner act.

### Phase 2 — owner capture after login

After that login, copy and run this separate block:

```sh
cd /Users/ryan/.codex/worktrees/ef5e/chirality
PROOF_ROOT="/private/tmp/chirality-login-proof-owner-2a38b15f-07de-48c4-87ef-ccd246bd92fa"
node projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs capture --session-root "$PROOF_ROOT"
```

Treat proof as passing only if capture exits zero and both `summary.json` and
`evidence-package.json` report `PASS`. Preserve only the three public redacted
JSON files `prepared.json`, `summary.json`, and `evidence-package.json` as the
evidence package. Do not package or publish private `.capture-state.json` or
`.capture-state.consumed.json`. Any nonzero exit, missing file, cleanup
residual, default-protection failure, unchanged login-session identity, or
inconsistent source/job/process identity is a failed proof and must not be
manually upgraded.

## Operator-facing effect and containment

The current operator job, plist, and CLI launcher were observed read-only
before and after packaging and were unchanged:

- `com.chirality.runtime`: loaded/running separately; no job action occurred
- `~/Library/LaunchAgents/com.chirality.runtime.plist`: SHA-256
  `2ebc556673d7dc1232a9e230a88a75355dec6916ad6c432f707a525b29a6c7bc`
- `~/.local/bin/chirality`: SHA-256
  `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`

The package was not launched. Under
`OWNER_RULING_2026-08-21_APP_PARKED_DECISION_SLATE.md`, the first later
authorized GUI launch of this rebuilt package may idempotently rewrite the CLI
launcher. That expected operator-facing effect is inside the accepted launcher
baseline and is **not** a park condition. It is not authorized or performed by
this staging record. The owner daemon-deployment act remains separate from the
login-session proof.

## Evidence, derivative status, and handoff

- Executor attempt 1 evidence:
  `execution/_Coordination/AgentRuns/APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21/instances/WI-PKG09-LOGIN-STAGING-01/executor/`
- Fresh successful executor evidence:
  `execution/_Coordination/AgentRuns/APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21/instances/WI-PKG09-LOGIN-STAGING-01/executor-attempt-2/`
- Runtime telemetry and review evidence remain under the same manager instance.

This run record, build outputs, integrity summary, and executor returns are
derivative evidence tied to the accepted source snapshot/build commit above.
They do not replace source truth. Current package staging is complete with no
agent blocker. Actual prepare, logout/login, capture, proof acceptance, and
later operator deployment remain owner acts. Rerun `desktop:pack` if the
frontend tree changes before owner use; choose new proof values if the staged
root, label, or plist ceases to be unique and absent. DEL-09-04 remains
`IN_PROGRESS`.
