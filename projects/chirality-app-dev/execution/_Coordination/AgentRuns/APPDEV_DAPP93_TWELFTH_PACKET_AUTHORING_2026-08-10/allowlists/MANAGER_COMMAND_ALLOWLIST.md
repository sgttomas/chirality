# Manager command allowlist and binary pins

Restricted environment: `PATH=/usr/bin:/bin:/opt/homebrew/Cellar/ripgrep/15.2.0/bin`; working directory is repository root or the twelfth run root; scratch targets remain under `scratch/**`.

| Element | Kind | SHA-256 | Necessity |
|---|---|---|---|
| `/bin/zsh` | real binary | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | frozen shell for syntax-only packet-script checks |
| `/usr/bin/python3` | real binary | `44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698` | execute manager validators and harmless probes |
| `/usr/bin/shasum` | executable script | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | exact byte identities |
| `/usr/bin/perl` | real binary | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | transitive interpreter for `/usr/bin/shasum` |
| `/usr/bin/stat` | real binary | `a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65` | durable file-count/byte telemetry |
| `/usr/bin/wc` | real binary | `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` | bounded byte and line measurements |
| `/usr/bin/grep` | real binary | `e9e8aa8089241c6dcb8fa744d0dd4a7eabd3b1dae657cc824946d17e3dc457e8` | exact sentinel checks |
| `/usr/bin/sed` | real binary | `fec09f1c7235be662ba4346b2bf68be392c82ad4e73841b06428318402626708` | bounded display of new-root evidence only |
| `/usr/bin/awk` | real binary | `3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a` | exact inventory formatting |
| `/usr/bin/find` | real binary | `05aa84ee15d95122cfa3de6a132ace019eb78b27da57534b5d555719c8380f7b` | new-root-only inventory enumeration |
| `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | resolved real binary | `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` | embedded per-stub historical-ID classification in fan-in |

`/opt/homebrew/bin/rg` is a symlink to the pinned real binary and is not used by frozen forms. `/usr/bin/shasum` has shebang `#!/usr/bin/perl`; the transitive chain is pinned above. Manager validators use the direct absolute Python interpreter and may invoke only the pinned resolved `rg` path.

Frozen forms:

- `M01 /usr/bin/python3 manager/VERIFY_CITATIONS.py`
- `M02 /usr/bin/python3 manager/VALIDATE_SKELETON.py packet returns/N1_SELF_CENSUS.md`
- `M03 /usr/bin/python3 manager/VALIDATE_PACKET.py --mode fixture scratch/filled_fixture specs`
- `M04 /usr/bin/python3 manager/VALIDATE_PACKET.py --mode reject-fixture scratch/reject_fixture specs` (expected exit `2` with classified locations)
- `M05 /usr/bin/python3 manager/VALIDATE_PACKET.py --mode packet packet specs`
- `M06 /usr/bin/python3 manager/OBSERVE_PROGRESS.py packet`
- `M07 /bin/zsh -n packet/scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh`
- `M08 /bin/zsh -n packet/scripts/CAPTURE_TRACE_EVIDENCE.zsh`
- `M09 /usr/bin/shasum -a 256 <exact allowlisted file>`
- `M10 /usr/bin/stat -f %z <exact new-root file>`
- `M11 /usr/bin/find <exact new-root directory> -type f -print`
- `M12 /usr/bin/wc -c <exact new-root file>`
- `M13 /usr/bin/grep -F <literal sentinel> <exact new-root file>`
- `M14 /usr/bin/sed -n <bounded range> <exact new-root file>`
- `M15 /usr/bin/awk <fixed inventory expression> <new-root-only input>`
- `P01 /bin/zsh --version`
- `P02 /usr/bin/python3 --version`
- `P03 /usr/bin/perl -v`
- `P04 /usr/bin/shasum -a 256 scratch/tool-probe.txt`
- `P05 /usr/bin/stat -f %z scratch/tool-probe.txt`
- `P06 /usr/bin/wc -c scratch/tool-probe.txt`
- `P07 /usr/bin/grep -F probe scratch/tool-probe.txt`
- `P08 /usr/bin/sed -n 1p scratch/tool-probe.txt`
- `P09 /usr/bin/awk NR==1 scratch/tool-probe.txt`
- `P10 /usr/bin/find scratch/filled_fixture -type f -print`
- `P11 /opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg --version`
- `P12 /bin/zsh -n scratch/filled_fixture/scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh`
- `P13 /bin/zsh -n scratch/filled_fixture/scripts/CAPTURE_TRACE_EVIDENCE.zsh`

Parent-provided activation intake before graph freeze: exact baseline/status and Receipt 159 validation; bounded receipt read; `git ls-tree` path-metadata enumeration of D-APP-93 run-root names; exact SHA reads of the six authorized fifth clearance records and one authorized ledger; host tool path/type/hash resolution and neutral version/probe calls. No historical blocked-root content other than those exact authorized files was read.
