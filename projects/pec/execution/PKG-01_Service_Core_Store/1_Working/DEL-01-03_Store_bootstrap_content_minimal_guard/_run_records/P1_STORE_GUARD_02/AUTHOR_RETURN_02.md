# AUTHOR_RETURN_02 — P1_STORE_GUARD_02 (D-PEC-87 C-A), correction cycle 2 (N2')

Role: TASK (Type 2) author, instruction-asserted. This is the same author
session as `AUTHOR_RETURN_01.md`, acting on the WORKING_ITEMS manager's
correction message. No delegation. Date: 2026-09-24 (session date). The host
reports the serving model as Opus 5.5 (`claude-opus-5-5`). Interpreter:
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, Python
3.13.7. Write scope and rules are unchanged. No state-changing git was run.
`AUTHOR_RETURN_01.md` is left unedited.

Input: `VERIFIER_VERDICT_01.md` (FAIL on B-1; N-1..N-5 non-blocking), read in
full before editing. The manager directed B-1, N-1, N-2 and N-5, plus a
correction of AUTHOR_RETURN_01 item 5. N-3 and N-4 are notes and were not
directed, so they are not acted on.

## Changes this cycle

Only two of the seven granted files changed this cycle. No code changed:
`content_minimal_guard.py`, `ports/store.py`, `sqlite_store.py`,
`test_store_lifecycle.py` and `software-workflow.json` are byte-identical to
their cycle-1 postimages.

| Item | Status | Locator (postimage) | Change |
|---|---|---|---|
| B-1 (blocking) | DONE, documentation only | `v2/docs/STORE_LIFECYCLE_AND_GUARD.md:84` (PATH row, decision cell) | The overclaim is removed. The row now says the bounds are checked on the characters the guard inspects. It says they do not close the pre-existing, guard-wide `str`-subclass channel, through which a validated value can still persist different text, including multi-line text. The prose-like single-line residual is kept, with a pointer to Boundary and residuals. |
| B-1 | DONE | `STORE_LIFECYCLE_AND_GUARD.md:140-158` (Boundary) | The old "stops multi-line file bodies…" paragraph is replaced. The bound now holds only for an exact `str`. A new paragraph, **`str`-subclass channel (guard-wide, pre-existing since D-PEC-85, not closed by D-PEC-87 R1)**, gives the mechanism: the caller's object is returned and persisted, `sqlite3` calls `__conform__` on a non-exact `str`, and the SHA and hash rendering calls `__format__`. It notes that no forged shell is needed. It lists the reach: record IDs, field names, source paths, PATH values, and SHA and hash digests. It states that the store does not enforce PEC-K-10 against a caller supplying `str` subclasses until the channel is closed. Closure needs an exact-`str` rule on every string the guard outputs, which is outside the R1 exact rule and routed for a separate owner ruling. |
| B-1 (consistency) | DONE | `STORE_LIFECYCLE_AND_GUARD.md:92-96` | The pre-existing (D-PEC-85) sentence claims "even a … forged frozen wrapper cannot bypass the domain checks". One sentence now follows it: the checks inspect the characters of each supplied string, and the `str`-subclass residual is not closed by them. This is the same overclaim class in the same file; I added nothing beyond the pointer. |
| N-1 | DONE | `STORE_LIFECYCLE_AND_GUARD.md:160-173` | The proposal's statement is kept for PRD §7.1 source locators: existence at the cited source SHA, checked by the ingest caller (DEL-03-01 or the PKG-02 scanners). Added for PRD §7.2 dirty and untracked path names, which have no source SHA: the observing caller is DEL-06-02 (Git worktree scanner), the closing check is presence in the observed worktree status, the D-PEC-87 survey covered tracked paths only, and such a caller should count an `INVALID_VALUE` rejection (a control character, or non-UTF-8 bytes decoded to a lone surrogate) rather than drop it. |
| N-2 | DONE | `STORE_LIFECYCLE_AND_GUARD.md:62` and `:65` | The admission-transaction row now reads "`admit_batch()`" (no longer "only"). A new row records the `reopen()` commit after the PRAGMA and DDL statements (`sqlite_store.py:159`). |
| N-5 | DONE, test only, in place, no new test ID | `v2/tests/storage/test_content_minimal_guard.py:313-316` and `:336`, inside `test_ver_008_policy_is_fixed_finite_and_domain_checked` | Adds `over_total_multibyte = "/".join(["é" * 127] * 16) + "/" + "y" * 17`: 2,065 characters, 4,097 UTF-8 bytes, largest segment 254 bytes. In-test assertions pin the byte length at 4,097, the character length at ≤ 4,096 and every segment at ≤ 255 bytes. The value is added to `bad_paths`, so it must fail the constructor and be rejected as both `SOURCE_CITATION` and `INVALID_VALUE`. |

## Correction of AUTHOR_RETURN_01 item 5

AUTHOR_RETURN_01 item 5 said the `str`-subclass gap "is not a content
channel" and that "the residual is limited to normalization semantics". **That
was wrong.** I assumed `sqlite3` binds the underlying string buffer. It does
not: for a non-exact `str`, `sqlite3` adapts through `__conform__`. The guard
also persists the caller's own object instead of an exact-`str` copy, and
builds rendered SHA and hash values with f-strings that call the subclass's
`__format__`.

Reproduced this cycle in the session scratchpad, against a `tempfile`
checkout and the current candidate bytes. I used a `str` subclass whose
`__conform__` and `__format__` both return a two-line body:

- `RepositoryPath(Sneaky("docs/readme.md"))`, built through the public
  constructor, was admitted (`accepted=1`). `read_all()` returned the two-line
  body as both `source_path` and the PATH field value.
- A record using the subclass as record ID, field name, source-SHA digest,
  SHA digest and hash digest was admitted. `read_all()` returned the two-line
  body as the record ID, the field name and `source_sha_digest`, and inside
  `sha1:<body>` and `blake2b-256:<body>`.

So it is a guard-wide content channel. The verifier states that it reproduces
identically at HEAD `6b4a0f59d`, which means it is pre-existing since
D-PEC-85; I did not rerun it at HEAD. R1's new checks still run on the
supplied characters, but they do not control what is persisted. Code closure
(an exact-`str` rule on every string the guard outputs) was not attempted,
per the manager's direction. It is routed for a separate owner ruling.

## Verification (on the final bytes of all seven files)

| Check | Command (cwd) | Exit | Result |
|---|---|---|---|
| v2-store-guard | `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` (`projects/pec`) | 0 | Ran 13, all `ok`; same 13 IDs and VER mapping as AUTHOR_RETURN_01 (the map is unchanged) |
| v2-core-posture | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` (`projects/pec`) | 0 | `verdict: PASS`; dependency, locality and registration PASS; findings `[]` |
| v2-loop-registry | `python3 -m unittest discover -s v2/tests/config -p 'test_*.py'` (`projects/pec`) | 0 | Ran 12, OK |
| v2-api-contract | `python3 -m unittest discover -s v2/tests/contracts/api -p 'test_*.py'` (`projects/pec`) | 0 | Ran 6, OK |
| harness-self-check | `python3 tools/practitioner_harness/harness.py self-check` (repo root) | 0 | INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124 (same as cycle 1); no finding names a changed path or the run root |
| X-1 selector | `python3 tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json v2/src/pec_v2/core/__init__.py` (repo root) | 0 | selects `harness-self-check`, `v2-api-contract`, `v2-core-posture`, `v2-loop-registry`, `v2-store-guard` |
| whitespace | `git diff --check` (repo root) | 0 | no output |
| containment | `git diff --name-only` (repo root) | 0 | exactly the seven granted paths |

Supplementary scratch evidence: a mutation measuring the total path length in
characters (`len(value) > _MAX_PATH_BYTES`) was applied to a `tempfile` copy
of `v2/src` and `v2/tests/storage`. The suite exits 1, with
`test_ver_008_policy_is_fixed_finite_and_domain_checked` failing, so the N-5
fixture catches it. The N-5 fixture was first written with a literal `é`.
It was normalized to the `é` escape used by the neighbouring fixtures
(the test file is ASCII-only again), and all checks above were rerun after
that final edit.

## Postimage SHA-256 (relative to `projects/pec/`)

| Path | SHA-256 | Changed this cycle |
|---|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `d63932c28dd346581deb0b04bb14841f00eff9481432a379ce67dd8e9d626b33` | no |
| `v2/src/pec_v2/core/ports/store.py` | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` | no |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `05b9846a2baa9a5fe2691196d83d35770b8227f8b653f39c3831dcd4b89eae0a` | no |
| `v2/tests/storage/test_store_lifecycle.py` | `edbd41df5e05573d9992ee9778aba053570b4de6d4a0bf392ff7a888ff42cadf` | no |
| `v2/tests/storage/test_content_minimal_guard.py` | `c8e23563c226585c9f557d0c7d14eb880232452ab30541fa034a643afd561c29` | yes (N-5) |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `1f626001f4a0fe228aaf5ecccc96317b79b43f0f2164f25552090bbe16e5bb5e` | yes (B-1, N-1, N-2) |
| `software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` | no |

`v2/src/pec_v2/adapters/storage/__init__.py` is unchanged and was never
opened: `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540`.

## Routed or open items

1. **`str`-subclass content channel: code closure.** An exact-`str` rule on
   every guard output string (record ID, source path, field names, PATH
   values, SHA and hash digests) needs a separate owner ruling. The manager is
   routing it, and I made no code change. Until then, the documentation now
   states the residual.
2. **`close()` not wrapped.** Unchanged from AUTHOR_RETURN_01 item 4, and the
   verifier agrees it is a scope decision.
3. **N-3 and N-4 (verifier notes, not directed).**
   - N-3: the accounting `RuntimeError` cannot be triggered by a test.
   - N-4: only the `read_all` wrapping is test-proven for R8.

   Neither needed a change under the specification. Either could be taken up
   only if the manager directs it.
4. **Interpreter-generated `__pycache__/`.** It is gitignored and was left as
   reported in cycle 1.

Nothing here claims review, acceptance, CHECKING, merge or any lifecycle
change.
