# Negative Fail-Closed Checks

Status: `PASS`

| Case | Expected | Observed |
|---|---|---|
| Partial legacy kit | `INVALID`; nonzero; no candidate | `INVALID`; missing `Specification.md`, `Procedure.md`, and `Guidance.md`; exit 1; no candidate |
| Dual format without accepted authority | `AMBIGUOUS`; nonzero | `AMBIGUOUS`; exact isolated authority required; exit 1 |
| Checklist with `D-GOV-16@0123456` | Refuse before output | Exit 1; exact ruled authority named; output artifact absent |
| Converter with `D-GOV-16@0123456` | Refuse before output | Exit 1; exact ruled authority named; `ScopeOfWork.md` absent |

All negative fixtures were child-local transient workspaces and were removed after the no-output assertions passed.
