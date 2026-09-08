# Final checks

Status: PASS.

- Exact disposable composition: three ordered adoptions, `accepted-pending-publication`, `published=false`, `execution_authority=false`; four Root guards pass; 12 invalid cases reject; counts remain 53 source, 46 governance, seven Runtime and nine holds.
- Focused successor tests: 12 passed using `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python` with `PYTHONPATH=tools/validation`.
- Registered affected tests: 1380 passed, one warning, 45 subtests passed.
- G0, G1, G2 and G3: PASS. Instruction tranche schema and entrypoints: PASS.
- Root self-check exited zero with the repository's pre-existing REVIEW/WARN findings retained; no new waiver is claimed.
- Candidate whitespace against fetched `origin/main` `579015fab0c121e702d10c255d2824a86bcad58d`: PASS. `git diff --check`: PASS.

The initially supplied PR base `d4b8a8cec2e4d3c636740cb97a27fe3b1a3ef327` is not present as a commit object in this lane. Its refused whitespace invocation is preserved in `CHECK_NOTE.md`; the successful fetched-main check is retained in `check-10.log`. The same supplied base was accepted by the affected-test selector and that suite passed.
