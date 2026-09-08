# Sealed basis amendment — proof-closed publication candidate

This append-only amendment supersedes only the staged-selection counts, tree, and diff stated in `SEALED_BRIEF.md`. All purpose, authority, write scope, exclusions, and acceptance checks remain unchanged.

CHANGE expanded the subject to make the accepted manifests fail-closed and recomputable, then applied exact-path format declarations without changing accepted evidence bytes:

- proof-closed subject: 79 paths, comprising the original 68 unchanged paths, four missing proof files, and seven direct members required by the selected manifests;
- complete pre-existing staged set outside this Root run: 83 paths, comprising the 79 subject paths, `.gitattributes`, and three format-method records;
- exact index tree: `64f944b55cc69b34ecccaca585f4ca399354d8c5`;
- staged binary diff SHA-256: `4e00e0147eb66b779ce6a7aecc079c61ad87e2afc854110e12685df2b7f61577`;
- `.gitattributes` postimage SHA-256: `ebd621ac7c403ca0a3728cd07f8a7e76ddfc7f31110a7dffcaa5a5938fac40cf`, containing 17 exact-path representation declarations;
- format-method evidence: FORMAT `146d7fdbcf100b5b8aab7c0f7fd279dfce428cf0432979784b3659ff68c9f2ce`, CHECKS `9c87bad673302983bbe39b90d31bc17dfe703002b4b2881bf471c463c088030e`, MANIFEST `f809b877487e18e24b9607b63560681283f759708b3b4ea661985979e0dc2c7a`;
- candidate whitespace and `git diff --check`: PASS.

All 83 paths are read-only and must remain staged and byte-exact during Root authoring. Root outputs remain unstaged until CHANGE receives the final reviewed selection.
