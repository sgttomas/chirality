# Decomposition Coverage Report — SCA-APP-007 Post-change DEL-03 Reconciliation

**Status:** `WARNINGS`

**Authoritative input:** `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (`sha256:dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`)

**Authoritative companion:** `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` (`sha256:84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`)

**Expected source snapshot:** current accepted decomposition plus SCA-APP-007 Gate-5 migrated filesystem

**Expected handoff phase:** `SCA-APP-007 Gate 5 post-change`

**Derivative purpose:** post-change scope evidence; not decomposition truth

## Check summary

| Check | Verdict | Evidence |
|---|---|---|
| 1 Package forward coverage | PASS | 2/2 declared scoped packages resolve by stable ID |
| 2 Deliverable forward coverage | PASS | 10/10 declared scoped deliverables resolve; DEL-03-01..04 and DEL-09-01..06 are present |
| 3 Reverse folder coverage | PASS | Exactly one physical root exists for each scoped package, and no undeclared scoped deliverable folder exists |
| 4 ID consistency | PASS | All ten declared folder IDs match their decomposition package/deliverable IDs |
| 5 Context fidelity | PASS | 10/10 contexts are present and aligned, including ContextEnvelope |
| 6 Artifact presence | WARNING | Ten SOW_V1 contracts validate; named folder-local implementation artifacts remain unmatched |
| 7 Objective mapping | PASS | All 7 objective IDs supported by scoped deliverables have existing support; no scoped deliverable lacks objective mapping |
| 8 Ledger integrity | PASS | All 24 `IN` ledger rows involving scoped deliverables reference valid packages, deliverables, and objectives; one `TBD` and one `OUT` row were also checked |
| 9 Derivative-package parity | SKIPPED | Not variant-owned for SOFTWARE |
| 9b Package-shape conformance | PASS | Main/companion authority roles and companion inventory are explicit |
| 10 Active snapshot and handoff | PASS | `_ScopeChange/_LATEST.md` still resolves exactly to SCA-APP-006; its required closure artifacts and handoff state remain internally consistent |
| 11 Lifecycle distribution | PASS | All ten declared scoped deliverables are `IN_PROGRESS` |
| 12 Comparison mode | SKIPPED | No `PRIOR_RUN_LABEL` requested; the targeted pre/post comparison is stated below |

## SCA-APP-007 post-change proof

The pre-change audit reported two Check-3 topology warnings:

1. Two physical roots resolved to PKG-03.
2. The historical root contained an undeclared reverse-only DEL-03-06 folder with 38 proof files.

Both are resolved. The only current PKG-03 root is:

`projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/`

It contains exactly the accepted DEL-03-01 through DEL-03-04 folders. `projects/chirality-app-dev/execution/PKG-03_Harness_Runtime_Core/` does not exist, so neither a duplicate PKG-03 root nor a reverse-only DEL-03-06 deliverable is discoverable.

The 38 historical proof files are preserved under:

`projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Historical_DEL-03-06/`

The migration manifest records 38 rows, 38/38 matching pre/post SHA-256 values, and 97,817 total bytes. `PROVENANCE.md` identifies the old and new roots, accepted owner, source commits, historical tree, and zero-byte decomposition disposition. These evidence subfolders do not match the production-unit folder pattern and therefore do not create reverse decomposition members.

The proof runner now routes future output to `DEL-09-06/Evidence/NETWORK_POLICY_PROOF_<timestamp>`. Its current path and output label contain neither DEL-03-06 nor OI-002. Preserved historical bundle names remain unchanged as provenance.

## Scoped and repository topology

| Measure | Scoped | Repository |
|---|---:|---:|
| Packages | 2 declared / 2 found | 10 |
| Deliverables | 10 declared / 10 found | 51 |
| Objectives | 7 supported in scope | 10 |
| Scope items / ledger rows | 26 examined for scoped involvement | 78 / 78 |
| Reverse-only deliverables | 0 | Not evaluated outside scope |

## Delta from pre-change targeted findings

| Metric | Pre-change | Post-change | Delta |
|---|---:|---:|---:|
| Blockers | 0 | 0 | 0 |
| Warnings | 12 | 10 | -2 |
| Duplicate scoped package roots | 1 | 0 | -1 |
| Reverse-only scoped deliverable folders | 1 | 0 | -1 |
| Scoped reverse coverage | 90.9% | 100.0% | +9.1 pp |

No new blocker or warning was introduced. The ten remaining warnings are the same anticipated-artifact filename observations as the pre-change baseline.

## What to fix for a cleaner rerun

The SCA-APP-007 topology repair needs no further decomposition correction. The remaining ordinary work is for the ten scoped deliverable owners to materialize or link the named anticipated implementation artifacts as their `IN_PROGRESS` work matures. This does not block SCA-APP-007 Gate-5 fan-in.

Per the sealed brief, `_Evaluation/DecompCoverage/_LATEST.md` remains unchanged and continues to identify the prior active audit snapshot.
