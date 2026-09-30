# A0 direct compile trial grant

ROOT accepts A0's sealed preparation and authored-lock addendum at coordination
`888e388812f65dffce4428c96c18d2ddc8d2ae61`. The numerical library remains the
unaltered 36-file snapshot from `3bddc2b05f6106e969c7cf43373b230845c7cc66`.
No A1 proof closure, realized solver result or product repair is accepted.

Independent backcheck closes GR-01/02 on `tools/host_guard_v2.py`, SHA256
`533a6f7506da4e031d8a824a27b4e9c496f374a3af8b7e98c72da55e8bbc26b5`.
The reviewer checked all live qualification files and confirms those control
observations carry to unchanged v2 control code for a separately budgeted tiny
direct-compile trial. GR-03's qualification-controller replay cleanup is fixed
and independently backchecked in v3; it does not affect this compile path.
Final incremental PR review is still in progress. GEN-8 passed on the staged
888e3888 candidate (1 passed, 10 deselected, 34.11 s); clean integration-base
GEN-8 also passed. Compile execution does not authorize a PR merge.

DESIGN may resume its original A1-DIAGNOSIS TASK for **one direct cargo build**,
using the shared isolated runtime and reviewed v2 guard. This grants the one
global heavy slot to that command only; other TASK work stays lightweight.
The TASK writes new evidence only in `instances/A1-DIAGNOSIS/continuation_02/**`,
its existing scratch and reserved target. Cargo may make normal tool-managed
writes in the isolated CARGO_HOME, never the owner's default toolchain/config.
Preserve all sealed preparation bytes and source snapshot bytes.

- Direct pinned native cargo/rustc paths and hashes from the lock addendum.
- Exact argv: cargo build --offline --locked --manifest-path <A1_SCRATCH>/Cargo.toml
  --bin a1_public_probe --no-default-features -j 1.
- Guard job kind compile, inherited-group; candidate full SHA 888e3888 above;
  unique job identity, explicit executable/source/manifest/lock hashes.
- Both group RSS and footprint caps: 2 GiB; allowance: 128 MiB; timeout: 300 s;
  disk-write budget: 1 GiB; disk reserve: 4 GiB. These are diagnostic operating
  limits, not a proven allocation bound or final W1 limits.
- Guard's three fresh quiet preflight samples and projected availability above
  40% remain mandatory. Preserve its pressure/swap/identity/heartbeat checks,
  observed cap overshoot allowance and ACTIVE latch behavior. No prior sample
  is current admission. One job, no parallel model or compiler.
- RUSTUP_TOOLCHAIN=1.97.1, RUSTUP_AUTO_INSTALL=0, CARGO_BUILD_JOBS=1,
  RUST_TEST_THREADS=1, CARGO_INCREMENTAL=0, CARGO_NET_OFFLINE=true; direct RUSTC
  and isolated target/home bindings. Use a small explicit outer environment
  preserving HOME/CODEX_HOME if present, with no seeded-fault controls, wrappers,
  RUSTFLAGS/CARGO_ENCODED_RUSTFLAGS or inherited Cargo target/config overrides.
  Inspect applicable ancestor/isolated Cargo configuration before invocation.
  No cfg(test), mutation feature, dependency fetch/install or network.

The authored two-package lock is validated by this offline locked build. Check
the exact input/snapshot/tool hashes before and after; preserve raw logs, guard
job/registry/events, exit reason, timings, sampled RSS/footprint, resulting
binary/lock hashes and sanitized copies. A compiler refusal or guard stop is a
named result, not a success. Do not erase a latch or blindly retry. No source
or probe repair is granted by this compile trial; return any needed adjustment.

No numerical case runs in this grant. Return the build/operability checkpoint
to DESIGN/ROOT first. ROOT will then decide the B01–B16 grant from the actual
compile evidence; C17–C24 still require the separate extension checkpoint.
