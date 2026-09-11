# H_REVIEW_FIXES — RETURN

Type 2 TASK return for the six non-blocking findings (N2, N3, N6, N8, N9, N10)
from `../CONSOLIDATED_REVIEW.md`. Worktree branch
`claude/chirality-v3-mvp-trial-ab05cb`; nothing committed, stashed, installed,
or built beyond `npm run typecheck` (which refreshes R `dist`). No file outside
`R/packages/*/src`, `R/tests`, `F/src`, `F/electron` was touched, and no
validation or test was weakened.

`R` = `projects/chirality-runtime`, `F` = `projects/chirality-app-dev/frontend`.

## Items

### N2 — shared pattern constants (R)

Files:
- `R/packages/core/src/runtime-service.ts` — imports `HOSTED_MODEL_ID_PATTERN`
  / `HOSTED_REASONING_EFFORT_PATTERN` from `@chirality/runtime-contracts`;
  `validateModelSelection` now tests against them. Kept as the pre-catalog
  shape gate (the daemon policy returns without validation when no catalog is
  retained, so RuntimeService must still reject a malformed/unmet selection);
  doc comment added saying catalog membership is decided only by
  `resolveHostedModelSelection`. There was no second, separate duplicate check
  to delete — the finding's "duplicates" is this same function, which the
  brief says to keep.
- `R/packages/daemon/src/codex-supervisor.ts` — constructor reasoning-effort
  check (`:143`) and `assertCatalogChoice` model/effort checks (`:242-243`) use
  the constants. The constructor's model check (`length > 128 || /[\x00-\x1f]/`)
  is a different, looser rule and was left as is.
- `R/packages/core/src/delegated-runtime.ts` — `resolveTurnAttribution` no
  longer builds `new RegExp(...)` per call; the helper takes the constant.

Behaviour is byte-identical (same regex source, same messages, same reasons);
the existing R tests pass unchanged. Other inline `[\x21-\x7e]` regexes in
`codex-session.ts`, `hosted-identity-binding.ts`, etc. were outside the
finding and were not touched.

### N3 — create-path wording for MODEL_NOT_IN_CATALOG (F)

Files:
- `F/src/lib/harness/error-display.ts` — `modelNotInCatalogUiError(error,
  context)` and `toHarnessUiError(error, context)` take
  `HarnessUiErrorContext { sessionModel?, origin?: 'session-create' | 'session' }`.
  `origin: 'session-create'` renders
  "Model <X> is no longer offered by your Codex account. Refresh your account
  status and choose again." (model-less fallback: "The chosen model is no
  longer offered by your Codex account. Refresh your account status and choose
  again."), nextStep "Refresh your account status and choose a model your
  account offers." Default/`'session'` keeps the existing "This chat used <X>,
  which your Codex account no longer offers. Start a new chat."
- `F/src/components/shell/chat-panel.tsx` — a `sessionCreateInFlight` ref is
  set just before `createHarnessSession` and cleared when it resolves; the
  submit catch passes `origin` accordingly (boot and turn-stream failures keep
  the session wording, including boot right after a successful create).
- Tests: `F/src/__tests__/components/chat-panel-model-selectors.test.tsx`
  (new: create rejection shows the refresh wording, boot/stream are not
  called, selectors stay enabled; a subsequent boot failure on the same panel
  shows the session wording) and
  `F/src/__tests__/lib/harness-error-display.test.ts` (new: both origins,
  default origin, and model-less fallback).

### N6 — `within()` escape test (F/electron)

- `F/electron/attachment-picker.ts` — `relative === '..' ||
  relative.startsWith('..' + path.sep)`; the absolute/realpath containment is
  unchanged.
- `F/src/__tests__/electron/attachment-picker.test.ts` — fixture adds a real
  in-root `..notes.md` and an out-of-root `escape.md`; new test asserts
  `..notes.md` is accepted (canonical path returned) and that `../escape.md`,
  `docs/../../escape.md`, the `link-out.txt` symlink escape, and the parent
  directory are still rejected with "inside the project folder".

### N8 — single `HostedProjectInitializationResponse` (F)

- Declared once in `F/src/lib/runtime-client/daemon-harness-port.ts` (already
  exported there). `F/src/lib/harness/hosted-bootstrap-client.ts` now does
  `import type { HostedProjectInitializationResponse } from
  '../runtime-client/daemon-harness-port'` and re-exports it as a type so
  existing importers of the client module are unaffected. The port module
  imports `node:path`, so only a type-only import is renderer-safe; `import
  type` is erased at compile time and the renderer `tsc` project is clean.

### N9 — drop unused `runtime` / `legacyHref` from `AccountPopoverProps` (F)

- `F/src/components/shell/account-popover.tsx` — props and the
  `void legacyHref; void runtime;` line removed; unused
  `RuntimeSettingsViewProps` import removed.
- `F/src/components/shell/shell-frame.tsx` — `AccountRow` call site no longer
  passes them; the internal `AccountPresentation` no longer takes `legacyHref`
  (it only forwarded it), and `ShellFrame` no longer destructures it. The
  public `ShellFrameProps.legacyHref?` is left in place because
  `woven-dialogue-shell.tsx` still passes it (and separately uses `legacyHref`
  for `Navigator`); it is now accepted-but-unused by `ShellFrame`. Removing it
  from the ShellFrame contract would touch the woven shell and its test mock,
  which is beyond this finding — flagged for the owner.
- `account-row.tsx` needed no change (it spreads `AccountPopoverProps`).
- `F/src/__tests__/components/account-presentation.test.tsx` — `AccountRow` /
  `AccountPopover` usages no longer pass `runtime`/`legacyHref`; the two
  popover tests that only built a `runtime` object to pass in were reduced to
  their rendered-content assertions (`it.each([false,true])` collapsed to one
  `it`, since the loaded flag no longer reaches the popover). `SettingsView`
  usages keep `runtime`.

### N10 — catalog on the controlled fixture engine (F test)

- `F/src/__tests__/electron/hosted-account-sequence.integration.test.ts` —
  `CATALOG_ENTRIES` (default `fixture-model` high [low, medium, high];
  `fixture-alt` medium [medium, low]); `materializeAdmission` returns
  `catalog: hostedModelCatalog(CATALOG_ENTRIES)` with `selection.model =
  catalog.default.model` (the daemon requires the selection to be the catalog
  default). Step 7 (completed login) now asserts the status observed through
  `performHostAccountOperation` → real `HostAccountClient` with exact
  `toEqual`, including `models` and `selection: { model: 'fixture-model',
  reasoningEffort: 'high' }`; step 8 (after sign-out) asserts with exact
  `toEqual` that `models`/`selection` are gone.

## Checks

| Check | Result |
|---|---|
| F `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json` | clean (no output, exit 0) |
| F `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.electron.json` | clean |
| R `npm run typecheck` (`tsc -b`, emits dist) | clean; `dist` for core/daemon now references the imported constants |
| Targeted F files (chat-panel-model-selectors, harness-error-display, attachment-picker, account-presentation, hosted-account-sequence.integration) | 5 files, 57 tests passed |
| Targeted R files (hosted-bootstrap-integration, codex-primary-chat-integration) | 2 files, 8 tests passed |
| Full F suite `node node_modules/vitest/vitest.mjs run` | **209 passed / 1 skipped files (210); 2216 passed / 4 skipped tests (2220)** — baseline 2214 + 3 new tests − 1 collapsed `it.each` pair = +2 |
| Full R suite `node node_modules/vitest/vitest.mjs run` | **81 passed / 1 skipped files (82); 1073 passed / 14 skipped tests (1087)** — identical to baseline; the two known load-sensitive tests did not flake on this run, so no solo rerun was needed |

Note: the full F run prints one `{"status":"FAIL","summaryPath":...}` JSON line
to stdout; that is a daemon-proof test's expected fixture output, not a test
failure (the suite reports 0 failures).

## Files changed (all uncommitted, alongside the pre-existing tranche)

- `R/packages/core/src/runtime-service.ts`
- `R/packages/core/src/delegated-runtime.ts`
- `R/packages/daemon/src/codex-supervisor.ts`
- `F/src/lib/harness/error-display.ts`
- `F/src/components/shell/chat-panel.tsx`
- `F/electron/attachment-picker.ts`
- `F/src/lib/harness/hosted-bootstrap-client.ts`
- `F/src/components/shell/account-popover.tsx`
- `F/src/components/shell/shell-frame.tsx`
- `F/src/__tests__/components/chat-panel-model-selectors.test.tsx`
- `F/src/__tests__/lib/harness-error-display.test.ts`
- `F/src/__tests__/electron/attachment-picker.test.ts`
- `F/src/__tests__/components/account-presentation.test.tsx`
- `F/src/__tests__/electron/hosted-account-sequence.integration.test.ts`
- `R/packages/*/dist` refreshed by `npm run typecheck` (generated)
