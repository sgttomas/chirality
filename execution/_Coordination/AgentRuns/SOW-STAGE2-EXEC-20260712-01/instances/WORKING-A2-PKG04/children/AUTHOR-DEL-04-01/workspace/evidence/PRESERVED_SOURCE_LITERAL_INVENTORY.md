# Preserved Source Literal Inventory — DEL-04-01

Verdict: `PASS — GENERATED_EVIDENCE_PORTABLE`

The byte-identical seeded control files contain two machine-specific checkout
literals. They are classified `PRESERVED_SOURCE_LITERAL` and were not
normalized:

- `_REFERENCES.md:13`: literal-value SHA-256 `a3cac78bef681f58532728953499f8aae694018faf27eeaa3799ec607faaccd6`.
- `_DEPENDENCIES.md:54`: literal-value SHA-256 `caadd57123e88e03a00b4ee2a412b32d6e6043a93416845a02bb898e6ab1f37e`.

Both occurrences are accepted control content. Neither occurs in the four
production sources, `ScopeOfWork.md`, either rendered HTML derivative, or any
generated author evidence. Generated paths use repository-relative paths or
`{REPO_ROOT}` tokens.

Inventory counts:

- Seeded accepted source/control bytes: `2` occurrences, classified
  `PRESERVED_SOURCE_LITERAL`.
- Candidate and candidate copy: `0` occurrences.
- Render derivatives: `0` occurrences.
- Generated run/evidence metadata: `0` occurrences.
