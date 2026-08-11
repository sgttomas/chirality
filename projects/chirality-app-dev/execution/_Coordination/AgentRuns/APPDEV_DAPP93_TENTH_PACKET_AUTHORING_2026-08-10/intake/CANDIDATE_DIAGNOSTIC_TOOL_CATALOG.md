# Tenth-lineage diagnostic tool catalog

Status: `SEALED — MINIMAL TRACE SURFACE; TWO-TIER PROBES`

All safe probes run from the tenth root with pinned `/bin/zsh --no-rcs` under
`/usr/bin/env -i`, `PATH=/nonexistent`, exact run-local HOME/TMPDIR,
`PYTHONDONTWRITEBYTECODE=1`, `LANG=C`, and `LC_ALL=C`. External tools use
absolute paths. Ambient PATH, aliases, functions, build/install/overlay tools,
npm, and node are excluded.

## Author/control tools

| Chain | Bytes SHA-256 |
|---|---|
| `/bin/cat` | 118800 `c024d50a247255d4d620a9270113fc7d79d824c72ca6803defbc125448cc3417` |
| `/usr/bin/shasum -> /usr/bin/perl` | 9979 `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3`; 101648 `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` |
| `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | 6495920 `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` |
| `/usr/bin/wc` | 102048 `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` |
| `/usr/bin/stat` | 118576 `a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65` |
| `/bin/test` | 101280 `ef72d7615d6f7badb794fbc1f1289b47166a85add6d39d1be3a4f51bcc601640` |
| `/usr/bin/env` | 102176 `6e8b85a2efe5bf44ad11302f2b7b7e8c6b2f2c94f9bf117f5d4654b79bf85271` |
| `/bin/zsh` | 1357312 `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` |
| `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3 -> python3.13` | 17424272 `1a2e543a5426f665b9f321d391995b46e985fbea8df2a5bea86d7210c603460a` |

## Packet candidates

Every surviving entry needs a one-line necessity tied directly to the
owner-operated LLDB trace. Convenience/generic inventory is rejection.

| Function | Chain | Pin(s) |
|---|---|---|
| shell | `/bin/zsh` | `528da649...25e8` |
| clean environment | `/usr/bin/env` | `6e8b85a2...5271` |
| evidence markers | `/usr/bin/printf` | `f2a76beee50f16a1193244519ecfad592b3af0623276b41c088c0ef8650c05f7` |
| exact gates | `/bin/test` | `ef72d761...1640` |
| evidence directories | `/bin/mkdir` | `eb3b48e064031c5491bcb9a99bbf44753c9ee074d10c69d114cb4cbc236ca02c` |
| host version | `/usr/bin/sw_vers` | `a5879fe2c946cbdfb74e3f614d89786031e62e85002ffab7d4047859bbcedd95` |
| architecture | `/usr/bin/uname` | `fdd05a10dfc0901947dfe8acd4ad14dae3d7c3efb4701a46ce6b7cb8bffeb5d7` |
| hashes | `/usr/bin/shasum -> /usr/bin/perl` | `0812595f...1e3`; `626702a7...afd` |
| isolated keychain | `/usr/bin/security` | `2b5c0eae2ee36c5400309edc44635b07e08dc7d9e3fac26c1fa7612a3493ddc7` |
| direct-child relation | `/bin/ps` | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` |
| bounded parse | `/usr/bin/awk` | `3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a` |
| timestamp | `/bin/date` | `28f40376c23f2d4f8bd58eb27c9aa86c25a51fe949f12dab1bc0254f906aa9f6` |
| debugger | `/usr/bin/xcrun -> /Applications/Xcode.app/Contents/Developer/usr/bin/lldb` | `4bc0cc7099775fbe35c653ceb09e0e393d2e5ada024db872e0eb8c43500b4dc6`; `0035650adb4c8278122f70771e2e052a2b6e6d644a76745ffecf8c3a0bd686ca` |
| transcript | `/usr/bin/tee` | `d284dd54c2e98bd7da539085105bf50a5455eb467c5aaf382413bc0b9b02a226` |
| first signal if command-shaped | `/bin/kill` | `08fab82eded4aad982575622b90b2c8c6058b241432f66caeaed212347b44160` |
| bounded wait | `/bin/sleep` | `b675bfecd394b9708eec132b91cecaa5def4b245291d5bf8bdfe531ea0451bde` |
| cleanup | `/bin/rm` | `c12e91a60bbc9da47579b3d78275bd2e08e694833b030b41c7bcdb64f88123e7` |

`AGENT_PROVEN` requires an exact restricted neutral probe and full chain pin.
`OWNER_PREFLIGHT` is allowed only when the binary exists/readable/pinned, the
exact neutral form fails by sandbox entitlement/operation denial rather than
missing/syntax, and necessity ties directly to the trace. Every owner-tier form
becomes packet Step 0 with exact owner command, pin, expected exit/output,
recording fields, and stop-unexecuted route. Missing tools and wrong syntax are
hard rejections.
