# STEP0_DISCOVERY — APPDEV_V3_NODE_D_2026-09-03

Recorded before any product-source edit. All commands run 2026-09-03 in the
scratch worktree on branch `codex/app-v3-nodeD-v2-session-access-2026-09-03`.

## Git state

| Item | Value |
|---|---|
| Basis (`git rev-parse HEAD` after `git worktree add ... origin/main`) | `0c683fb1657706316272951e4c3a0f7781b46009` |
| Required basis | `0c683fb16` or descendant — satisfied (equal; `git merge-base --is-ancestor 0c683fb16 HEAD` exit 0) |
| `git status --short` line count | 0 (clean) |
| Branch | `codex/app-v3-nodeD-v2-session-access-2026-09-03` (tracking `origin/main`) |
| Parent worktree | untouched; work confined to the scratch worktree |

## Validators (Step 0 core)

| Check | Command (cwd) | Result |
|---|---|---|
| Receipts validator | `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` (REPO_ROOT) | `VALID ... frozen through Receipt-52; versioned receipt contract satisfied` |
| Authority corpus status | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` (WORKING_ROOT) | all `[MATCH]`; `no drift.` |
| APP-HOLD-1 dispatch preflight | `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path loop/LOOP_INIT.md --target DEL-05-01` (WORKING_ROOT) | `"verdict": "ALLOW"`, `scan_held_deliverables: []`, scan fingerprint `c8cc4556356b227fba10d79f110d9efdcc26f408889a10824fe9736e97449747` |
| Harness self-check | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` (REPO_ROOT) | exit 0 |
| Pinned completion reference | `shasum -a 256 plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (REPO_ROOT) | `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` — matches the standing plan pin |
| Newest applicable receipt | `loop/LOOP_RECEIPTS.md` | Receipt-205 (`Examined-Through 8140daec7ab7165f8972451dbdd3a67b8bb2fd38`, `AWAITING_OWNER`); PR #681 merged at basis `0c683fb16` → seating is live, `DEL-05-01-V3-01` is `SELECTABLE` on `main` |
| `npm ci` | `npm ci` (FRONTEND) | exit 0; Node `v24.18.0`, npm `11.16.0`, Vitest `4.1.10` |

## A1 re-stage declaration (this tranche touches `frontend/src/**`)

Quoted from `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md`
lines 28-36 (repo-root `plans/steers/`):

> Recorded form: G0.25 is PASSED and WP-00 is closed. The standing
> frontend-freeze guard from G0 C2 is replaced by the recorded re-stage rule:
> any mutation under `projects/chirality-app-dev/frontend/` invalidates the
> staged procedure for any future proof claim and requires a newly staged
> revision and a fresh owner-executed proof. This ruling makes no signing,
> notarization, DMG, deployment, distribution, publication,
> release-readiness, or acceptance claim beyond the login-session proof
> itself; DEL-09-04's remaining scope stays `IN_PROGRESS` and separately
> gated.

Declaration: this tranche mutates `projects/chirality-app-dev/frontend/src/**`
(product source and tests). Under the A1 re-stage rule, the staged R20 login-
session proof procedure is invalidated for any future proof claim; a newly
staged revision and a fresh owner-executed proof are required before any such
claim. No proof claim is made by this tranche.

## Item contract re-derived from the live tree

- `_STATUS.md` `## Remaining` carries `DEL-05-01-V3-01` (`SELECTABLE`) with
  write locus `frontend/src/lib/harness/session-manager.ts` and related
  tests/fixtures plus deliverable-local state — matches the brief.
- `ScopeOfWork.md`: OUT-001 (canonical folder-backed store and first-touch
  legacy migration); R003 (legacy flat records converted on first
  read/list/resume/save/delete access); R004 (existing flat records list and
  resume through canonical conversion; runtime code must not keep flat
  records as a standing parallel *storage* shape); R015 (evidence names the
  active module, helper behavior, and focused validation commands).
- `_DEPENDENCIES.md` DEP-05-01-006 (`Current session storage implementation
  and tests`, ACTIVE / SATISFIED) — the existing lazy conversion path in
  `session-manager.ts` is the basis; DEP-05-01-013 (Root daemon store) is
  consumed only by `V3-02`, which stays parked.
- D-APP-41 ruling (Option D, 2026-06-21): canonical store is
  `.chirality/sessions/<sessionId>/session.json`; flat records convert on
  first access; duplicate shape resolves "by migrating, archiving, or removing
  the flat record according to the migration implementation" with no field
  loss for supported legacy fields.
- `docs/SPEC.md` §8.1 (legacy flat records MUST remain readable during
  migration), §8.2 (canonical layout, `CHIRALITY_SESSION_ROOT` override),
  §25.4 (legacy project-local `.chirality/sessions` records "are read lazily
  and migrated non-destructively on access. No bulk rewrite or destructive
  source move is permitted.").
- Live implementation (`session-manager.ts` at basis): `canonicalizeSessionRecord`
  merges legacy+canonical with canonical precedence, writes canonical, and
  then `rm`s the legacy flat file; `readOptionalSessionFile` swallows parse
  errors as `undefined` (so malformed records surface as `SESSION_NOT_FOUND`
  and are silently skipped by `list`). Existing tests
  (`src/__tests__/lib/session-manager.test.ts`) assert legacy-file removal
  after list/resume/save.

## Stale-map / instruction deltas found (live tree wins)

- **Delta 1 — destructive legacy removal vs. non-destructive access
  (re-classified after review: OWNER DECISION, ruled A13).** The live
  implementation and D-APP-41's "removing the flat record" wording delete
  the legacy flat file on first touch; the later authority text
  (`docs/SPEC.md` §25.4, applied decomposition row L322 as seated in
  `V3-01`) and the sealed brief require non-destructive first-touch access.
  The first freeze treated this as a stale-map delta plus agent latitude.
  The independent reviewer (F1, MAJOR) correctly re-classified it as a
  conflict between two sets of *accepted* authority, because DEL-05-01's
  accepted Scope of Work also carried, verbatim (pre-amendment):
  - `DEL-05-01-R010`: "If both canonical folder and legacy flat records
    exist for the same `sessionId`, resolution MUST prefer defined canonical
    values, preserve legacy-only fields, write the merged canonical
    `session.json`, and remove the flat record." (source: D-APP-41;
    `docs/SPEC.md` Section 8.1)
  - CLM-012 verification row for R003/R004/R005/R010/R016: "Legacy fixture
    tests proving flat `.json` records are converted through list, retrieve,
    resume, save, and delete surfaces; duplicate fixture tests proving merge
    precedence, legacy-only field preservation, and flat-file removal."

  Both were superseded in this tranche by owner ruling **A13**
  (`plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md`,
  2026-09-03, K-AUTH-1: "Ratify retention"): retention is the v3 posture;
  R010 and the CLM-012 row are amended in `ScopeOfWork.md` (dated note
  CLM-032; pre-amendment SHA-256
  `41d232f31ee5882721e87a97ebea30973ca412b8ba9268b89713b51118f6b40b`,
  post-amendment
  `312cb00c36cf8b3bbfd0736c319c812ffbbe06a3a51918fd77fbd53fca259df6`);
  a `legacySource` consumption marker makes the flat file a non-read input
  after materialization (reviewer F2); the list-abort regression is fixed
  (F3); D-APP-41 is historical on this one point and its files are not
  edited. Legacy bytes are left intact; materialization writes only to the
  canonical folder; the four existing removal assertions are byte-identity
  assertions. Recorded for the receipt as `Owner-Direction` (A13 pointer),
  not as a stale-map delta.
- **Delta 2 — closed `HarnessErrorType` union.** `HarnessErrorType` lives in
  `runtime/packages/contracts/src/harness/types.ts` (Root-owned, outside the
  write locus). No dedicated error type for an unreadable session record can
  be added in this tranche; typed failure is carried by a dedicated
  `SessionRecordAccessError` subclass with `kind` and structured `details`,
  under the existing `SESSION_NOT_FOUND` type (status 404 for `missing`,
  422 for `malformed`/`unsupportedVersion`). A dedicated contract type is a
  residual for the Root-routed schema work consumed by `V3-02`.
- Brief path note: `plans/steers/...a1...` resolves at repo root
  (`{REPO_ROOT}/plans/steers/`), not under `WORKING_ROOT`; the pinned HTML
  also resolves at `{REPO_ROOT}/plans/`. The receipts validator resolves at
  `{REPO_ROOT}/tools/validation/`.

## Concurrency note

Receipts 206 and 207 are not present on `main` at basis; the brief assigns
this tranche Receipt 208 (parent `Receipt-205`), consistent with concurrent
sibling nodes sharing the parent under ledger rule 7.
