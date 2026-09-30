# K0-L1 — concrete private-layout compile proposal

**Prepared for ROOT selection; not applied, compiled or executed.** This is a
separate assignment from K0-S1/S2. It becomes executable only after guard GR-01/
GR-02 additive repair, independent backcheck, relevant controlled qualification,
fresh headroom and ROOT's command-specific compile grant. V1's pure test pass
or read-only provider witness does not admit this compile.

## Smallest private source change

Copy the exact dependency-free frame_kernel library into a new response-owned
private archive. Append `K0_L1_LAYOUT_OVERLAY.rs.txt` to **one file only**:
`src/structural/retained/adaptive.rs`. The reviewable unified patch is
`K0_L1_LAYOUT_PATCH.diff`; preimage/postimage/overlay hashes and every row's
real Rust type are in `K0_L1_LAYOUT_MANIFEST.json`.

The single child module is gated by a dedicated `k0_layout_witness` cfg, not
cfg(test) or mutation-controls. It adds no canonical export/visibility change,
solver call, test harness, build script, executable main or global allocator.
Canonical FK and ROOT's original A1 source snapshot remain read-only. Only the
new disposable copy receives the append, after exact preimage validation.
No lookalike Wide, Option, FK control or BTree node structure is used.

The table contains 126 actual type rows: widths 4/8/16 and real Wide/Option,
factor/bound/refusal/report/control/summary/case/cache/source structures, actual
inline tracker/ledger/evidence tuples and collection headers. Each emits size,
alignment and Layout::array request size/alignment at capacities 0,1,3,17,512,
4096. These are const evaluations; no array buffer is created. Fifteen actual
Arc payload types additionally emit a **source-derived** Arc request layout,
using real AtomicUsize layout and the pinned repr(C) ArcInner formula. That is
explicitly not direct sizing of a mirrored ArcInner.

Four uncalled functions force ordinary library monomorphization for the actual
geometry map, tracker map, holding set and VR publication map key/value types.
Their safe bodies insert a supplied value/key into a supplied collection and
return it; they call no solver. Their purpose is to expose actual private
LeafNode/InternalNode debug sizes and allocation call constants in emitted IR.
No executable or test invokes them. No stdlib source is patched or rebuilt.
If the compiler omits or ambiguously names a needed node/layout, record that
cell as unverified; do not replace it with an assumed mirror value. Additional
consumer JSON types are outside this dependency-free FK witness and need their
separate pinned source/layout closure.

## Source and write scope for a later sealed assignment

- Product/FK source: `3bddc2b05f6106e969c7cf43373b230845c7cc66`; latest checked
  coordination HEAD: `fe6ca966259d29d8d6ed2f05460400f6cb5d5de0`.
- Exact compiler/runtime: isolated native Rust 1.97.1, aarch64-apple-darwin,
  default features, no mutation feature. Pin rust-src through
  `Run/runtime_setup/02_rust_src/SETUP.json` and actual library source hashes.
- ROOT prepares `<RESPONSE_RUNTIME>/scratch/k0-layout/<source-sha>/fk` via
  read-only Git/archive provenance. The TASK never changes Git/index or the
  original A1 snapshot. Compare the complete library-file set to source before
  appending; verify Cargo.toml still has no dependencies/build script.
- Archive-only write: that new adaptive.rs append; owned output under
  `<RESPONSE_RUNTIME>/targets/k0-layout/<source-sha>/`; raw logs/IR under its
  own job directory; portable records only
  `Run/instances/I21-K6C/layout_01/**`. ROOT must grant this exact set.
- Read scope: Root/project/TASK instructions; accepted source-only packet;
  exact source and rust-src relevant types/layout allocation paths; repaired
  guard contract/review/qualification and isolated runtime binding.

## Proposed command, not executed

Use the repaired and command-qualified guard with an explicit job record,
executable/source/overlay/lock/compiler hashes and a single owned target.
No `+toolchain` selector. Cargo controls are **before** the forwarding separator:

```text
<isolated-cargo> rustc --manifest-path <private-fk>/Cargo.toml --lib   --target aarch64-apple-darwin --offline --locked -j 1 --   --cfg k0_layout_witness --check-cfg 'cfg(k0_layout_witness)'   --emit=llvm-ir -C opt-level=0 -C codegen-units=1 -C debuginfo=2
```

Environment: isolated RUSTUP_HOME/CARGO_HOME, RUSTUP_TOOLCHAIN=1.97.1,
RUSTUP_AUTO_INSTALL=0, CARGO_INCREMENTAL=0, CARGO_BUILD_JOBS=1,
RUST_TEST_THREADS=1 and that assignment's CARGO_TARGET_DIR. Record exact
compiler verbose identity and artifact identities through ROOT's setup/grant.
Do not inherit contradictory RUSTFLAGS/Cargo config silently. A grammar refusal
returns to ROOT, not to an argument bypass. Never use cargo test, cargo run,
--tests, --all-targets or a test/mutation feature for this witness.

A conservative initial compile proposal is a 1-GiB group cap, 256-MiB allowance,
180-second maximum and an explicitly allocated disk/log budget; these are
unmeasured operating proposals, not a grant. ROOT chooses final values after
qualification/headroom. Compilation has no binary heap backstop and must stay
under the qualified group monitor. No automatic retry/escalation on refusal.

## Required output and checks

1. Source-file manifest before append, exact one-file diff, overlay/preimage/
   postimage hashes, Cargo manifest/lock/features, compiler/rust-src/guard/grant
   identities and full command/env. No stale same-named probe artifact.
2. Compile exit, warnings and complete IR hash/size. Only library/IR artifacts;
   no emitted probe binary is executed. Compile-only does not mean the compiler
   itself uses no memory; preserve its guard and resource evidence.
3. Decode `K0_LAYOUT_ABI` and `K0_LAYOUT_ROWS` from the new IR. Require native
   pointer size/alignment/endian to match the recorded target, all 126 IDs exactly
   once, sane power-of-two alignments and array sizes equal capacity×type size.
   A decode/const-evaluation/visibility failure is outstanding evidence, not zero.
4. Decode all 15 `K0_ARC_DERIVED` rows and independently reproduce source-derived
   extend/pad arithmetic. Label them derived allocator layouts. Size of Arc<T>
   itself is only a pointer/container fact.
5. Locate actual LeafNode/InternalNode debug metadata and corresponding boxed
   allocation size/alignment constants for all four forced map/set generic
   shapes. Preserve exact IR loci and extracted type names; a missing cell
   remains open. BTreeMap/Set header size does not substitute for node allocation.
6. Crosswalk each result to K0-S1/S2's exact layout variable and the historical
   formula assumption. Report mismatches instead of weakening an asserted
   coefficient. Independent reviewer checks extraction and mapping before the
   complete phase formula is accepted.

No Vec push/filter/sort/VecDeque/BTree operation is executed. Growth/reallocation
contracts come from the pinned sources and source-path derivation; compile-only
output cannot establish observed high-water memory or OS RSS/footprint. No
solver result, final E_max, W1 limit, final A1 compatibility or engineering
acceptance follows. Any future runtime allocation microprobe would require a
separate narrowly scoped grant; it is not hidden inside this witness.
