# RTCORE capability inventory: notes (R1b, run RUN_D128_CONCORDANCE_2026-09-21_1614Z)

Area: `projects/chirality-runtime/packages/{core,cli,daemon}/**` at frozen basis `00115c719`. The file list is the 56 `Area=RTCORE` rows of `R1_INVENTORY/IMPLEMENTATION_SURFACES.csv`.
Output: `RTCORE_capabilities.csv`, 50 rows (`CAP-RTCORE-001` to `050`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders and nothing under `projects/chirality-runtime/execution/**` were read. The inventory was built from code, a value-import graph, a symbol-level map from tests to modules, and the evidence pack.

## 1. Census

CENSUS rows=50 LIVE=46 LEGACY_ONLY=1 TEST_ONLY=3 UNREACHED=2 ENABLED=39 DISABLED=11

- The rows marked `UNREACHED` are:
  - 048: the compatibility session policy. Its row is `REACH=LEGACY_ONLY`.
  - 050: the package-surface row. It is tagged LIVE because of its live barrel, and its Notes name `daemon/src/hosted.ts` as `LEGACY_ONLY UNREACHED`.
- The TEST_ONLY rows are:
  - 014: signal-shutdown;
  - 046: physical-filesystem;
  - 047: process-supervisor with descendant-tracker.
- Mixed-reach rows are tagged by their live path. The Notes then name the other file's reach:
  - 024: `agent1-run-coordinator.ts` is TEST_ONLY;
  - 042: `native-role-config.ts` is TEST_ONLY;
  - 049: `cli/src/index.ts` is TEST_ONLY;
  - 050: `daemon/src/index.ts` is TEST_ONLY.
- `PostReleaseBasis=YES` on 5 rows: 002, 028, 029, 030 and 033.

## 2. Granularity rationale

- One row per Runtime behavior or contract surface that a deliverable could own. Most rows are one HTTP route family plus the service code behind it, for example hosted-bootstrap account routes, turn registry/SSE, server requests, steering, native Plan, application tools and method selection.
- The large files are split by behavior, not by file:
  - `runtime-daemon.ts` (1460 lines) appears in about 20 rows, one per route family.
  - `codex-supervisor.ts` has four rows: thread/turn lifecycle, notification pass-through, server requests and application tools.
  - `session-store.ts` has five rows: records, journal/replay, settlement, selection and provider span.
- Composition-disabled surfaces get their own row, so that forward workers do not read them as live behavior. These are residency/models, credentials, scaffold, Agent 1 runs, runtime tools and the provider-span successor.
- Helper modules fold into the behavior they serve:
  - `engine-registry` goes into 003.
  - `retirement-failure` goes into 013.
  - `role-policy` stays separate, because it binds evidence.
  - `method-transition` goes into 037.
  - `runtime-attachment-resolver` and `attachment-copy` go into 026.
- The package barrels, manifests and configs share one row (050).

## 3. Files covered versus total

COVERAGE covered=56 total=56

- Every file in the area list, including `package.json`, `tsconfig.json` and `vitest.config.ts`, is named in at least one row's `Paths`.
- Config files are listed only in 049 and 050.

## 4. Dead, unreached, disabled or retired code observed

The static reach map was confirmed with a value-import scan in the scratchpad. It covers `packages/{core,daemon,cli}/src`, the App importers of `@chirality/runtime-{core,daemon,cli}`, and `frontend/scripts/build-electron.mjs`.

**The evidence pack over-reports core.**
- `REACHABILITY.csv` marks every `core/src/*` module LIVE through the chain `electron/main.ts > electron/attachment-picker.ts > core/src/index.ts`, because `export *` makes every re-exported module a reach edge.
- The only live consumers of core values are:
  - `electron/attachment-picker.ts`, for the attachment-copy functions;
  - `app/api/working-root/workflow-drafts/workflow-draft-store.ts`, for `discoverMethodCatalog` and `inspectMethod`;
  - the daemon: `app-owned-composition.ts`, `runtime-daemon.ts` and `codex-supervisor.ts`.
- Following value imports from those symbols, these modules are reached **only through the barrel**:
  - `agent1-run-coordinator.ts`: only `tests/agent1-run.test.ts` uses `GovernedAgent1RunCoordinator`.
  - `process-supervisor.ts` and `descendant-tracker.ts`: tests only.
  - `native-role-config.ts`: tests only.
  - `compatibility-session-policy.ts`: no importer anywhere, including tests. It is written up as `LEGACY_ONLY UNREACHED`, because it selects claude-agent-sdk/Anthropic adapters from `CHIRALITY_HARNESS_PROVIDER`.
- Pack rows that agree with the code:
  - `physical-filesystem.ts` is TEST_ONLY. `build-electron.mjs` defines an alias for its subpath, but nothing imports it.
  - `daemon/src/signal-shutdown.ts` is TEST_ONLY.
  - `daemon/src/index.ts` and `cli/src/index.ts` are TEST_ONLY; the App integration test imports them.
  - `daemon/src/hosted.ts` is UNREACHED. It is documented as the Electron surface, but nothing imports it.

**Disabled by the App-owned composition** (`app-owned-composition.ts`). The routes stay mounted but fail by design:
- Residency and models: control stubs at lines 180-181 throw `ENGINE_UNAVAILABLE`.
- Credentials: the store at line 225 reports `configured:false`, and set/remove throw.
- Scaffold: no port is supplied, so `runtime-service.ts:621` returns 501.
- Agent 1 runs: no port is supplied, so `runtime-service.ts:664-670` returns `REQUIRED_DELEGATION_MISSING`.
- Provider-network consent: a no-op that returns status unchanged (`hosted-bootstrap.ts:55-58`).

**Computed but not delivered for Codex:**
- Chirality runtime tools are computed at `turn-coordinator.ts:193-199`, but `DelegatedRuntime.turn` discards them (`delegated-runtime.ts:289`, `_runtimeTools`), and `runtimeControlTools` is false.
- The provider-span context successor is never used, because the delegated adapter has no `prepareContextSuccessor`.
- The engine boot-turn branch (`runtime-service.ts:348-557`) is never used, because the Codex adapter has `boot: "none"`.
- The local omlx residency admission in `turn-coordinator.ts` is never used.

**Dead methods:**
- `AuthRegistry.registerMemoryAccountHost`, `authenticateMemoryAccountHost`, `revokeMemoryAccountHost` and `revokeAllMemoryAccountHosts` have no caller.
- `CodexAppServerClient` is used only inside its module and by its test.

**Application tools:**
- They are composed and enabled in the Runtime, behind the App-host principal only.
- No App frontend or Electron code registers or polls them at the frozen basis. The only App-side touch is `packages/client/src/client.ts`, which is outside this area.

**PostReleaseBasis:**
- Every touched range in RTCORE comes from `da95ec194` (application tools), except `codex-supervisor.ts:677-691`, which comes from `cb08dbe2f`.
- `session-store.ts` (6-8, 128-158) and `runtime-daemon.ts` (15-16, 57, 169-171, 660-686) are touched only in application-tool code, so their other rows are `NO`.
- The touched lines in `codex-supervisor.ts` are application-tool guards, but they sit inside `acquire`, `interrupt`, `close`, `handleNotification`, `handleExit` and `handleServerRequest`. The three supervisor rows that rely on those methods (028, 029 and 030) are therefore `YES`, and a Notes line lists the specific lines.

## 5. Method friction with §5.2

- **Barrel re-exports inflate reach.** The pack counts `export *` in `core/src/index.ts` as a reach edge. As a result, test-only and unreferenced core modules appear LIVE. Confirming this needed a symbol-level import check.
  - Proposal: in `reachability.py`, resolve named value imports through barrels to their defining module, and emit `LIVE(barrel-only)` when a module is reached only by `export *`.
- **STATE for unwired modules is ambiguous.** A TEST_ONLY module has no flag. I used `STATE=DISABLED (not composed)`.
  - Proposal: state that `STATE` means "active in the product composition at the frozen basis", so unwired modules are `DISABLED` by definition.
- **"Relies on" is vague for PostReleaseBasis.** A capability can depend on a function that contains touched lines serving a different feature, like the supervisor rows here.
  - Proposal: allow `YES(incidental)` as a value, or require a Notes citation of the touched lines whenever the touched code serves another capability.
- **EntryPoints for HTTP routes.** Route paths are not symbols or file paths, so I kept them in `Capability`.
  - Proposal: permit `ROUTE:<METHOD> <path>` tokens in `EntryPoints`.
- **Target 20-60 rows.** The count reached 50 because disabled-by-composition surfaces get their own rows. That seems right for concordance, since deliverables may claim those surfaces.

## 6. Effort

- Files read: 26 Runtime source files, some in line ranges and some through signature or JSDoc greps. The largest were `runtime-daemon.ts`, `app-owned-composition.ts` (in full), `codex-supervisor.ts`, `runtime-service.ts` and `session-store.ts`.
- Also inspected by grep: 5 App importers, `build-electron.mjs`, and the Runtime test directory.
- The value-import graph and the symbol-to-test map came from scratchpad scripts.
- Context was moderate, not tight.
