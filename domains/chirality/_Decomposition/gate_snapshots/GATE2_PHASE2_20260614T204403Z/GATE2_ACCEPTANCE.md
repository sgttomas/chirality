# Gate 2 Acceptance - Chirality DOMAIN_DECOMP Phase 2

Package role: snapshot / handoff artifact

Gate: Gate 2 Atomization / Normalization

Scope: Active Phase 2 accepted source-unit set after Batch 1 carry-forward and Batches 2-6 closure

Status: ACCEPTED

Accepted UTC: 2026-06-14T20:44:03Z

Human confirmation:

```text
I approve Gate 2 closure.  Proceed accordingly.
```

## Accepted Atomization

- Domain root: `domains/chirality`
- Accepted Gate 1 snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Prior Batch 1 Gate 2 snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Current source manifest SHA-256: `6d9ea9bf796ab83a0e0e01fc5d0d24e095fcb6ce0bf6a6739d4f50fa0296509e`
- Accepted source-unit register: `domains/chirality/_Decomposition/Gate2_Source_Unit_Register.csv`
- Accepted source-unit register SHA-256: `2901efdbbebce5b58f152e1592d5ca4141b99f77fee15df24fa9786347b8e61e`
- Accepted canonical ledger: `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- Accepted canonical ledger SHA-256: `a7e28a2ff0902b4b86ad650c661612aa9bc413bc78213181570f93d64367e588`
- Accepted vocabulary map: `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- Accepted vocabulary map SHA-256: `5f48d0e49aecd92be36f4c149832237b6c7ff6a456c12ced35ab20c69c26a899`

## Accepted Source-Unit Scope

| Source-unit subset | Source units | Notes |
|---|---:|---|
| Batch 1 active carry-forward | 9 | Excludes 11 retired Batch 1 rows and excludes Batch 1 skill README/template rows superseded by `SRC-SKILLPACK-META`. |
| Batch 2 agent contracts | 36 | Regenerated active agent-contract batch excluding retired `AG013`. |
| Batch 3 governance/thesis context | 22 | Active `DG010`..`DG031` rows. |
| Batch 4 grouped skill packs | 38 | `SKP000`..`SKP037`; component-map SourceRefs cite original repo skill files. |
| Batch 5 work-surface registry | 4 | Human-directed registry sources for `domains/` and `projects/` work surfaces. |
| Batch 6 license | 1 | `SRC-LICENSE` / `RT005`. |
| **Total** | **110** | Accepted Phase 2 source-unit surface. |

## Accepted Ledger Telemetry

| Metric | Value |
|---|---:|
| Atom rows | 19473 |
| IN rows | 19403 |
| OUT rows | 20 |
| TBD rows | 50 |
| Accepted source units | 110 |
| Vocabulary terms | 2582 |
| Multi-source vocabulary terms | 556 |
| TOC-prior source-pair rows | 21964 |

## Grouped Skill-Pack Caveat

Batch 4 is accepted as grouped-source atomization for skill contracts. The file-level `Source_Manifest.csv` still records 153 individual `SKILL_CONTRACTS` rows, while Gate 2 accepts 38 grouped `SKP000`..`SKP037` source units backed by generated pack markdown and `source_components` maps in the Batch 4 asset manifests. SourceRefs cite original repo component files, not the generated pack markdown, when a component line is the source of the atom.

`OI-018` remains open as a governance note for workflows that require strict one-row-per-accepted-source manifest parity. Phase 3 may proceed from `Gate2_Source_Unit_Register.csv` as the accepted source-unit authority.

## Phase 2.5 Refresh Evidence

- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T204703Z`
- Catalog schema: `chirality-source-db/v2`
- Catalog validation: PASS, 0 blockers, 0 warnings
- Catalog source docs: 274
- Catalog artifacts: 500
- Catalog chunks: 29843
- Chunk types: `MARKDOWN_SECTION=4076`, `SECTION_NODE=6294`, `LEDGER_ATOM=19473`
- Retrieval status: `BM25_ONLY`
- Retrieval rows: 29843
- Retrieval smoke query: `derivative-package rule` returned `@repo/AGENTS.md` at rank 1.
- Dense embeddings: deferred, not built.
- TOC-prior matrix Markdown: `domains/chirality/_Decomposition/cross_source_toc_matrix.md`
- TOC-prior matrix Markdown SHA-256: `3aef6f8a82f75424d0511f47b81c17a7d4929623d198142483a6f65f8d6a52c1`
- TOC-prior matrix CSV: `domains/chirality/_Decomposition/cross_source_toc_matrix.csv`
- TOC-prior matrix CSV SHA-256: `05309d52d702162564daffb259f7ed5b1f709e1e0f22c3086a232836fa86dd03`

## Gate 2 Verdict

The accepted canonical Phase 2 ledger reflects the current source-unit set, the IN/OUT/TBD classifications are accepted for normalization, source bindings are accepted, and the vocabulary map is accepted as the Phase 2 vocabulary basis.

This acceptance closes Gate 2 normalization. It does not create Category, Knowledge Type, Knowledge Subject, hypergraph, DBM publication, dense embedding, or public export truth.
