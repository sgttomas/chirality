# HARNESS capability inventory: R2 tag pass notes (unit HARNESS-TAG)

Area: `projects/chirality-app-dev/frontend/src/lib/harness/**` at frozen basis `00115c719`.
Input: `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` (60 rows, not edited).
Output: `R2/SURFACES/HARNESS_capabilities.csv`. It has the same header, the same 60 rows, IDs and order.
The R0 `Notes` text is kept, and the tags are appended after ` | `.
Validator: `RESULT PASS errors=0 warnings=0`.

## 1. Census

CENSUS rows=60 LIVE=27 LEGACY_ONLY=31 TEST_ONLY=2 UNREACHED=0 ENABLED=25 DISABLED=35

- **LIVE (27):**
  - 001–006, 008–021 and 023–027: all `STATE=ENABLED`.
  - 022 and 036: `STATE=DISABLED`.
- **LEGACY_ONLY (31):**
  - 028–035 and 037–059, all `STATE=DISABLED`.
  - None of these modules is composed in the product. Every `/api/harness/**` route delegates to `lib/runtime-client/daemon-harness-port`.
- **TEST_ONLY (2):** 007 and 060, both `STATE=DISABLED`.
- **UNREACHED (0):** `REACHABILITY.csv` has no UNREACHED module in this area.

### Method

**Reach is tagged per capability, at symbol level where the pack's module-level class is misleading.** A capability that spans paths is tagged by its live path, and the other paths' reach is named. The same convention is used in the ELECTRON, RTCONTRACT and RTCORE rows.

**`STATE` was decided from the rendered tree, not only from static reach.** Every page passes its legacy shell as the `legacy` prop, and `woven-dialogue-route.tsx:18` discards it (`void legacy`).
- I recomputed reach from the pack's own graph code (scratchpad script), cutting the page-level edges to `loop-shell`, `portal-loop-shell` and `loop-tertiary-shell`.
- `ChatPanel` stays rendered: `woven-dialogue-shell.tsx:855` mounts it with `presentation="woven"`. It also renders inside the 404 `AppShell`.
- The only HARNESS-imported renderer module that drops out of the rendered set is `components/pipeline/pipeline-surface.tsx`, which is the caller of 022.
- Among production importers of HARNESS modules, `session-list-view.tsx` renders only on the 404 route and `agent-matrix.tsx` is not rendered. Every symbol they import also has a woven caller.

## 2. Coverage

COVERAGE covered=64 total=64

Every file listed for Area=HARNESS in `R1_INVENTORY/IMPLEMENTATION_SURFACES.csv` is named in at least one row's `Paths`. None is uncovered.

## 3. Substance changes

none

- No cell other than `Notes` changed.
- Every `Paths`, `EntryPoints` and `CoveringTests` path exists at the frozen basis.
- Every symbol in `EntryPoints` is exported by the row's `Paths`.
- `PostReleaseBasis` stays `NO` on all rows: `TOUCHED_PATHS.csv` has no path under `projects/chirality-app-dev/frontend/`.
- Two small inaccuracies in R0 text were left as written and stated precisely in the appended tags:
  - 023: R0 says "Imported by 35 route files". The importers are 34 route files (33 under `app/api/harness`, plus `app/api/working-root/validate/route.ts`) and one helper, `app/api/harness/hosted-bootstrap/request.ts`.
  - 016: `bindHostedBootstrapProject` has no direct caller. It is reached through `hydrateHostedBootstrapProject` (`hosted-bootstrap-client.ts:127`).

## 4. Tags that contradict the R0 note, the R0 §3 reading, or the pack

| Row | R0 reading | R2 tag | Evidence |
|---|---|---|---|
| 007 | In the "reached from production code" block, with no legacy prefix | `REACH=TEST_ONLY; STATE=DISABLED` | `listDirectChatPersonas` has no production caller: `persona-picker.tsx:8` uses `listRoles` and mentions `listDirectChatPersonas` only in a comment at :20. The `agent-roster.ts` functions have no non-test caller. The module is LEGACY_ONLY only through its persona constants. |
| 022 | Production block | `REACH=LIVE; STATE=DISABLED` | The only renderer caller is `pipeline-surface.tsx`, and it renders only inside `LoopTertiaryShell`, which is discarded at `woven-dialogue-route.tsx:18`. |
| 036 | Production block ("reached through run-logger redaction") | `REACH=LIVE; STATE=DISABLED` | `electron/api-key-storage.ts` sets the globals, but it is never invoked (CAP-ELECTRON-034). The engine-side getters are LEGACY_ONLY. `getProviderApiKey` and `hasProviderApiKey` are TEST_ONLY. |
| 029 | No `LEGACY-IN-PROCESS:` prefix (R0 §3 lists these files in the legacy cluster) | `REACH=LEGACY_ONLY` | Not composed by the App. Its importers are `runtime.ts` and the CI fixture `scripts/controlled-ci-runtime.ts:15-16`. |
| 037 | Legacy (agrees) | `REACH=LEGACY_ONLY` at symbol level | The pack marks `session-manager.ts` LIVE through `assertProjectRootAccessible` (that is CAP-026). `FileSessionManager` is imported only by `runtime.ts`. |
| 052 | Legacy (agrees) | `REACH=LEGACY_ONLY` | **The pack is wrong here.** It marks `scaffold.ts` and `sanitize.ts` LIVE through `app/api/harness/scaffold/route.ts`. But `route.ts:3` imports only the type `CoordinationMode`, without the `type` keyword, and uses it only at :10, so the import is elided at compile. The static regex cannot see this. |
| 060 | `LEGACY-IN-PROCESS:` | `REACH=TEST_ONLY` | There is no non-test importer. The only importer is `__tests__/api/harness/fake-daemon-harness-port.ts`. The pack says LEGACY_ONLY only because the R0 row is a seed. |
| 049 (partial) | `LEGACY-IN-PROCESS:` | `REACH=LEGACY_ONLY`, with `claude-tool-binder.ts` TEST_ONLY | Same seed effect as 060. R0 already notes that it has no importer except tests. |

**Other observations**
- R0 §1 puts 001–027 in a "reached from production code" block. That holds statically, but 007 and 022 are not product-effective.
- R0 §3 names three duplicate client surfaces in `client.ts`: `listHarness*`/`inspectHarness*`, `replace`/`resolveHarness*`, and the native-plan functions. They have **no** production caller at all; they are TEST_ONLY at symbol level. The tags on 008–010 say so.
- R0 §3 says the legacy cluster is reachable only through `scripts/controlled-ci-runtime.ts`, `run-pec-bridge-rehearsal.ts`, `run-dapp52-live-llm-demo.ts` and tests. A BFS from `frontend/scripts/**` confirms this.

## 5. Method friction

- **The LEGACY_ONLY class in `REACHABILITY.csv` is self-seeded.** For every seed in this area, the pack's `EntryPoint` is the module itself, so the pack cannot tell a legacy module that something uses from one that nothing uses (060, `claude-tool-binder.ts`). Checking this needed a separate importer scan.
  - Proposal: in the pack, give each seed its non-seed importers, or the scripts that reach it, as the chain.
- **The static reach misses unmarked type-only imports** (`import { T }` of a type under `isolatedModules`). That gave a false LIVE on 052.
  - Proposal: have `reachability.py` resolve whether each imported name is a type in the target module, or flag imports whose names are all `export type` in the target.
- **Module-level reach against symbol-level capabilities.** `client.ts`, `session-manager.ts` and `api-key-store.ts` each mix live, legacy and test-only symbols.
  - Proposal: state in §5.2 that `REACH` is judged at the level of the capability's own symbols, citing the pack's module class when they differ. Siblings already do this.
- **Rendered versus static reach** needs a cut list: the discarded `legacy` props and the 404-only `AppShell`.
  - Proposal: the pack could ship a second column, `Rendered=YES|NO`, computed with those page edges cut.
- **`CoveringTests` on 045 and 046 are indirect** (hooks and overlay tests), but R0 lists them without the ` (indirect)` suffix. The brief forbids non-substantive cell edits, so I left them unchanged.

## 6. Effort

- I read or grepped about 25 source files in line ranges: pages, `woven-dialogue-route`, `app-shell`, `chat-panel` gates, `api-key-store`, `run-logger`, the scaffold route, the permission route, `hosted-bootstrap-client`, `agent-roster` and `persona-picker`.
- Import, rendered-reach and test maps came from scratchpad scripts that reuse `R2/_scripts/reachability.py` functions.
- I read sibling R2 capability rows for tag conventions and cross-references (ELECTRON, SETTINGS, SHELL, WORKSPACE, RTCONTRACT, BUILD).
- The context budget was comfortable.
