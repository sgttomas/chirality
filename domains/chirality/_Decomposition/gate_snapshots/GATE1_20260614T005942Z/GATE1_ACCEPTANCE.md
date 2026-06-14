# Gate 1 Acceptance - Chirality DOMAIN_DECOMP

Package role: snapshot / handoff artifact

Gate: Gate 1 Intake

Status: ACCEPTED

Accepted UTC: 2026-06-14T00:59:42Z

Human confirmation:

```text
I accept Gate 1
```

## Accepted Intake

- Domain root: `domains/chirality`
- Working surface: `domains/chirality/_Decomposition/Chirality_Domain_Decomposition.md`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `f072b1d43eb98b057cdb392a674bc9e7feaffbe483c7f59a06f5557219762fb1`
- Source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T005449Z`
- Catalog schema: `chirality-source-db/v2`
- Retrieval index status: `BM25_ONLY`
- Source-copy policy: `source_files_copied=false`

## Accepted Telemetry

- Manifest source rows: 242
- Skeletons generated: 242
- Review HTML files generated: 242
- Section-node CSVs generated: 242
- Total sections: 4449
- In-scope sections: 4446
- Dispatch units: 242
- Oversized dispatch units: 0
- Deferred sources: 1
- Skeleton failures: 0

## Accepted Decisions

- `SRC-LICENSE` remains `AtomizeInV1=NO`, `InOutDefault=OUT`, with a synthetic OUT review section and no Phase 2 dispatch unless the human later changes the source-boundary decision.
- `SRC-DOCS-THESIS-GLOSSARY` is admitted in scope for v1 atomization and has one dispatch unit.
- Manifest-backed Phase 2 SourceRefs use `@repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>`.
- Per-kind asset review surfaces are N/A for Markdown-only manifest rows unless future source rows carry actual asset manifests.

## Gate 1 Verdict

The manifest-backed source set, source-prefix map, skeleton inventory, and deferred-source decisions are accepted as the intended Chirality DOMAIN_DECOMP intake.

Phase 2 atomization has not started.
