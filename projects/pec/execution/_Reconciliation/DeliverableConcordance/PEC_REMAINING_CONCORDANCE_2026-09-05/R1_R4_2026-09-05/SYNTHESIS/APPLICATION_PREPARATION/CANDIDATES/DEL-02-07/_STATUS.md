# Status: DEL-02-07

**Current State:** INITIALIZED
**Last Updated:** 2026-07-25

## History
- 2026-07-25 — State set to OPEN (PREPARATION)
- 2026-07-25 — State set to INITIALIZED (TASK+status-advance)

## Remaining

- [ ] DEL-02-07-REM-001 — Declare the consumed manifest grammar and YAML parsing approach within REQ-002/REQ-007, then produce the per-project feed-manifest reader and valid/undeclared-field invariance evidence.
  Depends: NONE
  (gated: separate exact owner-ruled DEL-02-07 production packet on origin/main opening the named source/test paths, acts, verification and rollback under F-PEC-1; WORKING_ITEMS activation; current reliance preflight)

- [ ] DEL-02-07-REM-002 — Resolve the loop-to-project manifest relation using accepted evidence; if no accepted derivation exists, obtain the CON-002 scope-change ruling. Implement and verify loop-set acquisition only through the LoopRegistry port.
  Depends: DEL-01-06
  (gated: separate exact owner-ruled DEL-02-07 production packet on origin/main opening the named source/test paths, acts, verification and rollback under F-PEC-1; WORKING_ITEMS activation; current reliance preflight) (gated: accepted CON-002 loop-to-project relation derivation or owner-ruled SCOPE_CHANGE if not derivable)

- [ ] DEL-02-07-REM-003 — Produce and verify explicit absent/unreadable/malformed/schema-invalid manifest limitations; source byte preservation; content-minimal payload; zero-third-party runtime dependency and no external egress.
  Depends: NONE
  (gated: separate exact owner-ruled DEL-02-07 production packet on origin/main opening the named source/test paths, acts, verification and rollback under F-PEC-1; WORKING_ITEMS activation; current reliance preflight)

- [ ] DEL-02-07-REM-004 — Produce and register the DEL-02-07 fixture suite covering VER-001..006, then run the PKG-02 suite and show every assertion derives from the accepted contract.
  Depends: NONE
  (gated: separate exact owner-ruled DEL-02-07 production packet on origin/main opening the named source/test paths, acts, verification and rollback under F-PEC-1; WORKING_ITEMS activation; current reliance preflight)
