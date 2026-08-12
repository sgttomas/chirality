# D-APP-92 Reproduction Rebuild Card — 2026-08-11 (minder-prepared, owner-operated)

Purpose: rebuild the D-APP-92 sealed-replay helper/GUI from the frozen candidate
source so the owner can execute the approved D-APP-93 LLDB trace packet
(aggregate `db704c96…`). Basis: origin/main@43f89f96 (frontend baseline verified
byte-identical to the replay's D-APP-89 baseline; all 12 candidate hashes
verified against the replay's frozen SOURCE_MANIFEST.md).

Recorded deviations from the 2026-08-04 register (record in evidence form):
1. Rebuild occurs in scratch worktree /Users/ryan/dev/chirality-dapp93-build,
   not the original session paths.
2. Build uses the owner's normal shell (mise node 24.18.0); the register's
   `env -i …/opt/homebrew/bin npm` no longer resolves (no homebrew node).
   Actual node/npm versions recorded at build time.
3. Register row C037 (`@chirality/policy` projection) is stale: the package no
   longer exists in runtime/packages or the dependency tree. Projection updated
   to today's full @chirality symlink set, absolute into the main checkout.
4. Built .app binaries will not be hash-identical to the replay's C043
   identities (builds are not byte-reproducible); actual hashes recorded.
5. Fresh temp root /private/tmp/chirality-dapp93-trace-20260811.

Steps R1–R8 (rebuild), L1–L3 (launch), then the packet's operative trace
sequence; cleanup via `git worktree remove --force` + temp-root removal after
evidence freeze. Full commands and the 12-hash verification manifest are in the
session chat of 2026-08-11; candidate hashes equal SOURCE_MANIFEST.md values.
