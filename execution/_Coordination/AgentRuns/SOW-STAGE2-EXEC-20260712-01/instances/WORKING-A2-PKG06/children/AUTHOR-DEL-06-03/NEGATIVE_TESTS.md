# AUTHOR-DEL-06-03 Negative Fail-Closed Evidence

Basis: `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` and the exact isolated conversion brief.

| Case | Expected | Observed | Verdict |
|---|---|---|---|
| Converter with `D-GOV-16@0123456` | Non-zero; no candidate | Exit 1; exact-authority error; no `ScopeOfWork.md` emitted | PASS |
| Dual-format validator without isolated authority | Non-zero `AMBIGUOUS` | Exit 1; dual production formats require isolated workspace and exact authority | PASS |
| Checklist derivation on unauthorized dual state | Non-zero; no output artifact | Exit 1; no unauthorized checklist emitted | PASS |

These tests used disposable child-local copies of the frozen four documents and `_STATUS.md`. The disposable workspaces were removed after verification.
