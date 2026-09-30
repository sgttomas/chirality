# Authored-lock preparation addendum

The previously sealed 16-entry preparation packet is preserved unchanged.
ROOT subsequently granted, through DESIGN's native message, an explicitly
authored version-4 lockfile containing exactly `a1_public_probe 0.1.0` and
`open_pipe_stress_frame_kernel 0.1.0`, with the sole dependency edge.

`Cargo.lock` is that **authored recreated input**, not a Cargo-generated file.
It was copied byte-for-byte into the existing bound runtime scratch directory.
SHA256: `ca870fd55afca7aebeadd4410bb77a2a40391ac80a7ff95c36ab6b55fe66bc4d`. A pure `tomllib` check confirms the version, exact package
inventory and dependency edge. The later guarded offline `--locked` build must
validate Cargo compatibility; no Cargo command, compiler or model has run.

Environment pin: `RUSTUP_TOOLCHAIN=1.97.1` exactly. Host-specific direct compiler
and cargo paths/hashes are retained in this addendum's `CONTEXT.json`, from the
already verified installed files. This removes the need for the inadmissible
`generate-lockfile` step in the original plan; the planned offline locked build
remains subject to ROOT's separate guard/headroom/budget/heavy-slot grant.

Original manifest SHA256: `074e005899a76e8f26e2b2f021187a39331e2aca2d426856868f35467a8e5545`.
Original return SHA256: `f95dae59146122c0099f77f05125488db1c165abbabdf60da72ec898db47f93c`.
This addendum has its own `SHA256SUMS`; the original manifest covers the original
16 files and this manifest covers the three addendum files. All 24 cases remain
UNRUN. The B-first order, C extension checkpoint and every other hold remain.

Return to DESIGN and end preparation here.
