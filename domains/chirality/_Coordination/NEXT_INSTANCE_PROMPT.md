# NEXT INSTANCE PROMPT - Chirality DOMAIN_DECOMP

## Entry Protocol

1. Read `/Users/ryan/ai-env/projects/chirality/AGENTS.md`.
2. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DECOMP_BASE.md`.
3. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DOMAIN_DECOMP.md`.
4. Act in the `DOMAIN_DECOMP` persona for `/Users/ryan/ai-env/projects/chirality/domains/chirality`.
5. Read `/Users/ryan/ai-env/projects/chirality/skills/domain-source-atomize/SKILL.md`.
6. Read `/Users/ryan/ai-env/projects/chirality/plans/chirality_domain_decomp_readiness_2026-06-13.md`.
7. Read the current decomposition control and handoff surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Chirality_Domain_Decomposition.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/phase2_batches/_LATEST_BATCH1_ATOMIZATION.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_ATOMIZATION_HANDOFF.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Validation_Checks.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Open_Issues_Register.csv`
8. Read the Chirality domain-pack source surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/README.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/domain-pack.yaml`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/SOURCE_BOUNDARY.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/Source_Manifest.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_LocalIndexes/_LATEST.md`
9. Run `git status --short` before coordination-sensitive planning or edits.

## Active Direction

Continue from the accepted Gate 1 package and the completed Batch 1 Phase 2 fan-out/fan-in state.

Gate 1 is accepted. Batch 1 binding-governance atomization is complete and ready for Gate 2 review. Gate 2 is **open / not accepted**.

Do not proceed to Phase 2.5 retrieval refresh, Phase 3 Categories, KTYs, hypergraph generation, DBM publication, or public export from the Batch 1 ledger as accepted truth until the human explicitly accepts Gate 2 or returns review flags for repair.

## Current Accepted Evidence

Use the Gate 1 acceptance snapshot as the authoritative upstream handoff:

- source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T005449Z`
- catalog schema: `chirality-source-db/v2`
- artifact count: `242`
- source doc count: `242`
- chunk count: `4523`
- retrieval index status: `BM25_ONLY`
- source-copy policy: `source_files_copied=false`
- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z/`

Run this first:

```sh
python3 tools/source_catalog/validate_source_database.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --domain-root domains/chirality \
  --repo-root .
```

If validation fails, stop and repair or report the blocker before proceeding. If manifest hashes have drifted, rebuild the source catalog and BM25 index before using retrieval as evidence.

## Source Model

Live repo files are source truth. The `domains/chirality/` pack records manifest membership, hashes, local derived indexes, and decomposition artifacts.

Do not copy the 242 manifest source files into `_Sources/` as authoritative source snapshots.

Use `@repo/<RepoRelPath>` provenance for live repo files. Generated skeletons, dispatch plans, minimal asset manifests, section-node CSVs, review HTML, telemetry, ledgers, and vocabulary maps are decomposition companion artifacts, not source truth.

## Accepted Batch 0 State

Accepted Batch 0 companions live under:

`/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/`

Accepted dispositions:

- `SRC-LICENSE` remains `AtomizeInV1=NO`, `InOutDefault=OUT`, and has no Phase 2 dispatch unless the human later changes the source-boundary decision.
- `SRC-DOCS-THESIS-GLOSSARY` is in scope and has one dispatch unit.
- Repo-backed SourceRefs are accepted for Phase 2.
- Per-kind asset surfaces are N/A for Markdown-only manifest rows.

## SourceRef Policy

The accepted SourceRef form for atomization is:

```text
@repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

`tools/decomp/build_atomization_brief.py` emits `SOURCE_REF_BASE` from `Source_Decomp_Prefix_Map.csv`.

## Batch 1 Current State

- batch ID: `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`
- handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_ATOMIZATION_HANDOFF.md`
- pointer: `domains/chirality/_Decomposition/phase2_batches/_LATEST_BATCH1_ATOMIZATION.md`
- selected sources: `22`
- dispatch units: `22`
- per-unit atom CSVs: `22`
- per-unit vocabulary CSVs: `22`
- raw worker atom rows: `3276`
- merged atom rows: `3274`
- deduped duplicate hash rows: `2`
- IN rows after merge: `3262`
- OUT rows after merge: `12`
- TBD rows after merge: `0`
- per-source ledgers: `22`
- raw vocabulary seed rows: `830`
- merged vocabulary terms: `670`
- atom-review HTML files: `22`
- Gate 2 status: `OPEN / NOT_ACCEPTED`

Primary Batch 1 outputs:

- `domains/chirality/_Decomposition/dispatch_outputs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`
- `domains/chirality/_Decomposition/Vocabulary_Map.csv`
- `domains/chirality/_Decomposition/source_review_html/<Batch1 SourceDocID>.html`
- `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/Dispatch_Run_Log.csv`

## Validation Evidence

Latest recorded checks:

- source database validation: `PASS` against `SRCIDX_20260614T005449Z`
- BM25 smoke query `derivative-package rule`: `@repo/AGENTS.md` rank 1
- per-unit QA: `PASS` for all 22 units
- per-source merge: `PASS` with strict coverage
- cross-source merge: `PASS`, `rows=3274`, `unresolved_corrects=0`
- vocabulary merge: `PASS`, `terms=670`, `multi_source=115`
- atom-review render: `PASS`, `22` files

## Required Next Human Ruling

Gate 2 remains open until the human reviews the 22 Batch 1 atom-review HTML files and confirms or returns flags.

The Gate 2 confirmation should be explicit and batch-scoped, for example:

```text
The Batch 1 merged Domain Ledger reflects the selected binding-governance corpus content, the IN/OUT/TBD classifications are correct, the cleaning rule was applied correctly, and the vocabulary choices are acceptable.
```

If the human returns flags, repair only the affected source/dispatch unit, then rerun per-source merge, cross-source merge, vocabulary merge if affected, atom-review render, and validation.

## Non-Goals

Do not start with:

- full unbatched atomization of all 242 files;
- treating Batch 1 partial `Atomic_Domain_Ledger.csv` as full-corpus truth;
- Gate 2 closure without explicit human review;
- dense embedding build as a prerequisite;
- copying live repo source files into `_Sources/` as authoritative source truth;
- final Category, KTY, Knowledge Subject, or full Atomic Domain Ledger truth;
- hypergraph generation;
- DBM publication;
- public export changes;
- treating generated catalog or retrieval snapshots as decomposition truth.

## Closeout

Report:

- files created or changed;
- validation run;
- skipped checks and why;
- remaining human rulings;
- whether Gate 1 remains accepted after validation;
- whether Gate 2 remains open or has been explicitly accepted.
