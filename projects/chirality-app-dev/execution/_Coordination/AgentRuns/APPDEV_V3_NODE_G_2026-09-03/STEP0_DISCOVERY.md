# Step 0 — Discovery (recorded before any product edit)

Run: `APPDEV_V3_NODE_G_2026-09-03` · Implementer: Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · Date: 2026-09-03

## 1. Git state, basis, validators

| Check | Command (cwd) | Result |
|---|---|---|
| Worktree creation | `git -C /Users/ryan/dev/chirality fetch origin && git -C /Users/ryan/dev/chirality worktree add <scratch>/wt-nodeG -b codex/app-v3-nodeG-egress-probe-restriction-2026-09-03 origin/main` | branch created; HEAD `e59efa4830fb54143c86e511ec35a6d1a476f72e` = PR #686 merge (node A closeout) |
| Basis | `git merge-base --is-ancestor e59efa4830fb54143c86e511ec35a6d1a476f72e HEAD` (REPO_ROOT) | true — basis is exactly `e59efa483`, as the brief requires |
| Git status | `git status --porcelain` (REPO_ROOT) | empty (clean) |
| Receipts validator | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` (REPO_ROOT) | `VALID … frozen through Receipt-52; versioned receipt contract satisfied`, exit 0 |
| Authority corpus (D-APP-38) | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` (WORKING_ROOT) | `corpus current_version: v20`, all eight `[MATCH]`, `no drift.`, exit 0 |
| Pinned completion reference | `shasum -a 256 plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (REPO_ROOT) | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` — matches the workplan pin |
| Newest receipt | `loop/LOOP_RECEIPTS.md` | Receipt 212 (node A; `Examined-Through 0c683fb16…`, Parent Receipt-205, Gate-Outcome `EXECUTED`); its PR #686 merged at `e59efa483` (this basis) and seeded DEL-09-06-V3-05 as `SELECTABLE` |
| Decision register | `execution/_Coordination/_DECISIONS/_REGISTER.md` | no ruling newer than Receipt 212 affects DEL-09-06-V3-05; the item carries no gate |
| Routed Root notices | `ls execution/_Coordination/NOTICE_*` | 41 notices, newest `NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`; none bears on this item (it has no `NOT_SELECTABLE_UNTIL` state) |
| Remote sibling branches | `git branch -r \| grep -i node` (REPO_ROOT) | none pushed yet at Step 0; a local sibling worktree `wt-nodeF` (`codex/app-v3-nodeF-consent-ux-fixtures-2026-09-03`) exists in the parent's scratch area — not touched |
| Toolchain | `node --version` / `npm --version` / `npx vitest --version` (FRONTEND) | v24.18.0 / 11.16.0 / 4.1.10 |
| Dependencies | `npm ci && npm run build` (REPO_ROOT/runtime), then `npm ci` (FRONTEND) | fresh worktree had no `node_modules`; runtime `tsc -b` built the `file:`-linked `@chirality/runtime-*` packages; frontend install completed; only `allow-scripts` warnings; no lockfile edit |
| Baseline focused Vitest (basis bytes) | `npx vitest run src/__tests__/electron/renderer-window-policy.test.ts src/__tests__/scripts/run-packaged-security-proof.test.ts src/__tests__/contract-pins.test.ts` (FRONTEND) | 3 files, 87 tests passed (renderer-window-policy 62; contract-pins 16; run-packaged-security-proof 9) |

## 2. APP-HOLD-1 dispatch preflight

Command (WORKING_ROOT):
`python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-09-06`

Result: `"verdict": "ALLOW"`; `DEL-09-06` `contract_status: CLEAR`, `hold_status: NOT_HELD`, `verdict: ALLOW`; `active_hold_deliverables: []`; `scan_held_deliverables: []`; `register_sha256 e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; `scan_fingerprint_sha256 a9bfb75515b8c4ced2707b38b5b31e1f9b6c272f5262ceea3064f7196bd75b9b`; `repo_head e59efa4830fb54143c86e511ec35a6d1a476f72e`; exit 0.

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

Declaration: this tranche mutates files under `projects/chirality-app-dev/frontend/` (`electron/renderer-window-policy.ts`, `scripts/run-packaged-security-proof.mjs`, and tests/pins under `src/__tests__/**`). Under the A1 re-stage rule this frontend mutation **invalidates the staged R20 procedure for any future proof claim** and **requires a newly staged revision and a fresh owner-executed proof** before any such claim is made. The R20 PASS of 2026-08-23 is unaffected as historical evidence of the bytes it was executed against; it is not carried forward as a claim about the post-tranche bytes.

## 4. The seated item (exact text from DEL-09-06 `_STATUS.md` `## Remaining` at basis `e59efa483`)

> - **DEL-09-06-V3-05** (`SELECTABLE`) — restrict the packaged-proof egress-layer probe URL to destinations the REQ-NET-001 egress policy denies, or hard-code the `:8443` probe and drop `CHIRALITY_EGRESS_LAYER_PROBE_URL` (residual R-B of DEL-09-06-V3-01; review 2 NOTE-2, coordinator decision D4).
>   Trace: OUT-001, AC-001, VER-001; DEL-09-06-REQ-005/014/015. Origin: `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03/RETURN.md` §5 R-B.
>   Plan: WP-09; G-CSP evidence hygiene. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
>   Depends: DEL-09-06-V3-01 (landed). No owner gate: the hook is env-gated, adds no destination to REQ-NET-001, and carries no credential; this item only removes the possibility of one unauthenticated main-process GET to an already-allowlisted URL under a deliberately set launch environment.
>   Write locus: `frontend/electron/renderer-window-policy.ts` (`runEgressLayerProbe`), `frontend/scripts/run-packaged-security-proof.mjs`, tests under `frontend/src/__tests__/**`, `Evidence/**`, and deliverable-local state.
>   Checks: registered frontend gates, packaged security proof, APP-HOLD-1 dispatch preflight, `git diff --check`, harness self-check and pytest, and the independent-review path; Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
>   Return: unit tests proving the probe refuses (or cannot be pointed at) any URL the egress policy would allow, and a packaged proof run still observing `egressLayerDiagnostics > 0`; durable non-secret bytes per the Evidence contract.
>   Removed when: the restriction lands with review PASS.

Selectability re-derived from the live tree: the item carries no `(gated: …)` suffix and no `NOT_SELECTABLE_UNTIL:` state; its only dependency (DEL-09-06-V3-01) is recorded as landed in the same `_STATUS.md` History (2026-09-03) and on `main` at basis; the accepted DepClosure snapshot is not affected (no dependency row changes).

## 5. Write locus (sealed by the brief; re-derived against the seated item)

- `frontend/electron/renderer-window-policy.ts` (`runEgressLayerProbe`)
- `frontend/electron/main.ts` — only if wiring must change (finding below: it does not)
- `frontend/scripts/run-packaged-security-proof.mjs`
- tests under `frontend/src/__tests__/**` (including `contract-pins.manifest.ts` — the brief names `frontend/src/lib/contract-pins/**`; the live tree has no such directory, the pin manifest lives at `frontend/src/__tests__/contract-pins.manifest.ts` and is inside the tests locus — live tree wins, delta recorded here)
- DEL-09-06 `Evidence/Node_G_Egress_Probe_Restriction_2026-09-03/**` and `_run_records/**`
- this run record; `_STATUS.md`, `MEMORY.md`, and `loop/LOOP_RECEIPTS.md` only at closeout after `REVIEW_PASS`

## 6. The concern, confirmed in the live tree (not from the brief)

- `frontend/electron/renderer-window-policy.ts:453-494` `runEgressLayerProbe(window, { env })`: `const url = options.env.CHIRALITY_EGRESS_LAYER_PROBE_URL?.trim();` gated on `CHIRALITY_RENDERER_SECURITY_PROBE !== '1' || !url`; issues `window.webContents.session.fetch(url, { method: 'GET', cache: 'no-store', signal: AbortSignal.timeout(3000) })` and logs `[egress-layer-probe]` with `summarizeDestination(url)` (protocol + hostname). Nothing constrains `url` to a policy-denied destination: a launch environment setting both variables with an allowlisted URL (`https://api.anthropic.com/…`, or a loopback URL) would pass `main.ts:277-297` `onBeforeRequest` (`evaluateRendererEgressPolicy` allows `https:` `api.anthropic.com` with empty or `443` port, and loopback hosts) and produce one unauthenticated main-process GET.
- `frontend/electron/main.ts:550` wires `runEgressLayerProbe(window, { env: process.env })` — the signature keeps `env` for the gate and delay variables, so no wiring change is needed.
- `frontend/scripts/run-packaged-security-proof.mjs:56` `EGRESS_PROBE_URL = 'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked'` is passed as `CHIRALITY_EGRESS_LAYER_PROBE_URL` in `proofEnv` (`:597`); the summarizer (`:350`, `:358-364`) counts `anthropic_port_not_allowlisted:8443` diagnostics and requires an `[egress-layer-probe]` payload with `hostname === 'api.anthropic.com'` and `outcome === 'rejected'`.
- Is the env var needed for the proof script's own operation across environments? No: the script sets it to a constant; `.github/workflows/desktop-release-template.yml:154-157` invokes `npm run proof:packaged-security` with only `--app-path`, `--output-root`, `--source-revision`; `scripts/run-network-policy-proof.mjs` does not use it; `docs/**` does not mention it (grep over `projects/chirality-app-dev/docs`: 0 hits). Only the node A evidence and run record mention it historically. So the brief's preferred option (hard-code, drop the env var) is available — decision D1 in `COORDINATOR_DECISIONS.md`.
- Pins touched by a hard-coded destination: `src/__tests__/contract-pins.manifest.ts:261` (`electron/renderer-window-policy.ts` must contain `CHIRALITY_EGRESS_LAYER_PROBE_URL`) and `:338` (`scripts/run-packaged-security-proof.mjs` must contain `CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_PROBE_URL`) — both must be replaced deliberately (recorded in `RETURN.md`).
