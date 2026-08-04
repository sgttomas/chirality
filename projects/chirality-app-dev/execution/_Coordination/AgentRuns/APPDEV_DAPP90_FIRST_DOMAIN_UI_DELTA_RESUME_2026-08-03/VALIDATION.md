# Validation — D-APP-90 First-Domain Resume

Overall: `PASS — REPAIRED DERIVATIVE HANDOFF; POST-COMMIT RANGE CHECK PENDING`

## Committed input and authority

| Check | Result |
|---|---|
| `HEAD` / `origin/main` | PASS — both `88e7590d3664d4f1daf91bed2a8899bda0748b92` |
| D-APP-90 ruling / proposal | PASS — SHA-256 `cde0ff…36b1` / `eda530…3c57`; exact rider preserved |
| Response committed identity | PASS — mode `100644`, blob `a71145…fbd3`, SHA-256 `e38c56…35e7` |
| Fitness tests 1–5 | PASS — exact crosswalk in `PIPING_INPUT_CHECK.md` and sealed dossiers |
| E-01..E-29 survey hashes | PASS — all reproduced against `97678a841ef58345c73d3470ed8de57c9b1405d2` |
| Tests 4–5 emphasis | PASS — exact UI/CLI/draft API/absent-runtime evidence and Piping-local/candidate-generic separation |

## Delta, source rebind, and comparison

| Check | Result |
|---|---|
| Exact U | PASS — six distinct planning nodes U-01..U-06 with exact E-ref provenance |
| App corpus | PASS — 185 entries; data-line digest `ad2628…92aa4` |
| Corpus manifest | PASS — 185 data lines; repaired file SHA-256 `864d04…956` |
| Critical App paths | PASS — all 13 path/hash pairs reproduce |
| Source baseline | PASS — D-APP-89 fingerprint unchanged; zero target-selector matches |
| TL/TA | PASS — TL target 0 all; A TA explicitly unmeasured, B 0, C 1 generated binding |
| DC | PASS — intended 0 all; B risk census 11 retained |
| BM / DeltaBM | PASS — 8 target cells / increase 4 |
| MCI | PASS — A 24, B 43, C 28, each with U=6 |
| Coexistence | PASS — isolated state survives; shared Root runtime remains conditional/blocked |
| Elimination | PASS — A/B/C survive; none selected |

## Fresh adversarial verification

Attempts 01–03 are preserved as BLOCK and receive no acceptance credit. R4 is
preserved at SHA-256
`59a8cb078742806f7ebf476e15721d52b272c6eb8d2a9bf81a4fba5ecb76534f`
as the accepted pre-repair semantic review, but it receives no credit for the
repaired manifest bytes.

The genuinely fresh R5 Agent 2 independently verified the final repaired
manifest, old/new identity chain, 185 data lines, unchanged data-line digest,
185/185 selected hashes, historical-R4 preservation, and no-ruling boundary.
Its verdict is `ACCEPT`, return SHA-256
`192720231b83340a72b882e789bb91b953199ab44f86fe8ec4ee4c7e0a8c2419`.
It used read-only filesystem, SHA-256, byte-count, and Git inspection; no
writes, Git mutation, network, native Pi, delegation, selection, or ruling
occurred.

## Preservation and containment

- The six D-APP-81 rows remain literal `HISTORICAL_RELATION_UNKNOWN` at
  unchanged CSV SHA-256
  `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`.
- D-APP-88 stays advisory; D-APP-89 stays baseline; two-target/domain-first
  stays fixed; generic runtime/sandbox/identity/version/resume/Bash stays
  `BLOCKED_BY_ROOT`.
- The repaired manifest removes exactly one terminal LF. `git diff --check`
  passes for the working repair diff, and the historical R4 files remain
  absent from it.
- The D-APP-91 proposal and its single `AWAITING_RULING` register row now exist
  as an owner packet. This repair changes only their evidence hashes; it does
  not change packet status, recommendation semantics, return tokens, or the
  no-effect boundary, and it records no selection or ruling.
- No product/source, PRD, decomposition, SCOPE_CHANGE, deliverable/status,
  Task Management, receipt/corpus, Root/Piping/PEC, completion-log, Git,
  release, lifecycle, or publication write exists in the repair write set.
- Frontend typecheck, tests, build, render, package, and premerge gates were
  skipped because no runtime/product source byte changed. This is a static
  derivative planning proof.

The exact validator command
`python3 tools/validation/validate_candidate_whitespace.py --base-ref
88e7590d3664d4f1daf91bed2a8899bda0748b92` was run before Git mutation. Its
staged/unstaged portions find no repair defect, but its committed-range check
still sees the pre-repair blank line in current `HEAD`; therefore CHANGE must
rerun it after the repair commit advances `HEAD`. This sequencing result is
not represented as a PASS. No Git operation was performed by this repair run.
