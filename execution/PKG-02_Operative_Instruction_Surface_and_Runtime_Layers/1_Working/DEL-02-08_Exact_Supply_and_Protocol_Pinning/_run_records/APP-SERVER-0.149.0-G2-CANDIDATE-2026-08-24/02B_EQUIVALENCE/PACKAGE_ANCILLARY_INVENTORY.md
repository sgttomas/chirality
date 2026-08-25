# Package Ancillary Inventory and R14-B Hash Gate

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

The package archive contains five files: the equivalent app-server, three
ancillary executables, and one JSON metadata file. N2b inventoried them
statically and executed none.

| Member | Role | Bytes | SHA-256 | Static type | Mode | Cross-package result |
| --- | --- | ---: | --- | --- | --- | --- |
| `bin/codex-app-server` | required payload | `179721344` | `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` | Mach-O arm64 | executable | byte-identical to primary and zstd |
| `bin/codex-code-mode-host` | ancillary executable | `57150048` | `8f9f6969cd5e69540482d58791f72e4e9b9888e576ae3ad446c422a058b70128` | Mach-O arm64 | executable | package-only |
| `codex-path/rg` | ancillary executable | `4030432` | `b4a0ff402c26bf623ce5ddc8a806c65a29397ecca0d7210147b0f9224c70558c` | Mach-O arm64 | executable | package-only |
| `codex-resources/zsh/bin/zsh` | ancillary executable | `754208` | `4707e28b5f2fc75ce07c5fa3ff32d76a0fc43812c7880f9a98005dbc65a77e32` | Mach-O arm64 | executable | package-only |
| `codex-package.json` | layout metadata | `222` | `e29318e209d8d9d78c441c5f748365618ab4ebad82625f391e25eb67b4b50fac` | JSON | non-executable | package-only |

The metadata declares layout version `1`, version `0.149.0`, target
`aarch64-apple-darwin`, variant `codex-app-server`, entrypoint
`bin/codex-app-server`, resources directory `codex-resources`, and PATH
directory `codex-path`.

Static signature inspection found Team Identifier `2DC432GLL2`, hardened
runtime, strict modified-signature failure, and `spctl` failure on each Mach-O
member. The app-server and code-mode host report the invalid-entitlements
warning; `rg` and `zsh` expose no entitlements content. These observations
are inventory, not reliance. They reproduce the preserved prior-N2b results
and introduce no new disagreement.

Before any R14-B execution, N3 must independently verify the target file's
SHA-256 against `EXECUTABLE_HASH_FREEZE.json` and the network-deny profile.
R14-B permits only the evidence-producing executions it names; this inventory
does not itself authorize or require every ancillary member to run.

No `LICENSE`, `NOTICE`, or `COPYING` member is present. The exact-tag
Apache-2.0 license remains the N2 identity: `10926` bytes, SHA-256
`d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc`.
