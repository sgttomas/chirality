# NEXT INSTANCE PROMPT - Chirality DOMAIN_DECOMP

## Entry Protocol

1. Read `/Users/ryan/ai-env/projects/chirality/AGENTS.md`.
2. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DECOMP_BASE.md`.
3. Read `/Users/ryan/ai-env/projects/chirality/agents/AGENT_DOMAIN_DECOMP.md`.
4. Act in the `DOMAIN_DECOMP` persona for `/Users/ryan/ai-env/projects/chirality/domains/chirality`.
5. Read `/Users/ryan/ai-env/projects/chirality/skills/domain-source-atomize/SKILL.md`.
6. Read `/Users/ryan/ai-env/projects/chirality/plans/chirality_domain_decomp_readiness_2026-06-13.md`.
7. Read the Chirality domain-pack surfaces:
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/README.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/domain-pack.yaml`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/SOURCE_BOUNDARY.md`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_Sources/Source_Manifest.csv`
   - `/Users/ryan/ai-env/projects/chirality/domains/chirality/_LocalIndexes/_LATEST.md`
8. Run `git status --short` before coordination-sensitive planning or edits.

## Active Direction

Continue from the accepted Gate 1 package:

`/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/Chirality_Domain_Decomposition.md`

Batch 0 is complete, Gate 1 is accepted, and Batch 1 binding-governance setup is ready at `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`. Resume at explicit staged Batch 1 worker fan-out only if the human asks for it; otherwise keep planning and validation staged. Do not run full unbatched atomization of all 242 files.

Before any Phase 2 worker dispatch, re-run validation, confirm the accepted Gate 1 snapshot still matches the working package, verify the rendered Batch 1 briefs under `domains/chirality/_Decomposition/dispatch_briefs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/` still contain repo-backed `SOURCE_REF_BASE`, and keep dispatches staged.

## Current Accepted Evidence

Use the Gate 1 acceptance snapshot as the authoritative handoff for exact hashes and counts. The current accepted evidence, subject to fresh validation at run start, is:

- source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T005449Z`
- catalog schema: `chirality-source-db/v2`
- artifact count: `242`
- source doc count: `242`
- chunk count: `4523`
- retrieval index status: `BM25_ONLY`
- source-copy policy: `source_files_copied=false`

Run this first:

```sh
python3 tools/source_catalog/validate_source_database.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --domain-root domains/chirality \
  --repo-root .
```

If validation fails, stop and repair or report the blocker before proceeding. If manifest hashes have drifted, rebuild the source catalog and BM25 index before using retrieval as evidence.

## Source Model

Live repo files are source truth. The `domains/chirality/` pack records manifest membership, hashes, local derived indexes, and later decomposition artifacts.

Do not copy the 242 manifest source files into `_Sources/` as authoritative source snapshots.

Use `@repo/<RepoRelPath>` provenance for live repo files. Generated skeletons, dispatch plans, minimal asset manifests, section-node CSVs, review HTML, telemetry, and future ledgers are decomposition companion artifacts, not source truth.

## Accepted Batch 0 State

The manifest-backed DOMAIN_DECOMP adapter layer exists under:

`/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/`

Accepted Batch 0 companions include:

- `Chirality_Domain_Decomposition.md`
- `Source_Decomp_Prefix_Map.csv`
- `source_asset_manifests/*.json`
- `source_skeletons/*_skeleton.json`
- `source_dispatch_plans/*_dispatch_plan.json`
- `source_review_html/*.html`
- `source_section_nodes/*_section_nodes.csv`
- intake telemetry and open-issue records
- Gate 1 acceptance snapshot: `_Decomposition/gate_snapshots/GATE1_20260614T005942Z/`

Telemetry:

- sources: `242`
- skeletons: `242`
- review HTML files: `242`
- section-node CSVs: `242`
- total sections: `4449`
- in-scope sections: `4446`
- dispatch units: `242`
- deferred sources: `1`
- failures: `0`

Accepted dispositions:

- `SRC-LICENSE` remains `AtomizeInV1=NO`, `InOutDefault=OUT`, and has no Phase 2 dispatch unless the human later changes the source-boundary decision.
- `SRC-DOCS-THESIS-GLOSSARY` is in scope and has one dispatch unit.
- Repo-backed SourceRefs are accepted for Phase 2.
- Per-kind asset surfaces are N/A for Markdown-only manifest rows.

## Adapter Rules

Minimal asset manifests are authoritative decomposition companions for Markdown-only source handling, not source truth.

Use this accepted SourceRef form for atomization:

```text
@repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

`tools/decomp/build_atomization_brief.py` emits `SOURCE_REF_BASE` from `Source_Decomp_Prefix_Map.csv`.

Gate 1.5 asset surfaces (`equations.html`, `figures.html`, `tables.html`, `images.html`, `folios.html`) are `N/A` for this Markdown-only manifest unless a later source row has an asset manifest with actual assets. The section/atom review HTML remains required.

## Retrieval Use

Use the accepted BM25-only index for source discovery and scope checks during startup. Dense embeddings are optional later and are not a blocker for Batch 0.

Example query:

```sh
python3 tools/retrieval/query_source_index.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --query "derivative-package rule" \
  --k 10
```

## Current Phase 2 Batch 1 Setup

Batch 1 setup is ready but worker fan-out is not started.

- batch ID: `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`
- setup handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_SETUP.md`
- source register: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/Batch_Source_Register.csv`
- dispatch unit register: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/Dispatch_Unit_Register.csv`
- validation register: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/Validation_Checks.csv`
- dispatch briefs root: `domains/chirality/_Decomposition/dispatch_briefs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- reserved output root: `domains/chirality/_Decomposition/dispatch_outputs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`
- selected sources: `22`
- dispatch units: `22`
- rendered briefs: `22`
- atomization status: `NOT_RUN`

No per-unit atom CSVs, per-source ledgers, cross-source `Atomic_Domain_Ledger.csv`, or `Vocabulary_Map.csv` have been produced for Batch 1 yet.

## Non-Goals

Do not start with:

- full unbatched atomization of all 242 files;
- `TASK + domain-source-atomize` fan-out outside an explicitly selected staged batch and explicit human authorization;
- dense embedding build as a prerequisite;
- copying live repo source files into `_Sources/` as authoritative source truth;
- final Category, KTY, Knowledge Subject, or Atomic Domain Ledger truth;
- hypergraph generation;
- DBM publication;
- public export changes;
- treating generated catalog or retrieval snapshots as decomposition truth.

## Gate 1 Status

Gate 1 is accepted. The acceptance snapshot is:

`domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z/`

Do not reopen Gate 1 unless source manifest membership, source hashes, skeleton inventory, or deferred-source decisions change.

## Closeout

Report:

- files created or changed;
- validation run;
- skipped checks and why;
- remaining human rulings;
- whether Gate 1 remains accepted after validation;
- next action for Phase 2 setup or explicitly authorized Batch 1 worker fan-out.

Do not commit unless the human explicitly asks.
