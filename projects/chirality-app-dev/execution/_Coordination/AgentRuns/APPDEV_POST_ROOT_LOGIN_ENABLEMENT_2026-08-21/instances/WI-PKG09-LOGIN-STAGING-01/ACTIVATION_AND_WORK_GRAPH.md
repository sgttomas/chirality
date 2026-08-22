# WI-PKG09-LOGIN-STAGING-01 — Activation and work graph v1

- RunID: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- InstanceID: `WI-PKG09-LOGIN-STAGING-01`
- Parent: `HELP_HUMAN`
- Role: `WORKING_ITEMS` (Agent 1)
- Package / selected deliverable: `PKG-09` / `DEL-09-04`
- Accepted basis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Selection authority: owner standing direction transcribed at the run root
- Posture: `TERMINAL_FAN_OUT_IN`, serialized executor then fresh reviewer
- State: `SOW_V1`; DEL-09-04 remains `IN_PROGRESS`

## Objective

Rebuild the unsigned packaged app with `npm run desktop:pack`, bind the app to
the exact 40-character build commit, prove the frontend tree remains identical
from that commit through the node return, and create a DEL-09-04 run record that
stages—but does not execute—the concrete R12 owner login-session procedure.

## Boundary

Persistent writes are limited to DEL-09-04 status/memory/run-record surfaces
and this instance directory. The packaging command may regenerate only its
documented ignored evidence outputs under `frontend/.next`, `dist-electron`,
`dist-runtime`, `dist`, and `artifacts`. No product source edit is authorized.

Excluded and forbidden: GUI launch; `prepare` or `capture`; `launchctl`
bootstrap/kickstart; logout/login; any access that mutates
`com.chirality.runtime`, `~/Library/LaunchAgents/com.chirality.runtime.plist`,
or `~/.local/bin/chirality`; signing, notarization, distribution, publication,
release-readiness or issuance claims; provider expansion; artifact-proof
labeling; staging, commits, push, PR, receipt, and shared completion surfaces.

## Nodes

1. `A2-PKG09-LOGIN-PACK-01` — ephemeral Agent 2 executor.
   - Reads: frozen run plan/transcription, DEL-09-04 R12 and status, owner
     launcher-baseline ruling, build profile/docs, package manifest, Git state.
   - Writes: documented ignored packaging evidence and this instance's
     `executor/` records only.
   - Return: exact source commit, command/result/duration, app path and identity,
     integrity/dependency results, frontend-diff proof, forbidden-target
     before/after observations, and containment.
2. `A2-PKG09-LOGIN-REVIEW-01` — fresh read-only ephemeral Agent 2 reviewer.
   - Dependency: accepted executor return and manager-authored DEL-09-04 run
     record.
   - Reads: 100% of node persistent diff plus executor evidence and generated
     summary.
   - Writes: this instance's `review/` records only.
   - Return: PASS or enumerated actionable findings.

Edge: `PACK-01 -> manager fan-in/run record -> REVIEW-01`. A failed review
returns only this node for at most two repair plus fresh-review cycles.

## Fan-in gates

- `npm run desktop:pack` exits zero and includes its dependency-boundary and
  instruction-root-integrity checks.
- `frontend/dist/mac-arm64/Chirality.app` exists at the recorded absolute path.
- The exact build commit is 40 hexadecimal characters and
  `git diff --stat <build-commit>..HEAD -- projects/chirality-app-dev/frontend`
  is empty at return.
- The concrete `PROOF_ROOT` is unique and nonexistent; the concrete
  `PROOF_LABEL` begins `com.chirality.ci.runatload.login.owner.` and is not
  loaded or installed.
- No forbidden operator path or service changed; no owner procedure step ran.
- DEL-09-04 stays `IN_PROGRESS`; all proof and release boundaries remain.
