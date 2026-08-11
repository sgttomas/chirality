# Normalization amendment — fifth-lineage Stage 4 CSV

Status: `OWNER-AUTHORIZED BYTE HYGIENE; SUBSTANTIVE BLOCK UNCHANGED`

The owner authorized removal of exactly one surplus terminal LF from
`taint_clearance/STAGE_4_LEDGER_ROW_PROVENANCE.csv` on 2026-08-10.

| Identity | Bytes | SHA-256 | Terminal bytes |
|---|---:|---|---|
| Preserved pre-repair identity | 38,510 | `bdfdd3d98ca911947ebdb87b5d06ea749ac3f04ed6a034292c9cc83e81b78f3b` | `0a 0a` |
| Normalized post-repair identity | 38,509 | `3a0e8235b2a453c249ab9fd09894bc786833c33a985b1a65dfc4bd42db230985` | `0a` |

Relation proof: the post-repair byte sequence is exactly the first 38,509
bytes of the pre-repair sequence; the sole removed byte is its final `0x0a`.
No other file was changed by the normalization operation. Existing citations
inside preserved child records were not rewritten; citations to the pre-repair
SHA remain resolvable through this amendment.

This amendment changes no taint result, manager BLOCK verdict, lineage state,
packet/freeze/verifier state, execution authority, or execution effect.
