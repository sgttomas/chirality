# AUTHOR_RETURN_03 — P1_STORE_GUARD_02 (D-PEC-87 C-A), correction cycle 3

Role: TASK (Type 2) author, instruction-asserted. This is the same author
session as cycles 1 and 2, acting on the WORKING_ITEMS manager's cycle-3
message (verifier cycle 2: PASS with non-blocking findings). No delegation.
Date: 2026-09-24 (session date). The host reports the serving model as
Opus 5.5 (`claude-opus-5-5`). Interpreter:
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, Python
3.13.7.

Scope this cycle: documentation only, and only
`projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md` was edited. No code or
test edit was made and no state-changing git was run. `AUTHOR_RETURN_01.md`
and `AUTHOR_RETURN_02.md` are unedited.

No `VERIFIER_VERDICT_02.md` was on disk when this cycle ran, so the findings
were taken from the manager's message. I identified the over-long line by
measurement (below).

## Changes (postimage line numbers in `STORE_LIFECYCLE_AND_GUARD.md`)

| Item | Locator | Change |
|---|---|---|
| C2-1 (first pointer) | `:80-82` | After "Record IDs and field names are bounded envelope coordinates; they are not free-form stored payload." I added: "That bound holds only for exact `str` inputs; see the `str`-subclass channel under Boundary and residuals." |
| C2-2 | `:97-101` | My cycle-2 sentence ("The checks inspect the characters of each supplied string; …") is replaced. The new text says a `str` subclass is not covered by the preceding forged-wrapper statement. The normalization, absolute-path and `..` checks call methods that a `str` subclass can override. The D-PEC-87 character and byte checks use a regular expression and unbound `str` methods instead, but no check controls what is persisted. It points to the `str`-subclass channel under Boundary and residuals. |
| C2-3 | `:92-104` | The over-long line was the cycle-2 line 96 (124 characters), which carried "…is not closed by them. A state rejection names its record and field and". The paragraph from "cannot bypass…" to "source prose." is rewrapped to the file's prose width. After the edit, no non-table line exceeds 79 characters, measured in Python characters. The only other hit from a byte-based `awk length` check was old line 110 (now `:118`, "Against PRD §7.2…"). It is D-PEC-85 text and measures 79 characters; awk counted the two-byte `§` twice. It was not touched. |
| C2-1 (second pointer) | `:108-109` | After "…only typed paths, counts, SHAs, hashes, and the six lifecycle states above." I added: "That holds only for exact `str` inputs; see the `str`-subclass channel under Boundary and residuals." The following D-PEC-85 sentence ("Receipt bodies, …") is left on its original line, not reflowed, to avoid touching unchanged text. It renders as the same paragraph. |

## Verification (final bytes)

| Check | Command (cwd) | Exit | Result |
|---|---|---|---|
| v2-store-guard | `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` (`projects/pec`) | 0 | Ran 13, 13 `ok`, OK |
| v2-core-posture | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` (`projects/pec`) | 0 | `"verdict": "PASS"` |
| whitespace | `git diff --check` (repo root) | 0 | no output |
| containment | `git diff --name-only` (repo root) | 0 | exactly the seven granted paths |

## Postimage SHA-256 (relative to `projects/pec/`)

| Path | SHA-256 | Versus cycle-2 postimage |
|---|---|---|
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `e9d65fc77ae3009a3d362eb34c8de527350456fcd7bc7670ef9e95ff9641ed35` | changed (was `1f626001…b5e`) |
| `v2/src/pec_v2/core/content_minimal_guard.py` | `d63932c28dd346581deb0b04bb14841f00eff9481432a379ce67dd8e9d626b33` | identical |
| `v2/src/pec_v2/core/ports/store.py` | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` | identical |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `05b9846a2baa9a5fe2691196d83d35770b8227f8b653f39c3831dcd4b89eae0a` | identical |
| `v2/tests/storage/test_store_lifecycle.py` | `edbd41df5e05573d9992ee9778aba053570b4de6d4a0bf392ff7a888ff42cadf` | identical |
| `v2/tests/storage/test_content_minimal_guard.py` | `c8e23563c226585c9f557d0c7d14eb880232452ab30541fa034a643afd561c29` | identical |
| `software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` | identical |
| `v2/src/pec_v2/adapters/storage/__init__.py` (unopened) | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` | identical |

## Open items (unchanged)

- The code closure of the `str`-subclass channel still needs a separate owner
  ruling.
- `close()` is still not wrapped under R8, which is a scope decision.
- The gitignored `__pycache__/` directories created by the check runs are
  still in place.

Nothing here claims review, acceptance, CHECKING, merge or any lifecycle
change.
