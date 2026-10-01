# Additive source completion of the three binary-envelope cells

Source basis: `3bddc2b05f6106e969c7cf43373b230845c7cc66`. The parent
continuation_01 packet is unchanged. These are source-derived, parameterized
upper sums for requested allocator heap, including K6's growing-realloc move
counter. They are not measured heap, final E_max, admission, or A1 acceptance.

Aliases: FK=P/core/solver/frame_kernel; SD=P/core/solver/sparse_direct;
H=P/core/solver/performance_harness; VR=P/validation/benchmarks/numerical_robustness;
P=projects/chirality-piping. K=FK/src/structural/retained. L is the previously
pinned Rust 1.97.1 library. J is the authenticated serde_json 1.0.151 source.
INPUTS.json pins the actual additional sources; the parent pins remain valid.

## Common operators and required input values

`σT` and `αT` are actual size/alignment of type T, supplied by a later real
layout witness. `E(k,T)=kσT`. `P(k,T)` is the **capacity in elements** of a
fresh push-only Vec: 0 at k=0, otherwise max(min(T),next_pow2(k)). min(T)
is 8/4/1 for sizes 1 / 2…1024 / >1024. `G(k,T)=P(k,T)σT`.
`MG(k,T)` charges the growing buffer plus its predecessor; ≤1.5G is safe
once it has grown, and ≤1.5G remains an upper bound for the small initial
allocation. `A(k,T)=max(min(T),2k)σT` (zero for k=0) is the safe generic
iterator/resize capacity envelope when a positive lower hint or an exact
non-power-of-two starting capacity prevents using P. `MA=1.5A` is its
growing-move envelope. For exact results, retain the source reserve recurrence
`c'=max(2c,len+additional,min(T))` from the parent packet.

`Sort(k,T)=max(k,48)σT` is the pinned stable-sort scratch upper; unstable
sort has no heap scratch. `Text(L)=max(8,2L)` and `MText(L)=1.5Text(L)`
bound a nonempty format/String output of at most L UTF-8 bytes; a known
borrowed String clone instead requests exactly its length. A literal-only
format can allocate less. These functions include no OS allocator padding.

`TI(k,K,V)` is the insertion tree allocation: zero for a never-populated
empty map; otherwise at most `(1+floor((k−1)/5))*max(σLeaf<K,V>,σInternal<K,V>)`
for k > 0. For deletion/iteration, retain the prior population's bound until
nodes are freed; an emptied existing root may remain. `TB(k,K,V)` uses
the parent-proved bulk counts: leaves=1+floor(k/12), and internal level h≥1
has 1+floor(k/12^(h+1)) nodes when k≥12^h. Add actual key/value child heaps.
`TB` includes temporarily empty right-spine nodes before right-border repair.

Every future run packet must bind these **values**, without changing the
formulas: exact argv strings/count/UTF-8 byte lengths; selected file paths
and lengths; immutable file byte lengths F and SHA256; metadata-size hint H
if not using the exact-file branch; parsed shape/count/string-length descriptor;
candidate/feature/toolchain identity; and actual layout cells. Existing
PARAMETERS.json supplies the 24-case family file's byte length and compact
JSON shape histograms. The twelve large-model hashes stay historical expected
identities until actual prepared bytes are supplied. Missing values do not
leave a source-composition hole.

Incoming runtime-owned requested live bytes at the observation entry are
`B0`. This is an explicit baseline input to the **binary** envelope, not
measured slack substituted for a kernel term. Later lazily created stdout,
file/path, parser and output allocations are explicitly added below. If a
whole-process claim includes pre-entry runtime startup, its baseline witness
must cover that separately; these sums do not invent a startup constant.

## S-H-LineReasonTemplateMax: closed formatting and input/I/O sum

### Finite reason grammar and every Line

`derive_envelope_parameters.py` reads the actual enum declarations and
applies the pinned non-alternate Debug grammar. A unit variant contributes
its name; a tuple contributes name/parentheses/separators and child bounds;
a struct contributes name/braces/field labels/separators and child bounds.
Numeric limits are u8=3, u32=10, u64/usize=20 and u128=39 decimal digits.
Static text uses the maximum raw literal byte length in the pinned producer
sources, with a conservative 6× escaped-string allowance. GeometryUnavailable
can receive only Range/InvalidInput from this geometry/Expansion path, not
an arbitrary StructuralError direction Vec. Refusal's fixed six-component
rigid-parameter array is nevertheless retained in the common reason bound;
there is no variable-size formatted vector in the reachable W1 reason types.

The deliberately conservative no-precision binary64 text bound is 1137 bytes:
2 for sign/point, 1074 fractional binary64 positions, a 53-digit significand
upper and 8 for exponent syntax. Shortest/exponential output is much shorter;
the upper uses binary64 range and the source's no-precision format sites,
not an empirical maximum. Arbitrary user Display implementations or format
precision/width are outside these fixed call sites.

The checked grammar yields SourceError 75, AttemptOutcome 143,
UnresolvedReason 66 and the common wrapped reason upper **6902 bytes**.
The latter retains the overbound for six f64s rather than relying on the
fixed-root exclusion. The complete variant table is in PARAMETERS.json.
`bounded(format!(...))` first allocates the whole reason, then its ≤240-char
copy; these allocations overlap. Its printed cap is not a bound on formatting.

The same file contains every literal/dynamic-key method occurrence from
H main.rs and w1.rs. It is a common **multiset superset** of each emitted
Line, not a claim every occurrence is on one line. Dynamic occurrences get
19 copies (the largest loop appending to one line is the 19-stage list;
precision, mode and work loops are smaller). Each dynamic placeholder has
20 ASCII bytes, covering the actual precision/mode/stage names. Keys are
ASCII identifiers; values have method-specific bounds: integer 39, bool 5,
null 4, quoted hex 18, f64 ≤1137, strings by the finite literal/model/reason
grammar. Counting source occurrences rather than deduplicating keys preserves
repeated insertions in the String representation.

For the pinned sources this gives a common Line payload upper **907,668 B**,
requested move upper **2,723,004 B**, and **27,132 B** for overlapping full/
bounded reason, dynamic key, numeric and control-character-format helpers.
The bound is intentionally broad but comes from the source grammar; it is
not a chosen safety constant or an observed peak. Each individual Line is
covered by that same envelope. Core scalar formatting uses inline scratch;
the heap belongs to these Strings. Field rows retain exact source lines.

Thus `H_emit = 1024 + 2,723,004 + 27,132`, before the already-owned model,
counts, current outcome, saved attempts and prefix controls. The 1024 bytes
are the pinned stdout LineWriter buffer. Only one Line owns its String at
a time. `work_by_precision` contributes at most G(4,PrecisionWork) while
the outcome line grows; gate formatting and helper Vec<(u64,u64)> of length
≤2 are added by `H_control = G(4,PrecisionWork)+E(2,(u64,u64))`.
The parent packet already covers saved/current attempt and prefix Vecs;
they are not multiplied by the number of repeats.

The row dump is streamed through an 8192-byte BufWriter. At each row, bound
bits String≤16, key≤18 (`end.<u32>.<i|j>.<component>` is the longest), and
value token≤16 coexist. A safe separate phase is
`H_dump = 1024+8192+MText(16)+MText(18)+MText(16)`.
Publication size q does not multiply that row-format scratch. Debug and
canonical FNV digests also stream; no full publication/evidence Debug String
is charged. See H/k6/mod.rs, canonical.rs, w1/rows.rs and main/w1 output paths.

### Argv, paths and file reads

L/std/src/sys/args/unix.rs:21–61 creates E(argc,OsString) and exact byte
copies of each argument, then common.rs wraps that Vec's IntoIter. Parsing
moves flag/value Strings; it does not clone the entire argv. Therefore
`ArgvPeak = E(argc,OsString)+sum_i len(argv_i)` covers the parser's ordinary
argument-owned heap. Retained Args fields use their actual subset of those
strings after the iterator drops. Add any explicit case/id clone (VR adds
one) separately. Valid prepared argv are UTF-8 and preserve the original
flags/backstops; invalid input is not a route to bypass the estimate.

`OpenPath(p)=0` for byte length p<384, otherwise p+1 requested bytes.
The pinned small_c_string helper uses stack storage below 384; its allocating
CString<&[u8]> specialization reserves exactly len+1. A path constructed by
crate_dir/cases_dir/join has its separately named PathBuf allocation(s), each
bounded by Text(final length). Sum the few source construction identities
until their call returns; do not treat a borrowed path as another clone.

L/std/src/fs.rs:383–390 reserves exactly the metadata length before reading.
For a stable sealed file of F bytes with metadata F, `Read(F)=F`: io/mod.rs
probes EOF in a 32-byte stack buffer before doubling an exact-fit Vec. This
is the normal exact-file branch, requiring that byte/metadata binding.
For a supplied different/unknown hint H (use0 when unknown), the safe
fallback is `Read(F,H)=max(H,64,2F+64)` retained bytes and at most
`ReadMove(F,H)=3*max(H,F+32,32)`. The constants come from the 32-byte probe
and RawVec growth, including an extra reserve at a full-buffer EOF; no
provider run is needed to state the formula. Hash/metadata drift refuses
use of the exact branch, not silently treating an unknown reading as F.

On Unix I/O error formatting, the source strerror buffer is 128 stack bytes;
at most 127 bytes are returned. UTF-8-lossy replacement gives at most 381
bytes of description, with `MText(381)` as its heap envelope. Appending the
signed errno and source literal wrappers is bounded with the same Text
operator. Invalid UTF-8/NUL and reserve errors use the source's constant
error forms. A serde WriterFormatter failure can additionally allocate
`Box<io::error::Custom> + Box<StringError> + 9` for "fmt error"; these
private standard-library layouts remain named witness cells. This closes
the error-path sum without an unbounded OS-error-string assumption.

For H's valid canonical model-file path, the parse result's persistent
heap is `M_H`: exact-reserved node/member/load arrays, pushed restraints,
and exact cloned label/id/source strings (all bounded by the input's byte
descriptor). The counts/section token Vecs have P(6,String), P(12,String);
their payloads total≤F. A current line has at most 8 borrowed tokens. The
final canonical comparison allocates one streamed-to-String serialization
of length F plus at most six 16-byte hex temporaries. Hence:

```
H_model_file = ArgsRetained + PathOwned + OpenPath(p)
             + Read(F) + M_H
             + G(6,String)+G(12,String)+F+G(8,&str)
             + max(MText(20), F+MText(F+18), MText(F)+6*MText(16))
```

The first branch covers the eagerly formatted missing-key message. The
second covers a `take` line clone overlapping its eagerly evaluated
`ok_or(format!("expected {key}: {line}"))`: key length is at most 7 and the
wrapper is 11 bytes. The last branch covers serialization. These error
arguments are evaluated even when the Option is Some. Their full sum is also safe if a reviewer elects a
simpler envelope. Bounds use the **sealed canonical bytes**, not arbitrary
malformed input pretending to be a fixture. Earlier model-generation/source
phases from the parent still apply to `--model` rather than `--model-file`.

The counts-file path holds its read String while parsing one line at a time;
no Vec of all parsed records is collected. `json_integer` holds a formatted
search pattern plus digit String; produced u128 fields have≤39 digits.
`parse_counts_line` clones only the model id into its tuple. A closed phase is
`H_counts_file = ModelAndFrames + ArgsRetained + Read(Fc)+OpenPath(pc)
 + id_len + MText(Kmax+4)+MText(39)+H_emit`.
Kmax is the longest literal parser key (source-derived; or use the recorded
key upper from PARAMETERS). Counts bytes/hash and model digest remain
bound to the candidate/RV22-3 contract. The read String and id tuple are
dropped before entering the solve.

The full completed H binary addition is the maximum of ArgvPeak,
H_model_file (or the parent's generator phase), H_counts_file (or parent
counts-construction phase), `OwnedDuringCall+H_emit+H_control`,
`OwnedDuringDump+H_dump`, prefix emission and their named I/O error prefixes,
all plus B0. No dynamic formatting/input-I/O composition is left unnamed.

## S-VR-parse-envelope: closed typed/tree compositions

Define `JP(v)` for an input JSON Value tree: each array contributes
G(length,Value); each object contributes TI(key_count,String,Value);
add all key/decoded string bytes and recurse into children. The source
Value visitor starts an empty Vec and pushes (J/value/de.rs:107–117).
Use `JC(v)` for a deep clone/to_value tree: known arrays use E(length,Value),
strings exact length, maps their copied topology or the TI upper. Object
keys in the sealed canonical inputs are unique. Let `Jpeak(v)=JP(v)
 + max_array(0.5G(length,Value)) + MA(longest_decoded_string,u8)`.
The extra array term covers the one active array reallocation. The scratch
Vec uses bulk extend as well as push and is cleared/reused, so its upper is
MA rather than a fresh push-only G; a non-power-of-two reserve is retained
across strings. Fixed-number fields are bounded
integer tokens in these files, not arbitrary-precision Number strings.
The compact histograms in PARAMETERS determine JP and this upper directly.

For a typed parsed model define:

```
M(v) = G(N,String)+G(N,[f64;3])+E(m,Member)+E(sp,SpringSpec)
     + E(om,String)+E(r,(u32,usize))+E(l,(u32,usize,f64,String))
     + E(t,(u32,u32,f64))
     + node-name + member-name + spring-key + omitted-key + load-source bytes
Mpeak(v) = M(v)+max(0.5G(N,String),0.5G(N,[f64;3]))
```

`parse_model` pushes the first two arrays; all other arrays map borrowed
JSON arrays and collect with exact length. Its strings clone exact payload.
`Mclone` replaces all G arrays with E and retains the same string payload;
cloning nested strings is explicit.

For a String→String map m let `SM(m)=TB(k,String,String)+sum(key/value bytes)`
and `SMwork(m)=max(E(k,(String,String))+Sort(k,(String,String)),
 E(k,(String,String))+TB(k,String,String))`. The input Vec slots persist
through bulk construction; moved String payload is already in SM and is
not cloned again. SMwork is an explicit conservative control-buffer upper
on top of the completed map bytes; it can overcount completed nodes while
the map is partial, which is safe and disclosed.

Typed Case heap is:

```
C(v) = bytes(id,family,basis,units,k4src_sha256,optional model_sha256)
     + E(R,Row) + sum row key/expected/class/optional scale bytes
     + E(C,Control) + sum control-id bytes
     + sum value-control SM(m) or outcome-defect String bytes
     + SM(scales) + optional SM(s_full)
     + E(not_covered_count,String)+sum not_covered-key bytes
     + optional M(model)
Cpeak(v) = C(v)+max(all SMwork in this case,
                   optional [Mpeak(model)-M(model)],0)
```

These are all owned Case fields at cases.rs:223–280. Struct/header layouts
are σ parameters; source keys/fields are explicit, not an opaque "case cost".
The parent raw Value tree remains while Cpeak is built. Output model field
Some/None is determined by the committed case, not guessed from size alone.

For family lines v_i and file F_family, `load_file` builds the case Vec by
filtering lines: capacity P(k,Case). One parsed Value tree exists at a time.
A complete upper is:

```
VR_family_load = ArgsRetained + PathOwned + OpenPath(pathlen)
               + Read(F_family) + sum_i C(v_i)
               + max(MG(k,Case),
                     G(k,Case)+max_i[Jpeak(v_i)+Cpeak(v_i)-C(v_i)])
```

This substitutes the full final case payload for the partial prefix/current
payload. It does not duplicate C(current). `find` consumes the returned case
Vec; until its iterator drops, the same family envelope covers the old backing
and remaining cases. After that statement, only the selected C(v_j) remains.

The small/embedded branch then adds Mclone(model) while C(v_j) still owns
the original Model. The large branch calls `load_large_model`: raw text,
raw Value and parsed model coexist. Its tuple evaluates parse_model first,
then sha256_hex, so the parsed model also overlaps hash scratch. Let Q(F)
be64*ceil((F+9)/64). Hash's Vec starts with an exact F-byte clone, appends1,
zero pads and appends8; apply R to that exact sequence for Hcap(F), Hmove(F).
Its eight temporary 8-digit strings concatenate into 64 bytes while the
message Vec still exists, giving
`Hash(F)=max(Hmove(F),Hcap(F)+104)`;104=32+64+8 at the last hex-output grow.

```
VR_large_load = ArgsRetained + C(v_j) + cloned_case_id + PathOwned
              + OpenPath(p)+Read(F_model)+Jpeak(model_shape)+Mpeak(model_shape)
              + Hash(F_model)+64
```

The final64 is the returned digest, conservatively retained alongside
construction scratch. Overcounting Jpeak/Mpeak and Hash as a simultaneous
envelope is explicit; no phase omission is hidden. Small models use C+Mclone.
Hash comparisons require the existing expected SHA; no missing file is
silently admitted or reconstructed here.

The twelve missing large shapes can be supplied from the eventual sealed
input bytes, or bounded now from the RF generator schema: root object 7 keys
(58 key bytes), outer arrays N,m,r,l,t and two empty arrays; N inner arrays 4,
m arrays 13, r arrays 2, l arrays 4, t arrays 3. String payload is node/member
label totals +48N+144m+16l+source-id bytes+16t. These are symbolic expressions
of already-bound fixture cardinalities; scalar hexadecimal values always
have 16 bytes and need not be computed. Thus absence of the raw files leaves
F/hash-byte verification pending, not the tree composition.

`expected_unresolved()` additionally performs its once-only file read and
Value parse while the lane outcome may be live. Add
`Read(Fu)+Jpeak(vu)+E(u,String)+sum selected case-name bytes+PathOwned` at
initialization; thereafter retain only the last two terms' String Vec/payload
as the OnceLock owner. PARAMETERS supplies this file's shape and F. It must
not disappear from the fixed binary term merely because initialization is
usually early. Streamed emit, record cloning and comparison phases remain
as closed in the parent packet.

## S-VR-binary64-tail: closed sparse phase maximum

The caller drops `run` before the tail but retains `record`, case, model,
Args, counts/ids and OnceLock data. Let this fixed union be T0; include
JC(record), not the dead kernel caches. Tail is
`T0 + max(RCM_tail, Binary64_tail, emit_tail, named_error_prefixes)`.

### RCM tail

For free row a let d_a be its structural free-neighbor count. free_adjacency
allocates n bools, n usize positions, E(f,BTreeSet<usize>), and one insertion
tree per row. Per-member temporary DOFs contain 12 usize; use A(12,usize).
Conversion to Vec rows overlaps the old set backing/nodes with new row
vectors; a conservative upper is:

```
Adj = n + E(n,usize) + E(f,SetHeader) + sum_a TI(d_a,usize,())
    + max(A(12,usize), E(f,VecHeader)+sum_a A(d_a,usize))
AdjResult = E(f,VecHeader)+sum_a A(d_a,usize)
```

This also covers any in-place reuse of the outer owned map; no new buffer
is required in that branch, but the sum safely permits both until layouts
select it. Both orderers symmetrize again, retaining neighbor capacity for
2d_a before dedup. Their common base is
`E(f,VecHeader)+sum_a A(2d_a,usize)+E(f,usize) degrees+f visited+E(f,usize) order`.
Add the max of one row's stable-sort scratch, reachable/queue BFS and later
queue. K4's BFS uses the parent's four-frontier bound. SD's BFS additionally
clones next_level into last_level; a sufficient helper bound is
`3MA(f,usize)+3E(f,usize)+f`, naming component/current/next growing arrays,
saved caller last-level, old inner last-level and new clone, plus marked.
That extra clone is not assumed identical to K4's implementation.

`RCM_tail=max(Adj,AdjResult+RCM_K4,AdjResult+E(f,usize)+RCM_SD,
AdjResult+2E(f,usize))`. K4's returned order stays live during SD. The caller
explicitly drops adjacency and both orders before binary64 parity.

### Sparse binary64 parity

This call is `parity(model,false)`. The early return at parity.rs:244–246
precedes dense assembly/roundoff matrices and dense solve. None is included
as an executed allocation. Users/blocks/springs are empty for named RF;
options are unscaled; force binding is Legacy; formation source and audit
load terms are absent. Consequently D-5 formation-check and typed load-fidelity
branches do not allocate here. Existing criteria/refusals remain unchanged.

Let c=144m, z be global stored pattern entries, zf the stored free block,
s64 the numerical-zero RCM skyline length. All are integer storage counts;
s64 is **not silently equated** to K4's structural skyline. Without a tighter
count witness, substitute the source bound s64≤f(f+1)/2 arithmetically; do
not materialize that matrix. Let t_e be contributions to global entry e,
sum_e t_e=c, and trow=max_i sum_(entry in row i) t_e. For RF, t_e≤node degree
and trow≤12*dmax. These use the parent connectivity multiplicities.

Define Expansion vector envelope
`X(k)=G(k,f64)`, `Xadd(k)=X(k)+MG(k,f64)`; each add can grow its newly built
next Vec while old terms remain. An expansion of k accumulated scalar terms
has≤k terms. Products add at most 2 terms.

The following named blocks enumerate all reachable allocations. Layout
variables are exact real types, never borrowed wrapper sizes.

| Block | Requested live envelope / constituents | Source |
|---|---|---|
| B64 model | A(N,FrameNode) temporary; A(m,FrameElement) fallible frames; E(n,f64) force; E(r,usize) restrained; G(f,usize) free; E(r,(usize,f64)) prescribed plus its sort scratch. Result keeps frames/force/free/prescribed; temporary nodes/restrained drop | VR/parity.rs:39–99 |
| Contributions | MG(c,StiffnessContribution) while building; G(c,StiffnessContribution) kept | parity.rs:104–129 |
| Allowances | two insertion maps with≤z `(usize,usize)→(f64,usize)` entries; out persists, magnitude is consumed. Element transform/local/global Matrix12 and roundoff matrices are inline arrays, no per-member heap | parity.rs:135–169; FK/structural.rs:2116 |
| Sparse assembly | E(m,(usize,usize,Matrix12)) formed; E(m,(usize,usize)) connectivity; node-neighbor headers and sum_v A(2d_v,usize); n bool spring flags; E(n,VecHeader) expanded rows with row capacities from actual grouped reserve (safe A); E(n+1,usize) starts, A(z,usize) columns, E(z,usize) transpose; E(z,f64) values. Temporary formed/connectivity/neighbor/row buffers drop on return | FK/structural/sparse.rs:85–160,592–696 |
| Sparse caller | roundoff G(z,f64), operation-count G(z,usize), prescribed-position E(n,usize), plus persistent model/contributions/allowance map/SparseStiffness | parity.rs:214–234; sparse.rs:889–915 |
| Preparation core | E(f,i32) exponents, E(n,usize) free positions, E(f+1,usize) starts; MG(zf,usize) columns/source entries, MG(zf,f64) values during their growth; E(f,usize) diagonal, E(f,f64) RHS, E(zf,usize) transpose; one row's filtered entry/coupling tuples bounded by A(global row length,T), unstable sort; n-bool validation scratch and optional n-f64 negative direction; cloned symmetry-basis String | sparse.rs:1031–1100,1299–1478 |
| Contribution audit | `Sums=E(z,Expansion)+sum_e X(t_e)` and its active-add max; `Differences=E(z,Expansion)+sum_e X(t_e+1)` and its add max; rounding vector MG(z,ContributionRounding) plus cloned children `8*sum_e(2t_e+1)`. Sums/differences/rounding overlap; zero prescribed values mean no delta-product expansion terms, but coupling-index Vecs still exist | sparse.rs:1184–1214,1521–1616 |
| Ordering | A(lower_entries,SymmetricMatrixEntry), sparse adjacency headers/inner usize buffers; SD RCM above; profile helper ordered_position/first/original_indices E(f,usize), E(f+1,usize) row starts and MA(s64,f64) values. Helpers and temporary profile values drop before actual factor | SD/structural.rs:56–76; SD/lib.rs:215–282 |
| Positive factor | E(f,VecHeader)+8s64 row payload; order and first clones E(f,usize), f seen, E(f,usize) position; caller ordering.order and first_columns each stay borrowed/alive; factor loop another first clone, E(f,f64) work and MG(f,PivotEvidence). Factor result keeps rows/order/first/pivots; no second full factor/profile clone | sparse.rs:1740–1792; FK/structural.rs:1973–2027 |
| Condition | cloned pivots E(f,PivotEvidence) passed to finish; at most five f-f64 buffers from x/y/signs and inner solve x/result; validation n-bool scratch. The five Hager iterations are sequential | sparse.rs:1797–1809; structural.rs:1562–1647,2029–2054 |
| Refinement | y E(f,f64), u E(n,f64), MG(f,ResidualRow); correction MG(f,f64) and solve x/result 2E(f,f64); at most three correction iterations, no accumulation across them | structural.rs:1667–1804 |
| Intended-action audit | fresh Sums as above; residual rows already held; new MG(f,ResidualRow); one `Xadd(1+2trow)` residual expansion. Both reports persist on success; fresh sums drop before return | structural.rs:917–990 |
| Success report | u; original and intended row buffers; moved cloned pivots; E(f,i32) scale clone; exact-length ContributionRounding outer clone and exact child term clones; symmetry-basis clone. These coexist with prepared/factor until finish returns; return of solve_sparse_prepared drops prepared/factor | structural.rs:1749–1784 |
| Refused factor/witness | prepared persists; failed partial factor buffers unwind; direction E(f,f64) plus mapped E(n,f64) on a witnessed pair; the search itself is scalar/O(nnz). Error classification formats finite static labels, not the direction Vec | sparse.rs:1937–1979; VR/parity.rs:173–186 |

Use a phase max, not a sum over every row: `B64_model_build`; then persistent
model + contributions-build; persistent model/contributions + allowances;
persistent model/contributions/allowances + sparse-assembly; then caller fixed
block plus the max of preparation/audit, ordering, factor, condition, refinement,
intended audit, success-copy and witness phases. Each helper retains the named
prior blocks and releases the indicated scratch at return. It is permissible
to substitute a complete persistent block while partially constructing it;
that only increases its explicit envelope. A dynamic Vec contributes its
old buffer only in its own grow phase, or via the disclosed MG upper.

For a concise closed sum, define `B=kept B64 model + contributions + allowance
out + SparseStiffness + round/count arrays + prescribed-position`,
`P=prepared core + kept rounding payload`, and `F=factor rows/order/first/pivots`.
Let each block's suffix `*` mean the construction upper given in the table.
Then:

```
Binary64_tail = max(
 B64_model_build*, kept_model+Contributions*,
 kept_model+contributions+Allowances*,
 kept_model+contributions+allowance_out+SparseAssembly*,
 B+PreparationCore*+ContributionAudit*,
 B+P+Ordering*, B+P+Factor*,
 B+P+F+max(Condition*, Refinement*, IntendedAudit*, SuccessReport*),
 B+P+Witness*, B+max(SuccessReport*,8n)+class_or_error_text
)
```

Every starred symbol is expanded in the table, including retained predecessor
arrays where stated. For independent arithmetic implementation, FORMULAS.json
lists their expression dependencies; none means an unreviewed external routine.
No phase contains a dense n×n allocation. A large symbolic skyline upper is
an admission-estimate consequence, not permission to run it. This closes the
third source-composition cell while keeping actual storage/layout/input values,
independent checking and the final A1-dependent E_max decision separate.

The binary64 return-to-classification phase retains the returned solution or
error direction while the class String is formed; the final max therefore
adds `max(SuccessReport*,8n)` beside class text. Likewise actual factorization
retains the caller's two ordering vectors while borrowing them. These owners
are explicit in FORMULAS.json rather than being covered by presumed slack.
