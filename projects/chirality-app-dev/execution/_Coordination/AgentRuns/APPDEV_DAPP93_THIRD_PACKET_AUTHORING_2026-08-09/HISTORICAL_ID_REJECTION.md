# Historical command-identity rejection contract

The manager will scan the complete authored preparation scope
`packet/**`, `returns/N2_AUTHOR_RETURN.md`, and
`source_reconstruction/STAGE_5_COMMAND_AUTHORITY_LEDGER.csv`.

The scan is case-sensitive and must return zero matches for these historical
identity families:

- `C[0-9]{3,}`
- `A3-OP-[0-9]{3}`
- `R[0-9]+-C[0-9]{3,}`
- `ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+`

Paths are also scanned for the blocked-root basenames named in
`validation/HISTORICAL_ROOT_PRESERVATION.md`. A match rejects fan-in. The
fresh namespace is `L3-CMD-001` upward, contiguous with no gaps, duplicates,
aliases, inherited IDs, or external command-identity references.
