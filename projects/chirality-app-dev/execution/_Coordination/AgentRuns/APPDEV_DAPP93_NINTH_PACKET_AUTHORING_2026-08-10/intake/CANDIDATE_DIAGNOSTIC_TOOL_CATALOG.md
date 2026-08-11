# Ninth-lineage candidate diagnostic tool catalog

Status: `SEALED PRE-DISPATCH — TWO-TIER CLASSIFICATION REQUIRED`

## Operative environment contract

Every safe author probe and manager re-probe runs from the ninth run root
under pinned `/bin/zsh --no-rcs` with `/usr/bin/env -i`, exact scratch `HOME`
and `TMPDIR`, `LANG=C`, `LC_ALL=C`, and `PATH=/nonexistent`. Every external
command uses its absolute catalog path. Packet commands freeze the same
discipline, changing only packet-owned isolated paths.

## Authoring-only frozen tools

| Tool/chain | Actual path | Bytes | SHA-256 | Permitted form |
|---|---|---:|---|---|
| cat | `/bin/cat` | 118800 | `c024d50a247255d4d620a9270113fc7d79d824c72ca6803defbc125448cc3417` | one exact whole-file operand |
| shasum wrapper | `/usr/bin/shasum` | 9979 | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | `-a 256` plus one exact operand |
| shasum interpreter | `/usr/bin/perl` | 101648 | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | recursive shebang chain only |
| rg | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | 6495920 | `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` | exact full-pattern scan of one new file |
| wc | `/usr/bin/wc` | 102048 | `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` | `-c` plus one exact new file |
| stat | `/usr/bin/stat` | 118576 | `a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65` | BSD `-f '%z'` plus one exact file |
| test | `/bin/test` | 101280 | `ef72d7615d6f7badb794fbc1f1289b47166a85add6d39d1be3a4f51bcc601640` | exact gate |
| env | `/usr/bin/env` | 102176 | `6e8b85a2efe5bf44ad11302f2b7b7e8c6b2f2c94f9bf117f5d4654b79bf85271` | exact clean launcher |
| zsh | `/bin/zsh` | 1357312 | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | `--no-rcs` probes and `-n` syntax |

`/usr/bin/shasum` is a `#!/usr/bin/perl` script and its complete chain is
pinned. All other authoring-only paths are Mach-O binaries.

## Packet candidates

Every row needs a one-line necessity justification tied directly to the
owner-operated LLDB causal trace. Convenience, builds, overlays, installation,
and generic inventory are rejected. Every surviving tool and full execution
chain appears in the unified probe ledger.

| Candidate | Complete path/chain | Bytes | SHA-256 | Narrow diagnostic function |
|---|---|---:|---|---|
| shell | `/bin/zsh` | 1357312 | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | exact owner shell constructs |
| clean environment | `/usr/bin/env` | 102176 | `6e8b85a2efe5bf44ad11302f2b7b7e8c6b2f2c94f9bf117f5d4654b79bf85271` | prevent ambient executable selection |
| evidence text | `/usr/bin/printf` | 101808 | `f2a76beee50f16a1193244519ecfad592b3af0623276b41c088c0ef8650c05f7` | exact evidence markers |
| gates | `/bin/test` | 101280 | `ef72d7615d6f7badb794fbc1f1289b47166a85add6d39d1be3a4f51bcc601640` | exact stop conditions |
| evidence directory | `/bin/mkdir` | 101280 | `eb3b48e064031c5491bcb9a99bbf44753c9ee074d10c69d114cb4cbc236ca02c` | isolated evidence root |
| host version | `/usr/bin/sw_vers` | 135248 | `a5879fe2c946cbdfb74e3f614d89786031e62e85002ffab7d4047859bbcedd95` | bind relevant macOS host |
| architecture | `/usr/bin/uname` | 101264 | `fdd05a10dfc0901947dfe8acd4ad14dae3d7c3efb4701a46ce6b7cb8bffeb5d7` | bind host architecture |
| evidence hash | `/usr/bin/shasum` -> `/usr/bin/perl` | 9979 / 101648 | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` / `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | bind scripts and evidence |
| isolated keychain | `/usr/bin/security` | 660768 | `2b5c0eae2ee36c5400309edc44635b07e08dc7d9e3fac26c1fa7612a3493ddc7` | D-APP-94 isolated login-keychain baseline |
| target relation | `/bin/ps` | 170432 | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` | prove exact direct-child PID |
| bounded parse | `/usr/bin/awk` | 301568 | `3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a` | parse declared process fields |
| timestamp | `/bin/date` | 135104 | `28f40376c23f2d4f8bd58eb27c9aa86c25a51fe949f12dab1bc0254f906aa9f6` | bind trace timing |
| debugger launcher | `/usr/bin/xcrun` -> `/Applications/Xcode.app/Contents/Developer/usr/bin/lldb` | 117104 / 554848 | `4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6` / `0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca` | exact LLDB attach/script invocation |
| transcript capture | `/usr/bin/tee` | 101040 | `d284dd54c2e98bd7da539085105bf50a5455eb467c5aaf382413bc0b9b02a226` | preserve interactive LLDB bytes |
| first signal | `/bin/kill` | 101312 | `08fab82eded4aad982575622b90b2c8c6058b241432f66caeaed212347b44160` | exact helper SIGTERM act |
| bounded wait | `/bin/sleep` | 100976 | `b675bfecd394b9708eec132b91cecaa5def4b245291d5bf8bdfe531ea0451bde` | bounded observation cadence |
| cleanup | `/bin/rm` | 118992 | `c12e91a60bbc9da47579b3d78275bd2e08e694833b030b41c7bcdb64f88123e7` | exact disposable diagnostic root |

## Two-tier rule

- `AGENT_PROVEN`: sandbox-permitted form; exact restricted probe, chain, pins,
  invocation, exit, and output recorded. Operative forms unsafe to execute may
  be `REVIEWED_NOT_EXECUTED`, but their neutral tool probe remains proven.
- `OWNER_PREFLIGHT`: only when the exact binary exists, is readable and pinned;
  the neutral/exact probe actually fails because the sandbox denies execution
  (`operation not permitted`, entitlement, or setuid refusal); and the tool is
  trace-necessary. Missing tools and syntax errors are hard rejection.

Every OWNER_PREFLIGHT form becomes packet Runbook Step 0 with exact command,
pin confirmation, expected exit/output shape, evidence record fields, and a
mandatory stop before any operative act on mismatch.

## Explicit exclusions

`npm`, `node`, `git`, `cp`, `ditto`, `plutil`, `find`, `readlink`, `cmp`,
`sort`, `xargs`, build/install/overlay tools, aliases, functions, ambient-PATH
selection, and unlisted executables are excluded as non-diagnostic surfaces.
