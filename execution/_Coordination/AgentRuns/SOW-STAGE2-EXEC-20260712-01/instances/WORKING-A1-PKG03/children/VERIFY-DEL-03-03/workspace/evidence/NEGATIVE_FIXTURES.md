# Negative Fixtures — DEL-03-03 Verifier

Verdict: `PASS — FAIL_CLOSED`

| Fixture | Validator | Checklist compiler | Output safety |
|---|---|---|---|
| Partial legacy kit (missing `Procedure.md`) | exit `1`; `INVALID`; exact missing-file issue | exit `1` | no checklist artifact emitted |
| Complete dual kit without isolated authority | exit `1`; `AMBIGUOUS`; exact authority issue | exit `1` | no checklist artifact emitted |

The fixture commands wrote only captured stdout/stderr and validation JSON inside the verifier subtree. Neither failure altered source inputs or the accepted candidate.
