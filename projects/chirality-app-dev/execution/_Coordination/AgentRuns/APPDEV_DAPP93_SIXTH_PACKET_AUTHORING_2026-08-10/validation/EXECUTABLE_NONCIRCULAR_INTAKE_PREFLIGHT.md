# Executable non-circular intake and tool preflight

Status: `PASS — ALL GATES SATISFIED BEFORE N1 DISPATCH`

Observed at `2026-08-11T01:11:28Z`; native context telemetry unavailable.

## Resolved binary identities

Each PATH-selected tool was resolved through symlinks to the actual host file
and its bytes were pinned.

| Tool | Actual absolute path | Bytes | SHA-256 | Host syntax |
|---|---|---:|---|---|
| cat | `/bin/cat` | 118800 | `c024d50a247255d4d620a9270113fc7d79d824c72ca6803defbc125448cc3417` | whole-file operand accepted |
| shasum | `/usr/bin/shasum` | 9979 | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | `-a 256` accepted |
| rg | `/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg` | 6495920 | `1c57905960cd69dbb5b05492560957f4a57cdd4d39137e20de23981c6e1f4423` | exact `-n -e` form accepted |
| wc | `/usr/bin/wc` | 102048 | `32f22e2b385cbc5250c5cc9a11465f5afa74c024724040f47d9edb71ce429e1a` | BSD `-c` accepted |
| stat | `/usr/bin/stat` | 118576 | `a3119dde345aa860c2f2e293ecd5f9f3db450d2570343e3319838ac154617b65` | BSD `-f '%z'` accepted |

## Frozen-form execution probes

| Form | Exact probe | Exit | Observed | Result |
|---|---|---:|---|---|
| F01 intake 1 | whole-file `cat` of capsule | 0 | 7303 source bytes; pinned hash `5e4c3c8f...d5b` | PASS |
| F01 intake 2 | whole-file `cat` of brief | 0 | 1864 source bytes; pinned hash `464dfa98...7cf` | PASS |
| F01 intake 3 | whole-file `cat` of read allowlist | 0 | 9176 source bytes; pinned hash `a5677883...dd6` | PASS |
| F01 intake 4 | whole-file `cat` of historical-root fence | 0 | 1042 source bytes; pinned hash `6ffa5a46...687` | PASS |
| F02 intake 1–4 | exact `shasum -a 256` once per same file | 0 each | all four expected identities | PASS |
| F02 generic | exact scratch-file form | 0 | one digest row | PASS |
| F03 | exact full-pattern `rg` form on harmless scratch file | 1 | stdout zero bytes | PASS — required clean form |
| F04 | exact BSD `wc -c` form on scratch file | 0 | 39 bytes | PASS |
| F05 | exact BSD `stat -f '%z'` form on scratch file | 0 | 39 bytes | PASS |
| W01 | manager-created scratch and sealed files via `apply_patch` | success | exact paths only | PASS |

The four mandatory child intake reads were executed exactly as frozen, not
shape-checked. Each emitted the complete source file and exited zero; source
byte counts and content hashes were independently recorded. The 59-entry read
allowlist is unique, exact, and all 59 files exist. It includes no broad
historical root. The only historical-root entries are the fourteen
owner-authorized exact citation records.

## Non-circularity result

The dispatch message itself supplies the exact first F01 capsule command and
pins the capsule, brief, allowlist, and fence hashes. The capsule contains the
complete operative rule set, frozen forms, allowed reads, exact writes,
durable stages, clocks, checks, and escalation rule. The brief contains no
additional operative rule. Therefore no obligation is available only inside
material the child cannot lawfully read in full.

Manager verdict: `RELEASE N1`.
