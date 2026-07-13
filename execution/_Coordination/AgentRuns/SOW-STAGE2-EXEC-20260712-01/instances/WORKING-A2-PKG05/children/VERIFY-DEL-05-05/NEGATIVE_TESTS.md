# DEL-05-05 Negative Fail-Closed Tests

Verdict: `PASS`

## Partial legacy kit

- Input: candidate plus `Datasheet.md`, with `Specification.md`, `Procedure.md`, and `Guidance.md` absent.
- Validator result: exit `1`, format `INVALID`, explicit missing-file issue.
- Checklist result: exit `1`; no output artifact was created.

## Unauthorized dual format

- Input: candidate plus all four legacy documents, without isolated-migration authority on invocation.
- Validator result: exit `1`, format `AMBIGUOUS`, explicit exact-authority issue.
- Checklist result: exit `1`; no output artifact was created.

These initial failures are retained as evidence; no candidate or live source was repaired or changed.
