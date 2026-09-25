# Bounded source-blocks frontend executor

Read Root AGENTS.md, agents/AGENT_TASK.md, Piping AGENTS.md and loop/LOOP_INIT.md.
Act as TASK: understand this objective/boundary, implement and check the bounded
contribution, support the return with actual evidence and gaps, obey the write
boundary, and do not delegate. ROOT will launch or resume the actual TASK;
record its real name and ROOT parentage. WORKING_ITEMS /root/numerical_resume
coordinates the return and owns overall integration. This brief is not proof of
an actual launch.

Use the source-recovery checkout selected by ROOT, branch
codex/piping-source-recovery-20260924, base
0a438a68672269e5750900792c9565ae9e5555b0. Resolve REPO_ROOT there and WORKING_ROOT
as projects/chirality-piping. Other checkouts are read-only. The run's cut root is
execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/SOLVER_MANAGER/ORDINARY_NUMERICAL_CUT.
Evidence writes belong only under its SOURCE_RECOVERY_IMPLEMENTATION_01/FRONTEND_READERS.

## Basis and intended result

ROOT selected CARRIER_DESIGN/CONTRACT.md, API_HANDOFF.md,
source_block_receipt.schema.json, HASH_PAYLOADS.md and INTEGRATION_MAP.md in the
same implementation directory. Bind the actual versions read. Initial selected
schema SHA is e3e59d0bfb7f4969fa3fbaabb6012103ac827af03644d4906b69010c17f6347d;
API handoff SHA is 6f5dfeffba9a350d137e826b6900bd6c79f82ff1ab872f984ddf36cb49d7a7fd.
The new producer semantic ID is
openpipestress.result_semantics/0.3.0/source-blocks-1, raw 0.2/canonical 0.3.
The additive raw field is source_block_recovery. Keep p1 and its immutable table,
hash and historical behavior. Physics-1 remains separately dispatched until ROOT's
reviewed join; do not write the parallel engine-integration checkout.

Other TASK owns maintained table
fixtures/results/semantic_contract_v0_3_source_blocks_1.json (SHA
5f299065f15a157bbedf9467a598994ae684c4ecb3f851bbcb291981ec550a9f)
and schemas/source_block_recovery.schema.json, plus Rust/Python consumers.
Read them as they land; never overwrite them. Parent owns product lib.rs,
source_receipt.rs coordination, src-tauri and headless/native driver wiring.

Implement actual source-method reader/Current/rule/export/history/analysis/report
connections. This is necessary solver interface work, not general UI polishing.
No real material/component libraries or code rules are seeded. Invented test
controls remain explicit validation data.

## Exact write ownership

Paths below are relative to apps/desktop/src. Edit only those needed; no claim
that every listed file requires change. New helper names are reserved here.

- types.ts
- features/results/sourceBlockRecovery.ts and sourceBlockRecovery.test.ts
- features/results/numericalResultQuality.ts and numericalResultQuality.test.ts
- features/results/resultSemantics.ts and resultInterpretation.ts
- features/results/analysisResultHashScope.ts and analysisResultHashScope.test.ts
- features/results/HistoricalRunContext.tsx and HistoricalRunContext.test.tsx
- features/results/ResultsPanel.tsx and ResultsPanel.test.tsx
- services/analysisRunCompatibility.ts and analysisRunCompatibility.test.ts
- services/previewService.ts and previewService.test.ts
- services/ruleCheckService.ts and ruleCheckService.test.ts
- services/inputManifestService.ts and inputManifestService.test.ts
- features/workspace/resultsSessionState.ts and resultsSessionState.test.ts
- features/workspace/workspaceSession.ts
- features/result-export/resultExportAdapter.ts and resultExportAdapter.test.ts
- features/stress-neutral/StressNeutralExportPanel.tsx and StressNeutralExportPanel.test.tsx
- features/report/renderableReportInput.ts, reportPackageRequest.ts, reportPackageRequest.test.ts,
  ReportPanel.tsx and renderedReport.test.tsx
- features/native-package/NativePackagePanel.tsx and NativePackagePanel.test.ts
- features/local-fea-handoff/LocalFeaHandoffPanel.tsx and LocalFeaHandoffPanel.test.tsx
- features/comparison/ComparisonPanel.tsx
- App.tsx and App.test.tsx only if necessary to connect the existing solve/result lifecycle

No src-tauri, core, shared schema/table, build configuration, general styling,
graph, instruction or unrelated source writes. Coordinate any necessary additional
path with the manager while independent work continues; no owner prompt is needed
for routine implementation choices within the authorized solver undertaking.

## Binding and admission requirements

The Value-aware producer captures the entire actual request before deserialization,
plus the actual resolved mode. Invocation hash payload is
{request: actualProductRequest, solver_mode: actualResolvedMode}. Never reserialize
typed inputs, insert default fields, strip unknown raw fields, or invent an override
material list to match a receipt. The actual native driver constructs
{model,materials:[]} today; capture that actual invocation through the real solve
call. Typed-only historical product entries retain ordinary/p1 behavior.

Numerical standing is presently synchronous while checked canonical hashing uses
the asynchronous Rust-WASM authority. Implement the smallest safe bridge: genuine
async receipt validation before result publication, then a private qualification
token bound to the actual source and independently retained invocation. A stale or
mutated source/invocation must not reuse a token. Do not substitute a public flag,
self-claimed accuracy label, unchecked object-identity cache or a JS hash fallback.
Keep actual model/input/build/source and AnalysisRun authentication as separate
requirements. Missing actual invocation context remains unqualified. Imported
history does not become Current just because a receipt hashes correctly.

Exact-selected cases qualify through complete new-method evidence; ordinary-selected
cases qualify only through unchanged p1 checks_passed predicates, never Sensitive.
Ordinary numerical_quality remains truthful, so N06 may retain an unresolved
ordinary attempt alongside successful exact source recovery. Unsupported/failed
physical cases or inspection-only physical rows withhold qualified whole-envelope
use. Each physical row must bind an actual projection or an implemented checked
derived recipe; a recipe string is not a proof. Nonphysical observations may remain
disclosed. Keep the mechanism bounded, without a generic capability/store framework.

Reject new receipt-field presence under p1/legacy/physics-1, including falsy and
rehashed contradictions; reject unknown future identities. New table meanings
include support_reaction_component_v2 with Fx/Fy/Fz in N and Mx/My/Mz in N*m,
global/node, actual support identity, support-on-pipe signs and basis
recovered_from_assembled_support_law. Do not turn a free equilibrium zero into a
spring action or put a torque in an N resultant.

Preserve source raw bytes and receipt publication hash across analysis/rule revisions.
Investigate existing rule-check and workspace updates: if they mutate the producer
carrier, keep that revision in the proper analysis/derived layer rather than
silently recomputing a producer receipt in the frontend. Canonical/analysis/stress-
neutral transport can preserve inspectable records without granting qualified use.

## Verification and return

No Git, Cargo/npm test/build, browser or native execution until the shared lane is
scheduled by ROOT/manager. Source work and small static checks can proceed. Use
one current basis/return and final diff; preserve meaningful observed failures, not
per-function freezes or full source copies. Parent will supply real both-mode
source-block carriers for connected verification; label synthetic validator controls
accurately and do not use injected hash functions as actual runtime proof.

Cover rehashed/header contradictions, malformed/partial/missing case and row
coverage, changed actual invocation, source mutation after validation, wrong mode,
private-token bypass attempts, history without actual context, and genuine positive
Current/export bindings. Send the chosen validation/token API early. Return exact
edited files, actual check commands/results, source hashes when stable, and remaining
integration needs to WORKING_ITEMS, with ROOT receiving the actual execution return.
