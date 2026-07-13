# Negative Fixtures

| Fixture | Validator | Checklist | Output safety | Verdict |
|---|---|---|---|---|
| partial legacy kit | exit 1; `INVALID`; missing `Procedure.md` | exit 1; validated SOW required | no checklist output | PASS |
| unauthorized dual | exit 1; `AMBIGUOUS`; exact isolated authority required | exit 1; exact authority required | no checklist output | PASS |

The failures occurred before checklist output and did not mutate any source, candidate, lifecycle, control, or project file.
