# Portability Exceptions

Disposition: `PRESERVED_SOURCE_LITERAL` under the accepted author amendment and parent instruction.

The checkout-root prefix occurs only in exact copied source/control bytes, exact fixture copies used for fail-closed verification, the marker-bound candidate source block, and deterministic HTML reproductions of that block. These literals were not normalized because normalization would break source identity or parity. No generated metadata, run record, return/status, map/parity/checklist metadata, verdict, check, manifest, or negative-result record contains that prefix. No temp prefix occurs.

| Artifact | Occurrences | Exact source/hash/line or marker binding | Reason |
|---|---:|---|---|
| `workspace/Datasheet.md` | 1 | `Datasheet.md` SHA-256 `ff00ec279937b42d6a86999dca8968c6488d019b67f63ec1ca1bbda0c9b813dd`, line 69 | Exact copied legacy source byte. |
| `workspace/_REFERENCES.md` | 1 | `_REFERENCES.md` SHA-256 `045cc70a94a4128486e60e6ced5499ac8659fee1cbcb1fc64ff629e9c0579ea9`, line 13 | Exact copied control byte. |
| `workspace/_DEPENDENCIES.md` | 2 | `_DEPENDENCIES.md` SHA-256 `093b1b267a5054d7d56aed6103d7cc6b5f277daed911469e737090b20fbeef4b`, lines 26–27 | Exact copied control bytes. |
| `workspace/ScopeOfWork.md` | 1 | Candidate SHA-256 `8eeb463884aa9549a8ebf79d8c454bf60fdc6e0dd5a5e7359734ead1d23e47b0`, candidate line 116, marker `CLM-006`, source `Datasheet.md` lines 59–69 with the hash above | Marker-bound deterministic verbatim source block. |
| `evidence/fixtures/live_legacy/Datasheet.md` | 1 | Exact fixture copy of `Datasheet.md`, line 69 and hash above | Live-format fixture preservation. |
| `evidence/fixtures/live_legacy/_REFERENCES.md` | 1 | Exact fixture copy of `_REFERENCES.md`, line 13 and hash above | Live-format fixture preservation. |
| `evidence/fixtures/live_legacy/_DEPENDENCIES.md` | 2 | Exact fixture copy of `_DEPENDENCIES.md`, lines 26–27 and hash above | Live-format fixture preservation. |
| `evidence/fixtures/partial_legacy/Datasheet.md` | 1 | Exact fixture copy of `Datasheet.md`, line 69 and hash above | Partial-format fail-closed fixture preservation. |
| `evidence/fixtures/partial_legacy/_REFERENCES.md` | 1 | Exact fixture copy of `_REFERENCES.md`, line 13 and hash above | Partial-format fail-closed fixture preservation. |
| `evidence/fixtures/partial_legacy/_DEPENDENCIES.md` | 2 | Exact fixture copy of `_DEPENDENCIES.md`, lines 26–27 and hash above | Partial-format fail-closed fixture preservation. |
| `evidence/fixtures/unauthorized_dual/Datasheet.md` | 1 | Exact fixture copy of `Datasheet.md`, line 69 and hash above | Unauthorized-dual fixture preservation. |
| `evidence/fixtures/unauthorized_dual/_REFERENCES.md` | 1 | Exact fixture copy of `_REFERENCES.md`, line 13 and hash above | Unauthorized-dual fixture preservation. |
| `evidence/fixtures/unauthorized_dual/_DEPENDENCIES.md` | 2 | Exact fixture copy of `_DEPENDENCIES.md`, lines 26–27 and hash above | Unauthorized-dual fixture preservation. |
| `evidence/fixtures/unauthorized_dual/ScopeOfWork.md` | 1 | Exact candidate copy; candidate line 116, marker `CLM-006`, source `Datasheet.md` lines 59–69 | Unauthorized-dual fixture preservation. |
| `evidence/ScopeOfWork_1.html` | 1 | Render SHA-256 `ca4d7205d46f4952f9f4b09bfb22e26442ded1bd02777a8a9d589fe42af51bd9`, line 88; candidate marker `CLM-006` / `Datasheet.md` lines 59–69 | Deterministic verbatim rendered source text. |
| `evidence/ScopeOfWork_2.html` | 1 | Same render hash and binding as render 1 | Deterministic verbatim rendered source text. |

Total: 20 preservation-bound occurrences in 16 artifacts. All other generated verifier surfaces have zero prohibited checkout-root and temp-prefix occurrences.
