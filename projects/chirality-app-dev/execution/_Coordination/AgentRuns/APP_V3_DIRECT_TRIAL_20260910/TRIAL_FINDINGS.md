# Direct trial testing — 2026-09-10

Agent 0 is testing the installed signed trial through Computer Use at the human’s request. This is functional testing, not release acceptance. The twelve-item checklist remains in the preserved aed8 continuity directory.

## First-run sign-in: blocked

Installed App: `/Users/ryan/Applications/Chirality Trial 20260910.app`, launched through its dedicated `.command`; isolated user data: `/Users/ryan/Library/Application Support/Chirality Trial 20260910`.
Synthetic workspace: `/Users/ryan/Chirality Trial Workspace 20260910`, containing a workshop brief only.

Observed sequence:
1. Fresh GUI has Runtime offline, unavailable role, no account sign-in before folder selection.
2. Select synthetic folder. Account menu offers “Use this folder”; clicking fails with missing `runtime/auth/tokens/hosted-bootstrap-host.token`.
3. Settings has no Runtime installation/start control. Clicking bottom Runtime only probes; Details opens Activity.
4. Source corroboration: hosted settings suppresses the section containing both local-model controls and shared Runtime lifecycle controls. Type 2 `trial_startup_repair` owns minimal UI repair.
5. Temporary diagnostic workaround: dedicated trial launcher `--check-only` PASS; installed protected `~/.local/bin/chirality daemon install` and `daemon start` each exit 0. No installed App bytes modified. Daemon log confirms startup at 2026-09-11T00:23:30Z.
6. “Use this folder” now succeeds and Help Human becomes selectable. “Allow provider network” fails with “Hosted account service is unavailable.” GUI log repeatedly reports `Unknown project: chirality-app-dev`; account-host connection depends on this fixed development-project binding. Type 2 `trial_account_binding` owns diagnosis/repair.

Both workers use gpt-5.6-sol medium, bounded directly from parent testing. Independent source review and updated packaged retest remain required. No OAuth authorization, model request, or completed checklist item yet. Remaining eleven checklist items are not tested, not passed. Existing package/signature/security evidence is preserved and does not establish first-run functional success.

## Independent local UI checks while sign-in is blocked

The Files panel renders the synthetic `brief.md` accurately in the Markdown preview. The attachment picker selects that file and displays its removable composer reference. A draft request was entered, not sent. These partial observations do not pass checklist item 3: model receipt, response references, and PDF fallback remain untested.

## Repair review

The first hosted-settings patch restored shared Runtime controls but independent review correctly required the same prerequisite to be discoverable in the compact account menu. Author is refining that path and adding an action-level regression.

Account binding repair passed a separate gpt-6-astra high review under the standing limited exception: authenticated daemon reachability controls account-host availability independently of the optional development project; absence of that project is a valid fresh installation; existing manifest/private-token/scoped-auth checks remain if it exists. Behavioral repeated-healthy-sample coverage is retained. A newly added source-substring assertion is being removed because it mirrors wiring text and was brittle even during this repair. Signed GUI first-run and restart testing remain pending.

Both source repairs are now independently reviewed PASS. Hosted account popover offers Runtime setup before project setup; actual install callback regression passes. Account change final scope is three files after removing brittle source assertions.

First rebuild attempt: `npm run build` with Node 24.18 PATH, inherited environment (NODE_ENV unset). Compiled successfully, but Next prerender failed at `/500` with null `useContext` and `/workbench` with workUnitAsyncStorage invariant. Log: `/private/tmp/chirality-direct-trial-repair-build.log`. Exit 1 before packaging. Dependency/build environment investigation is active; no package produced from these new sources yet.

## Rebuild environment diagnosis and recovery

Bounded Type 2 diagnosis ran with gpt-6-astra high under the standing repeated-failure exception. APP-HOLD-1 dispatch preflight for `HELP_HUMAN:TRIAL:REPAIR`, DEL-09-04, returned ALLOW/CLEAR/NOT_HELD at HEAD `3a4c9c2ef3bd82fe571a32407125d0398d1d99b4`.

Root cause was the local dependency setup: `frontend/node_modules/.bin` is a symlink to `/private/tmp/chirality-v3-adoption-20260909/projects/chirality-app-dev/frontend/node_modules/.bin`. Consequently `npm run build` launched the foreign Next CLI even though ordinary `require.resolve('next')` resolved to the selected checkout. That CLI resolves its renderer, React, and work-unit async storage in the foreign tree, while generated server bundles resolve current-checkout modules. The two identities explain the framework-owned Head `useContext` failure and missing request storage. The environment-normalized second npm attempt reproduced the failure at `/404`.

Invoking the current checkout's CLI directly proved the diagnosis. From the selected checkout's `projects/chirality-app-dev/frontend`, both commands exited 0:

```sh
HOME=/Users/ryan TMPDIR=/private/tmp NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 /Users/ryan/.local/share/mise/installs/node/24/bin/node ./node_modules/next/dist/bin/next build
HOME=/Users/ryan TMPDIR=/private/tmp NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 /Users/ryan/.local/share/mise/installs/node/24/bin/node ./scripts/build-electron.mjs
```

Next completed all 35 prerenders and correctly classified `/workbench` and the other operator routes as dynamic. Electron main/preload and runtime CLI bundles completed. Existing nonfatal package-version import warnings remain. No product source, runtime source, lockfile, or dependency links were changed by this diagnosis. Failed `.next` trees are preserved as `failed-next-build-01` and `failed-next-build-02` under `/private/tmp/chirality-local-human-trial-20260910-09`; successful logs are `build-03-canonical-entrypoint.log` and `build-03-electron.log` in that directory. `prerender-diagnosis.json` records resolved entrypoints and log hashes. Current `.next`, `dist-electron`, and `dist-runtime` are the successful candidate outputs.

Packaging tools `electron-builder` and `esbuild` still resolve through admitted development dependency symlinks. Parent will verify packaging resolution/version against the earlier successful trial and consume the new output through the existing wrapper's explicit checkout cwd/config. This recovery establishes build success only; packaging and the signed GUI checklist remain parent work.

Packaging of reviewed repaired source started in `/private/tmp/chirality-local-human-trial-20260910-09` using the prior successful wrapper argv/environment with new output/checkpoint paths. Supplier, native addon and lock inputs compare unchanged. Current signer changes were already committed/reviewed before this trial repair. Packaging is running; no PASS asserted yet.

Attempted draft restart via Computer Use: original idle GUI was quit and the dedicated launcher opened through Finder. Computer Use then timed out selecting the reopened App; process/log inspection shows GUI processes and Runtime active. Draft persistence is therefore still unverified; tool access uncertainty is not yet attributed to an App defect.

## Restart finding confirmed

After reselecting the same synthetic folder in the reopened App, both unsent draft and attachment are absent. Actual origin changed 58737 to 59669. Both GUI startup records name the same trial userData directory. Source diagnosis confirms packaged renderer binds port 0 every launch while folder/drafts persist in origin-scoped localStorage. Runtime project registration is separate and remains preserved; no claim of transcript loss.

Type 2 `trial_restart_persistence` is implementing a bounded stable loopback port per userData: preserve HTTP/CSP/exact-origin IPC, reject invalid/occupied persisted port instead of silently changing origin, and test actual bind/reuse/failure behavior. Stage09 package completed exit0 at nested-signed phase but its final measurement/provisioning is held; it lacks this newly found repair. Stage09 is preserved. No additional checklist items passed.

## Reviewed source checkpoint

All three source repairs passed separate independent review: hosted Runtime setup (`trial_startup_review`, Sol medium), account-host/default-project binding (`trial_account_review`, Astra high), stable renderer origin (`trial_restart_review`, Sol medium). Relevant typechecks and focused behavioral tests passed. Review did not assert native OAuth success. Optional low-impact port-record hardening was recorded without expanding the release blocker set.

Stage10 reuses the successful unchanged Next output and rebuilds Electron for the stable-port addition. Its wrapper completed exit0 and reached `nested-signed`; final measurement, sealing/provisioning, and direct GUI acceptance remain pending. Stage08 installed trial and stage09 intermediate are preserved. Source is checkpointed separately from final trial acceptance.

Reviewed source checkpoint commit: `83b16175c`. Stage10 support measurement completed exit0; profile digest `ffd2a6f390a2672688eb96a631b3f08ab95c4f5cc4d81eac9eced9cd2ad6113a`. Actual stdout and invocation are under stage10. This records the new binary/profile basis, not OAuth or checklist success. Account-free observer recipe preparation is next.

## Repaired trial provisioned and logo scope corrected

Stage10 completed its eight account-free observer checks, payload binding, governance preparation, sealing, separate durable copy, three final observation checks, and provisioning (all exit 0). The repaired App is `/Users/ryan/Applications/Chirality Trial 20260910 Repaired.app`; its guarded launcher is `/Users/ryan/Applications/Launch Chirality Trial 20260910 Repaired.command`. Provisioned anchor SHA is `af13af8adf900865384a311d2e62b68224cc5a6b07bf027a7e785b4cdaa333d1`; observation SHA is `e8cae9845546348dedd76c4e742b657f7c508e8d0da18bee3f8c380736bdea1c`. Owner-private state and exact three-line launcher derivation were checked. Original trial bundle/data are preserved; its idle daemon registration was removed after preserving the plist. No OAuth or full checklist item is yet established by these checks.

User directed website-based artwork, then clarified: no logo in the UI. Type 2 author `trial_website_logo` and separate reviewer `trial_logo_review` both used gpt-5.6-sol medium. The final six-file source change removes the shell image and unused CSS, deletes the public image and web favicon SVG, and retains website artwork only in native macOS SVG/ICNS assets. Independent full-diff review PASS: no stale UI references, no layout issue, embedded source bytes exact, all ten ICNS representations valid. No cosmetic-whitespace gate or additional behavioral test was introduced for this simple removal. Stage10 remains sealed with its previous artwork; the next build must include this change.
