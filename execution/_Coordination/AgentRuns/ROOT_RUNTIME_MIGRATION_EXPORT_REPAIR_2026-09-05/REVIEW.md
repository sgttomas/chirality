# Export relocation repair review

Verdict: PASS for the three-file frozen diff. No actionable bug or boundary regression found. Parent /root; reviewer /root/runtime_workspace_move, ephemeral Agent 2, OpenAI GPT-6; exact serving model ID unavailable. Role instruction-asserted, not mechanically enforced.

The exporter no longer requires or reads the old Root runtime directory. It checks required source members at projects/chirality-runtime, then projects five explicit root files plus packages/ and tests/ into the unchanged public runtime/ path. Those allowlisted members cover all 79 tracked files in SOURCE_RELOCATION.json. Existing relative workspace references and package identities retain the same exported layout.

Project-level AGENTS.md, chirality.project.json, docs/, execution/ and loop/ cannot enter through the runtime copy because they are outside that allowlist. The existing recursive copy filter still excludes node_modules, build outputs and operational dot-directories beneath packages/tests. The runtime projection does not copy the projects ancestor, and private-top-level project exclusion remains unchanged. Missing destination members fail before staging-tree replacement.

Regression assertions require real source package bytes and a core implementation file, so a leftover ignored old directory cannot satisfy the previously weak empty-export outcome. The tests also assert absence of the newly introduced private project scaffold. The G4 manifest includes the new validation-test change and exporter consumer repair with bounded migration rationale. Existing guards and sanitizer remain in place.

No tests were rerun: parent owns execution evidence. This is code/boundary review of the exact hashes below, not authority acceptance, runtime release approval, export publication or PR-merge permission. The previous CI/tool search omitted exports/; this repair correctly covers that additional active source consumer without reopening historical documents.

Reviewed bytes:

- `exports/chirality-app/export_public.py`: SHA-256 `db0cfd1d8f68c9bd2a608b13581acf7424e6ef7cd40d9394b619e4c10a8e230a`
- `tools/validation/test_public_export_profile.py`: SHA-256 `725c0b694403d1d76d8a6cba62f4aed87b14fc8fb16a912856d333a5910b33e4`
- `docs/governance_harness/tranche_manifests/ROOT-RUNTIME-MIGRATION-20260905.yaml`: SHA-256 `0ec1ff7fd9c0b52a0b751a414b889be6e4464fa36d0516f116cee50807b0459a`
