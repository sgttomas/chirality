# WSR-DOMAINS-PIPING-DESIGN

## Registry Scope Note

This document is a work-surface registry source for later DOMAIN_DECOMP Phase 2 atomization. It records topology, ownership, and governance principles for the live `domains/piping-design/` surface. It is not a decomposition ledger, atom CSV, vocabulary CSV, Gate packet, or source-manifest amendment.

## Work-Surface Identity and Role

- Work surface: `domains/piping-design/`
- Registry document: `WSR-DOMAINS-PIPING-DESIGN`
- Role: Piping-design domain pack for source corpora, extraction products, and domain-decomposition preparation.

The README describes this as a "Domain shell for piping-design knowledge, decomposition state, and local source corpora." Evidence: @repo/domains/piping-design/README.md:L1-L5.

The domain pack configuration names the pack `piping-design`, describes it as a Chirality workflow domain pack, and declares local roots for `_Sources`, `_Decomposition`, `_Coordination`, and `vocabularies`. Evidence: @repo/domains/piping-design/domain-pack.yaml:L1-L10.

## Major Live Subareas

- `_Sources/`: Authoritative source-corpus root. `_Sources/_LATEST.md` lists the live source set: `MWK_1956/`, `Piping_Manual/`, `Process-Piping-Design-Rip-Weaver-Volume-1/`, `Process-Piping-Design-Rip-Weaver-Volume-2/`, `Pipe-Stress-Engineering/`, and `industry-practices/`. Evidence: @repo/domains/piping-design/_Sources/_LATEST.md:L1-L8.
- Five named book/extraction folders under `_Sources/`: Each contains an assembled Markdown source, section-node CSV, asset manifest, and supporting `audit/` or `tables/` artifacts where present. Directory evidence: @repo/domains/piping-design/_Sources/MWK_1956/, @repo/domains/piping-design/_Sources/Piping_Manual/, @repo/domains/piping-design/_Sources/Process-Piping-Design-Rip-Weaver-Volume-1/, @repo/domains/piping-design/_Sources/Process-Piping-Design-Rip-Weaver-Volume-2/, @repo/domains/piping-design/_Sources/Pipe-Stress-Engineering/.
- `_Sources/industry-practices/`: Multi-chapter industry-practices corpus. Its NOTE describes the collection as a private knowledge base of piping-design industry practices meant to provide design-judgment context, while explicitly not including underlying codes. Evidence: @repo/domains/piping-design/_Sources/industry-practices/NOTE.md:L1-L8.
- `plans/`: Contains live planning surfaces for PDF2MD campaign continuation and export-format interoperability. Evidence: @repo/domains/piping-design/plans/INDUSTRY_PRACTICES_PDF2MD_CAMPAIGN_RESUME.md:L1-L18; @repo/domains/piping-design/plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md:L1-L15.
- `_Decomposition/`: Decomposition-state root declared by the domain pack. No live accepted decomposition package was identified in this registry pass; the observed `.proof-case/` content is excluded below because it marks itself archived. Evidence for the declared root: @repo/domains/piping-design/domain-pack.yaml:L7-L10.
- `_LocalIndexes/`: Rebuildable local source database and retrieval-index area. Evidence: @repo/domains/piping-design/_LocalIndexes/README.md:L1-L5.
- `skills/`, `tools/`, and `vocabularies/`: Present as local placeholder roots with `.gitkeep` only at inspection time. Directory evidence: @repo/domains/piping-design/skills/, @repo/domains/piping-design/tools/, @repo/domains/piping-design/vocabularies/.

## Organization and Apparent Rationale

The surface is organized around source corpora first, with decomposition state and indexes as secondary processing/governance surfaces. This is directly supported by the README, the domain pack roots, and `_Sources/_LATEST.md`. Evidence: @repo/domains/piping-design/README.md:L3-L5; @repo/domains/piping-design/domain-pack.yaml:L7-L10; @repo/domains/piping-design/_Sources/_LATEST.md:L1-L8.

The `industry-practices/` subarea is organized by topical chapter folders. The PDF2MD campaign plan records a corpus of 108 PDFs across 19 chapter folders and gives chapter completion status, which supports interpreting the numbered directories as a managed conversion campaign rather than arbitrary file grouping. Evidence: @repo/domains/piping-design/plans/INDUSTRY_PRACTICES_PDF2MD_CAMPAIGN_RESUME.md:L3-L18; @repo/domains/piping-design/plans/INDUSTRY_PRACTICES_PDF2MD_CAMPAIGN_RESUME.md:L26-L52.

Inference: `audit/`, `tables/`, section-node CSVs, and asset manifests are support artifacts for source review and later atomization; the registry should cite their presence as structural evidence but should not atomize them as separate implementation details in this topology pass.

## Ownership and Decomposition Boundary

This work surface owns piping-design knowledge source material and extraction state for domain atomization. It is concerned with domain knowledge, design-practice corpora, source conversion status, local retrieval indexes, and future domain-decomposition preparation.

This work surface does not own OpenPipeStress implementation code, app tranches, schemas, runtime tests, desktop packaging, or project lifecycle state. Those belong under `projects/chirality-piping/` and should be decomposed through that project work surface.

The `industry-practices` NOTE explicitly frames the corpus as design-stage context, not code-compliance content. Evidence: @repo/domains/piping-design/_Sources/industry-practices/NOTE.md:L5-L8.

## Execution and Governance Model

PDF-to-Markdown conversion is managed as a campaign with per-PDF workflow, filesystem audits, validation, chapter gates, and resume points. Evidence: @repo/domains/piping-design/plans/INDUSTRY_PRACTICES_PDF2MD_CAMPAIGN_RESUME.md:L11-L23; @repo/domains/piping-design/plans/INDUSTRY_PRACTICES_PDF2MD_CAMPAIGN_RESUME.md:L56-L65.

The export interoperability plan is a planning surface that connects the piping-design knowledge domain to downstream model/export strategy. It frames the app as a local-first open model authoring and solver-handoff workbench, with downstream tools responsible for formal analysis, code compliance, reporting, and professional design acceptance. Evidence: @repo/domains/piping-design/plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md:L17-L34; @repo/domains/piping-design/plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md:L87-L112.

## Relationship to Chirality Domain Decomposition

This registry describes a domain pack adjacent to the Chirality governance-core domain. It can be admitted later as a topology source for the Chirality DOMAIN_DECOMP workflow, but it is not itself accepted decomposition truth for either domain.

If admitted, atomization should describe the organization of the live domain surface and its source-boundary posture, not the technical content of the piping books, industry-practice chapters, equations, or tables.

## Explicit Exclusions

- `.archive/` and `_Archive/`.
- `_Sources/*_pdf2md_work/` and per-PDF working directories as generated conversion scratch.
- `_LocalIndexes/` generated retrieval/index artifacts, except the README as structural evidence.
- `_Decomposition/.proof-case/` as authoritative decomposition truth; its README explicitly marks it archived and not the next decomposition. Evidence: @repo/domains/piping-design/_Decomposition/.proof-case/README.md:L7-L12.
- Bulk extraction support artifacts such as `audit/`, `tables/`, asset manifests, and section-node CSVs as atomization targets in this registry pass. Their presence is structural evidence only.
- OpenPipeStress implementation code, project execution state, and app validation artifacts under `projects/chirality-piping/`.

## Review Flags

- `_Decomposition/.proof-case/` is inside a live domain directory but explicitly says "Status: archived. Not the start of the next decomposition." It should remain excluded from authoritative decomposition truth unless a human later accepts it as historical evidence only. Evidence: @repo/domains/piping-design/_Decomposition/.proof-case/README.md:L7-L12.
- The `industry-practices` corpus contains private knowledge-base material and source-organization attribution. Any later admission should preserve the existing boundary that these sources provide design-judgment context and are not redistributed code content. Evidence: @repo/domains/piping-design/_Sources/industry-practices/NOTE.md:L5-L8; @repo/domains/piping-design/_Sources/industry-practices/NOTE.md:L25-L31.
- Local `skills/`, `tools/`, and `vocabularies/` directories currently appear as placeholders. Do not infer live local skill/tool/vocabulary contracts from them without later inspection. Directory evidence: @repo/domains/piping-design/skills/, @repo/domains/piping-design/tools/, @repo/domains/piping-design/vocabularies/.

## Evidence References

- @repo/domains/piping-design/README.md:L1-L5
- @repo/domains/piping-design/domain-pack.yaml:L1-L10
- @repo/domains/piping-design/_Sources/_LATEST.md:L1-L8
- @repo/domains/piping-design/_Sources/industry-practices/NOTE.md:L1-L35
- @repo/domains/piping-design/plans/INDUSTRY_PRACTICES_PDF2MD_CAMPAIGN_RESUME.md:L1-L70
- @repo/domains/piping-design/plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md:L1-L143
- @repo/domains/piping-design/_Decomposition/.proof-case/README.md:L1-L56
- @repo/domains/piping-design/_LocalIndexes/README.md:L1-L5
- Directory evidence: @repo/domains/piping-design/_Sources/, @repo/domains/piping-design/_Decomposition/, @repo/domains/piping-design/plans/
