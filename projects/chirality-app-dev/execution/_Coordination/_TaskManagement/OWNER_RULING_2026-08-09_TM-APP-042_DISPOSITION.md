# Owner Ruling and Executed Disposition — TM-APP-042

Date: `2026-08-09`

Row: `TM-APP-042` — Retained D-APP-94 probe-root cleanup disposition
(`OPEN`, `MEDIUM`, owner-initiated 2026-08-09).

Authority: direct owner ruling by Ryan C Tufts in the HELP_HUMAN (Agent 0)
session on 2026-08-09, under the row's recorded resolution path
(`TASK_MANAGEMENT owner-gated bounded disposition; A=human-only`) and the
accepted terminal session handoff SHA-256
`06a3b3ddea0ba1267cfb2d31bbe9463bcea3e9b0f146158643a02172b7307088`, which
recorded the retained roots and deferred their disposition to a separately
gated owner act. The bounded act was executed by HELP_HUMAN at the owner's
direction immediately after the ruling.

## Ruled and executed act

Delete exactly the three retained D-APP-94 probe roots on `/private/tmp` and
nothing else. All accepted repo evidence namespaces remain byte-untouched.

## Before-state verification (read-only, fail-closed gate)

Immediately before deletion, an independent inventory of each root reproduced
the accepted handoff identities exactly — file count, total bytes, and the
sorted `relative-path<TAB>bytes<TAB>sha256` set digest:

| Root | Files | Bytes | Set digest (reproduced) |
|---|---:|---:|---|
| `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809` | 294 | 308571263 | `39637ef58b171384fd13365cbdb400103d82a2884146f9601be0e71352e950d1` |
| `/private/tmp/chirality-dapp94-option-c-keychain-probe-r5-20260809` | 322 | 308592165 | `c3aa1f9b165fa5e2067636a2a1106ba136f0699cac4d91fef23492ba0bddef07` |
| `/private/tmp/chirality-dapp94-option-c-keychain-probe-r7-20260809` | 313 | 308592253 | `29faef9a6f5eebc7474d3d455a7dec395752f73085b293bb6db6117a61933244` |

The bytes deleted were therefore byte-identical to the closure-time inventory
in the accepted handoff. All discovery evidence remains preserved in the
accepted R4/R5/R7 repo intakes; the deleted bulk was reproducible
extracted-Electron state derived from the hash-pinned cached archive
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.

## After-state verification

- All three roots verified absent immediately after deletion.
- Repo evidence namespaces verified intact immediately after deletion:
  `returned_r8/` contains 134 objects and `returned_r4_4_6/` contains 40
  objects; no repo path was written, moved, or deleted by this act.
- Approximately 925 MB was reclaimed.

## Requested register effect at next TASK_MANAGEMENT invocation

Close `TM-APP-042` as `RESOLVED_BY_DECISION`, citing this record as the
disposition evidence. This record grants no other authority; no product,
package, runtime, keychain, credential, Git, or foreign-loop effect occurred.
