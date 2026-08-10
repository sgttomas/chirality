# Manager validation — fourth-lineage N1 BLOCK

Verdict: `BLOCK_N1_PREVALIDATED_COMMAND_FORM_NOT_EXECUTABLE`

## Fan-in identities

| Output | Bytes | SHA-256 |
|---|---:|---|
| `taint_clearance/STAGE_1_SALVAGE_HASHES.md` | 1,472 | `25ba97175e4113a3a57d589ba2b753846c9e85676d8987ed37044299d380b384` |
| `taint_clearance/STAGE_2_IDENTITY_SCAN.md` | 2,041 | `51a22ded86c91ebe030f1fcb599dc6979c020aac8dd2ae33ad1de1156b2793c2` |
| `returns/N1_TAINT_CLEARANCE_RETURN.md` | 5,398 | `c4ee40ab3b5d7dbc689a62355b56d85fab05bbb5b2604bd8564906d2adfca81a` |

Stage 1 is independently reproducible from the six exact salvage paths: all
six byte counts and hashes equal the third terminal record, total 111,145
bytes, and the ledger is 42,705 bytes at the owner-ruled SHA-256
`dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`.

Stage 2 is a valid BLOCK record, not a taint-clearance result. The frozen scan
form named `/usr/bin/rg`; that executable does not exist. The available binary
is `/opt/homebrew/bin/rg`, but substituting it after dispatch would violate the
frozen command preflight and the owner's no-silent-repair rule. The historical
identity result is therefore not established in this lineage.

The child also honestly reported that the prevalidated
`/usr/bin/sed -n ... -- <file>` form is not valid BSD `sed` syntax here: `--`
was treated as a nonexistent filename before the exact allowlisted Stage 6
file was displayed. No undeclared existing byte was opened. This actual
command fails fan-in allowlist conformance because the pathname `--` was not
declared, even though it resolved to nothing.

## Independent gate disposition

| Required N1 result | Manager result |
|---|---|
| Six salvage identities | `PASS` |
| Full four-pattern zero-hit scan | `NOT ESTABLISHED — BLOCK` |
| 80-row live-source provenance resolution | `NOT RUN — HELD` |
| 80-row / 13-field / contiguous identity validation | `NOT RUN — HELD` |
| Actual command/read allowlist conformance | `BLOCK` due attempted nonexistent `--` path; no forbidden existing byte read |
| Taint snapshot PASS | `ABSENT` |
| Four blocked-root preservation | `PASS` — Git status empty for all four and tree identities remain `256c7c43...`, `801c9430...`, `1298c1c8...`, `6b164aa0...` |

The pre-dispatch validator checked path containment and command shape but did
not resolve executable availability or exercise platform-specific option
semantics. That manager-owned validation defect is the exact fourth-lineage
cause. It cannot be repaired inside this lineage because N1's mandatory first
node returned BLOCK and the owner required whole-lineage closeout on any
failure.

N2, N3, freeze, and N4 were never dispatched. No packet, index, author return,
freeze manifest/hash, verifier, execution-approval request, or execution
authority exists.
