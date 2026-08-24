# SCA-APP-008 Pointer Act — CHANGE Launch Brief

**RunID:** `APP_V3_POINTER_ACT_2026-08-24`
**Role:** `CHANGE` (Agent 1), dispatched by `HELP_HUMAN`
**Branch:** `codex/app-v3-pointer-act-2026-08-24`
**Basis:** `84fe4c6cef3771da8ccf63a0a6fb1d81804e7dfd`
**Upstream:** `origin/main` at the same commit; ahead/behind `0/0`
**Execution posture:** owner-authorized exact pointer application; fail closed

## Immutable direction

- Steer: `plans/steers/chirality_app_v3_pointer_act_steer_app_2026-08-24.md`, SHA-256 `ac7920b2adcf2d77835cb4989b956d1be4ae7c97fb70839c4e25fe83ffbcd5c1`.
- Ruling A9: `plans/steers/chirality_app_v3_app_ruling_record_a9_2026-08-24.md`, SHA-256 `6ce5534514b8298ab9cfff3c72ba7f0532a41f58278ef03cc6c4cdadf9b47178`.
- Basis contains Gate-5 merge `d5e40b3c25fe527919f1d2d2a31ea97ce2835795`.
- Receipt ledger validated before use; latest applicable cursor is `Receipt-199`.
- Selected committed workplan: `projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md`, Git blob `5f01938c92b719426e9c0716a5d5a3980cf78566`.

## Sealed objective

Perform only the pre-review transaction phase. After the exact basis gate and an immediate live pre-image recheck, atomically replace the live `_LATEST.md` pointer with bytes copied from the immutable `Phase5/_LATEST.proposed.md` snapshot. Record the transaction and return it for fresh independent review.

## Authorized write set for this phase

1. `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` — exact snapshot bytes only.
2. New evidence strictly under this RunID.

Receipt 200, staging, commit, push, PR publication, notice routing, and every other repository path are outside this phase.

## Basis gate — verified before first write

| Surface | Required identity | Observed identity | Result |
| --- | --- | --- | --- |
| Branch basis | `84fe4c6cef3771da8ccf63a0a6fb1d81804e7dfd` | HEAD and `origin/main` exact; ahead/behind `0/0`; porcelain empty | PASS |
| Gate-5 ancestry | `d5e40b3c25fe527919f1d2d2a31ea97ce2835795` | ancestor of `origin/main` | PASS |
| Live pointer | SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`; 1347 bytes; Git blob `c6ce8b2a92c67506887d95c88790a445dbc5668d` | exact | PASS |
| Proposed payload | SHA-256 `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`; 1572 bytes; 21 lines | exact; Git blob `cdccf5e6740a18ea4ecb2d556fbe3b2704d2c617` | PASS |
| Pointer candidate | SHA-256 `44c39e11b4de7621fe25d643d049443223ffbbcd8160855c3fb85d4a4186609a` | exact | PASS |
| App decomposition | SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` | exact | PASS |
| App contract | SHA-256 `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` | exact | PASS |
| Companion register | SHA-256 `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` | exact | PASS |
| Authority corpus | v19, no drift | all governed members match | PASS |

## Transaction and rollback protocol

Immediately before replacement, verify the live target again with `shasum -a 256`, `wc -c`, and `git hash-object`; all three must match the frozen pre-image. Copy the immutable snapshot to a same-filesystem temporary file, verify its identity, and rename it over the target as one atomic replacement. Then verify SHA-256, byte count, line count, and Git-blob agreement with the snapshot.

If any immediate precheck or postcheck fails, restore the live target from Git blob `c6ce8b2a92c67506887d95c88790a445dbc5668d`, verify byte-for-byte restoration, preserve evidence, and stop. No regeneration, retyping, substitution, or scope expansion is permitted.

## Review acceptance checks

- Every pinned basis identity is reproduced.
- Immediate pre-image re-verification evidence precedes the write.
- Applied bytes have snapshot provenance and exact post-image identity.
- Only the target pointer and this new RunID contain changes.
- Receipt 200 and Git publication have not occurred.
