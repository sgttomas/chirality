# A2-PKG09-R19-REVIEW-R1-01 sealed brief

Status: `FROZEN`

## Identity and write scope

- Fresh ephemeral generalist Agent 2; no delegation
- Parent: `WI-PKG09-R19-STAGING-01`
- Write only:
  `instances/WI-PKG09-R19-STAGING-01/repair-cycle-1/review/`
- Do not modify any reviewed byte.

## Objective

Freshly review repair cycle 1 and the complete R19 candidate. Return
`VALIDATED_PASS_WITH_RETAINED_TEST_LIMITATION` only if both original findings
are exactly repaired, the prior complete matrix remains supported, and the
Pi/oMLX cure failure remains claim-calibrated; otherwise return exact findings.

## Frozen repair inputs

- repair return SHA-256:
  `4c606d4e7b8798e6998e61e781c377b3e159e6e0868b6fddd684a69cc7d013c0`
- restored log: 16,098 bytes, SHA-256
  `2c0229474bad89dce1ced7e1303a2cd5b5bff0d0df3624dd5cd850baf1cb2db8`
- recovered field: 9,588 bytes, SHA-256
  `0f1611f07c7a52900d89bd60f8702986555435a632305542e73b400f29e155b3`
- repaired R19 SHA-256:
  `0d0a1246d0473a9e6bc6d5e0dd6e44f3eba64ecfee5c0244603fb4aeab768234`
- unchanged status SHA-256:
  `852bb42d8d593f9f34beec1b834b37b2a223669718a2f29112a985a69eadaf8a`
- immutable original review SHA-256:
  `253ae21c59f5de81e80a67541a38df1e881c3ef6d2a3973f21d4c8b06ed19712`

## Required matrix

1. Independently verify deterministic gzip preimage, old log hash/size,
   recovered-field hash/size and exactly-once occurrence, exact preimage
   prefix/suffix identity, restored log hash/size, and absence of suppression
   marker. Verify no byte outside the exact marker replacement changed.
2. Verify the restored log carries the complete retained output and preserves
   custom electronDist, no download/GitHub/release-assets indicator, builder,
   dependency, instruction-root exact revision, and exit gates. No pack rerun.
3. Verify R19 log hash/completeness pointers and exact top result:
   `SUBSCOPE PASS / TRANCHE VALIDATION NOT PASS — UNSIGNED OFFLINE PACKAGE,
   EMPIRICAL PRECHECK, AND OWNER-PROCEDURE STAGING PASSED; RETAINED FULL-SUITE
   CURE REMAINS NON-PASS`. Confirm dependent wording remains consistent and
   no proof/product/lifecycle/release overclaim exists.
4. Confirm status, source/test/package hashes, app/CLI hashes, executor return,
   and original review remain unchanged. Confirm no command rerun or mutation
   outside allowed repair bytes.
5. Re-evaluate the prior review matrix from retained evidence: basis/supply/
   package/guard, empirical direct-daemon health and cleanup, staged R19 block
   safety, semantic equality, DEL state, fences, containment, and index.
6. Preserve the sandbox diagnostic and local-socket cure as NOT PASS. Confirm
   the sole 504 remains supported as
   `PRE_EXISTING_TEST_HARNESS_TIMING_FLAKE_ENVIRONMENT_LIMITATION`, not a
   product defect and not a passing suite. No reproduction or rerun.
7. Run only read-only hash, byte comparison, JSON/JSONL, whitespace/no-index,
   diff, containment, inventory, and index checks. Do not run any test, pack,
   build, precheck, preflight, network/provider, proof, or operator command.

Write `repair-cycle-1/review/REVIEW.md` with exact verdict, hashes, inventory,
findings, and retained limitation. No additional write target is authorized.
