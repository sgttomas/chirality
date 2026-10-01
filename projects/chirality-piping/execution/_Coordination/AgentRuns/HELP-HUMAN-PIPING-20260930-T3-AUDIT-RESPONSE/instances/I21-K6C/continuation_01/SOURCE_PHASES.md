# K0-S1/S2 source closure — continuation 01

This is a new source analysis on FK/H/VR `3bddc2b05f6106e969c7cf43373b230845c7cc66`,
using the actual isolated Rust 1.97.1 library and locally authenticated locked
dependency sources. It changes no earlier K0 packet. No compiler, model,
provider, guard or runtime allocation experiment was run. Private layout
variables and the precise remaining source cells are retained below.

Aliases: P=projects/chirality-piping; K=P/core/solver/frame_kernel/src/structural/retained;
H=P/core/solver/performance_harness; VR=P/validation/benchmarks/numerical_robustness;
L=<RESPONSE_RUNTIME>/rustup/toolchains/1.97.1-aarch64-apple-darwin/lib/rustlib/src/rust/library;
J=<OWNER_CARGO_HOME>/registry/src/index.crates.io-1949cf8c6b5b557f/serde_json-1.0.151.
Hashes and consultation limits are in SOURCE_INPUTS.json.

## Scope and finite inputs

The domain remains the original 33 H fixtures, named VR RF-LARGE scale
schedule, budget prefixes and repeated single calls. No combinations,
multi-case invocation bound, arbitrary model file or new kernel-wide memory
theorem is added. VR's 193 factored count-compatibility tests and full suite
remain obligations; their non-RF spring/multi-body shapes must not be adapted
as zero merely because the timed RF family has none.

SOURCE_PARAMETERS.json binds each H model to its canonical SHA256 and K4SRC
SHA256/FNV/length; every recorded q and K4SRC length is independently checked.
The arithmetic constructs only integer connectivity/zero-support metadata,
never coordinates, stiffness, a Rust model or a solver. Available canonical
files are hashed against their sealed model manifest. All 24 VR RF identities
are retained; 18 original scale count lengths agree. Twelve large VR model
files remain represented by their committed hashes, not claimed regenerated
bytes. K4STF's identity is the deterministic stiffness projection of its
sealed K4SRC through pinned source.rs; no uncomputed K4STF byte hash is invented.

H's actual Builder::load skips zero components; CHAIN calls it once per
force/moment offset at the tip, TREE once per distinct branch tip, CONT once
per distinct center. Rotation changes components, not node/offset identity.
DEC053 from_fixture enumerates the force vector once and filters zero. Thus
the 33 fixtures have exactly one nonzero load per loaded DOF. This is source
and sealed-record reasoning, not an inference from the K6Model comment.
The canonical files' parsed load indices independently confirm the available
subset. The source-id total `sum len("k6:"+global_dof)` agrees exactly on all 33.

For these H fixtures, ledger u=l and every normalized magnitude is one u64:
one binary64 term has at most 53 significant bits and from_accumulator removes
trailing zeros. K4LED length is **10+26l**, not merely the general 10+562l
upper. VR RF uses l0…l(l−1); the embedded 12 models confirm uniqueness/nonzero
and the source-id sum. Its larger generated identities use the RF generator's
map-components path; until that generator-to-large-byte binding is accepted,
keep the ≤68-limb general bound as an explicit alternative. RF-CANCEL's
authored-contribution path does not belong to this timed family.

Every fixture is connected, has no springs/directional/support groups, one
station per member, zero prescribed values and a fully fixed node0. These
facts follow the adapter and connectivity/restraint definitions; the script
checks the cardinalities and root mask. They do not license removing failed
precision, shift, budget, publication or geometry-preparation branches.

## Capacity contracts from pinned source

Write `sT=sizeof(T)`, `aT=alignof(T)`. Non-ZST heap payloads are requested
capacity×sT. Heap ownership of the containing struct is counted once. No
allocator size-class padding is added to K6 requested heap; OS footprint is
a different metric. Exact private layouts remain L1 inputs.

- **R(c,len,add,T):** if len+add≤c, no allocation; otherwise new capacity is
  max(2c,len+add,min(T)), min=8 for sT=1,4 for 2…1024,1 above 1024. A growing
  realloc's K6 move peak includes old c*sT plus new c'*sT. Use the actual
  reserve sequence, including non-power-of-two starting capacities.
- **P(k,T):** fresh push-only capacity is0 at k=0; otherwise
  max(min(T),next_pow2(k)). **E(k,T)** is exact k*sT for with_capacity(k),
  successful TrustedLen collection and borrowed slice clone. A clone copies
  len, not capacity; inner Vec/String clones remain additional allocations.
- Borrowed slice/range `.map` and applicable `.zip/.enumerate/.take` preserve
  TrustedLen. Filter/filter_map have lower 0 and no TrustedLen, so borrowed
  filtered collections use P. `Result`/`Option` collection uses GenericShunt,
  lower 0 even when its underlying map is exact length: factor.solve's borrowed
  fallible collections therefore use P, not E.
- Owned Vec IntoIter can reuse its backing allocation. A map/shunt chain's
  in-place eligibility requires equal alignments and source bytes×MERGE_BY
  ≥destination bytes×EXPAND_BY (vec/in_place_collect.rs:168–245). It returns
  floor(source_capacity*sSrc/sDest), shrinking only for a byte remainder;
  otherwise it falls back to the generic/TrustedLen path. This conditional
  is part of the formula until the required source/destination layouts are
  supplied; a second allocation is not presumed on the reuse branch.
- Important actual sites: Builder points→model nodes can reuse its owned
  allocation when the two 48-byte tuple layouts agree; H restrained_dofs→
  Constraint grows the element and cannot reuse an 8-byte source; DEC coordinates
  Option<[f64;3]>→named node uses Option-shunt and the layout eligibility test;
  VR Nat::mul maps owned u64→u32 but alignment8≠4 prevents reuse, so the u64
  accumulator and exact-length u32 destination overlap. Layout conditions are
  recorded, not guessed away.
- Stable-sort scratch is a separate phase, bounded by max(k,48)*sT from the
  pinned normal/size-optimized implementations. sort_unstable allocates no
  heap scratch. Dedup, retain, drain, pop and trim do not shrink capacities.
  shrink_to_fit after prune requests len; the K6 **shrinking** realloc branch
  does not charge an old+new move peak. It is not physical realloc evidence.
- VecDeque grows its RawVec and relocates inside that ring. Its high-water
  capacity follows R; no extra relocation Vec is created.
- Arc request is `align_up(align_up(2*sizeof(AtomicUsize),aT)+sT,
  max(alignof(AtomicUsize),aT,2))` for the pinned repr(C,align(2)) ArcInner.
  Use actual header/payload alignment cells. Arc clone shares this request.
  Box<T> requests Layout<T>, with moved child buffers counted once.

K4SRC, K4STF, K4LED and K4RST begin with an exact six-byte Vec. In this fixture
domain every subsequent scalar/string write is at most8 bytes by the time it
can exceed capacity; after the first 4-byte write capacity is12 and all later
growth doubles. Their exact retained capacity is therefore
`C6(length)=6*2^ceil(log2(length/6))`. The move peak at the last growth is
1.5*C6 for lengths above6. This differs from rounding length to a power of 2.
All33 lengths and capacities, including each retained width, are emitted.
H load-id formatting has initial literal estimate6: IDs of length ≤ 6 retain 6
bytes; longer fixture IDs retain 12. Source cloning then allocates exact ID
length. VR's parsed load-id clones use exact payload length.

## Preparation and geometry phases

The table in CAPACITY_TABLE.json names each allocation and its phase/lifetime.
These formulas use the same allocation identities. Symbolic phases may
overbound a partly built result by its complete payload, but that overcount
is explicit and never substitutes for a missing kind of allocation.

For node degree d_v, every one of its six global rows receives12d_v entries
before SparsePattern dedup, so total pre-dedup entries=144m and upper
positions/tagged count=78m. The initial sparse row capacity is
`sum_v 6P(12d_v,usize)`; it is not derived from post-dedup z. Let f_v be its
number of free components. Each free row at v has
`d_a=f_v−1+sum_(neighbor u) f_u` free neighbors. Ordering adjacency capacity
is sum_a P(d_a,usize); RCM's symmetric reinsertion capacity is
sum_a P(2d_a,usize). Both distributions and sums are computed per fixture.

Structure phases are the max of:

1. positions + sparse row headers/inner capacities + building row_starts/
   columns/transpose; while columns extend owned rows, the outer row headers
   persist and each not-yet-consumed inner capacity remains. Bound columns
   by its actual per-row R sequence (or ≤max(4,2z) capacity), not z exactly.
2. completed pattern + positions + tagged with growth old/new.
3. completed pattern + positions + tagged backing + starts + next + items.
   Consuming tagged transfers elements but keeps its buffer until iteration
   ends. starts/next each have z+1 usize; items exactly 78m Contributions.

Ordering's integer phase retains its sparse source, free/position and borrowed
adjacency, then RCM neighbors/degrees/visited/order. A safe BFS helper envelope
is `4P(f,usize)*sizeof(usize)+f` above that base: component, saved last level,
current level and next level, plus a marked bool array. This dominates the
reachable+queue branch (two frontiers plus marked). RCM's later traversal
queue is another max alternative, not another simultaneous BFS. Neighbor
stable-sort scratch is the maximum over one row's final degree. RCM helper
buffers drop before rank/first creation; integer phase formulas take a max.
Free-block construction retains old components while one stack/current
component grows; body Vec is exact b, outer positions follows P(b,Vec).

CasePrep ledger-build peak includes the growing `(usize,ExactAccumulator,bool)`
array and simultaneously formed exact-length final entries/nonzero flags/
per-entry limb allocations. The build element contains the inline 1088-byte
accumulator, so its push minimum is 1. For H each net magnitude is exactly one
u64; retain the general68 alternative where uniqueness is not established.
Source1 and source2 clone are distinct; source encodings include the group's
K4STF, CasePrep K4SRC and VR lane's additional encoding. H layout is P(q,Meta),
prescribed outer is E(r,pair), and its r inner one-term Vecs each have capacity1.
Zero prescribed **values** eliminate verification operand pushes but not those
headers or the original one-term CasePrep allocations.

### Geometry scratch is bounded without trusting SVD success

The six fixed root DOFs exclude a successful nonzero rigid witness: at root,
rotation is its candidate component, and translation is positive length times
its candidate component; exact_radix refuses loss rather than returning a
silently zero product. However, original_rigid_witness builds exact_motions
for all nodes **before** checking grounds. Therefore the scratch is reachable
when the numerical SVD does not take its early Restrained branch.

For one connected body, bound the geometry helper by its simultaneously held
body nodes, local-index map, coordinates, grounds, relative coordinates,
original SVD rows and their clone, candidates and one exact-witness build.
Candidates≤7+2(N−1)=2N+5. Each coordinate difference expansion has≤ 2 terms;
each translation expansion receives≤ 10 scalar additions (two from length×
translation and eight from four difference-term products); rotation ≤ 1.
Thus motion child buffers are at most `N*[3P(10,f64)+3P(1,f64)]*8 =480N`
bytes on the pinned primitive widths. The outer exact_motions capacity is
P(N,[Expansion;6]). During one add, old terms remain while next grows;
charge at most192 bytes for next's old8/new16 f64 buffers, plus96 bytes
for the three difference buffers. This is a source bound, not measured slack.

One sufficient named phase is:

```
G_geo = E(1,BodyGeometry) + P(N,u32)*4 + BTree_insert(N,u32,usize)
      + E(N,[f64;3]) + P(r,usize)*8
      + P(N,[f64;3])*24 + P(r,[f64;6])*48 + E(r,[f64;6])
      + P(2N+5,[f64;6])*48 + P(N,[Expansion;6])*sizeof([Expansion;6])
      + 480N + 288
```

P in products denotes capacity in elements; E denotes bytes as defined above.
The redundant products on P make units explicit. Source parameters encode
that distinction. The root exclusion stops before the returned node_motion/
exact_scalar conversion path; no successful witness-output Vec is budgeted
for these fixtures. If that source argument is rejected, add that named
conversion phase (including clone/difference buffers); do not infer a zero
term from historical geometry labels. Expansion layout is an additional L1
cell, not an already measured32-byte claim.

## Tracker and tree closure

The stop rule has at most 4B disagreement keys,2B estimate keys,2B charge keys:
eight per body. Estimate values exist only on force/moment rows (`verify.rs`
w construction); charge uses the same kind branch; the other keys are never
offered. Total offers≤q+2F, with F=18m+r on H, and generally
F=12m+6t+sp+3ds+r+2su. The earlier12B/3q bounds remain conservative, but8B
and q+2F are the checked narrower contracts. All original H and RF scale
fixtures have B=1, so each tracker map/holding set fits at most one 11-slot
leaf. A set after removing its last key may retain an empty root; budget it.

For each tracker j let R_j be offers so far, t_j current table len, c_j its
capacity, ℓ_j its lazy capacity. Table capacity after arbitrary shrink/rebuild
is ≤max(4,2R_j), not always next_pow2(R_j): shrinking to10 then growing to13
can request20. Use R(c,len,add) for exact capacities.

Keep distinct phase sums:

| Tracker phase | Additional live heap above other owners |
|---|---|
| offer lazy growth | Other lazy buffers + old/new current lazy + all tables + map/set nodes |
| collapse table extension | Taken lazy backing remains + all tables including active old/new table growth; no newly pruned buffer yet |
| stable sort | Other trackers' lazy buffers + all tables + sort scratch for t_j entries |
| drain to kept | Other trackers' lazy buffers + all old table capacities + newly kept growing buffer (and its old buffer during growth); draining does not free the old table allocation |
| shrink kept | Old table + kept buffer until the assignment; K6 shrink has no old/new move addition |
| replacement/finish | Old table drops after replacement; taken lazy drops before prune; subsequent tracker finish allocates no table clone |

In this source, `collapse` drops its taken lazy
**before calling prune** (`adaptive.rs:700-703`). Thus stable-sort, drain and
shrink use other trackers' lazy buffers only; the table-extension phase uses
the taken current lazy. The explicit timing avoids summing two disjoint
transients. See CAPACITY_TABLE's authoritative phase expressions.

Lazy peak caps remain source-grounded: standalone 768 rows, stop set 4096+512,
solve residual tracker plus three retained fallback trackers and one growing
tracker =512+3×512+768=2816. Fallback row lists are separate 4304-byte entries.
Map inline tracker headers are part of node layout, not those row caps.

For repeated insertion without deletion, every new split/root node remains
in the final tree: node.rs:1058-1088,1253-1262,1288-1306 and map.rs root push.
With nonroot minimum 5 and nonempty root ≥ 1, an insertion population K has
at most `1+floor((K−1)/5)` nodes. Charge each as max(actual Leaf,Internal)
unless actual node counts are retained. Empty-root retention adds the K=0
case when the container was previously populated. Removal/draining creates no
replacement tree, so retain the high-water node population rather than
recomputing it from decreasing current length.

BTreeMap::from_iter first collects an input Vec and stable-sorts it; these
are real allocations. Then append.rs bulk_push builds the right spine.
Before its final right-border repair, at K>0 the leaf count is1+floor(K/12),
and level h≥1 contributes `1+floor(K/12^(h+1))` when K≥12^h. These base12
carry counts include temporarily empty right-spine nodes. Final fix only
steals entries/edges from the plentiful left sibling; no new allocation. Charge input Vec through the bulk
build and take a max with earlier sort scratch. Clone allocates the source
topology plus recursively cloned keys/values, overlapping the original;
it is not pointer sharing. Actual private node byte layouts still need L1.

## Finish/control lifetime sums

Let K_p be the union of kept source/group/cache/state allocations, metadata
and report Arc payload at the selected path. Let D be decision-owned summary/
floor heaps, A the existing attempt array and its child heaps. There are at
most4 distinct attempt records,3 verification summaries,10 work segments and
9 prefix limits in the original schedule. Each summary owns E(B,[f64;2]),
E(B,f64), E(B,Option<f64>); each attempt can own at most 2b BlockRefusals with
its actual filter/extend capacity. These nested allocations are not covered
by sizeof(AttemptRecord).

```
finish-classify = K_p + D + A + E(q,Binary64Outcome)
                + E(B,[f64;4]) + E(B,[f64;4])
                + E(q,PublishedRow) + body_scale_collection

finish-evidence = K_p + D + A + values + publication
                + verification_summary + one_selected_record_deep_clone
                + evidence_children_in_construction

finish-box      = K_p + D + values + publication + verification_summary
                + one_selected_record_deep_clone + evidence_children
                + BoxLayout(RetainedSolve)
```

Classification's raw/coupled body-scale scratch is gone before evidence
construction. `body_scale_collection` is P(4B,tuple), not TrustedLen: its inner value is
a Map over a slice iterator, not an array covered by FlattenCompat's fixed-
size specialization. After the first item the inner lower hint is 3, yielding
initial capacity 4; later reserves occur in four-entry groups with doubling.
For B=1 capacity is exactly 4, subject to the tuple minimum-capacity class
confirmed by L1. Evidence source identity is an exact-length clone;
ledger/state encodings are C6 buffers while growing; publication body_scales
and evidence's exact-length clone coexist. absolute_verified a and unpublishable
u satisfy a+u≤q, each using its own filtered capacity. Input DOFs are E(r,Dof),
resolution/theta/floor exact B arrays, certified bounds a filtered ≤B array.
Three summaries clone their actual lengths, each bounded by4B/2B/2B.
Attempts, states, geometry and successful Arc caches are moved/shared, not
new deep copies at Box allocation.

Single-case W1 has no repeated failed verification-cache visit and no later
selected finish after verify_precision returns an error: run_schedule returns
terminal immediately. Thus cache.clone in finish_selected shares successful
payloads; its generic failed-refusal-Vec clone branch is not reached in this
single-case successful path. On the failed verification-build path the cache
stores a refusal clone while the original refusal Vec moves into the attempt;
count both until solve_cases drops groups. Prefix stops retain the partial
helper maximum before unwind. This excludes only unreachable generic reuse,
not real refusal evidence.

H keeps the last full attempt clone across subsequent repeats. While assigning
the next `w1_last_attempts`, old clone + new clone + current outcome coexist;
each deep clone includes summary/refusal child Vecs. Prefix execution keeps
the full attempts and prefix-limit labels/vector through the new solve.
prefix_matches creates full and prefix segment Vecs simultaneously, then
drops them. Five repeats are sequential; five kernel cache sets are not live.

## Binary/serde closure and remaining source cells

Five local .crate archives exactly match VR Cargo.lock checksums. All180
archive files across serde_json 1.0.151, serde/serde_core 1.0.229, itoa 1.0.18 and
zmij 1.0.23 compare byte-for-byte to installed source files. No checksum file
was presumed: these extracted trees lack .cargo-checksum.json, so archive
bytes supplied the authentication. No package was installed or fetched.
The local manifest graph requests std/default and float_roundtrip, not
preserve_order/arbitrary_precision/raw_value. Final compiled feature identity
is still a later check.

With those features, Value::Number has no arbitrary-precision string,
Map<String,Value> is BTreeMap, and json!($expr) calls to_value(&$expr): a new
serialized tree, not ownership transfer. Value::clone recursively clones its
array/string/map payload. Known-length SerializeSeq uses with_capacity(len),
strings clone exact length, maps allocate BTree nodes/keys. Define J(v)
recursively as its array requested payload plus child J, map node bound plus
key lengths plus child J, or string length; primitive leaves add no heap.
Define M(v) by replacing each growing map insertion with its proven node
high-water bound. These are closed symbolic tree formulas with Value and
node layouts left to the consumer witness.

VR lane's comparison phase holds outcome, lane K4SRC encoding, published
row map, floor member-scale map and one row's comparison temporaries. The
floor map drops at the selected branch end, before records::case_record.
Record construction retains outcome, encoding, published map and accumulated
diagnostic/control lists. Take the max of these phases.
After CaseRun returns the kernel outcome
has dropped; `run.record.clone()` creates a second record. `json!({record:record})`
creates a **third** record payload transient at emit while both earlier
records remain. Value Display streams through serde's writer, not to_string;
there is no serialized full-line String in this emit path. `run` then drops,
but the local record persists into RCM/binary64 tail. Other report emit fields
clone their strings/arrays through serialization too; list fields are not
moved out of CaseRun by json!.

H Debug/FNV and canonical digest stream. Line owns one growing String; each
numeric/hex/float to_string/format temporary overlaps that Line at append.
format's initial capacity is either0 or twice literal-piece bytes, followed
by R, so a known output-length L has retained capacity≤max(8,2L), with growing
move accounted separately. `bounded(format!(reason))` retains the full reason
while building up to 240 chars; truncation is not an earlier allocation bound.
Rows dump has an 8192-byte BufWriter on this target; initialized stdout has
a 1024-byte LineWriter buffer. These are pinned source facts, not runtime
measurements. Argument/file-read owners still need their own binary baseline
and input-envelope cells. These are not implicit kernel bytes.

VR exact comparison uses bounded decimal and dyadic Nat buffers, not a
third-party bignum. Parse mantissa digits d bound bits by4d; from_f64 bits ≤ 53
and p2∈[−1074,971]. Align adds exponent differences to bit counts
(`bits+Δp2+4Δp10`), addition adds at most1 bit, multiplication sums bits.
The precise source operators allocate: shl's initial word-prefix plus grown
output; mul_pow10's exact clone with growth; add max-limb+1 output; sub
left-limb output; mul's u64 accumulator plus u32 destination (alignment
prevents in-place reuse); parse digit String/chunk-reference Vec. One
comparison row runs at a time. SOURCE_PARAMETERS retains per-case decimal
digit/exponent bounds. `comparison_bound` in the script composes the source operator DAG and charges
all fresh allocation requests of its alternative scalar, magnitude, floor,
outside-binary64 and control branches together. This allocation-volume upper
is conservative for simultaneous live scratch; sequential row loops use its
maximum, not their sum. Across 24 RF cases the maximum is 345,392 requested
bytes, with a 49,062-bit intermediate-significand upper in this interval
arithmetic. It computes no comparison result or model value. Only actual
reference/control decimal fields feed it; model hex strings are excluded.
Persistent caller objects and diagnostic formatting remain separate. This
closes the symbolic scratch cell subject to independent accounting review.

Still OPEN: complete H reason-template/Line maximum and argv/file-read envelope;
VR full-family parsing/model input trees and final binary64-tail envelope.
All dependencies needed for the consulted serde/core paths are present;
these are identified source-composition work, not missing-tool excuses.
No final E_max, corrected numerical replay or A1-compatible bound is claimed.
CAPACITY_TABLE.json and RETURN.md give the minimal follow-up cells and layout
requests rather than substituting an arbitrary fixed allowance.
