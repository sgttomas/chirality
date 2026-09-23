# APP-REPLAY-BOUNDARY-2026-09-23 — substantive slice evidence

Candidate source: `d82568bc1fb09ff2c26ed5cb210605a1b6b538b4` on `codex/app-loop-trial`, based on `2a9b00fe9e67a4d98017833dace867a01867c591`. The App replay projection now treats foreign instruction history and basis records as identity conflicts, filters them from the selected-session view, and keeps explicit conflict diagnostics. An instruction-only conflict leaves the correctly identified transcript and its selected-session linkage intact. Runtime `/replay` derives that transcript from canonical events plus session metadata; metadata/event/transcript ID conflicts still force a rebuild from admitted events. No Runtime code or contract changed. The focused regression covers mixed events/instructions and instruction-only conflict with selected native linkage.

## Execution and review

- Mechanism: delegated-harness-native descendant of HELP_HUMAN Agent 0; this WORKING_ITEMS Agent 1 integrated all writes in the isolated worktree. Engine/provider/model: Codex / OpenAI / GPT-6. Reviewer: fresh-context read-only Type 2 TASK descendant using `software-code-review`, with no write scope and no delegation; Codex model inherited from the parent task.
- APP-HOLD-1: `dispatch` for DEL-05-04 and `accepted-dependency-consumption` for DEL-05-01/02/03/05 and DEL-04-01 returned `ALLOW` at starting `2a9b00fe`; no hold or lifecycle status was changed.
- Independent reviewer checked 100% of `2a9b00fe..d82568bc1`, including graph, pointer, source and tests, and returned PASS with no blocking finding. Reviewer also ran the replay and Session lens suites (15 passing tests), scope validator and `git diff --check`.
- Source/test/dependency inputs are listed in sorted `INPUTS.sha256`; from the repository root rerun `shasum -a 256 -c projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/INPUTS.sha256`.

## Checks on source candidate `d82568bc1`

`REGISTERED_CHECKS.json` is the runner's canonical stdout/stderr and machine result for the seven selected `software-workflow.json` checks, run from the repository root with `--timeout-seconds 600`. Its aggregate status is FAIL solely because the initial `frontend-premerge` invocation started Next without the controlled Runtime binding. The other six result entries all have exit code 0: full frontend Vitest (2,274 passed, 4 skipped), frontend/Electron typecheck, Next/Electron build, practitioner-harness self-check, practitioner-harness pytest (379 passed), and App hold integrity. The report's SHA-256 is `fe6c06b670265e59ac327b37393b39fc26454489b5f19040f58550515e723b6d`.

`PREMERGE_CHECK_CANONICAL_TMP.json` is the canonical rerun of `frontend-premerge`: exit 0, Section 8 summary PASS (8/8) and report-only Section 9 PASS (16/16). `SECTION8_SUMMARY.json` and `SECTION9_SUMMARY.json` preserve those machine results. The premerge report's SHA-256 is `63d78202070887002202b4170004d38310a1b317469e78404aa4755e85dc2de1`.

The Section 9 summary retains its original temporary log and ignored artifact paths. Their actual bytes are preserved here as `SECTION9_MANIFEST.json` (SHA-256 `6a01eb393e93948a66a19fb5a172c38efd80cbd594f4aad827f67502e410b1b8`), `SECTION9_VITEST.stdout.log` (`ad2e8a3ca6fcf78a02ac87c6dc9a1adf139638888b94a0f9aaf8c96e3ebf77bd`) and empty `SECTION9_VITEST.stderr.log` (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`). The manifest names the evaluator test files and evidence files in the committed candidate; `INPUTS.sha256` pins the slice's directly consumed source and contract files. The copy changes no result or source identity.

`git diff --check` and the sorted input hash recomputation also passed.

The check runner command was:

```text
python3 tools/software_workflow/run_registered_checks.py projects/chirality-app-dev/software-workflow.json --check frontend-test --check frontend-typecheck --check frontend-build --check frontend-premerge --check harness-self-check --check harness-pytest --check app-hold-integrity --output projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/REGISTERED_CHECKS.json --timeout-seconds 600
```

For premerge, the same runner was invoked with only `--check frontend-premerge` and the `PREMERGE_CHECK_CANONICAL_TMP.json` output. The controlled fixture was built with `node ./scripts/build-controlled-ci-runtime.mjs` from `frontend`, then run with `CHIRALITY_CONTROLLED_CI_RUNTIME=chirality-controlled-ci-runtime/v1` and `node out/controlled-ci/controlled-runtime.mjs --manifest <this checkout>/projects/chirality-app-dev/chirality.project.json`. It printed a ready line matching the registered App project and socket. Relevant effective environment for the passing premerge: `CHIRALITY_RUNTIME_SOCKET_PATH=/private/tmp/chirality-replay-runtime/runtime/control.sock`, `CHIRALITY_RUNTIME_TOKEN_FILE=/private/tmp/chirality-replay-runtime/runtime/auth/tokens/project-c37b716d-960e-46f0-a334-278e7abf3c77.token`, `CHIRALITY_RUNTIME_PROJECT_ID=chirality-app-dev`, `CHIRALITY_RUNTIME_PROJECT_ROOT=<this checkout>/projects/chirality-app-dev`, `CHIRALITY_RUNTIME_DIRECTORY=/private/tmp/chirality-replay-runtime/runtime`, `CHIRALITY_INSTRUCTION_ROOT=<this checkout>`, `HARNESS_PROJECT_ROOT=<this checkout>/projects/chirality-app-dev`, `TMPDIR=/private/tmp/chirality-replay-runtime/tmp`, and `PATH` prefixed by `/Users/ryan/dev/chirality/.venv/bin`. The runner selected an ephemeral loopback port for Next and shut it down; the controlled Runtime was stopped after the check. The token contents were not copied into evidence.

Two environment details explain the earlier failed premerge attempts: the standalone runner profile starts Next but not the controlled Runtime service that GitHub CI provisions, and macOS's default `/var/folders` TMPDIR is a symlink to `/private/var/folders`, while the shared Runtime requires canonical root paths. With the Runtime binding and canonical TMPDIR, all eight premerge checks passed. Node `v24.18.0`, npm `11.16.0`, Python virtualenv `3.13.14`, Vitest `4.1.10`. This is controlled-fixture conformance for the bounded App replay change, not a native Codex session or release claim.

## Supplied instruction and method basis

SHA-256 values are of the bytes actually read at the start revision, except the reviewer rows, which are unchanged at `d82568bc1`. The original LOOP_INIT hash precedes the pointer edit.

| Origin | SHA-256 |
|---|---|
| `AGENTS.md` | `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57` |
| `projects/chirality-app-dev/AGENTS.md` | `ef79bf154c8c68215327b6fc023ab30c610323d38a2f4ca470b455082f35e5d9` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `agents/AGENT_TASK.md` (reviewer) | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/chirality-app-dev/init/dev-loop-init-prompt.md` | `ee617f5fa910b8a43dc161f746d03b1688b7f9fb10e426541433e78b5a256cbe` |
| `projects/chirality-app-dev/loop/LOOP_INIT.md` at start | `ae3398c4467e5a4f5b84bbe4e945b901d47e15351fd99f8e28beeb29d4b4c745` |
| `workflows/construct-local-work-graph/WORKFLOW.md` | `060f7153fb8a1b75825b23a799c58de45b6538b5e95d758f777079925b121c47` |
| `workflows/construct-local-work-graph/resources/work-graph-template.md` | `67eb71ca1c85c63fda82f68d6ea610ad48e109b9a4b0f05a67961f0f79c004d7` |
| `.agents/skills/chirality-change/SKILL.md` | `2b490e172436417896c1cd25db543c676e3473aa58b7663985d75785ff7dba` |
| `.agents/skills/software-code-review/SKILL.md` (reviewer) | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |

The fractional `maxItems` floor-to-zero observation is outside this trial and remains ordinary possible DEL-05-04 work. It has a current deliverable home, so no Task Management intake is warranted here.
