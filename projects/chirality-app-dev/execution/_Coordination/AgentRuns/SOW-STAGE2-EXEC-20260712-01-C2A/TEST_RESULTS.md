# C2A Manager Fan-In Test Results

Verdict: `PASS`

## Focused seam

Command: `npx vitest run` over the seven frozen API/scanner/MCP/dependency/workspace test files.

- exit: `0`;
- test files: `7 passed`;
- tests after review repair: `70 passed`;
- skipped: `0` in the focused invocation.

## Registered profile and accepted gates

The normalized evidence is in `MANAGER_CHECK_RESULTS.json`; the successful
premerge rerun is in `PREMERGE_RERUN_RESULTS.json`.

| Check | Exact registered command | Result |
|---|---|---|
| full frontend test | `npm test` | PASS — 97 files passed, 1 skipped; 707 tests passed, 4 skipped |
| frontend typecheck | `npm run typecheck` | PASS |
| frontend build | `npm run build` | PASS — Next build and Electron TypeScript build |
| repo self-check | `python3 tools/practitioner_harness/harness.py self-check` | PASS, exit 0 |
| practitioner pytest | `python3 -m pytest -q tools/practitioner_harness` | PASS — 264 passed |
| premerge, first attempt | `npm run harness:validate:premerge` | substrate FAIL — no listener at `127.0.0.1:3000`; 0 executed; all fetches failed |
| premerge, registered rerun | `npm run harness:validate:premerge` | PASS — Section 8: 8/8; Section 9 report-only: 16/16 |

For the premerge rerun, the already-built local Next app was started on the
documented loopback endpoint, the registered check ran, and the validation
server was stopped immediately afterward. The initial failure is classified
as execution substrate/configuration, not a C2A product failure.

## Review, containment, and hygiene

- independent review scope validation: PASS, 4 changed paths within 9 allowed;
- independent review found one blocker (`INVALID` could validate at `OPEN`);
- exact repair applied and regression added; focused 70/70 and typecheck PASS;
- correction-only reviewer rerun stalled; manager backcheck is recorded in
  `REVIEW_BACKCHECK.md` under the authorized read-only substrate fallback;
- final `validate_change_scope.py`: PASS, violations `[]`;
- `git diff --check -- projects/chirality-app-dev/frontend`: PASS;
- Stage-1 seam-token search: zero matches;
- owned local validation server: stopped.

No check wrote a tracked source path outside the four entries in
`CHANGED_PATHS.txt`.
