# QA Report

## Scan coverage

- Parsed `Packages`, `Deliverables`, and `Scope Ledger` by semantic heading; SOFTWARE objective mapping used Scope Ledger `ObjectiveID(s)` plus deliverable reverse views.
- Audited `PKG-03` and `PKG-09`: 2 packages, 10 deliverables, and 7 objective IDs supported by those deliverables.
- Scanned all physical `PKG-03_*` and `PKG-09_*` roots and confirmed exactly one root for each scoped stable package ID.
- Read all ten scoped `_CONTEXT.md` and `_STATUS.md` files.
- Rechecked the same 26 ledger rows used in the pre-change baseline: 24 `IN`, one `TBD`, and one `OUT` row involving a scoped package or deliverable.
- Inspected SCA-APP-007 migration provenance, its 38-row SHA-256 manifest, the new evidence destination, the absent old root, and the proof runner's current destination and label.
- Resolved `_ScopeChange/_LATEST.md` to the closed SCA-APP-006 snapshot and inspected its declared closure state. It remains the active pointer by explicit override.

## Parse and integrity results

- All required semantic headings resolved unambiguously.
- All ten declared deliverable folders were found and their stable IDs and context fields matched.
- Current repository topology remains 10 packages, 51 deliverables, 10 objectives, 78 scope items, and 78 ledger rows; scoped counts are reported separately.
- Current scoped physical topology is 2 package roots and 10 deliverable folders: DEL-03-01 through DEL-03-04 and DEL-09-01 through DEL-09-06.
- `PKG-03_Harness_Runtime_Core` and its former reverse-only DEL-03-06 container are absent.
- The new `Historical_DEL-03-06` evidence surface contains 38 historical proof files plus `PROVENANCE.md` and `MIGRATION_SHA256_MANIFEST.csv`. The manifest has 38 rows, 38 `MATCH` results, and 97,817 bytes.
- `frontend/scripts/run-network-policy-proof.mjs` now targets accepted `DEL-09-06/Evidence/NETWORK_POLICY_PROOF_*` and no longer uses DEL-03-06 or current `OI-002` output labels.
- The decomposition and authoritative companion hashes match the pre-change run; SCA-APP-007 required a zero-byte decomposition amendment.

## Limits

- Artifact presence remains a conservative deliverable-folder filename check. It does not prove implementation evidence elsewhere in the repository is absent.
- Historical bundle names and internal historical claims remain evidence provenance, not current decomposition or output-label authority.
- This snapshot validates the post-change filesystem state. Final SCA-APP-007 Gate-5 acceptance and lifecycle closeout belong to SCOPE_CHANGE and the human owner.
