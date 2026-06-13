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

Continue from:

`/Users/ryan/ai-env/projects/chirality/plans/chirality_domain_decomp_readiness_2026-06-13.md`

Current scope is DOMAIN_DECOMP startup only:

- accept and revalidate the retrieval-first upstream evidence;
- implement Batch 0, the manifest-backed Markdown adapter and Gate-1 preflight;
- produce intake telemetry and a Gate 1 confirmation packet for the human;
- do not run full Phase 2 atomization until Gate 1 and the adapter SourceRef policy are accepted.

## Current Accepted Evidence

Use the readiness plan as the authoritative handoff for exact hashes and counts. The current accepted evidence, subject to fresh validation at run start, is:

- source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- source manifest SHA-256: `507201a0e5bad74d6e97fc771a37065ea3f8903332b231cd4eff35081634c920`
- source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260613T232620Z`
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

## Batch 0 Work

Create the manifest-backed DOMAIN_DECOMP adapter layer under:

`/Users/ryan/ai-env/projects/chirality/domains/chirality/_Decomposition/`

Produce, at minimum:

- `Chirality_Domain_Decomposition.md`
- `Source_Decomp_Prefix_Map.csv`
- `source_asset_manifests/*.json`
- `source_skeletons/*_skeleton.json`
- `source_dispatch_plans/*_dispatch_plan.json`
- `source_review_html/*.html`
- `source_section_nodes/*_section_nodes.csv`
- intake telemetry and open-issue records

Use explicit stable unique source prefixes. Recommended families:

- `RT001...` for root docs
- `DG001...` for root governance docs
- `AG001...` for agent contracts
- `SK001...` for skill contracts
- `TL001...` for tool registry docs
- `HX001...` for harness/export docs

Handle `LICENSE.md` explicitly. It is headingless and will fail `tools/decomp/build_source_skeleton.py` unless deferred or adapted. Do not silently skip it.

## Adapter Rules

Minimal asset manifests are authoritative decomposition companions for Markdown-only source handling, not source truth. Each should include at least:

```json
{
  "doc_stem": "<SourceDocID or stable source name>",
  "source_doc_id": "<SourceDocID>",
  "repo_rel_path": "<RepoRelPath>",
  "catalog_rel_path": "@repo/<RepoRelPath>",
  "source_manifest_sha256": "507201a0e5bad74d6e97fc771a37065ea3f8903332b231cd4eff35081634c920",
  "assets": [],
  "pages": []
}
```

Before atomization, propose and ask the human to accept this SourceRef form:

```text
@repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

If existing tooling requires the older `<book>.md:L####|<book>.html#anchor` form, surface that as an adapter issue and propose the smallest safe change. Do not proceed to atomization until this is resolved.

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

## Non-Goals

Do not start with:

- full unbatched atomization of all 242 files;
- `TASK + domain-source-atomize` fan-out before Gate 1 acceptance;
- dense embedding build as a prerequisite;
- copying live repo source files into `_Sources/` as authoritative source truth;
- final Category, KTY, Knowledge Subject, or Atomic Domain Ledger truth;
- hypergraph generation;
- DBM publication;
- public export changes;
- treating generated catalog or retrieval snapshots as decomposition truth.

## Gate 1 Output

End Batch 0 by presenting a Gate 1 confirmation packet containing:

- accepted source manifest and catalog snapshot;
- validation result;
- source-prefix map summary;
- source counts by group;
- skeleton count and failures;
- dispatch-unit counts by group;
- deferred-source decisions;
- `LICENSE.md` disposition;
- SourceRef adapter recommendation;
- companion inventory;
- open issues and required human rulings.

Use this Gate 1 confirmation language:

```text
The manifest-backed source set, source-prefix map, skeleton inventory, and deferred-source decisions are accepted as the intended Chirality DOMAIN_DECOMP intake.
```

Do not mark Gate 1 closed unless the human explicitly confirms.

## Closeout

Report:

- files created or changed;
- validation run;
- skipped checks and why;
- remaining human rulings;
- whether Gate 1 is awaiting acceptance or accepted;
- next action for Phase 2 setup.

Do not commit unless the human explicitly asks.
