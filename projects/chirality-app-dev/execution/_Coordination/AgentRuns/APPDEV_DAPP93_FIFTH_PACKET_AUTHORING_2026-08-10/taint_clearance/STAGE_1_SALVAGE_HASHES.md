# Stage 1 — salvage hashes

Status: `PASS`

Each owner-authorized salvage file was addressed directly by its exact path.
No historical root was listed, globbed, searched, or walked, and no salvage
file was copied.

| Exact salvage file | SHA-256 | Result |
|---|---|---|
| `STAGE_1_SOURCE_INVENTORY.md` | `108374dd11765af00dfb8ebab6edd13a05e6cfa9a3544a5bc553bf42edc71625` | PASS |
| `STAGE_2_AUTHORITY_SEMANTICS.md` | `7dbd151853ded2f65101e72287a42ef1d000dc73be35c4a388e09dbece431bf6` | PASS |
| `STAGE_3_COMMAND_EXTRACTION_CORE.csv` | `37c11862375a70f7335a4010f0608b8da9028141f81b58304f90a365a68cbb5b` | PASS |
| `STAGE_4_COMMAND_EXTRACTION_SAFETY.csv` | `c518dff8162feab3e85c37dac53761ad955187800301212b7c48b372be61018d` | PASS |
| `STAGE_5_COMMAND_AUTHORITY_LEDGER.csv` | `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809` | PASS — exact owner-recorded digest |
| `STAGE_6_LEDGER_ALIGNMENT_CHECK.md` | `9b50c68b74a94232acca87de7cca48f0d55987c92578c27ca0ef9a8078c3ed5c` | PASS |

Frozen form F01 was invoked once per file as `/usr/bin/shasum -a 256
"{exact-salvage-file}"`; all six invocations exited `0` and emitted one
digest/path row. Native context telemetry: unavailable.
