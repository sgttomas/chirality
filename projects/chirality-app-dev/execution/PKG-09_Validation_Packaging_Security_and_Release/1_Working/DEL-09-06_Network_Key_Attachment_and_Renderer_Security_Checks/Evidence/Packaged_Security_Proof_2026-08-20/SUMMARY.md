# Packaged security proof — 2026-08-20

## Verdict

- Proof implementation: **PASS**.
- DEL-09-06 acceptance closure: **BLOCKED**.
- Subject: fresh unsigned macOS app built from source revision
  `357a58b56726feba49507534159c3fbc4656b818`.
- Packaged identity SHA-256:
  `4eba146b2f4a973c9f2b1e53629878502ecc76eace8508ad403dd959bcef5255`.

The passing host proof exercised the packaged executable and `app.asar`, not a
repository-dev substitute. It proved an isolated safeStorage fixture
store/status/remove cycle, encrypted non-plaintext storage with owner-only
mode, provider isolation, no retained fixture material, packaged security-byte
presence, a blocked renderer probe/diagnostic, five descendant process/TCP
snapshots, and zero non-loopback outbound TCP.

Acceptance cannot close because the packaged production implementation still
resolves `CHIRALITY_ANTHROPIC_API_KEY` before `ANTHROPIC_API_KEY`. DEL-09-06's
accepted order is UI safeStorage, `ANTHROPIC_API_KEY`, then
`CHIRALITY_ANTHROPIC_API_KEY`. The executable expected-failure regression is
retained in `frontend/src/__tests__/electron/api-key-storage.test.ts`; the
semantic repair belongs to DEL-02-05 R03 / DEL-04-05 RQ-001 and was excluded
from this proof-only write scope. The exact DEL-09-06 Remaining item therefore
stays open.

## Primary evidence

- `packaged-host-attempt-2/summary.json` — passing packaged host proof and
  artifact identity.
- `packaged-host-attempt-2/tcp-snapshots.json` — descendant TCP samples.
- `packaged-host-attempt-2/packaged-daemon.log` and
  `packaged-host-attempt-2/packaged-gui.log` — retained redacted host logs.
- `registered-product-checks-final.json` — full frontend tests, typecheck,
  build, and APP-HOLD integrity, all PASS.
- `source-network-policy-attempt-3/summary.json` — passing source renderer
  egress proof after two retained proof-loop attempts.
- `instruction-root/summary.json` and `instruction-root/manifest.json` —
  packaged instruction-root integrity PASS.
- `secret-scan/secret-scan-summary.json` — initial secret scan PASS; the final
  normalized scan is retained alongside this package after fan-in.

## Proof-loop attempts

- Packaged attempt 1 failed fail-closed because the per-user macOS temp path
  exceeded the AF_UNIX socket-path limit. The retained daemon log records
  `listen EINVAL`. Proof glue was corrected to use the canonical short `/tmp`
  alias; attempt 2 passed.
- Source network attempts 1 and 2 failed fail-closed while removing an obsolete
  owner-daemon dependency. Attempt 3 passed with an isolated user-data root and
  explicit renderer-egress boundary. Provider policy remains separately
  exercised by the focused/full automated security tests.

## Exclusions preserved

No real credential, signing, notarization, publication, release, provider
expansion, owner user-data mutation, daemon deployment, lifecycle transition,
Checking Approval SHA change, decision/register edit, lockfile change, commit,
push, PR, or merge occurred.
