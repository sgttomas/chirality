# HARNESS capability inventory — notes (R0 calibration, unit S-H)

Area: `projects/chirality-app-dev/frontend/src/lib/harness/**` at frozen basis `00115c719`.
Output: `HARNESS_capabilities.csv`, 60 rows (`CAP-HARNESS-001`…`060`). Validator: `RESULT PASS errors=0 warnings=0`.
No deliverable folders were read. The inventory comes from code, the import graph and test imports.

## 1. Granularity rationale

- One row per behavior or contract surface that a deliverable could own. Examples: turn streaming, working-root admission, the permission broker, managed delegation.
- Parallel implementations of one behavior share a row. For example, `method-selection-client.ts` and the `listHarness*`/`inspectHarness*` functions in `client.ts` call the same routes.
- `client.ts` (567 lines, about 25 exported calls) is split into seven rows by user-visible function: session lifecycle, turn streaming, steering, server requests, permission decisions, replay, and personas.
- `mcp/read-tools.ts` is split into read tools, mutating tools and domain tools, because different deliverables plausibly own them.
- Small helper modules are folded into the capability they serve: `event-factory`, `sanitize`, `options`, `tool-pool` and `pi-event-mapper`.
- Rows are ordered in two blocks:
  - 001–027: surfaces reached from production code (renderer components, Next.js API routes, Electron).
  - 028–060: the legacy in-process engine cluster (see §3).
- The count reached the 60-row ceiling. That is a sign the area mixes two layers (§3); splitting it into two areas would bring each nearer 25–35 rows.

## 2. Files covered versus total

- Total files in the area: **64**. There are 58 top-level `.ts`/`.tsx` files and 6 under `mcp/`. One file is `.tsx`.
- Files named in at least one row's `Paths`: **64 of 64**.
- `PostReleaseBasis` is `NO` on every row. `git show --stat` of `da95ec194`, `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a` shows that none of them touches `frontend/src/lib/harness/**`.
  - Three touch only `projects/chirality-runtime/**`.
  - `ccb95e06a` touches `exports/`, `frontend/electron`, a tranche manifest and a CI action.

## 3. Dead or unreferenced code observed

The import graph was computed over `frontend/{src,electron,scripts}`, excluding `__tests__`.

- **Legacy in-process engine cluster (40 of 64 files).** No importer in `src/` or `electron/` outside `lib/harness`.
  - It is reachable only through:
    - `scripts/controlled-ci-runtime.ts`, which uses `StubAgentSdkManager` and `LegacyAgentEngineAdapter` for the CI Runtime fixture;
    - `scripts/run-pec-bridge-rehearsal.ts`;
    - `scripts/run-dapp52-live-llm-demo.ts`;
    - tests.
  - The cluster:
    - `runtime.ts`, `turn-engine.ts`, `engine-registry.ts`, `agent-sdk-manager.ts`, `anthropic-agent-sdk-manager.ts`, `claude-agent-sdk-manager.ts`, `sdk-options-builder.ts`, `sdk-message-mapper.ts`, `scripted-agent-sdk-proof.ts`;
    - `pi-*`, `omlx-provider-config.ts`, `options.ts`, `attachment-resolver.ts`, `persona-manager.ts`;
    - `permission-{broker,event-channel,overlay}.ts`, `tool-*`, `chirality-hooks.ts`, `chirality-tool-bridge.ts`, `claude-tool-binder.ts`;
    - `event-factory.ts`, `harness-ui-bridge.ts`, `managed-delegation.ts`, `subagent-*`, `agent-runtime-contract.ts`, `runtime-fingerprint.ts`;
    - all of `mcp/`.
  - Production API routes go through `lib/runtime-client/daemon-harness-port` instead.
  - `__tests__/api/harness/fake-daemon-harness-port.ts` composes this legacy runtime as a test double for the daemon port. Route tests therefore still exercise it.
- **No importer except tests:** `claude-tool-binder.ts`.
- **Only importer is a test fake:** `runtime-fingerprint.ts`.
- **Reachable only as types from production:**
  - `scaffold.ts`: the scaffold route imports only `CoordinationMode` and delegates execution to the daemon port. Its execution code is reached only through `mcp/read-tools.ts`, which is legacy.
  - `agent-roster.ts` and `session-events.ts`: `client.ts` imports types only.
- **Partially live:**
  - `session-manager.ts`: production uses only `assertProjectRootAccessible`, from the working-root routes. `FileSessionManager` is legacy.
  - `api-key-store.ts`: live only through `run-logger` redaction, imported by `lib/woven-dialogue/chat-organization.ts`.
- **No direct test import:**
  - `session-boot-readiness.ts`, `workflow-feedback.ts`, `scripted-agent-sdk-proof.ts`: no test found.
  - `tool-path-policy.ts`, `tool-shell-policy.ts`: exercised only indirectly, through the hooks and overlay tests.
  - `workflow-drafts.ts`: covered through component and route tests.
- **Duplicate client surfaces:** `client.ts` (`listHarnessRoles`, `listHarnessMethods`, `inspectHarnessMethod`, `resolveHarnessSelectedContext`, `replaceHarnessSelectedMethods`, native-plan functions) duplicates `method-selection-client.ts`. Production components import the latter.

## 4. Method friction with §5

- **No field for reachability.** A large share of this area is legacy code reachable only from scripts and tests. §5 has no field for that, so the rows carry the prefix `LEGACY-IN-PROCESS:` in `Notes`.
  - Proposal: add an optional `Reachability` column with values `PRODUCTION`, `SCRIPT_ONLY`, `TEST_ONLY` and `TYPE_ONLY`. Without it, forward-pass workers may treat legacy engine rows as live App behavior.
- **`CoveringTests` has no convention for "no test found".** I used `NONE_FOUND`, mirroring the ledger vocabulary. I also listed indirect coverage without marking it as indirect; that is mentioned only in `Notes`.
  - Proposal: allow a `(indirect)` suffix.
- **Test files are not only `*.test.*`.** `__tests__/api/harness/fake-daemon-harness-port.ts` is a helper module under `__tests__`, and it is the only importer of `runtime-fingerprint.ts`. I listed it as covering test support.
- **`EntryPoints` is loosely defined.** I mixed exported symbols with repo-relative consumer paths, and used one glob (`app/api/harness/**`) for `http.ts`, which 35 routes import.
  - Proposal: define `EntryPoints` as exported symbols only, and add consumers in a separate column or in `Notes`.
- **The 20–60 row target is tight here.** The area mixes a thin live renderer/route layer with a large legacy engine. The per-behavior rule landed exactly on 60 rows.
  - Proposal: allow a sub-area split, such as `HARNESS` and `HARNESS_LEGACY`, when reachability divides an area.
- **`PostReleaseBasis` was cheap to settle** for this area, because none of the four commits touches it. A path-scope precheck in the manager brief would save each worker the `git show`.
- **Suggested CauseTags in `Notes`.** Some rows name a candidate CauseTag, such as `CODEX_SOLE_ENGINE` or `NATIVE_DELEGATION`. These are hints for forward workers, not dispositions.

## 5. Effort

- Files read, partially or by grep: about 30 harness files through export and comment greps. About 10 files were read in line ranges. Several route and script headers and the validator were also inspected.
- The import graph and test map were computed with a scratchpad script, not by reading.
- Context was comfortable, not tight.
