# Checks and evidence lineage

## One-shot checks

| Check | Exact command | Exit/result |
| --- | --- | --- |
| APP-HOLD dispatch | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PR632-FIXTURE-IMPLEMENT-01.md --target DEL-09-04` from the App root | `0`; `ALLOW`; DEL-09-04 `CLEAR` / `NOT_HELD` |
| Ordinary-host focused suite | `./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` from `frontend` | `0`; `1` file passed; `72/72` tests passed |
| Post-fix Linux-shaped focused suite | `umask 0002` followed by the same focused Vitest command, in one shell, from `frontend` | `0`; `1` file passed; `72/72` tests passed; invoked exactly once post-fix |
| Typecheck | `npm run typecheck` from `frontend` | `0` |
| Unchanged proof-script syntax | `node --check scripts/run-packaged-launchagent-login-proof.mjs` from `frontend` | `0` |
| Exact mode/source assertion | `node projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PR632-FIXTURE-IMPLEMENT-01/exact-mode-source-assertions.mjs` from the repository root | `0`; exact `2/2` directory and `3/3` file mode coverage; product proof hash unchanged |
| Diff whitespace | `git diff --check` from the repository root | `0`; no output |
| Containment/index freeze | `git status --porcelain=v1 --untracked-files=all`; `git diff --name-only -- projects/chirality-app-dev/frontend`; `git diff --cached --quiet` | `0`; all dirt App-only; sole frontend dirt is the focused test; index empty |

An earlier inline assertion wrapper exited `1` at the zsh parser with `zsh:2: parse error near ')'`. Node never executed and no mutation occurred. WORKING_ITEMS disposition classified this as a documented no-verdict wrapper diagnostic and authorized one corrected POSIX-safe read-only assertion. No prior one-shot check was rerun.

The exact candidate-whitespace check is reserved as the terminal command after this record freeze: `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main`. Its result is reported out of band; no record is edited afterward.

## Deterministic log preservation

Three complete raw PASS logs ended with terminal blank output. Per the sealed brief they were preserved with `gzip -n -9`; the raw names were replaced by deterministic `.gz` artifacts.

| Raw log | Raw bytes | Raw SHA-256 | Gzip bytes | Gzip SHA-256 |
| --- | ---: | --- | ---: | --- |
| `focused-normal.log` | `264` | `4ec03614060f3cc5753276ef047ac33405a3c7a48e6fc3d072caa81ab7f16cac` | `212` | `56094069868c3e730f0f63d2400848cd742d4a18ba67a42860251f95b4be01e2` |
| `focused-umask-0002-postfix.log` | `264` | `a4f2b191adb5162af8bdd89fd9e2a4bb0fa5817d8b3179e41c82049bfbc00d6e` | `212` | `1d979a898aafe56660872f7a8778dacaa30b8e9d22c0b95d555534480d796a44` |
| `typecheck.log` | `136` | `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f` | `115` | `eb355223a12447bc6afe239b3e311ce8b1215f87a33ae438018bcaeb98198309` |

`gzip -cd ... | shasum -a 256` reproduced all three raw hashes exactly.

Other logs:

- `app-hold.log`: `942` bytes; SHA-256 `5e924860e02a995bdd40f677cacc745698ff054b806551baadd67378531bf8ea`.
- `exact-mode-source-assertions.log`: `402` bytes; SHA-256 `80e8707ad62505c82018066c3a84ace0f803300ae8ae54d9104ebb6372ff6d27`.
- `proof-script-syntax.log`: `0` bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
