# Frontend API and composite handoff

Paths below are relative to `projects/chirality-piping/apps/desktop/src`. The branch is `codex/piping-source-recovery-20260924`; the frozen source/hash inventory is FINAL_SOURCE.json. Only the assigned21 paths were written. ROOT owns the unified candidate and external Git; numerical/physics managers own integration.

## Native origin (shared implementation)

`services/previewService.ts` exports:

```ts
type NativeMechanicsInvocation = {
  request: { model: PreviewModel; materials: [] };
  solver_mode: PreviewSolverMode;
};
hasNativeMechanicsInvocation(source, model, solverMode?): boolean;
retainedNativeMechanicsInvocation(source, model): NativeMechanicsInvocation | null;
loadBundledMechanicsReference(mode?): Promise<BundledMechanicsReference>;
```

The registrar is private. Capture precedes actual direct IPC or a locally started job, sends that exact captured model, retains invalidation/terminal-claim state, and checks full source/context fingerprints across checked async hashing. The source-block validator composes inside private `validateCapturedSource(source,capture)` before generic registration. Failed, unknown, mismatched, cancelled and invalidated jobs never register. Generic provenance is additional to scientific/numerical/model/input/run/build requirements.

Browser run/start refuse with `BROWSER_SOLVE_BACKEND_REQUIRED_REFERENCE_ONLY` (edited-model diagnostic retained). Reference loading returns original bytes/values plus external reference provenance and no live registration. Workspace fresh publication rejects old browser fixture job receipts. No reference-view UI or persistence stash was added here; reuse the physics reader’s separately reviewed reference-view/persistence work at composite fan-in.

## Source method

`features/results/sourceBlockRecovery.ts` exports:

```ts
validateSourceBlockRecovery(source, independentlyRetainedInvocation): Promise<{eligible,findings}>;
sourceBlockStanding(source, model): {eligible,findings};
retainedSourceBlockInvocation(source, model): SourceBlockInvocation | null;
sourceBlockModeMatches(source, model, mode): boolean;
sourceBlockReceiptShape(value): boolean;
```

The independent invocation is `{request:<entire actual preparse request>,solver_mode:<actual resolved mode>}`. Its material override shape is never inferred from a receipt. The private method registration binds full raw content, signed-zero identity and unchanged invocation/model content. JSON-normalization is not permission to alter projection bits. A copied/history carrier has no registration. The separate generic native gate remains mandatory for Current even when a received artifact’s method record validates.

`numericalResultQuality.ts` adds explicit `source_blocks` dispatch and exports `currentSemanticContract(source)` plus `hasCurrentSourceContract(source)`. p1 remains fixed. Current workspace/export/report/rule gates preserve their existing model/run/input/build checks. `ruleCheckService.ts` sends `sourceBlockInvocation` only from a valid private method registration; manager owns the corresponding native optional Value argument/shared Rust contextual standing. Rule/analysis status updates do not rewrite producer raw.

## Projection and publication

AnalysisRun/canonical/stress-neutral derivatives preserve the source receipt and selected semantic binding, raw source hash and original row metadata. The source-block table is SHA256 `5f299065f15a157bbedf9467a598994ae684c4ecb3f851bbcb291981ec550a9f`. Known method policy and recipe IDs remain explicit; no plugin registry/framework was introduced.

Live stress publication uses private `liveStressBinding(model,result,analysisRun)`: safe known-method/native/numerical checks plus checked full content. It snapshots before async construction and rechecks before set, during rendering and capture-phase JSON/native-save/CSV activation. Pure constructor remains reference-compatible; it cannot mint native standing. Existing CSV policy remains independently authoritative. The current canonical exporter snapshots all4 inputs and rechecks content/native/method standing after async derivation.

Do not copy the entire preview service from one branch over the other. Reconcile only explicit current semantic dispatch, profile-specific validator composition and the shared native lifecycle. The numerical source-block helper rejects physics-only evidence namespaces and its stress/geometry arithmetic is the original numerical producer recipe. The combined physics-source profile needs its own reviewed table/hash, required physical evidence, selected-method coverage, geometry/stress correspondence and genuine new producer fixtures before native qualification.
