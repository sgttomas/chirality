# RETURN — D1_IMPLEMENTER — APPDEV_V3_NODE_D_2026-09-03

Item: `DEL-05-01-V3-01` — v2 session-data lazy non-destructive access
fixtures with typed failure.
Status: `FROZEN_FOR_REVIEW` (local commit; not pushed).
Basis: `0c683fb1657706316272951e4c3a0f7781b46009`; branch
`codex/app-v3-nodeD-v2-session-access-2026-09-03`.
Model: Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 implementer
under HELP_HUMAN (Claude Fable 5.1).

## Behavior delivered

`frontend/src/lib/harness/session-manager.ts` (`FileSessionManager`):

1. **Typed record reading.** `readSessionRecordFile` returns
   `ok | missing | malformed | unsupportedVersion` for either shape (legacy
   flat `{id}.json`, canonical `{id}/session.json`) and never throws on
   record content. `unsupportedVersion` covers a declared `schemaVersion`
   (2.0.0 project-local records carry none) and a version-less record that
   lacks the required v2 fields `projectRoot` / `createdAt`.
2. **Typed access surface.** New `inspect(sessionId): SessionAccessResult`
   (`ok { session, materialized, siblingFailures } | missing | malformed |
   unsupportedVersion`) and `listWithDiagnostics(projectRoot):
   { sessions, failures }`. `list` still returns `SessionRecord[]`
   (`ISessionManager` unchanged — it is Root-owned). `getById` / `resume` /
   `save` / `delete` throw `SessionRecordAccessError` (a `HarnessError`
   subclass, wire type `SESSION_NOT_FOUND`, status 404 for `missing`, 422
   for `malformed` / `unsupportedVersion`, `kind` + `details.{kind, shape,
   filePath, reason, schemaVersion?, projectRoot?}`), never a raw parse
   error. List no longer silently skips unreadable siblings: they are
   returned as `failures` (a malformed file cannot prove its project, so it
   is reported unless it declares a different `projectRoot`).
3. **Non-destructive first touch.** Access never writes, truncates, or
   deletes a legacy flat file. Materialization writes only
   `{id}/session.json`: on first touch of a legacy-only record, or when a
   legacy record contributes fields the existing canonical record lacks
   (key-order-insensitive compare, so repeat access writes nothing).
   Canonical fields win over legacy fields (D-APP-41 precedence; legacy-only
   fields preserved). A corrupt canonical record fails closed and is never
   overwritten from the flat sibling. `list` materializes only sessions
   bound to the requested project root. The pre-existing `rm` of the legacy
   flat file on first touch is removed.
4. **Preserved semantics.** `list` order (createdAt), project-root
   filtering, `save` merge, unsafe-id guard, 404 for absent sessions, and
   `delete` (opens first; removes the deleted session's canonical folder and
   legacy flat file; siblings untouched) are unchanged. `delete` of an
   unreadable record throws the typed error and leaves all bytes as found.

Out of scope and untouched: canonical folder layout, `HarnessEvent`,
`events.jsonl` handling (`session-events.ts`), `runtime/**`, dependencies,
bulk migration, backup/rollback (S-4).

## Files

| Path (under `projects/chirality-app-dev/`) | Change |
|---|---|
| `frontend/src/lib/harness/session-manager.ts` | typed reader/resolver, `inspect`, `listWithDiagnostics`, `SessionRecordAccessError`, non-destructive materialization |
| `frontend/src/__tests__/fixtures/sessions/v2/{manifest.json, sess_v2_readable.json, sess_v2_malformed_truncated.json, sess_v2_unsupported_version.json, sess_v2_missing_version_fields.json, sess_v2_other_project.json, sess_v2_duplicate.json, sess_v2_duplicate/session.json, sess_v2_duplicate/events.jsonl}` | new representative 2.0.0 fixtures (placeholder project roots; no secrets/user data) |
| `frontend/src/__tests__/lib/session-manager-v2-legacy-access.test.ts` | new evaluator (23 tests): typed states, byte identity, idempotence, list diagnostics, precedence, fail-closed canonical, save, delete |
| `frontend/src/__tests__/lib/session-manager.test.ts` | four post-access assertions changed from "flat file removed" to "flat file byte-identical"; titles updated; delete contract test unchanged |
| `execution/PKG-05_.../DEL-05-01_.../Evidence/V3-01_v2_lazy_access_2026-09-03/{BYTE_IDENTITY_PROOF.md, FIXTURE_INVENTORY.sha256, focused_vitest_results.json, focused_vitest_stdout.txt}` | evidence packet per the workplan Evidence contract |
| `execution/PKG-05_.../DEL-05-01_.../_run_records/TASK_RUN_2026-09-03_V3-01_v2_lazy_access.md` | run record incl. D-APP-60/64 latitude exercises and rejections |
| `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/{ORCHESTRATION_PLAN.md, WORK_GRAPH.json, STEP0_DISCOVERY.md, instances/D1_IMPLEMENTER/LAUNCH_BRIEF.md, RETURN.md, CHECKS.json, PREMERGE_RESULTS.json}` | this run record |

Deliverable `_STATUS.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, and
Receipt 208 are written only after `REVIEW_PASS` (brief order).

## Byte-identity proof

`Evidence/V3-01_v2_lazy_access_2026-09-03/BYTE_IDENTITY_PROOF.md` §3:
every evaluator test snapshots the seeded session root, performs the
operation, and asserts `Buffer.equals` on each legacy flat file (and the
duplicate's `events.jsonl`) plus a before/after file-set comparison proving
the only new path is the accessed session's canonical `session.json`.
Fixture identities: `FIXTURE_INVENTORY.sha256` (sorted SHA-256).
Machine-readable results: `focused_vitest_results.json` (35/35 passed).

## Checks

Exact commands, cwd, exit codes: `CHECKS.json`.

| Check | Result |
|---|---|
| `npm run typecheck` (frontend) | PASS |
| `npm test` full Vitest (frontend) | PASS — 156 files passed, 1 skipped; 1300 tests passed, 4 skipped |
| focused Vitest (2 session-manager files) | PASS — 35/35 |
| `npm run build` (frontend; optional for `src/**`) | PASS |
| premerge via `run_registered_checks.py --check frontend-premerge` | FAIL — every route 503 `ENGINE_UNAVAILABLE "Chirality runtime daemon client is not configured"`: the absent-runtime-daemon-bindings class (precedent in Receipts at `LOOP_RECEIPTS.md:5183,5313`); deferred to PR CI per the brief and `AGENTS.md` host-capability rule. Not attributable to this change: the HTTP routes call the daemon port, not `FileSessionManager`. |
| `git diff --check` (repo root, working tree and staged) | PASS |
| harness `self-check` (repo root) | PASS (exit 0) |
| harness pytest (repo root) | PASS — 350 passed |
| APP-HOLD scan `--require-register-match` (working root) | PASS |
| authority corpus `status` (working root) | PASS — no drift |
| receipts validator (repo root) | VALID |
| write-scope `validate_change_scope.py` | PASS (see `CHECKS.json`) |

Prerequisite performed once: `cd runtime && npm ci && npm run build`
(the CI order; produces ignored `dist/` so `@chirality/runtime-contracts`
resolves for typecheck/Vitest). No tracked file under `runtime/` changed.

Incident (recorded, repaired): the first `run_registered_checks.py`
invocation with a run-record-relative `--output` resolved it against the
workspace root and wrote an untracked stray
`{REPO_ROOT}/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/PREMERGE_RESULTS.json`
under the Root project's `execution/` tree; it was removed before any
commit (confirmed untracked; `git status` clean of non-App paths) and the
runner was rerun with a `projects/chirality-app-dev/...`-prefixed output.

## Stale-map / instruction deltas (live tree wins)

See `STEP0_DISCOVERY.md`: (1) destructive flat-file removal in the live
code and D-APP-41's "removing" wording vs. `docs/SPEC.md` §25.4 and the
seated item's non-destructive requirement — the seated item governs; (2)
`HarnessErrorType` is a closed Root-owned union — typed failure rides on
`SESSION_NOT_FOUND` with `kind` and status 422; (3) brief paths for the A1
steer, pinned HTML, and receipts validator resolve at `{REPO_ROOT}`.

## Residual risks and follow-ups (not blockers)

- `inspect` / `listWithDiagnostics` exist on `FileSessionManager` only;
  `ISessionManager` and the HTTP routes (which now target the daemon port)
  are outside this locus, so UI labelling of unreadable records needs a
  route/port surface — candidate for the Root-routed schema work consumed
  by `DEL-05-01-V3-02` or a DEL-05-04 transcript-view item.
- No dedicated `HarnessErrorType` for unreadable records (Root contract);
  clients must read `details.kind` / the `SessionRecordAccessError` class.
- Retained legacy flat files after materialization are never cleaned up
  here (by design; S-4 `SCOPE_AMENDMENT_REQUIRED` is unseated). A record
  with `schemaVersion` declared is always `unsupportedVersion`; the supported
  set is exactly "no declared version" until a Root schema is routed.
- Non-record I/O failures during `list` materialization (e.g. `EACCES` on
  the canonical folder) now propagate instead of being silently swallowed.
- Premerge is PR-CI-owed for this branch (daemon-binding class).
- A1 re-stage rule applies: `frontend/` mutated; any future R20 proof claim
  needs a newly staged revision and a fresh owner-executed proof.

## Write-scope validation

`python3 tools/software_workflow/validate_change_scope.py . --allowed
projects/chirality-app-dev/frontend/src/lib/harness/session-manager.ts
--allowed projects/chirality-app-dev/frontend/src/__tests__ --allowed
projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-01_Canonical_Session_Folder_and_Legacy_Session_Migration
--allowed projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03
--allowed projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` → `PASS`, zero
violations (result recorded in `CHECKS.json`).
