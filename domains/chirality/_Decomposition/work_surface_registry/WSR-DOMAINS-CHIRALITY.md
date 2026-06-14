# WSR-DOMAINS-CHIRALITY

## Registry Scope Note

This document is a work-surface registry source for later DOMAIN_DECOMP Phase 2 atomization. It records topology, ownership, and governance principles for the live `domains/chirality/` surface. It is not a decomposition ledger, atom CSV, vocabulary CSV, Gate packet, or source-manifest amendment.

## Work-Surface Identity and Role

- Work surface: `domains/chirality/`
- Registry document: `WSR-DOMAINS-CHIRALITY`
- Role: Chirality governance-core domain pack for retrieval-first self-knowledge workflows.

The local README states that this domain pack is the "Domain shell for Chirality's own governance-core knowledge" and that it treats the live repository as the source of truth rather than copying source files into the domain pack. Evidence: @repo/domains/chirality/README.md:L1-L8.

The domain pack configuration names the pack `chirality`, describes it as a governance-core domain pack, and declares local roots for `_Sources`, `_Decomposition`, `_Coordination`, `vocabularies`, and `_LocalIndexes`. Evidence: @repo/domains/chirality/domain-pack.yaml:L1-L12.

## Major Live Subareas

- `_Sources/`: Manifest-referenced source boundary. `_Sources/Source_Manifest.csv` records live repository paths, authority roles, inclusion state, archive state, and expected hashes; catalog outputs use `@repo/<RepoRelPath>` instead of copied source files. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L8-L17.
- `_Decomposition/`: Current domain-decomposition control and derivative execution surface. It contains the active decomposition working surface, source prefix map, validation/open-issue registers, phase batch registers, gate snapshots, dispatch plans, review surfaces, ledgers, and vocabulary maps. Directory evidence: @repo/domains/chirality/_Decomposition/.
- `_Coordination/`: Next-instance and workflow entry surface for Chirality DOMAIN_DECOMP. It points agents to AGENTS, DECOMP_BASE, DOMAIN_DECOMP, source-boundary files, decomposition state, and validation/open-issue surfaces. Evidence: @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L1-L27.
- `_LocalIndexes/`: Rebuildable retrieval/source database outputs. The README says generated local indexes are derived, rebuildable, and git-ignored except for the README and placeholder. Evidence: @repo/domains/chirality/README.md:L18-L19.
- `vocabularies/`: Local root named by the domain pack for vocabulary surfaces. Evidence: @repo/domains/chirality/domain-pack.yaml:L7-L12.
- `plans/`, `skills/`, and `tools/`: Present as local placeholder directories with no live source-bearing files beyond `.gitkeep` at inspection time. Directory evidence: @repo/domains/chirality/plans/, @repo/domains/chirality/skills/, @repo/domains/chirality/tools/.

## Organization and Apparent Rationale

The surface is organized around a manifest-referenced source model: source truth stays in live repo files, while the domain pack stores references, hashes, decomposition control, review packages, and derivative retrieval/index artifacts. This is directly stated in the README and source boundary. Evidence: @repo/domains/chirality/README.md:L5-L8; @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L10-L17.

The admitted V1 corpus is governance-focused: root framing/bootstrap documents, root governance docs, agent instruction contracts, repo-native skill contracts, tool registry/retrieval documentation, and selected export summary docs. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L19-L28.

Inference: `_Decomposition/` is intentionally a control-and-review surface rather than a raw source corpus. The coordination prompt lists decomposition control files, gate snapshots, batch setup/acceptance surfaces, validation checks, and open issues as current workflow inputs. Evidence: @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L10-L18.

## Ownership and Decomposition Boundary

This work surface owns Chirality governance-core domain knowledge: agent framework rules, agent instruction contracts, skill contracts, tool registry/retrieval documentation, root governance framing, and the DOMAIN_DECOMP state needed to atomize those sources.

This surface does not own active product implementation, project workspaces, examples, existing domain packs, generated export staging, dependency folders, caches, build outputs, or non-governance code internals. Those exclusions are explicit in the source boundary. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L29-L38.

Active frontend work is specifically outside this domain boundary and belongs under `projects/chirality-app-dev/`. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L40-L50.

## Execution and Governance Model

The workflow opens through DOMAIN_DECOMP. The coordination prompt requires reading AGENTS, DECOMP_BASE, DOMAIN_DECOMP, the `domain-source-atomize` skill before Phase 2 atomization, and the current decomposition/source surfaces. Evidence: @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L3-L25.

The active manifest and batch state are governed through explicit batch IDs, gate status, accepted/open status, validation warnings, and open issues. Evidence: @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L38-L55; @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L96-L143; @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L145-L201.

The prompt records that accepted Batch 1 is prior-boundary evidence for active reuse until carry-forward or rebaseline is accepted, and that later batches require human Gate 2 acceptance before becoming decomposition truth. Evidence: @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L28-L49; @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L203-L211.

The top-level agent index defines DOMAIN_DECOMP as the handbook/knowledge-domain decomposition persona and states that DOMAIN_DECOMP dispatches `TASK + domain-source-atomize` during Phase 2. Evidence: @repo/AGENTS.md:L63-L66; @repo/AGENTS.md:L114.

## Relationship to Chirality Domain Decomposition

This is the owning Chirality DOMAIN_DECOMP work surface. The registry document should be treated as a new source describing live repository topology, not as a replacement for existing source-manifest truth, accepted atom ledgers, or Gate decisions.

The registry should be admitted only if the owning workflow updates source-boundary/manifest state later. This task intentionally does not modify `Source_Manifest.csv`, batch registers, Gate snapshots, atom ledgers, vocabulary maps, or source catalog outputs.

## Explicit Exclusions

- `.archive/` and `_Archive/`.
- `projects/`, `frontend/`, existing `domains/`, and `examples/` as source truth for this Chirality governance-core pack unless explicitly admitted later. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L31-L38.
- Generated export staging, dependency folders, caches, and build outputs. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L35-L38.
- `_LocalIndexes/snapshots/` and other rebuildable retrieval/index output as source truth.
- Bulk generated `_Decomposition` batch outputs, including dispatch outputs, generated review HTML, generated source skeletons, per-source ledgers, source asset manifests, source pack markdown, and vocabulary seed batches. These are derivative review/processing packages unless separately accepted by the owning workflow.
- Retired/prior-boundary rows and companions as active source truth unless explicit carry-forward or rebaseline is accepted. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L40-L72.

## Review Flags

- The current active manifest state is not fully closed across batches: Batch 2, Batch 3, and Batch 4 still require human Gate 2 acceptance before their atoms become accepted decomposition truth. Evidence: @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L203-L211.
- Retained Batch 1 prior-boundary companions still reference retired sources, so downstream derivative packages must not be treated as current full-corpus truth without explicit carry-forward or rebaseline. Evidence: @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L69-L80.
- `plans/`, `skills/`, `tools/`, and `vocabularies/` are present locally, but only placeholder files were observed in `plans/`, `skills/`, and `tools/`; they should not be treated as additional source-bearing subareas without later review. Directory evidence: @repo/domains/chirality/plans/, @repo/domains/chirality/skills/, @repo/domains/chirality/tools/, @repo/domains/chirality/vocabularies/.

## Evidence References

- @repo/domains/chirality/README.md:L1-L19
- @repo/domains/chirality/domain-pack.yaml:L1-L12
- @repo/domains/chirality/_Sources/SOURCE_BOUNDARY.md:L1-L80
- @repo/domains/chirality/_Sources/Source_Manifest.csv:L1-L80
- @repo/domains/chirality/_Coordination/NEXT_INSTANCE_PROMPT.md:L1-L231
- @repo/AGENTS.md:L63-L66
- @repo/AGENTS.md:L114
- Directory evidence: @repo/domains/chirality/_Decomposition/, @repo/domains/chirality/_Sources/, @repo/domains/chirality/_Coordination/, @repo/domains/chirality/_LocalIndexes/
