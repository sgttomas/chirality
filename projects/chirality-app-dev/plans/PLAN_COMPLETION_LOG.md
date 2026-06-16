# Runtime Plan Completion Log

This log preserves landed-tranche narrative for the active runtime completion plan, currently `plans/PLAN_2026-06-13_runtime_completion.md`.

This file is history, not authority. Project truth remains in governed docs, decomposition and deliverable artifacts, source, tests, evidence records, and git history. Nothing here is a lifecycle decision, release-readiness claim, professional approval, certification, sealing, authentication, or code-compliance acceptance.

---

## 2026-06-16 - R5 executable child turn integration landed (`R5-EXEC-001`)

Landed the bounded D-APP-10 Option C executable R5 path for `R5-SLICE-006`. The SDK
`Agent` tool is model-visible only when the parent explicitly requests `Agent` and
subagent governance has produced delegated Type 2 child names. SDK `agents` definitions are
generated for delegated child names with `tools: []`, descriptor-derived `disallowedTools`
including `Agent`, `maxTurns: 1`, and `permissionMode: dontAsk`.

Permission callback and `chirality.subagent.pre_tool_use` hook enforcement both re-check
the requested child name against the delegated list before execution. Non-workspaceWrite
modes, missing delegation, and unknown children remain denied. Adapter task messages map to
provider-neutral `subagent.started`, `subagent.progress`, `subagent.completed`, and
`subagent.failed` evidence.

Child capability inheritance or expansion, unrestricted child tool access, nested subagent
execution, concrete non-Anthropic provider implementation, provider routing, network
expansion, Pi runtime paths, dependency-register edits, project-wide strict
dependency-closure claims, release-readiness claims, lifecycle issuance, professional
approval, certification, sealing, authentication, code-compliance acceptance, and
professional-boundary claim changes remain denied.

Validation passed: focused R5 executable suite
`npm run test -- --run src/__tests__/lib/harness-subagent-governance.test.ts src/__tests__/lib/agent-runtime-contract.test.ts src/__tests__/lib/subagent-bridge.test.ts src/__tests__/lib/sdk-options-builder.test.ts src/__tests__/lib/chirality-hooks.test.ts src/__tests__/lib/permission-overlay.test.ts src/__tests__/lib/tool-descriptor.test.ts src/__tests__/lib/claude-agent-sdk-manager.test.ts src/__tests__/lib/sdk-message-mapper.test.ts`;
`npm run typecheck`; full `npm run test`; `npm run harness:validate:premerge` after
starting the local Next dev server on port 3000; and `npm run instruction-root:integrity`.

## 2026-06-16 - D-APP-10 ruled Option C

Human project authority corrected the D-APP-10 ruling to Option C. A bounded executable
`R5-SLICE-006` path may proceed using landed `R5-BRIDGE-001` evidence as prerequisite.

The ruling permits executable child turn integration only for governed, delegated Type 2
subagents through the current Claude Agent SDK first-adapter path. Child capability
inheritance or expansion, unrestricted child tool access, nested subagent execution,
concrete non-Anthropic provider implementation, provider routing, network expansion, Pi
runtime paths, dependency-register edits, project-wide strict dependency-closure claims,
release-readiness claims, lifecycle issuance, professional approval, certification,
sealing, authentication, code-compliance acceptance, and professional-boundary claim
changes remain denied.

`_DECISIONS/_REGISTER.md` now records `D-APP-10` as `RULED`. The active plan selects
`R5-EXEC-001` for implementation.

Validation for this ruling-record step is docs/control-plane only; implementation
validation belongs to `R5-EXEC-001`.

## 2026-06-16 - Post-bridge R5 continuation packet prepared (`D-APP-10`)

Prepared `D-APP-10` after `R5-BRIDGE-001` landed. The packet asks which post-bridge R5
path is approved: lifecycle events only, non-executable scaffolding through bounded child
output artifact references, executable child turn integration, a narrower custom
continuation, or continued hold.

`_DECISIONS/_REGISTER.md` now records `D-APP-10` as `AWAITING_RULING`. Until the human
rules, R5 continuation beyond the landed non-executable bridge remains denied, including
parent-child lifecycle event scaffolding beyond current preflight evidence, child output
artifact reference semantics, model-visible SDK `Agent`, executable SDK `agents`, child
turn execution, child output artifacts from executable child runs, child capability
inheritance or expansion, concrete provider implementation, provider routing, network
expansion, Pi runtime paths, dependency-register edits, project-wide strict
dependency-closure claims, release-readiness claims, lifecycle issuance, professional
approval, certification, sealing, authentication, code-compliance acceptance, and
professional-boundary claim changes.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, package resources, release-readiness
posture, or professional-boundary posture changed in this packet step.

Validation for this packet step is docs/control-plane only; implementation validation
belongs to whichever D-APP-10 option is later ruled.

## 2026-06-16 - R5 non-executable subagent bridge landed (`R5-BRIDGE-001`)

Landed the approved D-APP-09 Option B bridge through `R5-SLICE-003`. The runtime now builds
inert SDK `agents` option-shape definitions only from already-delegated Type 2 candidates
resolved by subagent governance, while keeping the SDK `Agent` tool out of model-visible
`tools` / `allowedTools` and in `disallowedTools`.

The bridge definitions are non-executable: they carry `tools: []`, descriptor-derived
`disallowedTools` including `Agent`, `maxTurns: 0`, and `permissionMode: dontAsk`.
Permission overlay hard-denies `Agent`, and the Chirality `PreToolUse` hook records
`chirality.subagent.pre_tool_use` evidence before blocking Agent execution fail-closed.

Executable child turns, model-visible executable SDK `Agent`, executable SDK `agents`, child
output artifacts from executable child runs, child capability inheritance or expansion,
concrete provider implementation, provider routing, network expansion, Pi runtime paths,
dependency-register edits, project-wide strict dependency-closure claims, release-readiness
claims, lifecycle issuance, professional approval, certification, sealing, authentication,
code-compliance acceptance, and professional-boundary claim changes remain denied.

Validation passed: focused R5 bridge suite
`npm run test -- --run src/__tests__/lib/harness-subagent-governance.test.ts src/__tests__/lib/subagent-bridge.test.ts src/__tests__/lib/sdk-options-builder.test.ts src/__tests__/lib/chirality-hooks.test.ts src/__tests__/lib/permission-overlay.test.ts src/__tests__/lib/tool-descriptor.test.ts`;
`npm run typecheck`; full `npm run test`.

## 2026-06-16 - D-APP-09 ruled Option B

Human project authority approved `D-APP-09` Option B. A future tranche or sequence may
implement approved non-executable bridge slices 001-003: child definition eligibility, SDK
`agents` option-shape bridge, and Agent preflight/hook gate.

The ruling requires SDK `Agent` to remain non-model-visible or hard-denied. Executable child
turns, model-visible executable SDK `Agent`, executable SDK `agents`, child output artifacts
from executable child runs, child capability inheritance or expansion, concrete provider
implementation, provider routing, network expansion, Pi runtime paths, dependency-register
edits, project-wide strict dependency-closure claims, release-readiness claims, lifecycle
issuance, professional approval, certification, sealing, authentication, code-compliance
acceptance, and professional-boundary claim changes remain denied.

`_DECISIONS/_REGISTER.md` now records `D-APP-09` as `RULED`. The active plan selects
`R5-BRIDGE-001` for implementation.

Validation for this ruling-record step is docs/control-plane only; implementation validation
belongs to `R5-BRIDGE-001`.

## 2026-06-16 - Post-design R5 slice-selection packet prepared (`D-APP-09`)

Prepared `D-APP-09` after `R5-DESIGN-001` landed. The packet asks which post-design R5
path is approved: `R5-SLICE-001` only, non-executable bridge through slice 003,
non-executable scaffolding through slice 005, executable slice 006 after earlier evidence,
or continued hold.

`_DECISIONS/_REGISTER.md` now records `D-APP-09` as `AWAITING_RULING`. Until the human
rules, runtime source implementation, SDK `agents` option construction, model-visible SDK
`Agent`, child turn execution, child output artifacts from executable child runs, child
capability inheritance or expansion, concrete provider implementation, provider routing,
network expansion, Pi runtime paths, dependency-register edits, project-wide strict
dependency-closure claims, release-readiness claims, lifecycle issuance, professional
approval, certification, sealing, authentication, code-compliance acceptance, and
professional-boundary claim changes remain denied.

The packet preserves `D-APP-07` and cycle-driven resolution posture: the residual six-node
SCC remains non-gating only for bounded R5 dispatch selection and remains unresolved for
project-wide strict dependency closure. No SCC cut, merge, decompose, invert, or dependency
amendment is approved by the packet.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, package resources, release-readiness
posture, or professional-boundary posture changed in this packet tranche.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
targeted `rg` checks for `D-APP-09`, `R5-SLICE`, `AWAITING_RULING`, and denied-surface
references; referenced-path existence checks for the D-APP-09 packet, decision register,
active plan, completion log, R5 design package, D-APP-07/D-APP-08 rulings, SCC evidence,
and validation routing docs; decision-register ID uniqueness check; source/package
exclusion check. Frontend runtime tests, typecheck, harness premerge, instruction-root
integrity, build, packaging, network proof, and DMG checks were skipped because this
tranche only prepared a decision packet and updated control-plane planning surfaces.

## 2026-06-16 - R5 executable implementation design package landed (`R5-DESIGN-001`)

Prepared `plans/R5_EXECUTABLE_IMPLEMENTATION_DESIGN_PACKAGE_2026-06-16.md` under
`D-APP-08` Option C. The package decomposes executable R5 into bounded future slices:
child definition eligibility, SDK `agents` option-construction bridge, Agent preflight and
hook gating, parent-child lifecycle event mapping, bounded child output artifact references,
and executable child turn integration.

The package applies the cycle-driven resolution doctrine from
`/Users/ryan/ai-env/projects/chirality/docs/CYCLE_DRIVEN_RESOLUTION.md` and
`{REPO_ROOT}/docs/CYCLE_DRIVEN_RESOLUTION.md`: the dependency graph is objective-relative;
the residual six-node SCC remains non-gating only for bounded R5 dispatch under
`D-APP-07`; cycle-participating dependency rows are not closure evidence; project-wide
strict dependency closure remains unclaimable until a later SCC-resolution package records
named moves and a fresh dependency-closure audit accepts the result.

This package does not approve or implement model-visible SDK `Agent` tool execution,
executable SDK `agents` definitions, child turn execution, child output artifacts from
executable child runs, child capability inheritance or expansion, concrete provider
implementation, provider routing, network expansion, Pi runtime paths, dependency-register
edits, project-wide strict dependency-closure claims, release-readiness claims, lifecycle
issuance, professional approval, certification, sealing, authentication, code-compliance
acceptance, or professional-boundary claim changes.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, package resources, release-readiness
posture, or professional-boundary posture changed in this package tranche.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
targeted `rg` checks for `D-APP-08`, `R5-DESIGN-001`, `R5-SLICE`, and
`CYCLE_DRIVEN_RESOLUTION` references; referenced-path existence checks for the D-APP-08
packet/ruling, decision register, active plan, completion log, design package,
RECONCILIATION SCC ruling package, and cycle-driven resolution doctrine; decision-register
ID uniqueness check; source/package exclusion check. Frontend runtime tests, typecheck,
harness premerge, instruction-root integrity, build, packaging, network proof, and DMG
checks were skipped because this tranche only prepared a design/evidence package and
updated control-plane planning surfaces.

## 2026-06-16 - D-APP-08 ruled Option C

Human project authority approved `D-APP-08` Option C. No executable code lands from this
ruling. WORKING_ITEMS must prepare an implementation design and evidence package that
decomposes executable R5 into smaller implementation slices and validation gates.

The design package must consider
`/Users/ryan/ai-env/projects/chirality/docs/CYCLE_DRIVEN_RESOLUTION.md` when planning
through the residual SCC. The residual SCC remains non-gating only for bounded R5 dispatch
selection under `D-APP-07`; it remains unresolved for project-wide strict dependency
closure.

This ruling does not approve model-visible SDK `Agent` tool execution, executable SDK
`agents` definitions, child turn execution, child output artifacts from executable child
runs, child capability inheritance or expansion, concrete provider implementation,
provider routing, network expansion, Pi runtime paths, dependency-register edits,
project-wide strict dependency-closure claims, release-readiness claims, lifecycle
issuance, professional approval, certification, sealing, authentication, code-compliance
acceptance, or professional-boundary claim changes.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, package resources, release-readiness
posture, or professional-boundary posture changed in the ruling-record tranche.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
`rg -n "D-APP-08|Option C|R5 implementation design" execution/_Coordination/_DECISIONS plans`;
referenced-path existence checks for the packet, ruling, register, plan, cycle-driven
resolution doctrine, and RECONCILIATION package; decision-register ID uniqueness check;
source/package exclusion check. Frontend runtime tests, typecheck, harness premerge,
instruction-root integrity, build, packaging, network proof, and DMG checks were skipped
because this tranche only recorded the human ruling and updated control-plane planning
surfaces.

## 2026-06-16 - Bounded executable R5 implementation decision packet prepared (`D-APP-08`)

Prepared `D-APP-08` after `D-APP-07` ruled the residual six-node SCC non-blocking for
bounded R5 dispatch selection. The packet asks whether to approve bounded executable R5
implementation, approve a non-executable R5 bridge, require an implementation design
package first, or continue to hold executable subagent capability.

The tranche did not change runtime source, package manifests, dependencies, lockfiles,
desktop wrapper behavior, provider scope, network policy, tool exposure, package resources,
release readiness, lifecycle issuance, professional approval, certification, sealing,
authentication, or code-compliance acceptance. `_DECISIONS/_REGISTER.md` now records
`D-APP-08` as `AWAITING_RULING`; model-visible SDK `Agent`, executable SDK `agents`, child
turn execution, child output artifacts, child capability inheritance, provider routing,
network expansion, Pi runtime paths, project-wide closure claims, release-readiness claims,
and professional-boundary changes remain denied until ruled.

Residual: the latest dependency closure evidence still reports one six-node strict SCC, so
project-wide strict dependency closure remains unclaimable. `D-APP-07` permits future R5
selection without using that SCC as an R5 dispatch blocker, but it did not approve
executable implementation.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
`rg -n "D-APP-08|Bounded executable R5 implementation" execution/_Coordination/_DECISIONS plans`;
referenced-path existence checks for the packet, register, plan, D-APP-05/D-APP-06/D-APP-07
rulings, RECONCILIATION package, and runtime contract docs; decision-register ID uniqueness
check; source/package exclusion check. Frontend runtime tests, typecheck, harness premerge,
instruction-root integrity, build, packaging, network proof, and DMG checks were skipped
because this tranche only prepared a decision packet and updated control-plane planning
surfaces.

## 2026-06-16 - D-APP-07 ruled Option B

Human project authority approved `D-APP-07` Option B. The residual six-node strict SCC
blocks project-wide strict dependency-closure claims only. A later bounded executable R5
packet or tranche may be selected without claiming project-wide closure, with the SCC's
cycle-participating rows held non-gating only for R5 dispatch.

This ruling is a posture ruling. It does not itself approve executable R5 implementation,
SDK `Agent` exposure, executable SDK `agents`, child turn execution, child output artifacts
from executable child runs, child capability inheritance or expansion, dependency-register
edits for the residual SCC, cut/merge/decompose/invert moves, Pi runtime paths, concrete
provider implementation, provider routing, network expansion, release-readiness claims,
lifecycle issuance, professional approval, certification, sealing, authentication,
code-compliance acceptance, or professional-boundary claim changes.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, package resources, release-readiness
posture, or professional-boundary posture changed in the ruling-record tranche.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
`rg -n "D-APP-07|Option B|project-wide strict dependency-closure claims only" execution/_Coordination/_DECISIONS plans`;
referenced-path existence checks for the packet, ruling, register, plan, RECONCILIATION
package, human-ruling workbook, and dependency closure report; decision-register ID
uniqueness check; source/package exclusion check. Frontend runtime tests, typecheck,
harness premerge, instruction-root integrity, build, packaging, network proof, and DMG
checks were skipped because this tranche only recorded the human ruling and updated the
decision register, active plan, and completion log.

## 2026-06-15 - Residual SCC executable R5 implication decision packet prepared (`D-APP-07`)

Prepared `D-APP-07` from the RECONCILIATION package's required `HR-001` human ruling.
The packet asks whether the residual six-node strict SCC blocks executable R5 until closure
or amendment, blocks only project-wide dependency-closure claims, or requires
dependency/decomposition amendment before executable R5 can proceed.

The tranche did not change runtime source, package manifests, dependencies, lockfiles,
desktop wrapper behavior, provider scope, network policy, tool exposure, package resources,
release readiness, lifecycle issuance, professional approval, certification, sealing,
authentication, or code-compliance acceptance. `_DECISIONS/_REGISTER.md` now records
`D-APP-07` as `AWAITING_RULING`; executable R5 remains held until a ruling lands.

Residual: project-wide strict dependency closure remains unclaimable while the latest
dependency-closure evidence reports one six-node SCC. No dependency-register amendment,
cut, merge, decompose, invert, executable R5 implementation, SDK `Agent` exposure,
executable SDK `agents`, child turn execution, child output artifacts, child capability
inheritance, Pi runtime path, concrete provider, provider routing, network expansion,
release-readiness claim, or professional-boundary claim was approved.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
`rg -n "D-APP-07|Residual SCC executable R5 implication" execution/_Coordination/_DECISIONS plans`;
referenced-path existence checks for the packet, register, plan, RECONCILIATION package,
human-ruling workbook, and dependency closure report; decision-register ID uniqueness
check; source/package exclusion check. Frontend runtime tests, typecheck, harness premerge,
instruction-root integrity, build, packaging, network proof, and DMG checks were skipped
because this tranche only prepared a decision packet and updated control-plane planning
surfaces.

## 2026-06-15 - Residual six-node SCC RECONCILIATION package prepared

Prepared the RECONCILIATION longer-cycle ruling package required by `D-APP-06` for the
residual six-node strict SCC. The stepwise run dispatched `AUDIT_DEP_CLOSURE`, which
created `execution/_Reconciliation/DepClosure/CLOSURE_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1820/`
and confirmed the current graph still has one strict SCC of size six:
`DEL-03-01`, `DEL-03-02`, `DEL-03-03`, `DEL-03-04`, `DEL-04-03`, and `DEL-05-02`.

The RECONCILIATION package lives at
`execution/_Reconciliation/RECON_APP_RESIDUAL_SIX_NODE_SCC_RULING_PACKAGE_2026-06-15_1825/`.
It determines that the SCC blocks project-wide strict dependency-closure claims. It also
records that dependency evidence alone does not prove every possible bounded executable R5
implementation is technically blocked, but executable R5 remains held until human project
authority chooses the package's R5 implication path.

No cut, merge, dependency-register amendment, executable R5 implementation, SDK `Agent`
exposure, executable SDK `agents`, child turn execution, child output artifacts, child
capability inheritance, Pi runtime path, concrete provider, provider routing, network
expansion, release-readiness claim, lifecycle issuance, professional approval,
certification, sealing, authentication, code-compliance acceptance, or professional-boundary
claim change was approved or implemented.

Validation: docs/control-plane and CSV/JSON checks only: `git diff --check -- execution/_Reconciliation plans`;
JSON parsing for the closure summaries; CSV parsing for the SCC edge and human-ruling
workbooks; artifact existence checks for the RECONCILIATION package and dependency-closure
snapshot; pointer checks for `_Reconciliation/_LATEST.md` and `DepClosure/_LATEST.md`.
Runtime tests, typecheck, harness premerge, build, packaging, network proof, and DMG checks
were skipped because this tranche changed only reconciliation evidence and planning
surfaces.

## 2026-06-15 - D-APP-06 ruled Option C

Human project authority approved `D-APP-06` Option C. Executable R5 governed subagent
implementation is held until RECONCILIATION prepares a longer-cycle ruling package for the
residual six-node SCC reported in the latest dependency closure snapshot.

The required RECONCILIATION package must determine whether the SCC is blocking for
executable R5 implementation, blocking only for project-wide dependency closure claims, or
evidence that decomposition/dependency amendment is required before R5 can proceed.

This ruling does not approve SDK `Agent` exposure, executable SDK `agents` definitions,
child turn execution, child output artifacts, child capability inheritance, Pi runtime
paths, concrete provider implementation, provider routing, network expansion,
release-readiness claims, lifecycle issuance, professional approval, certification,
sealing, authentication, code-compliance acceptance, or professional-boundary claim
changes.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, package resources, release-readiness
posture, or professional-boundary posture changed in the ruling-record tranche. The next
required action is a RECONCILIATION longer-cycle ruling package; no executable R5
implementation tranche is unblocked by this ruling alone.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
`rg -n "D-APP-06|Option C|longer-cycle" execution/_Coordination/_DECISIONS plans`;
referenced-path existence checks for the
packet, ruling, register, plan, and dependency closure report; decision-register ID
uniqueness check; source/package exclusion check. Frontend runtime tests, typecheck,
harness premerge, instruction-root integrity, build, packaging, network proof, and DMG
checks were skipped because this tranche only recorded the human ruling and updated the
decision register, active plan, and completion log.

## 2026-06-15 - Post-contract R5 executable subagent runtime decision packet prepared (`D-APP-06`)

Prepared the post-prerequisite R5 decision packet for executable governed subagent runtime.
The packet asks whether to approve a bounded executable implementation after
`AGENT-SUBAGENT-CONTRACT-001`, approve another non-executable bridge, require residual
dependency/SCC reconciliation first, or hold R5 capability expansion.

The tranche did not change runtime source, package manifests, dependencies, lockfiles,
desktop wrapper behavior, provider scope, network policy, tool exposure, package resources,
release readiness, lifecycle issuance, professional approval, certification, sealing,
authentication, or code-compliance acceptance. `_DECISIONS/_REGISTER.md` now records
`D-APP-06` as `AWAITING_RULING`; model-visible SDK `Agent` execution, executable SDK
`agents` definitions, child turn execution, executable child output artifacts, child
capability inheritance, Pi implementation paths, concrete providers, and provider/network
broadening remain blocked until a ruling lands.

Residual: the latest dependency closure snapshot still reports a residual six-node strict
SCC. This packet does not claim project-wide dependency closure or replace the recommended
RECONCILIATION longer-cycle ruling package.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
`rg -n 'D-APP-06|Post-contract R5 executable' execution/_Coordination/_DECISIONS plans`;
referenced-path existence checks for the packet's governing docs and dependency closure
report; decision-register ID uniqueness check; trailing-whitespace check over the four
changed files. Frontend runtime tests, typecheck, harness premerge, instruction-root
integrity, build, packaging, network proof, and DMG checks were skipped because this tranche
only prepared a decision packet and updated the decision register, active plan, and
completion log.

## 2026-06-15 - Provider-adapter-neutral agent/subagent contract prerequisite landed (`AGENT-SUBAGENT-CONTRACT-001`)

Landed the bounded D-APP-05 prerequisite contract for governed agent/subagent runtime work.
The tranche added a Chirality-owned `agent-runtime-contract` module with contract-only
child-run records, explicit blocked executable-delegation posture, provider-neutral
child-run event categories, adapter metadata isolation, child capability non-inheritance,
and validation helpers for child-run records.

Runtime contract docs now define the current prerequisite posture: executable delegation is
blocked, generated child definitions are contract-only future scope, Pi remains a pattern
corpus/reference only, concrete non-Anthropic provider routing remains blocked, and child
runs do not inherit parent capabilities. `docs/TYPES.md` now describes child-run records in
provider-neutral terms, with adapter-specific task/session/tool IDs confined to adapter
metadata.

This tranche did not expose the SDK `Agent` tool, generate executable SDK `agents`
definitions, add Pi package imports or runtime paths, add a concrete non-Anthropic provider,
broaden network policy, change package/runtime requirements, alter the desktop wrapper, or
make release-readiness, lifecycle issuance, professional approval, certification, sealing,
authentication, or code-compliance claims.

Residual: executable subagent runtime remains future/human-gated. Any later implementation
must define the bounded child tool set, generate adapter-specific child definitions from
the Chirality contract, enforce `evaluateSubagentGovernance` at the executable boundary,
persist parent-child output artifact references, and validate that provider/SDK details
remain adapter metadata only.

Validation: `npm run test -- agent-runtime-contract`; `npm run typecheck`; `npm run test`
(44 files, 336 tests). Static diff/stale-reference checks were run over the changed
runtime-contract, docs, plan, and completion-log surfaces. Harness premerge was skipped
because this tranche did not change browser-facing session, SSE, or turn-route behavior and
did not require a running local harness API. Instruction-root integrity, build, packaging,
network proof, and DMG checks were skipped because no instruction-root packaging, build,
provider/network, or release/distribution behavior changed.

## 2026-06-15 - D-APP-05 ruled Custom Option B/A-prerequisite

Human project authority approved a custom prerequisite ruling for `D-APP-05`. Before
executable SDK subagents are exposed, Chirality must implement or specify a Chirality-owned
provider-adapter-neutral agent/subagent runtime contract informed by both Claude Agent SDK
and Pi agent SDK patterns.

The ruling allows Claude Agent SDK `Agent` to remain the first adapter-specific substrate
and allows Pi to be used as an architectural pattern corpus. Neither Claude nor Pi may
define Chirality's public/core runtime contract.

This ruling does not approve Pi package import, Pi adapter/fork/sidecar/spike, Node 22
sidecar or runtime-floor migration for Pi, concrete non-Anthropic provider implementation,
provider routing, provider/network expansion, remote MCP/plugins, executable SDK subagent
exposure, release readiness, lifecycle issuance, professional approval, certification,
sealing, authentication, or code-compliance acceptance.

No runtime source, package manifest, dependency, lockfile, desktop wrapper, provider
implementation, network policy, tool exposure, or release-readiness posture changed in the
ruling-record tranche. The next unblocked plan item is the provider-adapter-neutral
agent/subagent runtime contract prerequisite.

Validation: docs/control-plane static checks only. Frontend runtime tests were skipped
because this tranche only recorded the human ruling and updated the decision register,
active plan, and completion log.

## 2026-06-15 - R5 governed SDK subagent runtime decision packet prepared (`D-APP-05`)

Prepared the post-Bash R5 decision packet for governed SDK subagent runtime. The packet
asks whether to approve a bounded R5 implementation, approve prerequisite-only registry
and hook work, require residual dependency/SCC reconciliation before implementation, or
hold subagent capability expansion.

The tranche did not change runtime source, package manifests, dependencies, lockfiles,
desktop wrapper behavior, provider scope, network policy, tool exposure, package resources,
release readiness, lifecycle issuance, professional approval, certification, sealing,
authentication, or code-compliance acceptance. `_DECISIONS/_REGISTER.md` now records
`D-APP-05` as `AWAITING_RULING`; SDK `Agent` exposure, executable SDK `agents`
definitions, and governed subagent runtime execution remain blocked until a ruling lands.

Residual: concrete non-Anthropic providers, provider/network broadening, remote MCP/plugins,
Pi implementation paths, `MultiEdit`, mutating Chirality MCP tools, package/runtime
migration, release-candidate DMG proof, release-readiness claims, and professional-boundary
changes remain future/human-gated. The latest dependency closure snapshot still reports a
residual six-node strict SCC; this packet does not claim project-wide dependency closure or
replace the recommended RECONCILIATION longer-cycle ruling package.

Validation: docs/control-plane static checks only: `git diff --check -- execution/_Coordination/_DECISIONS plans`;
`rg -n "D-APP-05" execution/_Coordination/_DECISIONS plans`; referenced-path
existence checks for the packet's governing docs, D-APP-04 ruling, and dependency closure
report; decision-register ID uniqueness check. Frontend runtime tests were skipped because
this tranche changed only the decision packet, decision register, active plan, and
completion log.

## 2026-06-15 - Instruction-root split-root package integrity repair landed (`INSTRUCTION-ROOT-SPLIT-001`)

Repaired the normal package `instruction-root:integrity` path for the app-dev split source
layout. The verifier now supports explicit split source roots and auto-detects the app-dev
frontend workspace shape: root files (`AGENTS.md`, `README.md`, and
`PROFESSIONAL_ENGINEERING.md`) plus `agents/` come from the Chirality monorepo root, while
current governance docs come from `projects/chirality-app-dev/docs`. The generated manifest
records `sourceLayout: split`, per-source root paths, and the packaged resource comparisons.

Updated Electron `extraResources` to package app-dev governance docs from `../docs`, added
the required app-dev `docs/WHAT-IS-AN-AGENT.md`, indexed that file in the docs package, and
aligned the workflow guide's current-posture summary with the active plan now landed through
R4 Bash. The old temporary merged-root workaround is no longer required for package integrity.

Residual: dev-server harness default instruction-root resolution remains a separate runtime
resolver concern if selected later. This tranche did not change provider scope, runtime tool
exposure, network policy, package dependencies, runtime language, SDK subprocess behavior,
DMG distribution posture, release readiness, lifecycle issuance, professional approval,
certification, sealing, authentication, or code-compliance acceptance.

Validation: `npm run test -- verify-instruction-root-integrity dmg-packaging-policy`;
`npm run test` (43 files, 331 tests); `npm run typecheck`; `npm run desktop:pack`, which ran
`npm run build`, unsigned/unnotarized macOS arm64 app-directory packaging with publishing
disabled, and `npm run instruction-root:integrity`. The fresh integrity summary passed with
`sourceLayout: split`, 46 checked files, zero missing files, zero hash mismatches, and zero
unexpected bundled agent files at
`frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. `desktop:dist`
was skipped because this was an app-directory package-layout repair, not a DMG or release
candidate review. Harness premerge was skipped because no running harness API, SSE contract,
session lifecycle, or runtime source behavior changed in this tranche.

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
