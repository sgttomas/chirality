# Formula candidate and record arithmetic

**Status: a conditional full-phase specification plus an evaluated, incomplete
schedule normalization. Neither is a final E_max or an admission grant.**
No Rust/compiler/allocator/solver measurement was performed. All evaluated
figures use the preserved counts and explicitly identified historical ABI
assumptions. A1's final candidate does not exist in this assignment.

`ALLOCATIONS.md` defines n, m, f, z, s, q, b, B and the capacity notation.
Source/input basis is `3bddc2b05f6106e969c7cf43373b230845c7cc66`.

## Full-phase specification

For binary j, input x, precision p and reachable phase a, define:

```
L(a,x,j) = binary_owned(a,x,j)
         + sum(requested_capacity(v,a,x) * layout(element(v)))
         + sum(heap_owned_control_object_sizes(a,x))
         + active_library_scratch(a,x)
         + one_active_reallocation_old_buffer(a,x)

E_all(x,j) = max over reachable source/count/group/build/solve/verification/
            shift/decision/finish/refusal/prefix phases a of L(a,x,j)
```

The sums enumerate allocation identities from ALLOCATIONS.md. A moved Vec
does not add a second buffer; a deep clone does. Arc clones share payload;
error/refusal Vec clones do not. A cap accounts requested live allocator
bytes; E_all must dominate the allocator's **move** peak, independently of
the in-place cap. RSS/physical footprint remain separately calibrated.

The schedule's retained envelope before phase p is the union of the source,
group and case data, completed lower/equal-precision Shared/Solved payloads,
completed VerifyShared payloads, and attempt/cache metadata. A previous
VerificationReport is dropped after that loop iteration; reports are not
accumulated across all precisions. A rejected solved verification becomes
the next candidate by Arc reuse. Failed builds add their partial phase peak
and retained failure evidence; they do not contribute a completed payload.
Keeping all successful payloads as a conservative envelope is permitted only
after error and control storage is also counted.

The intended bound domain is the original I21 contract: H's 33 sealed W1
fixtures, their specified precisions/budget prefixes/repeats, and VR's original
named RF-LARGE scale runs with its existing suite/count compatibility checks.
It is not a promise for arbitrary PrimitiveSource, combinations, unbounded
multi-case invocations, unbounded reference strings, or arbitrary parser input.
Additional adapter shapes already exercised by VR's 193 factored count checks
must retain correct count/estimate behavior, without turning this work into a
new all-kernel-input memory theorem. ALLOCATIONS.md marks the wider source
paths for separation and future applicability, not as automatic I21 scope.

This specification is intentionally not implemented as `old E_max + delta`.
The implementation should expose named phase byte sums and take their max.
Nonnegative checked arithmetic must refuse on count/layout overflow; a
wrapped u128/u64 must never produce a small admission value.

## Closed lifetime corrections

With `o = sizeof(Option<Wide<L>>)` and `w = sizeof(Wide<L>)`, the inner Uc
helper peak is:

```
Uc-u:       2 f w                       # a + c
Uc-nl:      4 f w                       # retained c + at + bt + ct
Uc-form:    2 f w + 2 b w + b BlockBound # c + ct + u + n_l + out
```

The caller also holds bounded coefficients, Abar, ke_w, its f×u32
block-of-rows mapping and b refusal slots. `bounded` has no explicit drop
before Uc; it remains in the build closure. The m×144 bounded assembly
blocks were destroyed on assemble_bounded return. Temporary member operators
at qW were destroyed on the formation `else` return. Therefore:

```
VerifyBuild = kept_before + complete_VerifyShared_payload_envelope
            + bounded_coefficients + uc_refused_slots
            + max(bounded_block_scratch,
                  qW_member_and_directional_scratch,
                  Uc_helpers + block_of_rows + maxima)
```

Any output bytes already included in complete_VerifyShared must not be
added twice by a supposedly exact phase sum. The evaluated normalization
deliberately overbounds them at helper peaks and says so in its code.

At the shift's nl_pass peak:

```
row/skyline portion = 3 q o
                    + s w + 36 f            # ScaledProfile
                    + s w + 32 f + f o      # ShiftedFactor, no work
                    + 3 f w                 # at, bt, ct
```

Add the pass's live locals and **all** caller/schedule per-block allocations:
data, s_refused, start, results, current, sigma, in_flight, refused, failed.
At the result-forming subphase, replace 3fw by fw+bw+next's allocation;
factorization instead has fw for its work. The peak is the max of these
phases. At most three factorization attempts are sequential, not three
simultaneously live shifted factors.

Under the old ABI observation `o=w`, the known row/skyline correction to
H's old at_shift is exactly `2 f w - 8(3q+f)`. At P=1024 on both TREE
10,000-member counts, this is **10,799,688 B**. It excludes additional
per-block, capacity and binary corrections. At lower precision the net
delta can be negative; applying a positive 1024 delta to every phase would
not derive the phase model.

| RF CHAIN/TREE members | f | q | P256 delta | P512 delta | P1024 delta | Uc c+at+bt+ct at P1024 |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 60 | 263 | -1,032 | 2,808 | 10,488 | 34,560 |
| 100 | 600 | 2,513 | -7,512 | 30,888 | 107,688 | 345,600 |
| 1,000 | 6,000 | 25,013 | -72,312 | 311,688 | 1,079,688 | 3,456,000 |
| 10,000 | 60,000 | 250,013 | -720,312 | 3,119,688 | 10,799,688 | 34,560,000 |

Full per-model counts, phase values and deltas, including CONT and both
orientations, are in provisional_results.json. No matrix was constructed.

## Evaluated normalization N0

`derive_checkpoint0.py:normalized` computes named candidate phases from the
33 H counts lines. This is a **new analysis**, not a reissued historical
audit result. N0 does the following explicitly:

- Replaces the shift's work by at/bt/ct; makes separate factor/nl/result
  phases; uses o=w only as a historical layout assumption.
- Adds per-block slots, shift results and report structures with stated ABI
  ceilings; their sizes need a pinned witness, not extrapolation from M5.
- Takes the maximum over bounded formation, qW formation and Uc scratch.
- Adds formation_scale/recovery scratch as another pass candidate.
- Adds factor-work/condition helper candidates and retains a conservative
  tracker-table normalization that allows source/drained/pruned buffers.
- Reuses the old fixed, Shared, state and broad solve envelopes where full
  capacity/control closure is **not** yet proved. It deliberately does not
  invent numeric completion of the OPEN finish/geometry/binary terms.

This last property prevents calling N0 a heap upper bound even if its maximum
is above every recorded measurement. It is nevertheless a concrete source-
derived phase candidate and a replay input useful for assessing the scale of
the known repair.

| Model family, AX | members | N0 with H fixed (B) | Peak among evaluated phases |
|---|---:|---:|---|
| CHAIN | 10 | 22,804,868 | decide_1024 |
| TREE | 10 | 22,804,440 | decide_1024 |
| CONT | 10 | 22,737,597 | decide_1024 |
| CHAIN | 100 | 49,034,474 | decide_1024 |
| TREE | 100 | 49,042,422 | decide_1024 |
| CONT | 100 | 48,322,189 | decide_1024 |
| CHAIN | 1,000 | 316,623,240 | solve_1024 |
| TREE | 1,000 | 316,714,314 | solve_1024 |
| CONT | 1,000 | 305,093,532 | solve_1024 |
| CHAIN | 10,000 | 3,020,639,308 | pass_1024 |
| TREE | 10,000 | 3,021,567,276 | pass_1024 |
| CONT | 10,000 | 2,862,641,205 | decide_1024 |

The 10,000 TREE H result is only 1,786 B above the old known-term correction;
this is not justification for treating omitted capacities as zero. The per-
block correction is small for one block, while other models can have many.

## Binary fixed terms and coverage limits

The historical like-for-like comparison uses:

```
N0_vk = N0_h - old_H_fixed + old_VR_fixed
```

It never compares a k6_observe fixed term directly to a vk_scale peak.
For TREE-n10000-AX/ROT, N0_vk is 3,048,041,328 / 3,050,290,050 B; the
preserved in-place and move peaks are 3,030,269,132 / 3,031,977,247 B.
Their margins are 17,772,196 / 18,312,803 B. These are conditional
normalization comparisons, not fixed-term validation.

Old H fixed explicitly counts model nodes, member labels/indices, loads and
FrameElements; two source payloads; case ledger/prescribed/encoding/layout;
group sparse structure/order/blocks (`counts.rs:424-447`). Old VR substitutes
its own model/lane map term (`scale.rs:263-275`) but also has Case/reference
data, lane encoding, JSON records and output-format allocations. Its BTree
entry overhead is an amortized assumption, not a proved per-input capacity.

Prefer a reviewed `BinaryEnvelope` adapter giving actual retained capacities,
maximum format/reference scratch and feature identity, while kernel phases
stay common. A binary can record current allocator-live bytes at a clean
counts boundary, but that only replaces **already live** objects; it does not
bound future record/serialization allocations or the earlier parse peak.
The counts-only process must itself remain under the cap. Making this API
concrete probably needs H main/allocator reporting in addition to the old
write fence; obtain ROOT's exact path addition before editing.

## Capacity and layout obligations

1. Reserve/clone/TrustedLen vectors: prove requested capacities from pinned
   stdlib behavior or use a conservative bound checked against that build.
   `with_capacity(k)` alone guarantees a minimum, not the implementation's
   universal upper bound. Preserve zero-length behavior.
2. Push/filter/Result-collect/encoding vectors: account initial minimum,
   doubling, extend reserve, source-capacity reuse and shrink behavior.
   A next-power-of-two rule is provisional until checked. Per-inner-vector
   sums matter for graph adjacency, supports and prescribed terms.
3. Dedup retains capacity; use pre-dedup multiplicity, not z alone. Stable
   sort may allocate scratch. VecDeque and BTree allocations require their
   own model; they do not share Vec's rule.
4. Tracker `prune` drains an allocated table into growing `kept` before
   assigning it, and `shrink_to_fit` may allocate/move. Test this independently
   of lazy-row caps; the old table allowance is not accepted by restatement.
5. A1 may invalidate all precision/row/control assumptions. No final W1
   limit, bound claim or final-formula replay can be sealed before the impact
   ledger's final-candidate check.

The pinned compiler was absent at launch. DELIVERY subsequently relayed
ROOT's successful isolated exact-1.97.1 native installation; this TASK did
not inspect that installation or invoke it. This checkpoint still authorizes
no compiler, build or model execution. Those witnesses remain required.
More source derivation can
close the explicit OPEN terms without a build; the first runtime checks then
validate the parameterized model, rather than infer it from spare measured
memory.
