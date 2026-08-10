# D-APP-93 R4.4.5 stale prior-run-root sweep and successor repair plan

Status: `READ-ONLY SWEEP COMPLETE — SUCCESSOR REPAIR HELD FOR OWNER EVIDENCE`

This is a bounded plan, not an amendment or execution authority. No prepared
or frozen byte may change, and no successor freeze or verifier may be created,
until the owner completes the current terminal route and returns its immutable
evidence for intake.

## Sweep scope and method

The read-only sweep searched the complete R4.4.5 `prepared/` corpus and its
live control surfaces—command inventory, branch/raw-byte matrix, host-path
audit/backcheck, and manager freeze—for the prior D-APP-92 fixed-root literal
`/private/tmp/chirality-dapp92-option-a-20260804` and its run-local path. It
also read the exact reused Attempt-5 overlay script, SHA-256
`ba5142bfd3e4ee62a48a1acf663862a357b4790b48f66a33e8bd807148ab208b`.

## Findings and classification

1. **Operational stale root — repair required.** The reused Attempt-5 overlay
   hard-codes
   `/private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip`
   and writes that value into both `electron-builder.runtime-helper.json` and
   `package.json`. Frozen C1102 invokes that prior-run-owned script even though
   C1100 places the archive at
   `/private/tmp/chirality-dapp93-owner-operated-20260807/electron-dist/electron-v43.2.0-darwin-arm64.zip`.
2. **Operational provenance pointer — repair required.** C1102 and the package
   reconstruction manifest point to the D-APP-92 Attempt-5 overlay. The method
   may be reused, but the live successor overlay/config must be D-APP-93-owned
   and bind the D-APP-93 fixed root.
3. **Descriptive stale-root sentence — mechanically update with successor.**
   The manifest's preparation-time absence statement names the old D-APP-92
   fixed root. It is not the immediate cause, but a successor live manifest
   must state the correct D-APP-93 root/status rather than retain a misleading
   prior-run absence as its current operational condition.
4. **Intentional preserved provenance — no repair.** Preserved C196 and the
   LLDB static revalidation point to the original D-APP-92
   `trace/lldb-signal-trace.txt`. This is explicitly owner-approved byte-exact
   provenance, independently bound by the prepared script SHA-256
   `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.
   It is not a stale temporary-root reference and must remain unchanged.
5. No other live prepared/control surface contains the D-APP-92 fixed-root
   literal. Historical D-APP-92 citations that do not control a current temp
   path remain provenance, not repair targets.

## Bounded successor repair

After current-route evidence is returned and accepted for repair intake:

1. Create one D-APP-93-owned prepared overlay script by preserving the accepted
   Attempt-5 method and changing its single `electronDist` value to
   `/private/tmp/chirality-dapp93-owner-operated-20260807/electron-dist/electron-v43.2.0-darwin-arm64.zip`.
2. Recompute and freeze the D-APP-93 overlay-script SHA-256 and the two exact
   post-overlay whole-file hashes produced from the already-frozen pre-overlay
   inputs. Do not promote the failed run's generated config bytes as a new
   basis.
3. Change only C1102's overlay-script operand to the D-APP-93-owned script.
   Preserve every other operation byte. C1100 already targets the correct
   archive, and C1103/C1104 remain the raw hash/config evidence producers.
4. Update only mechanically affected ledger purpose/cross-reference text,
   package manifest overlay identity/path and expected config hashes,
   ingestion expectations, prepared packet index, future owner token,
   successor backcheck/freeze, and necessary same-run cross-references. Touch
   runbook or command inventory only if their bound identities require it;
   do not alter route semantics.
5. Prove the command delta is exactly the C1102 script-path substitution;
   prove the overlay source delta is exactly the D-APP-92→D-APP-93
   `electronDist` substitution; prove all other command/sub-input digests,
   C196/C197 rows, ordinary C1145→C1144→C1130 order, terminal cut, raw packet,
   manifest cleanup repair, and unaffected prepared hashes unchanged.
6. Repeat the absolute-executable and stale-root sweeps. Require zero live
   D-APP-92 temporary-root literals and classify the preserved D-APP-92 C196
   script path explicitly as intentional provenance.
7. Freeze the successor and stop for HELP_HUMAN acceptance. Only after that
   acceptance may exactly one genuinely fresh, read-only verifier audit the
   bounded repair and return PASS/BLOCK without repair.

No implementation, freeze, verifier dispatch, new owner token, or execution
receipt is authorized by this plan. Current state remains held for completion
of the dispositioned Post-first-write/pre-C196 route and owner-returned raw
evidence.
