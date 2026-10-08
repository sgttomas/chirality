# I104 B1-SQ: Addendum 1 to RETURN.md (G6, the witnesses, the challenge, RSS_TIME; for R6b and R9)

TASK (Type 2), I104, for ROOT. 2026-10-08 UTC. No delegation. RETURN.md and its SHA256SUMS stay as sealed; this addendum's files are in `SHA256SUMS.addendum_01`.

ROOT's R6a: M = 10.5 GiB, provisional; the per-call observation rule is not applied. This addendum covers G6, the witnesses, the challenge, RSS_TIME, DEF-O's shares and QUAL §11's carry. **QUAL_B1.md** is the qualification record; **RSS_TIME.md** the measurements.

### Head

`WT/b1-q`, `codex/piping-t3-b1-q-20261008`: **`69002bc862`**, one commit over `b075c5c59f` (`_run_records/g6/g6_commit.diff`). Clean.
- Inside the brief's writes: the generated block (N-5), G-B's bound (SF-1), the law-test and challenge re-pins, the witnesses, the shared test inputs, and the guard item (E-12).
- `threshold_bytes` is unchanged: `registration.diff` is for ROOT after R6b. Until it is applied, 8 `retained_memory::` lib tests that need the registered M fail by design (`g6/law/g6_law_tests.unregistered.log`).

### G6

| Item | Result |
|---|---|
| N-5 (and B1's two other adapter reservations) priced | T11 gains SP's parked slots (2 × 1,336 B in this build) and per-case counters (96 B); T13 the batch source vector (744 B). **E_mov,max + R: 9,800,676,166 B sparse, 9,859,807,510 B dense** (+3,512 B; **0.8693 / 0.8745 M**). c = 1 unchanged |
| The 0.9 M rule, both modes | holds: 346,184,070 / 287,052,726 B under ⌊0.9 M⌋; text-error budget 8.05 % / 6.67 % |
| `admission_bound` at M − R − 1, M − R, M − R + 1; the pure `maximum` test | pass at the new M |
| G-B's bound (SF-1) | **T11 − F_T11_LATE_CAPTURE / C = 405,120 B** (the defective bound was 329,088); the late form is exactly C × one case's, at the chain and in-build |
| N-1, N-2 | the runner's literal read from source and held to C + 1; the C = 3 parked-slot test kills RV112's G04 (0 ≠ 101) |
| Re-pins (§3.3, A1-N-3, I89) | done (QUAL_B1.md §9) |
| E-12 | `retained_product.rs` added to s11f's rule 8: two integer accumulations listed; s11f 11/11 |
| Registration in a scratch copy | **PP: 741 passed, 1 failed (Mac t13), 79 ignored**; the law tests 47/47 |
| Release record | byte-identical to the dev/test record |
| QUAL §11 | carried: 408 of 412 non-candidates are RV87's; the 4 new read by type, no identifier alias |

### The witnesses (R/16 = 4 MiB; one process per entry point and mode; dev/test registered and release)

**All 40 entry points (28 witnesses, the 2 pins, 10 DEF-O reports) pass in both builds, with every outcome asserted; no overflow, abort or panic.** Unchanged: W1, W2, W2-deep, W3, W4, W7 and headroom. Since B1:
- W6 on case C → Native;
- W2b → NoTriggeredCase;
- **W2b's replacement `b2_k1e3` → Candidate;**
- **W-C2 → Successor at 4 MiB and 1 MiB**; W-C2's (A, C) → Successor;
- **c1 → Successor;**
- **the three-case input** (inside D1 by `assess`) → **Successor** in both modes.

The deepest call chain on B1's graph is **40**, unchanged.

### The challenge and RSS_TIME (dev/test registered and release; `t3_exclusive.sh`, 3 repetitions, one mode per process)

**Every challenge peak is within its bound** (A1-S-1: E_mov,max for a run with W1 work, else the W1 phase; `CAP_BYTES` 16 GiB). The largest:

| Run (dense) | Requested-heap peak | Bound (E_mov,max) | Max RSS | Wall time |
|---|---|---|---|---|
| The three-case input, Direct, a successor (6.65 MB), dev/test | 113.3 MiB | 9,339.0 MiB (1.21 %) | 161.0 MiB | 51.7 s (debug, counting allocator) |
| The same, release witness (W5 reached) | — | — | **206.5 MiB** (footprint 134.4 MiB) | **1.76 s** (W1 1.72 s) |
| c1, Direct, a successor, dev/test | 40.0 MiB | 0.43 % | 73.2 MiB | 17.2 s |
| `b2_k1e3`, Direct, an N1 notice (Candidate, W2), dev/test | 12.6 MiB | 0.14 % | 38.0 MiB | 20.5 s |
| The milestone, Direct, a successor, dev/test | 3,556,346 B (U4's registered run: 3,541,898 B sparse, 2,252,863 B dense) | 0.04 % | 20.5 MiB | 0.65 s |

**Against 16 and 32 GB:**
- the largest measured RSS, 206.5 MiB, is 1.3 % of 16 GiB and 0.6 % of 32 GiB;
- the priced worst case, E_mov,max + R = 9.18 GiB, is 57 % and 29 %;
- release wall time is at most 1.77 s per invocation at the caps.

**W3–W5 are measured at the caps** (c1, and the three-case input at C = 3 with |A| = 3). Behaviour under memory pressure on a 16 GB machine is not observed (RSS_TIME.md §5).

### DEF-O's shares (item 9; report only)

The cap-maximal inputs produce **two SharperExact fallbacks** (`b2_k1e3`, one per mode). In each, the first failing row, and so the reported cause, is a mm→SI row (`displacement_magnitude`). **But 79 rows outside both of NC-1's classes also fail, so neither DEF-O property is the sole cause of either fallback** (0 of 2). Failing rows: mm→SI 4 of 162 (2.5 %); support magnitudes 0. The publishing inputs (c1 and the three-case input) fail no row. Details: RSS_TIME.md §6.

### For ROOT

1. **R6b:** RV-Q reviews G6 (QUAL_B1.md, `g6_commit.diff`, `registration.diff`). Then ROOT applies `registration.diff` to b1-q (one hunk). With it applied, the head's 8 unregistered failures pass.
2. **R9:** RSS_TIME.md, against 16 and 32 GB.
3. **DEF-O:** on these inputs, a DEF-O revision alone would not recover `b2_k1e3`'s availability (NC-1 is ROOT's).
4. **Item 10** (the optional Direct fault variant) is not taken.
5. **`noncand_compare.py` at C > 1:** its key includes the multiplicity, so at C = 3 it flags every per-case row. `g6/tools/noncand_compare_nomult.py` is the comparison used here. Pass B's gate script should take it, or C = 1's sweep, before the next re-registration.
6. **Targets** are `WT/targets/i104-sq-*`, as at G5.

### Execution

- **Cargo**, through `t3_cargo.sh`, in fresh targets: `i104-sq-g6` (the b1-q head), `i104-sq-reg` (the registered copy's suite), `i104-sq-rel` (release), `i104-sq-mut` (G04).
- **Python and the witnesses** through `t3_slot.sh`, one process per entry point.
- **The RSS and time measurements** through `t3_exclusive.sh`, four batches (159 runs, all exit 0).
- **One heavy job of mine at a time,** each with one waiter. My waits have ended, and no other job was touched.
- **Git:** one commit (`69002bc862`); reads with `GIT_OPTIONAL_LOCKS=0`.
- **Records:** placeholder paths only (`g6/tools/sanitize_copy.py`); the large witness outputs are gzipped (`gzip -n`); no symlink and no `build` folder. The host screen (`WT/tools/t3_host_screen.py`'s patterns, host names included) finds 0 hits over this record's 582 files and over the commit's diff.
