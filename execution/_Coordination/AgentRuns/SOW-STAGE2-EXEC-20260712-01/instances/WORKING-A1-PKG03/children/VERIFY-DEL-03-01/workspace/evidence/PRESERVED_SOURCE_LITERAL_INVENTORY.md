# Preserved Source Literal Inventory — DEL-03-01 Verifier

Verdict: `PASS — GENERATED_EVIDENCE_PORTABLE`

The accepted control file `_REFERENCES.md` contains one machine-specific checkout literal in the `REF-007` Source field at line 13. It is classified `PRESERVED_SOURCE_LITERAL`; its literal-value SHA-256 is `a3cac78bef681f58532728953499f8aae694018faf27eeaa3799ec607faaccd6`.

The accepted bytes were not normalized. The same single accepted literal appears in two byte-identical verifier copies:

- `workspace/_REFERENCES.md:13`
- `workspace/legacy_state/_REFERENCES.md:13`

Inventory counts:

- Unique accepted source/control literals: `1`.
- Byte-identical copied occurrences: `2`, both classified `PRESERVED_SOURCE_LITERAL`.
- Candidate: `0` occurrences.
- Render derivatives: `0` occurrences.
- Genuinely generated verifier metadata/evidence outside this explicit inventory: `0` occurrences.

Generated paths use repository-relative paths or `{REPO_ROOT}` tokens.
