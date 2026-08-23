# Sealed brief — A2-PKG09-R18-FULLTEST-CURE-01

## Identity and objective

- RequestedBy / Parent: `WI-PKG09-R18-STAGING-01`
- RunID: `APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22`
- ChildInstanceID: `A2-PKG09-R18-FULLTEST-CURE-01`
- Fresh ephemeral generalist Agent 2; no delegation
- Dependency: accepted whitespace executor return
- Objective: execute exactly one owner-authorized full-suite cure, preserve
  exact no-source-change evidence, update R18/status documentation, and
  harvest one TM candidate without acting on it.

## Allowed writes

- `repair-cycle-1/full-suite-cure/` evidence and return;
- existing R18 record
  `_run_records/R18_ELECTRON_SUPPLY_FREEZE_AND_OFFLINE_BUILD_2026-08-22.md`;
- minimal DEL-09-04 `_STATUS.md` amendment;
- `repair-cycle-1/TM_CANDIDATE_LOCAL_SOCKET_FIXTURE_SANDBOX_DETERMINISM.md`.

Do not touch source/tests/package.json/lock, the five repaired evidence files,
original review, package output, receipt, or other records.

## Pre-run freeze

Before the unrestricted run, require exact HEAD
`f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`, empty index, and the frozen
frontend candidate hashes:

- verifier `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`;
- wrapper `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db`;
- verifier test `c9c4af600a703afa995f8316ee04eb3160d72ef7f8cba8ec2ce53c7f952cb38d`;
- wrapper test `a66af130420412e5a3d9cf48856c1b416234fea5aa78e14e3867b4adfd7664e2`;
- package.json `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc`.

Create a complete pre-run frontend candidate diff that includes the tracked
package diff plus no-index additions for all four new files. Record its hash
and exact per-file hashes. Record the retained sandbox diagnostic log hash
after whitespace normalization and its 21 failed / 1,246 passed / 4 skipped
classification.

## Exact cure command

From exact cwd `projects/chirality-app-dev/frontend`, run exactly one command:

```text
npm test
```

Use the execution tool's owner-approved elevated/local-socket permission only
as necessary so loopback and Unix-socket test fixtures may bind. The command
string is exactly `npm test`: no env prefix, wrapper, pipe, redirect, or second
test command. Request no network URL and invoke no network tool. External
provider/network remains forbidden. Capture the complete tool output exactly
once into `full-suite-cure/npm-test.unrestricted.log` after the run without
rerunning; record exit and counts. Fail closed on nonzero.

Immediately after, reproduce the same five hashes and complete candidate diff;
require exact equality. No additional full-suite run.

## Documentation and harvest

Update R18/status only to:

- classify the retained diagnostic as `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`;
- record diagnostic counts and exact unrestricted `npm test` counts/exit/log;
- prove no source/test/package change between runs;
- retain package evidence-only/non-adopted and DEL `IN_PROGRESS`/unproved;
- name PR pre-merge release-quality wrapper `full_test` + typecheck as future
  independent confirmation of record, explicitly not yet observed;
- retain R19 separate/no proof.

Create the owner-attributed harvest-only TM candidate: mark local-socket
fixture tests with sandbox-detect skip-with-reason or use a separate Vitest
project so sandboxed runs are deterministic. State no implementation, row,
ruling, or disposition occurred.

## Checks and return

Refresh R18/status hashes, docs whitespace, candidate-wide whitespace/
staged-equivalent checks, JSON, receipt validator, APP-HOLD, self-check,
practitioner suite if documentation mapping requires, App-only containment,
exact inventory, and empty index. Do not rerun focused/typecheck/full tests,
pack, instruction-root, or network.

Return exact command count/cwd/permission classification, log/exit/counts,
pre/post source hashes/diff equality, documentation/TM hashes, checks, and
fresh-review requirement. No receipt/stage/commit/push/PR/merge/proof.
