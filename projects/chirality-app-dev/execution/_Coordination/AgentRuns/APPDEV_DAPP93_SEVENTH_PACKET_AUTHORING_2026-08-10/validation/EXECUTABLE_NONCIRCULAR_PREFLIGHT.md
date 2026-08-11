# Seventh-lineage executable non-circular preflight

Status: `PASS — ALL REQUIRED FORMS EXECUTED BEFORE N1`

Observed 2026-08-11T02:26:04Z. Native context telemetry unavailable.

| Tool | Actual absolute path | Bytes | SHA-256 |
|---|---|---:|---|
| cat | `/bin/cat` | 118800 | `c024d50a247255d4d620a9270113fc7d79d824c72ca6803defbc125448cc3417` |
| shasum | `/usr/bin/shasum` | 9979 | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` |
| rg | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | 6495920 | `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` |
| wc | `/usr/bin/wc` | 102048 | `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` |
| stat/test | `/usr/bin/stat`, `/bin/test` | 118576 / 101280 | `a3119dde...b65` / `ef72d761...640` |
| zsh | `/bin/zsh` | 1357312 | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` |

Mandatory whole-file F01 reads of capsule, brief, read allowlist, historical
fence, and approved probe forms each exited 0 and emitted complete content.
F02 repeated all five exact hashes. F03 harmless scan exited 1 with zero
stdout; F04/F05 observed 31 bytes; F06 exact executable check exited 0; F07
matched the zsh pin; F08 harmless script exited 0 with expected line; F09
syntax-only script exited 0.

The 66-entry read allowlist is unique, exact, and all entries exist. It names
no broad historical root. The capsule contains all rules and the dispatch
message supplies its exact pre-probed first read; no circular obligation
exists. The packet-surface safe-probe catalog is hash-pinned and explicitly
forbids operational probes.

Manager verdict: `RELEASE N1`.
