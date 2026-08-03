# WORKING_ITEMS Activation — D-APP-86 Option A

RunID: `APPDEV_PARITY_INSTRUMENT_2026-08-03`

InstanceID: `WI-PKG09-DAPP86-A`

Parent: App `HELP_HUMAN`

Package: `PKG-09 Validation, Packaging, Security, and Release`

Selected deliverable: `DEL-09-04 macOS DMG Packaging and Instruction Root Integrity`

Representation: `SOW_V1`

Status: `ACTIVATED — EXECUTION EVIDENCE ONLY`

## Authority and accepted basis

- Owner ruling: D-APP-86 Option A, ruling SHA-256
  `b6d927259dc7ee706d019b395aeedb9d38e409c2b132797c515fa168169241e8`.
- Selected packet: SHA-256
  `80c5bd5d752715eb69f10aa510ded3d6856bc5f036a48018d352401b3e8921d6`.
- App software workflow profile: SHA-256
  `97b6717a5991549367aa098629fbd7140bce7c7c226a15ef9419c0c3397f65e9`.
- DEL-09-04 ScopeOfWork: SHA-256
  `3692eec8e5fc8720c5615e6e5bae970e84bb40afe4bb6a2c09c88c3c632bdd8d`.
- DEL-09-04 live status at activation: `IN_PROGRESS`, SHA-256
  `404b5e39a599d62c4d03a54cae65d00155428553133467d215a92ab4d066411a`.
- D-APP-89 migration manager return and handoff: SHA-256
  `db5022bfb43381a0c9997402e3cd4e32b81cfe4b028787d2993eb7cf3514dfc7`
  and
  `1dd896ee223d07d39e671b146c98dd2428e0b8dc373bab6d0c5602f47dfed3a0`.
- D-APP-88 R2 blocked manager return and handoff: SHA-256
  `4ed34171427ddb7edaee02495ce7e21b1b5c6ad6ba675fe42f53ee99ab56d2a5`
  and
  `5ff048a4452e546c0b1b97481c1b8456eee2ad1a9d33cd219ab4d553f1d8c918`.

The live source basis is `HEAD`
`97678a841ef58345c73d3470ed8de57c9b1405d2` plus the uncommitted accepted
D-APP-89 App migration candidate. At activation, the complete binary diff
under `projects/chirality-app-dev/frontend/` hashes to
`09d244e3aff0cc73133c1a2cd93b88ee98de13557bf082b744b97a6012e6a7e2`
and names 111 tracked paths plus the untracked dedicated rollback probe
`frontend/src/__tests__/lib/harness-contract-rollback.test.ts`. The executor
must freeze a file-level source manifest before build and prove it unchanged
after all observations.

## Objective

Build exactly one unsigned local packaged App from the frozen current source,
run it with an isolated packaged daemon and isolated App/user-data posture,
and record the four D-APP-86 observations under one source/package/evidence
manifest:

1. Workbench opens, preserves its governed content/interaction boundary, and
   returns without route or state corruption.
2. Pipeline opens, preserves its governed dispatch boundary, and returns
   without route or state corruption.
3. Guarded navigator selection changes the selected recorded session without
   mutating a turn in flight or crossing the read-only replay boundary.
4. A real daemon-owned session with transcript events renders at least one
   transcript item with session/event provenance and preserved manager/child
   attribution wherever the fixture run actually records such attribution.

## Ownership and write boundary

This manager owns only the derivative run package under this directory and
ignored/generated package/check outputs created by the exact validation
commands. No tracked product change is authorized. No other package's
deliverable status, pointers, or run records are written in this activation;
successful cross-package reconciliation is returned to App `HELP_HUMAN`.

## Frozen constraints

- The current accepted package is the shared-identity package. D-APP-88 Option
  B is not implemented and remains blocked.
- Any later accepted D-APP-88 helper implementation is a mandatory rerun
  trigger for this parity evidence.
- D-APP-89's zero-ordinary-facade-consumer migration is preserved.
- No signing, notarization, publication, distribution, issuance, release,
  lifecycle advancement, professional-reliance claim, generic runtime work,
  Agent-2 Bash policy expansion, provider/network expansion, or D-APP-88
  closure is authorized.
- No Root/Piping/PEC/foreign-loop, Task Management, decision, PRD,
  decomposition, SCA, receipt, source-corpus, completion-log, or Git write is
  authorized.
- The six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations remain untouched.

## Return contract

Return the six D-APP-86 named evidence outputs, child returns, telemetry,
secret/containment/cleanup checks, fresh-verifier verdict, derivative handoff,
and a claim-calibrated notice to `HELP_HUMAN` naming DEL-02-02, DEL-08-02, and
DEL-05-04 for later package-local pointer/status reconciliation.
