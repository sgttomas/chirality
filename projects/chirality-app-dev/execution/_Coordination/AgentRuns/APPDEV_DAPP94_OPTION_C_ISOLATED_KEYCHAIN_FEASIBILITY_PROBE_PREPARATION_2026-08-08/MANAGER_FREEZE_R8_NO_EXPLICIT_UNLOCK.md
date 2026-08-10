# R8 no-explicit-unlock manager freeze

Status: `IMMUTABLE CANDIDATE — ONE FRESH VERIFIER`

| Object | SHA-256 |
|---|---|
| R7 unlock-stop intake | `43340470531d9fbb9788d7aa7e48693e82117da9d5aeacdc82125843a00fc961` |
| R8 driver | `d183572fadb5d67d8716858ae3b589acd60535433aea8239f0acf65b53738afd` |
| R8 packet | `60a179fc8456b541980e140b6f3caa3e535f87a39b3a9add2227ce20670e090c` |
| R8 evidence contract | `c641c9dac802a580af3425505930a5cb5e3999d46c8979262b29dc1c43f93fc9` |
| R8 withheld token | `5e717da8a9a8ddbbc7c74828a391e990b1b1f02be82a3d51417ad4722b3a7e32` |
| R8 validation | `6b1a8b7f67b2469adc07af10b1679bb6f4bfc9ed8e4023f4c1d6decac920e71a` |
| Apple SDK `SecKeychain.h` primary source | `7dd9966ba8769c1dd9ed29e52d04b5fceea16efc8c2f0ca20ead84a513d74d65` |
| Preserved R7 driver | `091b77160a127f371266fa08e440e9c39ec4be0123766da7f0284256cfff8edd` |
| R7 calibrated freeze | `a3c06b374109a61e7cdd611a0ab866a403d3c491ccc2181cdee43e34ae09c3dd` |
| R7 verifier PASS | `c3ac58d0555d1c06788611863b2cabe1d725dbc66b9165b525fae6700b2eb9c6` |

Frozen design truth: R8 omits explicit unlock entirely and makes no
create-leaves-unlocked claim. Exact synthesized default/search readback and the
actual safeStorage availability/public-constant roundtrip are the direct
empirical gates. R7-to-R8 executable delta is R8 namespace/evidence naming plus
exact removal of the unlock command/status/gate; all owner guard/backstop,
prompt, failure-retention, commit-before-delete, cleanup, and exclusion bytes
remain otherwise preserved.

R7 root and occupied `returned_r7/` are present and immutable. R8 root and
`returned_r8/` are absent. R8 zsh syntax passes. No candidate/security/
Electron/deletion or prohibited action occurred, and the R8 token remains
withheld pending the one authorized fresh verifier.
