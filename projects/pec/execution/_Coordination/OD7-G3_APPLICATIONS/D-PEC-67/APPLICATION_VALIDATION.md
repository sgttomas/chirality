# D-PEC-67 Application Validation

**Date:** 2026-07-27
**Basis:** `a6b10683219c22f45f31e3dffa4fb164b4582051`
**Result:** `PASS — APPLIED_PENDING_CHANGE`

## Identity and precondition checks

- Approved package artifact manifest reproduced:
  `4628c7efcef138aa23fcd9d4715a8c43e89ec44b6ece44f06e487b79fc9bf5c1`.
- Approved application packet reproduced:
  `343e94db96267715b0aa283bfb9d7de88392ca1eb6d923931c587eb4bd9be6d8`.
- Approved application tranche manifest reproduced:
  `ff958188c0961a73180bc9d4aa68fe3579081a1e5310811d5a4446cc8769c033`.
- All seven approved section-gate and section-manifest pairs reproduced.
- All existing live preimages reproduced exactly.
- `D-PEC-67`, its archive, the hold register, tool, tests, and notices were
  absent before application.
- The execution-time PEC decision scan identified `D-PEC-67` as next free.
- Receipt 113 was next free after Receipt 112.

## Exact postimage checks

- The live PEC decision-register, PRD, project overlay, hold register, hold
  tool, hold tests, script README, root tool registry, and two notices
  reproduce their approved candidate postimages exactly.
- The PRD changes only PEC-K-03 and PEC-K-11.
- One D-PEC-67 row is present; no D-PEC-68 through D-PEC-74 carrier was
  created or relied upon.
- The owner ruling is transcribed verbatim in both the ruled decision and
  `OWNER_RULING.md`.
- Receipt 113 is one additive receipt after Receipt 112.
- L-A2 is absent and L-A1 remains `ACTIVE`.
- No decomposition, ScopeOfWork, runtime, implementation, profile, lifecycle,
  release, dependency, estimate, or schedule surface is changed.

## Deterministic checks

- Single-carrier candidate validator: `129/129 PASS`.
- PEC reliance-hold tests: `7/7 PASS`.
- Practitioner harness: `349/349 PASS`.
- Python syntax compilation: `PASS`.
- Candidate-whitespace validation: `PASS`.
- `git diff --check`: `PASS`.

These checks are evidence of exact application. Git publication remains a
separate `CHANGE` gate.
