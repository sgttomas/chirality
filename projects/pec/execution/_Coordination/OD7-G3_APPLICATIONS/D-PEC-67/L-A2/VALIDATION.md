# OD7-G3 L-A2 — Application Validation

**State:** `PASS`
**Basis:** `3babf48cfc295f29982aeebdceadb60413a8b3cd`

## Deterministic results

- Exact ScopeOfWork postimage: `PASS`
  (`e7c7ae02b254726a0a25422859b8a798b4b1989cd6cf013b0e1d41886ce3c80f`).
- ScopeOfWork schema validation: `PASS` (`SOW_V1`).
- Receipt sequence: `PASS`; Receipt 114 is present exactly once and Receipt
  115 is absent.
- Receipt-ledger postimage: `PASS`
  (`2eca42ec712396301f023f14bf2ddcb7fcd1a6e68968b0c95f2aaccd5cc334f5`).
- Active-hold register unchanged: `PASS`
  (`d92d134bdfe4466dc06292fa53fa44cf368d6be1dfeb04fefa6ce188bba8002a`).
- Reliance-control tests: `PASS` (7/7).
- Prohibited `rely-for-production` operation: `BLOCK`, as required.
- Allowed `candidate-validation` operation: `ALLOW`, as required.
- No decision-register row added: `PASS`.
- PRD, decomposition, metadata, dependency, and implementation surfaces
  unchanged: `PASS`.
- Changed-path containment, whitespace, and `git diff --check`: `PASS`.

L-A1 remains authoritative and active. L-A2 does not release the hold.
