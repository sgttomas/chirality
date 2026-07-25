# F1-RENDERER-REFRESH — RETURN

**Run:** follow-up under TRB-APPDEV-DAEMON-SERVICE-2026-07-25 (owner-directed fast path: implement → fan-in to Agent 0).
**Agent:** Agent 2 (opus), sealed brief. **Branch:** `feat/daemon-handoff` (= `main` @ `612c35226`, PR #333 merged).
**Write scope honoured:** `frontend/src/**` and `frontend/src/__tests__/**` only. No `frontend/electron/**`, no `package.json`, no `globals.css`, no new styles, no git commits, no `package-lock.json` change (`git status` clean for it).

---

## 1. Defect addressed

Live-observed on the owner's machine: opening the app via Finder while the daemon runs causes the daemon to spawn the GUI and retire. The renderer's mount-time fetches land in the dead-socket window and latch terminal errors — persona roster stuck on `WORKING_ITEMS (unavailable)`, dialogue pane red `ENGINE_UNAVAILABLE: Chirality runtime daemon client is not configured`, empty session lists behind error banners. The main process later logs `runtime.connectivity.bound` and pushes `state: connected`; the top-bar RUNTIME chip updates, the data panes never do.

Root cause in renderer terms: every runtime-backed pane fetches once at mount and keeps whatever it got. The connectivity transition existed as a signal (Stage A4) but no data path consumed it.

## 2. Mechanism — one reconnect epoch, consumed as a React dependency

A single counter, incremented once per observed non-connected → connected transition, exposed through context. A pane opts in by adding one dependency to an effect it already has; there is no per-component listener to register or forget to tear down.

**`frontend/src/lib/shell/runtime-connectivity.ts`** — new pure predicate `isRuntimeReconnect(previous, next)`. True only when a *previously observed* snapshot was not `connected` and `next` is. Two deliberate calls:

- The first snapshot a renderer ever sees is never a reconnect (no predecessor ⇒ nothing failed before it), so a cold start with a healthy daemon does zero extra work.
- `connecting` counts as non-connected. The packaged-app case is a renderer that mounted while the *first* bind was still in flight; treating `connecting` as connected would leave exactly the reported failure unfixed. Cost: on a cold start where the first bind was in flight at mount, each runtime-backed pane issues one extra GET.

**`frontend/src/components/shell/runtime-connectivity-provider.tsx`** (new) — `RuntimeConnectivityProvider` holds `{ snapshot, epoch }`; `useRuntimeEpoch()` returns the epoch (or `0` with no provider); `useRuntimeConnectivitySnapshot()` returns the shared snapshot, falling back to its own subscription when rendered standalone.

**`frontend/src/components/shell/use-runtime-connectivity.ts`** — gained an `enabled = true` parameter so the provider is the app's single bridge subscriber. Without it the top bar and the epoch would be two independent listeners on the same channel; with it, the chip and the data panes provably read one snapshot. Standalone behaviour (and the existing `listenerCount() === 1` assertion) is unchanged.

**`frontend/src/app/layout.tsx`** — provider mounted outermost, above `WorkspaceProvider`.

Retry posture: **one refresh per transition, renderer-side never retries.** The main process owns retry/backoff (Stage A4); a renderer retry loop would be a second, uncoordinated one. Repeated `connected` pushes are inert by construction — the epoch only moves on a transition.

`useRuntimeEpoch()` returning `0` without a provider is what keeps ~140 existing suites that render single panes in isolation behaving exactly as before: an epoch-dependent effect runs once and stays put.

## 3. Every renderer path that reaches a daemon-backed API, and its disposition

Daemon dependence was determined by which route handlers call `getDaemonHarnessPort()`. That is exactly the ten routes under `src/app/api/harness/**`. `src/app/api/working-root/**` and `src/app/api/project/**` are pure filesystem work inside the Next server process (`lib/workspace/filesystem`) and cannot fail from daemon connectivity.

### Covered

| Call site | API | How |
|---|---|---|
| `components/shell/persona-picker.tsx` — `listDirectChatPersonas` | `GET /api/harness/agents` | epoch in effect deps; success path already clears `loadError`. This is the reported `WORKING_ITEMS (unavailable)` surface. |
| `components/shell/session-list-view.tsx` — `listHarnessSessions` | `GET /api/harness/session/list` | epoch in effect deps; the load's own `setError(null)` also clears an error left by a failed *open* (`replaySessionEvents`). |
| `components/woven-dialogue/woven-dialogue-shell.tsx` — `listHarnessSessions` | `GET /api/harness/session/list` | epoch in effect deps. Repairs three surfaces at once: Navigator mode groups, Coordination panel hierarchy, and the shell's `sessionsError`, all projections of the one `sessions` state. |
| `components/woven-dialogue/woven-dialogue-shell.tsx` — selected-session replay lens | `GET /api/harness/session/{id}/events` | new epoch effect: if the lens is `UNAVAILABLE` (still on screen — it hides only on `IDLE`), reload it once through the loader. State read via refs so the effect depends on the epoch alone and cannot re-arm itself. |
| `components/shell/chat-panel.tsx` — `createHarnessSession` / `bootHarnessSession` / `streamHarnessTurn` / `interruptHarnessSession` | `POST /api/harness/session/create`, `/boot`, `/turn`, `/interrupt` | not a mount fetch, but the latched red banner the owner saw. Cleared on epoch change. Deliberately **cleared, not retried** — the draft is left intact and the operator's next send is the retry. |
| `components/settings/runtime-settings.tsx` — daemon/model status | Electron IPC → daemon | re-probed on epoch. Its entire content is a claim about the daemon ("not running", "no models"); a claim captured while unbound is the one the operator opens the panel to check. |

### Deliberately not covered, with reasons

- **`components/shell/permission-requests.tsx`** (`POST /api/harness/permission`) — no mount fetch; its error state already self-clears when no requests are live (`live.size === 0` → `setError(null)`). Adding an epoch dependency would change nothing.
- **`components/pipeline/pipeline-surface.tsx`** (`POST /api/harness/scaffold`) — user-initiated, one-shot action error, no mount fetch. Re-running a scaffold on reconnect would be a side effect, not a refresh.
- **`components/workspace/deliverables-provider.tsx`, `workspace-provider.tsx`, `workbench/workbench-surface.tsx`, `shell/file-tree-panel.tsx`, `shell/document-view.tsx`, `shell/file-picker.tsx`** — all hit `/api/project/**` or `/api/working-root/**`, which never touch the daemon port. Making them epoch-aware would add refetches that fix nothing.
- **`lib/harness/mcp/pec-bridge-client.ts`** — a separate external bridge, not the runtime daemon; out of scope.
- **`ChatPanel.activeSession`** — *not* invalidated on reconnect. See risk R-2.

## 4. Test additions

Four new files plus additions to two existing ones; conventions matched per suite (bare-node vitest, `react-test-renderer`, class-name traversal, fake desktop bridge on `globalThis.window`, no DOM/CSS/timers). No existing assertion was modified; the `data-chat-input="primary"` contract and ARIA polarity assertions are untouched.

- `src/__tests__/lib/shell-runtime-connectivity.test.ts` (+5) — `isRuntimeReconnect`: disconnected→connected, connecting→connected, first-observation is never a reconnect, repeated `connected` is inert, no non-connected terminus counts.
- `src/__tests__/components/runtime-reconnect-refresh.test.tsx` (new, 6) — end-to-end through the real provider and real panes: **epoch bumps on reconnect push**; **exactly one refetch per transition**; **stale `ENGINE_UNAVAILABLE: …` banner cleared and `WORKING_ITEMS (unavailable)` replaced by the real roster**; **no refetch on duplicate `connected` push**; no refetch on drop-out; a pane rendered *without* the provider is unchanged (guards the isolated suites); session list re-lists via `connecting → connected` and stays silent when no Working Root is selected.
- `src/__tests__/components/chat-panel-runtime-reconnect.test.tsx` (new, 1) — failed send latches the banner, reconnect clears it, draft preserved, `streamHarnessTurn` never re-invoked.
- `src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx` (new, 3) — shell re-lists once and clears `sessionsError`, then ignores a repeated `connected`; an `UNAVAILABLE` replay lens is reloaded exactly once; an idle lens is left alone.
- `src/__tests__/components/runtime-settings-reconnect.test.tsx` (new, 1) — daemon re-probed once per reconnect, not on a repeated report.
- `src/__tests__/components/shell-frame-runtime-connectivity.test.tsx` (+1) — with the provider mounted, the chip reads the shared snapshot and there is still exactly **one** bridge listener.

## 5. Validation

```
cd projects/chirality-app-dev/frontend
npm run typecheck   # clean (tsc + tsc -p tsconfig.electron.json)
npx vitest run
```

- **Baseline (start of run):** 136 passed | 1 skipped files — **1060 passed | 4 skipped** tests.
- **Final full suite:** 141 passed | 1 skipped files — **1093 passed | 4 skipped** tests. **0 failures.**
- **Attributable to this run:** +17 tests (6 files exercised: 34 passed, of which 17 pre-existing). Verified by running only the files this run touched.
- **The remaining +16 (and 1 file) are a sibling agent's uncommitted work in the same worktree** — `frontend/electron/runtime-socket-watch.ts` + `src/__tests__/electron/runtime-socket-watch.test.ts` (13) and 3 tests added to `src/__tests__/electron/runtime-connectivity.test.ts`. So this run alone would read **1077 passed | 4 skipped**. See risk R-4.
- `npm run build` not run: `build:electron` would compile the sibling's in-flight `frontend/electron/**`, and it is the integration owner's gate. The only App-Router-structural change here is one client provider wrapping the existing provider chain in `layout.tsx`, mirroring `WorkspaceProvider`; typecheck is clean.
- No commits made. `git status` shows `package-lock.json` untouched.

## 6. Risks and notes for Agent 0 review

- **R-1 (behaviour, low): a reconnect that lands immediately after a mid-turn failure will clear the chat banner quickly.** Sequence: daemon drops mid-turn → turn fails, banner shown → daemon returns seconds later → banner cleared. The banner is stale by then and the transcript/draft are preserved, but an operator who looked away loses the text of the failure. Narrowing this to connectivity-class error codes only was considered and rejected as extra classification for a marginal case; flagging rather than deciding.
- **R-2 (pre-existing, not changed): `ChatPanel.activeSession` is not invalidated on reconnect.** If the daemon actually restarts (rather than the client merely rebinding to a live daemon), the cached `sessionId` may no longer exist daemon-side, and `ensureSessionBooted` returns it without revalidating — a latch of a different kind, cleared only by changing persona / mode / Working Root. Clearing it on reconnect would have discarded a still-valid session in the *reported* scenario (client rebinding to a daemon that never died), so it was left alone. Recommend assessing against Stage V drill 3 ("kill daemon mid-session").
- **R-3 (pre-existing defect found, not fixed): the replay lens "Retry" button is a no-op.** `SelectedSessionReplayLens.onRetry` calls `loadReplay(selectedReplayId(replayState))`, and `guardRecordedSessionSelection` answers `UNCHANGED` for a re-request of the session already selected (`guarded-session-selection.ts:79-84`), so the shell returns before reaching the loader. Out of this brief's scope (it is not a connectivity defect), and the reconnect path added here bypasses the guard deliberately, so a stale lens now recovers on reconnect even though its button still does nothing. Candidate for the F-3/F-7 replay-lens residual tranche.
- **R-4 (process): two agents were writing into the same worktree concurrently.** F1-SERVICE-SIGNAL's `frontend/electron/**` work is uncommitted in this checkout alongside mine. Scopes are disjoint (verified by `git status`), and nothing here touched their files, but the full-suite counts above are joint. The integration owner should re-baseline after serializing the two returns.
- **N-1:** one extra GET per runtime-backed pane on a cold start whose first bind was still in flight at mount — the accepted cost of treating `connecting` as non-connected (§2).
- **N-2:** `useRuntimeConnectivity` gained an optional parameter. Every existing caller is unaffected; the parameter exists solely so the provider can be the single subscriber.
