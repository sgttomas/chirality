# Portability Exceptions

Authority: `BRIEF_AMENDMENT-001.md` (`ACTIVE — PORTABILITY/PRESERVATION CLARIFICATION`).

The prohibited checkout-root prefix occurs only in exact copied source/control bytes or deterministic verbatim reproductions of a preserved source block. No temp prefix occurs anywhere. These occurrences are preservation-bound text, not generated path authority, and were not normalized because normalization would violate exact source preservation and parity.

| Artifact | Occurrences | Source binding | Reason |
|---|---:|---|---|
| `workspace/Datasheet.md` | 1 | SHA-256 `ff00ec279937b42d6a86999dca8968c6488d019b67f63ec1ca1bbda0c9b813dd`, line 69 | Exact copied legacy source byte. |
| `workspace/_REFERENCES.md` | 1 | SHA-256 `045cc70a94a4128486e60e6ced5499ac8659fee1cbcb1fc64ff629e9c0579ea9`, line 13 | Exact copied control byte. |
| `workspace/_DEPENDENCIES.md` | 2 | SHA-256 `093b1b267a5054d7d56aed6103d7cc6b5f277daed911469e737090b20fbeef4b`, lines 26–27 | Exact copied control bytes. |
| `workspace/ScopeOfWork.md` | 1 | Candidate SHA-256 `8eeb463884aa9549a8ebf79d8c454bf60fdc6e0dd5a5e7359734ead1d23e47b0`; `Datasheet.md` preserved range ending at line 69 | Deterministic verbatim source block. |
| `candidates/W_A1/APP-PKG01/DEL-01-03/ScopeOfWork.md` | 1 | Exact copy of candidate SHA-256 `8eeb463884aa9549a8ebf79d8c454bf60fdc6e0dd5a5e7359734ead1d23e47b0` | Deterministic verbatim source block. |
| `workspace/evidence/ScopeOfWork_1.html` | 1 | HTML SHA-256 `ca4d7205d46f4952f9f4b09bfb22e26442ded1bd02777a8a9d589fe42af51bd9`; rendered candidate source block | Deterministic verbatim rendered source text. |
| `workspace/evidence/ScopeOfWork_2.html` | 1 | HTML SHA-256 `ca4d7205d46f4952f9f4b09bfb22e26442ded1bd02777a8a9d589fe42af51bd9`; rendered candidate source block | Deterministic verbatim rendered source text. |

Total: 8 preservation-bound occurrences in 7 artifacts. Generated metadata, run-record fields, claim-map/parity/checklist metadata, verdicts, checks, manifests, return, and status have zero prohibited checkout-root and temp-prefix occurrences.
