# I65 U4 G6: return

**Status.** G6 is complete. The qualification record is `QUALIFICATION.md`, the identifier audit is `ID_CLASS_AUDIT.md`, and the registration change is prepared in `registration.diff` but **not applied**.
- **Code:** WT/f2a-memory, on top of `cba3e9fda7`, uncommitted: +294 / −185 in 5 files, all inside the G6 fence (`_run_records/candidate_g6.diff`).
- **The registry is still empty** in the worktree.

## The numbers

| | Sparse | Dense |
|---|---|---|
| E_req,max (W3, Direct) | 3,318,504,979 | 3,338,215,427 |
| E_mov,max (W3) | 3,507,808,260 | 3,527,518,708 |
| E_mov,max + R | **0.8878 M** | **0.8927 M** |
| Below 0.9 M | 48,961,532 B | 29,251,084 B |
| Text-error budget (margin / TAV_W) | 3.12 % | **1.86 %** |

- **After both the 42 closures and the identifier audit, the maximum is still ≤ 0.9 M.** So no stop, and the phase-aware span stays in reserve.
- The release build's record is byte-identical to the dev/test build's.
- **Headless** is refused at D1.0, so it has no admitted maximum.

## Each item, separately

1. **The 42 Estimates are closed.** ESTIMATES = 0: 190 InBuild atoms, 16 SourceUpper, 6 Text. Each is bound to the actual owner its roster line denotes; the table is in QUALIFICATION.md §2. Closing them adds +9.77 MB to the maximum. The large ones are `TrackerE` (4,472 B, against G3's 64; P3's Tracker(O) law), `LazyE` (4,304), `LaneTerminal` (4,168), `RegistryE` (1,608) and `PreparedMemberEvent` (1,304). The C2 maps, conversions and lane terminals are bound conservatively, as double counts.
2. **The identifier-class audit (ROOT's addition):**
   - 747 copy entries over 599 sites, each priced by source: input 128, result id 1,024, diagnostic id 2,330, own template, composite 600, or static. 72 entries are raised and none is lowered.
   - **The run enforces it:** an identifier hit outside the table makes TEXT incomplete, and a removed-entry control proves it.
   - RV87's 18 sites are priced exactly at RV87's bounds (+32,373,120 B). Beyond them, the audit raised:
     - rows.rs:370 (a ResultItem id);
     - `projection_id`/`functional_id` (≤ 188/199);
     - lib.rs:1763's entries (≤ 8,241);
     - 3 `diagnostic_ref` copies to 2,330, plus RV87 N-1's 5;
     - the force-scaling quantity (145) and the pressure refs join (148);
     - 40 error-`Display` fields to the static class.
   - **TEXT** becomes 2,149,902,046 B (+33.3 MB: W +4.3 MB, X +33.3 MB), and is complete.
3. **The build identity:** register **one**, the dev/test build on this host:
   - aarch64-apple-darwin, rustc 1.97.1 (`8bab26f4f68e`);
   - `profile=debug`, `opt_level=0`, `debug_assertions=true`, `panic=unwind`, no RUSTFLAGS.
   
   That is the build that `cargo test` uses for U3 grant 2's milestone E2E, U7's facade publications and U9's gates on this host. **The release identity is qualified** (identical record; all nine witnesses pass) but not proposed, because nothing named is known to run a release PP build here. Hosted Linux CI is `Stale`, so it is fail-closed.
4. **The pinned record is identity-gated** (ROOT's ruling): it asserts only in `PINNED_RECORD_IDENTITY`'s build and prints a skip elsewhere, as seen in the release build.
5. **The qualification record** has every brief §4 item:
   - E_req and E_mov per caller and mode;
   - R and the S1 evidence (measured, not a proof), with the 40-frame chain (RV83 N-3), carry 8's limit and the panic-hook residual;
   - the identity and reviewed-input texts and the reader layouts;
   - the D1 predicate;
   - the D-7 non-claims (statics counted in every phase);
   - the cfg(test) argument: the production build's evaluation equals the record.
   
   **Proposed M = 4,026,531,840 B.**
6. **The registration change** (`registration.diff`, 4 files):
   - **the entry**, with `threshold_bytes` M;
   - **`admit_grants_a_permit_for_the_milestone_in_the_registered_build`**: both modes; Headless refused; a two-case variant refused;
   - **`the_registered_profile_is_the_only_permit_source`**;
   - **seven "no permit" tests restated** for a registered build. Two of them are in files outside U4's fence (`retained_facade_tests.rs`, `tests/retained_precision_admission.rs`), as proposals for ROOT to apply.
   
   **Applied in a scratch copy:**
   - **PP:** 696 passed, 1 failed (t13).
   - **Sweep:** every report goes `Missing → Registered`. The milestone publishes a successor in both modes, peaking at 3.5 / 2.3 MB. The two `rejected_stress_range` fixtures gain U3's N1 notice, because they are admitted and their W1 falls back.
7. **RV89 on part 2:**
   - **S-1:** the five result-id copies are RES by source type.
   - **S-2:** `witness_w2_deep_milestone_publishes` is committed. It publishes at 4 MiB and 1 MiB in both modes and both builds. W2 and W2b now assert `Fallback(Preparation)` and `Fallback(Candidate)`.
   - **S-3:** `maximum_takes_every_phase`; Q10 is in the mutant set and is killed.
   - The margin standard is stated above.
8. **RV83 N-3:** 40 frames, carried. N-1 and N-2 are optional and not taken.

## Controls

**Unregistered, against base `8abb5274a9`:**
- **Sweep:** byte-identical (`0690bc64…`).
- **PP:** 695 passed, 1 failed (t13), 11 ignored. Only the U4 tests differ from base.
- **runner/headless, FK and SR:** identical to base.

**Mutants:** **162 run, 158 killed by a test, 0 compile-only** (`controls/mutants_g6.out.jsonl`). The sets are part 1's 84, RV89's 24, part 2's 40 and G6's 14. G6's 14 are nine FK exports, four profile bindings and RV89's Q10, which `maximum_takes_every_phase` kills. **The 4 survivors are all recorded:** – "build_status ignores bindings" is equivalent by decision 7, since nothing is registered in the worktree; – RV89's V19 (build.rs) cannot be observed in-crate; – "Estimate count ignored" and "estimates not counted" are equivalent now that ESTIMATES = 0. `priced_maximum(1, ·)` is still tested as `Unpriced`

## Decisions for ROOT

1. **Register the dev/test identity only?** Or also the qualified release identity: one more entry, and its record and witnesses are ready.
2. **Before applying the registration, two consequences follow from D1's design** (QUALIFICATION.md §8):
   - **Admitted-but-blocked requests change bytes.** D1 admits Direct requests whose ordinary run is blocked (an invalid category or document kind; `rejected_stress_range`). Under registration, these publish U3's W1-unavailable fallback: the ordinary envelope plus one `RETAINED_PRECISION_UNAVAILABLE` info notice. They are no longer byte-identical to the value route.
   - **The permitted path's single ordinary dispatch (U3's B-1) is uncounted.** No test hook counts it; that needs a lib.rs hook. **Proposed for U3 grant 2.**
3. **Two hunks of `registration.diff` touch tests outside U4's fence:** `retained_facade_tests.rs` and `tests/retained_precision_admission.rs`. ROOT applies them with the entry, or routes them to their owner.

## Execution record

- **Who and when:** I65, TASK (Type 2) under ROOT, no descendants; 2026-10-04.
- **Memory guard:** PID 5387 was running throughout, and every cargo job checked it.
- **Cargo:** the default toolchain, `--locked --offline`, `CARGO_BUILD_JOBS=4`, `RUST_TEST_THREADS=2` (1 for the witnesses and the challenge), one cargo job at a time.
- **Writes:**
  - the five code files in WT/f2a-memory;
  - this folder;
  - WT/scratch/i65_u4_g6_01/ (the TEXT runs, the candidate, registration and mutant copies, logs);
  - WT/targets/i65-g5/ and WT/targets/i65-g6/.
- **Not run:** no Git writes (reads used `GIT_OPTIONAL_LOCKS=0`), no installs, no new tooling, and no native, solver-at-scale or DEC-025 jobs. The Python is stdlib only.
- **Records:** placeholder paths only; a check for machine paths finds none. `SHA256SUMS` covers this folder.

## Addendum: ROOT's rulings on G6 (RR, after G6's return)

**Ruling 1: register the dev/test identity only.** Done.
- `registration.diff` registers that one identity.
- QUALIFICATION.md §5 records the release identity as qualified, ready and unregistered. It becomes a one-entry change when a release run is named.

**Ruling 2(a): G-C declines W1 when the ordinary route did not attempt the case's solve.** Done, inside U4's fence (QUALIFICATION.md §8a).
- **The fact** is `PhaseFact::OrdinarySolveNotAttempted`, the last of G-C's 19 facts, with a bound of 0. A refusal there is `W1Fallback::CompleteGate`: the ordinary bytes are exact, and no notice is rendered, because the notice exists only inside `retained_w1`.
- **The predicate** is `ordinary_solve_attempted(capture)`: the capture has at least one seed, and every seed has `initial.is_some()`. It reads the observer's own G-b record, which is set exactly at the attempt (lib.rs:4125–4148) or at an `Ok` attempt's report (:4543).
- **It cannot read `blocked_envelope`.** That function is returned both before and after an attempted solve (`solver_blocked`; post-solve `has_blocking`), so the envelope's status is ambiguous.
- **The predicate is unambiguous for every ordinary outcome inside D1, so there is no stop.** The exits before and after the attempt are cited in §8a and in the function's doc comment.
- **The examples, checked in both modes:**
  - **Declined** (exact bytes, no notice): invalid `document_kind`, invalid load category, no supports, and a lone spring (`SOLVER_SYSTEM_BLOCKED` before the attempt).
  - **Proceeds:**
    - the milestone (Sensitive), which publishes;
    - a 1e-300 spring (the attempt fails `NumericallyUnresolved`), which reaches W1;
    - W6 (the attempt fails, then W2 publishes);
    - **`rejected_stress_range`.** Its solve ran Sensitive, and only the legacy source-block finalization then blocked the envelope. By your rule it proceeds and keeps U3's N1 notice on fallback. **Note this one:** of the examples I named, it is the one whose bytes still change under registration.
- **Tests:**
  - `g_c_declines_w1_when_the_ordinary_solve_was_not_attempted`, in the worktree (both modes, both groups, and the predicate's empty and unset-seed edges);
  - `registered_g_c_declines_only_unattempted_solves`, in `registration.diff`. In the registered build, for each blocked example, Direct's bytes equal the value route's exactly, with `CompleteGate(OrdinarySolveNotAttempted)`. The milestone publishes, and the failed attempt and `rejected_stress_range` reach W1.
  - The admission integration test's invalid-document case now expects exact bytes in every build.
- **Mutants:** 5 new ones for the fact (§9). The bound raised to 1, the fact zeroed, empty seeds counted as attempted, a seed alone counted as attempted, and only a reported solve counted as attempted are all killed.

**Ruling 2(b):** B-1's single-dispatch count goes to I61's U3 grant 2, as recorded.

**Ruling 3:** the two out-of-fence test hunks stay in `registration.diff`, to be applied with the entry.

**Re-run after 2(a):**
- **Unregistered candidate:**
  - the sweep is byte-identical to base (`0690bc64…`);
  - PP: 696 passed, 1 failed (t13), 11 ignored;
  - runner/headless: identical to base;
  - law suite: 39 passed in both builds;
  - nine witnesses pass in both builds;
  - the profile and record are unchanged, at 0.8878 / 0.8927 M.
- **Registered copy:**
  - PP: 698 passed, 1 failed (t13);
  - the milestone publishes in both modes (challenge peaks 3.5 / 2.3 MB);
  - every retained report is `Registered` (140 of 140 parsable);
  - the sweep sha256 is unchanged, `3b22de97…`, since no sweep fixture is an unattempted solve;
  - the blocked examples are byte-identical (the test above).
- **`registration.diff`** is regenerated: 4 files, 287 lines.
- **Mutants:** 167 run, 163 killed by a test, 0 compile-only. The 5 new G-C mutants are all killed, and the 4 survivors are unchanged and recorded.
