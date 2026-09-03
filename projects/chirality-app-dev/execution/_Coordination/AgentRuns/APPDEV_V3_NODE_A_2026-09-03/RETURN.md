# RETURN — A1_IMPLEMENTER (frozen for independent review)

- **Run:** `APPDEV_V3_NODE_A_2026-09-03` · **Executor:** Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · **Skill method:** `software-bounded-implementation`
- **Basis:** `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge; exactly the required basis) · **Branch:** `codex/app-v3-nodeA-credential-ipc-2026-09-03` · **Frozen commit:** recorded in the freeze message to HELP_HUMAN (this file predates the commit that contains it; the commit SHA is the diff's identity)
- **Items:** DEL-09-06-V3-01, DEL-04-05-V3-01, DEL-02-05-V3-01 (one integration owner for the shared `frontend/electron/api-key-ipc.ts`)
- **Status:** implementation complete; every registered check passes except the premerge, which failed in the recorded absent-runtime-daemon-bindings class and is deferred to PR CI; `REVIEW_READY`. Nothing pushed; no `_STATUS.md`, receipt, `HANDOFF_STATE.md`, or `MANIFEST.sha256` written yet (those follow `REVIEW_PASS`).

## 1. Behavioural summary

**Sender authorization (DEL-09-06-V3-01).** The origin policy formerly private to `runtime-control-ipc.ts` now lives in `frontend/electron/ipc-sender-policy.ts` (`isAuthorizedSender`, plus `describeIpcSender` for origin-only diagnostics). `runtime-control-ipc.ts` imports it (behaviour identical; its 11 tests unchanged). `api-key-ipc.ts` takes `ApiKeyHandlerOptions { rendererOrigin, log? }` and guards all six channels before any argument validation or daemon call; a foreign, missing, or unparseable sender gets `{ ok:false, error:'Credential request was denied' }` on the three mutation channels and a fail-closed status object carrying the same `error` on the three status channels, plus one `warn desktop.credential_ipc.denied { channel, sender:<origin> }` line. `main.ts` now resolves `rendererOrigin` once and registers the credential handlers after the renderer URL is known (the window is created later, so nothing can call them in the gap); the same origin feeds the runtime-control handlers as before.

**Typed safeStorage states (DEL-04-05-V3-01).** New shared vocabulary `frontend/src/lib/credential-storage-state.ts` (`missing | storageUnavailable | decryptFailed | available` + guard). `api-key-storage.ts` gains `readProviderCredential` (exact definitions in its doc-comment; strictly non-destructive; only the pre-existing permission-bit repair mutates anything), `probeProviderCredentialStorage` (state only), and `SafeStorageCredentialStore.status()` → `{ configured, source, storage }`. Source precedence is untouched; the state is orthogonal, so `env` + `decryptFailed` is representable. `retrieveProviderApiKey` is now a thin wrapper with identical results. The daemon spreads the store's status verbatim (`runtime-daemon.ts:278`), so the field reaches `RuntimeClient` and the IPC layer with **no `runtime/**` change** — confirmed end-to-end by the packaged proof, which shows the real daemon reporting `missing → available/ui → missing`. The IPC projection validates `storage`, fails closed on unknown values or inconsistent `(source, storage)` pairs, derives `encryptionAvailable = storage !== 'storageUnavailable'`, and maps a pre-typed-state daemon answer to what that daemon could distinguish (`ui → available`, else `missing`; commented as compatibility).

**Settings panel (DEL-02-05-V3-01).** `api-key-settings.tsx` carries `storage?` on `ApiKeyStatus`, renders `data-storage` on the status line, and adds two remediation paragraphs (`p.api-key-warning[data-storage-state]`): `storageUnavailable` (keychain unavailable; stored key left in place unread; set `<ENV>` and restart; entry hidden) and `decryptFailed` (could not be decrypted, cannot be used, kept unchanged, nothing deleted; re-enter or remove explicitly; names the env variable when one is in use; entry open and "Remove Stored Key" offered). Labels stay source-first; a legacy answer without `storage` maps conservatively. No key material in the DOM beyond the masked controlled input.

## 2. Files (17 at freeze, before this RETURN/evidence set; see `git show --stat` of the frozen commit for the full list)

Product: `frontend/electron/{api-key-ipc.ts, api-key-storage.ts, ipc-sender-policy.ts (new), main.ts, runtime-control-ipc.ts}`, `frontend/src/components/settings/api-key-settings.tsx`, `frontend/src/lib/credential-storage-state.ts (new)`. `preload.ts` needed no change (channels and pass-through unchanged).
Tests: `frontend/src/__tests__/electron/{ipc-sender-policy.test.ts (new), api-key-ipc.test.ts, api-key-storage.test.ts}`, `frontend/src/__tests__/components/{api-key-settings-storage-states.test.ts (new), api-key-settings.test.ts}`, `frontend/src/__tests__/contract-pins.manifest.ts`.
Evidence/state: DEL-09-06 `Evidence/Node_A_Credential_IPC_Sender_Authorization_2026-09-03/**` and `_run_records/TASK_RUN_2026-09-03_NODE_A.md`; DEL-04-05 `Evidence_TYPED_STORAGE_STATES_2026-09-03.md` and `_run_records/TASK_RUN_2026-09-03_NODE_A.md`; DEL-02-05 `Evidence_TYPED_STORAGE_STATES_UI_2026-09-03.md` and `_run_records/TASK_RUN_2026-09-03_NODE_A.md`; this run record (`ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`, `STEP0_DISCOVERY.md`, `CHECKS.json`, `RETURN.md`, `instances/A1_IMPLEMENTER/LAUNCH_BRIEF.md`).

## 3. Check evidence (full table with commands, cwd, exit codes: `CHECKS.json`)

| Check | Result |
|---|---|
| `npm run typecheck` | pass |
| `npm test` (full Vitest) | pass — 157 files passed / 1 skipped; 1364 tests passed / 4 skipped |
| focused Vitest (7 touched files) | pass — 151 tests |
| `npm run build` | pass |
| premerge (`next dev` :51226 + `harness:validate:premerge`) | **FAIL — absent runtime-daemon bindings class** (8/8 HTTP 503; LOOP_RECEIPTS.md:5183, :5313 precedent); deferred to PR CI per AGENTS.md; no pass inferred; server stopped before later build/pack |
| `npm run desktop:pack` | pass (in-sandbox; no escalation needed) |
| `npm run proof:packaged-security` | pass (in-sandbox); identity `f8b954e1…`; compact bytes retained under DEL-09-06 evidence with `MANIFEST.sha256` |
| `git diff --check` | pass |
| harness `self-check` | pass (exit 0) |
| harness pytest | pass (350) |
| APP-HOLD dispatch preflight / scan | ALLOW / PASS |
| `select_affected_checks.py` | recorded; all selected checks executed |
| `validate_change_scope.py` (brief fence) | PASS (re-run at freeze over the final file set; see freeze message) |
| Receipts validator; corpus status | VALID; no drift (Step 0) |

## 4. Write-scope validation

Every changed path is inside the brief's fence: the five named `electron/` files plus the one new shared policy module, the settings component, `src/lib/credential-storage-state.ts`, `src/__tests__/**`, the three deliverable folders (evidence + `_run_records` only at freeze; `_STATUS.md` untouched until `REVIEW_PASS`), and this AgentRuns record. `validate_change_scope.py` → `PASS`, `violations: []`. Not touched: `runtime/**`, `package.json`/lockfiles (no dependency change), `preload.ts`, `next.config.mjs`, any `docs/**`, register, receipts, or Root surface.

## 5. Residual risks, follow-ups, and needs reported to the parent (not taken silently)

1. **G-CSP scope need (HELP_HUMAN decision).** Window-open denial (`setWindowOpenHandler`), a navigation constraint (`will-navigate`/`will-redirect`), and a renderer CSP are **absent from source**, not merely untested. The item's Return names them; this brief's locus (`main.ts` plumbing only) does not permit adding them. Recommended follow-on within DEL-09-06-V3-01's own write locus (`frontend/electron/**` window/CSP policy): a small `frontend/electron/renderer-window-policy.ts` (deny window-open, restrict navigation to `rendererOrigin`, one `hardenRendererWindow(window, origin)` call from `createMainWindow`) plus a CSP at the Next response layer, each with unit tests. Whether DEL-09-06-V3-01 closes on this tranche's evidence (sender checks + contextIsolation/sandbox/egress pins) or stays open until those land is the owner's/HELP_HUMAN's call; `STEP0_DISCOVERY.md` §5 and the DEL-09-06 `EVIDENCE.md` §5 carry the honest inventory.
2. **Premerge** is PR-CI-owed (recorded class). The root workflow runs it with the stub provider.
3. **Packaged proof identity vs. commit.** The bundle was built from the pre-commit working tree; `sourceRevision` reports HEAD `0c683fb16`, and the artifact hashes identify the proved bytes. A post-merge `artifact-proof`-labelled run of `.github/workflows/desktop-release-template.yml` would bind a proof to the merged SHA; I did not need `HOST_RERUN_REQUIRED` because the proof ran in-sandbox.
4. **Compatibility mapping.** A daemon that predates the typed state yields `available`/`missing` by mapping; the renderer cannot tell mapped from reported. Both processes ship in one bundle, so this only affects a dev GUI against an older packaged daemon; documented in code and tests.
5. **`instruction-root:integrity` "source completeness status: needs_remediation"** is pre-existing (root commit `3d522842e`), status `pass`; not introduced here.
6. **A1 re-stage rule** applies: the staged R20 procedure is invalidated for future proof claims by this `frontend/` mutation; a newly staged revision and a fresh owner-executed proof are owner acts (declaration in `STEP0_DISCOVERY.md` §3).
7. Concurrent nodes: no shared write path with this tranche except the append-only receipts ledger at closeout (Receipt 206, parent Receipt-205).

## 6. Coordination notices

None owed beyond this return: no `agents/**`, corpus, register, or Root surface changed.
