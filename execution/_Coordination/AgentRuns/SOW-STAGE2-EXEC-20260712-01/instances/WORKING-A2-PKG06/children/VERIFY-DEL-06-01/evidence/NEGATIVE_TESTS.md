# Fail-Closed Negative Tests

## Partial legacy production kit

- Input: isolated folder containing only `Datasheet.md` and `_STATUS.md`.
- Validator result: exit `1`, `format=INVALID`, `valid=false`.
- Issues: `format state is INVALID`; `partial legacy production kit; missing: Specification.md, Procedure.md, Guidance.md`.
- Checklist derivation result: exit `1`.
- Output assertion: `PARTIAL_SHOULD_NOT_EXIST.json` was not created.

## Unauthorized dual format

- Input: isolated complete four-document source kit plus `ScopeOfWork.md`, without `--isolated-migration` or `--migration-authority`.
- Validator result: exit `1`, `format=AMBIGUOUS`, `valid=false`.
- Issues: `format state is AMBIGUOUS`; `dual production formats require an isolated conversion workspace and exact migration authority`.
- Checklist derivation result: exit `1`.
- Output assertion: `UNAUTHORIZED_DUAL_SHOULD_NOT_EXIST.json` was not created.

## Verdict

PASS — partial and unauthorized-dual inputs fail closed and do not emit checklist artifacts.
