# Eighth-lineage candidate diagnostic tool catalog

Status: `SEALED PRE-DISPATCH — EVERY CANDIDATE REQUIRES AUTHOR DISPOSITION`

## Operative environment contract

Every author safe probe and every manager independent re-probe runs from the
eighth run root under pinned `/bin/zsh --no-rcs` with `/usr/bin/env -i`, an
exact scratch `HOME` and `TMPDIR`, `LANG=C`, `LC_ALL=C`, and
`PATH=/nonexistent`. Every external command is therefore invoked by its exact
absolute catalog path. Operative packet commands must freeze the same
environment pattern, replace scratch HOME/TMPDIR only with the packet's exact
isolated paths, name the exact working directory before each phase, and use
no PATH-selected executable.

## Authoring-only frozen tools

| Tool/chain | Actual path | Bytes | SHA-256 | Permitted form |
|---|---|---:|---|---|
| cat | `/bin/cat` | 118800 | `c024d50a247255d4d620a9270113fc7d79d824c72ca6803defbc125448cc3417` | one exact whole-file operand |
| shasum wrapper | `/usr/bin/shasum` | 9979 | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | `-a 256` plus one exact operand |
| shasum interpreter | `/usr/bin/perl` | 101648 | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | recursive shebang chain only |
| rg | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | 6495920 | `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` | exact full-pattern scan of one new file |
| wc | `/usr/bin/wc` | 102048 | `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` | `-c` plus one exact new file |
| stat | `/usr/bin/stat` | 118576 | `a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65` | BSD `-f '%z'` plus one exact file |
| test | `/bin/test` | 101280 | `ef72d7615d6f7badb794fbc1f1289b47166a85add6d39d1be3a4f51bcc601640` | exact file/executable gate |
| env | `/usr/bin/env` | 102176 | `6e8b85a2efe5bf44ad11302f2b7b7e8c6b2f2c94f9bf117f5d4654b79bf85271` | exact clean environment launcher |
| zsh | `/bin/zsh` | 1357312 | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | `--no-rcs` safe probe and `-n` syntax |

`/usr/bin/shasum` is a `#!/usr/bin/perl` script; the complete chain is
therefore pinned above. All other authoring-only paths are Mach-O binaries.

## Packet candidates requiring one direct diagnostic disposition each

The author must place every row in Stage 1 as either `SURVIVES — DIRECTLY
NECESSARY` with a concrete causal-trace function, or `REMOVED — NO DIRECT
DIAGNOSTIC NECESSITY`. Convenience, build, overlay, package preparation,
generic inventory, and merely familiar workflow are not acceptable reasons.
Every surviving row must appear in every relevant exact probe-ledger chain.

| Candidate | Path / complete chain | Bytes | SHA-256 | Narrow candidate function |
|---|---|---:|---|---|
| shell | `/bin/zsh` | 1357312 | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | exact owner shell constructs |
| clean environment | `/usr/bin/env` | 102176 | `6e8b85a2efe5bf44ad11302f2b7b7e8c6b2f2c94f9bf117f5d4654b79bf85271` | prevent ambient executable selection |
| evidence text | `/usr/bin/printf` | 101808 | `f2a76beee50f16a1193244519ecfad592b3af0623276b41c088c0ef8650c05f7` | exact terminal/evidence markers |
| gates | `/bin/test` | 101280 | `ef72d7615d6f7badb794fbc1f1289b47166a85add6d39d1be3a4f51bcc601640` | stop on exact pre/postconditions |
| evidence directory | `/bin/mkdir` | 101280 | `eb3b48e064031c5491bcb9a99bbf44753c9ee074d10c69d114cb4cbc236ca02c` | isolated trace evidence root only |
| host version | `/usr/bin/sw_vers` | 135248 | `a5879fe2c946cbdfb74e3f614d89786031e62e85002ffab7d4047859bbcedd95` | bind macOS version if causally required |
| architecture | `/usr/bin/uname` | 101264 | `fdd05a10dfc0901947dfe8acd4ad14dae3d7c3efb4701a46ce6b7cb8bffeb5d7` | bind host architecture if causally required |
| evidence hash | `/usr/bin/shasum` -> `/usr/bin/perl` | 9979 / 101648 | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` / `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | bind script/transcript/package precondition |
| isolated keychain | `/usr/bin/security` | 660768 | `2b5c0eae2ee36c5400309edc44635b07e08dc7d9e3fac26c1fa7612a3493ddc7` | D-APP-94 isolated login-keychain baseline only |
| target relation | `/bin/ps` | 170432 | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` | prove exact direct-child PID |
| bounded parse | `/usr/bin/awk` | 301568 | `3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a` | parse only declared ps fields |
| timestamp | `/bin/date` | 135104 | `28f40376c23f2d4f8bd58eb27c9aa86c25a51fe949f12dab1bc0254f906aa9f6` | bind trace timing |
| debugger launcher | `/usr/bin/xcrun` -> `/Applications/Xcode.app/Contents/Developer/usr/bin/lldb` | 117104 / 554848 | `4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6` / `0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca` | exact LLDB attach/script invocation |
| transcript capture | `/usr/bin/tee` | 101040 | `d284dd54c2e98bd7da539085105bf50a5455eb467c5aaf382413bc0b9b02a226` | preserve interactive LLDB bytes if exact architecture permits |
| first signal | `/bin/kill` | 101312 | `08fab82eded4aad982575622b90b2c8c6058b241432f66caeaed212347b44160` | exact helper SIGTERM act only |
| bounded wait | `/bin/sleep` | 100976 | `b675bfecd394b9708eec132b91cecaa5def4b245291d5bf8bdfe531ea0451bde` | bounded observation cadence only |
| cleanup | `/bin/rm` | 118992 | `c12e91a60bbc9da47579b3d78275bd2e08e694833b030b41c7bcdb64f88123e7` | exact disposable diagnostic root only |

Every listed path is Mach-O except shasum, whose absolute Perl interpreter is
closed above. `xcrun` resolves the exact LLDB binary shown; both identities are
mandatory whenever xcrun survives.

## Explicitly excluded chains

`npm` and `node` are not frozen. The seventh failure demonstrated that the npm
path is a mise bash wrapper, but the stronger eighth requirement is diagnostic
necessity: neither a package-manager convenience nor a build chain directly
observes helper SIGTERM survival. The author must expressly confirm
`npm/node: REMOVED — NOT DIAGNOSTICALLY NECESSARY`. If the author instead finds
one necessary, the lineage blocks because the sealed catalog cannot be
expanded after dispatch.

Also excluded as convenience/build/overlay/preparation surfaces: `git`, `cp`,
`ditto`, `plutil`, `find`, `readlink`, `cmp`, `sort`, `xargs`, and any Electron
build/install/overlay tool. No PATH-selected executable, wrapper, shebang
interpreter, shell alias/function, package script, or unlisted binary is
permitted.
