# Checklist Fail-Closed Check

Verdict: `PASS`

- Invocation omitted `--isolated-migration` and the exact migration authority on the ambiguous dual-format workspace.
- Exit code: `1`.
- Error: `format state is AMBIGUOUS; validated ScopeOfWork.md is required: dual production formats require an isolated conversion workspace and exact migration authority`.
- No output artifact was created.
