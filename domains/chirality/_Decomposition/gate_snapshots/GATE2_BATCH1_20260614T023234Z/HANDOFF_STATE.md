# Gate 2 Handoff State - Chirality DOMAIN_DECOMP Batch 1

Package role: snapshot / handoff artifact

Status: Gate 2 accepted for Batch 1; Phase 2.5 source catalog, retrieval, and TOC-prior refresh complete.

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Batch 1 atomization package: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- Batch 1 atomization handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_ATOMIZATION_HANDOFF.md`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- Accepted Batch 1 partial ledger: `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- Accepted Batch 1 partial ledger SHA-256: `ce781347e9417577127251a7ce713b1cfd9e3b7d27b54c98b270a775d1cf5bf8`
- Accepted Batch 1 vocabulary map: `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- Accepted Batch 1 vocabulary map SHA-256: `a428b77b2b2bcbe60500f6f91fffdf4543d84a9f8d886d32d43d7be23b3dc98e`

## Current Derived Retrieval Package

- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T023650Z`
- Catalog validation: PASS, 0 blockers, 0 warnings
- Catalog source docs: 242
- Catalog artifacts: 485
- Catalog chunks: 12246
- Catalog artifact roles include manifest source markdown, Batch 0 section-node CSVs, and Batch 1 `Atomic_Domain_Ledger.csv`.
- Searchable chunk types: `MARKDOWN_SECTION=4523`, `SECTION_NODE=4449`, `LEDGER_ATOM=3274`
- Retrieval index: `source_v2`
- Retrieval status: `BM25_ONLY`
- Retrieval rows: 12246
- Retrieval input chunks SHA-256: `8b23254265e80d1b21214d51c75b1472d68c5aaad76ea3d7015b331ab394c91b`
- Dense embeddings: deferred.
- Smoke query: `derivative-package rule` -> `@repo/AGENTS.md` rank 1.

## Current TOC-Prior Package

- TOC matrix Markdown: `domains/chirality/_Decomposition/cross_source_toc_matrix.md`
- TOC matrix Markdown SHA-256: `ecf5fcd007e79258cfe466e163bcfb7e489fe6e32215d7391f658e6b6806cfc1`
- TOC matrix CSV: `domains/chirality/_Decomposition/cross_source_toc_matrix.csv`
- TOC matrix CSV SHA-256: `afb903b1fc311ebe8123988a9932d71b336cfb0276039b6f7df41386d973f2a3`
- Scope: 22 accepted Batch 1 skeletons.
- Pair rows: 81.

## Derivative-Package Status

- `_LocalIndexes/snapshots/SRCIDX_20260614T023650Z` is a derived local catalog/retrieval package. It cites accepted Gate 1 source truth and accepted Batch 1 decomposition companions; it is not a substitute for decomposition truth.
- `cross_source_toc_matrix.{md,csv}` is a derived Batch 1 planning aid generated from accepted Batch 1 skeletons.
- Batch 1 per-unit CSVs, per-source ledgers, vocabulary seeds, atom-review HTML files, `Atomic_Domain_Ledger.csv`, and `Vocabulary_Map.csv` are accepted Phase 2 decomposition companions for the 22-source binding-governance batch only.
- Dense embeddings, category/KTY/subject truth, hypergraph snapshots, DBM publication packages, and public exports do not exist for this accepted state.

## Closure Verdict

- Gate 1 Intake: CLOSED / ACCEPTED.
- Batch 1 Phase 2 atomization: CLOSED / ACCEPTED.
- Phase 2.5 source catalog refresh: CLOSED / PASS.
- Phase 2.5 BM25 retrieval refresh: CLOSED / PASS.
- Phase 2.5 TOC-prior refresh: CLOSED / PASS.
- Gate 3 Categories / Knowledge Type / Knowledge Subject: NOT STARTED.

## Rerun Requirements

- If any manifest-backed source file changes, update `Source_Manifest.csv`, rebuild the source catalog, rebuild retrieval, and regenerate affected skeleton/dispatch/section-node companions before using retrieval as evidence.
- If `Atomic_Domain_Ledger.csv`, `Vocabulary_Map.csv`, or any source section-node CSV changes, rebuild the source catalog and retrieval index before Gate 3 work.
- If Batch 1 skeletons or source membership change, regenerate `cross_source_toc_matrix.{md,csv}` before category proposal work.
- If dense retrieval is required later, rebuild the retrieval index without `--no-embeddings` on the then-current accepted source catalog snapshot.

## Remaining Blockers And Next Action

- Full-corpus atomization remains incomplete: Batch 1 covers 22 of 242 manifest sources.
- Gate 3 category, knowledge-type, and subject proposal/evaluation has not started and must remain batch-scoped unless later batches are accepted.
- No hypergraph, DBM publication, or public export phase may treat this Batch 1 package as full-corpus truth.
- Next DOMAIN_DECOMP action is to prepare Batch 1 Gate 3 category/KTY/subject proposal surfaces from the accepted Batch 1 ledger and refreshed retrieval substrate, or to stage the next Phase 2 source batch if the operator chooses continued atomization first.
