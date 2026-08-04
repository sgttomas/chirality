# Validation — D-APP-90 First-Domain Resume

Overall: `PASS — VALIDATED MANAGER HANDOFF`

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
| Corpus manifest | PASS — 185 data lines; file SHA-256 `66b6f3…79be` |
| Critical App paths | PASS — all 13 path/hash pairs reproduce |
| Source baseline | PASS — D-APP-89 fingerprint unchanged; zero target-selector matches |
| TL/TA | PASS — TL target 0 all; A TA explicitly unmeasured, B 0, C 1 generated binding |
| DC | PASS — intended 0 all; B risk census 11 retained |
| BM / DeltaBM | PASS — 8 target cells / increase 4 |
| MCI | PASS — A 24, B 43, C 28, each with U=6 |
| Coexistence | PASS — isolated state survives; shared Root runtime remains conditional/blocked |
| Elimination | PASS — A/B/C survive; none selected |

## Fresh adversarial verification

Attempts 01–03 are preserved as BLOCK and receive no acceptance credit. Their
evidence-delivery/coverage findings were repaired only in this run. Final R4
verdict is `ACCEPT_WITH_NONBLOCKING_NOTES`, return SHA-256
`59a8cb078742806f7ebf476e15721d52b272c6eb8d2a9bf81a4fba5ecb76534f`.
The R4 Agent 2 used no Bash, shell, filesystem, network, native Pi, write, or
delegation.

Nonblocking notes are carried exactly: A TA remains unmeasured; source-category
counts overlap and are not a partition; final containment is reconciled below.

## Preservation and containment

- The six D-APP-81 rows remain literal `HISTORICAL_RELATION_UNKNOWN` at
  unchanged CSV SHA-256
  `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`.
- D-APP-88 stays advisory; D-APP-89 stays baseline; two-target/domain-first
  stays fixed; generic runtime/sandbox/identity/version/resume/Bash stays
  `BLOCKED_BY_ROOT`.
- Tracked and cached diff-name inventories are empty. Every untracked write is
  inside the exact fresh AgentRuns root. `git diff --check` and trailing-
  whitespace checks pass.
- No A/B/C selection packet, decision/register row, product/source, PRD,
  decomposition, SCOPE_CHANGE, deliverable/status, Task Management,
  receipt/corpus, Root/Piping/PEC, completion-log, Git, release, lifecycle, or
  publication write exists in the run write set.
- Frontend typecheck, tests, build, render, package, and premerge gates were
  skipped because no runtime/product source byte changed. This is a static
  derivative planning proof.

The final artifact inventory contains only the files enumerated by this fresh
root. No Git operation was performed.
