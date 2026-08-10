# Stage 1 — Salvage hash clearance

Verdict: `PASS`

All six owner-authorized third-lineage staged files were read only by their
exact allowlisted paths. Their current byte counts and SHA-256 identities are:

| File | Bytes | SHA-256 |
|---|---:|---|
| `STAGE_1_SOURCE_INVENTORY.md` | 8,851 | `108374dd11765af00dfb8ebab6edd13a05e6cfa9a3544a5bc553bf42edc71625` |
| `STAGE_2_AUTHORITY_SEMANTICS.md` | 9,227 | `7dbd151853ded2f65101e72287a42ef1d000dc73be35c4a388e09dbece431bf6` |
| `STAGE_3_COMMAND_EXTRACTION_CORE.csv` | 23,816 | `37c11862375a70f7335a4010f0608b8da9028141f81b58304f90a365a68cbb5b` |
| `STAGE_4_COMMAND_EXTRACTION_SAFETY.csv` | 19,065 | `c518dff8162feab3e85c37dac53761ad955187800301212b7c48b372be61018d` |
| `STAGE_5_COMMAND_AUTHORITY_LEDGER.csv` | 42,705 | `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809` |
| `STAGE_6_LEDGER_ALIGNMENT_CHECK.md` | 7,481 | `9b50c68b74a94232acca87de7cca48f0d55987c92578c27ca0ef9a8078c3ed5c` |

Total: 111,145 bytes. The ledger identity is exactly the owner-specified
`dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`.

Actual commands:

```text
/usr/bin/wc -c -- <the six exact salvage paths as explicit arguments>
/usr/bin/shasum -a 256 -- <the six exact salvage paths as explicit arguments>
```

Actual read paths: the six `source_reconstruction/STAGE_1` through `STAGE_6`
paths enumerated exactly in `allowlists/N1_READ_ALLOWLIST.txt`; no directory
or other blocked-root byte was read.
