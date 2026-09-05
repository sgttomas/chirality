# Gate-3 Candidate Validation — SCA-APP-010

**Basis:** `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`
**Mode:** static candidate validation in the SCA snapshot; no Gate-5 application, no live-file write, no post-change audit.

| Check | Result |
| --- | --- |
| Worktree basis and cleanliness | PASS — branch `claude/sca-app-010-gate1-intake` at the basis; only SCA-APP-010 snapshot files and the receipts ledger differ from `origin/main`. |
| Decomposition pre-image SHA-256 | PASS — `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`. |
| Decomposition exact post-image | PASS — `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`; builder exit 0. |
| Decomposition diff whitespace | PASS — `git diff --no-index --check` empty; trailing newline preserved. |
| SSOW / Scope Ledger counts | PASS — 84 / 84; IDs unique; sets equal. |
| Scope disposition counts | PASS — IN 79 / OUT 4 / TBD 1. |
| Package / deliverable / objective counts | PASS — 10 / 52 / 10. |
| Context envelope counts | PASS — S9 / M41 / L2 / XL0. |
| Scope Ledger ↔ Deliverables reverse relations | PASS — zero missing, zero extra across all 84 ledger rows and 52 deliverable rows. |
| New ID collision scan | PASS — SOW-081 to SOW-084, DEC-025, OI-008 absent from the pre-image (builder refuses otherwise). |
| Transaction anchors | PASS — every anchor matched exactly one line and every in-line substring occurred exactly once (builder fails closed otherwise). |
| Companion pre-image SHA-256 | PASS — `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`. |
| Companion exact post-image | PASS — `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`. |
| Companion CSV structure | PASS — 18 columns, 83 rows, 83 unique IDs, 50 families, no row-width drift. |
| Companion semantic-diff bound | PASS — 83 pin rebinds; exactly one row (K-PATH-2) changes beyond the pin: `AppDeliverableIDs` gains `DEL-07-03`, `RationaleEvidenceAnchor` gains `#SOW-081`; contract pins and ownership unchanged. |
| Amendment action register | PASS — 30 rows (25 MODIFY, 5 ADD); every builder transaction maps to an action; `SupersessionBindingPresent=YES` set equals the delta's DecisionID set. |
| Supersession delta / cumulative map | PASS — 11 delta rows; cumulative map 45 rows from SCA-APP-009's 34; accumulator findings 0 total, 0 blocking. |
| Pre-change coverage JSON | PASS — `Pre_Change_Coverage.json` is the exact Gate-1 audit `coverage_summary.json`. |
| Independent Gate-3 review | PASS — 0 BLOCKER / 0 MAJOR / 3 MINOR (documentation-only, corrected in the package; post-images unchanged); `Evidence/Gate3/GATE3_INDEPENDENT_REVIEW.md` SHA-256 `8c4b1ef94edbf2ecfbe5800a3d1a54dc801a98c3160a02b9bab81465920abec6`. |

## Not run at Gate 3

Post-change AUDIT_DECOMP, post-change coverage, companion reconciliation
against applied bytes, authority-corpus post-application status, dependency
extraction and closure, snapshot layout verification, and pointer parity
are `NOT_RUN_GATE3`; they belong to the owner-approved Gate-5 transaction.
