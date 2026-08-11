# Sealed brief — N3 fifth-lineage fresh packet verifier

- RequestedBy: `WORKING_ITEMS-DAPP93-L5-20260810`
- ChildInstanceID: `A2-DAPP93-L5-N3-VERIFY-01`
- PackageID: `D-APP-93 exact packet preparation`
- Objective: independently and read-only verify the manager-frozen packet
  against the accepted N1 ledger/provenance result, rulings, allowlist, hard
  zero-identity criterion, and frozen inventory.
- Dependencies: explicit manager N2 acceptance and freeze.
- DeclaredReads: exactly `allowlists/N3_READ_ALLOWLIST.txt`.
- AllowedTools: `apply_patch` and F01-F11 only.
- AllowedWriteTargets: `verification/STAGE_1_FREEZE_REPRODUCTION.md`,
  `verification/STAGE_2_LEDGER_COVERAGE.md`,
  `verification/STAGE_3_SEMANTIC_AND_AUTHORITY_REVIEW.md`,
  `verification/STAGE_4_FINAL_VERDICT.md`, and
  `returns/N3_FRESH_VERIFIER_RETURN.md`.
- EXCLUSIONS: packet and freeze files are read-only; every historical root is
  excluded except direct consultation of Stage 5/Stage 6 as allowlisted. The
  verifier must never repair an author output.

## Durable stages and shared clock

1. reproduce packet file hashes and aggregate approval token (6 minutes);
2. prove complete/exactly-once 80-row coverage and zero F02 hits (8 minutes);
3. substantive authority, sequencing, failure-route, evidence, cleanup,
   no-execution, and allowlist review (8 minutes);
4. terminal PASS/BLOCK and return (5 minutes).

Total expectation 27 minutes; first checkpoint not before minute 6, later
interval 8 minutes. Progress is durable file/byte growth. Native context
telemetry is unavailable unless exposed.

PASS requires unchanged freeze bytes, complete ledger coverage, literal
operations, coherent stop/failure/rollback routes, packet/index/return
completeness, zero historical identities, and exact approval-gate posture.
Any issue is BLOCK with evidence only. No edit, execution, or sixth lineage.
