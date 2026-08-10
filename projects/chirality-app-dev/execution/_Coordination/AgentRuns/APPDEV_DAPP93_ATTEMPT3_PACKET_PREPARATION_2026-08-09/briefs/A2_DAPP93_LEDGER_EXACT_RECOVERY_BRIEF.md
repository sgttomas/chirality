# Sealed brief — exact recovery of lost attempt-3 ledger

- RequestedBy: `WORKING_ITEMS`
- Parent run: `APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_2026-08-09`
- Child: original `A2-DAPP93-A3-REMEDIATE-01` session only
- Objective: recover exact preserved bytes, not reconstruct content

Read `RECOVERY_ACTIVATION.md` and `BLOCKED_DRAFT_SNAPSHOT.md`. The expected
SHA-256 is exactly
`8577d875c97b1f2af7a88e83bd0734d1eab48efaa2f7d6d464fe405de563e0dc`.

Use only exact bytes preserved in your original session context, such as the
exact final patch/content you previously applied. Do not read sibling draft
documents to regenerate semantics, do not reconstruct from prose, do not edit
or improve content, and do not guess. If exact bytes are unavailable in
preserved context, write only `recovery/CHILD_RECOVERY_RETURN.md` with status
`RECOVERY_BLOCKED_EXACT_BYTES_UNAVAILABLE`; do not create the recovered ledger.

If exact bytes are available, use `apply_patch` to create exactly:

`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_2026-08-09/recovery/COMMAND_AUTHORITY_LEDGER_RECOVERED.md`

Then hash it independently. Write
`recovery/CHILD_RECOVERY_RETURN.md` recording:

- recovery source: exact preserved original-session bytes;
- destination;
- observed SHA-256;
- exact expected SHA-256;
- `RECOVERY_MATCH` or `RECOVERY_BLOCKED_EXACT_BYTES_UNAVAILABLE`/
  `RECOVERY_MISMATCH`;
- files written and exclusions honored.

AllowedWriteTargets are only the recovered ledger and child return above.
Do not alter any existing file or `prepared/**`. Do not delegate. Execute no
packet/operational/Security/Keychain/Electron/package/LLDB/runtime/network/
credential/product/C1118/Git/Task-Management/receipt action. No freeze or
verifier follows from your return.

