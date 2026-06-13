# Chirality Domain Pack

Domain shell for Chirality's own governance-core knowledge.

This domain pack treats the live repository as the source of truth. The first
milestone is retrieval-first: `_Sources/Source_Manifest.csv` admits selected
repo files by path and SHA-256, and the source catalog stores `@repo/...`
references instead of copying source files into this domain pack.

Initial scope is the Chirality governance and agent-operating-system surface:
root framing documents, root governance documents, agent contracts, skill
contracts, tool registry documents, and harness/export documentation.

Out of scope for the initial corpus: private project workspaces, existing
domain packs, public examples, archives, generated export staging, caches,
build outputs, and non-governance code internals.

Generated local indexes under `_LocalIndexes/` are derived, rebuildable, and
ignored by git except for the README and placeholder.
