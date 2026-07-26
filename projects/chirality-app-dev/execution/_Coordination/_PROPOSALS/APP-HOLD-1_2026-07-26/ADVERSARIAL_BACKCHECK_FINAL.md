# APP-HOLD-1 Durable-Authority Backcheck

Verdict: `ADMIT`

## Basis

`AUTHORITY_BACKCHECK_BASIS_HASHES.sha256` SHA-256:
`6e75c5349bde8121e06de8fb3eef37ee5c7003053bc1021595df3629f2802d46`

All 18/18 listed artifacts reproduced exactly at Git HEAD
`918bb48b8fcee66c031d0d6d4040a46089f96067`.

## AHB-001 disposition

`CLOSED`.

`D-APP-75_RULING_TEMPLATE.md` is unambiguously a non-ruling proposal:

- `Status: PROPOSAL_TEMPLATE_NOT_RULED`;
- `OwnerRuling: PENDING`;
- it expressly grants no application authority; and
- it requires exact owner acceptance plus final candidate identity before
  effectiveness.

`INTEGRATION_CONTRACT.md` names the complete durable
authority-and-application path:

- materialized D-APP-75 ruling record;
- App decision-register row;
- live hold register;
- tool and tests;
- App instruction surfaces;
- root tool registry; and
- App script catalog.

It also requires a collision check for D-APP-75 and returns for remint and
refreshed approval if that identifier is unavailable. The live App decision
register has no D-APP-75 at the frozen basis.

## Reproduction

- Fail-closed authority enforcement: verified. The tool requires
  `authority_basis == D-APP-75`; the preparation-only-authority fixture exits
  `2`.
- Full test suite: `12/12 PASS`.
- Live scan: `PASS`.
- Contracts scanned: `53`.
- Held contracts: exactly `6`:
  `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-05-04`, `DEL-08-02`,
  `DEL-08-03`.
- Register parity: exact.
- Repinning: none.
- Scan fingerprint:
  `dd8657773edc7ac57107a3741d19e8f348cf08382645a6c96a3347dd5e16ca4a`.
- Output-escape target: absent.

No new material defect was found. The only remaining act is the intended
human gate: owner approval must supply and transcribe the actual D-APP-75
ruling and final accepted candidate identity before application. This is the
designed authority boundary, not a warning.

## Reviewer attestation

No files were written, edited, staged, committed, or applied by the reviewer.
Git status remained limited to the four pre-existing untracked
proposal/evaluation directories.

Engine: Codex  
Provider: OpenAI  
Model: UNKNOWN
