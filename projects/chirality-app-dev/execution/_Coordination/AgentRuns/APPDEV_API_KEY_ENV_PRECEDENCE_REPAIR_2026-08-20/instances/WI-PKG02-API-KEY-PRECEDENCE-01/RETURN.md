# Return — WI-PKG02-API-KEY-PRECEDENCE-01

RUN_STATUS: SUCCESS

## Outcome

N2 repaired and accepted the DEL-02-05 R03 IPC/status consumer against the
amended N1 credential-store source fact. Electron IPC now validates and
projects the daemon-owned non-secret `source: ui | env | none` discriminator
and performs no environment-source re-inference.

The integrated accepted order is UI safeStorage, `ANTHROPIC_API_KEY`, then
`CHIRALITY_ANTHROPIC_API_KEY`. Malformed or internally inconsistent daemon
replies fail closed; unavailable, store/remove, unsupported-provider, oMLX
isolation, and non-disclosure behavior is preserved.

## Product identities

- Accepted N1 `api-key-storage.ts`:
  `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db`
- Accepted N1 storage test:
  `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4`
- N2 `api-key-ipc.ts`:
  `3293cbf15164105ac61f7cc7e34da66c5c12701823a6e302f90d59c385eed3cb`
- N2 IPC test:
  `818b7424ef1de3f4418486a4a7ae839cb837d84a23af6fdd73621f847d74b1a6`

## Acceptance evidence

- Focused storage + IPC + settings Vitest: PASS, 3 files / 47 tests.
- Manager registered evidence: PASS, six checks:
  - frontend test: 150 passed / one skipped file; 1,174 passed / four skipped
    tests;
  - frontend typecheck and build: PASS;
  - harness pytest: 350 tests PASS;
  - harness self-check: PASS, unchanged four REVIEW / 31 WARN baseline; and
  - APP-HOLD integrity: PASS, register match and zero held deliverables.
- Final accepted-dependency-consumption APP-HOLD: ALLOW for DEL-04-05.
- Secret scan: PASS, 5,846 files, zero blocked findings,
  `rawSecretValuesWritten: false`.
- Exact scope, JSON, tracked/untracked whitespace, and N1 hash preservation:
  PASS.
- Fresh Review 02: PASS, 14/14 hashes, 1,050/1,050 product/test lines,
  Review-01 evidence finding closed, zero findings.

Evidence: `FROZEN_DIFF_MANIFEST.md`,
`N2_MANAGER_REGISTERED_CHECKS.json`,
`N2_APP_HOLD_RELIANCE_FINAL.json`,
`secret-scan/secret-scan-summary.json`, and
`../TASK-PKG02-API-KEY-STATUS-CONSUMER-REVIEW-02/RETURN.md`.

## DEL-02-05 calibration

The dated 2026-06-20 assessment is preserved and its overreaching R03 claim is
superseded by the 2026-08-20 R03 calibration. Assessment, status, memory, and
one run record now point to the proved behavior and gates.

DEL-02-05 remains `IN_PROGRESS`; Remaining remains empty. Dependencies,
ScopeOfWork, lifecycle, and Checking Approval SHA
`8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` are unchanged. No other
requirement was closed or advanced.

## Boundaries and disposition

No public/runtime contract, dependency, lockfile, provider/network,
credential-material, shared receipt/register/completion-log, Git, commit,
push, PR, merge, release, or lifecycle action was performed by N2.

MISSING: none

NEEDS_HUMAN_RULING: none

DEPENDENCY_NOTES: N2 consumed accepted amended N1 byte-identically. Agent 0
may accept this terminal handoff and release N3. Any frozen-byte or credential
serialization change requires proportional checks, refreeze, and fresh review.
