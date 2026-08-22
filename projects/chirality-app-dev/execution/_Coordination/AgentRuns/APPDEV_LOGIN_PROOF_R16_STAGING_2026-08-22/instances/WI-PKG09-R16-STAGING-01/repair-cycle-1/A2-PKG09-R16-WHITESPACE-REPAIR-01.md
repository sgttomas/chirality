# Sealed Agent 2 brief — R16 whitespace repair cycle 1

- Parent: WORKING_ITEMS instance `WI-PKG09-R16-STAGING-01`
- Role/form: fresh ephemeral generalist Agent 2 executor
- Session: `A2-PKG09-R16-WHITESPACE-REPAIR-01`
- Basis: branch `codex/app-login-proof-r16-staging`; exact HEAD
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`; empty index
- Delegation: prohibited
- Build, proof, GUI, operator-path, temp-root, or Git mutation: prohibited

## Exact objective and byte authority

Repair exactly twelve whitespace defects reported by CHANGE:

1. Delete exactly one surplus final LF, leaving exactly one terminal LF, in
   each of these six files beneath the run root:
   `CHAT_TRANSCRIPTION.md`, `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`,
   `instances/WI-PKG09-R16-STAGING-01/ACTIVATION_AND_WORK_GRAPH.md`,
   `instances/WI-PKG09-R16-STAGING-01/briefs/A2-PKG09-R16-EXECUTE-01.md`, and
   `instances/WI-PKG09-R16-STAGING-01/briefs/AMENDMENT_02_POST_COMMIT_STEP0_PORTABILITY.md`.
2. In both `instances/WI-PKG09-R16-STAGING-01/executor/desktop-pack.log` and
   `instances/WI-PKG09-R16-STAGING-01/executor-attempt-2/desktop-pack.log`,
   remove only the trailing carriage-return/whitespace bytes on lines 16, 17,
   and 18. Preserve the visible build-log text and line boundaries.

Prove the direct delta is exactly six one-byte terminal-LF deletions plus six
trailing-whitespace repairs at the named log lines, with no other direct
subject byte change. Then compute old/new SHA-256 identities and search the
entire 35-path subject and repair controls for every stale current reference.
Refresh only directly dependent current hash/reference fields and the current
manager return as needed. Do not rewrite historical raw evidence merely
because it records a then-current hash; distinguish historical evidence from
a claim of current identity. Do not change package identity, R16 procedure,
DEL lifecycle, verdict, fence, state, command, path, count, or other semantic
claim.

## Write scope

- the eight exact direct-repair files above;
- only current-reference-bearing files inside the existing run root or R16
  record whose hash tokens are made stale by the direct repair;
- this cycle's `executor/RETURN.md` plus read-only-check logs under
  `repair-cycle-1/executor/`.

Do not change DEL `_STATUS.md` unless it contains a current hash reference
made stale by the direct repair. Do not write outside
`projects/chirality-app-dev/`.

## Mandatory validation and return

- preserve before copies or hashes sufficient to reconstruct all direct byte
  transitions without writing outside the authorized repair-cycle evidence;
- inventory the exact original 35 subject paths and prove no missing/extra
  subject path;
- run `python3 tools/validation/validate_candidate_whitespace.py --repo-root .
  --base-ref origin/main --paths projects/chirality-app-dev`;
- run `git diff --check -- projects/chirality-app-dev` and
  `git diff --cached --check`;
- run `git diff --no-index --check /dev/null <path>` separately for every
  non-ignored untracked text file in the 35-path subject and all new repair
  controls, accepting only the normal no-index content-difference status and
  rejecting any whitespace diagnostic;
- construct a staged-equivalent patch of all untracked/new candidate files in
  a temporary index or temporary patch, run `git apply --check --whitespace=error-all`
  and/or equivalent Git whitespace checking, and leave the real index byte-for-byte
  empty;
- require App-only containment, exact HEAD unchanged, no build/proof/operator
  boundary action, and no semantic delta beyond refreshed identity references;
- return `PASS` or `FAIL` with exact old/new hashes, updated dependent paths,
  command exit statuses, findings, and rerun triggers.

Use `apply_patch` for authored-file edits. A deterministic formatting command
may normalize only the six exact CR/trailing-whitespace locations in the two
raw logs. Do not stage, commit, push, merge, build, launch, prepare, capture,
bootstrap, kickstart, or delegate.
