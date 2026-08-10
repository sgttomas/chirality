# Work-graph amendment v1.2 — sole verifier convergence replacement

Status: `ADOPTED BY WORKING_ITEMS — UNCHANGED FREEZE`

The first fresh verifier emitted no return and was interrupted after bounded
convergence requests. This is a session-convergence failure, not a substantive
verifier verdict. The frozen packet remains byte-identical.

Exactly one genuinely fresh replacement verifier is dispatched against the
same `MANAGER_FREEZE.md`. It is read-only except its distinct R2 return, may
not repair, and must produce an evidence-first terminal `PASS` or `BLOCK`
without further reference expansion. No third verifier is permitted in this
tranche.
