CI run [34019371445](https://github.com/sgttomas/chirality/actions/runs/34019371445) reached App registration after the Linux Runtime suite passed, then failed with `ERR_PACKAGE_PATH_NOT_EXPORTED` because the App’s CommonJS bundle eagerly required the import-only Pi coding-agent package. PR #737 was subsequently merged under owner direction with this failure unresolved.

Load both Pi SDK packages through native ESM imports when a Pi turn starts, preserving the synchronous Runtime factory and preventing the App bundle from rewriting the SDK boundary to `require()` or bundling a second provider registry. Reserve the session before loading, snapshot admitted inputs, and keep loading within cancellation and deadline handling.

Add a pinned esbuild development dependency and consumer regression coverage for CommonJS and ESM using the real SDK with offline transport. Coverage includes continuation, cold-load cancellation, close, binding revocation, deadline, capacity, input mutation and loader failure. The Runtime repair requires no frontend change.

Validation: final manager review and parent aggregate evidence pending. Do not publish this preparation draft as final validation evidence. The final body must report actual results, including failed attempts retained in the run and the exact App probe limitation.

The run’s durable entry, delegation, review and continuation evidence lives in `projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_PACKAGING_2026-09-06/`. These are derivative implementation records on the accepted migration/specification basis. A separate bundled delegated-conformance `import.meta.url` limitation remains. Supplier Candidate 2 remains interrupted without a new binary; supplier acceptance, hosted conformance, client adoption, nine holds, lifecycle and release decisions remain unchanged. Future merge requires owner direction.

Attribution: OpenAI GPT-6; exact serving model ID unavailable. HELP_HUMAN Agent 0 and native delegated CHANGE/WORKING_ITEMS/specialist roles are instruction-asserted, not mechanically enforced.
