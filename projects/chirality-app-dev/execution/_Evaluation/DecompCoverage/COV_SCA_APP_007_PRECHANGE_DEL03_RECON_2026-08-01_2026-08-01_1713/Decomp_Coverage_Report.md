# Decomposition Coverage Report — SCA-APP-007 Pre-change DEL-03 Reconciliation

**Status:** `WARNINGS`

**Authoritative input:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (`sha256:dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`)

**Authoritative companion:** `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` (`sha256:84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`)

**Expected source snapshot:** current accepted decomposition plus `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` (resolved to `SCA-APP-006_2026-07-27_1159_Invariant_Mapping_Repair/`)

**Expected handoff phase:** `SCA-APP-007 Gate 1 pre-change`

**Derivative purpose:** pre-change scope evidence; not decomposition truth

## Check summary

| Check | Verdict | Evidence |
|---|---|---|
| 1 Package forward coverage | PASS | 2/2 declared scoped packages resolve by stable ID |
| 2 Deliverable forward coverage | PASS | 10/10 declared scoped deliverables resolve; DEL-03-01..04 are present under the current PKG-03 root |
| 3 Reverse folder coverage | WARNING | PKG-03 has two physical roots and the historical root contains undeclared reverse-only DEL-03-06 |
| 4 ID consistency | PASS | All ten declared folder IDs match their decomposition package/deliverable IDs |
| 5 Context fidelity | PASS | 10/10 contexts are present and aligned, including ContextEnvelope |
| 6 Artifact presence | WARNING | Ten SOW_V1 contracts validate; named folder-local implementation artifacts remain unmatched |
| 7 Objective mapping | PASS | All 7 objective IDs supported by scoped deliverables have existing support; no scoped deliverable lacks objective mapping |
| 8 Ledger integrity | PASS | All 24 `IN` ledger rows involving scoped deliverables reference valid packages, deliverables, and objectives; one `TBD` and one `OUT` row were also checked |
| 9 Derivative-package parity | SKIPPED | Not variant-owned for SOFTWARE |
| 9b Package-shape conformance | PASS | Main/companion authority roles are explicit and the companion inventory is discoverable |
| 10 Active snapshot and handoff | PASS | `_LATEST.md` resolves exactly to SCA-APP-006; its required closure artifacts exist and its scope-change-only handoff is internally consistent |
| 11 Lifecycle distribution | PASS | All ten declared scoped deliverables are `IN_PROGRESS`; reverse-only DEL-03-06 has no current `_STATUS.md` and is `UNKNOWN` |
| 12 Comparison mode | SKIPPED | No `PRIOR_RUN_LABEL` requested |

## DEL-03 topology and history

### Current declared work

The current decomposition declares `DEL-03-01` through `DEL-03-04`, and all four folders exist at:

`projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/`

Their contexts match current package name, deliverable name, type, responsible party, description, objective mapping, and ContextEnvelope. Each is `IN_PROGRESS`; none is missing.

### DEL-03-05

`DEL-03-05` existed in the 2026-02-21 accepted decomposition as **Anthropic Provider Integration & Key Provisioning Contract**. Commit `92a25d2708dfb109790075513e920b5118f0b85c` deleted its 14-file deliverable kit on 2026-05-19 while replacing the old topology. The current decomposition has no DEL-03-05 declaration and the current filesystem has no DEL-03-05 folder, so there is no current forward- or reverse-coverage defect.

Its former concern was not simply lost: current `DEL-04-05` owns the App credential/client/network bridge and current `DEL-09-06` owns network, key, attachment, and renderer security checks. The current package description also excludes generic provider/runtime ownership from App PKG-03. This is a current decomposition mapping observation, not an assertion that every historical DEL-03-05 artifact was migrated.

### DEL-03-06

`DEL-03-06` likewise existed in the 2026-02-21 decomposition as **Outbound Network Guardrails (Anthropic-only) + Verification**. Its old deliverable kit and original proof were deleted in the same 2026-05-19 topology replacement. Later commits `4412157d1de854cd4df6b96c0d00ac6612eadb76` and `deed6f58fa0031d0dfa3b63085440b742d0c5fdd` reintroduced 38 tracked proof files under the old physical path without restoring a current decomposition row or deliverable metadata.

The result is a genuine current reverse-coverage discrepancy, not proof that the accepted decomposition omitted a newly intended deliverable. Current `DEL-09-06` expressly covers renderer allowlist, API key, provider endpoint, provider-expansion, and attachment security validation, and `frontend/scripts/run-network-policy-proof.mjs` still targets the old DEL-03-06 evidence path. SCOPE_CHANGE should therefore test evidence rehome and proof-runner retargeting against DEL-09-06 first; only residual scope not covered by accepted deliverables would justify a topology amendment.

## What to fix for a cleaner rerun

1. Through SCOPE_CHANGE, classify every tracked file under historical DEL-03-06 against current accepted owners, especially DEL-09-06, and record provenance for any migration.
2. Retarget `frontend/scripts/run-network-policy-proof.mjs` away from the undeclared historical root if DEL-09-06 is confirmed as the owner.
3. Remove the duplicate historical PKG-03 physical root only after its tracked evidence is preserved at an accepted location.
4. Rerun AUDIT_DECOMP post-change. A clean topology rerun should have one physical PKG-03 root and no reverse-only DEL-03-06 row.
