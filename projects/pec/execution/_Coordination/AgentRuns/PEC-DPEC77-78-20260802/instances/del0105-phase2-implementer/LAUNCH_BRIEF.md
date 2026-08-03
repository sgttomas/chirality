# Agent 2 brief — DEL-01-05 phase-2 implementation completion

RequestedBy: HELP_HUMAN  
ParentManager: WORKING_ITEMS  
RunID: PEC-DPEC77-78-20260802  
InstanceID: del0105-phase2-implementer

## Bounded objective

Inspect the existing partial D-PEC-77 phase-2 product bytes, complete the exact
implementation and the three missing test files, and return deterministic
test evidence to WORKING_ITEMS. Do not create manager-owned run records or
coordination handoff artifacts.

## Authority

D-PEC-77 O-A/G-A packet §§3.2–3.5 and owner-accepted DEL-01-05 SOW SHA-256
`53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53`.

## Allowed writes

- `projects/pec/v2/config/service_core_posture.json`
- `projects/pec/v2/tools/check_service_core_posture.py`
- `projects/pec/v2/docs/SERVICE_CORE_POSTURE.md`
- the exact ten fixture files already enumerated by packet §3.2
- `projects/pec/v2/tests/enforcement/test_dependency_assertion.py`
- `projects/pec/v2/tests/enforcement/test_locality_assertion.py`
- `projects/pec/v2/tests/enforcement/test_gate_registration.py`
- `projects/pec/software-workflow.json` only to the exact packet §3.4 postimage
- this instance's `RETURN.md` and `STATUS.json`

Every other path is read-only. In particular: no contracts, reviews,
lifecycle, run records, execution handoff, manifests, decomposition,
registers, decisions, receipts, or foreign-loop files.

## Acceptance checks

- The checker is Python-standard-library only, read-only, fail-closed, and
  reports located dependency/locality/registration findings.
- All dependency/locality fixtures produce packet-defined results, including
  loopback and Unix local transport parity.
- Fault cases and missing/disabled registration fail explicitly.
- The three test modules pass.
- The exact four registered project checks pass or return a precise blocker.
- Return exact changed paths, hashes, commands, outputs, and any blocker.
