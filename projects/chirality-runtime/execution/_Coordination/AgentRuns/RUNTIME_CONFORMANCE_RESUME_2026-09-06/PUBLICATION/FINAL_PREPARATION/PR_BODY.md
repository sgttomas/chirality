The App daemon failed during CommonJS startup because Runtime eagerly loaded the ESM-only Pi SDK (`ERR_PACKAGE_PATH_NOT_EXPORTED`, CI run 34019371445). Runtime now uses native dynamic imports when a Pi turn starts, while preserving cancellation, deadlines, capacity, and synchronous factory behavior. The final App-equivalent bundle reaches the Electron API boundary locally; actual Electron registration still needs fresh CI.

This Runtime-only continuation also addresses failures found in actual Codex candidate runs:

- Disable startup shell snapshots and verify exact policy readback.
- Validate supplier network callback tokens without weakening general identifier checks or inventing unsupported decisions.
- Join interruption, failure, and completion to one generation-bound retirement attempt; do not publish a terminal after failed reconciliation.
- Close the owned transport through bounded EOF/TERM/KILL phases, preserve cleanup errors, and restrict signals to original process ownership.

Validation: build/typecheck pass; the final registered Runtime suite has **560 passed, 14 skipped, zero failed**. All 22 changed source/test/manifest files match the tested generation. Governance entrypoints/G0–G4, Runtime status/drift and self-check pass; all 43 accepted basis hashes remain unchanged. Global candidate-whitespace passes after losslessly archiving exact original evidence bytes and declaring readable presentations as derivatives.

Actual no-account tests use separately identified, unaccepted suppliers. Candidate2 passes public normal retirement, primary/child cancellation and timeout scenarios, primary network allow and host-interrupt cancellation with durable attribution, native OFF/ON controls, and controlled role/read tests. These retain their controlled-launcher and production-role-envelope limitations; returned interrupted-event parity is unresolved. Native ask fails closed with `FOREIGN_PRIMARY_TURN`, and ask-deny is unsupported by the observed supplier decision dialect.

Candidate2 exposed a confirmed foreign write through a project symlink in its filesystem helper. Separately built Candidate3 corrects helper-default policy broadening; its source tests pass and bounded P1 passes. The unchanged protected-path star fixture executes all 24 probes, observes primary/child alias EPERM, successful project patch controls, and unchanged monitored host files, but still **fails** its known MATCH classifier. Three other families, ambiguous creation-denial evidence, immutable leaves, and full selected-supplier conformance remain open. Candidate2 results are not transferred to Candidate3, and the accepted supplier pin is unchanged.

Protected-fixture maintenance remains stopped after two automatic screening rejections. Native approval ancestry/liveness/durable provenance is prepared for owner discussion before any significant design change. No supplier acceptance, client adoption, hold release, lifecycle promotion, hosted-account acceptance, or product release is implied. A future merge requires owner direction.

Durable evidence and fresh-entry handoff are under `projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CONFORMANCE_RESUME_2026-09-06/`, with the earlier packaging snapshot under `RUNTIME_PACKAGING_2026-09-06/`. Failed attempts and historical seals remain recoverable through `PUBLICATION/LOSSLESS_PRESENTATION_V1/ORIGINALS.json` and `LOSSLESS_PRESENTATION_V2/ORIGINALS.json`. Fresh Linux Runtime/App registration, governance, and PEC CI will be recorded in the publication supplement.

OpenAI GPT-6; exact serving model ID unavailable. HELP_HUMAN Agent 0 and actual native manager/specialist roles are instruction-asserted.

🤖 Generated with [Codex](https://openai.com/codex/)
