# Preserved Source Literal Inventory — DEL-03-03 Verifier

Verdict: `PASS — GENERATED_EVIDENCE_PORTABLE`

The accepted control files contain two machine-specific checkout literals:

- `_REFERENCES.md` `REF-007` Source field at line 13; literal-value SHA-256 `a3cac78bef681f58532728953499f8aae694018faf27eeaa3799ec607faaccd6`.
- `_DEPENDENCIES.md` decomposition-authority note at line 52; literal-value SHA-256 `caadd57123e88e03a00b4ee2a412b32d6e6043a93416845a02bb898e6ab1f37e`.

Both are classified `PRESERVED_SOURCE_LITERAL`. The accepted bytes were not normalized. Each literal appears in two byte-identical verifier copies:

- the corresponding accepted control file at `workspace/` root;
- the corresponding accepted control file under `workspace/legacy_state/`.

Inventory counts:

- Unique accepted source/control literals: `2`.
- Byte-identical copied occurrences: `4`, all classified `PRESERVED_SOURCE_LITERAL`.
- Candidate: `0` occurrences.
- Render derivatives: `0` occurrences.
- Genuinely generated verifier metadata/evidence outside this explicit inventory: `0` occurrences.

Generated paths use repository-relative paths or `{REPO_ROOT}` tokens.
