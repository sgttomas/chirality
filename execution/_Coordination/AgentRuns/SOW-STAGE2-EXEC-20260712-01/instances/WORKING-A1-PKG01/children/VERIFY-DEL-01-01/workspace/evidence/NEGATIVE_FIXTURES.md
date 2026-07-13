# Negative Fixture Results

| Fixture | Input state | Invocation authority | Validator/checklist exit | Output artifact | Verdict |
|---|---|---|---:|---|---|
| `negative/partial/` | only `Datasheet.md` from the legacy kit | none | 1 / 1 | absent | fail-closed PASS |
| `negative/unauthorized_dual/` | `ScopeOfWork.md` plus all four legacy documents | none | 1 / 1 | absent | fail-closed PASS |

The partial fixture reports the exact three missing legacy sources. The unauthorized-dual fixture reports `AMBIGUOUS` and requires an isolated conversion workspace plus exact migration authority. Neither invocation changed the accepted verifier workspace or candidate.
