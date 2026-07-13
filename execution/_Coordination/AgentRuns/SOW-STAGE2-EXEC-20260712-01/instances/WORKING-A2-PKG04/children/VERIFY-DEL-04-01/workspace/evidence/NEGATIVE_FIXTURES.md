# Negative Fixtures

Verdict: `PASS`

| Fixture | Validation | Checklist | Output containment |
|---|---|---|---|
| Partial legacy kit plus candidate | exit 1; `INVALID`; missing Specification, Procedure, Guidance | exit 1 | `SHOULD_NOT_EXIST.json` absent |
| Complete dual kit with `D-GOV-16@0123456` | exit 1; `AMBIGUOUS`; exact authority rejected | exit 1 | `SHOULD_NOT_EXIST.json` absent |

The fixture copies are confined to `workspace/fixtures/`; no project, candidate, author, sibling, or package path was changed.
