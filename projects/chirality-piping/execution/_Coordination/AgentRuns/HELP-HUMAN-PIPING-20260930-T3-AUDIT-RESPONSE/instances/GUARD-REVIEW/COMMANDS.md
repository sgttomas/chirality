# Review commands and results

Working directory: Git repository root. `Run` uses REVIEW.md's repository-relative
alias. Python: 3.13.7, Clang 16.0.0 build metadata as retained in FROZEN_SCOPE.json.
No toolchain executable was invoked. Python executions set
`PYTHONDONTWRITEBYTECODE=1` where an import could create bytecode.

1. Read `AGENTS.md`, `agents/AGENT_TASK.md`, the Piping AGENTS, sealed review
   brief and software-code-review skill; retain actual hashes in CONTEXT.json.
   Read the complete guard and meaningful tests with `nl`, `sed`, and `cat`.
   Read supporting prose/JSON/script records and inspect SDK declarations using
   bounded `rg` and `sed`. Some initial batched displays exceeded the output
   limit; separate bounded reads recovered the required guard/test/doc bodies.
2. ROOT clarified read-only Git permission. Run `git diff --stat`, and use
   `git diff --name-only`, `git diff --binary` and `git show <sha>:<path>` through
   standard-library subprocess calls for the two exact base/candidate pairs
   in FROZEN_SCOPE.json. All 109 paths, candidate bytes and worktree bytes agree;
   binary diffs agree. Git source is canonical: only diff hash and blob/path
   inventory are retained, not a duplicate whole-diff snapshot.
3. Run
   `PYTHONDONTWRITEBYTECODE=1 python3 Run/instances/GUARD-IMPLEMENTATION/test_host_guard.py`.
   Redirect stdout/stderr to `Run/instances/GUARD-REVIEW/pure-tests.log`.
   Exit 0: 41 tests pass. The supplied test harness patches live process,
   signal, provider and socket capabilities before import and in each test.
4. Run
   `PYTHONDONTWRITEBYTECODE=1 python3 Run/instances/GUARD-REVIEW/check_compile_schema.py`.
   Redirect stdout to `compile-schema-results.json`. Exit 0: a correct cargo
   build and all three reported problematic argv forms are accepted. This
   reproducer reuses the supplied capability fence and fake file strategy;
   no Cargo/rustc command, process, real provider or signal is invoked. Its
   success means reproduction of the current defect, not that the jobs are safe.
5. Standard-library integrity inspection, recorded in RECORD_CHECKS.json:
   iterate frozen changed paths; parse JSON with `json.loads`, Python with
   `ast.parse`; hash each manifest target with SHA256. Guard manifest entries
   use repository root; other manifests use their containing directories.
   Compare all nine SDK header hashes from GUARD-IMPLEMENTATION/CONTEXT.json
   against the installed CLT MacOSX26.5 SDK. All checks pass: 83 entries,
   42 JSON and 10 Python files, 9 SDK hashes. No helper scripts are executed.
6. Supplementary static checks in SUPPLEMENTARY_CHECKS.json: hash 36 source
   blobs with `git show 3bddc2b...:<descriptor-path>` and compare snapshot
   descriptor digests; hash the 64 I21 INPUTS.json target files; inspect stored
   provisional result counts/status. All hashes match. No runtime snapshot,
   compiler, model, layout witness, historical oracle or formula is executed.
7. Seal CONTEXT.json, REVIEW.md and evidence SHA256SUMS within the owned folder.
   FROZEN_SCOPE.json includes the exact commands' revision inputs and per-file
   blobs. RECORD_CHECKS/SUPPLEMENTARY_CHECKS preserve individual check results.

No denial is represented as a pass. This assignment does not run hosted CI,
GEN-8, DEC-025, a native guard witness or an independent solver experiment.
ROOT's separately relayed hosted-check/GEN-8 results were not re-witnessed here.
Read-only Git used no fetch, stage, commit, ref/worktree or index mutation.
No network, installation or delegation occurred. The shared filesystem write
fence is prompt-only, and no complete host-wide write audit is claimed.
