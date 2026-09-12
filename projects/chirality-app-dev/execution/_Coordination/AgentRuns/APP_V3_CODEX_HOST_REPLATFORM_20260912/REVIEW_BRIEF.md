# Review brief: independent source review of the D-GOV-43 (A2) candidate

Prepared 2026-09-12T16:00Z by the implementing session for a fresh reviewer with no
authorship of the change. The review record goes in `INDEPENDENT_REVIEW.md` next to this
file, following the pattern in
`../APP_V3_TRIAL_COMPLETION_20260910/R16_RESTART_ADMISSION/INDEPENDENT_REVIEW.md`.

## Subject

- Checkout: this worktree, branch `claude/chirality-codex-replatform-3999f1`, HEAD `886eb2707`
  (PR #774). Base: `e83cb1f47` (merged main). Review `git diff e83cb1f47..886eb2707` for
  `projects/chirality-runtime/packages` and `projects/chirality-app-dev/frontend`
  (`electron/`, `scripts/`, `src/`, `package.json`), together with the complete final files.
  Governance and docs changes in the same range are context, not the subject.
- What the change is (settled design, not to be reopened): the App's Electron main owns and
  spawns the Runtime service as a child (`electron/runtime-service-host.ts`,
  `runtime-service-launcher.ts`) over a Unix socket with a per-launch client token; the
  service owns one stock, lockfile-pinned `codex app-server` child (`packages/daemon/src/
  codex-supervisor.ts`, `codex-app-server-client.ts`) with an effective Codex home that
  overlays the user's `~/.codex` while keeping authentication separate
  (`codex-effective-home.ts`, `codex-login.ts`); turn ownership lives in the service
  (`turn-registry.ts`) so execution, observation, interruption and shutdown are distinct;
  the App's Next routes proxy turns, attach/reconnect (`session/[id]/turn/stream?after=`),
  turn state, pending server requests and answers, and interruption
  (`src/app/api/harness/**`, `src/lib/harness/http.ts`, `client.ts`); the renderer recovers
  a running turn after a disconnect (`src/components/shell/chat-panel.tsx`); method
  transitions are additive for engines without successor preparation and the Codex adapter
  boots without a turn (`packages/core/src/runtime-method-service.ts`, `runtime-service.ts`,
  `delegated-engine-adapter.ts`). The private supplier, admission addon, LaunchAgent and
  host-account machinery are removed.
- Acceptance already recorded (do not repeat): S-1..S-8 and the disconnect check pass from
  source, `spike/EVIDENCE.md`; run history in `RUN_LOG.md`; design in `SPIKE_DESIGN.md`.

## Questions to answer

1. Turn ownership and reconnection: can a renderer disconnect, reload or reattach ever cause
   a second execution, a lost terminal frame, a stuck "active" turn, or a server request left
   unanswered? Check seq numbering, `after=` semantics, buffer retention and release, the
   keepalive, and the recovery path in `chat-panel.tsx`.
2. Interruption versus retirement (the PR #767 defect): does `turn/interrupt` interrupt only
   the turn, leaving the session and the Codex child alive, and does shutdown retire the
   child in the right order (SIGTERM, escalation, socket cleanup) without being confused with
   an interrupt? Are the regression tests deterministic?
3. Protocol completeness: every `codex app-server` server request is answered (approvals,
   user input, and unknown methods), notifications are recorded unfiltered, and the user's
   Codex configuration is not overridden except through the documented per-turn policy
   selection. Check the `-c cli_auth_credentials_store=file` argument and any other flags.
4. Authentication separation: sign-in writes credentials only into the effective home; the
   symlink overlay never links `auth.json`, `auth*`, `models_cache.json` or lock files;
   sign-out cannot touch `~/.codex/auth.json`; the project-scoped token cannot perform
   account actions; tokens and the socket are unreadable to other users; nothing logs
   credentials or the account e-mail.
5. Additive transitions and bootless boot: with instruction-policy drift no longer checked
   for additive engines, can a changed role, workflow or project instruction be silently
   dropped or applied without record? Does the "Chirality context update" path re-freeze
   the bytes with the accepting turn and record it in the session?
6. Service lifecycle and failure handling: crash of the service or Codex child, ready-line
   timeout, socket path length, stale socket, token file permissions, restart behaviour, and
   what the renderer shows in each case.
7. Packaging scripts: `scripts/pack-electron.mjs`, `verify-codex-pin.mjs`,
   `sign-electron-runtime-v2.mjs`, `finalize-electron-resources.mjs`,
   `verify-packaged-dependency-boundary.mjs`: does the packaged App run the same composition
   as the source run, and does pin verification actually bind the bundled binary to the
   lockfile version?
8. Removed code: dangling references, dead exports, retired environment variables still read,
   documentation in `frontend/docs/harness` that contradicts the code.
9. Test adequacy for the above, and any gap that should block the build.

## Constraints

- Read-only source review. Edit no product, test or documentation file except writing
  `INDEPENDENT_REVIEW.md`. Commit nothing. Do not push.
- You may run `npx tsc -b --pretty false` in `projects/chirality-runtime`, `npm run
  typecheck` in `frontend`, and focused `npx vitest run <files>` in either workspace. Do
  not run the App, Electron, the packaging scripts, or anything that opens a window or
  a network connection.
- Never read live identity, auth, token, binding, keychain, Codex home, or session/event
  files under `~/.codex`, `~/Library`, or any `userData`; do not run `security`. Reading
  source and test fixtures is the job.
- No em-dashes in prose. `file:line` references relative to the two workspace roots.

## Output

`INDEPENDENT_REVIEW.md` with: reviewer line (model, reasoning, no delegation, HEAD reviewed);
verdict PASS or FAIL; blocking findings first (each with file:line, the failure scenario and
the smallest repair); non-blocking findings by severity; the commands run with results; test
gaps. Return the verdict and the blocking findings in your final message as well.
