# WORKING_ITEMS launch brief — D-PEC-77 phase 2

RequestedBy: HELP_HUMAN  
RunID: PEC-DPEC77-78-20260802  
InstanceID: working-items-del0105-phase2  
PackageID: PKG-01  
SelectedDeliverables: DEL-01-05

## Objective

Execute only D-PEC-77 O-A packet phase 2 against the owner-accepted
DEL-01-05 production contract. Produce the exact deterministic enforcement,
fixtures/tests, posture note, additive workflow registration, run records,
execution handoff, and verification evidence defined in packet §§3.2–3.5.

## Authority and prerequisite

Owner accepted `ScopeOfWork.md` SHA-256
`53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53`
as the DEL-01-05 production contract on 2026-08-03 and ruled that D-PEC-77
phase 2 may open. D-PEC-77 O-A / G-A and packet SHA-256
`f848d55557d4b59d4c425e3924b850d634011a4a7db6c6fbd2eee9fc46cc5c31`
govern.

## Allowed writes

Exactly the phase-2 paths enumerated in D-PEC-77 packet §3.2:

- `projects/pec/v2/config/service_core_posture.json`
- `projects/pec/v2/tools/check_service_core_posture.py`
- `projects/pec/v2/docs/SERVICE_CORE_POSTURE.md`
- `projects/pec/v2/tests/enforcement/**` limited to the three named tests and
  exact dependency/locality fixtures in §3.2
- `projects/pec/software-workflow.json` only to the exact additive §3.4
  postimage
- DEL-01-05 `_run_records/D-PEC-77_ACTIVATION.md`
- DEL-01-05 `_run_records/D-PEC-77_REGISTERED_CHECKS.json`
- D-PEC-77 `EXECUTION_HANDOFF.md` and its manifest
- this instance's `RETURN.md` and `STATUS.json`

No other source, contract, status, review, decomposition, register, decision,
receipt, domain profile, foreign-loop, or lifecycle path may change.

## Required verification and return

Execute every packet §3.5 item 1–14, including reliance preflights, exact
SOW/checklist binding, conforming and violating dependency/locality fixtures,
fail-closed fault injection, registration mutation, exact-state evidence,
no-mutation/no-network proof, posture-note inspection, exact workflow
postimage, all four registered checks, accepted-source preservation, strict
registers, dependency closure, graceful-absence/harness parity, containment,
manifest, coordination, and whitespace checks.

Return exact file hashes and results. Output is candidate work only. Do not
change lifecycle, satisfy any AC by inference, accept artifacts, reopen
DEL-01-06 RF-001, close TM-PEC-009, release, or claim professional reliance.
