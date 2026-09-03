# DEL-05-01-V3-01 — v2 session-data lazy non-destructive access: evidence packet

**Epistemic status:** implementation evidence (derivative). Authority remains
the accepted Scope of Work, `docs/SPEC.md` §8 and §25.4, and the D-APP-41
ruling; on any disagreement those govern.

Run record: `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/`
(basis `0c683fb1657706316272951e4c3a0f7781b46009`; branch
`codex/app-v3-nodeD-v2-session-access-2026-09-03`).

## 1. Active module and helper behavior (R015)

- Active session storage module: `frontend/src/lib/harness/session-manager.ts`
  (`FileSessionManager`, the in-process `ISessionManager` used by
  `frontend/src/lib/harness/runtime.ts`).
- Record reader: `readSessionRecordFile(filePath, shape)` returns a typed
  `SessionRecordReadResult` (`ok | missing | malformed | unsupportedVersion`)
  and never throws for record content. `missing` = `ENOENT`/`ENOTDIR`;
  `malformed` = unreadable file, invalid JSON, or a non-object document;
  `unsupportedVersion` = a declared `schemaVersion` (2.0.0 project-local
  records carry none) or, with no `schemaVersion`, a record lacking the
  required v2 fields `projectRoot` and `createdAt`.
- Access resolver: `resolveSessionRecord(sessionId, { materializeOnlyFor? })`
  reads both shapes; canonical `session.json` wins field-by-field, legacy-only
  fields are preserved; the canonical record is written only when absent or
  when the legacy record contributes fields the canonical record lacks
  (key-order-insensitive comparison, so a second access writes nothing). A
  canonical record that cannot be opened fails closed and is never
  overwritten from the legacy sibling. The legacy flat file is never written,
  truncated, or removed by access.
- Public typed surface: `FileSessionManager.inspect(sessionId)` returns
  `SessionAccessResult`; `listWithDiagnostics(projectRoot)` returns
  `{ sessions, failures }`; `list` returns `sessions` (interface unchanged).
  `getById`/`resume`/`save`/`delete` throw `SessionRecordAccessError`
  (`HarnessError` subclass; wire type `SESSION_NOT_FOUND`; status 404 for
  `missing`, 422 for `malformed`/`unsupportedVersion`; `kind` mirrored in
  `details.kind` with `shape`, `filePath`, `reason`, `schemaVersion?`,
  `projectRoot?`).
- Delete: opens the record first (typed failure leaves every byte as found),
  then removes the deleted session's canonical folder and its legacy flat
  file — the pre-existing contract — and touches nothing else.

## 2. Fixture inventory (exact input identities)

Fixture root: `frontend/src/__tests__/fixtures/sessions/v2/` (release
`2.0.0` shape; placeholders `__PROJECT_ROOT__` / `__OTHER_PROJECT_ROOT__`
are substituted with the test's temporary absolute roots when seeded; no
secrets, credentials, or user data). Sorted SHA-256 inventory:
`FIXTURE_INVENTORY.sha256` beside this file (recompute from the fixture root
with `find . -type f | sed 's|^\./||' | LC_ALL=C sort | xargs shasum -a 256`).

| Session id | Files | Case | Expected typed state |
|---|---|---|---|
| `sess_v2_readable` | `sess_v2_readable.json` | (a) readable, well-formed | `ok`, `materialized: true` on first touch |
| `sess_v2_malformed_truncated` | `sess_v2_malformed_truncated.json` | (b) truncated mid-string | `malformed` (`invalid JSON: …`) |
| `sess_v2_unsupported_version` | `sess_v2_unsupported_version.json` | (c) `schemaVersion: "chirality.session/v9"` | `unsupportedVersion` |
| `sess_v2_missing_version_fields` | `sess_v2_missing_version_fields.json` | (c) no `schemaVersion`, no `projectRoot`/`createdAt` | `unsupportedVersion` |
| `sess_v2_other_project` | `sess_v2_other_project.json` | readable, other project root | `ok`; excluded from list and not materialized by list |
| `sess_v2_duplicate` | `sess_v2_duplicate.json`, `sess_v2_duplicate/session.json`, `sess_v2_duplicate/events.jsonl` | (d) legacy record with existing canonical counterpart | `ok`; canonical precedence, legacy-only fields materialized into canonical |

## 3. Byte-identity proof

Evaluator: `frontend/src/__tests__/lib/session-manager-v2-legacy-access.test.ts`.
Each test seeds the fixture set into a fresh `CHIRALITY_SESSION_ROOT`, takes a
full recursive byte snapshot (`snapshotBytes`), performs the access under
test, then re-reads every legacy flat file (and `events.jsonl`) and asserts
`Buffer.equals` against the snapshot (`expectBytesUnchanged`). File-set
assertions (`listFilesRecursively` before/after) prove that the only new
path is the materialized canonical `session.json` of the accessed readable
session and that no folder is created for unreadable records.

Assertions by operation (all in the evaluator file):

| Operation | Legacy bytes | Canonical writes | Typed observation |
|---|---|---|---|
| `inspect` over every fixture | identical (6 flat files + `events.jsonl`) | readable/duplicate/other-project only | kinds match manifest `expectedKind` |
| `inspect` twice | identical | second access writes nothing | `materialized: false` |
| `listWithDiagnostics` / `list` | identical | `sess_v2_readable/session.json` only | 3 failures reported (malformed, 2× unsupportedVersion) |
| `list` twice | identical | none on second run | results equal |
| `resume` / `getById` readable | identical | canonical only | record fields |
| `resume` malformed / unsupported (×3) | identical (whole root) | none | `SessionRecordAccessError` 422, `details.kind` |
| `getById` duplicate | identical (`sess_v2_duplicate.json`, `events.jsonl`) | canonical gains legacy-only fields once | canonical precedence |
| corrupt canonical + readable legacy | identical (both files) | none (corrupt bytes preserved) | `malformed`, `shape: 'canonical'` |
| unreadable legacy beside readable canonical | garbage preserved | none | `ok` + `siblingFailures[0]` |
| `save` | identical | canonical only | — |
| `delete` readable, then duplicate | siblings identical | deleted session's folder and flat file removed | remaining failures still reported |
| `delete` malformed / unsupported / absent | identical (whole root) | none | 422 / 422 / 404 |

Existing evaluator `frontend/src/__tests__/lib/session-manager.test.ts` was
extended: the four assertions that previously expected the legacy flat file
to disappear after resume/list/save/duplicate access now assert the seeded
bytes are returned unchanged; the delete contract test is unchanged.

## 4. Results (machine-readable and canonical stdout)

- `focused_vitest_results.json` — Vitest JSON reporter over the two
  evaluator files (35 tests, 35 passed, 0 failed); absolute worktree prefix
  replaced by `{REPO_ROOT}`.
- `focused_vitest_stdout.txt` — verbose reporter stdout for the same run
  (exit 0).
- Full registered checks: `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_D_2026-09-03/CHECKS.json`.

## 5. Environment

macOS (darwin 25.6.0, arm64); Node `v24.18.0`; npm `11.16.0`; TypeScript
`5.9.3`; Vitest `4.1.10`; Next `15.5.21`. Shared runtime built once with
`cd runtime && npm ci && npm run build` (CI prerequisite for
`@chirality/runtime-contracts` resolution; emits ignored `dist/` only).
Effective environment for the evaluator: `CHIRALITY_SESSION_ROOT` set per
test to a `mkdtemp` root under `os.tmpdir()`; no network; no credentials.

## 6. Rerun method (bounded)

```text
cd {REPO_ROOT}/runtime && npm ci && npm run build
cd {REPO_ROOT}/projects/chirality-app-dev/frontend && npm ci
npx vitest run src/__tests__/lib/session-manager-v2-legacy-access.test.ts src/__tests__/lib/session-manager.test.ts
npm run typecheck
npm test
cd src/__tests__/fixtures/sessions/v2 && find . -type f | sed 's|^\./||' | LC_ALL=C sort | xargs shasum -a 256 \
  | diff - {this directory}/FIXTURE_INVENTORY.sha256
```

## 7. Cleanup proof

Every evaluator test creates its session root with `mkdtemp` and removes it
in `afterEach` (`rm -rf`) and unsets `CHIRALITY_SESSION_ROOT`; no state is
left outside the temporary directory. No user-wide state, credentials, or
binaries are preserved in this packet.
