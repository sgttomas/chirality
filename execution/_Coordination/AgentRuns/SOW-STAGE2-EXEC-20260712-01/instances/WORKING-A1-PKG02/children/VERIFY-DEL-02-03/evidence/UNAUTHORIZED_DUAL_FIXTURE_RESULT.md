# Unauthorized Dual Fixture Result

- Command: `python3 tools/scope_of_work/derive_review_checklist.py <fixture> --output <fixture>/SHOULD_NOT_EXIST.json`
- Exit code: `1`
- Standard error: `ERROR: format state is AMBIGUOUS; validated ScopeOfWork.md is required: dual production formats require an isolated conversion workspace and exact migration authority`
- Output artifact exists: `no`
- Verdict: `PASS_FAIL_CLOSED`
