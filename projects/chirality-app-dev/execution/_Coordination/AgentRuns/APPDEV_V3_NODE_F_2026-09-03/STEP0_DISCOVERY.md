# Step 0 — Discovery (recorded before any product edit)

Run: `APPDEV_V3_NODE_F_2026-09-03` · Implementer: Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · Date: 2026-09-03

## 1. Git state, basis, validators

| Check | Command (cwd) | Result |
|---|---|---|
| Fetch + worktree creation | `git -C /Users/ryan/dev/chirality fetch origin && git -C /Users/ryan/dev/chirality worktree add <scratch>/wt-nodeF -b codex/app-v3-nodeF-consent-ux-fixtures-2026-09-03 origin/main` | branch created tracking `origin/main`; HEAD `e59efa4830fb54143c86e511ec35a6d1a476f72e` = PR #686 merge (node A) |
| Basis | `git rev-parse origin/main` = `git rev-parse HEAD` (REPO_ROOT) | `e59efa4830fb54143c86e511ec35a6d1a476f72e` — the required basis exactly |
| Git status | `git status --porcelain` (REPO_ROOT) | empty (clean) |
| Receipts validator | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` (REPO_ROOT) | `VALID … frozen through Receipt-52; versioned receipt contract satisfied`, exit 0 |
| Authority corpus (D-APP-38) | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` (WORKING_ROOT) | `corpus current_version: v20`; all eight `[MATCH]` (DIRECTIVE `50b816d5be74`, CONTRACT `51ec0d4872dd`, SPEC `c2fb9ecbbc37`, TYPES `a8cdc94d39e1`, PLAN `3741bb7ec389`, PRD `87ced649beae`, AGENT_SOFTWARE_DECOMP `ad849d9a9274`, AGENT_DOMAIN_ENGINE `bb2df7178d7b`); `no drift.`; exit 0 |
| Pinned completion reference | `shasum -a 256 plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (REPO_ROOT) | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` — matches the workplan pin |
| Standing plan (committed HEAD) | `git ls-tree HEAD projects/chirality-app-dev/loop/` bytewise-last `WORKPLAN_*.md` | `WORKPLAN_2026-09-03_app_dev_loop.md`, mode `100644` blob `5049fdbd…`; read via `git show HEAD:` |
| Newest receipt | `loop/LOOP_RECEIPTS.md` | Receipt 212 (node A; Parent Receipt-205; Gate-Outcome `EXECUTED — awaiting owner merge`); PR #686 has since merged at `e59efa483`, the basis |
| Routed Root notices | `ls execution/_Coordination/NOTICE_*` | newest `NOTICE_2026-09-03_APP_TM-ROOT-122_ELECTRON_AUTHORITY_DISPOSITION.md`; no notice routes an accepted Root DEL-02-09 account/consent contract, so DEL-02-05-V3-03 stays `NOT_SELECTABLE_UNTIL` and this node stays fake-backed |
| Toolchain | `node --version` / `npm --version` (FRONTEND) | v24.18.0 / 11.16.0 |
| Dependencies | `npm ci && npm run build` (runtime) then `npm ci` (FRONTEND) | required because `frontend/package.json` links seven `file:../../../runtime/packages/*` packages; outputs are gitignored (result in `CHECKS.json` `environment_preparation`) |

## 2. APP-HOLD-1 dispatch preflight

Command (WORKING_ROOT):
`python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-02-05`

Output (verbatim):

```json
{
  "active_hold_deliverables": [],
  "entry_path": "loop/LOOP_INIT.md",
  "operation": "dispatch",
  "register_sha256": "e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f",
  "repo_head": "e59efa4830fb54143c86e511ec35a6d1a476f72e",
  "results": [
    {
      "contract_status": "CLEAR",
      "deliverable_id": "DEL-02-05",
      "entry_path": "loop/LOOP_INIT.md",
      "hold_status": "NOT_HELD",
      "operation": "dispatch",
      "verdict": "ALLOW"
    }
  ],
  "scan_fingerprint_sha256": "a9bfb75515b8c4ced2707b38b5b31e1f9b6c272f5262ceea3064f7196bd75b9b",
  "scan_held_deliverables": [],
  "schema": "chirality-app-hold-check/v1",
  "targets": [
    "DEL-02-05"
  ],
  "verdict": "ALLOW"
}
```

Exit 0.

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

Declaration: this tranche mutates files under `projects/chirality-app-dev/frontend/` (new `src/lib/consent/**`, new `src/components/settings/account-consent-settings.tsx`, account/consent panel styles appended to `src/app/globals.css`, and tests under `src/__tests__/**`). Under the A1 re-stage rule this frontend mutation **invalidates the staged R20 procedure for any future proof claim** and **requires a newly staged revision and a fresh owner-executed proof** before any such claim is made. The R20 PASS of 2026-08-23 is unaffected as historical evidence of the bytes it was executed against; it is not carried forward as a claim about the post-tranche bytes.

## 4. Seated item (exact text on `main` at basis — `DEL-02-05/_STATUS.md` `## Remaining`)

```
- **DEL-02-05-V3-02** (`SELECTABLE`) — static WP-07 account/consent UX fixtures behind a fake consent port.
  Trace: OUT-002, REQ-001, REQ-003, REQ-004, REQ-005, AC-002, VER-002; CLM-028.
  Plan: WP-07 static fixtures permitted before runtime integration; fixture evidence toward AT-008/009/010/012/016/020/023/034 UI portions; no live-account success claim before G3/G-WIRE; `Opt-in Preview` label per G0 A8. Completion meaning from `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a`, completion reference only); status from current `main`.
  Depends: Fake adapter shaped by App `docs/CONTRACT.md` K-CONSENT-1 (`HostedEngineConsentPort`) and K-NET-1 posture vocabulary; DEP-02-05-008/009 name the Root-owned semantics and gates. Selectable before Root DEL-02-09 acceptance because the A12 owner selection names WP-07 fixtures as unlocked App-only work notwithstanding the `Carrier_Map.md` dispatch-matrix WP-04/WP-07 entry gate; fake-backed; no live claim. Live consumption is DEL-02-05-V3-03.
  Write locus: `frontend/src/**` account/consent UI, fixtures, copy, and tests plus deliverable-local state; no secret persistence, no ambient `~/.codex` read.
  Checks: registered frontend gates (typecheck, Vitest, `npm run validate:release-quality` build/premerge, D-APP-36 render bar for UI), APP-HOLD-1 dispatch preflight, `git diff --check`, repo-wide harness self-check and pytest, and the independent-review path (fresh read-only `TASK + software-code-review` PASS over 100% of the frozen diff before push); Step 0 must carry the A1 re-stage declaration because `frontend/` is touched.
  Return: Fixture and test bytes for per-root login explanation, root-private app-owned `CODEX_HOME` copy, login/logout/account and consent/revocation states, the three command-network postures (default off; ask per destination with host/protocol and queued-request caveat, `acceptForSession` only as an explicit user act; on with `network_access = true` labelled), rate-limit/approval status, `Opt-in Preview`, and role entry with the `role not mechanically enforced` label; durable non-secret bytes sufficient for independent recomputation per the successor workplan's Evidence contract: exact input/source identities and cited-byte inventory; fixture/evaluator/validator bytes; command, arguments, cwd, effective environment, tool/runtime versions, and exit status; canonical stdout/stderr and machine-readable results; sorted manifests with recomputable hashes; cleanup proof for disposable state; and a bounded rerun method.
  Removed when: the fixtures land with review PASS; live wiring moves to DEL-02-05-V3-03.
```

Selectability re-derived from the live tree: the item carries no `(gated: …)` suffix and no `NOT_SELECTABLE_UNTIL:` state; `_STATUS.md` Current State `IN_PROGRESS`, Checking Approval SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` (untouched by this node). The MAPPING.md WP-07 row (`APP_V3_PATHWAY_SEATING_2026-09-03/MAPPING.md` line 51) lists DEL-02-05-V3-02 as `SELECTABLE`, App-owned, live claims waiting for Root G3/G-WIRE; row S-7 (line 157) records that role entry and both posture labels were seated on DEL-02-05 (decomposition L297) and DEL-08-04 (L357) only, and that the Work/Agents role-entry UX for DEL-02-02 is parked — this node therefore renders role entry inside the DEL-02-05 settings panel and writes no Work/Agents surface.

## 5. Write locus (sealed)

- `projects/chirality-app-dev/frontend/src/**` — account/consent UI (`components/settings/account-consent-settings.tsx`), the UI-facing port vocabulary and fake adapter and fixtures (`lib/consent/**`), copy, panel styles (`app/globals.css`, appended block only), and tests (`__tests__/**`).
- `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/{Evidence/**,_run_records/**}` (deliverable-local state; `_STATUS.md` and `MEMORY.md` only at closeout after `REVIEW_PASS`).
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_F_2026-09-03/**` (this record).
- `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` (append only, closeout).

Not written: `runtime/**`, `docs/**`, `frontend/electron/**`, `frontend/package.json`/lockfiles, `frontend/src/components/shell/**` (the fake port is not mounted in the product shell), the decision register, prior receipts, any Root surface.

## 6. Stale-map deltas found while verifying the brief against the live tree (live tree wins)

- The brief cites `plans/steers/chirality_app_v3_app_ruling_record_a11_2026-09-03.md` for the G0 A8 `Opt-in Preview` label. A11 is the Task-Management triage ruling and does not contain that label. The label's ruling source is `plans/steers/chirality_app_v3_g0_record_2026-08-22.md` line 74 (`A8 — Posture label: [click] "Opt-in Preview".`), restated in `chirality_app_v3_phase0_steer_app_reissued_2026-08-23.md` line 42; the three command-network postures are G0 A7 (lines 62–72) and the root-private app-owned `CODEX_HOME` home is G0 A9 (lines 76–78). The delta is recorded here and in the receipt; no map is edited.
- The brief names `npm run validate:release-quality` as the premerge gate; the registered premerge check in `software-workflow.json` is `npm run harness:validate:premerge` behind a stub-provider Next dev server. Both are run and recorded in `CHECKS.json`.

## 7. Existing-surface inventory (read-only, at basis)

- No account/consent vocabulary exists in `frontend/` at basis: `grep -rn "networkApprovalContext|network_access|acceptForSession|CODEX_HOME|role not mechanically|Opt-in Preview|HostedEngineConsentPort" frontend/src frontend/electron frontend/packages` returns nothing. The node is greenfield inside the settings surface.
- Settings-panel pattern to follow: `frontend/src/components/settings/api-key-settings.tsx` (container + pure `…View` with `data-*` state markers; no secret in the DOM) and `frontend/src/lib/credential-storage-state.ts` (shared `as const` vocabulary + type guard). Render-test pattern: `frontend/src/__tests__/components/api-key-settings-storage-states.test.ts` (react-test-renderer, D-APP-36) and `api-key-settings.test.ts` (static markup).
- `frontend/src/lib/harness/managed-delegation.ts:22` defines `AgentType = 0 | 1 | 2`; the role-entry vocabulary here reuses those numerals.
- `frontend/src/components/shell/shell-frame.tsx:286-291` mounts `RuntimeSettings` and `ApiKeySettings` inside the "Runtime & credentials" disclosure; `shell-frame.test.tsx:27` mocks `ApiKeySettings`. The new panel is **not** mounted there (design decision recorded in `RETURN.md`).
