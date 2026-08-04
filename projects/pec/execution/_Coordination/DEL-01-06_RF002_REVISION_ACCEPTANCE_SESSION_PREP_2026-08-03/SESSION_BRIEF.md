# Session brief — DEL-01-06 RF-002 revision and exact acceptance

## Activation

- Owning production instrument: WORKING_ITEMS, narrowed to DEL-01-06 in PKG-01.
- Acceptance instrument: REVIEW, read-only on `ScopeOfWork.md`.
- Owner ruling: `REVISE_ADOPTED / EXECUTION_SEPARATELY_SCHEDULED` at owner-record
  SHA-256 `579230cf7ed303f7722b88e0ac9abff2b768c3a5e5a7d475092c3407a0327f64`.
- Objective: produce one revision-1.4-current DEL-01-06 SOW successor, validate
  it, and present its exact SHA-256 to REVIEW/owner for acceptance without a
  Gate 5 advance.

## Entry state

- Current accepted SOW: revision 1.3 / SOW-094, SHA-256 `7dfa008b…f38a`.
- Current accepted decomposition: revision 1.4 / SOW-077+SOW-094 / OI-003
  resolved, SHA-256 `7cca5cdb…b65c81`.
- RF-001: `RESOLVED`; RF-002: `MAJOR / HumanDisposition=TBD / OPEN`, with owner
  disposition direction `REVISE` not effective as finding resolution until
  exact successor acceptance.
- Lifecycle: `INITIALIZED`; Gate 5: HOLD.
- Current dependency baseline: 64 registers / 255 rows / 136 ANCHOR / 119
  EXECUTION; topology 119 edges / 0 SCCs / 0 bidirectional pairs.

## Session sequence

1. Reproduce all bound preimages and run reliance/authority preflight.
2. WORKING_ITEMS writes only the allowed DEL-01-06 `ScopeOfWork.md` currency
   diff in `ACCEPTANCE_CONTRACT.md`.
3. Validate SOW_V1 and derive the deterministic six-row checklist against the
   exact candidate SHA.
4. Re-run or reproduce the named producer evidence without changing product
   or source bytes.
5. REVIEW executes Gates 1–4 against the exact candidate and prepares the
   owner exact-artifact acceptance question.
6. Only an explicit owner acceptance of that exact SOW SHA may make the
   successor the accepted production contract and close RF-002. Gate 5 remains
   HOLD and `_STATUS.md` remains `INITIALIZED`.
7. Route validated file-state closeout to CHANGE; do not stage, commit, push,
   open a PR, or merge from the WORKING_ITEMS/REVIEW session.

## Write ownership for the future session

- WORKING_ITEMS integration owner: DEL-01-06 `ScopeOfWork.md` only.
- REVIEW: deliverable-local `_REVIEW.md` and `Review_Findings.csv`, plus a new
  immutable review snapshot, only after accepting the candidate for review.
- `_STATUS.md`: no write; no Gate 5 transition is authorized.
- CHANGE: later scoped Git closeout only after validated acceptance fan-in.

All other paths are reads or exclusions. No Agent 2 delegation is required by
this preparation package; the executor decides the lawful session mechanism.
