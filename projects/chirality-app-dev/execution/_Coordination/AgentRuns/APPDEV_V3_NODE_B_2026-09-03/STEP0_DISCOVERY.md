# STEP 0 DISCOVERY — APPDEV_V3_NODE_B_2026-09-03

Recorded before any write outside this run-record directory (2026-09-03, local host, worktree
`{SCRATCH}/wt-nodeB` on branch `codex/app-v3-nodeB-wp09-prep-2026-09-03`).

## Basis and git state

| Item | Observed |
|---|---|
| Basis commit | `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge, 2026-09-03T14:27:26-06:00) = `origin/main` at fetch; required basis `0c683fb16` satisfied (identical) |
| Branch | `codex/app-v3-nodeB-wp09-prep-2026-09-03`, cut from `origin/main` in a fresh scratch worktree; the dispatching worktree was not touched |
| `git status --short` before writes | clean (only this run-record directory untracked afterwards) |
| Standing plan (committed-HEAD selector) | `projects/chirality-app-dev/loop/WORKPLAN_2026-09-03_app_dev_loop.md` (bytewise-last `WORKPLAN_*`; read via `git show HEAD:`) |
| Newest applicable receipt | `Receipt-205` (Examined-Through `8140daec7ab7165f8972451dbdd3a67b8bb2fd38`, Parent `Receipt-203`); Receipt 206 is not present in the ledger at this basis; the brief reserves Receipt 207 for this tranche |

## Deterministic preflight results

| Check | Command (cwd) | Result |
|---|---|---|
| Receipts validator | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` (REPO_ROOT) | `VALID … frozen through Receipt-52; versioned receipt contract satisfied` |
| D-APP-38 corpus | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` (WORKING_ROOT) | `no drift.` (all rows MATCH; corpus v20) |
| APP-HOLD-1 dispatch preflight | `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-09-05` (WORKING_ROOT) | `"verdict": "ALLOW"`, `scan_held_deliverables: []`, fingerprint `c8cc4556356b227fba10d79f110d9efdcc26f408889a10824fe9736e97449747` |
| APP-HOLD-1 scan | `python3 execution/_Scripts/app_hold.py scan --require-register-match` (WORKING_ROOT) | `"verdict": "PASS"` |
| Harness self-check | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` (REPO_ROOT) | exit 0 |
| Pinned completion reference | SHA-256 of `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` recomputed | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` — equals the workplan pin |
| Decision register | `execution/_Coordination/_DECISIONS/_REGISTER.md` rows newer than Receipt 205 | none observed; D-APP-97 (C1) and D-APP-98 (`43.2.0`) remain the governing release-preparation rows |
| Routed Root notices | `execution/_Coordination/NOTICE_*` | no new App-consumable acceptance affecting DEL-09-05 V3-01/02/03 |
| `npm ci` (FRONTEND) | `npm ci` with warm `~/.npm` cache | exit 0 (allow-scripts warnings only; no script approval granted) |
| `npm ci && npm run build` (runtime workspace) | required so `tsc -p tsconfig.electron.json` can resolve `@chirality/*` `dist/` types; scratch worktree only, gitignored outputs | exit 0 |
| Baseline `npm run typecheck` (FRONTEND) | before any edit | exit 0 |
| Baseline `npm test` (FRONTEND) | before any edit | 155 files passed, 1 skipped; 1282 tests passed, 4 skipped; exit 0 |

## Host facts relevant to the evidence contract

- macOS 26.6.2, Xcode 26.6; `codesign`, `spctl`, `stapler`, `xcrun`, `hdiutil` present (used only as documented command names in the runbook; none executed against any artifact here).
- Node `v24.18.0`, npm `11.16.0`, Python `3.13.14`, git `2.55.0`.
- `syft`: **not installed on this host** (`which syft` → not found). Per the brief, no tool download or network act is in this grant; the SBOM evidence therefore records `UNAVAILABLE_UNDER_BOUNDS` with the exact command.
- No signing identity, Apple credential, or notarization tool was invoked; `CSC_IDENTITY_AUTO_DISCOVERY=false` remains the packaging posture.

## Selected items (owner-directed dev-slate selection; SELECTABLE at basis)

`DEL-09-05-V3-01`, `DEL-09-05-V3-02`, `DEL-09-05-V3-03` in
`execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow/_STATUS.md`
`## Remaining` — each carries no `(gated: …)` suffix and no `NOT_SELECTABLE_UNTIL:` state at basis; V3-04/05/06 stay parked and are not touched.

## Input identity inventory (SHA-256 at basis)

| Path | SHA-256 |
|---|---|
| `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` | `f9b02806eeab1a578e6729c41fc367074758a2b95cc0eda9c8d2edbda446f314` |
| `projects/chirality-app-dev/frontend/package.json` | `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc` |
| `projects/chirality-app-dev/frontend/package-lock.json` | `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458` |
| `projects/chirality-app-dev/frontend/THIRD_PARTY_NOTICES_PI.md` | `0195b5ce8b7be8b6bff6de3e50f6a38b3d9d4919c075e7c93ca8118b7e866328` |
| `.github/workflows/desktop-release-template.yml` (read-only context) | `3642152e730e3b6c59d48d860cbf1fd49a5c999d25d505deba4112dde62db2dc` |
| `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (meaning only) | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` |

## A1 re-stage declaration (applies: this tranche writes under `frontend/scripts/**`, `frontend/package.json`, `frontend/src/__tests__/scripts/**`)

Quoted verbatim from `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` lines 28–36:

```
  Recorded form: G0.25 is PASSED and WP-00 is closed. The standing
  frontend-freeze guard from G0 C2 is replaced by the recorded re-stage rule:
  any mutation under `projects/chirality-app-dev/frontend/` invalidates the
  staged procedure for any future proof claim and requires a newly staged
  revision and a fresh owner-executed proof. This ruling makes no signing,
  notarization, DMG, deployment, distribution, publication,
  release-readiness, or acceptance claim beyond the login-session proof
  itself; DEL-09-04's remaining scope stays `IN_PROGRESS` and separately
  gated.
```

Declaration: the frontend mutations made by this tranche invalidate the staged R20 procedure for any
future proof claim; a newly staged revision and a fresh owner-executed proof are required before any
such claim. This tranche makes no proof claim.

## Live-tree deltas against the brief (live tree wins)

- The brief's suggested read `git show HEAD:projects/chirality-app-dev/loop/WORKPLAN_2026-09-03_app_dev_loop.md` resolves as stated; no delta.
- The brief anticipates that the app "reports its version" somewhere in `electron/main.ts`. Live tree: no `app.getVersion()`, about-dialog, or UI version string exists in `electron/**` or `src/**`; the only `version` fields in runtime reports are engine/SDK `packageVersion` values, not the product identity. The version-identity check therefore records those surfaces as `ABSENT` (a finding for V3-06/AT-043, not fixed here because `electron/**` and product `src/**` are outside the write locus).
- No existing script writes a "release manifest" carrying the product version; the CI workflow's `summary.json` carries digests and posture only. Recorded as an `ABSENT` surface in the same report.
- `syft` is absent on the host (see above).

## Fences carried

F-APP-2 and D-APP-97 active through preparation; no signing identity, Apple service call, notarization,
distribution, product version change, `.github/workflows/**` change (SCOPE_AMENDMENT S-6), or
release-readiness claim; WP-11 never touched; `docs/**`, `electron/**`, product `src/**`,
dependencies, lockfile, version field, other deliverables, and Root surfaces are not written.
