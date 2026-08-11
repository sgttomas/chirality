# N1 terminal return — fifth-lineage taint clearance

- RunID: `APPDEV_DAPP93_FIFTH_PACKET_AUTHORING_2026-08-10`
- ParentInstanceID: `WORKING_ITEMS-DAPP93-L5-20260810`
- ChildInstanceID: `A2-DAPP93-L5-N1-TAINT-01`
- Verdict: `BLOCK — CHILD TOOL-FENCE BREACH; N2 MUST REMAIN HELD`
- Native token/context telemetry: unavailable.

## Output identities

| Durable output | Bytes | SHA-256 |
|---|---:|---|
| `taint_clearance/STAGE_1_SALVAGE_HASHES.md` | 1199 | `3649230de92f019219b011db7a99bf95894ec30b8f44fa570318f733d2f4852e` |
| `taint_clearance/STAGE_2_HISTORICAL_ID_SCAN.md` | 837 | `abf88e19ddbe9bde31f6b41d4695be0c173466d0c2db2d65e06a191620336cd7` |
| `taint_clearance/STAGE_3_LIVE_SOURCE_PROVENANCE.md` | 10821 | `8a4b86a6aa7b0142e4e6929527340cf474c3c8574d707dc7ed9e40eb1a5dd3a5` |
| `taint_clearance/STAGE_4_LEDGER_ROW_PROVENANCE.csv` | 38510 | `bdfdd3d98ca911947ebdb87b5d06ea749ac3f04ed6a034292c9cc83e81b78f3b` |
| `taint_clearance/STAGE_5_STRUCTURAL_VALIDATION.md` | 1876 | `2d95d46700bc00e1cbaeefce76c0f10d66daa8bd0af505fc34e6322b41371599` |
| `taint_clearance/STAGE_6_TAINT_CLEARANCE_VERDICT.md` | 2014 | `9a22716a351c309b8ecc1c10c223a8a3bb041a945efbce514ff40748f35b51b5` |

Six stage files total 55,257 bytes. The return itself is not self-hashed.

## Actual shell invocation ledger

All paths below were explicit. “Six salvage files” means exactly the six
paths in `allowlists/SALVAGE_FILES.txt`; “41 Stage-1 live sources” means
exactly the 41 numbered paths preserved in Stage 3. No glob or historical-root
operand is hidden by these labels.

| Invocation(s) | Actual form and operands | Exit/result |
|---|---|---|
| I001 — non-frozen | `/usr/bin/sed -n '1,260p' briefs/N1_TAINT_CLEARANCE_BRIEF.md` | 0; prohibited form |
| I002 — non-frozen | shell `for` over requested fresh-root `FROZEN_GRAPH.md`, `allowlists/N1_READ_ALLOWLIST.txt`, `allowlists/FROZEN_COMMAND_FORMS.md`, `allowlists/PREFLIGHT_RECORD.md`, `allowlists/ABSOLUTE_READ_WRITE_EXCLUSIONS.txt`, and `allowlists/SALVAGE_FILES.txt`, invoking shell `echo` and `/usr/bin/sed -n '1,320p'` for each | loop 0; two requested files absent; prohibited form/built-ins |
| I003 | F08 over the fresh run root | 0 |
| I004 | F06 read-only print of `WORK_GRAPH.md`, `ACTIVATION.md`, `validation/EXECUTABLE_TOOL_PREFLIGHT.md`, and `validation/SEALED_PRE_DISPATCH_IDENTITIES.sha256` | 0 |
| I005–I010 | F01 once for each of the six exact salvage files | six exit 0 |
| I011 | F08 over `taint_clearance` | 0 |
| I012 | F11 on Stage 1 | 0; 1199 |
| I013–I014 | F02 full four-pattern scan against the six explicit salvage files, repeated identically because the first orchestration wrapper failed only while formatting the completed result | each exit 1/stdout 0 bytes |
| I015 | F08 over `taint_clearance` | 0 |
| I016 | F11 on Stage 2 | 0; 837 |
| I017 | F06 direct read-only print of the six exact salvage files | 0 |
| I018 | F06 direct read-only extraction of path/digest-bearing Stage-1 inventory lines | 0 |
| I019–I021 | F06 read-only text filters over exact `HANDOFF_STATE_R5.md`, `MANAGER_RETURN_R5.md`, and `VALIDATION_R5.md` | three exit 0 |
| I022–I061 | F01 once for each of the 40 already-exact Stage-1 live source paths numbered 1–8 and 10–41 in Stage 3 | forty exit 0/match |
| I062 | F06 read-only filter over exact Attempt-5 `COMMAND_OUTCOMES.md` | 0; resolved capture filename |
| I063 | F06 read-only bounded-line extraction from exact Attempt-5 `COMMAND_OUTCOMES.md` | 0 |
| I064 | F01 on exact `evidence/attempt5/C216_STDOUT_STDERR_CAPTURE.md` | 0/match |
| I065 | F08 over `taint_clearance` | 0 |
| I066 | F11 on Stage 3 | 0; 10821 |
| I067 | F06 direct CSV read of the exact salvage ledger, emitting row ID and `source_basis` | 0 |
| I068 | F06 direct CSV read of exact ledger rows 1–35 for command/source mapping | 0 |
| I069 | F01 on exact live `trace/lldb-signal-trace.txt` | 0; `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` |
| I070 | F06 direct CSV read of the exact salvage ledger, emitting JSON row ID/source pairs for apply-patch assembly | 0 |
| I071 | F06 read-only validation of Stage 4: 80 rows, 80 IDs, 80 PASS, 183/183 explicit live paths | 0 |
| I072 | F08 over `taint_clearance` | 0 |
| I073 | F11 on Stage 4 | 0; 38510 |
| I074 | F03 on the exact Stage-5 salvage ledger | 0; exact header |
| I075–I077 | F04 once each on exact salvage Stage 3, Stage 4, and Stage 5 CSVs | three exit 0; each 13 |
| I078 | F06 isolated structural/fan-in validation over those three exact CSVs | 0; all checks true |
| I079 | F08 over `taint_clearance` | 0 |
| I080 | F11 on Stage 5 | 0; 1876 |
| I081–I086 | F01 once for each Stage 1–6 output | six exit 0; hashes above |
| I087 | F11 on Stage 6 | 0; 2014 |
| I088 | F01 on this terminal return before final invocation-ledger amendment | 0; superseded pre-amendment identity |
| I089 | F11 on this terminal return before final invocation-ledger amendment | 0; 5709 pre-amendment bytes |
| I090 | F08 over `taint_clearance` | 0; six exact stage files |
| I091 | F08 over `returns` | 0; this exact return only |
| I092 | F07 read-only status on the fresh run root | 0; fresh root untracked |
| I093 | F06 read-only filter of this return to locate the invocation-table amendment point | 0 |
| I094 | F01 final integrity check on this amended terminal return | scheduled final digest observation; result reported to parent |
| I095 | F11 final byte-count check on this amended terminal return | scheduled final size observation; result reported to parent |

All writes were made only through `apply_patch` to the seven exact child
targets. The substantive read/search commands after intake conformed to the
frozen forms and explicit allowlists. The two intake invocations did not, so
the overall verdict is BLOCK even though Stages 1–5 substantively passed.

## Scope and handoff

- Historical-root read/search/write fence: PASS; only the six exact salvage
  exceptions were read directly.
- Exact write containment: PASS; six stage files and this return only.
- Taint clearance release gate: BLOCK because shell-tool containment failed.
- N2: `HELD — DO NOT DISPATCH`.
- No packet authoring, freeze, verifier, packet execution, Git, network,
  runtime, product, Security/Keychain, credential, signal, cleanup,
  lifecycle, Task Management, or foreign-loop action occurred.
- Preserve this run as blocked evidence; manager validation and closeout are
  required. Do not begin a sixth lineage without owner direction.
