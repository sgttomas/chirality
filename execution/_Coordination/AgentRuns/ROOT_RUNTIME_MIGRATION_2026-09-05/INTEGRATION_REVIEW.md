# Runtime relocation integration review

Reviewer: /root/runtime_workspace_move, ephemeral Agent 2, OpenAI GPT-6; exact serving model ID unavailable. Role instruction-asserted, not mechanically enforced. Read-only integration review; this record is the only follow-up write. No broad tests rerun and no approval or authority inferred.

Verdict: PASS for the inspected relocation integration. No specific migration bug found.

The current diffs of `.github/workflows/harness-premerge.yml`, `desktop-release-template.yml` and `pec-tests.yml` replace source trigger, cache-lockfile and build/test working-directory paths with `projects/chirality-runtime`. Harness sparse checkout includes the enclosing projects cone and an explicit runtime project entry; the latter is redundant but harmless. PEC sparse checkout includes both PEC and its runtime dependency. Desktop uses a full checkout. All three build the runtime before installing/building their consumers. Harness retains runtime tests; PEC newly triggers when its runtime dependency changes, while keeping its workspace tests. Existing unsigned desktop artifact conditions and operational runtime user-data/socket/token paths remain unchanged.

Searches across Root `tools/` and `.github/workflows/` executable surfaces found no active old runtime source-location reference. Matches under runtime user-data sockets, frontend dist-runtime artifacts and `tools/workflow_runtime` are separate operational/generated/tool locations, not missed source moves. Historical documents were not classified as executable-path failures.

Recomputed SHA-256 for every SOURCE_RELOCATION.json destination: 79 checked, 79 unchanged. App's seven top-level runtime file dependencies resolve to existing destination packages. Installed App node_modules/@chirality runtime/engine links resolve to projects/chirality-runtime; its harness-contract link remains project-local. PEC's two runtime file dependencies and installed node_modules links resolve to the new runtime project. No installed runtime/engine link inspected resolves to the former Root runtime directory.

This inspection supports the migration candidate's source/build integration only. Runtime and consumer test evidence remain in their respective run returns; exact ownership transfer, release acceptance and publication are separate parent/owner decisions.
