# Negative Fixture Results

| Fixture | Input state | Invocation authority | Exit | Output artifact | Verdict |
|---|---|---|---:|---|---|
| `negative/partial/` | `ScopeOfWork.md` plus only `Datasheet.md` | none | 1 | absent | fail-closed PASS |
| `negative/unauthorized_dual/` | `ScopeOfWork.md` plus all four legacy documents | none | 1 | absent | fail-closed PASS |

The partial fixture reports the exact missing legacy sources. The unauthorized-dual fixture reports that dual production formats require an isolated conversion workspace and exact migration authority. Neither invocation changed the verifier's accepted workspace or candidate.
