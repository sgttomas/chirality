# Containment implementation brief

Parent: runtime implementation manager. Executor: ephemeral Agent 2, OpenAI GPT-6; exact serving model ID unavailable; role not mechanically enforced, instruction-asserted. No delegation.

Authority: IMPLEMENTATION_AMENDMENT_4.json and parent sealed dispatch. Write scope: packages/daemon/src/codex-containment.ts, tests/codex-containment.test.ts, and this evidence directory only. Tools: full available capabilities within current host policy, per explicit user direction.

Implement macOS sandbox-exec profile generation, minimal isolated environment and conservative Codex configuration. Verify real subprocess offline denial of outside writes, ambient file reads and socket creation, and permitted project write. No hosted turn, credentials, account operations, operational registry or production writes. Provider transport consent must come from trusted operator configuration; a structural JavaScript object is not proof of human authorization. Hosted network allowance must not be presented as command network enforcement.

Acceptance: focused tests and actual macOS sandbox probes; explicit limitations and safe cleanup that removes only newly created session files. Supplied privateDirectory and CODEX_HOME must already be private, canonical directories; no cleanup of supplied account directories.
