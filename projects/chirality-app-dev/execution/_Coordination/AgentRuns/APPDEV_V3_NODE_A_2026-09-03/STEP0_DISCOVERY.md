# Step 0 — Discovery (recorded before any product edit)

Run: `APPDEV_V3_NODE_A_2026-09-03` · Implementer: Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · Date: 2026-09-03

## 1. Git state, basis, validators

| Check | Command (cwd) | Result |
|---|---|---|
| Worktree creation | `git worktree add <scratch>/wt-nodeA -b codex/app-v3-nodeA-credential-ipc-2026-09-03 origin/main` (parent worktree) | branch created; HEAD `0c683fb1657706316272951e4c3a0f7781b46009` = PR #681 merge |
| Basis | `git merge-base --is-ancestor 0c683fb16 HEAD` (REPO_ROOT) | true — basis is exactly `0c683fb16` |
| Git status | `git status --porcelain` (REPO_ROOT) | empty (clean) |
| Receipts validator | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` (REPO_ROOT) | `VALID … frozen through Receipt-52; versioned receipt contract satisfied`, exit 0 |
| Authority corpus (D-APP-38) | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` (WORKING_ROOT) | `corpus current_version: v20`, all eight `[MATCH]`, `no drift.`, exit 0 |
| Pinned completion reference | `shasum -a 256 plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (REPO_ROOT) | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` — matches the workplan pin |
| Newest receipt | `loop/LOOP_RECEIPTS.md` | Receipt 205 (`Examined-Through 8140daec7…`, Parent Receipt-203, Gate-Outcome `AWAITING_OWNER`); PR #681 has since merged at `0c683fb16`, which confers selectability |
| Routed Root notices | `ls execution/_Coordination/NOTICE_*` | D-GOV-28, D-GOV-31, D-GOV-32, D-GOV-35, D-T0-24 — none resolves a `NOT_SELECTABLE_UNTIL` state relevant to this node; the three selected items carry no gate |
| Toolchain | `node --version` / `npm --version` (FRONTEND) | v24.18.0 / 11.16.0 |
| Dependencies | `npm ci` (FRONTEND) | completed in ~8.5 s from the warm cache; only `npm audit` and `allow-scripts` warnings; no lockfile edit |

## 2. APP-HOLD-1 dispatch preflight

Command (WORKING_ROOT):
`python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-09-06 --target DEL-04-05 --target DEL-02-05`

Result: `"verdict": "ALLOW"`; per-target `DEL-02-05`, `DEL-04-05`, `DEL-09-06` each `contract_status: CLEAR`, `hold_status: NOT_HELD`, `verdict: ALLOW`; `active_hold_deliverables: []`; `register_sha256 e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; `scan_fingerprint_sha256 c8cc4556356b227fba10d79f110d9efdcc26f408889a10824fe9736e97449747`; `repo_head 0c683fb1657706316272951e4c3a0f7781b46009`; exit 0.

## 3. A1 re-stage declaration (mandatory — this tranche mutates `frontend/`)

Quoted verbatim from `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` lines 28–36:

> ```
>   Recorded form: G0.25 is PASSED and WP-00 is closed. The standing
>   frontend-freeze guard from G0 C2 is replaced by the recorded re-stage rule:
>   any mutation under `projects/chirality-app-dev/frontend/` invalidates the
>   staged procedure for any future proof claim and requires a newly staged
>   revision and a fresh owner-executed proof. This ruling makes no signing,
>   notarization, DMG, deployment, distribution, publication,
>   release-readiness, or acceptance claim beyond the login-session proof
>   itself; DEL-09-04's remaining scope stays `IN_PROGRESS` and separately
>   gated.
> ```

Declaration: this tranche mutates files under `projects/chirality-app-dev/frontend/` (`electron/api-key-ipc.ts`, `electron/api-key-storage.ts`, a new `electron/ipc-sender-policy.ts`, `electron/runtime-control-ipc.ts`, `electron/main.ts`, `src/components/settings/api-key-settings.tsx`, a new `src/lib/credential-storage-state.ts`, and tests under `src/__tests__/**`). Under the A1 re-stage rule this frontend mutation **invalidates the staged R20 procedure for any future proof claim** and **requires a newly staged revision and a fresh owner-executed proof** before any such claim is made. The R20 PASS of 2026-08-23 is unaffected as historical evidence of the bytes it was executed against; it is not carried forward as a claim about the post-tranche bytes.

## 4. Selectability and dependency re-derivation (live tree, not the brief)

- `DEL-09-06-V3-01`, `DEL-04-05-V3-01`, `DEL-02-05-V3-01` are each marked `SELECTABLE` in their `_STATUS.md` `## Remaining` on `main` at basis, with no `(gated: …)` suffix and no `NOT_SELECTABLE_UNTIL:` state.
- `DEL-04-05-V3-01 Depends:` names the shared `frontend/electron/api-key-ipc.ts` write surface with DEL-09-06-V3-01 ("serialized or executed under one integration owner"); `DEL-02-05-V3-01 Depends:` names DEL-04-05-V3-01 as dependency-linked ("execute after it lands or in the same tranche under one integration owner") and states that `api-key-ipc.ts` is not written by DEL-02-05. This run is that single integration owner; the DEL-02-05 product write is confined to `frontend/src/**`.
- Live-tree confirmation of the brief's citations: `runtime-control-ipc.ts:85-95` is `isAuthorizedSender(event, rendererOrigin)` (origin equality on `event.senderFrame.url`, fail-closed on absent/unparseable URL); `api-key-ipc.ts:110-177` registers exactly six `ipcMain.handle` channels; `main.ts:590` registers the credential handlers before `rendererUrl` is known (line 652–654) while `main.ts:656-667` passes `rendererOrigin: new URL(rendererUrl).origin` to the runtime-control handlers — so plumbing requires moving the credential registration after `rendererUrl` is resolved (the window is created only at line 669, so no ordering hazard).
- Daemon credential path (read-only inspection; no `runtime/**` write): `runtime/packages/daemon/src/runtime-daemon.ts:275-279` returns `{ providerId, ...(await service.credentials.status(providerId)) }` — the store's status object is spread verbatim, so an additive non-secret `storage` field on `SafeStorageCredentialStore.status()` reaches `RuntimeClient.credentialStatus()` and the Electron IPC layer without any daemon change; `runtime/packages/core/src/runtime-service.ts:31` `RuntimeCredentialStore extends ProviderCredentialPort` accepts a wider return type.

## 5. G-CSP renderer-hardening inventory (unit-level test coverage in the repo at basis)

| Surface | Policy present in source? | Existing test evidence (file:line) | Gap at unit level |
|---|---|---|---|
| Explicit `contextIsolation` / `sandbox` / `nodeIntegration: false` | Yes — `frontend/electron/main.ts:512-517` (`contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`, preload path) | None: `src/__tests__/contract-pins.manifest.ts:188-209` pins `electron/main.ts` for egress/auto-update only; no pin names the webPreferences | Add contract pins for the three webPreferences and the preload wiring (testable via the existing pin mechanism) |
| Per-window bounded egress policy | Yes — `main.ts:68-70` allowlists, `main.ts:225-267` `evaluateRendererEgressPolicy`, `main.ts:269-292` `registerRendererEgressPolicy` installed per window at `main.ts:524` | `src/__tests__/contract-pins.manifest.ts:188-209` (allowlist constants, `session.webRequest.onBeforeRequest`, `REQ-NET-001`, redacted diagnostics, no `url: details.url`); packaged proof `scripts/run-packaged-security-proof.mjs:40,324,344,552` with its unit test `src/__tests__/scripts/run-packaged-security-proof.test.ts:61,81` | Covered at unit (pin) and packaged levels; add a pin that the policy is registered per window (`registerRendererEgressPolicy(window)`) |
| Window-open denial (`setWindowOpenHandler`) | **No policy in source** (`grep setWindowOpenHandler frontend/electron` → none) | None | Not testable at unit level without adding a product policy; adding one is outside this brief's write locus (`main.ts` plumbing only) — recorded as a scope need for HELP_HUMAN (see RETURN.md) |
| Navigation constraint (`will-navigate` / `will-redirect` to renderer origin) | **No policy in source** (`grep will-navigate frontend/electron` → none) | None | Same as above — scope need |
| CSP effectiveness (Content-Security-Policy header/meta on the renderer document) | **No CSP in source** (`grep Content-Security-Policy frontend/{electron,src,scripts,next.config.mjs}` → none) | None | Same as above — scope need; a CSP belongs at the Next response headers (`next.config.mjs`) or an `onHeadersReceived` hook, both outside this brief's locus |

Conclusion for this node: the sender-authorization portion of G-CSP is implemented and unit-tested here; contextIsolation/sandbox and per-window egress receive unit-level pins; window-open denial, navigation constraint, and CSP are reported honestly as absent policies that need a write-locus extension before they can be implemented and tested. No existing policy is weakened.
