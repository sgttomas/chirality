FAIL — one confirmed actionable finding.

**[P2] Use the product default for ordinary unpackaged launches.**

Location: `projects/chirality-app-dev/frontend/electron/main.ts:788`.

On a normal unpackaged launch without `CHIRALITY_INSTRUCTION_ROOT`, `resolveServiceInstructionRoot()` resolves the repository root (`main.ts:406–442`). Consequently, the new store seeds and restores repository `AGENTS.md`, rather than `projects/chirality-app-dev/instructions/AGENTS.md`. Fresh development profiles receive repository development guidance as their shared product instructions. Initialization preserves that mistaken seed across subsequent launches. The guarded native launcher’s staged-root override masks this path.

Minimal repair: resolve the product default explicitly for packaged resources versus source development, including intentional instruction-root overrides. Add a wiring regression with distinct repository and product contents, covering fresh initialization and Restore default. Store-only and packaged-manifest tests currently bypass this decision.

**Coverage and verification**

- Reviewed **100% of all 98 changed files**, including source, tests, instruction/governance surfaces, briefs, returns, and historical packaging/live records.
- Exact range: `85f19f019589b798331c804c4b206e34849eeab5..95b34251955650456f1473c1161763f829ca9c89`.
- Independently traced submission UUID forwarding, atomic attachment matching, replay isolation, pre-POST plan persistence, shutdown/restart classification, observation-only cancellation, and constrained panel sizing.
- Reviewed product storage/IPC, packaged source correspondence, native role materialization, instruction resolution/adoption evidence, pending-error propagation, update source/destination validation, semver, bounded fetches, and browser-only downloads.
- Scope validator: **PASS, 98 paths, zero violations**.
- Whitespace check reports only the previously disclosed intentional Markdown hard break in the verbatim historical review.
- Inspected changed regression tests and recorded validation summaries. No test suite, build, or live operation was repeated.

**Native qualification remains unresolved.** During this review, the parent reported that the corrected candidate’s existing chat returned the old instruction probe after an edit and restart. This is not a successful edited-guidance check. Public stock source confirms cold resume loads caller configuration, while idle unloading waits for shutdown; this does not establish which historical/current guidance influenced that response. Investigate the actual supplied basis and supplier history semantics before claiming edited-guidance qualification. [Cold-resume source](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/app-server/src/request_processors/thread_processor.rs), [idle-unload source](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/app-server/src/request_processors/thread_lifecycle.rs).

Remaining limits: raw-daemon cancellation concerns and prior `STOPPED_DEGRADED`/Pi-oMLX timing observations are not repaired by unrelated passing suites. Service-loss evidence covers graceful SIGTERM. Replacement packaging, owner install-over acceptance, notarization, and publishing remain separate.

Fresh independent read-only TASK, software-code-review, gpt-6-astra/high; no authorship, writes, Git mutations, private-state access, App actions, signals, or delegation. Not suitable for final fan-in until the P2 is repaired and reassessed; not owner or release approval.
