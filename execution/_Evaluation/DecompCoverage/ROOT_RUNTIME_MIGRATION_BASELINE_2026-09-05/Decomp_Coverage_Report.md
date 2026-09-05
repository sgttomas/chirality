# Root runtime migration source baseline audit

**Overall: BLOCKERS; closure readiness: FAIL under the current audit contract.** This does not revoke the owner's accepted SCA-004 basis or block preparation of the migration candidate. It identifies existing conformance debt for an explicit disposition before claiming clean scope-change closure. No Gate 1 confirmation is recorded.

Accepted upstream: `execution/_ScopeChange/SCA-004_2026-08-22_1749/`, decomposition revision 1.3; repository `5068899690ab2580fa3360f751f63952e6bdc563`. All seven authoritative live surfaces equal the accepted applied candidates byte for byte. All 785 measured execution inputs equal that pinned main commit. `INPUT_HASHES.csv` provides exact evidence identities.

## Verified topology and calibration

The live tree has **6 packages, 53 declared and materialized deliverables, 53 INITIALIZED status files, 104 ledger rows (95 IN / 9 OUT), and 7 objectives**. The historical handoff's 46-folder count is stale. DEL-02-07 through DEL-02-12 and DEL-04-11 all exist under their exact declared package/name paths. No migration deletion or missing carrier was found.

The software package uses descriptive suffixes in its authoritative IDs, despite the generic audit role's no-suffix example. Full authoritative IDs were compared directly with exact folder names. Context Package short IDs were compared with the corresponding declared ID prefix; both `ContextEnvelope` and `Context Envelope` labels were recognized.

## Core checks

| Check | Verdict | Evidence and interpretation |
|---|---|---|
| 1 Package forward coverage | PASS | All six exact package folders declared in the Packages section exist. |
| 2 Deliverable forward coverage | PASS | All 53 exact paths exist; `Decomp_Coverage_Matrix.csv`. |
| 3 Reverse coverage | PASS | No extra Root `PKG-*` or direct `1_Working/DEL-*` folders outside the declarations. |
| 4 ID consistency | PASS | Full declared package/deliverable identifiers equal folder identifiers. |
| 5 Context fidelity | PASS | 53 context mirrors match identity, package, type, responsibility, envelope and meaning; `Context_Comparison.csv`. DEL-04-06's description differs textually but preserves the shared CHANGE role, owner-proxy merge authority and K-MERGE-1; its additional citation is not semantic drift. |
| 6 Artifact and production contract presence | WARNING | All 53 carry ScopeOfWork.md only. The live common resolver validates 46 as SOW_V1 and reports seven INVALID contracts: DEL-02-07..12 and DEL-04-11. Raw errors in `Production_Contracts.csv` include missing AC definitions and output/evaluation matrix references/columns. These accepted-by-owner R7 files are preserved; this finding is current-validator conformance debt, not a claim they lack owner acceptance. 176 anticipated production outputs have no matching filename in their carrier; INFO because all carriers are INITIALIZED. |
| 7 Objective mapping | PASS | Seven objectives extracted from the authoritative ledger; each has materialized support. All objective companion support sets equal enumerated deliverable support; `Objective_Support.csv`. No deliverable lacks objective mapping. Fifteen IN ledger rows have blank direct ObjectiveIDs, counted explicitly; all have deliverable coverage, whose objectives provide indirect support. No unsupported objective is inferred. |
| 8 Ledger integrity | PASS | All 95 IN rows have declared, materialized package/unit references; 104 rows total. Cross-package coverage is permitted by accepted DEC-010. |
| 9 Derivative package parity | SKIPPED | Variant-owned parity check applies to DOMAIN. Exact SOFTWARE accepted source identities and objective companion parity were still measured independently. |
| 9b Package shape | PASS | Main document §3 explicitly distinguishes working surface and authoritative companions; heavy truth resides in registers. No publication derivative is substituted for authority. |
| 10 Active snapshot and handoff | BLOCKER | Pointer resolves one existing SCA-004 snapshot. Four filenames required by the current SCOPE_CHANGE layout are absent: Pre_Change_Coverage.json, Post_Change_Coverage.json, RUN_SUMMARY.md, Supersession_Map.csv. The actual pre/post audit evidence and fixed handoff fields exist elsewhere within that snapshot; layout absence is not evidence that owner gates never occurred. Its dated handoff also still describes seven folders/context propagation as pending, since completed; treat it as historical closure state, not live task selection. |
| 11 Lifecycle distribution | PASS | All 53 are INITIALIZED, zero UNKNOWN/RETIRED; no activation inferred. |

Optional comparison mode was not requested. All 12 core checks (1–9, 9b, 10, 11) are reported.

## What to fix for a cleaner rerun

1. Have the owning workflow disposition the four current-contract snapshot-layout gaps, preserving immutable historical SCA-004 evidence. A new reconciliation record can reference existing pre/post evidence and explain any non-applicable supersession map; do not fabricate retrospective decisions or overwrite accepted history merely to satisfy names.
2. Have the owning SOW workflow reconcile the seven current-validator findings against their exact R7 acceptance basis before relying on a claim of full current SOW schema conformance. Preserve accepted bytes until a scoped amendment is approved.
3. Carry the live 53-carrier denominator and deferred production-output state into migration accounting. Do not recreate the seven already materialized carriers or confuse materialization with activation.
4. Rerun after any accepted source/contract amendment or authority transfer, comparing this immutable baseline with the new source and destination packages. This snapshot is a derivative, and cannot confirm Gate 1 or transfer authority.

The 176 artifact rows measure filename presence within the owning folders, excluding ScopeOfWork and underscore metadata. They do not measure remote or externally stored acceptance evidence and are not a zero-productivity claim. The folders contain metadata/SOW/run records, not the anticipated named production outputs; candidate package acceptance elsewhere remains a separate authority question.
