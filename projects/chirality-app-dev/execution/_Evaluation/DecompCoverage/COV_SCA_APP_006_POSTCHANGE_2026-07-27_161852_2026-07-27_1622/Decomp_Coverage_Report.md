# Decomposition Coverage Report — SCA-APP-006 Post-change

**Status:** `WARNINGS`
**Authoritative input:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (`sha256:dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`)
**Authoritative companion:** `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` (`sha256:84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`)
**Expected source snapshot:** `execution/_ScopeChange/SCA-APP-006_2026-07-27_1159_Invariant_Mapping_Repair/`
**Expected handoff phase:** `SCOPE_CHANGE_GATE5_POSTCHANGE`
**Derivative purpose:** post-change closure evidence; not decomposition truth

## Check summary

| Check | Verdict | Evidence |
|---|---|---|
| 1 Package forward coverage | PASS | 10/10 declared product packages resolve by stable ID |
| 2 Deliverable forward coverage | PASS | 51/51 declared product deliverables resolve |
| 3 Reverse folder coverage | WARNING | PKG-00 and DEL-00-01/02 are intentional control surfaces; DEL-03-06 is undeclared historical residue |
| 4 ID consistency | PASS | All 51 declared folder IDs match their decomposition package/deliverable IDs |
| 5 Context fidelity | PASS | 51/51 contexts present and aligned; all seven SCA-propagated contexts pass |
| 6 Artifact presence | WARNING | 51 SOW_V1 contracts validate; named folder-local implementation artifacts remain unmatched |
| 7 Objective mapping | PASS | 10/10 objectives supported by existing declared deliverables; zero unmapped deliverables |
| 8 Ledger integrity | PASS | 78 rows total; every one of 73 `IN` rows references valid package, deliverable, and objective IDs |
| 9 Derivative-package parity | SKIPPED | Not variant-owned for SOFTWARE |
| 9b Package-shape conformance | PASS | Main/companion authority roles and field precedence are explicit; the 81-ID/48-family register is discoverable; topology remains 10/51 |
| 10 Active snapshot and handoff | PASS | `_LATEST.md` resolves exactly to SCA-APP-006; required artifacts exist and interim run/handoff state truthfully awaits this audit |
| 11 Lifecycle distribution | PASS | 51 declared product deliverables are `IN_PROGRESS` |
| 12 Comparison mode | SKIPPED | No `PRIOR_RUN_LABEL` requested |

## SCA-APP-006 closure findings

- Exact Gate-5 state validation passes: both accepted candidate manifests reproduce, 12 amendment rows resolve, applied authoritative hashes match, and no unexpected changed path exists.
- The companion register contains 81 unique invariant IDs in 48 families, and all referenced App package/deliverable IDs resolve.
- Section 8 / Section 9 assignment parity, seven accepted mapping amendments, and all seven propagated contexts are reflected in the applied state.
- No stable ID, package membership, deliverable count, objective count, context envelope, lifecycle state, dependency, estimate, schedule, or implementation authority changed.
- The active snapshot accurately states that post-change audit and final SCOPE_CHANGE assembly remain outstanding; it does not overclaim closure.

## What remains for the managing SCOPE_CHANGE instance

1. Copy or cite this immutable audit in the SCA-APP-006 closure package.
2. Finalize `Post_Change_Coverage.json`, `RUN_SUMMARY.md`, and `Handoff_State.md` without claiming implementation or contract reconciliation.
3. Update `_ScopeChange/_LATEST.md` only to transition the active SCA-APP-006 snapshot from pending-audit to its approved closure state.
4. Preserve all warning-class historical/control/artifact observations; none is a new amendment blocker.
