# Historical DEL-03-06 Evidence Migration Provenance

**Migration date:** 2026-08-01

**Authority:** SCA-APP-007, owner-approved Gates 1–4

**Accepted owner:** DEL-09-06 — Network, Key, Attachment, and Renderer Security Checks

**Disposition:** evidence-routing correction only; zero-byte decomposition amendment

## Ownership basis

The accepted decomposition assigns network guard tests, provider-expansion
guard tests, key storage checks, attachment validation, and renderer security
validation to `DEL-09-06`. The accepted runtime-stabilization plan assigns
`frontend/scripts/run-network-policy-proof.mjs` to `DEL-09-06`, and
SCA-APP-002 / D-APP-72 records the oMLX, key, and network security proof under
that deliverable. SCA-APP-007 therefore classifies the retired `DEL-03-06`
container as misrouted evidence, not as a decomposition member.

## Path mapping

- Old evidence root: `execution/PKG-03_Harness_Runtime_Core/1_Working/DEL-03-06_Outbound_Network_Guardrails/Evidence/`
- New evidence root: `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Historical_DEL-03-06/`
- Preserved historical bundle names: `OI-002_PROOF_2026-07-22_060044` and `OI-002_PROOF_2026-07-23_061410`
- Source commits: `4412157d1` and `deed6f58f`
- Historical source tree: `a5ba2c806734feeb68f6160f2961c6597d44b40d`

## Integrity result

- Evidence files: **38 pre-move / 38 post-move**
- Evidence bytes: **97,817 pre-move / 97,817 post-move**
- Per-file SHA-256 parity: **38/38 MATCH**
- Aggregate pre-audit hash (SHA-256 of the sorted pre-move `shasum -a 256` output): `e27ca076ec3fdaeb4f6ba6cba6e716aa50497e130e5b0e3feab5dbc800aca4ff`
- Aggregate post-audit hash after canonical substitution of the new root back to the old root: `e27ca076ec3fdaeb4f6ba6cba6e716aa50497e130e5b0e3feab5dbc800aca4ff`
- Exact parity result: **MATCH**

`MIGRATION_SHA256_MANIFEST.csv` records both old and new paths, byte counts,
pre-move and post-move SHA-256 values, and the per-file parity result. The
historical bundle contents were moved byte-for-byte and remain immutable.
Their retired names and internal historical claims are preserved as evidence;
they are not current deliverable or output-label authority.
