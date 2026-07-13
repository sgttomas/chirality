# Negative Fixtures

Verdict: `PASS`

| Fixture | Operation | Expected | Observed |
|---|---|---|---|
| `fixtures/partial/` | validate | `INVALID`, nonzero | `INVALID`; missing `Procedure.md`; exit 1 |
| `fixtures/partial/` | checklist | nonzero, no output | exit 1; requested artifact absent |
| `fixtures/unauthorized_dual/` | validate without migration authority | `AMBIGUOUS`, nonzero | `AMBIGUOUS`; exact-authority requirement reported; exit 1 |
| `fixtures/unauthorized_dual/` | checklist without migration authority | nonzero, no output | exit 1; requested artifact absent |

No `SHOULD_NOT_EXIST.json` artifact exists in either fixture.
