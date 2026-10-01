# Performed source/record checks

This is a method and verification record, not a reconstructed full terminal
transcript. Actual host calls contain the individual reads/outputs. Source
origins and hashes are in SOURCE_INPUTS.json; native resume/parentage and
grant limits are in CONTEXT.json.

1. Derived repository root with read-only `git rev-parse`. Compared accepted
   brief bytes to commit 888e388812f65dffce4428c96c18d2ddc8d2ae61 and its
   supplied SHA256. Checked unchanged Root/project/TASK instruction hashes.
2. Read the accepted brief, manager SOURCE_CLOSURE/RUST_SRC_INPUTS, ROOT's
   rust-src SETUP and runtime binding, original K0 packet and the proposed
   L1 manifest/prose. No L1 overlay was materialized or applied.
3. Verified all 17 manager-supplied Rust library hashes. Read actual collection,
   tree, formatting and I/O branches from that pinned installation. Used
   `rg`/bounded reads for repository source; no online or other-version fallback.
4. Located exact locked dependency sources in the owner's existing Cargo cache.
   The isolated Cargo source cache lacked those five packages. No install or
   fetch followed. `.cargo-checksum.json` was absent; each .crate SHA256 matched
   Cargo.lock, and all 180 member files compared byte-for-byte through Python
   tarfile reads, without extracting/writing archives.
5. Source discovery guessed missing btree/insert.rs and btree/bulk.rs paths;
   directory/symbol inspection resolved node.rs and append.rs. A guessed
   core flt2dec path was absent; the actual core/fmt/float.rs supplied the
   formatter scratch evidence. These misses are not missing-source findings.
6. Standard-library record arithmetic checked all 33 H cardinality/payload/
   source-ID identities and graph multiplicities, plus 24 VR RF identities
   and 18 original scale-count lengths. Existing canonical files were hashed;
   no generator or Rust model was imported/constructed/executed. Integer
   connectivity metadata contains no physics arrays or dense matrix.
7. The comparison-bound draft initially scanned every numeric-looking string,
   including hex model fields. Its unreasonable exponent bound exposed the
   wrong field set. The sealed script selects only actual reference/control/
   scale decimal fields. This corrected unsealed record arithmetic, not a
   numerical oracle, source file, protected criterion or historical output.
8. A pure integer model of append.rs's right-spine occupancy matched the
   derived bulk node formula for K=1…10,000. It allocated no Rust collection,
   ran no allocator probe and measured no heap. The result is source-contract
   arithmetic, not runtime evidence.
9. Final `git diff --name-only 3bddc2b05f6106e969c7cf43373b230845c7cc66 -- <FK> <H> <VR>`
   returned empty. All 13 original K0 manifest entries verified. Later ROOT
   coordination 84843dbf9b74c4c3fdb727610998910b740a48ea is recorded separately.

Reproduce the new parameter arithmetic from REPO_ROOT:

```
RUSTUP_AUTO_INSTALL=0 PYTHONDONTWRITEBYTECODE=1 python3 <Run>/instances/I21-K6C/continuation_01/check_source_parameters.py
```

Run means the response AgentRuns directory in RETURN. The script prints JSON;
it validates SOURCE_INPUTS hashes first and writes no files itself. Redirect
to new owned scratch for comparison, preserving this sealed result. It records
its own SHA256 independently from the source basis and actual coordination
HEAD. A changed source rejects; a changed script is a new analysis, not a
historical rerun. Verify SHA256SUMS before relying on this script identity.
`<OWNER_CARGO_HOME>` here identifies the observed read-only home `.cargo`
cache directory, not a claim about current effective Cargo configuration.

No unchanged broad suite or historical admission replay was repeated.
No Rust invocation, provider, guard operation, process query/signal, network,
download, install, model run, source edit, index operation or delegation
occurred. Compiler/layout/runtime checks remain explicitly outstanding.
