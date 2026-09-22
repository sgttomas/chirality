# R6 backcheck — D-APP-131

Source basis: `379df923927d157be3ebb51d8a1dcf783d970112` plus the exact production hashes in `SOURCE_STATE.csv` and R5 status manifests. Discovery basis: accepted R0–R4 at `00115c719` and their recorded later evidence integrations. This is a new derivative, not a rewrite of the original verdicts.

The checker independently discovers differing old/current units with the original `claim_index.py`, then matches every original split/unsplit R3 key to the manifest. It does not use the manifest to choose which production units to inspect. It re-extracts 91 ScopeOfWork source keys across 61 blocks/31 files and 47 pre-existing Remaining references; the 138-key combined multiset equals the authorized repair manifests. Fifty-four status control sections are additionally bound before/after, including new residual items and the removed audit bootstrap. Negative missing-key and duplicate-key inputs are rejected. All 54 SoWs inverse-reconstruct to their pre-repair bytes after restoring the declared blocks.

The all-row accounting covers 3,568 keys exactly once. Original R0–R4 files are byte-identical. All lifecycle and Checking Approval SHA fields and prior status history are unchanged. The Remaining census contains 54 deliverables and 111 top-level rows, with an explicit NONE row for retired DEL-09-07.

Commands, from repository root:

```sh
python3 projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R5/build_accounting.py
python3 projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R5/integrate_evidence.py
PYTHONDONTWRITEBYTECODE=1 python3 projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/R5/verify_backcheck.py
```

The first command applies only the documented status/memory/receipt-support derivative build from the named original basis; do not run it over independently edited statuses without reconciling those edits. The second writes evidence only. The third reads production and writes the R6 check outputs. `CHECKS.json` is the actual deterministic result; independent semantic review and final actual-candidate integration checks are in the parent Root run.

Actions are deliberately more precise than a single complete/incomplete verdict:

- 1321: `AUTHORIZED_NO_CHANGE`
- 55: `CLAIM_LIFT_APPLIED_RESIDUAL_PRESERVED`
- 2073: `EXPLICIT_UNCHANGED_RESIDUAL`
- 16: `HISTORICAL_EVIDENCE_RECOVERED_CURRENT_BINDING_OPEN`
- 36: `RECORD_LIFT_APPLIED`
- 47: `REMAINING_RECORD_UPDATED_RESIDUAL_PRESERVED`
- 20: `RETIRED_HISTORY_PRESERVED`

R5 lifts apply documentary corrections; they do not claim every surviving implementation, verification or authority obligation within the source row is discharged. Sixteen historical conversion Unknowns gain recovered mechanical evidence without a current-parity or personal-human-review assertion. P-08's 32 keys map to 15 current stable conditions, preserving specific uncovered checks rather than creating a blanket legacy-suite gate. Product source/tests were not modified or rerun by the App repair tranches.
