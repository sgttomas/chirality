# ROOT runtime-preparation addendum — 2026-09-30

ROOT reported that the guard's admitted environment pins
`RUSTUP_TOOLCHAIN=1.97.1` exactly. Use that value while retaining the isolated
host-specific direct cargo/rustc binary paths and their hashes. The previously
proposed host-suffixed environment value is superseded for this future run.
This changes no installed owner configuration or toolchain.

ROOT also reported that `cargo generate-lockfile` does not meet the guard's
offline/locked/-j1 compile command grammar. No unguarded Cargo invocation is
permitted to work around that boundary.

DESIGN inspected FK's frozen `Cargo.lock` and the inert probe's `Cargo.toml`.
FK's lockfile is version 4 with one dependency-free package,
`open_pipe_stress_frame_kernel` 0.1.0. The probe is `a1_public_probe` 0.1.0
with FK as its sole path dependency. DESIGN reported that a two-package
version-4 lockfile can be authored as a bounded recreated input, with its
true provenance and without registry source/checksum fields.

ROOT then explicitly granted this preparation adjustment through native
collaboration:

> ROOT grants the authored two-package version4 Cargo.lock preparation adjustment just described. Add it under the A0 owned evidence/scratch scopes as a recreated input with explicit provenance, no Cargo-generated claim; offline --locked build remains the validator. Preserve any already-sealed preparation packet and put the adjustment in continuation if necessary. Record exact env pin1.97.1 and direct compiler binary hashes. No compilation/model execution yet; guard v2 review/live qualification still finishing.

DESIGN forwarded that grant to the existing child
`/root/design_manager/a1_diagnosis`; no new child was launched. The exact
lockfile, provenance, scratch-copy hashes and command-plan consequence belong
to the child's preparation return. The later guarded `cargo build --offline
--locked ... -j 1` must validate the authored lockfile. Neither preparation
nor this addendum claims that Cargo generated or validated it.

All other preparation restrictions, B-first/C-extension sequencing and source
identities remain unchanged. This is not a build, model-run or heavy-slot grant.
