# RETURN — D1_IMPLEMENTER — APPDEV_V3_NODE_D_2026-09-03

Item: `DEL-05-01-V3-01` — v2 session-data lazy non-destructive access
fixtures with typed failure.
Status: `RE-FROZEN_FOR_REVIEW_ROUND_2` (second local commit on the branch;
not pushed).
Basis: `0c683fb1657706316272951e4c3a0f7781b46009`; branch
`codex/app-v3-nodeD-v2-session-access-2026-09-03`; first freeze
`3b6b4758bca7cd0e4ac84f9685052a0548c4ca2e` (review round 1:
`instances/D2_REVIEWER/REVIEW_ROUND_1.md`, 0 blocking / 1 major / 2 minor).
Model: Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 implementer
under HELP_HUMAN (Claude Fable 5.1).

## Owner ruling applied — A13 (K-AUTH-1, 2026-09-03)

`plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md`
(SHA-256 `557c64aaf765b20b877cd3a5331d0f6a4c73e562c5463eaf5f9c5e122e325271`),
"Ratify retention": retention of the legacy flat session record after
canonical materialization is the v3 posture (AT-035 "opens without
destructive rewrite"). Under it this tranche (a) amended DEL-05-01
`ScopeOfWork.md` rows R010 and CLM-012 and added the dated note CLM-032
(pre-amendment SHA-256
`41d232f31ee5882721e87a97ebea30973ca412b8ba9268b89713b51118f6b40b`,
post-amendment
`312cb00c36cf8b3bbfd0736c319c812ffbbe06a3a51918fd77fbd53fca259df6`; SOW
validator `PASS format=SOW_V1`); (b) added the `legacySource` consumption
marker (reviewer F2); (c) fixed the list-abort regression (reviewer F3);
(d) re-froze for a fresh review. D-APP-41 stays historical on the single
point of flat-record removal; its files are not edited.

Superseded text, verbatim (pre-amendment), for the record:

- `DEL-05-01-R010`: "If both canonical folder and legacy flat records exist
  for the same `sessionId`, resolution MUST prefer defined canonical values,
  preserve legacy-only fields, write the merged canonical `session.json`, and
  remove the flat record."
- CLM-012 row (R003/R004/R005/R010/R016): "Legacy fixture tests proving flat
  `.json` records are converted through list, retrieve, resume, save, and
  delete surfaces; duplicate fixture tests proving merge precedence,
  legacy-only field preservation, and flat-file removal."

The first freeze's classification of this fork as a stale-map delta plus
agent latitude was wrong in kind (reviewer F1); it is corrected in
`STEP0_DISCOVERY.md` Delta 1, the TASK run record, and
`BYTE_IDENTITY_PROOF.md` §1.

## Behavior delivered

`frontend/src/lib/harness/session-manager.ts` (`FileSessionManager`):

1. **Typed record reading.** `readSessionRecordFile` returns
   `ok | missing | malformed | unsupportedVersion` for either shape (legacy
   flat `{id}.json`, canonical `{id}/session.json`) and never throws on
   record content; `ok` carries the file's sha256. `unsupportedVersion`
   covers a declared `schemaVersion` (2.0.0 project-local records carry none)
   and a version-less record lacking the required v2 fields `projectRoot` /
   `createdAt`.
2. **Typed access surface.** `inspect(sessionId): SessionAccessResult`
   (`ok { session, materialized, siblingFailures, diagnostics } | missing |
   malformed | unsupportedVersion`) and `listWithDiagnostics(projectRoot):
   { sessions, failures, diagnostics }`. `list` still returns
   `SessionRecord[]` (`ISessionManager` unchanged — Root-owned). `getById` /
   `resume` / `save` / `delete` throw `SessionRecordAccessError`
   (`HarnessError` subclass; wire type `SESSION_NOT_FOUND`; 404 for
   `missing`, 422 for `malformed` / `unsupportedVersion`; `kind` +
   `details.{kind, shape, filePath, reason, schemaVersion?, projectRoot?}`),
   never a raw parse error. Unreadable siblings are returned as `failures`
   rather than skipped (reported unless they declare a different
   `projectRoot`).
3. **Non-destructive first touch with consumption marker (A13 / F2).**
   Access never writes, truncates, or deletes a legacy flat file.
   Materialization writes only `{id}/session.json` and stamps
   `legacySource: { sha256, materializedAt }` (sha256 of the flat file
   bytes). Legacy-only fields are merged exactly once — when the canonical
   record carries no marker (first touch of a legacy-only record, or a
   pre-existing canonical duplicate). With the marker present the flat file
   is not a read input: unchanged → ignored, no write; changed →
   `legacySourceChanged` diagnostic, ignored, no write. A field removed from
   the canonical record is therefore never resurrected. Canonical fields win
   over legacy fields (D-APP-41 precedence, unchanged). A corrupt canonical
   record fails closed and is never overwritten from the flat sibling.
   `list` materializes only sessions bound to the requested project root.
4. **List resilience (A13 / F3).** A per-candidate non-record I/O failure
   (e.g. the canonical folder path occupied by a file, read-only root) never
   aborts `listWithDiagnostics`: the candidate is re-resolved read-only; a
   readable record is listed unmaterialized with a `materializationFailed`
   diagnostic; an unreadable one becomes a typed failure entry.
   `getById`/`resume` still surface the environment fault so a following
   `save` cannot assume persistence.
5. **Preserved semantics.** `list` order (createdAt), project-root
   filtering, `save` merge, unsafe-id guard, 404 for absent sessions, and
   `delete` (opens first; removes the deleted session's canonical folder and
   legacy flat file; siblings untouched) are unchanged. `delete` of an
   unreadable record throws the typed error and leaves all bytes as found.

F2 design choice — "ignore and diagnose" over "re-merge and update marker":
after consumption the canonical record is the accepted truth; re-merging a
changed retained source would let an external edit silently alter the live
record and would resurrect removed fields (the F2 hazard). `docs/SPEC.md`
§8.3 lists `session.json` contents as SHOULD-include and tolerates extra
fields (the daemon's `RuntimeSessionRecord` carries an analogous
`legacy: { sourcePath, migratedAt }` marker and `normalizeLegacy` spreads
unknown fields through; replay consumers use `toMatchObject`-style reads),
so no schema requires a re-merge.

Out of scope and untouched: canonical folder layout, `HarnessEvent`,
`events.jsonl` handling (`session-events.ts`), `runtime/**`, D-APP-41 files,
dependencies, bulk migration, backup/rollback/cleanup (S-4).

## Files (combined, basis → HEAD)

| Path | Change |
|---|---|
| `projects/chirality-app-dev/frontend/src/lib/harness/session-manager.ts` | typed reader (+sha256), `inspect`, `listWithDiagnostics` (+`diagnostics`, resilience), `SessionRecordAccessError`, `legacySource` marker, non-destructive materialization |
| `projects/chirality-app-dev/frontend/src/__tests__/fixtures/sessions/v2/**` (9 files) | representative 2.0.0 fixtures (unchanged since first freeze; inventory matches `FIXTURE_INVENTORY.sha256`) |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/session-manager-v2-legacy-access.test.ts` | evaluator, 26 tests: typed states, byte identity, idempotence, list diagnostics, precedence, marker, no-resurrection (F2), edited-source diagnostic (F2), list resilience (F3), fail-closed canonical, save, delete |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/session-manager.test.ts` | four post-access assertions changed from "flat file removed" to "flat file byte-identical" (now authorized by A13); delete contract test unchanged |
| `projects/chirality-app-dev/execution/PKG-05_.../DEL-05-01_.../ScopeOfWork.md` | A13 amendment: R010, CLM-012 row, new CLM-032 |
| `projects/chirality-app-dev/execution/PKG-05_.../DEL-05-01_.../Evidence/V3-01_v2_lazy_access_2026-09-03/{BYTE_IDENTITY_PROOF.md, FIXTURE_INVENTORY.sha256, focused_vitest_results.json, focused_vitest_stdout.txt}` | evidence packet (results regenerated: 38/38) |
| `projects/chirality-app-dev/execution/PKG-05_.../DEL-05-01_.../_run_records/TASK_RUN_2026-09-03_V3-01_v2_lazy_access.md` | run record; latitude items re-labelled (item 1 owner-ruled A13; F2/F3 choices added); review round 1 noted |
| `plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md` | new owner ruling record (verbatim transcription) |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/**` | this run record incl. `instances/D2_REVIEWER/REVIEW_ROUND_1.md`, `CHECKS.json`, `PREMERGE_RESULTS.json`, `WRITE_SCOPE_VALIDATION.json` |

Deliverable `_STATUS.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, and
Receipt 208 are written only after `REVIEW_PASS` (brief order).

## Byte-identity proof

`Evidence/V3-01_v2_lazy_access_2026-09-03/BYTE_IDENTITY_PROOF.md` §3:
every evaluator test snapshots the seeded session root, performs the
operation, and asserts `Buffer.equals` on each legacy flat file (and the
duplicate's `events.jsonl`) plus a before/after file-set comparison proving
the only new path is the accessed session's canonical `session.json`; the
A13 rows add the marker, no-resurrection, edited-source, and list-resilience
proofs. Fixture identities: `FIXTURE_INVENTORY.sha256`. Machine-readable
results: `focused_vitest_results.json` (38/38 passed).

## Checks (second freeze; exact commands, cwd, exit codes in `CHECKS.json`)

| Check | Result |
|---|---|
| `npm run typecheck` (frontend) | PASS |
| `npm test` full Vitest (frontend) | PASS — 156 files passed, 1 skipped; 1303 tests passed, 4 skipped |
| focused Vitest (2 session-manager files) | PASS — 38/38 |
| `npm run build` (frontend; optional for `src/**`) | PASS |
| premerge via `run_registered_checks.py --check frontend-premerge` (first freeze; not rerun) | FAIL — every route 503 `ENGINE_UNAVAILABLE "Chirality runtime daemon client is not configured"`: absent-runtime-daemon-bindings class (precedent `LOOP_RECEIPTS.md:5183,5313`); deferred to PR CI per the brief. Not attributable to this change (routes call the daemon port, not `FileSessionManager`). |
| SOW validator (`tools/scope_of_work/validate_scope_of_work.py`) on DEL-05-01 | PASS `format=SOW_V1` |
| `git diff --check` (repo root; working tree and staged) | PASS |
| harness `self-check` (repo root) | PASS (exit 0; INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=43 pre-existing) |
| harness pytest (repo root) | PASS — 350 passed |
| APP-HOLD scan `--require-register-match` (working root) | PASS |
| authority corpus `status` (working root) | PASS — no drift |
| receipts validator (repo root) | VALID |
| write-scope `validate_change_scope.py` (basis → working tree, 6 declared roots) | PASS — 28 paths, 0 violations |

Prerequisite performed once: `cd runtime && npm ci && npm run build`
(CI order; ignored `dist/` only). No tracked file under `runtime/` changed.

Incident (first freeze; recorded, repaired): the first
`run_registered_checks.py` invocation with a run-record-relative `--output`
resolved it against the workspace root and wrote an untracked stray under
Root's `{REPO_ROOT}/execution/_Coordination/AgentRuns/`; removed before any
commit (confirmed untracked) and rerun with a `projects/chirality-app-dev/...`
output. Reviewer verified absence at `3b6b4758b`.

## Residual risks and follow-ups (not blockers)

- **N2 / Root-routed proposal for `DEL-05-01-V3-02`:** add a dedicated
  `HarnessErrorType` `SESSION_RECORD_UNREADABLE` (HTTP 422; `details.kind`
  = `malformed | unsupportedVersion`, plus `shape`, `filePath`, `reason`,
  `schemaVersion?`) to `runtime/packages/contracts/src/harness/{types,errors}.ts`
  so unreadable records are not typed `SESSION_NOT_FOUND`, and let
  `lib/harness/error-display.ts` consult `details.kind` in the interim.
  No Root write in this tranche; routed with the Root daemon session/storage
  schema work that `V3-02` consumes.
- `inspect` / `listWithDiagnostics` exist on `FileSessionManager` only;
  `ISessionManager` and the daemon-backed HTTP routes are outside this locus,
  so UI labelling of unreadable records and diagnostics needs a route/port
  surface (V3-02 or a DEL-05-04 transcript-view item).
- Retained legacy flat files accumulate with no cleanup path (by A13 design;
  S-4 `SCOPE_AMENDMENT_REQUIRED` unseated). A declared `schemaVersion` is
  always `unsupportedVersion` until a Root schema is routed.
- Read-permission / I/O errors on a record file are typed `malformed`
  (reason carries the errno code) — N1; folds into the N2 proposal.
- Premerge is PR-CI-owed for this branch (daemon-binding class).
- A1 re-stage rule applies: `frontend/` mutated; any future R20 proof claim
  needs a newly staged revision and a fresh owner-executed proof.

## Write-scope validation

`python3 tools/software_workflow/validate_change_scope.py . --base
0c683fb1657706316272951e4c3a0f7781b46009 --allowed
projects/chirality-app-dev/frontend/src/lib/harness/session-manager.ts
--allowed projects/chirality-app-dev/frontend/src/__tests__ --allowed
projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration
--allowed projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03
--allowed projects/chirality-app-dev/loop/LOOP_RECEIPTS.md --allowed
plans/steers/chirality_app_v3_app_ruling_record_a13_2026-09-03.md` → `PASS`,
28 paths, zero violations (`WRITE_SCOPE_VALIDATION.json`).
