# Gate 2 Handoff State - Chirality DOMAIN_DECOMP Phase 2

Package role: snapshot / handoff artifact

Status: Gate 2 accepted for the active Phase 2 source-unit set; Phase 2.5 source catalog, BM25 retrieval, and TOC-prior refresh complete.

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Prior Batch 1 Gate 2 snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z`
- Gate 2 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`
- Source manifest SHA-256: `6d9ea9bf796ab83a0e0e01fc5d0d24e095fcb6ce0bf6a6739d4f50fa0296509e`
- Accepted source-unit register SHA-256: `2901efdbbebce5b58f152e1592d5ca4141b99f77fee15df24fa9786347b8e61e`
- Accepted canonical ledger SHA-256: `a7e28a2ff0902b4b86ad650c661612aa9bc413bc78213181570f93d64367e588`
- Accepted vocabulary map SHA-256: `5f48d0e49aecd92be36f4c149832237b6c7ff6a456c12ced35ab20c69c26a899`

## Current Derived Retrieval Package

- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z`
- Catalog validation: PASS, 0 blockers, 0 warnings
- Catalog source docs: 274
- Catalog artifacts: 500
- Catalog chunks: 29843
- Searchable chunk types: `MARKDOWN_SECTION=4076`, `SECTION_NODE=6294`, `LEDGER_ATOM=19473`
- Retrieval index: `source_v2`
- Retrieval status: `BM25_ONLY`
- Dense embeddings: deferred.
- Smoke query: `derivative-package rule` -> `@repo/AGENTS.md` rank 1.

## Current TOC-Prior Package

- TOC matrix Markdown: `domains/chirality/_Decomposition/cross_source_toc_matrix.md`
- TOC matrix Markdown SHA-256: `3aef6f8a82f75424d0511f47b81c17a7d4929623d198142483a6f65f8d6a52c1`
- TOC matrix CSV: `domains/chirality/_Decomposition/cross_source_toc_matrix.csv`
- TOC matrix CSV SHA-256: `05309d52d702162564daffb259f7ed5b1f709e1e0f22c3086a232836fa86dd03`
- Scope: 110 accepted Gate 2 source-unit skeletons.
- Pair rows: 21964.

## Derivative-Package Status

- `_LocalIndexes/snapshots/SRCIDX_20260614T204703Z` is a derived local catalog/retrieval package. It cites accepted Gate 2 ledger/vocabulary/source-unit truth and is not a substitute for decomposition truth.
- `cross_source_toc_matrix.{md,csv}` is a derived planning aid generated from accepted Gate 2 source-unit skeletons.
- Batch-scoped ledgers and vocab maps for Batches 2-6 remain supporting evidence. The canonical accepted Phase 2 truth is `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, and `Gate2_Source_Unit_Register.csv` as snapshotted here.
- Dense embeddings, category/KTY/subject truth, hypergraph snapshots, DBM publication packages, and public exports do not exist for this accepted state.

## Closure Verdict

- Gate 1 Intake: CLOSED / ACCEPTED, with later source-boundary cleanup recorded.
- Gate 2 Phase 2 normalization: CLOSED / ACCEPTED.
- Phase 2.5 source catalog refresh: CLOSED / PASS.
- Phase 2.5 BM25 retrieval refresh: CLOSED / PASS.
- Phase 2.5 TOC-prior refresh: CLOSED / PASS.
- Gate 3 Categories: NOT STARTED.
- Gate 4 Knowledge Types: NOT STARTED.
- Gate 5 Coverage: NOT STARTED.
- Gate 6 Publish: NOT STARTED.

## Rerun Requirements

- If any accepted source file or grouped-source component file changes, update the source manifest or grouped component map, regenerate affected skeleton/dispatch/review companions, rerun affected atomization units, merge the canonical ledger/vocabulary, and rebuild the source catalog and retrieval index.
- If `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, `Gate2_Source_Unit_Register.csv`, or any accepted source section-node CSV changes, rebuild the source catalog and BM25 index before retrieval-driven Gate 3 work.
- If source membership or source-unit grouping changes, regenerate `cross_source_toc_matrix.{md,csv}` before category proposal work.
- If dense retrieval is required later, rebuild the retrieval index without `--no-embeddings` on the then-current accepted source catalog snapshot.

## Remaining Blockers And Next Action

- `OI-018` remains open as a governance note for grouped skill-pack source-unit parity with the file-level manifest. It does not block Phase 3 if Phase 3 consumes `Gate2_Source_Unit_Register.csv` as source-unit authority.
- Category, Knowledge Type, and Knowledge Subject proposal/evaluation has not started.
- No hypergraph, DBM publication, dense embedding, or public export phase may treat this package as beyond Gate 2 truth.
- Next DOMAIN_DECOMP action is Phase 3 category proposal and retrieval-driven ratification from the accepted Gate 2 ledger, vocabulary, TOC prior, and source catalog snapshot.
