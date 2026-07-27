# SCA-001 Gate 1 Basis Update

Status: `PRD_ADOPTION_CONTINGENCY_SATISFIED`
Recorded: `2026-07-26`
Branch basis: `main@7f30cc1db5f64dcffac03215b9395fe1dd7bafbb`

## Purpose

This is an additive update to the confirmed Gate 1 record. It does not revise
the owner's intake confirmation, reparse the actions, choose topology, or
approve Gate 2.

Gate 1 was confirmed with one external precondition: exact adoption and
application of the Root PRD runtime-stewardship amendment through D-GOV-28.
That precondition is now satisfied.

## Satisfied precondition

| Item | Current evidence |
|---|---|
| Adopted PRD subject | `docs/PRD_ROOT.md` |
| Adopted subject SHA-256 | `0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d` |
| Adopting instrument | `docs/governance_harness/_DECISIONS/D-GOV-28_root_runtime_stewardship.md` |
| Accepted candidate | `f78a83621cbd679e6af2c41199845aca74073480` |
| D-GOV-28 EffectiveSHA | `fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb` — merge of PR #364 |
| EffectiveSHA backfill closeout | `7f30cc1db5f64dcffac03215b9395fe1dd7bafbb` — merge of PR #365 |
| Adopted commitment | O-11, Continuing Root stewardship of the generic runtime |

The PRD bytes at the branch basis match the exact adopted candidate subject.
D-GOV-28's decision record carries the adoption and its applied-state SHA.

## Decomposition drift check

All seven protected decomposition-package hashes still match
`Pre_Change_Register_Baseline.json`:

| Surface | SHA-256 |
|---|---|
| `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `14067a7d97c94a43f5db0c2c1116206482504f260363de5ff6fa401a4df94cf7` |
| `chirality_root_scope_ledger_v1_0.csv` | `87f31c0d9f9118caf550b20223af4421a8165e987b03ee813892a731c253785a` |
| `chirality_root_deliverable_register_v1_0.csv` | `699e99e7ac7e75d3b8a677cc06705c96c813e6b29cc1c833ddb48bf401d1b90e` |
| `chirality_root_objective_register_v1_0.csv` | `7a639d0a9b1fa6f6795afd1a32f3a12ec5b0a19f7edee9302b91401fcae53281` |
| `chirality_root_prd_coverage_forward_v1_0.csv` | `0f04ef8f3b5d1c3c4de63661d7c9d3dde1f5f31e414595a7e8000971521c3883` |
| `chirality_root_trace_reverse_v1_0.csv` | `35ae8fb67a083ed07e5f9a5b512a3b65ff2752c2d3cab828dd1eb326f5198ba4` |
| `chirality_root_coverage_telemetry_v1_0.md` | `e8eee2fa5e439fcf7db292969ed4cd45c1747bda5734bf7050db74ae8b12bb28` |

No decomposition truth changed between the Gate 1 baseline and this update.
The existing audit remains a valid pre-change baseline.

## Gate effect

- Gate 1 remains `CONFIRMED`.
- Its D-GOV-28 contingency is `SATISFIED`.
- Gate 2 is eligible and its impact assessment may be prepared.
- No package, deliverable, scope item, dependency, write locus, or
  implementation authority is created by this update.
