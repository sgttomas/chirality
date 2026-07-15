# VERIFY-B2 Pre-freeze Mechanical Rebinding

Before terminal freeze, the inherited five-member verifier harness emitted the
correct three member records, mappings, source-line totals, and per-member
probe results, but retained two aggregate constants from its template:
`members_complete=5` and `fail_closed_probes=35`. This was a generated
verifier-evidence binding defect only. It did not affect any candidate, live
project path, source review, deterministic tool output, or per-member result.

The wrapper was narrowed to derive both aggregate values from the exact frozen
three-member `EXPECTED` set and the complete seven probes per member. The
verifier was then rerun in full; no prior output was accepted as terminal.

Pre-rebinding generated evidence hashes:

- `BATCH_RESULTS.json`: `2fb1dbc43897274a1bfbd0c1d95b472e7fd260d888ffefcb373fa028fc8f8bbc`
- `RUNTIME_EVENTS.jsonl`: `d710dbc12cd04c68d266ff8809ea4437e5b5b880906ecfe5c1c0e3e2ef7d2503`
- `PROGRESS.tsv`: `58335fd5a3af44e9b9768237021a9d9ad65c1b8a012ef62c072142bca60727b5`

Classification: `SAFE_MECHANICAL_VERIFIER_EVIDENCE_REBINDING`; candidate
repair, project repair, semantic repair, waiver, and omitted checkpoint: zero.

The first full-rerun invocation then failed before member execution because the
accepted harness deliberately creates each verifier member directory with
`exist_ok=false`, and the prior generated directories had not yet been removed.
Its partial `RUNTIME_EVENTS.jsonl` hash was
`652ccf105e8112ac82404b0ee0e7c5d6d9f72c63f209b196909cc8c5ebd38ae2`;
the unchanged `PROGRESS.tsv` hash remained
`58335fd5a3af44e9b9768237021a9d9ad65c1b8a012ef62c072142bca60727b5`.
The disposable generated verifier outputs were cleared within this verifier's
exclusive write scope, then the full run was restarted from member one. This
is an execution-substrate retry, not a candidate or semantic repair.

The first closure-finalizer invocation produced the correct 15 forward rows,
15 inverse rows, and three simulations, then stopped at its inherited
five-member aggregate assertion. The exact partial-output hashes were:

- `REPLACEMENT_ROWS.tsv`: `fbf7f2c23c67273b8618b75eb26b3b47961563da8830f4e1ceec2bd41d2bcb5e`
- `INVERSE_ROWS.tsv`: `a4ffaebb2a10056016bf4fcb9b9295cc61340f75348b010308524389029b2012`
- `SIMULATIONS.tsv`: `cb965a754eb1386c6624b69a33ccb58e34b5f8208720f5edb1f39776ebd4562e`

The finalizer wrapper was rebound to exact Batch-2 counts and the `VERIFY-B2`
identity, then rerun in full. This second mechanical binding correction also
changed no candidate or project byte and waived no check.
