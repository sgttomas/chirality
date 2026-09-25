# Frontend review findings

## FE-01 — P1: refuse source-blocks at the legacy report-package boundary

Location: `apps/desktop/src/features/report/reportPackageRequest.ts:132` (new broad admission), with the loss at lines236–238 and the legacy envelope at291 onward.

A genuine source-blocks-1 result from the maintained full-UI N05 dense request reaches the actual frontend native registrar through simulated IPC, passes numerical standing, and builds a verified manifest/AnalysisRun. `buildReportPackageRequest` now accepts it through `hasCurrentSourceContract`. However, `reportMetadata` cannot express Fx/Fy/Fz/Mx/My/Mz or `recovered_from_assembled_support_law`, and its required-metadata check excludes the reaction family. The returned legacy report request contains all **12 signed support component rows with metadata:null** and no per-row disclosure of this loss. In particular, the -1e-8 N*m spring Mx remains a magnitude with no structured component/frame/location/basis/sign metadata. The envelope also has no source recovery receipt or structured producer/semantic-contract binding for the new method. A textual method mention elsewhere is not this missing structured evidence.

[GENUINE_SOURCE_REPORT_REQUEST.json](GENUINE_SOURCE_REPORT_REQUEST.json) is the actual frontend request produced by the probe; [SIGNED_ZERO_NODE_OBSERVATIONS.json](SIGNED_ZERO_NODE_OBSERVATIONS.json) records source versus exported support metadata. This is a genuine received producer pair passed through actual frontend functions with mocked transport, not a new producer or native package execution.

Remedy: explicitly refuse source-blocks-1 in this unchanged legacy report constructor (and expose its unavailable status at the relevant call boundary). Keep the deliberate versioned report-contract extension in its existing graph home; do not add a new report format in this repair. ROOT confirmed this existing policy during review. A native token/hash cannot restore removed physical meaning. Add a genuine-pair refusal test and retain ordinary precision/legacy report behavior.

## FE-02 — P2: bind the caller model and serialized native input consistently

Location: `apps/desktop/src/features/results/sourceBlockRecovery.ts:207`, composed with `services/previewService.ts:94,127` and the unchanged manifest's structured clone.

With only the initial in-memory caller model's root X changed from +0 to -0, the native capture serializes and sends +0. The complete actual request field values are **identical to the unchanged genuine N05 request** (all keys retained; JSON object insertion order is immaterial). The actual frontend registrar reports native provenance true, and the method standing against its captured request model is eligible. But `sourceBlockStanding` compares the original caller model with Object.is semantics against the serialized model and returns `SOURCE_BLOCKS_VALIDATED_INVOCATION_REQUIRED`; the manifest preserves the original -0. The +0 control passes. Thus a legitimate result can be withheld by Current/export/rule consumers solely because they check a different model representation than the one captured and sent. The workspace clone can normalize the solve copy too, while export callers still receive the original UI model.

[DIRECT_NODE_RUN.json](DIRECT_NODE_RUN.json) records the final bounded run (exit1 is the deliberate failing invariant, not a setup failure), and [SIGNED_ZERO_NODE_OBSERVATIONS.json](SIGNED_ZERO_NODE_OBSERVATIONS.json) records both controls. The producer carrier was not changed or rehashed. The original actual request, mode and material-override shape remain unchanged; only the caller's pre-serialization zero sign differs.

Remedy: retain/bind the pre-serialization caller snapshot separately from the exact actual dispatched request, or otherwise define and enforce their normalization relationship at the actual private native boundary. Use the corresponding captured model for downstream standing. Do not merely erase all zero signs: existing source/projection-bit and captured-invocation post-validation mutation defenses must remain. Add the initial-negative-zero positive control plus source/model/invocation mutation negatives.
