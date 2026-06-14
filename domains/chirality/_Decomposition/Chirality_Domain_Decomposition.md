# Chirality Domain Decomposition

Package role: working surface

Status: Gate 1 intake accepted. Phase 2 Batch 1 Gate 2 accepted; Phase 2.5 source catalog, BM25 retrieval, and TOC-prior refresh complete. Phase 2 Batch 2 agent-contract setup is ready; worker fan-out is not started.

Generated UTC: 2026-06-14T02:42:51+00:00

## Source Model

The Chirality domain pack uses manifest-backed live repository files as source truth. Source files are not copied into `_Sources/`; decomposition companions point back to `@repo/<RepoRelPath>`.

Accepted manifest for this Batch 0 packet: `domains/chirality/_Sources/Source_Manifest.csv`

Current source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`

Current source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T023650Z`

Catalog schema: `chirality-source-db/v2`

Catalog validation result: `PASS`

Source files copied: `false`

Retrieval index status: `BM25_ONLY`

Retrieval smoke query: `PASS`

Dense retrieval status: `DEFERRED`

## Intake Summary

| Metric | Value |
|---|---:|
| Manifest source rows | 242 |
| Catalog artifacts | 485 |
| Catalog source docs | 242 |
| Catalog chunks | 12246 |
| Catalog markdown chunks | 4523 |
| Catalog section-node chunks | 4449 |
| Catalog ledger-atom chunks | 3274 |
| Skeletons generated | 242 |
| Review HTML files generated | 242 |
| Section-node CSVs generated | 242 |
| Total sections | 4449 |
| In-scope sections | 4446 |
| Dispatch units | 242 |
| Oversized dispatch units | 0 |
| Deferred sources | 1 |
| Skeleton failures | 0 |

## Group Telemetry

| SourceGroup | Sources | Skeletons | Deferred | Sections | In-scope Sections | Dispatch Units | Oversized Units |
|---|---:|---:|---:|---:|---:|---:|---:|
| AGENT_CONTRACTS | 37 | 37 | 0 | 1405 | 1403 | 37 | 0 |
| HARNESS_EXPORT_DOCS | 11 | 11 | 0 | 106 | 106 | 11 | 0 |
| ROOT_DOCS | 7 | 7 | 1 | 119 | 118 | 6 | 0 |
| ROOT_GOVERNANCE_DOCS | 31 | 31 | 0 | 1059 | 1059 | 32 | 0 |
| SKILL_CONTRACTS | 153 | 153 | 0 | 1713 | 1713 | 153 | 0 |
| TOOL_REGISTRY_DOCS | 3 | 3 | 0 | 47 | 47 | 3 | 0 |

## SourceRef Adapter Policy

The manifest-backed SourceRef form is accepted for Phase 2 atomization:

```text
@repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

This preserves live repo provenance and keeps the HTML half pointed at the Batch 0 review surface. `tools/decomp/build_atomization_brief.py` emits `SOURCE_REF_BASE` for the worker, and `skills/domain-source-atomize` explicitly accepts the repo-backed form for manifest-backed sources.

## LICENSE.md Disposition

`SRC-LICENSE` is headingless legal/license text. Batch 0 created a synthetic one-section review skeleton without copying or modifying `LICENSE.md`, marked the section OUT by default, and set `AtomizeInV1=NO`. This deferred-source decision was accepted at Gate 1.

## Gate 1.5 Asset Surface Policy

Per-kind asset audit surfaces are N/A for this Markdown-only manifest because the generated minimal asset manifests contain no assets or pages. The section review HTML remains required and has been generated under `domains/chirality/_Decomposition/source_review_html/`.

## Phase 2 Batch Status

Batch 1 binding-governance atomization is accepted at Gate 2. Worker fan-out, deterministic fan-in, vocabulary merge, atom-review HTML rendering, human Gate 2 acceptance, and Phase 2.5 refresh are complete for the selected 22-source batch. This is an accepted partial Phase 2 ledger over the binding-governance source set only; it is not full-corpus decomposition truth.

| Metric | Value |
|---|---:|
| Batch ID | `BATCH1_BINDING_GOVERNANCE_20260614T011101Z` |
| Selected sources | 22 |
| Dispatch units | 22 |
| Rendered INIT-TASK briefs | 22 |
| Atomization worker status | `SUCCESS` |
| Per-unit atom CSVs | 22 |
| Per-unit vocabulary CSVs | 22 |
| Raw worker atom rows | 3276 |
| Merged atom ledger rows | 3274 |
| Deduped duplicate hash rows | 2 |
| IN rows after merge | 3262 |
| OUT rows after merge | 12 |
| TBD rows after merge | 0 |
| Per-source ledgers | 22 |
| Merged vocabulary terms | 670 |
| Atom-review HTML files | 22 |
| Gate 2 status | `ACCEPTED` |
| Gate 2 snapshot | `GATE2_BATCH1_20260614T023234Z` |

Batch setup handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_SETUP.md`

Batch atomization handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_ATOMIZATION_HANDOFF.md`

Batch Gate 2 handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_GATE2_HANDOFF.md`

Batch source register: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/Batch_Source_Register.csv`

Dispatch unit register: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/Dispatch_Unit_Register.csv`

Dispatch run log: `domains/chirality/_Decomposition/phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/Dispatch_Run_Log.csv`

Batch atom outputs root: `domains/chirality/_Decomposition/dispatch_outputs/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`

Batch per-source ledgers root: `domains/chirality/_Decomposition/per_source_ledgers/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`

Batch vocabulary seeds root: `domains/chirality/_Decomposition/vocabulary_seeds/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/`

Partial cross-source ledger: `domains/chirality/_Decomposition/Atomic_Domain_Ledger.csv`

Merged vocabulary map: `domains/chirality/_Decomposition/Vocabulary_Map.csv`

## Phase 2 Batch 2 Setup Status

Batch 2 agent-contract setup is ready for future `TASK + domain-source-atomize` fan-out. The batch includes every admitted `AGENT_CONTRACTS` source with `AtomizeInV1=YES`, excludes all Batch 1 sources, and has not run any atomization workers.

| Metric | Value |
|---|---:|
| Batch ID | `BATCH2_AGENT_CONTRACTS_20260614T024251Z` |
| Selected source group | `AGENT_CONTRACTS` |
| Selected sources | 37 |
| Dispatch units | 37 |
| Rendered INIT-TASK briefs | 37 |
| Atomization worker status | `NOT_STARTED` |
| Gate 2 status | `NOT_OPEN` |

Batch 2 setup handoff: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T024251Z/BATCH2_SETUP.md`

Batch 2 source register: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T024251Z/Batch_Source_Register.csv`

Batch 2 dispatch unit register: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T024251Z/Dispatch_Unit_Register.csv`

Batch 2 validation register: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T024251Z/Validation_Checks.csv`

Batch 2 dispatch briefs root: `domains/chirality/_Decomposition/dispatch_briefs/BATCH2_AGENT_CONTRACTS_20260614T024251Z/`

Batch 2 reserved atom outputs root: `domains/chirality/_Decomposition/dispatch_outputs/BATCH2_AGENT_CONTRACTS_20260614T024251Z/`

## Phase 2.5 Retrieval Refresh

Phase 2.5 was run after human Gate 2 approval. The manifest-backed source catalog now includes live repo source markdown plus derived decomposition companions: section-node CSV chunks from Batch 0 and accepted `LEDGER_ATOM` chunks from the Batch 1 ledger.

| Metric | Value |
|---|---:|
| Source catalog snapshot | `SRCIDX_20260614T023650Z` |
| Catalog validation | `PASS` |
| Source docs | 242 |
| Artifacts | 485 |
| Total chunks | 12246 |
| `MARKDOWN_SECTION` chunks | 4523 |
| `SECTION_NODE` chunks | 4449 |
| `LEDGER_ATOM` chunks | 3274 |
| Retrieval status | `BM25_ONLY` |
| Retrieval rows | 12246 |
| Dense embeddings | `DEFERRED` |
| BM25 smoke query | `derivative-package rule` -> `@repo/AGENTS.md` rank 1 |
| TOC-prior matrix scope | 22 accepted Batch 1 skeletons |
| TOC-prior source-pair rows | 81 |

TOC-prior matrix Markdown: `domains/chirality/_Decomposition/cross_source_toc_matrix.md`

TOC-prior matrix CSV: `domains/chirality/_Decomposition/cross_source_toc_matrix.csv`

## References

- `domains/chirality/_Sources/Source_Manifest.csv` - manifest-backed source membership.
- `domains/chirality/_Sources/SOURCE_BOUNDARY.md` - source boundary.
- `domains/chirality/_LocalIndexes/_LATEST.md` - latest source catalog pointer.
- `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T023650Z` - current validated source catalog and BM25 retrieval snapshot.
- `domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z/` - accepted Gate 2 Batch 1 snapshot.

## Companion Inventory

| Filename | PackageRole | Description |
|---|---|---|
| `Chirality_Domain_Decomposition.md` | working surface | Main Batch 0 control surface and Gate 1 packet. |
| `Source_Decomp_Prefix_Map.csv` | authoritative companion register | Stable source-prefix map and SourceRef adapter metadata. |
| `Intake_Telemetry.csv` | authoritative companion register | Per-source intake, skeleton, render, and dispatch telemetry. |
| `Intake_Telemetry.json` | authoritative companion register | Batch 0 summary telemetry. |
| `Open_Issues_Register.csv` | authoritative companion register | Current open issues, including the Batch 1 Gate 2 human-review blocker. |
| `Validation_Checks.csv` | authoritative companion register | Current validation checks, including Batch 1 fan-out/fan-in status. |
| `Companion_Inventory.csv` | authoritative companion register | File-level inventory of generated companion artifacts. |
| `gate_snapshots/_LATEST_GATE1.md` | snapshot / handoff artifact | Pointer to the accepted Gate 1 snapshot. |
| `gate_snapshots/GATE1_20260614T005942Z/GATE1_ACCEPTANCE.md` | snapshot / handoff artifact | Immutable Gate 1 acceptance record. |
| `gate_snapshots/GATE1_20260614T005942Z/HANDOFF_STATE.md` | snapshot / handoff artifact | Gate 1 handoff state for later DOMAIN_DECOMP phases. |
| `gate_snapshots/_LATEST_GATE2.md` | snapshot / handoff artifact | Pointer to the accepted Batch 1 Gate 2 snapshot. |
| `gate_snapshots/GATE2_BATCH1_20260614T023234Z/GATE2_ACCEPTANCE.md` | snapshot / handoff artifact | Immutable Batch 1 Gate 2 acceptance record. |
| `gate_snapshots/GATE2_BATCH1_20260614T023234Z/HANDOFF_STATE.md` | snapshot / handoff artifact | Gate 2 / Phase 2.5 handoff state. |
| `phase2_batches/_LATEST_BATCH1_GATE2.md` | snapshot / handoff artifact | Pointer to the accepted Batch 1 Gate 2 handoff. |
| `phase2_batches/BATCH1_BINDING_GOVERNANCE_20260614T011101Z/BATCH1_GATE2_HANDOFF.md` | snapshot / handoff artifact | Batch 1 Gate 2 accepted and Phase 2.5 complete handoff. |
| `phase2_batches/_LATEST_BATCH2_SETUP.md` | snapshot / handoff artifact | Pointer to the current Batch 2 setup handoff. |
| `phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T024251Z/BATCH2_SETUP.md` | snapshot / handoff artifact | Batch 2 agent-contract setup handoff; worker fan-out not started. |
| `cross_source_toc_matrix.md` | derivative planning surface | Batch 1 cross-source TOC-prior review surface generated after Gate 2 acceptance. |
| `cross_source_toc_matrix.csv` | derivative planning surface | Batch 1 cross-source TOC-prior machine-readable matrix. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-AGENTS_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-AGENTS. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-AGENTS_skeleton.json` | authoritative companion register | Source skeleton for SRC-AGENTS. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-AGENTS_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-AGENTS. |
| `domains/chirality/_Decomposition/source_review_html/SRC-AGENTS.html` | authoritative companion register | Atom-review section+atom HTML for SRC-AGENTS; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-AGENTS_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-AGENTS. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-CHIRALITY-FRAMEWORK_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-CHIRALITY-FRAMEWORK. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-CHIRALITY-FRAMEWORK_skeleton.json` | authoritative companion register | Source skeleton for SRC-CHIRALITY-FRAMEWORK. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-CHIRALITY-FRAMEWORK_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-CHIRALITY-FRAMEWORK. |
| `domains/chirality/_Decomposition/source_review_html/SRC-CHIRALITY-FRAMEWORK.html` | authoritative companion register | Atom-review section+atom HTML for SRC-CHIRALITY-FRAMEWORK; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-CHIRALITY-FRAMEWORK_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-CHIRALITY-FRAMEWORK. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-CLAUDE_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-CLAUDE. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-CLAUDE_skeleton.json` | authoritative companion register | Source skeleton for SRC-CLAUDE. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-CLAUDE_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-CLAUDE. |
| `domains/chirality/_Decomposition/source_review_html/SRC-CLAUDE.html` | authoritative companion register | Atom-review section+atom HTML for SRC-CLAUDE; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-CLAUDE_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-CLAUDE. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-INIT_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-INIT. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-INIT_skeleton.json` | authoritative companion register | Source skeleton for SRC-INIT. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-INIT_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-INIT. |
| `domains/chirality/_Decomposition/source_review_html/SRC-INIT.html` | authoritative companion register | Atom-review section+atom HTML for SRC-INIT; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-INIT_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-INIT. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-LICENSE_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-LICENSE. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-LICENSE_skeleton.json` | authoritative companion register | Source skeleton for SRC-LICENSE. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-LICENSE_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-LICENSE. |
| `domains/chirality/_Decomposition/source_review_html/SRC-LICENSE.html` | authoritative companion register | Structure-mode section review HTML for SRC-LICENSE. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-LICENSE_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-LICENSE. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-PROFESSIONAL-ENGINEERING_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-PROFESSIONAL-ENGINEERING. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-PROFESSIONAL-ENGINEERING_skeleton.json` | authoritative companion register | Source skeleton for SRC-PROFESSIONAL-ENGINEERING. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-PROFESSIONAL-ENGINEERING_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-PROFESSIONAL-ENGINEERING. |
| `domains/chirality/_Decomposition/source_review_html/SRC-PROFESSIONAL-ENGINEERING.html` | authoritative companion register | Atom-review section+atom HTML for SRC-PROFESSIONAL-ENGINEERING; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-PROFESSIONAL-ENGINEERING_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-PROFESSIONAL-ENGINEERING. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-README_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-README. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-README_skeleton.json` | authoritative companion register | Source skeleton for SRC-README. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-README_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-README. |
| `domains/chirality/_Decomposition/source_review_html/SRC-README.html` | authoritative companion register | Atom-review section+atom HTML for SRC-README; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-README_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-README. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-CONTRACT_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-CONTRACT. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-CONTRACT_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-CONTRACT. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-CONTRACT_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-CONTRACT. |
| `domains/chirality/_Decomposition/source_review_html/SRC-DOCS-CONTRACT.html` | authoritative companion register | Atom-review section+atom HTML for SRC-DOCS-CONTRACT; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-DOCS-CONTRACT_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-DOCS-CONTRACT. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE. |
| `domains/chirality/_Decomposition/source_review_html/SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE.html` | authoritative companion register | Atom-review section+atom HTML for SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-DIRECTIVE_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-DIRECTIVE. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-DIRECTIVE_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-DIRECTIVE. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-DIRECTIVE_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-DIRECTIVE. |
| `domains/chirality/_Decomposition/source_review_html/SRC-DOCS-DIRECTIVE.html` | authoritative companion register | Atom-review section+atom HTML for SRC-DOCS-DIRECTIVE; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-DOCS-DIRECTIVE_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-DOCS-DIRECTIVE. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-PLAN_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-PLAN. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-PLAN_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-PLAN. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-PLAN_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-PLAN. |
| `domains/chirality/_Decomposition/source_review_html/SRC-DOCS-PLAN.html` | authoritative companion register | Atom-review section+atom HTML for SRC-DOCS-PLAN; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-DOCS-PLAN_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-DOCS-PLAN. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-PRD-CANDIDATE_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-PRD-CANDIDATE. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-PRD-CANDIDATE_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-PRD-CANDIDATE. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-PRD-CANDIDATE_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-PRD-CANDIDATE. |
| `domains/chirality/_Decomposition/source_review_html/SRC-DOCS-PRD-CANDIDATE.html` | authoritative companion register | Atom-review section+atom HTML for SRC-DOCS-PRD-CANDIDATE; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-DOCS-PRD-CANDIDATE_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-DOCS-PRD-CANDIDATE. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-SE-DESIGN-ANALYSIS_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-SE-DESIGN-ANALYSIS. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-SE-DESIGN-ANALYSIS_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-SE-DESIGN-ANALYSIS. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-SE-DESIGN-ANALYSIS_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-SE-DESIGN-ANALYSIS. |
| `domains/chirality/_Decomposition/source_review_html/SRC-DOCS-SE-DESIGN-ANALYSIS.html` | authoritative companion register | Atom-review section+atom HTML for SRC-DOCS-SE-DESIGN-ANALYSIS; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-DOCS-SE-DESIGN-ANALYSIS_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-DOCS-SE-DESIGN-ANALYSIS. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-SPEC_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-SPEC. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-SPEC_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-SPEC. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-SPEC_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-SPEC. |
| `domains/chirality/_Decomposition/source_review_html/SRC-DOCS-SPEC.html` | authoritative companion register | Atom-review section+atom HTML for SRC-DOCS-SPEC; Batch 1 Gate 2 review surface. |
| `domains/chirality/_Decomposition/source_section_nodes/SRC-DOCS-SPEC_section_nodes.csv` | authoritative companion register | Section-node retrieval substrate for SRC-DOCS-SPEC. |
| `domains/chirality/_Decomposition/source_asset_manifests/SRC-DOCS-TYPES_assets_manifest.json` | authoritative companion register | Minimal Markdown-only asset manifest for SRC-DOCS-TYPES. |
| `domains/chirality/_Decomposition/source_skeletons/SRC-DOCS-TYPES_skeleton.json` | authoritative companion register | Source skeleton for SRC-DOCS-TYPES. |
| `domains/chirality/_Decomposition/source_dispatch_plans/SRC-DOCS-TYPES_dispatch_plan.json` | authoritative companion register | Phase 2 dispatch plan for SRC-DOCS-TYPES. |
| `Companion_Inventory.csv` | authoritative companion register | Full file-level inventory for all 1390 generated companion entries. |

## Open Issues

| IssueID | Status | Issue | Recommendation |
|---|---|---|---|
| `OI-001` | ACCEPTED_FOR_PHASE_2 | LICENSE.md is headingless and legal/license text. | Keep AtomizeInV1=NO and InOutDefault=OUT for v1 unless human says license terms are in-domain. |
| `OI-002` | ACCEPTED_FOR_PHASE_2 | DOMAIN_DECOMP source atomization docs specify older <book>.md:L#### SourceRefs. | @repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID> |
| `OI-004` | ACCEPTED_FOR_PHASE_2 | Per-kind asset surfaces are N/A for Markdown-only manifest rows. | Use section review HTML only unless future sources carry actual asset manifests. |
| `OI-005` | OPEN | Full 242-file atomization is too large for one unbatched review gate. | Batch 1 Gate 2 is accepted; schedule later staged batches separately if full-corpus atomization remains required. |
| `OI-006` | CLOSED | Batch 1 atom boundaries, IN/OUT classifications, and vocabulary choices have not been human-reviewed. | Closed by human Gate 2 approval on 2026-06-14; accepted for the selected 22-source Batch 1 corpus only. |
| `OI-007` | OPEN | Accepted Batch 1 atoms do not yet have ratified Category/KTY/Knowledge Subject assignments. | Prepare batch-scoped Gate 3 proposal surfaces from the accepted Batch 1 ledger and refreshed retrieval substrate. |
| `OI-008` | OPEN | Batch 2 agent-contract worker fan-out has not started. | Dispatch the 37 rendered Batch 2 briefs only after explicit operator authorization. |

## Decision Log / Change Log

| DecisionID | Date | Decision |
|---|---|---|
| DEC-001 | 2026-06-14 | Repaired `SRC-INIT` manifest path from `INIT.md` to `init/INIT.md` after validation found the root path missing. SourceDocID and content hash were preserved. |
| DEC-002 | 2026-06-14 | Generated Batch 0 adapter companions from live repo paths; no source files were copied into `_Sources/`. |
| DEC-003 | 2026-06-14 | Proposed `SRC-LICENSE` as headingless OUT/deferred for v1 atomization pending Gate 1 acceptance. |
| DEC-004 | 2026-06-14 | Accepted repo-backed SourceRefs for manifest-backed atomization: `@repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>`. |
| DEC-005 | 2026-06-14 | Forced standalone `SRC-DOCS-THESIS-GLOSSARY` in scope for v1 atomization; the generic late-document glossary back-matter heuristic remains unchanged for other sources. |
| DEC-006 | 2026-06-14 | Human accepted Gate 1 intake, including the manifest-backed source set, source-prefix map, skeleton inventory, `SRC-LICENSE` OUT/deferred disposition, Markdown-only asset-surface N/A policy, and repo-backed SourceRef policy. |
| DEC-007 | 2026-06-14 | Prepared `BATCH1_BINDING_GOVERNANCE_20260614T011101Z` as the staged Phase 2 Batch 1 binding-governance setup: 22 sources, 22 dispatch units, 22 repo-backed dispatch briefs; no atomization workers were run. |
| DEC-008 | 2026-06-14 | Ran authorized Batch 1 `TASK + domain-source-atomize` fan-out for 22 dispatch units. All workers completed successfully and local QA passed. |
| DEC-009 | 2026-06-14 | Merged Batch 1 outputs into 22 per-source ledgers, partial `Atomic_Domain_Ledger.csv`, and `Vocabulary_Map.csv`; rendered 22 atom-review HTML files for Gate 2 review. |
| DEC-010 | 2026-06-14 | Human accepted Gate 2 for `BATCH1_BINDING_GOVERNANCE_20260614T011101Z`; recorded `GATE2_BATCH1_20260614T023234Z`. |
| DEC-011 | 2026-06-14 | Completed Phase 2.5 refresh: rebuilt source catalog `SRCIDX_20260614T023650Z`, rebuilt BM25 retrieval with 12246 rows, confirmed `@repo/AGENTS.md` rank 1 for `derivative-package rule`, and generated Batch 1 `cross_source_toc_matrix.{md,csv}`. |
| DEC-012 | 2026-06-14 | Staged `BATCH2_AGENT_CONTRACTS_20260614T024251Z` as the next Phase 2 atomization batch: 37 agent-contract sources, 37 dispatch units, 37 repo-backed dispatch briefs; no atomization workers were run. |

## Gate 1 Acceptance

Gate 1 was accepted by human confirmation on 2026-06-14:

```text
I accept Gate 1
```

Acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z/`.

Gate 2 for Batch 1 was accepted by human confirmation on 2026-06-14:

```text
Gate 2 approved.  Proceed accordingly.
```

Acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z/`.

Batch 2 agent-contract setup is ready at `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T024251Z/`. Do not run Batch 2 atomization workers until explicitly authorized, and do not treat Batch 1 partial ledger as full-corpus decomposition truth.
