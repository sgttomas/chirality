# N1 terminal return — staged source reconstruction and fresh ledger

RUN_STATUS: `FAILED`

Verdict: `BLOCK — EXCLUDED_ROOT_SEARCH_SCOPE_VIOLATION — N2 HELD`

RunID: `APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09`

ChildInstanceID: `A2-DAPP93-THIRD-N1-01`

RequestedBy: `WI-PKG09-DAPP93-THIRD-01`

## Durable stage returns

| Stage | Output | Bytes | SHA-256 | Result |
|---:|---|---:|---|---|
| 1 | `source_reconstruction/STAGE_1_SOURCE_INVENTORY.md` | 8851 | `108374dd11765af00dfb8ebab6edd13a05e6cfa9a3544a5bc553bf42edc71625` | accepted non-draft corpus bounded; retained candidate bytes independently concordant with accepted package evidence |
| 2 | `source_reconstruction/STAGE_2_AUTHORITY_SEMANTICS.md` | 9227 | `7dbd151853ded2f65101e72287a42ef1d000dc73be35c4a388e09dbece431bf6` | owner-operated and isolated sealed-HOME semantics aligned; exact-hash gate required for every future row |
| 3 | `source_reconstruction/STAGE_3_COMMAND_EXTRACTION_CORE.csv` | 23816 | `37c11862375a70f7335a4010f0608b8da9028141f81b58304f90a365a68cbb5b` | 43 core rows, contiguous through the frozen-script target gate |
| 4 | `source_reconstruction/STAGE_4_COMMAND_EXTRACTION_SAFETY.csv` | 19065 | `c518dff8162feab3e85c37dac53761ad955187800301212b7c48b372be61018d` | 37 safety/trace/replay/return/cleanup rows |
| 5 | `source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv` | 42705 | `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809` | complete 80-row ledger |
| 6 | `source_reconstruction/STAGE_6_LEDGER_ALIGNMENT_CHECK.md` | 7481 | `9b50c68b74a94232acca87de7cca48f0d55987c92578c27ca0ef9a8078c3ed5c` | mechanical checks pass; N1 blocked by absolute-exclusion search-scope violation |

Each stage was written durably when completed and reported immediately to the
manager with path, byte count, coverage, and next stage. Later audit-driven
amendments to already-completed stages were also immediately reported with
old/new byte counts and final hashes.

## Ledger acceptance evidence

- CSV fan-in: Stage 3 rows followed by Stage 4 rows equal Stage 5 rows field
  for field.
- Schema: exactly the 13 required columns on every row.
- Membership: exactly 80 command/operator-input rows.
- Namespace: contiguous and unique `L3-CMD-001` through `L3-CMD-080`.
- Empty required fields: zero.
- Owner-approval variance: zero; every row requires approval of the exact
  frozen packet hash.
- Missing failure routes: zero.
- Missing cleanup/rollback/retention dispositions: zero.
- Actors: owner terminal, owner GUI, or owner debugger input only.
- Authority classes: new owner-operated operation, exact preserved debugger
  fence, or explicit owner attestation only.
- Manager-defined historical command-identity scan: `0 matches`, exit `1`,
  stdout `0 bytes` on the final ledger and independently on every staged
  output.
- Excluded blocked-root basename scan: zero hits in the final ledger.
- Prohibited expansion scan: zero explicit-unlock, rejected-password-store,
  force-kill, network-client, signing/notarization, generic-password lookup,
  process-environment, or environment-dump commands.

## Coverage

The ledger is complete across preflight, source reconstruction, dependency
projection, local offline package construction, package identity/topology,
isolated HOME and disposable login-keychain preparation, exact helper and GUI
launch, direct-child PID binding, debugger attach/input, the first signal,
bounded trace and replay observations, raw evidence return, universal
stop/deviation retention, owner-state comparison, isolated-keychain cleanup,
source rollback, derivative/root cleanup, ingestion preparation, and terminal
status.

No retry, alternate PID, process census, second terminal, supervisor,
forwarder, watchdog, privilege/entitlement change, force signal, owner-keychain
write, credential lookup, memory/environment dump, network fetch, signing,
distribution, product acceptance, release, reliance, Task Management, or
foreign-loop action is present.

## Blocking compliance incident

One Stage 3 read-only discovery command used `rg -l` broadly under the project
with intended blocked-root exclusion globs that did not match as written. Its
returned path list included files inside all three absolute-exclusion blocked
roots. Because content search necessarily read those files, the command
violated the sealed brief even though no excluded content was displayed,
cited, copied, or used in the ledger.

The mechanically complete ledger and zero historical-identity scan are
preserved evidence only. They are not accepted N1 fan-in. No child retry or
replacement is authorized in this lineage, so N2 is held.

## Authority boundary

N1 performed source reads, deterministic static checks, hashing, and the seven
authorized durable writes only. N1 did not execute any represented package,
build, runtime, debugger, signal, Security/Keychain, cleanup, product, Git, or
evidence-ingestion command.

The ledger and this blocked return authorize nothing. No prepared packet and
no execution authority exist.

## Missing

- A compliant N1 run that honors the absolute excluded-root read boundary.
- N2 packet authoring, manager validation, freeze, and fresh verification were
  not dispatched.

## Needs human ruling

- Manager closeout of this third lineage with preserved evidence, validation,
  receipt, and the required three-failure causal comparison.
- Owner direction is required for any future lineage. N1 requests no retry.

## Dependency notes

N2 and every later node are held. The manager must not accept or route this
ledger downstream despite its mechanical completeness.
