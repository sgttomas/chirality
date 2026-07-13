# Portability Exceptions

Verdict: `PASS`

The accepted checkout-prefix literal is present only as preserved source content or its deterministic rendering:

| Artifact | Occurrences | Disposition |
|---|---:|---|
| `workspace/Datasheet.md` | 1 | exact manifest-bound source literal |
| `workspace/_REFERENCES.md` | 1 | exact manifest-bound control literal |
| `workspace/_DEPENDENCIES.md` | 2 | exact manifest-bound control literals |
| `workspace/Dependencies.csv` | 1 | exact manifest-bound control literal |
| `workspace/ScopeOfWork.md` | 1 | marker-bound preservation of `Datasheet.md` line 63 |
| `workspace/evidence/ScopeOfWork.1.html` | 1 | deterministic rendering of the same marker-bound source literal |
| `workspace/evidence/ScopeOfWork.2.html` | 1 | deterministic rendering of the same marker-bound source literal |

All generated metadata, JSON/TSV/Markdown verifier evidence, run records, terminal artifacts, and non-render derivatives have zero checkout-prefix and zero temporary-prefix occurrences. No accepted literal was normalized or repaired.
