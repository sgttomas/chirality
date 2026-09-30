# I21-K6C allocation inventory — source checkpoint

Source basis: `3bddc2b05f6106e969c7cf43373b230845c7cc66`. Aliases: `P = projects/chirality-piping`,
`FK = P/core/solver/frame_kernel`, `K = FK/src/structural/retained`,
`H = P/core/solver/performance_harness`, `VR = P/validation/benchmarks/numerical_robustness`.
All line references are on this basis, not the obsolete line numbers in I21.

This is an allocation/lifetime inventory and conditional accounting contract.
It does **not** establish a complete numeric upper heap bound. In particular,
the library-capacity, binary-owned, geometry-expansion and finish-accounting
items marked OPEN must not disappear into an unexplained fixed allowance.
`FORMULA.md` separates the computable normalization from those obligations.

## Counting language

`N` nodes; `n = 6N`; `m` members; `f` free DOFs; `z` stored pattern entries;
`s` skyline entries; `q` publication rows; `b` free blocks; `B` bodies;
`r` constraints; `l` loads; `t` stations; `sp`, `ds`, `su` scalar springs,
directional springs and support groups. Let `c = 78m + sp + 6ds` be the
number of tagged upper contributions for accepted nondegenerate members.
For W1's H adapter, `sp=ds=su=0`, `t=m`, every prescribed value is zero;
VR's adapter is more general. Do not infer these equalities merely from a
VR model's member count.

`E(k,T)` means one allocation with known requested capacity k and element
layout T. `G(k,T)` means a growing/filtered allocation whose capacity must
be bounded by the selected liballoc contract. `M(k,T)` includes the old
buffer during a growing realloc. `Cl(x)` is a distinct clone allocation;
it is not an Arc reference increment. For nested vectors, count the outer
allocation's Vec headers and each inner allocation separately. Stack Vec
headers do not count as allocator heap. Heap-owned structs include their
inline Vec headers once. Allocation identities, not variable names reused
at later stages, govern whether storage is shared.

The historical assumptions are `w(L)=8L+16`, `Option<Wide<L>>=w(L)`,
Vec header 24 B, usize 8 B; L=4/4/8/16 at p=128/256/512/1024, residual
L=4/8/16/16, verification qW L=8/16/16. They require the pinned build's
witness. `Wide`, `WideContext`, `ExactWideSum` and their arithmetic scratch
are inline arrays, not hidden Vec heaps (`wide.rs:200`, `wide/multi.rs:1122`,
`wide_sum.rs:112`). An `ExactWideSum` becomes heap data when it is an
element of a tracker/fallback Vec. Its historical aligned layout is 2144 B;
a tracker/fallback row is 4304 B. General Rust layout/capacity guarantees
alone do not prove all these equalities.

## Source, group, counts and fixed owners

| Phase / source | Allocations and capacity | Lifetime / overlap and status |
|---|---|---|
| Binary load and counts; H counts `:166-217`; H adapter `:40-85`; VR example `:381-425` | H K6Model node/member/label/load vectors, frame Vec; VR Case/model/reference/JSON strings and maps; temporary source; encoding; count adjacency/profile work | Count-only construction occurs **before** estimate admission; allocator cap already applies. Binary-owned data must be bounded independently. H's fixed `64N+80m+16l+sizeof(FrameElement)m` and VR `model_bytes` are old model estimates, not current capacity measurements. OPEN: parser/reference/record/string capacities and phase peak envelope. |
| PrimitiveSource creation; source `:351-583`, `:321-348` | SourceParts' nodes/members/springs/directional/constraints/loads/stations/support vectors move into source; load source-id strings and support-id subvectors; `constrained: E(n,Option<f64>)`; `body_of_node: E(N,u32)`; `parent:E(N,usize)`; `body_of_root:E(N,u32)`; chord `E(3,ExactWideSum)` | Source arrays persist until source drop; parent/body_of_root/chord return scratch. Stable sorts on source arrays require scratch separately. Under FK test/mutation-controls `caller_order` clones six arrays plus their strings, even for NONE; ordinary H dependency build does not set FK cfg(test). Feature-specific witnesses required. |
| Source encodings; source `:652-746` | Growing byte buffers for K4SRC and K4STF; out starts with six bytes and repeatedly extends | K4STF remains in solve_cases' group tuple; CasePrep identity K4SRC persists; caller VR lane also holds K4SRC. These are **distinct**. Old fixed has one `enc`; it is not a proof of all encodings' capacities. |
| Geometry; factor `:130-217`; FK `src/rigid_body.rs:33-239` | Per-body filtered nodes; `local_of` BTreeMap; coordinates; grounds; not_spanning; per-node directions; SVD relative/original/cloned b; candidates; exact_motions (6 Expansion headers/node and owned terms); recovered node_motion | Body work is sequential. NotAssessed stores not_spanning in geometry. Refusal may materialize a node-motion witness before discarding it. Growth, BTree nodes and Expansion::add replacement buffers (`structural.rs:707`) are OPEN transitive allocations; successful large restrained fixtures do not exclude this refusal phase. |
| Structure build; assemble `:548-651`, sparse `:58-78,:133-160` | `positions:G(c,(usize,usize))`; SparsePattern temporary rows headers and symmetric pre-dedup adjacency entries (≤2c); persistent row_starts E(n+1,usize), columns G(z,usize), transpose E(z,usize); tagged G(c,(usize,Contribution)); starts E(z+1,usize), next E(z+1,usize), items E(c,Contribution) | `positions` remains until Structure::new returns. Pattern row lists may retain duplicate-related capacity after dedup. `tagged` is consumed while items/starts/next exist, so its backing allocation persists through iteration. Pattern result persists; next/positions/tagged are then freed. Old `32c` transient is not a complete construction derivation. No dense matrix. |
| Ordering; factor `:226-398` | free filtered G(f,usize); position E(n,usize); adjacency outer/inner; RCM neighbors outer plus **both directed insertions** before dedup; degrees E(f,usize), visited E(f,bool), order E(f,usize), queue VecDeque; reachable and two BFS levels/last-level/next-level, marked; rank, first E(f,usize) | Adjacency persists through RCM and first construction. Neighbor capacity reflects pre-dedup insertion counts. BFS old level and new level overlap at assignment. VecDeque growth and stable neighbor degree-sort scratch need liballoc accounting. Keep free/position/order/rank/first only. |
| Free blocks; bound `:96-132` | of E(f,u32), positions G(b,Vec<usize>), component G(f_b,usize) per block, body E(b,u32), DFS stack G(f_b,usize) | All earlier component allocations persist while next block is built. Stack is freed each component. Sum component capacities is not necessarily f. |
| Case prep and ledger; adaptive `:856-933`, ledger `:88-128` | Second source clone; ledger building G(unique-loaded-DOFs,(usize,ExactAccumulator,bool)); final ledger entries and each net magnitude Vec; nonzero bool vector; prescribed E(r,(usize,Vec<(f64,f64)>)) and one term per constraint; identity G(enc,u8); layout G(q,QuantityMeta); extents E(B,f64) | ExactAccumulator is 2×68 u64 =1088 inline B. Netted result is created while the whole build array still lives. Each general net may use up to 68 limbs, whereas the old 64B/load models short nets. CasePrep source and caller source overlap throughout call. Combination operands/terms are not W1's single-case schedule; no multi-case bound is asserted. |
| Call/group/cache scaffolding; adaptive `:2750-2772,:3106-3119,:3447-3508` | Groups Vec with K4STF, Arc<GroupPrep>, GroupCache; output Vec; Arc<CasePrep>; geometry clone; attempts growing Vec; states growing Vec; Arc allocations for each completed Shared/VerifyShared/Solved | Arc clones preserve a single payload; failed cache slots retain stop, inline work, and verification-refusal Vec. Heap Arc headers/boxed selected outcome and Vec control objects remain OPEN layout facts. Up to four distinct precision states and three verification builds; repeats are separate calls. |

## Precision builds, solve and fallback

| Phase / source | Live additions | Lifetime / capacity consequence |
|---|---|---|
| Form members p; adaptive `:1265`, assemble `:65-97,:form_members` | E(m,MemberOperators<L>), directional E(ds,DirectionalBlock<L>); member holds 164 wides + padded IDs, directional holds nine wides + node/kind | Return vectors are reserved by member/directional count. All earlier precision caches/states persist. |
| Assemble p; assemble `:699-759` | K E(z,Wide<L>), done E(z,bool) | done is scratch and drops at assemble return. The source's full member list remains. Mutant-only contribution term vectors are not a production NONE allocation. |
| Re-form residual q; adaptive `:1280-1314` | members_q E(m,MemberOperators<R>) when q≠p; directional_q; K_q E(z,Wide<R>); bounded_q E(m,BoundedCoefficients<R>); assemble done E(z,bool) | members_q drops at the `else` block boundary, before factorization. bounded_q and directional_q persist in Shared. At p=1024 K_q is still a new widened Vec, not an alias of K. |
| Factor p; factor `:505-604` | profile inner rows totaling s wides; outer E(f,Vec); scale E(f,i64); first clone E(f,usize); screens E(f,PivotScreen<L>); work E(f,Wide<L>); order clone E(f,usize) | factor's work drops on return; it must be in **factor-build** phase only. Partial pivot/negative-energy/budget exits drop partial buffers; retain their pre-stop maxima. Result's payload = s*w + f*(2w+56) under historical ABI. |
| Condition; factor `:695-812`; bound `:171-212` | x, y, signs, z; solve_scaled local x/out; alternating/y tail; BlockRatios clone of positions and est per block at p≥256 | During second solve_scaled, outer x/y/signs plus inner x/out yield five f-wide buffers. BlockRatios.positions remains until estimates consumes it. No simultaneously live vectors from all five iterations. |
| Pivot tracker; adaptive `:1348-1365,:625-778` | BoundedExtremeTracker lazy/table, stable-sort scratch, prune kept table and shrink realloc overlap | Historical 768 lazy rows bound retained conditionally. Table's old allocation, newly kept table and growth old/new can overlap; old `(2+1)f*40` requires proof. Conservative normalization uses five offered-row equivalents. BTree nodes absent for this standalone tracker. |
| RHS/first solve; adaptive `:1694-1725`, assemble `:818-850`, factor `:630-678` | u E(n,Wide<L>), rhs E(f,Wide<L>), u_free; factor.solve scaled Result-collect, solve_scaled x/out, final Result-collect out | Result-collect may grow rather than allocate f exactly; must use a checked G capacity contract. At most one factor solve at a time, but inputs and returned output overlap. q-width four-n envelope in old solve is conservative in length, not a proof of every capacity. |
| Coalesced residual/refinement; adaptive `:1412-1478,:1729-1814` | evaluated outer growing Vec, up to four cloned f-wide states; u_free; u; rhs; residual rows E(f,(bool,f64,Wide<L>)); tracker; correction and factor solve temporary arrays | A new evaluated clone remains even after residual_rows returns. The residual row list and tracker stay alive during fallback invocation. When chosen evaluated[k] is cloned to replace u_free, old u_free survives through RHS evaluation of assignment. Up to three corrections; no fifth evaluated state. |
| Fallback bounded assembly; adaptive `:1560-1577`; assemble `:775-814` | Abar_q E(z,Wide<R>), temporary m 12×12 blocks at R; u, rhs, u_free, evaluated and caller's residual row/tracker storage remain | blocks drop at assemble_bounded return. They do not overlap fallback row-list construction. |
| Fallback per evaluated state; adaptive `:1577-1664` | one full u clone n wides; growing rows of (ExactWideSum,ExactWideSum,f64), historical size4304; worsts (≤4 GateRatio options); states (≤4 trackers); previous states' tracker/table heaps; current tracker; Abar_q | Peak row-list move capacity uses C+C/2 with C=next_pow2(f) for this >1024B element. Iterating consumes rows but backing allocation lives until loop completes. Failed eligibility drops current rows/tracker at continue; previous states remain. State loop does not retain four full row lists. |
| Recovery; recover `:239-478` | values E(q,Wide<L>), q_all E(m,[Wide;6]); end_actions E(m,[Wide;12]); scalar/directional action arrays; reaction E(n,Option<Wide>) | q_all and values persist in Solved; other buffers drop on recover return. At recovery, u/rhs/u_free/evaluated remain in solve scope. Current old solve envelope has slack, but no proved relation for every capacity/shape; a named recovery phase is required. |

## Verification, shift, decisions and unwind

| Phase / source | Live additions | Lifetime / capacity consequence |
|---|---|---|
| VerifyShared bounded assembly; verify `:443-471` | uc_refused E(b,Option<BoundRefusal>) outside closure; bounded E(m,BoundedCoefficients<L>); Abar E(z,Wide<L>); assemble_bounded blocks E(m,[Wide;144]) | bounded remains in closure until build returns. Bounded blocks drop at assemble_bounded return, **before** qW member formation or uc_bounds. |
| qW formation; verify `:475-501` | members_w E(m,MemberOperators<W>) when qW≠P; directional_w temporary operators; ke_w E(m,[Wide<W>;144]); returned directional_w matrices | Temporary members_w/directional operators drop at the `else` boundary. ke_w/matrices persist. At P=1024 qW=P, full_ke still allocates matrices. |
| Uc u_pass; verify `:490-501`, bound `:378-469` | block_of_rows E(f,u32); returned c from u_pass; u_pass a E(f,Wide<L>) | a and c coexist inside u_pass; a drops on return. bounded, Abar, ke_w, refusal slots and earlier caches remain. |
| Uc nl_pass; bound `:683-684`, `:485-565` | **c + at + bt + ct = four f-wide buffers** | c is a local of uc_bounds, used later in block_max; at/bt are locals of nl_pass, ct clone made before its return. Thus four-way overlap follows lexical ownership without an optimizer assumption. at/bt drop only when nl_pass returns. No m×144 bounded blocks or qW member temporary overlaps this phase. |
| Uc bound construction; bound `:683-707` | c,ct; u E(b,Wide); n_l E(b,Wide); out E(b,BlockBound<L>); caller block_of_rows and uc_refused | Out persists in VerifyShared; c/ct/u/n_l/rows/bounded/refusal slots drop at build completion. Partial refusal blocks still occupy every allocated row and block slot. A refusal is not a capacity reduction. |
| Early verify pass / formation_scale; verify `:759-800`, `:951`; formation_scale `:102-285` | w_abs n; e_rows q options; resolution B×2f64; q_all m×6, actions_all m×12, spring/directional action arrays, reaction n options; temporary resolution maxima B×2wide; resolution_hats output B×2f64 | formation_scale's q/actions/reaction scratch drops on return. Its second call for a_s runs with e_rows/w, much of pass live storage and output a_s. It is a separate possible peak from shift. |
| Prescribed/residual/correction; verify `:804-904` | terms_w and terms_p n Vec headers each plus each nonzero prescribed operand; two n bool flags; u_free, r_hat,sr_row; factor.solve temporary arrays; delta; delta_full; recovered q_all/values and recovery scratch; w q options | At shift, terms plus three n-wide arrays (w_abs,delta_full,w_s), eight f-wide arrays (u_free,r_hat,sr_row,delta,sr2,sas_inf,sas_one,sau), recovered q+6m and first three option-row vectors remain. Scratch operands clone at most one terms_w list inside contribution_products `:661`; include its capacity separately. |
| Norms/a_s; verify `:904-969` | sr2_row,sas_inf_row,sas_one_col,sau_row f; w_s n; a_s q options, formation_scale scratch above | Full live vector count is the old `live` expression; it excludes per-block/per-body and phase helper scratch. Prescribed Vecs are ordinary growing pushes; r×w is only payload, not a capacity bound. |
| Shift preparation; verify `:979-1018`; bound `:1187-1268` | data E(b,bool), s_refused E(b,Option<BoundRefusal>), start G(b,(usize,Wide,usize)); profile outer f headers, first f usize, block_of_row f u32, inner s wides | Profile remains through shift_schedule, drops at shift_run return. Empty start does not allocate profile. Profile-build refusal drops partial rows then marks s_refused for each start. |
| Shift scheduling and factor; bound `:1011-1056`, `:843-935` | results E(start_count,(usize,ShiftResult)); current clone; in_flight growing usize; refused E(b,Option<BoundRefusal>); sigma E(b,Option<Wide>); clone profile rows/first; shifted E(f,Option<Wide>); failed E(b,bool); **work E(f,Wide)** | Caller start, data, s_refused and profile remain. `work` belongs to shifted_factor and is not returned. It is dropped at function return even if allocator/compiler retains address ranges for reuse; allocated live bytes exclude freed requests. |
| Shift nl_pass; bound `:1059`, `:485-565` | all above returned factor data plus **at,bt,ct**, each f wides; **no work** | Correct row-wide addition relative to old pass = +2f*w. Historical Option overcount subtracts 8(3q+f). Per-block sigma/results/refusals/failed are additional. This is not uc_bounds: no retained c precedes this nl_pass. |
| Shift result formation/retry; bound `:1060-1129` | returned ct f, n_l b, next growing (usize,Wide,usize); previous current backing array persists through into_iter; result/update/refusal slots | at/bt have dropped. current=next happens before the old iteration's f/sigma/ct/n_l scope ends; next becomes current, but previous and next **profiles/factors** do not overlap across iterations. At most three sequential factors; never multiply factor memory by three. |
| Post-shift certificate/report; verify `:1019-1212`; bound `:1274-1315` | shifts results, data/s_refused/start still in closure; BlockCertificate b; BlockNorms b×7wide; theta b options; BodyReport B×13wide; charge and w_plus q options | Report owns e_rows,w,a_s,charge,w_plus,r_hat,delta,certificates,norms,theta,bodies,resolution. Other pass locals are dropped only when closure returns. Refusal/missing-bound early exits occur **after** some certificate allocations. |
| Decision/scales; adaptive `:1904-1948,:2021-2272` | report + cached payloads; skip q bool; raw/coupled scale arrays B×4wide overlap; hats B×2f64; optional floor B×2f64; TrackerSet BTreeMap and holding BTreeSet, lazy rows, table(s), stable-sort/prune/shrink scratch; three summary growing arrays keyed by body/kind | At most 12B tracker keys and 3q offered rows. G=4096/T=512 lazy bound historical; maps/sets must be budgeted in addition. `into_trackers` consumes the map; remaining tree nodes can overlap finished summary vectors. OPEN exact table/stdlib bound; no assumption of zero bytes merely for small B. |
| Selected finish; adaptive `:3295-3410,:2598-2657`; recover `:495-519` | selected.published q Binary64Outcome; classification raw/coupled f64 scales; PublishedRow q; publication body scales; verification summary theta/bounds/resolution; selected_record clone incl refusal Vec; evidence copies of summaries/body scales, input DOFs, absolute/unpublishable lists, source identity, ledger encoding, retained-state growing encoding, geometry and attempts; Box<RetainedSolve> | Report still lives at call site while finish_selected runs; selected state/caches are Arc-shared. Two copies of body_scales coexist. Classification output and evidence lists have filter/collect growth. State encoding capacity is not its final length. OPEN full capacity/formatting/binary-record envelope. |
| Refusal, budget and cache reuse; adaptive `:2782-2822,:2962-3015,:3017-3082`; bound A2 | Partial allocation prefixes; closure drops on Err; uc_refused→Vec<BlockRefusal>; stopped VerifySlot refusal clone; attempt.bound_refusals; verification summary clones; cached-hit refusal clones | On failed shared build the successful-payload cache does not exist, but prior precision caches remain. Full-success envelope can overbound absent payload only if it separately budgets error/control allocations. Cache hits clone Arc, not payload; error Vec clones are real allocations. Single-case W1 does not justify a bound for unbounded multi-case solve_cases retaining all outputs. |

## What can and cannot be concluded now

### Original I21 domain versus broader API inventory

The admission estimate under repair covers the original H/VR W1 schedule,
not every valid PrimitiveSource invocation. H's 33 sealed fixtures and VR's
18 named RF-LARGE scale models are finite input contracts; their precision
escalations, refusal/stop exits, prefixes, repeats and output paths still need
complete coverage. Existing VR count tests cover 193 factored CI cases; keep
their adapter/storage-count semantics and the full VR suite. A passing test
does not add a new arbitrary-input memory guarantee.

For the RF-LARGE scale rows, both recorded count sets identify zero springs;
H's adapter also explicitly excludes springs, directional springs and support
groups and sets all constraints to zero. Thus nonzero prescribed-operand
lists and arbitrary support-id/string multiplicity are broader API examples,
not reasons to expand I21. The general table names them so an adapter cannot
silently map a supported nonzero shape to zero. H/VR fixture identity and
adapter restrictions must be checked before applying a reduced expression.

Likewise, combinations and multi-case output accumulation are expressly outside
the single-case W1 envelope. Generic mechanism-witness/NotAssessed geometry
is a separate source branch: a source proof of its exclusion on the sealed
W1 scale fixtures can close that branch for this contract; it need not be
fully budgeted for all possible caller inputs. Retain the existing VR
mechanism/refusal tests without claiming that every such path is timed scale
work. Stable sorting, actual retained capacities, CasePrep/group encodings,
report/finish and refusal metadata on the real W1 schedule are genuinely
reachable gaps and cannot be dismissed this way.

The two nl_pass lifetime conclusions are closed by source inspection. They
apply equally to successful, per-block-refused and later-budget-stopped
paths up to their allocation points. The m×144 bounded formation buffers and
temporary qW members are **not** live during Uc; the persistent `bounded`
coefficients are. Thus verify-build must use a maximum across those helper
phases, not add all helper scratch to all later helpers.

The old source formulas do not encode enough facts to certify every row in
this inventory. In particular, `Vec::len`, post-dedup count, scalar source
encoding length and member count do not bound every retained capacity,
source string, standard-library tree or serialization allocation by themselves.
The inventory's OPEN entries are explicit work, not permission to patch FK,
change the guarantee, or silently use measured slack. See the precise next
conditions in RETURN.md.
