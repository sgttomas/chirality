# K6c deduplication, record delta and verification plan

This is a run-specific proposal. Checkpoint 0 authorizes no source edit.
Aliases and source basis are in ALLOCATIONS.md. FK/K4R remain excluded.

## Deduplication choice

Prefer a single callable kernel phase model in the already-public
`H/src/k6/w1/counts.rs`, used by both H and VR. Proposed API (names are
reviewable, not installed):

```
KernelCounts { member/node/dof/row/pattern/skyline/block/body counts,
               spring/directional/support multiplicities,
               load/prescribed/source/capacity parameters }
KernelLayouts { pinned private-layout facts; exported size_of facts }
KernelEnvelope { named persistent terms; named phase transients }
estimate_kernel(&KernelCounts, &KernelLayouts) -> Result<KernelEnvelope, Refusal>
with_binary_envelope(KernelEnvelope, BinaryEnvelope) -> Estimate
```

An H `estimate(W1Counts,W1SizeFacts)` compatibility wrapper can preserve
existing consumers while the count inputs are extended deliberately. VR
maps Counts/Sizes/model capacities to KernelCounts and retains its own
BinaryEnvelope. Do not produce `H estimate - H model + VR model` by guessing
which bytes belong to the model once the terms change; expose that separation
in the API. H and VR must bind equal kernel inputs to equal kernel phases.
Different fixed-memory terms are expected and tested.

The explicit VR dependency would be:

```
open_pipe_stress_solver_performance_harness = { path = "../../../core/solver/performance_harness" }
```

Static manifest traversal finds H depends on FK, nonlinear_integration,
diagnostics and sparse_direct, with local transitive crates curved_bend,
linear_supports, primitive_loads and nonlinear_supports. None depends on VR;
adding VR→H is acyclic. H registers its allocator only in its observation/test
binary; importing H's library does not install a global allocator. This is
source/manifest inspection, not `cargo metadata` or a compiled feature check.

VR gains H plus six additional local crates beyond its existing FK/sparse
graph. No new remote dependency is apparent in those manifest paths. The
compile/link cost is greater than a tiny shared estimate module, especially
on the M3, but still avoids a new product consumer. Measure compile costs
later; do not claim zero cost from library dead-code elimination. Preserve
VR's default-disabled seeded-fault controls and feature_guard tests.

Alternative: a dependency-light shared module/crate reduces the graph but
needs additional files/manifests/module wiring outside I21's fence and exact
source ownership. `include!` from H creates one textual definition but couples
relative paths and module imports; it cannot silently keep a second copy of
constants. A generated table would need a generator and regenerated artifacts,
would be incomplete for unlisted topology/count combinations, and would still
need independent binary semantics. It is inferior for the open input domain.

## Required write-set decisions before A

| Path or surface | Old I21 fence | Reason / proposed disposition |
|---|---|---|
| H `src/k6/w1/counts.rs` | Included | Common formula, named phases, overflow handling, layout/count adapter types and existing H wrapper |
| H `src/bin/k6_observe/w1.rs` | Included | Correct stale work comment: KF3 closes stage work on stopped and completed builds; preserve semantics |
| H `tests/k6b_*.rs`, H `runner/**` | Included | New accounting/adapter/boundary/record tests; runner consumes emitted common estimate |
| H `observations/k6b/**` | Included with historical discipline | Only maintained estimate fields/counts/manifest regeneration; preserve old run packet/measurement claims unless new additive candidate data is explicitly chosen |
| VR `src/scale.rs`, `examples/vk_scale.rs`, `Cargo.toml` | Included | Delete numerical copy, add path dependency, adapt dimensions/fixed terms and output |
| VR `tests/scale.rs` and any existing test/record with changed estimate fields | Conditional included | 193 storage-count cases stay covered; add H/VR cross-adapter tests and exact estimate-field masks |
| **VR Cargo.lock** | **Not explicitly included** | Path dependency requires lock entries for H and newly reachable local crates. ROOT must seal this path; regenerate under pinned offline/locked setup, do not hand-edit lock to make builds pass |
| H `src/bin/k6_observe/main.rs` | **Not included** | Needed if additional model/capacity inputs, formula/layout identity or binary-envelope fields must be emitted/read. Current binary estimate/backstop use must be reviewed. Request exact addition if chosen |
| H `src/bin/k6_observe/alloc.rs` | **Not included** | Only if adding a requested-live/capacity witness not possible through existing public accessors. Prefer existing current/stage counters; add path only for a concrete required helper |
| New H module/lib/Cargo features or standalone shared crate | **Not included** | Avoid for preferred design; exact expansion needed for a separately selected thin module/crate |
| H Cargo.lock | No new H dependency expected | Existing H lock need not change for VR→H; any actual change still requires a precise scope decision |
| FK exported size facts / private test edits | **Excluded** | No FK edit by I21. Prefer a separately sealed disposable archive layout probe; otherwise ROOT must select another owner/scope. A mirror struct does not witness actual private type layout |

The simple dependency mechanism fits the intended harness/validation purpose,
but cannot be completed byte-for-byte inside the old explicit set without at
least the VR lockfile decision. Broader capacity instrumentation may also
need H main and/or maintained test paths. Do not edit these now.

## Record/contract delta map

- H `observations/k6b/counts.jsonl`: 33 lines, all 24 RF-LARGE combinations
  (three families × two orientations × four sizes) and nine DEC053 lines.
  Candidate changes are `estimate_adm_bytes_w1a`, `estimate_w1_sel128_bytes`,
  and any changed `estimate_w1_{fixed,decide,shared_<p>,state_<p>,solve_<p>,verify_<P>,pass_<P>}`
  fields. New version/phase fields, if selected, require schema review. Exact
  per-line candidate numbers belong to the final formula, not N0.
- Preserve every non-estimate field: model bytes/digests, member/node/free/
  structural/storage counts, source status/encoding/digest, K6 four-mode
  estimates, outcome, row content/classes, work, timing and heap observations.
  A fresh counts-only run naturally has new time/heap fields; preserve that raw
  run in K6C and apply only the reviewed estimate-field delta to the maintained
  snapshot, as RV22's earlier binding required. Do not pretend old phase
  timing is a fresh candidate measurement.
- H `tests/k6b_w1.rs:699-712` recomputes every committed line from code
  (RV22-3). Keep it and extend it to all emitted phase/version fields, not
  merely E_max. Regenerated SHA256SUMS must bind exactly the intended files.
- H `observations/k6b/k6b_packet.json` retains pre-KF3 b3 measurements and
  historical admission estimates. Do not silently rewrite history to make
  them candidate-bound. Add final runs/replays under K6C and link them by hash.
- Source search found **no maintained VR observation file with the scale
  fields** `estimate_max_bytes`, `estimate_sel128_bytes`, `estimate_fixed_bytes`
  or `estimate_model_bytes`. They appear in `examples/vk_scale.rs` and the
  runner; committed scale counts/decisions are under old T3 V-K/KF3 records.
  Those immutable files get no rewrite. VR kernel_lane `estimate` entries are
  numerical **stage work**, not scale-estimate bytes, and remain unchanged.
- VR `tests/scale.rs` checks 193 factored CI cases against stored StorageCounts
  and estimate ordering. Existing lane/engine byte-for-byte records should
  remain byte-identical for a K6c-only change. Add a structural diff check
  that classifies `estimate` stage work as protected, even though its name
  contains the word estimate.
- A1-selected outcome/row/work changes, if any, use the independent A1 impact
  ledger and candidate basis. They are never disguised as estimate-field
  edits. ROOT assigns one VR writer and serializes integration.

## Test design and exact mutant evidence

Retain H `--all-targets`, the isolated `k6_alloc` binary, H Python runner
suite, all existing VR tests (47 historical minimum, including feature guards)
and its seeded-fault and harness kill matrices. Do not drop inventory,
tolerances, or NONE controls. Execute only later under the qualified runtime,
one global heavy slot, cargo `-j 1`, one test thread, offline/locked settings.

| Check / mutant | Discriminator and expected failure |
|---|---|
| Independent named phase accounting | Derive expected phase vectors from allocation events/inputs, independently from production constants. Assert every component and lifetimes, then E=max; not just duplicate the production formula |
| Drop at/bt/ct individually and combined | Tiny synthetic f>0 with fixed q/s/b, assert shift nl transient exactly includes 3fw. Each term-revert patch fails that phase assertion; run recorded-heap comparison as a separate check |
| Count factor work during nl_pass | Assert phase sets are disjoint: factor has work, nl has at/bt/ct and no work. Reverted model adds fw, so **exact phase equality** fails even though total admission remains safe. A heap≤estimate assertion alone cannot kill this overcount mutant |
| OPTION_EXTRA back to8 | Actual private-type pinned witness plus row/shift coefficient assertions. At L4/8/16, compare Option and Wide. A local lookalike type is not an actual FK witness |
| Drop Uc c/at/bt/ct overlap | Test verify-build helper vector sets with nonzero f and small m so Uc phase dominates. K6C arithmetic can construct counts; runtime cases must validate actual reachability separately |
| Drop refusal slots / certificate storage | Multi-block, mixed data and no-data fixtures; successful and refused bounds; measured prefix/phase observations with exact source and block counts |
| VR restores stale numerical port | Cross-consumer same KernelCounts yields identical kernel phase vector/version; use a case where old port differs. Keep independently different binary fixed adapters; runner and binary boundary tests also fail |
| Counts binding | All 33 final H lines recomputed from the compiled candidate; drift any final estimate field and require RV22-3 failure |
| Binary backstop and runner | Synthetic heap caps at 2E-1,2E,2E+1, zero/missing/overflow estimates; candidate counts from binary; runner consumes exactly those bytes. Conditional permission/ascent refusal stays separate. No run uses bypass to reach a large solve |
| Record masking / A1 separation | Compare parsed records after removing only named resource estimate fields; all other fields and model/source digests identical for K6c-only changes. Do not strip generic keys named `estimate` |
| Recorded-heap check | Every preserved W1/KF3 B heap metric with its own binary fixed term, and every new final W1-T4 row. A candidate mismatch stops; historical missing fields remain missing |
| NONE controls | Run identical commands/source baseline for each mutant family, assert passing control and exact failure site for mutant. Keep patch/hash/command/stdout/stderr/exit and candidate identities |

Save every actual mutant patch under final K6C `_run_records/**/mutants/<id>.diff`;
describe no hypothetical patch as executed. Neither these assertions nor a
source lint is runtime memory evidence. Tiny isolated allocation witnesses and
real guarded solve/prefix observations remain separately required.

### into_solve_128 stop

This is a scenario label, not an exported function found in current H/FK.
It is feasible through H's public W1 staged API without FK edits: first run a
tiny accepted case to obtain the 128 shared work and RHS stage work; rerun
with the case budget ending after RHS but before positive solve work. The
guard immediately after factor.solve (`adaptive.rs:1724`) should stop the
attempt with Budget(Case) in Stage::Solve. Assert attempted128, no publication,
positive solve work, exact total closure, zero unstaged under KF3, and a false
closure after subtracting one unit from the solve stage. This is a stop at
the solve stage's existing check, **not** an interruption mid arithmetic
loop. If that finer interpretation is required, H cannot inject it through
the current API; report the limitation and preserve the FK exclusion.

### Layout/capacity witness

Wide/BlockBound/ShiftResult/report/control types are crate-private, not in
retained_api (`FK/src/structural.rs:10-36`). H cannot directly size them.
Propose a separately authorized test-only patch in a disposable archive of
the exact final FK tree, inside its existing private module, emitting actual
size_of/align_of for the three widths and all option/block/control types.
Pin the patch and toolchain; exclude it from timing binaries and product
source. It must also witness grow/filter/Result collect/sort/shrink, adjacency
dedup capacity and BTree/VecDeque allocation events on the pinned stdlib.
This checkpoint supplies no compile probe and grants no archive mutation.
