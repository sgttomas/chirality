# I101 B3 readers, addendum 01: G8's sourced-case alignment (ROOT's ruling on I100's B3 addendum 01)

TASK (Type 2), I101, for ROOT. 2026-10-08 UTC. The basis is ROOT's message adding this item, and I100's `R/I100/b3_readers_01/ADDENDUM_01.md`, whose `SHA256SUMS.addendum_01` I verified (85 files).

## The rule and the change

Both routes, in RS and TS. A sourced case passes only when all three hold:
- `pressure_regions` is absent, null or `[]`, type-strict. On the exact route only `[]` passes, as before.
- `equivalent_static` is null or absent.
- No `analysis_state` key is present.

A case-level `pressure` is not read.

| Lane | Commit | Change |
|---|---|---|
| RS `b2-r` | **`c845e899da`** | I100's `RS_b2-r_b2b58699bb.diff` (`cfd94449…`), applied unchanged: the preview route's `pressure_regions` becomes type-strict. RS already held the `analysis_state` and `pressure` clauses. I reworded the comment for both routes. |
| TS `b2-t` | **`5ddb2a3eac`** (head `77aaaa61d1`, with the merge of `b2-r`) | I100's `TS_b2-t_36823f5b2d.diff` (`d4926986…`), applied unchanged: it drops `c.pressure == null`, adds `!Object.hasOwn(c, 'analysis_state')`, and makes the preview route's `pressure_regions` type-strict. |

**One new test per language** (`b3_add1_g8_sourced_case_on_the_preview_and_exact_routes`; TS: "ROOT's ruling on I100's B3 addendum 01 …") covers 54 shapes:
- I100's 22 values on PP's milestone successors in both modes, resealed with DEF-O's H;
- x08 (`analysis_state`) and p02 (a case-level `pressure`) on the three synthetic and both m3x exact successors, with DEF-E's H.

Bound readings are G8 `PREPARATION_MISMATCH` or eligible. Unbound and transport readings are never refused and never eligible.

## Reproduction on I100's 52 shapes

I read I100's input lines (`add1_inputs.jsonl`, `b719957a…`) with RS and TS through scratch harnesses that are never committed. I compared them with PY's verdicts at `b7721d27e9` (`py_add1_shapes.jsonl`) and with I100's `SHAPES.tsv` expectation.

| Heads | Preview shapes differing (of 44) | Exact shapes differing (of 8) | RS or TS unlike the expectation |
|---|---|---|---|
| Before (`b2b58699bb`, `36823f5b2d`) | 26 | 8 | many (`ADD1_CMP_today.json`) |
| **After (`c845e899da`, `77aaaa61d1`)** | **0** | **0** | **none** |

- **Readings:** the comparison covers bound, unbound and transport.
- **Exact bases:** the bases themselves (I100's 12-row tables also include them) read eligible in all three readers.

## Mutants (one per clause; a control in each language passes)

| Clause | RS | TS |
|---|---|---|
| C1 `analysis_state` admitted | killed | killed |
| C2 preview `pressure_regions` read as falsy (the old reading) | killed | killed |
| C3 preview: any list admitted | killed | killed |
| C4 a case-level `pressure` refused | killed | killed |

Each mutant is killed by its language's new test.

## Census and suites

- **07m:** 0 changes in RS and TS at the final heads, over 339 entries, against I100's I4′ census.
- **07n** (SC's corpus `ea113e7b…e283` in archive copies of the final heads): 0 changes in RS and TS over 638 entries, against I100's census at SC's head, comparing gate, code, detail, eligibility, standing, publication digest, classifications and input digest.
- **Suites:** see `RETURN.md`. This addendum adds 1 RE test and 1 vitest; nothing else changed.

## Stop

None.

## Records

`_run_records/addendum_01/` holds `harness/`, `mutants/`, `readers/`, `census/` and `logs/`.

`logs/rs_b28_trace.log.gz` is B3's B28 trace. It ran in a scratch copy with B28 applied and `need()` printing the refusing line, a probe that was never committed.
