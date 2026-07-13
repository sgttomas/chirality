# Negative-Fixture Results

Verdict: `PASS`

| Fixture | Invocation basis | Expected fail-closed result | Exit | Output artifact |
|---|---|---|---:|---|
| Partial legacy kit | Three named legacy files; `Procedure.md` intentionally absent | `INVALID`; exact missing file reported | 1 | none |
| Unauthorized dual | Exact accepted workspace without isolated-migration authority | `AMBIGUOUS`; exact authority requirement reported | 1 | none |
| Wrong-authority dual | Exact accepted workspace with `WRONG-AUTHORITY` | `AMBIGUOUS`; exact D-GOV-16 authority required | 1 | none |
| Unauthorized checklist | Exact accepted dual workspace without authority | checklist refuses ambiguous input before output | 1 | none |
| Partial-kit checklist | Partial legacy fixture | checklist refuses invalid input before output | 1 | none |

The partial fixture exists only under `workspace/evidence/negative_partial/`. The accepted workspace and candidate hashes were reproduced unchanged after all negative checks.
