# Gate-5 Reconciliation — SCA-APP-010

**Date:** 2026-09-04
**Basis:** `11b47882f7e8726a42829cd26db5ecd8383f43b5` (fast-forward descendant of approval basis `95b5687a7c9a4c6fe6e655f628495dec08ce04d8`)
**Result:** `PASS`

## Authority corpus

From the App working root, HELP_HUMAN ran after applying the authoritative pair:

`python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`

Exit zero; `current_version: v20`; every governed member `[MATCH]`; `no drift.`
The decomposition and companion register are not members of the v20 corpus,
so the amendment requires no corpus bump and no `_REFERENCES.md` rewrite.

## Companion register against the applied decomposition

| Check | Result |
| --- | --- |
| Live decomposition SHA-256 | `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (approved post-image) |
| Live companion SHA-256 | `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (approved post-image) |
| Companion structure | 83 rows, 83 unique IDs, 50 families, 18 columns |
| Decomposition pins | 83 of 83 rows carry `#candidate-sha256=c7c05169…`, the live decomposition identity |
| Semantic change beyond the pin | K-PATH-2 only: `AppDeliverableIDs` gains `DEL-07-03`; `RationaleEvidenceAnchor` gains `#SOW-081` |
| Contract pins | all 83 `ContractSourceSHA256` values unchanged (`842bf170…`); `docs/CONTRACT.md` unchanged |
| Diff parity | live `git diff -U0` equals `Gate3/COMPANION_DIFF.patch` and `Gate3/DECOMP_DIFF.patch` |

## Supersession map

`accumulate_supersession_map.py` with the SCA-APP-009 map and this
amendment's 11-row delta regenerated 45 rows with zero findings and
byte-parity (after CRLF normalisation) with `Supersession_Map.csv`,
SHA-256 `2045684e8d2d1aff5a46663016f07c16f0c60462c8c8d729ea3c3c1a64f8dbb6`.

## Not reconciled here

Deliverable-local working surfaces of the thirteen carriers, their
dependency registers, and the Task Management label are
`STALE_REBUILD_REQUIRED` and belong to the downstream owners named in
`DOWNSTREAM_HANDOFFS.csv`. This report creates no authority and claims no
closure.
