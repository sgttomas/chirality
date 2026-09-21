# ROUTES capability inventory: notes (R1b, area ROUTES)

Area: `projects/chirality-app-dev/frontend/src/app/**` at frozen basis `00115c719`. These are the Next.js pages and API routes.
Output: `ROUTES_capabilities.csv` has 44 rows (`CAP-ROUTES-001` to `044`). Validator result: `RESULT PASS errors=0 warnings=0`.
No deliverable folders were read. The rows come from the route and page source, `REACHABILITY.csv`, `TOUCHED_PATHS.csv`, a scratchpad import-closure script, and grep over consumers and tests.

## 1. Census

CENSUS rows=44 LIVE=44 LEGACY_ONLY=0 TEST_ONLY=0 UNREACHED=0 ENABLED=41 DISABLED=3

- Every route handler and page is a product entry point, so every row is `REACH=LIVE`. `workflow/workflow-read-contract.ts` is a TYPE-ONLY module that `workflow-store.ts` imports with `import type`. The pack gives it no static reach, so it is tagged `REACH=LIVE` with `TYPE-ONLY` (brief rule). No row carries the Addendum 1 item 4 `UNREACHED` marking.
- DISABLED rows:
  - 025: the provider-network consent route is a retained no-op.
  - 042: the pipeline/workbench deep links. `defaultSurface` is ignored.
  - 043: the legacy loop shells passed as the `legacy` prop, which is discarded.
- `PostReleaseBasis` is `NO` on all rows:
  - `TOUCHED_PATHS.csv` has no path under `frontend/**`.
  - The daemon-backed routes do reach `@chirality/runtime-client` through the runtime-client daemon port, and `da95ec194` touched `packages/client/src/client.ts`. The touched lines (50–54 and 363–383) are the application-tool methods only.
  - No App module references `ApplicationTool*` or `applicationTools` (grep over `src/` and `electron/`).

## 2. Granularity rationale

- API routes are grouped by behavior, not by file. For example:
  - steer and steer-receipt share one row;
  - the requests list and the answer share one row;
  - native-plan capability and revisions share one row;
  - methods list and inspect share one row;
  - hosted sign-in start, cancel and sign-out share one row.
- `session/[id]/route.ts` is split into GET (read) and DELETE (delete). The two differ in reach: DELETE has no renderer caller.
- Every row names its backend, because the backend decides reach:
  - **Daemon port** (`lib/runtime-client/daemon-harness-port`, `getDaemonHarnessPort`): rows 001–021. All `/api/harness/**` session, turn, request, permission, roster, method, native-plan and scaffold routes go through the Runtime daemon over `RuntimeClient`.
  - **Hosted bootstrap port** (`getHostedBootstrapPort`): rows 022–025.
  - **No route imports the legacy in-process harness.** The legacy engine appears only in the route tests, through `fake-daemon-harness-port.ts`.
  - **In-process** (no daemon): the `/api/working-root/**` and `/api/project/**` routes.
    - `lib/workspace` backs the tree, deliverables, scope, content, status, transition and dependencies routes.
    - `lib/harness/session-manager` backs the validate route.
    - Route-local `file-policy.ts` and `workflow-store.ts` back the file and workflow routes.
    - The workflow-drafts route calls `@chirality/runtime-core` in process.
- The pages have four rows: 041 (`/` and `/chat`), 042 (`/pipeline` and `/workbench`), 043 (the retained legacy-shell contract) and 044 (not-found). The layout and `globals.css` each have their own row.
- `file-policy.ts` has two rows:
  - 034: HTTP preview.
  - 035: the Electron native document-handoff policy. Electron `main.ts` imports it directly; it is not a route.
- Row 038 records the three coexisting error-envelope conventions as one contract surface.
- Rows 041 and 043 carry the page-row check requested by the brief: `WovenDialogueRoute` discards `legacy` at `components/woven-dialogue/woven-dialogue-route.tsx:18` (`void legacy`). Verified.
  - **Additional finding:** `WovenDialogueShell(_props)` also ignores `defaultSurface` (`woven-dialogue-shell.tsx:77`). The shell never reads it.
  - So `/pipeline` and `/workbench` render the same dialogue surface as `/`.
  - The two page tests mock the shell, so they cannot detect this.

## 3. Files covered versus total

COVERAGE covered=58 total=58

Every file in the `Area=ROUTES` list is named in at least one row's `Paths`, including `globals.css` (row 040). No file is uncovered.

## 4. Dead, unreached, disabled or retired code observed

Rendered reach was checked by computing the import closure from `WovenDialogueShell`, `app/layout.tsx` and `app/not-found.tsx` (scratchpad script). The static pack marks everything imported by a page as LIVE, including the discarded legacy shells. The findings below go beyond that static view.

- **Legacy prop discarded (row 043):** `LoopShell`, `PortalLoopShell` and `LoopTertiaryShell` are imported by the four pages but never rendered (`woven-dialogue-route.tsx:18`). This keeps `pipeline-surface.tsx`, `workbench-surface.tsx`, `agent-matrix.tsx` and `tertiary-sidebar-tabs.tsx` statically LIVE but unrendered.
- **Routes with no rendered consumer.** Each handler works; the callers sit only in unrendered or test-only UI.
  - `scaffold` (row 021): the only caller is `pipeline-surface`.
  - `working-root/scope` (row 029): the only caller is `workbench-surface`. No test covers the route or `scanProjectScopes`.
  - `deliverable/status`, `status/transition` and `dependencies` (rows 031–033): the callers go through `lib/workspace/deliverable-api.ts` from the pipeline and workbench surfaces. No `src/` caller issues `PUT` to the dependencies route.
  - `working-root/workflow` (row 036): the only caller is `components/woven-dialogue/workflows-view.tsx`, which the pack marks `TEST_ONLY`.
  - `DELETE /api/harness/session/[id]` (row 004): no `src/` or `electron/` caller. Renderer chat deletion is local organization state (`chatDeleted`).
  - `hosted-bootstrap/provider-network-consent` (row 025): a retained no-op under D-GOV-43, with no caller.
- **Stale comments and text:**
  - The `session/[id]/events` header still describes `events.jsonl` and `replayHarnessEvents`, but the handler calls the daemon `replaySession`.
  - The layout `metadata.description` still names PORTAL/PIPELINE/WORKBENCH.
  - `not-found.tsx` renders the older `AppShell`, not the woven shell.
- **Duplication:** `requireNonEmptyString` is re-implemented locally in the dependencies and transition routes; `lib/harness/http` already has one.
- **Test caveat:** the `/api/harness` route tests inject `fake-daemon-harness-port.ts`, which composes the legacy in-process runtime. Those tests check the route contract, not Runtime daemon behavior. `v3-runtime-proxy.integration.test.ts` covers the real `RuntimeClient` transport for a subset of routes.

## 5. Method friction with §5.2, and proposed revision

- **Static reach overstates pages.** Page-level static reach cannot express "imported but discarded". Everything reached through a `legacy` prop reads as LIVE, and so do the API routes whose only callers sit under it. I carried this in `STATE` and a `NO RENDERED CONSUMER` note.
  - Proposal: add a `RENDER=MOUNTED|UNMOUNTED` note tag, or have `reachability.py` treat `legacy={...}` JSX props of `WovenDialogueRoute` as non-edges. A `CONSUMER=NONE` tag for routes would also help.
- **STATE is ambiguous for endpoints.** It is unclear whether STATE applies to the endpoint or to the user-visible behavior. I used `STATE=ENABLED (endpoint)` where the handler works but no mounted UI calls it, and `DISABLED` only where the code itself switches the behavior off.
  - Proposal: say explicitly that STATE is judged at the capability's own boundary, and that consumer absence is recorded separately.
- **EntryPoints for routes:** I listed HTTP verbs plus client symbols and consumer paths. A `METHOD path` convention (e.g. `POST /api/harness/turn`) would be clearer.
- **PostReleaseBasis across package boundaries:** the brief does not say whether a route "relies on" a touched runtime-client file whose touched lines it never calls. I answered `NO` from a symbol-level check.
  - Proposal: judge at symbol level and cite the check in the notes.

## 6. Effort

- Files read: all 58 area files, fully except `globals.css` (header only). Also read: `woven-dialogue-route.tsx`, parts of both runtime-client port files, test headers, and the validator.
- Consumer and test maps came from grep plus a scratchpad import-closure script.
- The context budget was comfortable, not tight.
