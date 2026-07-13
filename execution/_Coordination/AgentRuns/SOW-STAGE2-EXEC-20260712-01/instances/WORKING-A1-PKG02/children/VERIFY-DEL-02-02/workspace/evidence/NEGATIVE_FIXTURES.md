# Negative Fixture Results

| Fixture | Input state | Invocation authority | Validator/checklist exit | Output artifact | Verdict |
|---|---|---|---:|---|---|
| `fixtures/partial/` | only exact `Datasheet.md` from the legacy kit | none | 1 / 1 | absent | fail-closed PASS |
| `fixtures/unauthorized-dual/` | exact `ScopeOfWork.md` plus all four legacy documents | none | 1 / 1 | absent | fail-closed PASS |

The partial fixture reports `INVALID` and the exact three missing legacy sources. The unauthorized-dual fixture reports `AMBIGUOUS` and requires an isolated conversion workspace plus exact migration authority. Both checklist invocations also exit 1 without creating their requested output. Neither fixture changed the accepted candidate or verifier seed.
