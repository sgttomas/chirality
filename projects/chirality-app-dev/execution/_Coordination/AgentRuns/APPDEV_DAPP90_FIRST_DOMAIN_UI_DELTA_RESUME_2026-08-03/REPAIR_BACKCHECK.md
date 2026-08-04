# Adversarial Verification Repair Backcheck

Final state: `PASS — R4 ACCEPT_WITH_NONBLOCKING_NOTES`

## Preserved attempts

| Attempt | Verdict | Exact issue | Manager response |
|---|---|---|---|
| 01 | `BLOCK` | verifier inherited paths but not material evidence bytes | preserved unchanged; no acceptance credit; created self-contained dossier path |
| 02 | `BLOCK` | launch transcription abbreviated E-21 despite correct draft bytes | preserved unchanged; no acceptance credit; durable dossier records full E-21 `1cb115ab65b160e19db5cab7341f94ceb09de1361d59d21ff9f41fd234432900` |
| 03 | `BLOCK` | dossier omitted five coverage classes | preserved unchanged; no acceptance credit; R4 supplement added exact tests, UNKNOWN rows, write inventory, App manifests, and metric definitions |
| 04 | `ACCEPT_WITH_NONBLOCKING_NOTES` | no blocking finding | accepted fan-in basis; all three notes carried into validation/handoff |

All repairs are confined to this fresh AgentRuns root. No proof conclusion was
changed merely to satisfy a reviewer: the repair sequence exposed evidence,
corrected a launch-only hash transcription, and expanded audit coverage.

## R4 acceptance basis

- base dossier SHA-256:
  `5b1fecc88f07e23657c6df6ee2dd96cf030517780e395975bcef8416ef84e243`;
- R4 supplement SHA-256:
  `70ffde8822301e31526af0dd50f5fc9383421d874cb7675e549a5098cd14561d`;
- 185-entry manifest file SHA-256:
  `66b6f32e75eed66dd63a2ac7b0712bc317e3c59f15dac3d5edcb7eda316b79be`;
- manifest data-line digest:
  `ad262802ab4dfd98475121a06eae49e76d461d71b172e860459e3be775392aa4`;
  and
- final verifier return: `reviews/A2_ADVERSARIAL_VERIFIER_RETURN.md`.

R4 explicitly accepts fitness tests 1–5, calibration, U, App rebind, metrics,
coexistence, elimination/non-selection, D-APP-81 preservation, fixed
constraints, write containment, and dossier coverage.

## Nonblocking notes carried forward

1. Final containment must be reconciled after closure files land.
2. A's TA is `NOT_YET_MEASURED_WITHIN_ALLOWLIST`, never inferred as zero.
3. Overlapping source-category figures are descriptive and not a partition of
   the 185-file corpus.
