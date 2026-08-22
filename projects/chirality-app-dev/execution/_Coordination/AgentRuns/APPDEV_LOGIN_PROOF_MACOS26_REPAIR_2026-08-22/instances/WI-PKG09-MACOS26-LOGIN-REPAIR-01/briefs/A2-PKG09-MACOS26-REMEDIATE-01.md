# Sealed brief — A2-PKG09-MACOS26-REMEDIATE-01

- RequestedBy: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- ParentInstanceID: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- ChildInstanceID: `A2-PKG09-MACOS26-REMEDIATE-01`
- AgentType: fresh ephemeral generalist Agent 2; no delegation
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- AcceptedBasis: frozen implementation candidate plus fresh-review F-01 at
  `review/REVIEW.md` SHA-256
  `adc3de73ed0ab46043ad599c9dbac34078c2982a7db9b9c8a7a42ce5a30b64d8`
- Mode: repair cycle 1, test/evidence only

## Objective

Repair only F-01 by adding direct fail-closed tests for every enumerated branch,
rerun the complete accepted validation matrix, and update only count/hash claims
made stale by the test edit. Do not change product source unless a new test
proves an actual defect; if that occurs, stop and return it rather than silently
expanding remediation.

## Required tests

Add direct cases for:

- non-Darwin platform;
- root/zero process UID;
- process UID versus current-account UID mismatch;
- invalid current-account usernames `root`, `loginwindow`, and `_mbsetupuser`;
- setup/loginwindow console identity as distinct console evidence;
- signaled `/usr/bin/stat`;
- signaled top-level `launchctl print gui/<uid>`;
- trailing top-level domain output after its closing brace;
- incomplete/unclosed top-level or security-context braces.

Every case must assert rejection/no PASS, no product/install execution, no
service-level or mutating launchctl operation, and no session-root creation.
Preserve all existing tests and product behavior.

## Reads, tools, and writes

Read the frozen run/implementation/review basis and full current test/source.
Use apply-patch and the same authorized checks as implementation. Writes are
limited to:

- `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
- DEL-09-04 R15
- DEL-09-04 `_STATUS.md` only where test counts/hash claims change
- this instance's `remediation-01/RETURN.md`

Do not edit product source, R14, original executor return, or any other path.

## Checks and return

Rerun syntax, focused Vitest, typecheck, full `npm test`, live optionless
preflight with proposed-root absence before/after, APP-HOLD, practitioner
self-check, forbidden-source scan, hashes, exact containment, and
`git diff --check`. Preserve the sandbox/unrestricted classification if the
full suite again requires local socket permission. No build/package/proof,
operator/LaunchAgents/launcher, network/provider, Git staging/publication, or
shared-surface action.

Write `remediation-01/RETURN.md` with exact changes/checks/hashes and return
PASS or blocker. Fresh full review remains mandatory after manager acceptance.
