# Recovery activation — lost attempt-3 command ledger

- Parent: `HELP_HUMAN`
- Manager: `WORKING_ITEMS` Agent 1
- Scope: recovery only within
  `APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_2026-08-09`
- Objective: recover the exact last-known bytes of the blocked-snapshot
  `prepared/COMMAND_AUTHORITY_LEDGER.md` into the distinct path
  `recovery/COMMAND_AUTHORITY_LEDGER_RECOVERED.md`.

## Pinned identity and live observation

- authoritative recovery pin: `BLOCKED_DRAFT_SNAPSHOT.md`, SHA-256
  `e35e1c54087324b862f12368b3ca7cee123e635a117ac9787fdaece34febdefb`;
- pinned ledger SHA-256:
  `8577d875c97b1f2af7a88e83bd0734d1eab48efaa2f7d6d464fe405de563e0dc`;
- live observation at recovery entry: the original
  `prepared/COMMAND_AUTHORITY_LEDGER.md` is absent;
- recovery destination was absent at entry.

Use the original interrupted remediation child session and only its preserved
session context. Do not dispatch a new reconstruction author and do not infer,
synthesize, normalize, or guess missing bytes. Exact SHA match is the only PASS.

## Writes and exclusions

Manager writes are limited to distinct recovery control/return records under
this run root. Child writes are limited to:

- `recovery/COMMAND_AUTHORITY_LEDGER_RECOVERED.md`;
- `recovery/CHILD_RECOVERY_RETURN.md`.

Do not write `prepared/**` or alter any existing file. Execute no operational
or packet command, C1118 act, token, Security/Keychain/Electron/package/LLDB/
runtime/network/credential/product/Git/Task-Management/receipt action. This
tranche has no freeze or verifier stage.
