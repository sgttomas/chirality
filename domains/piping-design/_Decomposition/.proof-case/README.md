# Proof-case Gate-1 dry run (2026-05-16)

Deterministic outputs from the revised DOMAIN_DECOMP v2 workflow, run end-to-end
on the 5-source piping-design corpus that existed at commit `edc3e716`
(`domain-decomp: rewrite AGENT_DOMAIN_DECOMP.md doctrine for scale`).

**Status: archived. Not the start of the next decomposition.**

The corpus is being expanded with new source materials; the actual fresh-
decomposition run will operate on a different source set, so these artifacts
are quarantined here rather than treated as Gate-1 close.

## Contents

| Artifact | Origin |
|---|---|
| `<book>_skeleton.json` (×5) | `tools/decomp/build_source_skeleton.py` |
| `<book>_dispatch_plan.json` (×5) | `tools/decomp/build_source_skeleton.py` |
| `<book>_section_nodes.csv` (×5) | `tools/decomp/render_source_html.py --mode structure` |
| `_atomization_work/<book>/` (×5) | Empty Phase-2 dispatch scratch dirs |

Per-source `<book>.html` review surfaces were also rendered but written under
`_Sources/<book>/audit/<book>.html`; those files were removed when this
proof-case was archived. The existing `equations.html` audit artifacts were
preserved verbatim.

## What this proved

- All 8 deterministic tools (`tools/decomp/*` + `tools/retrieval/*` extensions)
  run end-to-end on every source.
- Per-source dispatch plans cluster correctly within the `--budget-tokens`
  (15000) target (22 units MWK_1956, 13 units Piping_Manual, 12 units
  Process-Piping-Design-Rip-Weaver-Volume-1, 6 units
  Process-Piping-Design-Rip-Weaver-Volume-2, 23 units
  Pipe-Stress-Engineering — 76 total).
- SOURCE_PREFIX auto-derivation yielded unique prefixes across the corpus
  (`M1956`, `PM`, `PPDRWV1`, `PPDRWV2`, `PSE`).
- Output is byte-identical on reruns with the same inputs.
- The `domain-source-atomize` skill was smoke-tested via TASK dispatch
  against UNIT-PSE-0014 (20 atoms, 17 vocab seeds, all QA invariants pass,
  round-trips through the per-source merge tool to assigned stable
  `HBA-PSE-00001..00020` IDs).
- The audit-pattern HTML render correctly preserves prior equation review
  state (MWK_1956: 28/28 verified equations + 9/9 flagged equations carried
  through via the hash-based fallback in `build_eq_hash_index`).

## To start the real Phase 1

1. Finalize the source set under `_Sources/`.
2. From the package root run `tools/decomp/build_source_skeleton.py` per
   source, writing to `_Decomposition/` (NOT `.proof-case/`).
3. Run `tools/decomp/render_source_html.py --mode structure` per source.
4. Proceed to Phase 1.5 browser review.

The artifacts in this folder MUST NOT be referenced by the real run —
their `SOURCE_PREFIX` values and section counts are specific to the 5-source
corpus that existed at this snapshot.
