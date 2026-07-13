# Fail-Closed Negative Tests

All fixtures were created under this verifier's authorized folder from the exact bound inputs and removed after testing. No fixture or output residue remains.

## Partial legacy kit

- Fixture: exact `Datasheet.md` and `Specification.md`, with `Guidance.md` and `Procedure.md` absent.
- Validator result: exit `1`, format `INVALID`, issue `partial legacy production kit; missing: Procedure.md, Guidance.md`.
- Checklist result: exit `1`, `format state is INVALID`; requested output did not exist.
- Verdict: PASS — partial input failed before output.

## Unauthorized dual format

- Fixture: exact four legacy files, exact `_STATUS.md`, and candidate `ScopeOfWork.md`.
- Invocation intentionally omitted isolated-migration and migration-authority flags.
- Validator result: exit `1`, format `AMBIGUOUS`, issue `dual production formats require an isolated conversion workspace and exact migration authority`.
- Checklist result: exit `1`, `format state is AMBIGUOUS`; requested output did not exist.
- Verdict: PASS — unauthorized dual input failed before output.
