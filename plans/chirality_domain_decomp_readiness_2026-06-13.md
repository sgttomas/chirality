# Chirality Domain Decomposition Readiness Plan

Date: 2026-06-13

Repository root: `/Users/ryan/ai-env/projects/chirality`

Target domain root: `/Users/ryan/ai-env/projects/chirality/domains/chirality`

Status: handoff plan for the next `DOMAIN_DECOMP` agent instance. This plan completes the current session's scope only: accept the retrieval-first upstream evidence and define the readiness/run plan for the next agent. It does not run atomization, create category/KTY registers, create an atom ledger, or close any DOMAIN_DECOMP gate.

Package role: planning handoff artifact. It does not supersede `AGENTS.md`, `agents/AGENT_DOMAIN_DECOMP.md`, `agents/AGENT_DECOMP_BASE.md`, `docs/SPEC.md`, `docs/TYPES.md`, or future accepted decomposition snapshots.

## Executive Summary

The `domains/chirality/` retrieval milestone is ready to serve as upstream evidence for a `DOMAIN_DECOMP` run, with one important adapter decision: the domain pack uses manifest-backed live repo files as source truth, while `DOMAIN_DECOMP` tooling was originally shaped around copied handbook-style `_Sources/<book>/<book>.md` inputs with asset manifests.

The next logical agent should start as `DOMAIN_DECOMP`, but its first work is a bounded Phase 1/Phase 2 setup pass:

1. Reconfirm the accepted manifest and retrieval snapshot.
2. Generate a manifest-backed Markdown adapter layer for skeletons, dispatch plans, empty asset manifests, source-prefix assignment, and review surfaces.
3. Present Gate 1 intake for human confirmation.
4. Prepare, but do not launch blindly, Phase 2 `TASK + domain-source-atomize` fan-out.

All 242 manifest rows are admitted for the Chirality self-domain v1, but they should be processed in staged authority batches so human gates remain reviewable.

## Accepted Upstream Evidence

The following upstream evidence is accepted as the current retrieval input for the next `DOMAIN_DECOMP` agent, conditional on a fresh validation check at run start.

| Surface | Path / value | Status |
|---|---|---|
| Domain source boundary | `domains/chirality/_Sources/SOURCE_BOUNDARY.md` | Accepted as v1 source-scope statement |
| Domain source manifest | `domains/chirality/_Sources/Source_Manifest.csv` | Accepted as v1 corpus membership |
| Source manifest SHA-256 | `507201a0e5bad74d6e97fc771a37065ea3f8903332b231cd4eff35081634c920` | Current as of this plan |
| Domain pack metadata | `domains/chirality/domain-pack.yaml` | Present |
| Latest source catalog pointer | `domains/chirality/_LocalIndexes/_LATEST.md` | Points to accepted snapshot |
| Accepted source catalog snapshot | `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260613T232620Z` | Validated |
| Catalog schema | `chirality-source-db/v2` | Validated |
| Artifact count | `242` | Matches manifest row count |
| Source document count | `242` | One source doc per manifest row |
| Chunk count | `4523` | Markdown chunks only |
| Source files copied | `false` | Required retrieval invariant |
| Artifact CSV SHA-256 | `0fabe04f63babfac51b2b5c486b257639e92ecb2e29f1033cf2dd52e28296546` | Recorded in snapshot metadata |
| Chunks CSV SHA-256 | `8399dcbb0934a17a56e181c05275bf49634408bc9022ec890891a810ee646bd4` | Recorded in snapshot metadata |
| Retrieval index status | `BM25_ONLY` | Built for lexical acceptance queries |

Validation command run in this session:

```sh
python3 tools/source_catalog/validate_source_database.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --domain-root domains/chirality \
  --repo-root .
```

Result:

```text
PASS: /Users/ryan/ai-env/projects/chirality/domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260613T232620Z (0 blockers, 0 warnings)
```

BM25-only index command run in this session:

```sh
python3 tools/retrieval/build_source_index.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --no-embeddings
```

Acceptance queries returned expected governance surfaces:

| Query | Expected result class | Observed top result |
|---|---|---|
| `K-PROV-1` | provenance governance | `@repo/docs/thesis/02_literature_review.md` rank 1; exact K-PROV content present in top results |
| `TASK hard authorization boundary` | TASK contract | `@repo/agents/AGENT_TASK.md` rank 1 |
| `derivative-package rule` | governance integration rule | `@repo/AGENTS.md` rank 1 |
| `public export boundary` | public/private export boundary | `@repo/README.md` rank 1 |

## Corpus Scope

The v1 corpus remains the manifest-backed governance core only. Live repo files remain the source of truth; `domains/chirality/` records membership, source hashes, local catalog snapshots, and later decomposition outputs.

Manifest summary:

| SourceGroup | Files | Catalog chunks |
|---|---:|---:|
| `ROOT_DOCS` | 7 | 119 |
| `ROOT_GOVERNANCE_DOCS` | 31 | 1059 |
| `AGENT_CONTRACTS` | 37 | 1442 |
| `SKILL_CONTRACTS` | 153 | 1750 |
| `TOOL_REGISTRY_DOCS` | 3 | 47 |
| `HARNESS_EXPORT_DOCS` | 11 | 106 |
| Total | 242 | 4523 |

Excluded from v1, by source-boundary decision:

- `projects/`
- existing `domains/`
- `examples/`
- `.archive/`
- generated export staging
- caches, dependency folders, and build outputs
- non-governance code internals

## DOMAIN_DECOMP Readiness Findings

The source truth and retrieval substrate are ready. The decomposition tooling needs a manifest-backed Markdown adapter before Phase 1 can run cleanly.

Key findings:

1. `DOMAIN_DECOMP` expects source discovery under `_Sources/<book>/`, but Chirality v1 source files are live repo paths recorded as `@repo/<RepoRelPath>`.
2. `tools/decomp/build_source_skeleton.py` can operate on a live repo Markdown path if supplied a minimal asset manifest with `doc_stem`, empty `assets`, and empty `pages`.
3. A throwaway skeleton preflight against `AGENTS.md` succeeded with a minimal asset manifest and no copied source file:

   ```text
   source=AGENTS prefix=RT001 sections=9 in_scope=9 units=1
   ```

4. `LICENSE.md` is the only manifest row with no Markdown headings. `build_source_skeleton.py` fails fast on headingless Markdown, so the next agent must either add a synthetic in-memory/adapter heading for that source or mark it OUT/deferred for v1 atomization.
5. Naive source-prefix derivation collides for similarly named documents. The next agent must create an explicit source-prefix map before skeleton generation.

## Required Adapter Decision

Recommended adapter: keep live repo files as source truth and generate decomposition-local companion artifacts that point back to `@repo/` paths. Do not copy the 242 source files into `_Sources/` as authoritative source snapshots.

The next agent should create a preflight package under `_Decomposition/` similar to:

```text
domains/chirality/_Decomposition/
  Chirality_Domain_Decomposition.md
  Source_Decomp_Prefix_Map.csv
  source_asset_manifests/
    <SourceDocID>_assets_manifest.json
  source_skeletons/
    <SourceDocID>_skeleton.json
  source_dispatch_plans/
    <SourceDocID>_dispatch_plan.json
  source_review_html/
    <SourceDocID>.html
  source_section_nodes/
    <SourceDocID>_section_nodes.csv
  dispatch_briefs/
  dispatch_outputs/
  per_source_ledgers/
  Atomic_Domain_Ledger.csv
  Vocabulary_Map.csv
  Category_Register.csv
  Knowledge_Type_Register.csv
  Knowledge_Subject_Register.csv
  Open_Issues_Register.csv
  Coverage_Telemetry.csv
```

Adapter rules:

- `Source_Decomp_Prefix_Map.csv` is required before any skeleton or atomization work.
- Source prefixes must be explicit, stable, unique, and alphanumeric. Recommended pattern by source group:
  - `RT001...` for root docs
  - `DG001...` for root governance docs
  - `AG001...` for agent contracts
  - `SK001...` for skill contracts
  - `TL001...` for tool registry docs
  - `HX001...` for harness/export docs
- Minimal asset manifests are authoritative decomposition companions for Markdown-only source handling, not source truth. Each should include at least:

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

- `SourceRef` policy should preserve repo provenance. Preferred form:

  ```text
  @repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
  ```

  If existing `domain-source-atomize` briefs require the older `<book>.md:L####|<book>.html#anchor` form, the next agent should explicitly record the deviation and either:
  - adapt `build_atomization_brief.py` / the task brief to require `@repo/` SourceRefs, or
  - emit an additional provenance column in downstream ledgers that carries `@repo/<RepoRelPath>`.

- Gate 1.5 asset surfaces (`equations.html`, `figures.html`, `tables.html`, `images.html`, `folios.html`) are `N/A` for this Markdown-only manifest unless a later source row has an asset manifest with actual assets. The section/atom review HTML remains required.

## Recommended DOMAIN_DECOMP Run Strategy

All 242 manifest rows should remain admitted for v1, but atomization should be staged by authority batch. This preserves full coverage while keeping review gates tractable.

### Batch 0 - Adapter And Gate-1 Preflight

Purpose: make the corpus executable by DOMAIN_DECOMP without changing source truth.

Actions:

1. Re-run source catalog validation.
2. Recompute `Source_Manifest.csv` hashes or explicitly verify they are unchanged.
3. Generate `Source_Decomp_Prefix_Map.csv`.
4. Generate minimal asset manifests for all included Markdown files.
5. Build skeletons and dispatch plans for all heading-bearing files.
6. Handle `LICENSE.md` by one of:
   - mark `AtomizeInV1=NO`, `InOutDefault=OUT`, reason `headingless legal/license text`; or
   - create a derivative adapter view with a synthetic `# LICENSE` heading and record it as derivative/non-source-truth.
7. Generate section review HTML and section-node CSVs.
8. Produce intake telemetry:
   - files by group
   - files with skeletons
   - files deferred
   - section count by group
   - dispatch-unit count by group
   - oversized dispatch units
   - sources requiring human review notes

Gate 1 output:

- Updated main decomposition control surface draft.
- References list from `Source_Manifest.csv`.
- Companion inventory.
- Source-prefix map.
- Skeleton/dispatch telemetry.
- Open issue for `LICENSE.md` handling if not already resolved.

Gate 1 human confirmation required:

```text
The manifest-backed source set, source-prefix map, skeleton inventory, and deferred-source decisions are accepted as the intended Chirality DOMAIN_DECOMP intake.
```

### Batch 1 - Binding Governance Seed

Purpose: establish the highest-authority operating-system rules first.

Recommended sources:

- `AGENTS.md`
- root `README.md`, `INIT.md`, `CLAUDE.md`, `CHIRALITY_FRAMEWORK.md`, `PROFESSIONAL_ENGINEERING.md`
- core `docs/*.md` governance files, especially `CONTRACT.md`, `SPEC.md`, `TYPES.md`, `DIRECTIVE.md`, `PLAN.md`, `DBM_Agent_Instruction_Architecture.md`, `SE_Design_Analysis.md`
- `skills/README.md`, `skills/SKILL_TEMPLATE.md`
- `tools/REGISTRY.md`, `tools/EXTERNAL_TOOLS.md`, `tools/retrieval/README.md`
- `exports/chirality-app/README.md`, `exports/chirality-app/export-report.md`

Expected use: generate the first vocabulary seeds, initial atom ledger, and provisional category hypotheses.

### Batch 2 - Agent Contract Layer

Purpose: atomize the behavior, authority, gates, write scopes, and handoff rules of the live agent suite.

Recommended sources:

- all `agents/AGENT_*.md`

Special attention:

- `AGENT_DECOMP_BASE.md`
- `AGENT_DOMAIN_DECOMP.md`
- `AGENT_TASK.md`
- `AGENT_ORCHESTRATOR.md`
- `AGENT_DOMAIN_ENGINE.md`
- `AGENT_CHANGE.md`
- audit/evaluation agents

Expected use: stabilize categories and KTYs for agent roles, workflow phases, gates, derivative packages, snapshot rules, handoff states, and audit loops.

### Batch 3 - Skill Contract Layer

Purpose: atomize repo-native TASK method packs and their local contracts.

Recommended sources:

- all `skills/*/SKILL.md`
- supporting skill docs such as `BRIEF_SCHEMA.md`, `TOOL_POLICY.md`, `QA_CHECKS.md`, and skill-local README-style Markdown included by the manifest

Expected use: distinguish agent persona behavior from task-skill method behavior, and capture reusable TASK dispatch patterns.

### Batch 4 - Design-Basis And Harness Context

Purpose: incorporate broader Chirality rationale, thesis material, frontend harness docs, and public export context after the binding contracts are already represented.

Recommended sources:

- `docs/thesis/**/*.md`
- `docs/rubrics/**/*.md`
- `docs/templates/**/*.md`
- `frontend/README.md`
- `frontend/docs/**/*.md`

Expected use: enrich rationale, vocabulary, public/private boundary knowledge, harness concepts, and design-basis explanations without letting narrative context override binding contracts.

## Provisional Category And KTY Hypotheses

These are not accepted decomposition truth. They are starting hypotheses for the next `DOMAIN_DECOMP` agent to test against source evidence and retrieval results.

Potential flat categories:

| Candidate category | Rationale to test |
|---|---|
| Governance and Authority | Human authority, provenance, no-invention, write scopes, gates, snapshots, closure |
| Agent Operating System | Agent matrix, Type 0/1/2 roles, personas, shells, pipeline/workbench distinctions |
| TASK and Skill Execution | TASK hard boundary, method packs, runtime overrides, dispatch briefs, task-local QA |
| Domain and Decomposition Workflows | DECOMP_BASE, DOMAIN_DECOMP, source atomization, ledgers, KTYs, hypergraphs |
| Evidence, Retrieval, and Validation | Source catalog, BM25/dense retrieval, validation tools, test surfaces, metadata |
| Publication and Export Boundaries | Public export profile, private repo boundary, derivative packages, publishing reports |
| Harness and Runtime Surfaces | Frontend harness, artifact mirroring, app/runtime docs |
| Professional and Design Rationale | Chirality framework, professional accountability, thesis/design-basis material |

Potential KTY families:

- Governance rule
- Agent contract
- Task shell rule
- Skill method contract
- Tool contract
- Validation/check procedure
- Source/retrieval artifact
- Snapshot/handoff state
- Public/private boundary rule
- Review/audit workflow
- Design rationale
- Vocabulary/ontology term

The next agent must retire, split, or rename these when source evidence demands it. Categories must remain flat; every IN atom eventually maps to exactly one category.

## Phase 2 Atomization Plan

After Gate 1 acceptance, the next agent should run Phase 2 as bounded `TASK + domain-source-atomize` dispatches.

For each source with `AtomizeInV1=YES`:

1. Build or use the reviewed skeleton and dispatch plan.
2. Render a dispatch brief per unit:

   ```sh
   python3 tools/decomp/build_atomization_brief.py \
     --dispatch-plan <dispatch_plan.json> \
     --unit-id <UNIT-ID> \
     --md <live_repo_markdown_path> \
     --skeleton <skeleton.json> \
     --asset-manifest <minimal_asset_manifest.json> \
     --output-ledger-path <dispatch_outputs>/<SourceDocID>_<UNIT-ID>_atoms.csv \
     --output-vocab-seed-path <dispatch_outputs>/<SourceDocID>_<UNIT-ID>_vocab.csv \
     --scope-path domains/chirality/_Decomposition
   ```

3. Dispatch one `TASK + domain-source-atomize` worker per dispatch unit.
4. Merge per-source ledgers:

   ```sh
   python3 tools/decomp/merge_source_atomizations.py per-source \
     --dispatch-plan <dispatch_plan.json> \
     --unit-csv-glob '<dispatch_outputs>/<SourceDocID>_*_atoms.csv' \
     --source-prefix <SourcePrefix> \
     --source-name <SourceDocID> \
     --output <per_source_ledgers>/<SourceDocID>_atomic_units.csv \
     --strict-coverage
   ```

5. Merge cross-source ledgers after each accepted batch, not only at the end:

   ```sh
   python3 tools/decomp/merge_source_atomizations.py cross-source \
     --per-source <per_source_ledgers>/<SourceDocID>_atomic_units.csv \
     --output domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv
   ```

6. Merge vocabulary seeds:

   ```sh
   python3 tools/decomp/merge_vocabulary_seeds.py \
     --seed <per_source_or_dispatch_vocab.csv> \
     --source-doc <SourceDocID> \
     --output domains/chirality/_Decomposition/Vocabulary_Map.csv
   ```

Gate 2 should not close until:

- every dispatch unit in accepted batches has an atom CSV or an explicit deferral;
- every IN/TBD atom has a traceable SourceRef;
- ContentHash values recompute;
- vocabulary seeds are merged;
- source HTML review surfaces are regenerated in atom-review mode where supported;
- human review has resolved or accepted all open Gate 2 blockers.

## Retrieval Use During DOMAIN_DECOMP

The next agent should use the accepted BM25-only index for scope ratification and source discovery during planning and gates. Dense embeddings are optional later; do not make dense retrieval a blocker for Phase 1 or Phase 2.

Recommended starting commands:

```sh
python3 tools/source_catalog/validate_source_database.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --domain-root domains/chirality \
  --repo-root .

python3 tools/retrieval/query_source_index.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --query "derivative-package rule" \
  --k 10
```

If any manifest hash has drifted, rebuild the source catalog and BM25 index before using retrieval as gate evidence:

```sh
python3 tools/source_catalog/build_source_database.py \
  --domain-root domains/chirality \
  --repo-root . \
  --source-manifest domains/chirality/_Sources/Source_Manifest.csv

python3 tools/source_catalog/validate_source_database.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --domain-root domains/chirality \
  --repo-root .

python3 tools/retrieval/build_source_index.py \
  --snapshot domains/chirality/_LocalIndexes/_LATEST.md \
  --no-embeddings
```

## Non-Goals For The Next Agent Startup

Do not start with:

- full unbatched atomization of all 242 files;
- dense embedding build as a prerequisite;
- copying live repo source files into `_Sources/` as authoritative source truth;
- creating final categories/KTYs without atom evidence and Gate 3/Gate 4 review;
- DBM publication, hypergraph generation, or public export changes;
- treating generated catalog or retrieval snapshots as decomposition truth.

## Open Issues For The Next Agent

| ID | Issue | Required disposition |
|---|---|---|
| OI-001 | `LICENSE.md` is headingless and will fail the skeleton tool. | Decide OUT/defer vs synthetic derivative heading before Gate 1 closes. |
| OI-002 | `DOMAIN_DECOMP` SourceRef convention does not explicitly cover `@repo/` paths. | Accept an adapter SourceRef convention or patch brief/tool docs before atomization. |
| OI-003 | Explicit source-prefix map does not exist yet. | Generate and review `Source_Decomp_Prefix_Map.csv`. |
| OI-004 | Gate 1.5 asset surfaces are mostly N/A for Markdown-only sources. | Record N/A policy in main decomposition document. |
| OI-005 | Full 242-file atomization may produce many dispatches. | Run in staged authority batches with human gate checkpoints. |

## Handoff State

Accepted upstream snapshot:

- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `507201a0e5bad74d6e97fc771a37065ea3f8903332b231cd4eff35081634c920`
- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260613T232620Z`
- Catalog validation verdict: PASS, 0 blockers, 0 warnings
- Retrieval index: BM25-only, 4523 rows

Derivative-package status:

- `_LocalIndexes` catalog and BM25 index are derivative local artifacts.
- This plan is a planning handoff artifact.
- Future skeletons, dispatch plans, minimal asset manifests, section-node CSVs, source review HTMLs, atom ledgers, and vocabulary maps will be DOMAIN_DECOMP companion artifacts once created by the next agent.

Closure verdict:

- Current session scope #1 is closed: retrieval snapshot and manifest state are accepted for next-agent planning use.
- Current session scope #2 is closed: readiness and DOMAIN_DECOMP startup plan are recorded here.
- DOMAIN_DECOMP itself is not closed and has not begun Gate 1 acceptance.

Rerun requirements:

- Re-run source catalog validation at the start of the next agent session.
- If any manifest row hash mismatches, rebuild the catalog and BM25 index and update this handoff's accepted snapshot reference before proceeding.
- If `agents/`, `skills/`, `docs/`, root docs, `tools/REGISTRY.md`, `tools/retrieval/README.md`, `frontend/docs/`, or `exports/chirality-app/*.md` change before the next agent run, regenerate `Source_Manifest.csv` hashes and rebuild retrieval.

Remaining blockers:

- Human must confirm Gate 1 intake after the next agent generates prefix map, skeleton telemetry, and source review surfaces.
- Adapter SourceRef policy must be accepted before any `TASK + domain-source-atomize` dispatch.
- `LICENSE.md` handling must be resolved or explicitly deferred.

## Suggested Startup Brief For Next Agent

```text
Act as DOMAIN_DECOMP for domains/chirality.

Use /Users/ryan/ai-env/projects/chirality/plans/chirality_domain_decomp_readiness_2026-06-13.md as the handoff plan.

Do not run full atomization immediately. Start by validating the accepted retrieval snapshot, generating the manifest-backed Markdown adapter layer under domains/chirality/_Decomposition/, producing Source_Decomp_Prefix_Map.csv, skeletons, dispatch plans, minimal asset manifests, section review HTML, section-node CSVs, and intake telemetry. Then present Gate 1 intake for human confirmation.

Respect the manifest-backed source model: live repo files are source truth, and decomposition companion artifacts must cite @repo/<RepoRelPath> provenance.
```
