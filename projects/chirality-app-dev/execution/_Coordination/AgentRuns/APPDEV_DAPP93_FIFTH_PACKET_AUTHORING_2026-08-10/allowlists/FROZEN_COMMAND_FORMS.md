# Frozen host command forms

Status: `SEALED FOR FIFTH-LINEAGE CHILD BRIEFS`

Only the forms below may be used by N1, N2, or N3. Braced operands must be
replaced by explicit paths present in that child's read or write allowlist;
they are not shell-expanded globs. All path operands must be quoted. A child
must record every actual invocation in its terminal return.

| ID | Resolved binary | SHA-256 | Frozen form and expected behavior |
|---|---|---|---|
| F01 | `/usr/bin/shasum` | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | `/usr/bin/shasum -a 256 "{explicit-file}"` -> exit 0 and one SHA/path row |
| F02 | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg --case-sensitive --no-heading --line-number -e 'C[0-9]{3,}|A3-OP-[0-9]{3}|R[0-9]+-C[0-9]{3,}|ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+' "{explicit-file}" ...` -> exit 1/stdout 0 bytes is the required clean result; exit 0 is a taint hit, not a tool failure |
| F03 | `/usr/bin/sed` | `fec09f1c7235be662ba4346b2bf68be392c82ad4e73841b06428318402626708` | `/usr/bin/sed -n '1p' "{explicit-file}"` -> BSD-compatible, exit 0; no GNU `--` operand delimiter |
| F04 | `/usr/bin/awk` | `3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a` | `/usr/bin/awk -F, 'NR==1{print NF}' "{explicit-csv}"` -> exit 0 and positive field count |
| F05 | `/usr/bin/wc` | `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` | `/usr/bin/wc -c "{explicit-file}"` -> exit 0 and byte count |
| F06 | `/Users/ryan/.local/share/mise/installs/python/3.13.14/bin/python3.13` | `1a2e543a5426f665b9f321d391995b46e985fbea8df2a5bea86d7210c603460a` | `/Users/ryan/.local/share/mise/installs/python/3.13.14/bin/python3.13 -I -c '{standard-library read-only validation expression}' "{explicit-file}" ...` -> exit 0 and expression-specific result; no network, subprocess, directory walk, or writes outside the child write targets |
| F07 | `/opt/homebrew/Cellar/git/2.55.0/bin/git` | `5f0351f649aa1321345229d5256fc8043517778b134a3b4571ecdc3818f124b2` | `/opt/homebrew/Cellar/git/2.55.0/bin/git -C "/Users/ryan/.codex/worktrees/55d3/chirality" status --short -- "{explicit-allowed-path}"` -> exit 0; read-only Git status only |
| F08 | `/usr/bin/find` | `05aa84ee15d95122cfa3de6a132ace019eb78b27da57534b5d555719c8380f7b` | `/usr/bin/find "{fresh-run-root-or-child-write-root}" -type f -print` -> exit 0; never an existing historical root or broad `AgentRuns` root |
| F09 | `/usr/bin/sort` | `a61f82d2598a7a5b9cc273e2426b8c19c532eb72963f34dc97c9cd3d1210486f` | `/usr/bin/sort "{explicit-file}"` -> exit 0 |
| F10 | `/usr/bin/cmp` | `bf0111a82ee28deeb99a83eaee6f0829a743e09dcf8193ebd49b4c4190ad2457` | `/usr/bin/cmp -s "{explicit-file-a}" "{explicit-file-b}"` -> exit 0 for equal bytes |
| F11 | `/usr/bin/stat` | `a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65` | `/usr/bin/stat -f '%z' "{explicit-file}"` -> BSD-compatible, exit 0 and byte count |

`apply_patch` is an API operation, not a frozen host binary. It may write only
the exact child targets. Shell built-ins, unlisted binaries, command
substitution, broad globs, recursive search outside a child's write root,
network operations, and Git mutations are prohibited.
