# Gate 1 Handoff State - Chirality DOMAIN_DECOMP

Package role: snapshot / handoff artifact

Status: Gate 1 accepted; Phase 2 atomization not started.

## Accepted Upstream Snapshot

- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T005449Z`
- Catalog validation: PASS, 0 blockers, 0 warnings
- Retrieval status: BM25_ONLY, 4523 chunks

## Derivative-Package Status

- `_LocalIndexes/snapshots/SRCIDX_20260614T005449Z` is a derived local source-catalog/retrieval package.
- `_Decomposition/source_asset_manifests/`, `source_skeletons/`, `source_dispatch_plans/`, `source_review_html/`, and `source_section_nodes/` are DOMAIN_DECOMP companion artifacts generated from the accepted live repo source manifest.
- No Domain Ledger, Category Register, KTY Register, Knowledge Subject Register, hypergraph snapshot, or publication package exists yet.

## Closure Verdict

- Gate 1 Intake: CLOSED / ACCEPTED.
- Gate 1 closure basis: human confirmation on 2026-06-14 plus current validation checks in `Validation_Checks.csv`.
- Phase 2: NOT STARTED.

## Rerun Requirements

- If any admitted source file changes, update `Source_Manifest.csv`, rebuild the source catalog, rebuild BM25, regenerate the manifest-backed adapter companions, and revalidate before using retrieval or dispatch plans as evidence.
- If `tools/decomp/build_source_skeleton.py`, `tools/decomp/build_manifest_domain_adapter.py`, `tools/decomp/build_atomization_brief.py`, or `skills/domain-source-atomize/` changes before Phase 2 dispatch, rerun the affected tests and regenerate any stale Batch 0 companions.
- If future sources include actual assets, revisit the Gate 1.5 asset-surface N/A policy before atomization.

## Remaining Blockers And Next Action

- `OI-005` remains open for Phase 2 staging: full 242-file atomization must not run as one unbatched review gate.
- Next DOMAIN_DECOMP action is staged Phase 2 setup for Batch 1 binding-governance sources, using the accepted repo-backed SourceRef policy and the accepted dispatch inventory.
- Do not run `TASK + domain-source-atomize` fan-out unless explicitly requested for the next staged batch.
