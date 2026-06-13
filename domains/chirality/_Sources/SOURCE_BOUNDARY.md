# Chirality Domain Source Boundary

## Status

This source boundary defines the initial admitted corpus for
`domains/chirality/`.

## Source Model

The source corpus is manifest-referenced. Files are not copied into
`_Sources/`; instead, `_Sources/Source_Manifest.csv` records live repository
paths, authority roles, inclusion state, archive state, and expected SHA-256
hashes.

Catalog outputs use `@repo/<RepoRelPath>` as the artifact path. The source
catalog validator resolves these paths through the repository root and verifies
the recorded hashes.

## Included In V1

- Root framing and bootstrap documents.
- Root governance documents under `docs/`.
- Agent instruction contracts under `agents/`.
- Repo-native skill contracts under `skills/`.
- Tool registry and retrieval documentation.
- Public harness/export documentation.

## Excluded In V1

- `projects/`
- existing `domains/`
- `examples/`
- `.archive/`
- generated export staging
- dependency folders, caches, and build outputs
- non-governance code internals

## Downstream Status

This milestone creates retrieval-ready domain infrastructure only. It does not
create a DOMAIN_DECOMP category register, knowledge-type register, atom ledger,
hypergraph snapshot, or publication package.
