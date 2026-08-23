# Brief amendment 01 — failure-log final-status coverage

Disposition: `AMEND`, in-scope clarification relayed to `A2-PKG09-R20-IMPLEMENT-01` before candidate freeze.

Required semantics:

- preservation covers proof-observation failure, cleanup refusal/failure, and a later default-protection failure;
- `failed-logs` must already exist before any allowed runtime-data removal;
- copied failed logs may be removed only if the final proof status becomes `PASS`;
- no copied log may contain the actual operator token;
- token/auth ambiguity remains fail-closed and private-root-only.

No write scope, tool, build/full-suite, private-read, proof, operator, network, or Git authority changed.
