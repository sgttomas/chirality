# K0 source closure available before a runtime grant

Prepared by DELIVERY at coordination `fe6ca966259d29d8d6ed2f05460400f6cb5d5de0`;
FK/H/VR still match product source `3bddc2b05f6106e969c7cf43373b230845c7cc66`.
This is source-derived analysis, not full K0 acceptance. It supplements the
sealed I21 packet without changing it. N0 remains unaccepted; final A1 impact
and a complete phase model remain open.

Aliases: K = `projects/chirality-piping/core/solver/frame_kernel/src/structural/retained`;
H = `projects/chirality-piping/core/solver/performance_harness`;
VR = `projects/chirality-piping/validation/benchmarks/numerical_robustness`;
L = exact isolated Rust 1.97.1 `lib/rustlib/src/rust/library` source. Source
hashes/ranges are bound by BASIS.json. ROOT installed rust-src during this
continuation; its source availability does not qualify a compiler run.

## Payloads and cardinalities now closed from source

N nodes, n=6N DOFs, m members, t stations, r constraints, l loads, sp scalar
springs, ds directional springs, su support groups, B bodies, q published rows.
Let I be total load source-id byte lengths and J total support spring-ID counts.
These are lengths, not capacities or whole heap bounds.

| Quantity | Exact length / safe cardinality | Source |
|---|---|---|
| Publication layout | q=7N+12m+6t+sp+3ds+r+2su | K/recover.rs:104–197; each loop's multiplicity |
| K4STF | 26+24N+84m+17sp+41ds+5r bytes | K/source.rs:686–743; five u32 lengths and six-byte header |
| K4SRC | 38+24N+84m+17sp+41ds+13r+17l+I+16t+22su+4J bytes | K/source.rs:652–743; support mask has six bytes |
| K4LED | 10+18u+8·sum(limb_count_i) bytes, u distinct loaded DOFs ≤l | K/ledger.rs:218–232 |
| General case-ledger upper | ≤10+562l bytes, since each net uses ≤68 limbs | K/ledger.rs:32–62 and FK/src/exact_sum.rs:20–51. A proved single finite load per DOF tightens to 10+26l; do not assume uniqueness from an adapter comment |
| K4RST at selected width W | 22+(n+6m)(9+8W) bytes | K/recover.rs:495–529; header, precision/width/two counts; sign+exponent+W limbs per value |
| H specific layout | sp=ds=su=0, t=m, prescribed values zero | H/src/k6/w1/adapter.rs:40–88, actual construction |
| H source-id bytes | each `k6:<global>` has 4 through 3+digits(6N−1) bytes | adapter.rs:27–29; indices must remain valid |
| Evidence row partitions | absolute_verified length a, unpublishable length u; a+u≤q; not_covered is empty in finish_selected | K/adaptive.rs:3342–3355, different RowClass alternatives |
| Body/control evidence | publication scales=4B; input-derived DOFs=r; resolution/theta/floor/bound outputs each ≤B; each decision-summary vector ≤4B, safely ≤12B total | K/adaptive.rs:2598–2657, 2339–2364, 3330–3405. Tighten estimate/charge kinds only after explicit assignment proof |

`SOURCE_CARDINALITIES.json` checks all 33 committed H count records: every q
identity agrees and every recorded K4SRC payload fits the source-id bound.
The largest W=16 retained-state payload in those records is 16,440,844 bytes.
This is arithmetic on recorded dimensions, not a generated model or a heap
measurement. The stricter source-length identities cannot substitute for
Vec/String allocation capacities.

## Pinned liballoc facts now available

The following are specific to the installed/pinned 1.97.1 source, ordinary
nonzero-sized types and Global/K6 allocation tracking. Recheck source/toolchain
identity before final use; source claims do not generalize to arbitrary allocators.

- **Exact reserve:** L/alloc/src/raw_vec/mod.rs:446–481 requests the array
  layout at the requested capacity and stores that capacity. Global returns
  exactly the requested slice length (alloc.rs:205–226). Thus with_capacity(k)
  and the successful fixed vec/TrustedLen paths can have exact requested
  payload k·sizeof(T), with no guessed allocator rounding added to K6 heap.
- **Growth:** raw_vec/mod.rs:158–164 sets minimum nonzero capacity m(T)=8 for
  one-byte elements, 4 for size 2…1024, 1 for larger types. grow_amortized
  :518–531 uses max(2c, len+additional, m(T)). A fresh push-only buffer with
  k>0 elements therefore has c=max(m(T), next_pow2(k)); k=0 has no allocation.
  This does not apply blindly to an exact pre-reserve or to an owned iterator
  reusing an older allocation. Retain the complete reserve sequence when used.
- **Iterator classification:** vec/spec_from_iter_nested.rs:18–60 distinguishes
  general lower-hint growth from TrustedLen exact upper reserve. Filter and
  filter_map report lower=0 (core/iter/adapters/{filter,filter_map}.rs:118/126).
  A slice-based filtered collection can use the push recurrence. Result and
  in-place/owned iterator specializations need their actual source route bound
  per call site; do not equate every collect with either exact n or next_pow2(n).
- **Clone:** Vec::clone delegates to slice to_vec_in (vec/mod.rs:3806–3808);
  both clone paths reserve exactly source.len (slice.rs:425,448), then clone
  elements. The new outer Vec does not inherit source.capacity. Nested Vec/
  String/Box payload clones still allocate separately and overlap the source.
- **Shrink:** Vec shrink_to_fit selects len; RawVec shrink sets requested
  capacity to len after success (:839–860). Global uses realloc for equal
  alignment (alloc.rs:304–310). K6Alloc's shrinking branch does not add an
  old+new move peak (H alloc.rs:218–229). Model K6 requested heap, OS footprint
  and conceptual allocator-internal moves separately; do not claim that the
  measured move counter covers every physical realloc transient.
- **Sorting:** stable sort uses Vec scratch (alloc/slice.rs:854–872).
  The non-size-optimized path uses max(ceil(k/2),min(k,8,000,000/sizeof(T)),48)
  entries when heap scratch is needed (core/slice/sort/stable/mod.rs:94–129;
  shared/smallsort.rs:180–188). Charging max(k,48)·sizeof(T) is a simple safe
  source upper bound across the shown normal/size-optimized branches; zero
  scratch for small cases may be established separately. Do not add sorting
  scratch simultaneously to prune's later kept-buffer phase: sort returns
  before kept is constructed.
- **VecDeque:** reserve/grow uses RawVec and then copies within the enlarged
  ring buffer (collections/vec_deque/mod.rs:671–715,1109–1120,2794–2802).
  No separate relocation Vec is shown in that path. Count its own initial/
  high-water capacity; do not reset it after popping.
- **Arc:** sync.rs:382–405 specifies repr(C,align(2)) with two Atomic<usize>
  counters, followed by T, and extends/pads the header layout. The request is
  align_up(align_up(header_size,align(T))+size(T),max(header_align,align(T))).
  K0-L1 emits the derived Layout result using actual AtomicUsize and payload
  layouts. This closes the formula form, not a guessed constant 16 for every
  alignment. Arc::clone shares payload; failed cache/refusal Vec clones do not.
- **Box/BTree:** Box requests Layout<T> (boxed.rs:606–616). BTree's actual
  LeafNode has 11 key/value slots plus parent/index/len; InternalNode adds 12
  child pointers and repr(C) wrapping (collections/btree/node.rs:43–110).
  LeafNode's private Rust layout must not be asserted from a lookalike struct.
  Proposed compile-only forced monomorphizations expose real node debug/layout
  data for the four relevant FK/VR publication map/set shapes. S2 must also
  prove node-count/transient overlap from insertion/drain code; size alone is
  not a map bound. Serde JSON nodes require the actual pinned consumer types.

## Finalization and reporting lifetimes now narrowed

`finish_selected` (K/adaptive.rs:3295–3410) runs while the caller retains report
and decision. It allocates values, then classification raw/coupled body scales
and rows, then a binary64 verification summary. The classification raw/coupled
scale scratch dies before the evidence record is constructed, but publication
rows/scales persist. During evidence construction, source identity is cloned;
ledger/state encodings are new; selected_record clones at most one AttemptRecord
including its refusal Vec. Publication body_scales and its evidence clone both
persist. Attempts, geometry and states are moved, not deep-cloned by moving into
the result. The separate cache.clone passed at the call site shares successful
Arc payloads but deep-clones cached failure/refusal Vecs; count those explicitly.

Use separate finish subphases, then take their max:

1. caller kept+decision+report + values + classification (2×B arrays, rows,
   growing body_scales);
2. kept+decision+report+values+publication + verification summary + selected
   record clone + success-evidence arrays/encodings while each grows;
3. same live inputs at Box<RetainedSolve> allocation; moved fields are one
   allocation identity, while new clones remain separate.

Every temporary reserve/growth uses the pinned recurrence above; no finalization
lump allowance is justified by spare measured memory. Refusal prefixes retain
partial allocation maxima but need not all coexist with a completed outcome.

For H, `debug_digest` streams Debug into Fnv64 (H/src/k6/mod.rs:124–129), so it
does **not** allocate a string as large as the whole publication/evidence text.
`Line` builds one output String at a time (main.rs:55–143). `bounded(format!(...))`
truncates only after formatting the complete reason; 240 printed chars do not
bound that earlier temporary. Exact possible reason fields/format paths still
need source closure. Keep short numeric formatting/Line growth distinct.

For VR, `lane::run_parts` holds outcome, encoding, published BTreeMap, controls,
per-row exact-comparison temporaries and the new JSON record together through
records::case_record (lane.rs:191–340). It returns CaseRun, dropping the kernel
outcome. In vk_scale.rs:436–485, `run.record.clone()` occurs **after** that return,
so the double-record/report phase does not simultaneously retain the kernel
caches. It still retains the published map and binary/reference inputs. Pin
serde_json macro/Map/Value allocation semantics before counting serialization
clones; absent package source or private layout remains a named dependency.

## Remaining bounded work

The next source-only brief must apply these contracts to each real allocation
sequence and original fixture domain, including pre-dedup counts, ground/
geometry buffers, string formatting, actual collect specialization, cache
failure clones, tracker drain/sort/shrink phases and VR JSON/refusal records.
A restrained model does not by itself prove geometry-witness code unreachable;
prove an exclusion on the finite fixtures or bound the relevant branch.

Private compile layout and real allocator/model observations remain distinct.
K0-L1 can emit constants and compiler allocation metadata without executing a
program. It cannot claim observed Vec growth, sampler protection, physical
footprint, a solved model, final E_max or final A1 compatibility. The guard's
compile-admission GR-01/02 repairs and independent backcheck are prerequisite
to even that later compile. This manager performed source reads/arithmetic only.
