# Sealed brief — A2-PKG09-R18-NETWORK-03

## Identity and objective

- RequestedBy / Parent: `WI-PKG09-R18-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R18-NETWORK-03`
- Fresh ephemeral generalist Agent 2; no delegation
- Objective: execute and evidence exactly one renewed SHASUMS GET chain, then
  stop without implementation.

## Allowed write and request

Write only unique
`instances/WI-PKG09-R18-STAGING-01/executor-3/` evidence and `RETURN.md`.
Preserve attempts 1/2 and every manager/source/deliverable byte.

Initialize evidence before network. Then use one `/usr/bin/curl` invocation
starting at exact URL:

`https://github.com/electron/electron/releases/download/v43.2.0/SHASUMS256.txt`

Request escalation only for that exact invocation. Require HTTPS for initial
and redirect protocols, redirects enabled with maximum `1`, and capture the
body exactly once. No artifact URL/request. The only accepted response chain
is `github.com` then `release-assets.githubusercontent.com`; any other host,
extra redirect/request, or protocol fails the node. Record curl exit, each
status/host, effective host/status, redirect count, body bytes, and full body
SHA-256. Sanitize signed Location query values from repository headers after
validating the host; do not retain or reproduce tokens/JWTs.

Require final 2xx, plausible plain text near 7.6 KB, exactly one line for
`electron-v43.2.0-darwin-arm64.zip`, and exact hash
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
Record that line verbatim. Preserve the complete response body as evidence.

## Return and stop

Return PASS/fail with request count, accepted host chain, statuses, body size,
body SHA-256, exact arm64 line, evidence paths/hashes, final Git state, and
fence posture. Even on PASS, stop. Do not inspect/alter the staged zip, source,
tests, manifests, package output, R18, status, receipt, or proof surfaces.

No implementation, tests, build, sync, review, artifact download, other
network, GUI, proof act, bootstrap/kickstart, operator mutation,
sign/notarize/deploy/release claim, stage/commit/push/PR/merge, or delegation.
