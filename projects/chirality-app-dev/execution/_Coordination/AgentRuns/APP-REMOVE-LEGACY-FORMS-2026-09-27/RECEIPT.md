# Receipt — APP-REMOVE-LEGACY-FORMS-2026-09-27

Derivative account of the SCA-APP-011 code change. The
[work graph](../../WorkGraphs/app-lifecycle-deps-2026-09-26/WORK_GRAPH.md)
(row FU3) records the forms' withdrawal. SCA-APP-011 and the sources below
keep their authority.

**Status: accepted at SCA-APP-011 checkpoint group 3 (2026-09-27).** This is
the code side of SCA-APP-011. The owner accepted group 3 on 2026-09-27 ("I
accept SCA-APP-011 checkpoint group 3"): decision folder
`execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`
(`DECISION.md` SHA-256 `ab2af85f0528c7224c95f2e371e4b00a5e8338f17166e349fb8812fa591bc370`,
`ACCEPTED_MANIFEST.csv` SHA-256
`e076ba0525c84750fd5cc4e336a878a81c1e35e436ab7d255deab8b02df4cd90`), on the
integrated candidate `d48c785c5`. One PR (#995) lands it with the scope text
(choice Q-a) once CI and review have no blocking finding.

## Authority

**Owner direction.** CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. Ryan Tufts,
2026-09-27, Claude Code conversation, as recorded verbatim in the SCA-APP-011
`Brief.md`:

> We don't need to carry the Workbench or Pipeline forms any longer. They are obsolete.

On the dependency, status and status-transition routes the owner selected
"Remove the routes (Recommended)". On the scaffold route (choice S) the owner
selected "Remove the route too". On the route for changing accepted scope the
owner selected "Scope-change amendment (Recommended)".

**Scope-change amendment SCA-APP-011** (`execution/_ScopeChange/`):

- Checkpoint group 1, accepted: snapshot
  `checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/` (`DECISION.md`
  SHA-256 `412c78c28db13c245b8c8ebb58ad418c73fb63182dbb4ccfb085343dae449fa9`,
  `ACCEPTED_MANIFEST.csv` SHA-256
  `d7f96a8be345841d0fda6b3b20b217416dcecf7133334556637592b0030e3545`) and
  pointer `SCA-APP-011_GROUP-1_AUTHORIZED.md`. It accepted BASE, DQ-R, S-c,
  D restate, set L excluded, E no change, M-a and the scaffold library kept.
- Checkpoint group 2, accepted by the owner on 2026-09-27 ("Accept SCA-APP-011
  group 2: W-a, Q-a, with the revision-2 corrections and row 29."): snapshot
  `checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/` (`DECISION.md`
  SHA-256 `0b1a2b24f8b60a8d86694f34c35a2c4918308c99f0e1d58afad3ae289c4673eb`,
  `ACCEPTED_MANIFEST.csv` SHA-256
  `ef3129871c9d8971d5c47e36a5c2973bf24366c847b58daad73ec5adaf261c7e`) and
  pointer `SCA-APP-011_GROUP-2_AUTHORIZED.md`. This candidate was built from the
  package tree at `b0295688c`, before that snapshot was written; the snapshot
  binds the same group-2 files by hash.
- Code specification: `Propagation_Plan.md` §4, revision 2 at `b0295688c`
  (SHA-256 `c0a548dd5e357a7b7199e54fc4fc43d217a9c2268c36134530f822b05c78b1f2`).
  The exact scope text is `Amendment_Preview.md` (SHA-256
  `3781bf3e548bb1497e8f74fe2cb0ecd38314aac7834a7d6a4f7d3eeb7f6a6f40`); its
  verification hooks name the test files this candidate creates.
- Checkpoint group 3, accepted by the owner on 2026-09-27: decision folder
  `checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/` (`DECISION.md`
  SHA-256 `ab2af85f0528c7224c95f2e371e4b00a5e8338f17166e349fb8812fa591bc370`,
  `ACCEPTED_MANIFEST.csv` SHA-256
  `e076ba0525c84750fd5cc4e336a878a81c1e35e436ab7d255deab8b02df4cd90`).

SCA-APP-011 supersedes D-APP-74's route-retention clause, SCA-APP-010's "code
retained" bindings D-006 and D-015 and SR-06's "the code stays"
(`Supersession_Delta.csv`); those bindings took effect on group-3 acceptance.

## Result

The candidate starts from `dcd37f9ae` (the forms removal), cherry-picked onto
`main` at `5a305bc04`, and ends in the state `Propagation_Plan.md` §4 specifies.
For the SCA-APP-011 group-3 review it was integrated on `origin/main` `4087a4f8c`; between `5a305bc04` and `4087a4f8c` only `projects/pec` and `projects/chirality-piping` differ, and the App, `exports`, `docs` and `tools` trees are identical.

- **Forms removed** (from `dcd37f9ae`).
  `frontend/src/components/workbench/workbench-surface.tsx`,
  `frontend/src/components/pipeline/pipeline-surface.tsx` and
  `frontend/src/components/pipeline/lifecycle-gate-fields.tsx`, their tests
  `__tests__/components/workbench-surface.test.ts`, `pipeline-surface.test.ts`
  and `lifecycle-transition-gates.test.tsx`, and the form-only CSS in
  `app/globals.css` (`pipeline-*`, `workbench-layout` and the
  `workbench-documents-block` section; `workbench-card` stays for
  `app/not-found.tsx`). `createTertiarySidebarTabs`
  (`components/shell/tertiary-sidebar-tabs.tsx`) returns only the Portal tab.
  `woven-dialogue-shell.test.tsx` and `woven-dialogue-runtime-reconnect.test.tsx`
  drop their mocks of the two removed modules and the two assertions that
  depended on those mocks.
- **Deliverable routes removed.** `app/api/working-root/deliverable/status/route.ts`,
  `…/status/transition/route.ts` and `…/dependencies/route.ts`.
  `…/deliverable/content/route.ts`, used by the document viewer, stays.
- **Client module removed.** `lib/workspace/deliverable-api.ts` (the fetch
  functions `fetchDeliverableStatus`, `transitionDeliverableStatus` (client
  copy) and `fetchDeliverableDependencies`, `WorkspaceApiClientError` and their
  types) and `__tests__/lib/workspace-deliverable-api.test.ts`. After the forms
  went it had no product importer. The server-side
  `transitionDeliverableStatus` in `deliverable-contracts.ts` is a different
  function and stays.
- **Scaffold route removed.** `app/api/harness/scaffold/route.ts` and
  `__tests__/api/harness/scaffold-route.test.ts`;
  `scaffoldHarnessExecutionRoot` and its `ScaffoldExecutionRootResponse` and
  `CoordinationMode` imports in `lib/harness/client.ts`, and the case
  "scaffolds execution roots through scaffold route" in `harness-client.test.ts`.
- **App scaffold proxy removed.** In `lib/runtime-client/daemon-harness-port.ts`:
  the `scaffold` member of `DaemonHarnessPort`, its `daemonClientUnavailable`
  entry, its scope-map entry `scaffold: 'executionRoot'`, the
  `ScaffoldExecutionRoot*` imports, and the `'executionRoot'` routing kind with
  its branch, which nothing else used. `RuntimeDaemonHarnessPort.scaffold()` in
  `runtime-daemon-harness-port.ts`. The test stubs in
  `runtime-daemon-harness-port.test.ts`, `daemon-proxy-boundary.test.ts`,
  `turn-route-attachments.test.ts` and `fake-daemon-harness-port.ts`, and the
  case "uses only the fixed app-dev project for contained scaffold requests".
  The Runtime's own scaffold API and client method are Runtime-owned and
  untouched.
- **Route test split.** `__tests__/api/working-root/deliverable-contracts.test.ts`
  is replaced by:
  - `__tests__/lib/deliverable-contracts.test.ts` (new): the status, transition
    and dependency cases, calling `readDeliverableStatus`,
    `transitionDeliverableStatus`, `readDeliverableDependencies` and
    `writeDeliverableDependencies` directly; see the port account below;
  - `__tests__/api/working-root/deliverable-content-route.test.ts` (renamed
    remainder): the ten `content/route.ts` cases, unchanged, with the fixtures
    they need.
- **DEL-03-03 `RouteAdapterTestIndex.md`.** Drops its `scaffold-route.test.ts`
  file row and its `/api/harness/scaffold` route row, as the SCA-APP-011
  DEL-03-03 section states; the index records only tests that exist.

**Kept** (Propagation_Plan §4): `deliverable/content/route.ts`;
`lib/workspace/deliverable-contracts.ts`, `lib/workspace/filesystem.ts`
(`workspaceErrorPayload` stays for the content route), `lib/lifecycle/**` and
`lib/dependencies/**`; the scaffold library `lib/harness/scaffold.ts` and
`__tests__/lib/harness-scaffold.test.ts`; `lib/harness/mcp/**` and its tests;
`lib/workspace/task-scope.ts` and `lib/pipeline/pipeline-dispatch-contract.ts`;
every loop-first shell file except the tab-factory change (set L excluded);
`app/workbench/*` and `app/pipeline/*` (the `/workbench` and `/pipeline` URLs
still resolve, D-APP-108 Q3).

## Test port

The old route test had 46 test entries: 36 for status, transition and
dependencies (32 `it` and 4 `it.each` tables with 25 rows, 57 executed tests)
and 10 for the content route.

| Old block (route test) | New location | Entries | Executed tests |
|---|---|---|---|
| Status read, transition, actor and approval-SHA cases | `lib/deliverable-contracts.test.ts` | 5 `it` | 5 |
| "human-ruled CHECKING reversal" | same, same `describe` | 10 `it` + 2 `it.each` | 10 + 10 rows (was 11) + 2 rows = 22 |
| "reopening ISSUED -> IN_PROGRESS under an accepted amendment" (with "inside a Git work tree") | same, same `describe` | 6 `it` + 2 `it.each` | 6 + 5 rows (was 6) + 6 rows = 17 |
| Dependency read, recorded-register, linked-folder, symlink-path, write, write-failure and leaf-symlink cases | same | 11 `it` | 11 |
| Content route | `api/working-root/deliverable-content-route.test.ts` | 10 `it` | 10 |

Every case keeps its name, fixtures and file-state assertions. Result: 55
library tests (57 less the 2 retired rows) and 10 content-route tests.

**Retired with the routes** (request-body parsing, `INVALID_REQUEST`): the
`it.each` rows `['CHECKING', 'a non-string ruling', { ruling: 42 }, 'INVALID_REQUEST']`
and `['a non-string amendment', { amendment: 7 }, 'INVALID_REQUEST']`. The
library types `ruling` and `amendment` as `string` and has no runtime type
check, so these inputs are compile-time errors against it.

**How assertions were restated.** Where a case asserted an HTTP status and
`error.type`, it now asserts the thrown workspace error's `status` and `code`,
which are the values the route mapped to that status and type through
`workspaceErrorPayload`. The codes, statuses and `details` are unchanged. The
"checker code" checks, which searched the serialized error body, search the
same fields (code, message, details) of the thrown error. The thrown class is
`WorkspaceOperationError` for most refusals and `WorkspaceValidationError` for
path validation; the helper accepts either. Where a case asserted a 200
response, it now asserts the returned value (for example `transition.to`)
and the same file state. No outcome code or message changed.

**The ported tests exercise the gates.** Each library gate below was broken
temporarily and the new test file rerun; each broken gate failed the named
cases, and each file was restored:

- the `CHECKING -> IN_PROGRESS` ruling requirement disabled: 1 failure
  ("HUMAN with a SHA but no ruling");
- the ruling containment check disabled: 4 failures (outside, absolute
  outside, forward gate, symlink outside);
- the reversal opened to an agent actor: 1 failure ("an agent actor");
- an amendment-check refusal ignored on the `ISSUED` reopening: 9 failures.

## Records

- The APP-TRANSITION-FORMS receipt's dated note names SCA-APP-011 as the
  authority for removing the forms it built.
- Work-graph FU3 is WITHDRAWN and its D-APP-36 render-evidence item closed as
  moot. FU3 and FU4 now say the routes are retired under SCA-APP-011 and that
  the verification hooks are restated by the SCA-APP-011 scope text.
- MEMORY rows for the nine SCA-APP-011 deliverables: DEL-02-02, DEL-02-03,
  DEL-03-03, DEL-07-01, DEL-07-02, DEL-07-04, DEL-07-05, DEL-08-03 and
  DEL-09-03.
- `loop/LOOP_RECEIPTS.md` Receipt-269; tranche manifest
  `docs/governance_harness/tranche_manifests/APP-REMOVE-LEGACY-FORMS-20260927.yaml`.
- `exports/chirality-app/` regenerated with the export tooling.
- **Not written here.** The App SPEC, PRD and PLAN, the decomposition and the
  Scopes of Work and `_CONTEXT.md` files that SCA-APP-011 amends are the
  scope-text side (`Propagation_Plan.md` §2, W-a). `dcd37f9ae`'s own edits to
  the App SPEC and to the DEL-02-02, DEL-07-04 and DEL-08-03 Scopes of Work were
  dropped, because the SCA-APP-011 exact text replaces them.

## Legacy shell: what remains dead (not removed)

Every route renders `WovenDialogueRoute`, which discards its `legacy` prop.
These modules are reachable only through that discarded prop:
`components/shell/loop-shell.tsx`, `portal-loop-shell.tsx`,
`loop-tertiary-shell.tsx`, `sidebar-right-loop-layout.tsx`,
`tertiary-sidebar-tabs.tsx` and `components/portal/agent-matrix.tsx`. Set L
excluded them from SCA-APP-011, so they stay. Also dead, and recorded as
residuals in `Propagation_Plan.md` §11 or here:

- the `workbenchTab` and `pipelineTab` props, `WORKBENCH_TAB`/`PIPELINE_TAB` and
  the `'workbench'`/`'pipeline'` tab ids in `workspace-sidebar.tsx` and
  `sidebar-right-loop-layout.tsx`;
- `defaultSidebarTab="workbench"`/`"pipeline"` and the form subtitles in
  `app/workbench/workbench-client.tsx` and `app/pipeline/pipeline-client.tsx`;
- `DeliverablesProvider` in `app/layout.tsx`, which has no consumer but still
  fetches `/api/project/deliverables` when the working root changes;
- `/api/working-root/scope`, whose only caller was the Workbench form (its
  removal would be a separate owner decision);
- `task-scope.ts` `normalizeTaskScopeMode` and `sanitizeTaskSelection`: tests
  only (kept for DEL-08-03);
- the CSS rule `.woven-focused-surface > .panel`, which no component renders.

## Checks (worktree candidate)

Run on the actual candidate, with exit codes in the hand-off to the parent
session: frontend typecheck (0); the focused Vitest files (the new library
test, the content-route test, the harness client, daemon-port, daemon-proxy
and turn-route tests, and lifecycle-status, recorded-register-parity,
amendment-reopen-parity and harness-scaffold); the full Vitest suite (the
known uid-0 `harness-attachment-resolver` failure is the only failure); the
gate-mutation checks above; a repository search for the removed symbols and
route paths (no code reference remains); the Root validators G0–G3, the
agent-instruction, workflow-metadata, instruction-entrypoint, receipt,
conflict-marker and run-record-leak validators, the workflow index check,
`git diff --check` and G4 (this tranche's manifest); and export regeneration.
The App has no lint script. Independent review and actual-candidate CI remain
merge gates.

## Limits

- Group 3 of SCA-APP-011 is accepted. The candidate lands only with the
  scope text, in one PR, once CI and review have no blocking finding.
- The group-2 decision snapshot was not in the package tree this candidate
  read; its folder and hashes were bound afterwards, in the group-3 integration
  (see the group-2 entry under Basis).
- No build or packaged run. The removed forms were not mounted in the live App,
  and no live UI called the removed routes or the scaffold proxy.
- The Runtime keeps its scaffold API. The scope-change side sent the
  informational Runtime notice after group-3 acceptance:
  `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-27_APP_SCA-APP-011_SCAFFOLD_API.md`.
- The App authority corpus already drifted for the App SPEC; the drift is
  retained, not repinned.
- No lifecycle transition, approval-SHA refresh, dependency-register change,
  Task Management edit, release or issuance.

Execution: a Claude Code subagent (TASK-type executor, no delegation) in an
isolated worktree for the parent session. Model identifiers are withheld at the
dispatching session's instruction; the commit's session trailer identifies the
run.
