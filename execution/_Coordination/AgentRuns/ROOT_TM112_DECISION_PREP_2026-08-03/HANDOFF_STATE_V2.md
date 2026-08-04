# Handoff state v2 — N2 complete

- Accepted upstream: N1 accepted COMPLETE/PASS by HELP_HUMAN; Receipt 90 M6;
  Root register snapshots SHA-256 `1b963493…44f` and `3b6e9ff3…775`.
- Derivative package: current for N2; does not replace register truth or
  Receipt 90 authority.
- Closure verdict: `N2 COMPLETE / PASS FOR HELP_HUMAN FAN-IN`.
- Applied tracked state: Root handoff §1 now records 27 live = 16 OPEN / 11
  DEFERRED and 95 archived; every other handoff semantic/history byte is
  preserved.
- Rerun requirement: recompute both CSVs directly if either register changes
  before integration; do not reuse these counts after register drift.
- Remaining blockers/holds: N3 remains held pending HELP_HUMAN validation;
  TM-ROOT-112 semantics/implementation and all other excluded actions remain
  held.

