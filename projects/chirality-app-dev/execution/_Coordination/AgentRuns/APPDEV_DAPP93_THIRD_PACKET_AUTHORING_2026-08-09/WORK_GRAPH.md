# Frozen work graph v1 — D-APP-93 third authoring lineage

Selection authority: exact owner direction dated 2026-08-09.
Posture: serialized terminal fan-out/fan-in.

| Node | Objective | Writes | Depends on | Release gate |
|---|---|---|---|---|
| N1 | staged source reconstruction and fresh command ledger | `source_reconstruction/**`, `returns/N1_TERMINAL_RETURN.md` | activation | every staged output, terminal return, manager ledger acceptance and zero-ID scan |
| N2 | author complete packet, index, and terminal return against accepted N1 ledger | `packet/**`, `returns/N2_AUTHOR_RETURN.md` | accepted N1 | complete ledger coverage; zero historical IDs; coherent packet/index/return |
| N3 | manager fan-in validation | `validation/MANAGER_PACKET_VALIDATION.md` | accepted N2 | all acceptance checks pass |
| N4 | freeze all governed packet bytes | `freeze/**` | accepted N3 | deterministic manifest and packet hash; no post-freeze mutation |
| N5 | exactly one genuinely fresh read-only verifier | `briefs/N5_FRESH_VERIFIER_BRIEF.md`, `reviews/N5_FRESH_VERIFIER_RETURN.md` | accepted N4 | verifier PASS bound to exact freeze |
| N6 | manager return and approval-gate handoff | manager terminal records | accepted N5 | STOP at exact hash-bound owner approval gate |

N2-N6 remain held until their predecessors are accepted. No retry or
replacement chain is pre-authorized. A governed child failure closes this
lineage blocked; a fourth lineage may not be started or implied.

## N1 staged pacing and observability

| Stage | Durable completion output | Expected duration | Cumulative checkpoint boundary |
|---|---|---:|---:|
| 1 | `STAGE_1_SOURCE_INVENTORY.md` | 10 min | 10 min |
| 2 | `STAGE_2_AUTHORITY_SEMANTICS.md` | 12 min | 22 min |
| 3 | `STAGE_3_COMMAND_EXTRACTION_CORE.csv` | 15 min | 37 min |
| 4 | `STAGE_4_COMMAND_EXTRACTION_SAFETY.csv` | 15 min | 52 min |
| 5 | `STAGE_5_COMMAND_AUTHORITY_LEDGER.csv` | 18 min | 70 min |
| 6 | `STAGE_6_LEDGER_ALIGNMENT_CHECK.md` | 12 min | 82 min |
| terminal | `returns/N1_TERMINAL_RETURN.md` | 8 min | 90 min |

The credible total budget is 90 minutes. The first supervisory checkpoint is
not before minute 10. Each checkpoint records durable file count, total bytes,
delta from the preceding observation, stage/posture, observed paths/state, and
native-context telemetry availability. Mere quietness is not failure. A child
may be interrupted only after one full declared stage interval with zero new
durable output, with the exact on-disk state recorded in the interruption
event. Stage-completion messages trigger an immediate evidence observation and
progress notice but never shorten the next no-growth interval.
