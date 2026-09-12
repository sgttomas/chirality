# G — App model/reasoning selection tranche (DESIGN.md §7 steps 6-7) — RETURN

Role: TASK. Worktree: `.claude/worktrees/owner-alignment-inspection-db4335`, branch
`claude/chirality-v3-mvp-trial-ab05cb`. `F` = `projects/chirality-app-dev/frontend`. Nothing committed,
stashed, installed, or packaged. No file under `F/electron/**`, `projects/chirality-runtime/**`, or any
preserved checkout was modified. Other authors' uncommitted changes in the tree were left intact. Runtime
`dist` was consumed as rebuilt by tranche F (not rebuilt here).

Inputs read in full: `D_MODEL_SELECTOR_DESIGN/DESIGN.md` (§5, §6, §7), `F_RUNTIME_MODEL_SELECTION/RETURN.md`
§1 (the contract consumed below).

## 1. Files changed (all under `F/src`)

Product:
- `lib/harness/hosted-bootstrap-context.tsx` (new) — `HostedBootstrapProvider`, `useHostedBootstrap()`,
  `selectHostedModelCatalog(snapshot)` (catalog only when `registration === 'registered'`,
  `ceremony === 'signed-in'`, `admission === 'ready'`, and `models`/`selection` present), `isSelectionInCatalog`.
- `components/shell/shell-frame.tsx` — `AccountPresentation` wraps its children in `HostedBootstrapProvider`
  fed from the one existing `useHostedBootstrapController` instance (no second controller or poll).
- `components/shell/chat-panel.tsx` — `useHostedBootstrap()`; `modelChoice` state (null = admitted default);
  `nextSessionSelection` = valid explicit choice or `status.selection`; effect drops a choice not in the current
  catalog; draft hydrate/persist carry `model`/`reasoningEffort`; `ActiveSession` (+) `model`/`reasoningEffort`
  read from the booted/created record (`recordedModelSelection`) and from a resumed projection;
  `createHarnessSession` sends `modelSelection` whenever a catalog is present; boot and turn send no
  `opts.model`; two labelled selects "Model" and "Reasoning" in the existing context row after "Interaction
  mode", same `chat-mode-selector` class, explanations only in `title`; catch path maps
  `MODEL_NOT_IN_CATALOG` with the session's model.
- `lib/harness/chat-draft.ts` — `ChatDraftSnapshot` (+) optional `model`/`reasoningEffort`, sanitised as a pair
  with `HOSTED_MODEL_ID_PATTERN`/`HOSTED_REASONING_EFFORT_PATTERN` from contracts (partial or malformed → dropped);
  a pair alone is a nonempty snapshot.
- `lib/harness/client.ts` — `createHarnessSession` input (+) `modelSelection?: HarnessModelSelection`.
- `app/api/harness/session/create/route.ts` — passes `modelSelection` through verbatim.
- `lib/runtime-client/daemon-harness-port.ts` — `V3SessionCreateRequest` (+) `modelSelection`.
- `lib/runtime-client/runtime-daemon-harness-port.ts` — `createSession` forwards `modelSelection` to
  `RuntimeClient.createSession`. `asLegacySession`/`replaySession` already return the record unchanged, so
  `reasoningEffort` is kept (now pinned by a test).
- `lib/harness/error-display.ts` — `modelNotInCatalogUiError` + `toHarnessUiError(error, { sessionModel })`:
  `details.reason === 'MODEL_NOT_IN_CATALOG'` (boot route `details` or turn-stream `turn:error.details`) →
  "This chat used <model>, which your Codex account no longer offers. Start a new chat."
- `lib/harness/toolkit.ts`, `components/shell/operator-toolkit-panel.tsx` — free-text `opts.model` removed
  (`ToolkitValues.model`, sanitiser, opts builder, input); `tools`/`maxTurns`/governance kept. A stray stored
  `model` value is ignored by the sanitiser.
- `lib/woven-dialogue/contracts.ts`, `lib/woven-dialogue/operator-projection.ts` — `OperatorSessionProjection`
  (+) `reasoningEffort`, read with `readString(source.reasoningEffort)`, included in `projectionSignature`.
- `components/woven-dialogue/selected-session-replay-lens.tsx` — "Reasoning" row directly under
  "Recorded model selection".

Tests (DESIGN §6 App list):
- new `__tests__/components/chat-panel-model-selectors.test.tsx` (9 cases): signed out / no catalog →
  disabled + "Sign in to Codex to choose a model" + placeholder option, and a session created while signed out
  carries no `modelSelection`; options from `status.models`, default from `status.selection`, help only in
  `title`, `chat-mode-selector` reused; effort resets to the model's default on model change and the pair is
  persisted with the draft (out-of-list effort / unknown model ignored); stored pair outside the catalog dropped
  (model gone, or effort unsupported) and the admitted default used; `createHarnessSession` called with the
  displayed `modelSelection`, boot request `{ sessionId }` only, turn `opts` has no `model`, both selects fixed
  and disabled with the fixed-title showing the recorded pair even after the catalog changes, entry draft keeps
  the pair; default pair sent when nothing chosen; Plan Mode select unchanged and independent (only
  `Interaction mode`, `Model`, `Reasoning` selects exist — no permission selector); resumed projection shows the
  recorded pair fixed, and no invented effort when the record has none; `MODEL_NOT_IN_CATALOG` on boot and on the
  turn stream renders the design message, nothing rewritten.
- `__tests__/lib/runtime-daemon-harness-port.test.ts` — `createSession` forwards `modelSelection` (exact
  Runtime request), omits it when absent, `replaySession` keeps `reasoningEffort`.
- `__tests__/lib/harness-chat-draft.test.ts` — round-trip; partial/corrupt/over-length values dropped; pair-only
  snapshot stored, removed when cleared.
- `__tests__/lib/hosted-bootstrap-client.test.ts`, `__tests__/electron/host-account-ipc.test.ts` — a ready
  status with `models`/`selection` passes through untouched (`toEqual`).
- `__tests__/lib/operator-projection.test.ts` — `reasoningEffort` projected, absent/blank/non-string omitted,
  effort difference makes duplicates `CONFLICTING`.
- `__tests__/components/hosted-bootstrap.test.tsx` — settings view unaffected by the extra keys.
- `__tests__/components/selected-session-replay-lens.test.tsx` — Reasoning row rendered under Model only when
  recorded.
- `__tests__/lib/harness-toolkit.test.ts` — updated for the removed field; new case that `opts.model` is never
  emitted.
- `__tests__/components/chat-panel-folder-binding.test.tsx` — the "no permission selector" assertion now lists
  `['Interaction mode', 'Model', 'Reasoning']` (same proof: no permission posture select).

## 2. Deviations from DESIGN.md (and why)

1. **Provider placement.** DESIGN names `shell-frame.tsx:401-415`; in the current tree that is
   `AccountPresentation`, whose `children` is a render callback producing the workspace content (which contains
   `ChatPanel`). The provider wraps that callback's output. Non-workspace variants render no provider; the
   context default reads as signed out, and the context row itself only renders for `presentation === 'woven'`.
2. **Selection sent when catalog present, not only when explicitly chosen.** `createHarnessSession` sends the
   displayed pair (explicit choice or `status.selection`) whenever a catalog is present, so the request names
   exactly what the UI shows and a stale App snapshot is rejected by Runtime rather than silently defaulted.
   With no catalog, no `modelSelection` is sent (Runtime's `MODEL_SELECTION_UNSUPPORTED`/default path applies).
3. **Entry-draft consumption keeps the pair.** The existing first-turn consumption of the entry draft key
   clears draft/attachments/methods; the model pair is kept there so the next new chat offers the same pair
   (still re-validated against the current catalog before use). Methods are per-message references and stay
   consumed; the model pair is a session-level choice.
4. **Turn-stream error names the session's model from local state.** Runtime's `turn:error.details` carries
   only `runtimeCode` and `reason` (F RETURN §1), so the App supplies `activeSession.model` for the message;
   the boot route's `details.model` is preferred when present.
5. **Fake daemon port unchanged.** `__tests__/api/harness/fake-daemon-harness-port.ts` forwards the request
   object as-is to the in-process session manager, which ignores unknown keys, so no edit was needed for the
   interface extension.
6. **Fixed-session options.** When a session is active, each select renders exactly one option (the recorded
   value, or the placeholder if the record lacks it) so the value is visible while disabled; no catalog lookup
   is used for a fixed session.
7. **Status validators.** No App change was needed: `hosted-bootstrap-client.ts` and the Electron IPC forward
   the status object verbatim (confirmed by the new pass-through tests); the contracts validator in `dist`
   already accepts the keys.

## 3. Commands and results (from `F`, `PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:…`)

- `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json` → exit 0 (no output).
- `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.electron.json` → exit 0 (no output).
- `node node_modules/vitest/vitest.mjs run` (full frontend suite, final bytes) →
  **Test Files 209 passed | 1 skipped (210); Tests 2214 passed | 4 skipped (2218)**, 7.04s.
  Baseline before this tranche: 208 passed | 1 skipped; 2197 passed | 4 skipped. Delta: +1 file (the new
  selector suite), +17 tests. One stdout line `{"status":"FAIL","summaryPath":…daemon-proof-test…}` is printed by
  a packaged-proof script test exercising its failure path; it was present in every run and is not a test
  failure.
- `node node_modules/vitest/vitest.mjs run src/__tests__/components/chat-panel-model-selectors.test.tsx
  src/__tests__/lib/runtime-daemon-harness-port.test.ts` → 2 files, 35 passed.
- Intermediate run after the first pass flagged one pre-existing assertion
  (`chat-panel-folder-binding.test.tsx` select-list pin) — updated as in §1, no product change.

## 4. What only a native run can prove

- That the packaged Codex `model/list` produces the catalog shape Runtime publishes (field names, hidden
  semantics, effort labels) and that the selects therefore show real account models.
- That a non-default model and a non-default effort chosen in the selects are honoured by `thread/start`/
  `turn/start` under the native policy, and that the provider reports the same effort back.
- End-to-end sign-in → catalog appears in the context row → chat with chosen pair → replay lens shows Model and
  Reasoning → re-sign-in with a reduced catalog → boot of the old chat shows the "no longer offers" message.
- The visual fit of two more compact selects in the context row at real window widths (styling reuses
  `chat-mode-selector`; no CSS was changed).

## 5. Known limits (unchanged from F)

Managers (`startManager`) stay on the admitted default model; the v1 managed-auth / standalone paths publish no
catalog, so the selects stay disabled there with the sign-in title (they never invent a list).
