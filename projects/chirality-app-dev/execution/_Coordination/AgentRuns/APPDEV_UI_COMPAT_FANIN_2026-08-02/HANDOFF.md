# App-Dev UI Compatibility Repair — Cross-Package Fan-In

- Date: 2026-08-02
- RunID: `APPDEV_UI_COMPAT_FANIN_2026-08-02`
- Parent: `HELP_HUMAN` (Agent 0)
- Fan-in manager: `HELPS_HUMANS-APPDEV-UI-COMPAT-FANIN-2026-08-02`
  (`HELPS_HUMANS`, Agent 1)
- Accepted source basis: `1d4abf1cf1a23a33bd7fec59971251f86c010210`
- Verdict: `PASS_WITH_NON_BLOCKING_PREMERGE_RERUN_ADVISORY`
- Next owner: `CHANGE`; no commit, push, or merge was performed here.

## Original package split and child identities

HELP_HUMAN activated two one-package WORKING_ITEMS managers. PKG-02 instance
`WORKING_ITEMS-PKG02-DEL0202-UI-COMPAT` managed DEL-02-02 and dispatched TASK
Agent 2 attempts `TASK_RUN_DEL-02-02_2026-08-02_1812` and
`TASK_RUN_DEL-02-02_2026-08-02_1818_ATTEMPT_2`. PKG-08 instance
`WORKING_ITEMS-PKG08-DEL0802-R2` managed DEL-08-02 and dispatched ephemeral
generalist Agent 2 `A2-DEL0802-LEGACY-MARKER` under run
`APPDEV-PKG08-DEL0802-LEGACY-MARKER-2026-08-02`. Neither Agent 2 delegated.

The original split gave each package one deliverable and disjoint semantic
writes, but each child also bore Bash. Under the app-harness Bash rule that
makes each child a project-root integration owner, so package separation alone
was not a sufficient concurrency boundary. The correction is recorded here:
the completed package returns were frozen, no further concurrent child Bash
was allowed, and HELPS_HUMANS performed one serialized combined validation and
handoff as the integration owner. The historical child returns are preserved;
this correction does not rewrite them or imply that the earlier overlapping
test observation was package-isolated.

## Accepted package effects

- DEL-02-02: recorded session timestamps include their fixed year; the expanded
  toggle reads `Recent sessions`; the real React control is proven from the
  four-item recent view to all eight fixture sessions, including the
  unattributed record, and back. Invalid/empty dates remain blank.
- DEL-08-02: `WovenDialogueRoute` owns exactly one
  `data-legacy="true"` boundary on `legacy=1`; `display: contents` keeps the
  arbitrary injected legacy node layout-neutral; default Woven routes remain
  unmarked.
- Resolved Remaining bullets were removed only from the two owning status
  files. The owner-reserved total-per-Working-Root versus per-group count
  question and both packaged Desktop smoke residuals remain open.

## Test environment and combined validation

The checkout did not contain installed dependencies. HELP_HUMAN authorized the
temporary symlink
`projects/chirality-app-dev/frontend/node_modules` to
`/Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules`
after both `frontend/package-lock.json` files matched SHA-256
`674fe2dab74572f21d26455498461d62eaa4218560e45024ed2a31e00c635ab8`.
No dependency was installed or modified.

- Focused combined Vitest: PASS, 2 files and 15 tests.
- Full frontend Vitest: PASS, 140 files passed / 1 skipped; 1096 tests passed /
  4 skipped.
- Typecheck: PASS.
- Production Next, Electron main/preload, and CLI build: PASS.
- HELP_HUMAN in-app browser evidence: PASS on `/`, `/chat`, `/workbench`, and
  `/pipeline`. Each `?legacy=1&unknown=kept` route had one component-owned
  marker, computed `display: contents`, a `MAIN` child, preserved query, and no
  horizontal overflow; default routes had zero legacy markers, one expected
  Woven surface, preserved query, and no overflow. Four-route screenshot/manual
  review passed and the browser error log was empty.
- Practitioner harness: PASS, 349 tests. App status: PASS, 53/53
  `IN_PROGRESS`, no findings. Repository self-check: exit 0 with only the known
  cross-root findings. Authority corpus v18: PASS, no drift. Receipt validator:
  PASS after Receipt 110 was appended.

Local premerge remains a non-blocking rerun advisory. The registered managed
dev-server attempt reached ready state but served `_not-found`/404 for the
harness routes. A final bounded diagnostic used exact server command
`CHIRALITY_HARNESS_PROVIDER=stub NEXT_TELEMETRY_DISABLED=1 node node_modules/next/dist/bin/next start --port 3109`,
port `3109`, and `HARNESS_BASE_URL=http://127.0.0.1:3109`; the exact
`/api/harness/session/list?projectRoot=...` curl reached the real route and
returned HTTP 503 with body
`{"error":{"type":"ENGINE_UNAVAILABLE","message":"Chirality runtime daemon client is not configured"}}`.
Thus the local profile cannot satisfy the older in-process Section 8 assumption;
the established PR CI premerge check is the authoritative rerun. The active
local server was stopped.

## Preservation and CHANGE handoff

Lifecycle, authorization basis, directives, and all 53 Checking Approval SHA
fields are byte-preserved. Dependencies, decomposition, accepted closure
pointers, runtime/adapter behavior, D-APP-84 and H1 no-Bash posture, both Task
Management registers, the unselected parity instrument, and the six D-APP-81
UNKNOWN historical relations are unchanged. No authority, lifecycle, release,
issuance, reliance, or professional claim is created.

CHANGE should integrate the two package source/test/status/memory/run-record
sets together with this handoff, Receipt 110, and the completion-log entry.
The temporary dependency symlink is not an artifact and must be absent before
CHANGE begins. PR CI must rerun the authoritative harness premerge check.
