# Frozen manager command and path allowlist

Status: `FROZEN BEFORE N1 DISPATCH`

## Command forms after graph freeze

| ID | Exact executable/form | Purpose |
|---|---|---|
| M01 | `/usr/bin/python3 manager/MATERIALIZE_INPUTS.py` | create complete deterministic N1 inputs and M0 validation |
| M02 | `/usr/bin/python3 manager/VALIDATE_PACKET.py --phase fanin` | deterministic post-N1 validation and harmless probes |
| M03 | `/usr/bin/python3 manager/VALIDATE_PACKET.py --phase freeze` | immutable packet manifest/freeze validation |
| M04 | `/usr/bin/python3 manager/VALIDATE_PACKET.py --phase closeout` | final containment/inventory validation |
| M05 | `/opt/homebrew/bin/git status --short --branch` | scoped repository status observation |
| M06 | `/usr/bin/wc -c <exact-file-list>` | durable output telemetry |
| M07 | `/sbin/sha256sum <exact-file-list>` | exact identity observations only |
| M08 | `apply_patch` | manager-owned files inside this run root only |
| M09 | governed `spawn_agent` / `send_message` / `wait_agent` | sealed N1/N2 dispatch and supervision |
| M10 | `/usr/bin/python3 manager/OBSERVE_PROGRESS.py` | fresh-root durable file/byte/fill telemetry only |

No shell loop, glob, recursive search, root traversal, or command substitution
is permitted. The Python scripts contain their own closed exact operand lists.

## Exact manager read roots

- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/`
  - exact D-APP-93 ruling file
  - exact D-APP-94 Option-A ruling file
- exact live D-APP-92 trace script:
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/trace/lldb-signal-trace.txt`
- exact fifth-lineage authorized citation/hash exceptions only:
  - `taint_clearance/STAGE_2_HISTORICAL_ID_SCAN.md`
  - `taint_clearance/STAGE_4_LEDGER_ROW_PROVENANCE.csv` (hash only)
  - `taint_clearance/STAGE_5_STRUCTURAL_VALIDATION.md`
  - `taint_clearance/STAGE_6_TAINT_CLEARANCE_VERDICT.md`
  - `NORMALIZATION_AMENDMENT.md`
- this fresh eleventh run root.

All other paths under the eleven roots in `allowlists/HISTORICAL_ROOT_FENCE.txt`
are prohibited. (The file enumerates the ten closed lineages plus attempt-3's
two separately preserved roots, yielding eleven path entries.) No content from
a prior authored packet may be read.
