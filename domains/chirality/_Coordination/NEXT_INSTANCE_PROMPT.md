# NEXT INSTANCE PROMPT - Chirality DOMAIN_DECOMP

## Entry Protocol

1. Read `/Users/ryan/ai-env/projects/chirality/AGENTS.md`.
2. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DECOMP_BASE.md`.
3. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DOMAIN_DECOMP.md`.
4. Act in the `DOMAIN_DECOMP` persona for `/Users/ryan/ai-env/projects/chirality/domains/chirality`.
5. Read `/Users/ryan/ai-env/projects/chirality/skills/domain-source-atomize/SKILL.md` before any Phase 2 atomization work.
6. Read the current decomposition control and handoff surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Chirality_Domain_Decomposition.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE1.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/_LATEST_GATE2.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z/HANDOFF_STATE.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/phase2_batches/_LATEST_BATCH1_GATE2.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Validation_Checks.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Open_Issues_Register.csv`
7. Read the Chirality domain-pack source surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/README.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/domain-pack.yaml`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/SOURCE_BOUNDARY.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/Source_Manifest.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_LocalIndexes/_LATEST.md`
8. Run `git status --short` before coordination-sensitive planning or edits.

## Active Direction

Continue from accepted Gate 1 and accepted Batch 1 Gate 2.

Gate 2 for `BATCH1_BINDING_GOVERNANCE_20260614T011101Z` is **accepted**. Phase 2.5 source catalog, BM25 retrieval, and TOC-prior refresh are complete.

The accepted Batch 1 ledger is batch-scoped binding-governance decomposition truth for the selected 22 sources only. It is not full-corpus decomposition truth for all 242 manifest sources.

## Current Accepted Evidence

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z/`
- Gate 2 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z/`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- Accepted Batch 1 partial ledger: `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- Accepted Batch 1 partial ledger SHA-256: `ce781347e9417577127251a7ce713b1cfd9e3b7d27b54c98b270a775d1cf5bf8`
- Accepted vocabulary map: `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- Accepted vocabulary map SHA-256: `a428b77b2b2bcbe60500f6f91fffdf4543d84a9f8d886d32d43d7be23b3dc98e`
- Current source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T023650Z`
- Catalog schema: `chirality-source-db/v2`
- Source docs: `242`
- Artifacts: `485`
- Chunks: `12246`
- Chunk types: `MARKDOWN_SECTION=4523`, `SECTION_NODE=4449`, `LEDGER_ATOM=3274`
- Retrieval index status: `BM25_ONLY`
- Retrieval rows: `12246`
- Dense embeddings: `DEFERRED`
- Source-copy policy: `source_files_copied=false`
- TOC-prior matrix: `domains/chirality/_Decomposition/cross_source_toc_matrix.{md,csv}`

Run this validation first:

```sh
python3 tools/source_catalog/validate_source_database.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --domain-root domains/chirality \
  --repo-root .
```

Then confirm the smoke query if retrieval will be used:

```sh
python3 tools/retrieval/query_source_index.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --query "derivative-package rule" \
  --k 1
```

Expected rank 1 result: `@repo/AGENTS.md`.

## Batch 1 Accepted State

- batch ID: `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`
- selected sources: `22`
- dispatch units: `22`
- raw worker atom rows: `3276`
- merged atom rows: `3274`
- deduped duplicate hash rows: `2`
- IN rows after merge: `3262`
- OUT rows after merge: `12`
- TBD rows after merge: `0`
- merged vocabulary terms: `670`
- atom-review HTML files: `22`
- Gate 2 status: `ACCEPTED`
- Phase 2.5 status: `COMPLETE`

Primary Batch 1 outputs:

- `domains/chirality/_Decomposition/dispatch_outputs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_GATE2_HANDOFF.md`

## Source Model

Live repo files are source truth. Do not copy the 242 manifest source files into `_Sources/` as authoritative source snapshots.

Use `@repo/<RepoRelPath>` provenance for live repo files. Generated skeletons, dispatch plans, minimal asset manifests, section-node CSVs, review HTML, telemetry, ledgers, vocabulary maps, source catalogs, retrieval indexes, and TOC-prior matrices are derivative or companion artifacts, not source truth.

## Open Work

- `OI-005`: full 242-source atomization remains staged/incomplete; Batch 1 covers 22 sources.
- `OI-007`: accepted Batch 1 atoms do not yet have ratified Category/KTY/Knowledge Subject assignments.

Next valid DOMAIN_DECOMP actions are either:

- prepare batch-scoped Gate 3 Category/KTY/Knowledge Subject proposal surfaces from the accepted Batch 1 ledger and refreshed retrieval substrate; or
- stage the next Phase 2 atomization batch if the operator chooses continued source atomization first.

## Non-Goals

Do not start with:

- treating Batch 1 partial `Atomic_Domain_Ledger.csv` as full-corpus truth;
- dense embedding build as a prerequisite;
- copying live repo source files into `_Sources/` as authoritative source truth;
- final full-corpus Category, KTY, Knowledge Subject, or Atomic Domain Ledger truth;
- hypergraph generation;
- DBM publication;
- public export changes;
- treating generated catalog or retrieval snapshots as decomposition truth.

## Closeout

Report files created or changed, validation run, skipped checks and why, remaining human rulings, and whether Gate 1 and Batch 1 Gate 2 remain accepted after validation.
