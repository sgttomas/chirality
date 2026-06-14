# Batch 1 Atomization Handoff - Binding Governance Seed

Package role: snapshot / handoff artifact

BatchID: `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`

Status: FAN_OUT_AND_FAN_IN_COMPLETE_GATE2_OPEN

Generated UTC: 2026-06-14T02:28:00Z

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T005449Z`
- Retrieval status: `BM25_ONLY`
- Source-copy policy: `source_files_copied=false`

## Produced Companions

Batch 1 produced the Phase 2 atomization companions for 22 binding-governance sources:

| Metric | Value |
|---|---:|
| Selected sources | 22 |
| Dispatch units | 22 |
| Per-unit atom CSVs | 22 |
| Per-unit vocabulary CSVs | 22 |
| Raw worker atom rows | 3276 |
| Per-source merged atom rows | 3274 |
| Deduped duplicate hash rows | 2 |
| IN rows after merge | 3262 |
| OUT rows after merge | 12 |
| TBD rows after merge | 0 |
| Per-source ledgers | 22 |
| Per-source vocabulary seed files | 22 |
| Raw vocabulary seed rows | 830 |
| Merged vocabulary terms | 670 |
| Atom-review HTML files rendered | 22 |

The two deduped rows occurred during the per-source merge for `SRC-DOCS-DIRECTIVE`, where duplicate `ContentHash` rows were collapsed by `tools/decomp/merge_source_atomizations.py`.

## Validation Evidence

- Source catalog validation: `PASS` against `SRCIDX_20260614T005449Z`.
- BM25 smoke query: `derivative-package rule` returned `@repo/AGENTS.md` at rank 1.
- Per-unit QA: `PASS` for all 22 dispatch units; checks covered exact headers, `ContentHash`, `LocalSeq`, `InOutStatus`, `DispatchUnitID`, target `SectionID`, repo-backed `SourceRef`, and line-range bounds.
- Per-source merge: `PASS` for all 22 selected sources with `--strict-coverage`.
- Cross-source merge: `PASS`, `rows=3274`, `unresolved_corrects=0`.
- Vocabulary merge: `PASS`, `terms=670`, `multi_source=115`.
- Atom-review render: `PASS` for all 22 selected sources.

## Derivative-Package Status

The generated per-unit CSVs, per-source ledgers, `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, and atom-review HTML surfaces are Phase 2 decomposition companion artifacts ready for Gate 2 review. They are not a substitute for human-accepted decomposition truth.

`Atomic_Domain_Ledger.csv` is a Batch 1 partial ledger over the binding-governance source set only. It does not cover the full 242-source manifest-backed corpus.

## Closure Verdict

- Gate 1 Intake: CLOSED / ACCEPTED, unchanged.
- Batch 1 setup: CLOSED / SETUP_READY.
- Batch 1 Phase 2 worker fan-out: CLOSED / SUCCESS.
- Batch 1 deterministic fan-in: CLOSED / SUCCESS.
- Gate 2 normalization: OPEN / NOT_ACCEPTED.

No Category, Knowledge Type, Knowledge Subject, hypergraph, DBM publication, dense embedding refresh, or public export work was performed.

## Rerun Requirements

- If any selected source file changes, update `Source_Manifest.csv`, rebuild the source catalog and BM25 index, regenerate Batch 0 companions, regenerate Batch 1 briefs, rerun Batch 1 workers, and rerun fan-in.
- If `tools/decomp/build_atomization_brief.py`, `tools/decomp/merge_source_atomizations.py`, `tools/decomp/merge_vocabulary_seeds.py`, `Source_Decomp_Prefix_Map.csv`, or `skills/domain-source-atomize/` changes, rerun the affected briefs/workers and fan-in before Gate 2 review.
- If a human flags atomization errors in the atom-review HTML, rerun or manually repair only the affected dispatch units, then rerun per-source merge, cross-source merge, vocabulary merge if needed, and atom-review render.
- Rebuild the source database and retrieval index in Phase 2.5 only after Gate 2 normalization is accepted or after an explicit operator decision to index a review-only partial ledger.

## Remaining Blockers

- Human Gate 2 review is required for the 22 atom-review HTML files under `domains/chirality/_Decomposition/source_review_html/`.
- Gate 2 remains open until the human confirms the merged Batch 1 ledger, IN/OUT/TBD classifications, atom boundaries, and vocabulary choices are acceptable or returns flags for correction.
- No Phase 2.5 retrieval refresh, Phase 3 category proposal, or downstream decomposition publication should consume this Batch 1 output as accepted truth before Gate 2 closes.
