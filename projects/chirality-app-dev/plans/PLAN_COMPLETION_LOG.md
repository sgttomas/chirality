# Runtime Plan Completion Log

This log preserves landed-tranche narrative for the active runtime completion plan, currently `plans/PLAN_2026-06-13_runtime_completion.md`.

This file is history, not authority. Project truth remains in governed docs, decomposition and deliverable artifacts, source, tests, evidence records, and git history. Nothing here is a lifecycle decision, release-readiness claim, professional approval, certification, sealing, authentication, or code-compliance acceptance.

---

## 2026-06-15 - R4 Bash prerequisites and controlled Bash implementation landed (`BASH-R4-001`)

Landed bounded SDK `Bash` exposure for the opt-in first-adapter path. Bash is model-visible
only when requested in `workspaceWrite` mode after descriptor resolution, permission overlay
resolution, `canUseTool`, and Chirality `PreToolUse` hook checks pass. `readOnly`,
`dontAsk`, ordinary `ask`, and `bypass` continue to keep Bash out of the allowed model tool
set or deny execution through the SDK callback path.

The tranche added a conservative shell policy layer for Bash: default timeout injection
(`120000` ms), maximum timeout enforcement, no background execution, no sandbox override,
static no-network command/URL denial, obvious project-root path containment, instruction-root
blocking, and symlink rejection for redirection targets. Bash hook evidence records safe
metadata only. `PostToolUse` records stdout/stderr byte counts separately and spills
redacted overflow results to session-local tool artifacts when descriptor budgets require it.
Raw commands, stdout, stderr, API keys, and full output bodies are not stored in
`HarnessEvent.data`.

SDK message mapping now treats Bash built-in results as governed tool lifecycle evidence, so
scripted Bash results produce inferred `tool.started` and `tool.completed` / `tool.failed`
records with result-budget and stdout/stderr metadata. Runtime contract docs now describe the
approved Bash boundary.

Residual: governed SDK subagents, concrete provider expansion, provider/network broadening,
remote MCP/plugins, Pi implementation paths, `MultiEdit`, mutating Chirality MCP tools, full
read/write artifact storage, package/runtime migration, desktop-wrapper changes, packaged
SDK subprocess proof, release-readiness claims, lifecycle issuance, professional approval,
certification, sealing, authentication, and code-compliance acceptance remain out of scope or
future/human-gated. Normal instruction-root integrity remains blocked by the pre-existing
split source-root/package-resource posture.

Validation: `npm run test -- permission-overlay chirality-hooks tool-descriptor
sdk-options-builder sdk-message-mapper`; `npm run test` (43 files, 329 tests);
`npm run typecheck`; `CHIRALITY_INSTRUCTION_ROOT=/tmp/chirality-instruction-root.LMAekD
npm run harness:validate:premerge` against a local `next dev` server using a temporary
merged instruction root, producing pass status with 8 checks at
`frontend/artifacts/harness/section8/latest/summary.json`;
`CHIRALITY_INSTRUCTION_ROOT=/tmp/chirality-instruction-root.LMAekD npm run
proof:network-policy -- --runs 1 --idle-seconds 1 --idle-sample-seconds 1 --output-dir
/tmp/chirality-network-proof-bash-20260615023318`, producing `PASS` after temporarily
creating and then removing the script's missing `examples/example-project` fixture;
tranche-scoped `git diff --check` passed. `npm run instruction-root:integrity` was attempted
and failed because the nested app-dev source root lacks `agents/`. `node
./scripts/verify-instruction-root-integrity.mjs --source-root
/Users/ryan/ai-env/projects/chirality` was attempted and failed because the root source lacks
current app-dev governance docs such as `docs/DIRECTIVE.md`.

## 2026-06-15 - D-APP-04 ruled Option A

Human project authority approved `D-APP-04` Option A. A bounded R4 Bash tranche may now
proceed after `WRITE-HOOKS-001`.

The approved next implementation lane is Bash prerequisites and controlled Bash
implementation: descriptor exposure, permission/mode mapping, timeout behavior,
stdout/stderr capture, interrupt handling, result budgeting/storage, hook enforcement,
safe audit events, redaction checks, and required documentation/tests. Model-visible Bash
exposure is allowed only after tranche validation passes and closeout records the
evidence.

This ruling does not approve governed SDK subagent execution, concrete non-Anthropic
provider implementation or routing, provider/network broadening, remote MCP/plugins, Pi
adapter/fork/import/sidecar/runtime-floor/spike work, release-readiness claims, lifecycle
issuance, professional approval, certification, sealing, authentication, or code-compliance
acceptance.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, or release-readiness posture changed in the
ruling-record tranche.

Validation: docs/control-plane static checks only. Frontend runtime tests were skipped
because this tranche only recorded the human ruling and updated the decision register,
active plan, and completion log.

## 2026-06-15 - Post-write runtime capability decision packet prepared (`D-APP-04`)

Prepared `D-APP-04` for the first blocked dependency-spine item after `WRITE-HOOKS-001`.
The packet asks the human authority to rule which post-write runtime capability lane, if
any, may proceed next: R4 Bash prerequisites and controlled Bash implementation, R5
governed SDK subagent runtime, concrete provider-expansion preparation, or holding all
capability expansion pending additional evidence.

The recommendation is Option A only as a bounded R4 tranche, with Bash denied by default
and model-visible exposure allowed only after descriptor, permission, hook, timeout,
interrupt, result-budget, result-storage, audit-event, redaction, harness, and relevant
network checks pass. Governed subagents and concrete non-Anthropic providers remain
deferred unless the human ruling explicitly selects them. D-APP-01 and D-APP-02 continue
to rule out Pi adapter, fork, import, sidecar, runtime-floor migration, and spike work.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, or release-readiness posture changed.
`execution/_Coordination/_DECISIONS/_REGISTER.md` now records `D-APP-04` as
`AWAITING_RULING`; implementation remains blocked until a ruling record lands.

Validation: docs/control-plane static checks only. Frontend runtime tests were skipped
because this tranche changed only the decision packet, decision register, active plan, and
completion log.

## 2026-06-15 - Write/edit hooks and path containment landed (`WRITE-HOOKS-001`)

Added bounded SDK `Write` / `Edit` exposure for `workspaceWrite` mode behind Chirality-owned descriptor resolution, permission overlay decisions, and programmatic SDK hooks.

The tranche introduced a shared tool path policy helper that enforces project-root containment, instruction-root write blocking, symlink write rejection, and fail-closed behavior when the active project root cannot be checked. The SDK options builder now maps `workspaceWrite` to first-adapter `acceptEdits`, attaches Chirality `PreToolUse`, `PostToolUse`, and `PostToolUseFailure` callbacks, and exposes requested `Write` / `Edit` only in `workspaceWrite`. `ask` still does not auto-execute writes; `readOnly` / `dontAsk` deny writes; bash, network, subagent, notebook, `MultiEdit`, Pi, concrete non-Anthropic providers, package/runtime migration, and mutating Chirality MCP tools remain out of scope.

Write hooks append provider-neutral hook evidence with safe path metadata, pre/post file state metadata, result-budget metadata, and diff-provenance flags. Raw file contents, raw tool outputs, full diffs, artifact spill files, and result artifact storage contracts remain future scope. SDK write tool results now produce the same inferred `tool.started` and `tool.completed` / `tool.failed` evidence pattern as read built-ins.

Validation: `npm run test -- permission-overlay chirality-hooks tool-descriptor sdk-options-builder sdk-message-mapper`; `npm run test`; `npm run typecheck`; `CHIRALITY_INSTRUCTION_ROOT=/tmp/chirality-instruction-root.VBn3xf npm run harness:validate:premerge` against a local `next dev` server using a temporary merged instruction root, producing pass status with 8 checks at `frontend/artifacts/harness/section8/latest/summary.json`. `npm run instruction-root:integrity` was attempted and failed because the nested app-dev source root lacks `agents/`. `node ./scripts/verify-instruction-root-integrity.mjs --source-root /Users/ryan/ai-env/projects/chirality` was attempted and failed because the root source lacks current required app-dev governance docs such as `docs/DIRECTIVE.md`.

## 2026-06-15 - Tool result and event evidence expansion landed (`TOOL-EVIDENCE-001`)

Added provider-neutral read-tool lifecycle evidence for the approved read surfaces: Claude Agent SDK read built-ins and read-only Chirality MCP tools.

The tranche introduced a small tool-evidence helper for safe input summaries, descriptor identity, result byte counts, MCP content item counts, descriptor inline/artifact budget limits, overflow policy, and budget classification. Raw tool output is not stored in `HarnessEvent.data`; this tranche does not add artifact spill files or result artifact storage contracts.

Permission callbacks now append `tool.permission` events with allow/deny/ask behavior, decision id, reason, descriptor identity, adapter tool name, mode, surface, and safe metadata. If permission audit persistence fails, the SDK permission callback fails closed by denying execution. Chirality MCP read handlers now append `tool.started`, then `tool.completed` with budget metadata or `tool.failed` with redacted error metadata, while returning the same MCP `CallToolResult` shape on success. SDK message mapping now keeps per-turn tool-use state so SDK read built-in `tool_use_result` messages produce inferred `tool.started` and then `tool.completed` or `tool.failed`; Chirality MCP completion/failure remains owned by the local MCP wrapper to avoid duplicate completion evidence.

Write, edit, bash, network, subagent, Pi, concrete non-Anthropic providers, package/runtime migration, artifact spill storage, and desktop-wrapper changes remain out of scope. Write/edit hooks and path containment is the next runtime-spine item. Normal instruction-root integrity remains blocked by the pre-existing split source-root/package-resource posture.

Validation: `npm run test -- permission-overlay chirality-read-mcp sdk-message-mapper engine-conformance session-events claude-agent-sdk-manager`; `npm run test`; `npm run typecheck`; `CHIRALITY_INSTRUCTION_ROOT=/tmp/chirality-instruction-root.Pt2xf2 npm run harness:validate:premerge` against a local `next dev` server using a temporary merged instruction root, producing pass status with 8 checks at `frontend/artifacts/harness/section8/latest/summary.json`. `npm run instruction-root:integrity` was attempted and failed because the nested app-dev source root lacks `agents/`. `node ./scripts/verify-instruction-root-integrity.mjs --source-root /Users/ryan/ai-env/projects/chirality` was attempted and failed because the root source lacks current required app-dev governance docs such as `docs/DIRECTIVE.md`. Global `git diff --check` is blocked by a pre-existing unrelated whitespace change in `projects/chirality-app-dev/init/init-prompt.md`; tranche-scoped `git diff --check` was run over touched files.

## 2026-06-14 - Read MCP / descriptor integration landed (`READ-MCP-DESCRIPTORS-001`)

Added Chirality-owned read-only MCP descriptors and in-process MCP handlers for status read, dependency read, scope scan, and scaffold preview.

The tranche extends the descriptor registry with `mcp__chirality__status_read`, `mcp__chirality__deps_read`, `mcp__chirality__scope_scan`, and `mcp__chirality__scaffold_preview`. The SDK options builder now attaches the in-process `chirality` MCP server only when one of those read MCP descriptors is explicitly requested and allowed. Unrequested MCP tools remain in descriptor-derived `disallowedTools`. Unknown tools still fail structurally before adapter streaming begins.

The MCP handlers reuse existing project-root-contained status, dependency, and scope readers. Scaffold preview now has a non-mutating `previewScaffoldExecutionRoot` path planner that computes scaffold directories/files from decomposition markdown without creating them. The mutating scaffold function reuses the same planner to preserve behavior while avoiding duplicate path construction.

Write, edit, bash, network, subagent, Pi, concrete non-Anthropic providers, package/runtime migration, and desktop-wrapper changes remain out of scope. Tool result and event evidence expansion is the next runtime-spine item. Normal instruction-root integrity remains blocked by the pre-existing split source-root/package-resource posture.

Validation: `npm run test -- chirality-read-mcp tool-descriptor sdk-options-builder harness-scaffold permission-overlay`; `npm run test`; `npm run typecheck`; `CHIRALITY_INSTRUCTION_ROOT=/tmp/chirality-instruction-root.CehMaI npm run harness:validate:premerge` against a local `next dev` server using a temporary merged instruction root, producing pass status with 8 checks at `frontend/artifacts/harness/section8/latest/summary.json`. `npm run instruction-root:integrity` was attempted and failed because the nested app-dev source root lacks `agents/`. `node ./scripts/verify-instruction-root-integrity.mjs --source-root /Users/ryan/ai-env/projects/chirality` was attempted and failed because the root source lacks current required app-dev governance docs such as `docs/DIRECTIVE.md`.

## 2026-06-14 - SDK read-tool exposure behind capability policy landed (`SDK-READ-TOOLS-001`)

Enabled requested read-class Claude Agent SDK built-ins behind the Chirality-owned descriptor registry, permission overlay, and SDK options builder.

The tranche bumps the tool registry posture from descriptor-only to read-tool exposure for `Read`, `Glob`, `Grep`, and `LS`. Requested read descriptors now become deterministic SDK `tools` and `allowedTools`; denied and unrequested SDK names remain in `disallowedTools`. Unknown `opts.tools` fail structurally before `agentSdk` adapter streaming begins. The `canUseTool` callback remains attached and now applies a basic hard-deny for path-bearing read calls that resolve outside the active project root or arrive with an SDK blocked path.

Write, edit, bash, network, subagent, Pi, concrete non-Anthropic providers, Chirality MCP tools, package/runtime migration, and desktop-wrapper changes remain out of scope. Read MCP / descriptor integration is the next runtime-spine item. Tool result/event evidence expansion remains a later tranche.

Residual: normal harness premerge and instruction-root integrity still expose the pre-existing split instruction-root posture. The root that contains `agents/` lacks current app-dev governance docs, while the nested app-dev source root contains current docs but no `agents/`. Running-app premerge passed only after using a temporary merged instruction root for validation. `npm run instruction-root:integrity` still fails in the default nested source-root mode looking for `projects/chirality-app-dev/agents`; an explicit root source run fails because root `docs/DIRECTIVE.md` and sibling required docs are absent.

Validation: `npm run test -- permission-overlay tool-descriptor sdk-options-builder turn-engine claude-agent-sdk-manager`; `npm run test`; `npm run typecheck`; `CHIRALITY_INSTRUCTION_ROOT=/tmp/chirality-instruction-root.c2uFKG npm run harness:validate:premerge` against a local `next dev` server using the same temporary merged root, producing pass status with 8 checks at `frontend/artifacts/harness/section8/latest/summary.json`; `git diff --check` over touched runtime, test, contract, and plan/log files. Normal `npm run harness:validate:premerge` was attempted and failed with `INSTRUCTION_ROOT_INVALID` under the split-root posture. `npm run instruction-root:integrity` and `node ./scripts/verify-instruction-root-integrity.mjs --source-root /Users/ryan/ai-env/projects/chirality` were attempted and failed for the pre-existing split-root posture described above.

## 2026-06-13 - Capability policy / permission overlay skeleton landed

Added a Chirality-owned permission overlay skeleton for the first-adapter runtime spine.

The tranche introduced provider-neutral `HarnessPermissionDecision` records, a permission policy version, mode normalization for `readOnly`, `workspaceWrite`, `dontAsk`, `ask`, `bypass`, and legacy/default posture, and abstract allow/deny/ask resolution against tool-descriptor metadata. SDK option construction now attaches a `canUseTool` callback backed by the overlay, maps `readOnly` to SDK `plan`, keeps `workspaceWrite` on SDK `default` until write hooks land, and leaves `bypassPermissions` behind `CHIRALITY_ALLOW_SDK_BYPASS=1`.

Tool execution remains disabled for this tranche: `tools: []`, `allowedTools: []`, and the broad descriptor-derived `disallowedTools` list are preserved. Read-class tools can receive abstract overlay allow decisions, but write approval, bash, network, subagent, concrete non-Anthropic provider work, Pi work, read MCP, and write/edit execution remain out of scope.

Residual: SDK read-tool exposure behind the capability policy is the next runtime-spine item. Instruction-root integrity evidence remains pre-existing debt: the normal command resolves the nested app-dev workspace as the source root and fails looking for `agents/`; an explicit Chirality root source override then fails because current required governance docs live under app-dev while the existing packaged Resources docs match the archived root docs. This tranche did not modify package resources, instruction-root files, packaging scripts, package manifests, provider scope, network policy, or desktop wrapper behavior.

Validation: `npm run test -- permission tool-descriptor sdk-options-builder`; `npm run test`; `npm run typecheck`; `git diff --check -- frontend/src/lib/harness/permission-overlay.ts frontend/src/lib/harness/tool-descriptor.ts frontend/src/lib/harness/sdk-options-builder.ts frontend/src/__tests__/lib/permission-overlay.test.ts frontend/src/__tests__/lib/tool-descriptor.test.ts frontend/src/__tests__/lib/sdk-options-builder.test.ts`. `npm run harness:validate:premerge` was skipped because `http://127.0.0.1:3000` was not reachable. `npm run instruction-root:integrity` was attempted and failed for the pre-existing source-root/package-resource posture described above.

## 2026-06-13 - Package-local context and local-kit refresh landed (`SCA-APP-001-CLOSURE-002`)

Repaired the package-local `SCA-APP-001` closure follow-up for SCC-003 and SCC-004.

The tranche refreshed 26 impacted `_CONTEXT.md` files across PKG-01, PKG-04, PKG-06, PKG-09, and PKG-10 from the accepted v3.2 decomposition, preserving the SCA alignment notes while replacing stale base identity, package scope, deliverable scope, artifact, and traceability fields. It also reviewed the named local-kit surfaces and normalized stale first-adapter, provider-scope, network-scope, and permission-policy wording in `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, and `Dependencies.csv` where present.

Residual: a fresh `AUDIT_SCOPE_CLOSURE` rerun remains required before `SCA-APP-001` can be independently accepted as fully closed. The pre-existing dependency closure snapshot still reports one residual six-node strict SCC outside this package-local repair scope. No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider implementation, Pi implementation, network expansion, tool exposure, or release-readiness posture changed.

Validation: `git diff --check -- projects/chirality-app-dev/execution projects/chirality-app-dev/plans`; impact-CSV-to-decomposition alignment check for all 26 affected `_CONTEXT.md` files; stale local wording scan for `SDK Probe`, `deny-first`, `deny-overrides-allow`, `Anthropic-only`, `Pi-spike`, `blanket deny-first`, `permission_overlay_deny_first`, and `engine contract, SDK mapper`; Ruby CSV structural check for all 10 modified `Dependencies.csv` files; `node -e` JSON parse for `Post_Change_Coverage.json`; source/package exclusion check. Frontend runtime tests were skipped because this tranche changed only execution governance/package-local documentation, SCA repair evidence, and planning closeout records.

## 2026-06-13 - Scope-change pointer, propagation, and supersession repair landed (`SCA-APP-001-CLOSURE-001`)

Repaired the first set of `AUDIT_SCOPE_CLOSURE` findings for `SCA-APP-001`.

The tranche updated `execution/_ScopeChange/_LATEST.md` so it records accepted Gate 5 state, added a Gate 5 propagation classification addendum for the additional governance docs changed during Gate 5, and normalized `Supersession_Delta.csv` to the canonical supersession-map schema. `Supersession_Map.csv` was generated from the normalized delta.

Residual: SCC-003 and SCC-004 remain open for bounded package-local context refresh and local-kit/dependency/reference artifact review across affected PKG-01, PKG-04, PKG-06, PKG-09, and PKG-10 deliverables. No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider implementation, Pi implementation, or release-readiness posture changed.

Validation: `git diff --check -- projects/chirality-app-dev/execution/_ScopeChange projects/chirality-app-dev/plans`; `node -e` JSON parse for `Post_Change_Coverage.json`; Ruby CSV schema checks for `Supersession_Delta.csv` and `Supersession_Map.csv`; supersession-map accumulation with `tools/coordination/accumulate_supersession_map.py`; source/package exclusion check. Frontend runtime tests were skipped because this tranche changed only governance/control-plane artifacts.

## 2026-06-13 - Quality and validation skeleton landed (`GOV-QUALITY-001`)

Added app-dev `docs/VALIDATION_STRATEGY.md` and `docs/RELEASE_QUALITY_GATES.md` as first-class governance support surfaces for evidence routing and release-quality gate selection.

The validation strategy separates static governance evidence, runtime contract verification, harness workflow validation, packaging/instruction-root evidence, and boundary/claims review. The release-quality gates route governance, runtime, permission/tool, harness workflow, security/network, UI/claims, packaging, and future domain-adapter changes to appropriate evidence.

This tranche did not change runtime API, source code, package manifests, application wrapper, provider policy, tool exposure, release-readiness posture, or professional-boundary authority. Residual: `GOV-BUILD-001` build/release skeleton if the governance-support lane continues.

Validation: `git diff --cached --check -- docs plans execution/_Coordination`; positive reference search for the new validation and release-gate surfaces; referenced-file existence check; decision-register uniqueness check; staged frontend/package-source exclusion check. Frontend runtime tests were skipped because this tranche changed only docs, plans, and coordination files.

## 2026-06-13 - Build/release skeleton landed (`GOV-BUILD-001`)

Added app-dev `docs/BUILD_AND_RELEASE.md` as a first-class governance support surface for local build, packaging, artifact, and release-evidence posture.

The guide records the current Electron/Next command surface from `frontend/package.json`, artifact locations, suggested local evidence profiles, packaging review steps, future CI/release mapping, and open human-gated release decisions. It does not change package scripts, package dependencies, runtime language, desktop wrapper architecture, provider policy, tool exposure, release-publication authority, or professional-boundary authority.

Residual: `GOV-WORKFLOW-001` workflow and docs index cleanup if the governance-support lane continues.

Validation: `git diff --cached --check -- docs plans execution/_Coordination`; positive reference search for `BUILD_AND_RELEASE`, `build_release`, `GOV-BUILD-001`, `GOV-WORKFLOW-001`, `desktop:pack`, and `desktop:dist`; referenced-file existence check; decision-register uniqueness check; staged frontend/package-source exclusion check. Frontend runtime tests were skipped because this tranche changed only docs, plans, and coordination files.

## 2026-06-13 - Workflow and docs index cleanup landed (`GOV-WORKFLOW-001`)

Added app-dev `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json` as workflow and discovery surfaces. The workflow guide maps authority surfaces, current phase posture, tranche selection, `TASK` discipline, validation routing, closeout shape, and non-authority boundaries. The docs index and manifest make the governance package discoverable without changing authoritative semantics.

This tranche did not replace canonical agent instructions, change the active runtime queue, modify runtime API/source code/package manifests, alter provider policy, create release authorization, or change professional-boundary authority. Residual: no current governance-support item remains in the active plan; return to the runtime spine unless the human selects another governance tranche.

Validation: `git diff --cached --check -- docs plans execution/_Coordination`; `docs/MANIFEST.json` JSON parse check; positive reference search for the new workflow/index surfaces and `GOV-WORKFLOW-001`; stale queued-governance-lane search returned no matches; referenced-file existence check; decision-register uniqueness check; staged frontend/package-source exclusion check. Frontend runtime tests were skipped because this tranche changed only docs, plans, and coordination files.

## 2026-06-13 - Next-instance state file retired (`GOV-STATE-001`)

Retired `execution/_Coordination/NEXT_INSTANCE_STATE.md` as an active coordination surface and aligned app-dev with the piping control-plane model: `_COORDINATION.md` and `NEXT_INSTANCE_PROMPT.md` define the entry protocol, while current state is discovered from governed docs, decomposition and deliverable artifacts, dependency/SCC snapshots, decision records, source, tests, validation evidence, and git history.

The coordination files now point to `execution/_Reconciliation/DepClosure/_LATEST.md` for dependency/SCC discovery when blocker posture matters. The latest known dependency closure evidence still reports one residual six-node strict SCC, so project-wide strict `BLOCKED` / `UNBLOCKED` state is not claimed.

This tranche did not change runtime API, source code, package manifests, application wrapper, provider policy, tool exposure, release-readiness posture, professional-boundary authority, or dependency-row semantics.

Validation: static governance checks only. Frontend runtime tests were skipped because this tranche changed only docs, plans, and coordination files.

## 2026-06-13 - Provider-general runtime scope change landed (`SCA-APP-001`)

Accepted `SCA-APP-001 Provider-General Runtime and Pi Pattern-Corpus Reorientation`.

The amendment records provider-adapter generality as the strategic runtime direction, keeps Claude Agent SDK / Anthropic as the first concrete adapter and current shipped path, treats Pi as pattern corpus/reference only, and reframes permission governance as capability-forward, policy-mediated, and evidence-recorded tool use with explicit hard-deny precedence.

D-APP-01, D-APP-02, and D-APP-03 are now RULED in `execution/_Coordination/_DECISIONS/_REGISTER.md`. The active completion plan no longer selects Pi adapter/spike work.

Execution deliverable `_CONTEXT.md` files for affected PKG-01, PKG-04, PKG-06, PKG-09, and PKG-10 deliverables were aligned with SCA context. Their local `Guidance.md`, `Specification.md`, `Procedure.md`, `Datasheet.md`, dependency, and reference artifacts remain explicit follow-up review surfaces.

Validation: static governance checks only. Frontend runtime tests were skipped because this tranche changed governance, decomposition, planning, coordination, runtime-contract documentation, and execution metadata only; no runtime source or package files changed.

## 2026-06-13 - Tool descriptor design landed (`3bf6f9fb1`)

Added a Chirality-owned descriptor-only `HarnessToolDescriptor` registry for SDK built-ins and reserved future tool surfaces. The metadata covers provider-neutral permissions, path scope, idempotence, result-budget, provenance, human-gate, runtime exposure, and adapter-name fields.

SDK option construction now derives its broad `disallowedTools` list from the descriptor registry while preserving `tools: []` and `allowedTools: []`. Tool execution remains disabled until permission overlay, hooks, result storage, and model/tool-loop prerequisites land.

Known validation from tranche closeout: focused descriptor/options tests, full frontend test suite, typecheck, harness premerge validation after starting the dev server, and instruction-root integrity. Residual: permission overlay skeleton is the next active plan item.

## 2026-06-13 - Engine conformance fixtures landed (`02f92417b`)

Added a provider-neutral engine conformance evaluator plus deterministic scripted Claude Agent SDK adapter fixtures. The fixtures cover success, provider failure, interruption terminal evidence, public UI event names, and missing terminal evidence.

Residual: extend conformance fixtures as permission/tool phases land. Validation details are not restated in the compact coordination state; use the commit and associated test history as the evidence pointer.

## 2026-06-13 - HarnessEvent expansion landed (`e39d07827`)

Added provider-neutral persisted event categories for message, tool, hook, queue, branch, interruption, compaction, and subagent lifecycle coverage.

Expanded Claude Agent SDK message mapping for deterministic runtime evidence while preserving public browser SSE event names. Residual: replay and conformance coverage should expand as tool execution becomes real.

Validation details are not restated in the compact coordination state; use the commit and associated test history as the evidence pointer.

## 2026-06-13 - Turn lifecycle extraction landed (`c8d735e2e`)

Added product-owned `TurnEngine` lifecycle ownership for pre-stream turn preflight, same-session locking, attachment/governance shaping, adapter stream execution, session metadata persistence, cancellation delegation, and mid-stream terminal error mapping.

The tranche preserved `/api/harness/turn` SSE behavior. Residual: continue extracting policy from route-owned surfaces only where planned by the active runtime completion plan.

Validation details are not restated in the compact coordination state; use the commit and associated test history as the evidence pointer.

## 2026-06-13 - Provider-neutral runtime contract cleanup landed (`6b23eb96c`)

Generalized persisted `HarnessEvent` type names away from SDK-prefixed names. SDK identifiers remain adapter metadata, and `engineSessionId` was added as a provider-neutral compatibility alias.

Validation defaults were repaired for the nested app-dev workspace layout. Residual: continue preventing SDK-shaped names, transcript paths, and tool identifiers from becoming public or core Chirality semantics.

Validation details are not restated in the compact coordination state; use the commit and associated test history as the evidence pointer.
