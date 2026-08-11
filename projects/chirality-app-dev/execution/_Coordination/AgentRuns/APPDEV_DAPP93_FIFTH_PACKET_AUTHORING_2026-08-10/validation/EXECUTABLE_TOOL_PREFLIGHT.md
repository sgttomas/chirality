# Manager executable-tool preflight

Verdict: `PASS — ALL FROZEN COMMAND FORMS EXECUTABLE BEFORE N1`

Host observed at preparation time: `Darwin 25.6.0 arm64`, macOS `26.6`.
Base and branch: `226e92a69125fe746d3e55e44414ec5afe15010d`,
`codex/app-dapp93-fifth-authoring-lineage-20260810`.

Scratch input:
`scratch/tool-probe.txt`, 54 bytes, SHA-256
`0cbd64697d58f22e69b60ec023feac49d27af5b383682dad96bcae059f157f9f`.
All probes were harmless reads of that file or read-only status/inventory of
the fresh run root. No historical root was an operand.

## Resolution and byte pins

`command -v` was followed by symlink resolution. The exact real paths frozen
in `allowlists/FROZEN_COMMAND_FORMS.md` were hashed by `/usr/bin/shasum -a
256`; each value matched the table:

| Form | PATH resolution | Frozen real path | Binary SHA-256 |
|---|---|---|---|
| F01 | `/usr/bin/shasum` | same | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` |
| F02 | `/opt/homebrew/bin/rg` | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` |
| F03 | `/usr/bin/sed` | same | `fec09f1c7235be662ba4346b2bf68be392c82ad4e73841b06428318402626708` |
| F04 | `/usr/bin/awk` | same | `3868b14602a4851218210ae1b08732fbdee703ac2c1e2d1898272b42fd33151a` |
| F05 | `/usr/bin/wc` | same | `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` |
| F06 | `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3` | `/Users/ryan/.local/share/mise/installs/python/3.13.14/bin/python3.13` | `1a2e543a5426f665b9f321d391995b46e985fbea8df2a5bea86d7210c603460a` |
| F07 | `/opt/homebrew/bin/git` | `/opt/homebrew/Cellar/git/2.55.0/bin/git` | `5f0351f649aa1321345229d5256fc8043517778b134a3b4571ecdc3818f124b2` |
| F08 | `/usr/bin/find` | same | `05aa84ee15d95122cfa3de6a132ace019eb78b27da57534b5d555719c8380f7b` |
| F09 | `/usr/bin/sort` | same | `a61f82d2598a7a5b9cc273e2426b8c19c532eb72963f34dc97c9cd3d1210486f` |
| F10 | `/usr/bin/cmp` | same | `bf0111a82ee28deeb99a83eaee6f0829a743e09dcf8193ebd49b4c4190ad2457` |
| F11 | `/usr/bin/stat` | same | `a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65` |

Observed versions included ripgrep 15.2.0, Python 3.13.14, Git 2.55.0,
Apple sort 2.3, and awk 20200816. `/usr/bin/sed`, `wc`, `find`, and `stat`
reject GNU `--version`; this was treated as platform evidence, not as a
frozen command probe.

## Executed frozen forms

| Form | Probe result | Expected/observed behavior |
|---|---|---|
| F01 | exit `0` | one digest row; required/observed |
| F02 | exit `1`, stdout `0` bytes | clean zero-hit is required/observed; real resolved binary repeated the probe with the same result |
| F03 | exit `0` | BSD form `sed -n '1p' file`, no `--`; first line observed |
| F04 | exit `0`, stdout `3` | three CSV fields required/observed |
| F05 | exit `0`, stdout byte count `54` | required/observed |
| F06 | exit `0`, stdout `2 3` | isolated standard-library CSV read expression required/observed; real resolved Python repeated the result |
| F07 | exit `0` | read-only Git status reported only this untracked fresh root; real resolved Git repeated the result |
| F08 | exit `0` | one explicit scratch path observed; no broad/historical walk |
| F09 | exit `0` | two scratch lines sorted |
| F10 | exit `0` | scratch self-comparison equal |
| F11 | exit `0`, stdout `54` | BSD `stat -f '%z' file`; required/observed |

The F02 expected exit `1` is not a probe failure: the frozen contract defines
that exit as successful zero-hit behavior. Exit `0` would prove a taint match
and block substantive clearance. Every binary, flag shape, operand placement,
and expected exit behavior needed by the child briefs has therefore been
executed once before N1. No substitution is permitted after dispatch.

## Path-shape gate

Every frozen search form requires explicit allowlisted file operands. F08 is
limited to the fresh root or a child-owned write root. No command form accepts
a historical run root, the broad `AgentRuns` root, or the broad App project
root. Pre-dispatch declared-command review passes. The same rule is a
mandatory fan-in check for N1, N2, and N3.
