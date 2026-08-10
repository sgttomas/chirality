# Sealed brief — R4.4.6 attempt-2 intake and D-APP-94 fresh verifier

Role: genuinely fresh, read-only ephemeral Agent 2 adversarial verifier.

Objective: independently verify the immutable R4.4.6 attempt-2 returned
snapshot, derivative intake freeze, and non-decisional D-APP-94 environment
packet. Return PASS or BLOCK. Do not repair.

## Write scope

The sole permitted write is:

`reviews/A2_DAPP93_ATTEMPT2_INTAKE_DAPP94_FRESH_VERIFIER_RETURN.md`

No other file or state may change. No runtime, process inspection, signal,
package, helper/GUI, keychain, credential, product, Git, Task Management, or
foreign-loop action is permitted.

## Frozen candidate identities

- intake freeze:
  `R4_4_6_ATTEMPT2_INTAKE_FREEZE.md`, SHA-256
  `b5a5245f958a04889753a14db58d59e89defff7af37fb29a22aa7fed96830537`;
- D-APP-94 packet freeze:
  `DAPP94_DECISION_PACKET_FREEZE.md`, SHA-256
  `8107d832a01959a49e0993f7d3748171d4b40741fca943ada84aa67002dd6f4e`;
- D-APP-94 packet:
  `../../_DECISIONS/D-APP-94_PACKET_MISSING_KEYCHAIN_ENVIRONMENT_2026-08-08.md`,
  SHA-256
  `ce30c8fe04ee64263a3399c89753d84a167781092bc62bd7fa043fd6345709a6`;
- decision register:
  `../../_DECISIONS/_REGISTER.md`, SHA-256
  `5698122ebd7cdb8312b138d71c7c8439c3b2cf760f85fd9439825b8104f215ca`.

## Required checks

1. Reproduce the initial and final candidate hashes and every identity bound by
   both freezes. Any drift is BLOCK.
2. Treat `returned_r4_4_6/` as immutable. Require exactly 20 primaries and 20
   adjacent sidecars. `c1103.sha256.txt` is a primary and
   `c1103.sha256.txt.sha256.txt` is its sidecar. Reproduce all 20 pairings and
   the sorted-all-40 `name|byte_count|sha256\n` aggregate
   `97a9d3836b1b3a7557f4171f208a7ac55c4132a87d1a8ab956dc2fdef58c8110`.
3. Recompute the 22 ordered CONTROL marker ranges and exits. Require C1146.30
   as the last CONTROL input and no later input. Confirm step 14 and step 27
   are the only exit-1 markers.
4. Audit the frozen runbook and returned transcript. Confirm that runbook step
   14 required a stop on missing C1116 paths, C1116 found both paths missing,
   and step 15 nevertheless ran. The intake must classify step 14 FAIL and
   step 15 DEVIATION; it must not call the execution route-conformant.
5. Confirm the completed form is frozen and unedited. Verify the intake erratum:
   the `2026-08-08T05:57:26.027Z` `Unknown project: chirality-app-dev` line is
   in `gui.stdout.txt`, not `gui.stderr.txt`. Confirm C1118 was NOT_RUN and the
   line is supporting only, not a fresh-C1118 substitute or causal credit.
6. Reproduce C1105-C1108 complete outputs and exact two-record exits, all
   `command_exit=0` and `tee_exit=0`. Confirm C1108 built both packages from
   the D-APP-93 run root and the dependency-boundary check passed. Calibrate
   this as package/launch identity support only, not signal-path closure.
7. Validate returned helper/GUI PID evidence, addendum cleanup observations,
   applicable signal order, step-27 zero-row semantics, eight rollback hashes,
   empty C1141 output, fixed-root absence, and C196/C197 unused strictly from
   returned bytes and safe read-only filesystem checks. Do not inspect live
   processes.
8. Confirm the terminal verdict is STOP_INCOMPLETE and all eight signal-path
   causal cells remain UNKNOWN. Confirm no D-APP-88, DEL-09-04, TM-APP-036,
   product, remedy, release, or reliance conclusion follows.
9. Audit D-APP-94 as a neutral owner decision among A/B/C with a conditional A
   recommendation, exact preparation-only tokens, explicit risks/authority,
   evidence survival, affected surfaces, and later gates. Verify it decides
   nothing and grants no source/keychain/credential/execution authority.
10. Confirm the D-APP-94 row is unique and `AWAITING_RULING`. Confirm every
    future option still requires fresh C1118 and a separate repair of the
    step-14 observation/gate before any future attempt.
11. Read the relevant current `electron/api-key-storage.ts`, startup consumer
    surfaces, and tests only far enough to check that the option descriptions
    are plausible planning choices and that Option A remains conditional rather
    than asserting an already-proven bypass design.

The return must list exact evidence for every material finding and repeat the
final stability hashes. Stop after the sole return.
