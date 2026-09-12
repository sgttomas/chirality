# I_STAGE13_PREP — RETURN

Type 2 TASK return. Stage13 (R4) packaging procedure prepared from the completed Stage12 (R3) procedure. Nothing was executed beyond read-only checks; no build, npm install, packaging, codesign, launchctl, or GUI launch was run. `/private/tmp/chirality-local-human-trial-20260910-12`, the preserved checkout, `/Users/ryan/Applications`, `/Users/ryan/Library` and the lead worktree (other than this RETURN directory) were not modified (verified with `find …-12 -newermt "2026-09-10 21:00"` → empty; preserved checkout `git status` clean at HEAD `769f8ef0`).

## Deliverables

- Stage13 directory: `/private/tmp/chirality-local-human-trial-20260910-13` (created 0700, uid 501; every file create-only, scripts 0700, records 0600).
- Procedure: `/private/tmp/chirality-local-human-trial-20260910-13/STAGE13_PROCEDURE.md` (preflight 0a–0e, steps 1–26, section B "before first GUI launch").
- Derivation manifest: `/private/tmp/chirality-local-human-trial-20260910-13/stage13-derivation-manifest.json` (Stage12→Stage13 substitution rules and per-file source/output identities for the 13 script copies, 2 JSON copies and 19 templates; the seven new helper scripts, the expected launcher diff and the procedure are not in it — see inventory).

## Inventory (SHA-256)

45 files.

| path (relative to Stage13 root) | size | mode | sha256 | origin |
|---|---|---|---|---|
| `STAGE13_PROCEDURE.md` | 27365 | 600 | `f58df1b0f4145f0bd121795f7816ce9ef2072255500c59b91a58add56f71f27e` | new (Stage13 helper) |
| `build-plan.json` | 3549 | 600 | `645adf12a5ab458c4955cccc1141177ebdf28f9976dba528c8aa0d33c7a8bc7a` | Stage12 copy |
| `check-admitted.mjs` | 964 | 700 | `4aa6394694ecaca710dd8c3984ad80c81fe4f7e916696e0df22f1205179e12bb` | Stage12 copy (byte-identical) |
| `compare_macho.py` | 3558 | 700 | `181a4be5234508f19141a6288e13a608180e0bc1f00301dc6a266f62cc1843a2` | Stage12 copy |
| `derive-account-free.py` | 5299 | 700 | `818c228dc8d014be4e8d9ba1a71ef7e8bdb30bfdbcfbffdca00bdd143f94a5a2` | new (Stage13 helper) |
| `derive-final.py` | 8114 | 700 | `27c52c998e07b267eaf8e679d9427ab8b1e6520dd77d85ae2b9b99d76dabb99a` | new (Stage13 helper) |
| `derive-governance.py` | 7141 | 700 | `d8e51c998b9d167ae27221ef7131b114940eab0b721b98c2428d9181869dd0b4` | Stage12 copy + semantic patch |
| `derive-launcher.sh` | 2470 | 700 | `eba1b0dd5ac16fca797f533eb346d9740f705f0d0e16c9ffd2401f478c0e4017` | new (Stage13 helper) |
| `derive-measure.mjs` | 2717 | 700 | `3aa293567b53a2cb98f2d02c4dcf2c23289f6a64fe1f8b31de961c80dcac555f` | Stage12 copy |
| `derive-payload.py` | 5061 | 700 | `3812c9748266badb77660a3b6c10162397e12c78df5424337f6f3944aa50cc65` | new (Stage13 helper) |
| `derive-post-seal.py` | 2785 | 700 | `a95021356594f8d3e861963577769933be01d92804746777d62281ed51eb2516` | Stage12 copy + semantic patch |
| `derive-profile.py` | 1704 | 700 | `ba6a274902d9e0b2c512acf0b3f6d9e16e6afc06e8d35f1025280119045e4f4c` | new (Stage13 helper) |
| `derive-seal.mjs` | 3933 | 700 | `c7e6d141eb2526f54b5f514bd7d86cf40d129269ddd33b29fd3eea52aa0a2cb8` | Stage12 copy |
| `derive-stage13-from-stage12.py` | 13141 | 700 | `5dfde62358ed3d85216bf469727a663a388c536c704f1ba3e8a20099aafe319f` | new (Stage13 helper) |
| `derive-wrapper.py` | 5015 | 700 | `67e05cff69e7cf7ac3ed9cc3e0611bfd26885ed545051b49a4087e797d6cdec9` | new (Stage13 helper) |
| `execute-durable-copy.py` | 2495 | 700 | `57d46503b32e3364ade7dd83a7881c49cc79de0e959d0d6da625c78b1238e07d` | new (Stage13 helper) |
| `execute-plan.py` | 1648 | 700 | `6bb43c956c5af0fdc5c0f7a71afa73a669de9dfc0d339796bfc2e5f8318c40b5` | Stage12 copy (byte-identical) |
| `generate-candidate-evidence.py` | 4011 | 700 | `8f5d8fabdfe536dd2c0b146c1e79f36d6e8cd5a3ba58d2981c26bb4e466a5770` | Stage12 copy |
| `launcher-r3-r4.expected.diff` | 992 | 600 | `2ad7ed40eb29d3487623eb329a3255ab01c490ea59cfccc2db2e8331aaa8413e` | new (Stage13 helper) |
| `run-build.py` | 6264 | 700 | `3b5ad209c47ab403aa611c7f4445de905f2f2eee08e92f1d65b1ff52ea09430c` | Stage12 copy |
| `run-measure.py` | 2571 | 700 | `824a9a65b3e8862825b6aa004a380542b6486881f902a56b59fe05266181d0f8` | Stage12 copy |
| `run-wrapper.py` | 3143 | 700 | `40a99d1caf66a32ad231a0de156f683ef0b20f174e949a53d632b683d7b0e709` | Stage12 copy |
| `stage12-static-reuse-baseline.json` | 4137 | 600 | `6292b71dbc7aef1093abd73cdc52b89a7299737e21c26a049b76cf7567aa21e9` | Stage12 stage11-static-reuse-baseline.json, schema relabelled |
| `stage13-derivation-manifest.json` | 22076 | 600 | `812ce68440fde3f5bf1d1dfca5e07c0237b8c2322c0d35f3f9053221bbcbd41b` | new (Stage13 helper) |
| `templates/account-free-observer-invocation.template.json` | 5514 | 600 | `b8491eda57c78f8a6bfeb284f884868e1541fc1ec804327fb89fe31d8415ddd7` | template from Stage12 record |
| `templates/account-free-observer-plan.template.json` | 5045 | 600 | `19a1b482cb110ba233f3bc63ed6563af65f8508bbc6ce605cedd8369c7b00feb` | template from Stage12 record |
| `templates/build-invocation.template.json` | 9343 | 600 | `18de64aaf1fb79180c2ea5b064a0ac5f48d94979ead618594055cfcd02a43266` | template from Stage12 record |
| `templates/durable-copy-invocation.template.json` | 2289 | 600 | `7bcbc92aeef647cf667b1779c655983d8f06fca2cebd8639c7cbfb13d1ad053b` | template from Stage12 record |
| `templates/durable-copy-plan.template.json` | 1894 | 600 | `fcbe0956b6ff79f3b33e464393c61697367d114b2f34917892370975356f4006` | template from Stage12 record |
| `templates/final-observation-invocation.template.json` | 4638 | 600 | `0ea70f5e5a3373764a6c8cdc9499a0a3ef5b7d7d939ceaf10d511fcac5c82f25` | template from Stage12 record |
| `templates/final-observation-plan.template.json` | 4284 | 600 | `63c62a9289c15b0bd2871d0e0654f8278c6214bf20b291f3d42ffb2ef8cd10f4` | template from Stage12 record |
| `templates/governance-invocation.template.json` | 5031 | 600 | `f83c6accb47e4c7a8f56eadf1e74bb26c5c9826da3ae98fafcca7a089729000b` | template from Stage12 record |
| `templates/governance-plan.template.json` | 4649 | 600 | `709893183bce6bae95a42adba4491add263fa798b15526aec5e12b9ca84dcd30` | template from Stage12 record |
| `templates/measure-support-invocation.template.json` | 3436 | 600 | `d0ce80555eb721269e9243e0b93d44d997c13fc497222f4531b683f92c4a8da5` | template from Stage12 record |
| `templates/measure-support-plan.template.json` | 3003 | 600 | `b104d40bdeece92babd2970ae5c29fb3cbf343e40c2808cf3d4aacdead84c4c4` | template from Stage12 record |
| `templates/payload-invocation.template.json` | 5343 | 600 | `b3597a3201a26b9be24907fc2601b48757fcce4af6634e7f72dd80b467f79608` | template from Stage12 record |
| `templates/payload-plan.template.json` | 5029 | 600 | `11b42ca24e9dd96cd70f9fdf8e81ce1c4555459f2773c1c29beefad29e145199` | template from Stage12 record |
| `templates/provision-invocation.template.json` | 6982 | 600 | `1e0cb09471c3e3c820a898499b7c6da75b4d7df3fcf3c3c0be17816b67aad96c` | template from Stage12 record |
| `templates/provision-plan.template.json` | 6708 | 600 | `f1a94d1409ec0fb988b3e0d3b8e3b4f25b8276eaab8fce435fd5b2402c233dd9` | template from Stage12 record |
| `templates/seal-invocation.template.json` | 7698 | 600 | `846aee4ae7ace5876a5bcf3ff4ae2ce0b02f5117dfcad65a7d381553c0890c48` | template from Stage12 record |
| `templates/seal-plan.template.json` | 7335 | 600 | `66a23f90895aaa5a71fa71c363b9ec1de0154270681b24fc17615856cd06af38` | template from Stage12 record |
| `templates/wrapper-invocation.template.json` | 10803 | 600 | `40ddf4a1a609d4a6e9d2c776ee51af60f8466f800e0ee138366456c4e107f59d` | template from Stage12 record |
| `templates/wrapper-plan.template.json` | 10010 | 600 | `7cc731a309102082b3efdbf4524f79623ca761311b71c086496c9defc3f4faae` | template from Stage12 record |
| `verify-copy.py` | 3453 | 700 | `f7698bed5d11de2990591cf44a4486c6533dfe0be83059c2962406cb568349e0` | Stage12 copy |
| `verify-runtime-consumer.mjs` | 2178 | 700 | `645c7cb6813c9b3a18821044e6c4a37fc3d3358898cbda75b050872c00ee0bbc` | Stage12 copy |

## Substitutions made (Stage12 → Stage13)

Applied by `derive-stage13-from-stage12.py` to every copied script/record, in this order (earlier rules shift prior-stage references one stage later so Stage12 becomes the "prior stage"):

- `20260910-12` → `20260910-13`
- `20260910-11` → `20260910-12`
- `stage12` → `stage13`
- `stage11` → `stage12`
- `Stage12` → `Stage13`
- `Stage11` → `Stage12`
- `Chirality Trial 20260910 R3` → `Chirality Trial 20260910 R4`
- `Chirality Trial 20260910 R2` → `Chirality Trial 20260910 R3`
- `-r3-build` → `-r4-build`
- `R3 durable` → `R4 durable`
- `R2 durable` → `R3 durable`
- `create-only R3` → `create-only R4`
- `awaiting-R3-` → `awaiting-R4-`
- `R3 userdata` → `R4 userdata`
- `R3 copy` → `R4 copy`
- `launcher-r2-r3` → `launcher-r3-r4`

Kept unchanged: `repositoryRoot`/`runtimeRoot`/`frontendRoot` = preserved checkout `/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality`; node `24.18.0` and tsc paths; signing identity `C7F111429F7AC5085484A9DF6F5AE7CFF552DEEF`, team `8A7JL35U4S`, bundle `com.chirality.app`; Supplier source root `/private/tmp/chirality-supplier-release-20260910-02/evidence/trial-supplier-build-04/artifact`; XPC/grouped records; activation ids `codex-mvp-human-trial-20260910-login/-worker`, gate `D36`; expiry `2026-10-10T22:43:56.184Z`; admitted digests (dependency `e83a525c…`, Supplier tree `c1809bb5…`, Supplier exe `87162386…`, native addon `fa40fc23…`); owner-direction reference sha `d52aa1c4…`. `build-plan.json` keeps `"status": "ready-frozen-source"` verbatim from Stage12.

Semantic patches beyond substitution (both replay-verified against Stage12 data):
- `derive-governance.py`: Stage12 hard-coded the Stage12 profile digest `358a762b…` and `issuedAt 2026-09-11T02:35:00.000Z`. Stage13 takes `--expected-profile-digest <64 hex>` and `--issued-at <ISO ms UTC, before the expiry>`, and additionally checks the published `stage13-support-profiles.json` is exactly `[measured profile]`.
- `derive-post-seal.py`: Stage12 overwrote `verify-copy.py` non-create-only. Stage13 compares the pre-created `verify-copy.py` to its Stage12 derivation and only creates it if absent (verified: the Stage13 copy equals the derivation byte-for-byte).
- Generator fix during prep: template records that are *not* Stage13-fresh (prior-stage basis records, external tool/record files) keep their real Stage12-verified `size`/`sha256`; only Stage13-produced paths carry placeholders.

New Stage13 helper scripts (Stage12 performed these steps ad hoc without a script; each reproduces the exact Stage12 record shape and key order, create-only, 0600 outputs):
- `derive-wrapper.py` (step 3) — `wrapper-plan.json` from `build-invocation.json` + 14 baseline static inputs (re-hashed) + fresh emitted/generated files (re-hashed and compared to the build record) + 11 build records; basis Stage12 `wrapper-invocation.json`; env from basis with root substitution and explicit expected-value checks; `stage: "13"`.
- `derive-profile.py` (step 8) — publishes `[profile]` from `measure-support.stdout` after verifying the measurement invocation succeeded and the stdout hash matches.
- `derive-account-free.py` (step 10) — fresh recipe (new `runId`, supplier/native digests from the profile and cross-checked against the checkpoint `nestedSignatures` content, evidence digests, profile digest) and `account-free-observer-plan.json`.
- `derive-payload.py` (step 12) — byte copy `nested-signed-checkpoint.historical.json` + `payload-plan.json` (explicit env, checked key-for-key against the Stage12 basis).
- `execute-durable-copy.py` (step 19) — runs the planned `ditto` and records `durable-copy-invocation.json` (Stage12 shape incl. `exit`, `stdout`, `stderr`).
- `derive-final.py observation|provision` (steps 21/23) — `stage13-final-operation-arguments-sealed.json` + `final-observation-plan.json`; then byte-identical `trial-observation.json` + `provision-plan.json`.
- `derive-launcher.sh` + `launcher-r3-r4.expected.diff` (step 25) — sed-derives the R4 launcher from the R3 launcher (sha `d1c0813b…` checked), create-only 0700, records `diff -u -L … -L …` and compares it to the expected diff (exactly the `app_executable`, `user_data`, and usage lines). Expected R4 launcher sha256 `31b87f4fed7cfbab6ad4b1cf051f9af004e5af296998295c8d803faeb04522bb` (computed in the scratchpad; nothing was written under `/Users/ryan/Applications`).

## Placeholders

Templates under `templates/` are reference shapes only (each carries a `_template` note); the real records are produced by the named script at the named step. Placeholder forms: `<DERIVED-AT-STEP-N-BY-script>` (plan records), `<RECORDED-AT-STEP-N-BY-script>` (invocation records), `<FROZEN-COMMIT-…>`. No hash was invented.

| template | placeholders present |
|---|---|
| `templates/account-free-observer-invocation.template.json` | `<RECORDED-AT-STEP-11-BY-execute-plan.py account-free-observer>` |
| `templates/account-free-observer-plan.template.json` | `<DERIVED-AT-STEP-10-BY-derive-account-free.py>` |
| `templates/build-invocation.template.json` | `<RECORDED-AT-STEP-2-BY-run-build.py --execute>` |
| `templates/durable-copy-invocation.template.json` | `<RECORDED-AT-STEP-19-BY-execute-durable-copy.py>` |
| `templates/durable-copy-plan.template.json` | `<DERIVED-AT-STEP-18-BY-derive-post-seal.py>` |
| `templates/final-observation-invocation.template.json` | `<RECORDED-AT-STEP-22-BY-execute-plan.py final-observation>` |
| `templates/final-observation-plan.template.json` | `<DERIVED-AT-STEP-21-BY-derive-final.py observation>` |
| `templates/governance-invocation.template.json` | `<RECORDED-AT-STEP-15-BY-execute-plan.py governance>` |
| `templates/governance-plan.template.json` | `<DERIVED-AT-STEP-14-BY-derive-governance.py>` |
| `templates/measure-support-invocation.template.json` | `<RECORDED-AT-STEP-7-BY-run-measure.py --execute>` |
| `templates/measure-support-plan.template.json` | `<DERIVED-AT-STEP-6-BY-derive-measure.mjs>` |
| `templates/payload-invocation.template.json` | `<RECORDED-AT-STEP-13-BY-execute-plan.py payload>` |
| `templates/payload-plan.template.json` | `<DERIVED-AT-STEP-12-BY-derive-payload.py>` |
| `templates/provision-invocation.template.json` | `<RECORDED-AT-STEP-24-BY-execute-plan.py provision>` |
| `templates/provision-plan.template.json` | `<DERIVED-AT-STEP-23-BY-derive-final.py provision>` |
| `templates/seal-invocation.template.json` | `<RECORDED-AT-STEP-17-BY-execute-plan.py seal>` |
| `templates/seal-plan.template.json` | `<DERIVED-AT-STEP-16-BY-derive-seal.mjs>` |
| `templates/wrapper-invocation.template.json` | `<RECORDED-AT-STEP-5-BY-run-wrapper.py --execute>` |
| `templates/wrapper-plan.template.json` | `<DERIVED-AT-STEP-3-BY-derive-wrapper.py>` |

Procedure-level placeholders: `<FROZEN_COMMIT>` (lead-frozen commit on `claude/chirality-v3-mvp-trial-ab05cb`; candidate at prep time `fdb8c8e18c57345d53a0cf6e3d816acaeded0b65`), `<PROFILE_DIGEST>` (printed at step 8), `<OUTER_INVENTORY_SHA256>` (from step 17), `--issued-at` (real issue time at step 14).

## Dry run

Command: `cd /private/tmp && /usr/bin/python3 /private/tmp/chirality-local-human-trial-20260910-13/run-build.py --check --expected-commit 769f8ef0626396d3f07e455186c0c220fac43ffb` (current HEAD of the preserved checkout, branch `codex/chirality-change-lessons-20260910`). Exit 0. Stdout (exact):

```json
{
  "status": "PASS",
  "frozenCommit": "769f8ef0626396d3f07e455186c0c220fac43ffb",
  "dependencyResolutionDigest": "e83a525c2c38ce267abdaa0a25d26cab97baf9bc3acaa1c8e14e5ae86366b202",
  "commands": [
    {
      "name": "runtime-clean",
      "cwd": "/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality/projects/chirality-runtime",
      "argv": [
        "/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node",
        "/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality/projects/chirality-runtime/node_modules/typescript/bin/tsc",
        "-b",
        "--clean"
      ]
    },
    {
      "name": "runtime-build",
      "cwd": "/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality/projects/chirality-runtime",
      "argv": [
        "/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node",
        "/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality/projects/chirality-runtime/node_modules/typescript/bin/tsc",
        "-b",
        "--pretty",
        "false"
      ]
    },
    {
      "name": "runtime-consumer-resolution",
      "cwd": "/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality/projects/chirality-app-dev/frontend",
      "argv": [
        "/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node",
        "--experimental-import-meta-resolve",
        "/private/tmp/chirality-local-human-trial-20260910-13/verify-runtime-consumer.mjs"
      ]
    },
    {
      "name": "next-build",
      "cwd": "/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality/projects/chirality-app-dev/frontend",
      "argv": [
        "/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node",
        "./node_modules/next/dist/bin/next",
        "build"
      ]
    },
    {
      "name": "electron-build",
      "cwd": "/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality/projects/chirality-app-dev/frontend",
      "argv": [
        "/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node",
        "./scripts/build-electron.mjs"
      ]
    }
  ]
}
```
Stderr: (empty)

It passed first time (no tooling fix was needed for the check path): frozen commit matched, Runtime/frontend tree clean, `check-admitted.mjs` recomputed the admitted dependency and Supplier-tree digests, Supplier executable and native addon hashes matched, all 15 Stage12 static reuse inputs unchanged, the three R4 durable paths absent, no Stage13 execution output present.

Other read-only check modes: `run-wrapper.py --check` and `run-measure.py --check` need `wrapper-plan.json` / `measure-support-plan.json`, which only exist after the build; run now they fail exactly as expected:
```
FileNotFoundError: [Errno 2] No such file or directory: '/private/tmp/chirality-local-human-trial-20260910-13/wrapper-plan.json'
FileNotFoundError: [Errno 2] No such file or directory: '/private/tmp/chirality-local-human-trial-20260910-13/measure-support-plan.json'
```
Launcher `--check-only` was not run (the R4 launcher must not exist yet); the derivation is delivered as `derive-launcher.sh` plus the expected diff.

Syntax checks: `py_compile` on all 15 `.py`, `node --check` on all 4 `.mjs`, `zsh -n` on `derive-launcher.sh` — all clean.

## Replay verification of the new/patched scripts (scratchpad only)

Scratch copies of the seven derivation scripts were re-pointed at Stage12 inputs (stage=…-12, prior=…-11, outputs to the scratchpad; test-only relaxations: build `frozenCommit` taken from the record because HEAD has moved, the already-payload-bound Stage12 checkpoint replaced by its nested-signed historical copy, and the existing R3 app tolerated). Outputs compared to the real Stage12 records:
- byte-identical: `stage12-support-profiles.json`, `nested-signed-checkpoint.historical.json`, all four `worker-prerequisites/*.json`, `stage12-governance-recipe.json`, `durable-copy-plan.json`, `stage12-final-operation-arguments-sealed.json`, `trial-observation.json`, `release-inputs-inspection.json`, `payload-bound-checkpoint.historical.json`;
- structurally identical with only the expected differences: `wrapper-plan.json` (`stage` 12→13 only), account-free recipe (`runId` only), `account-free-observer-plan.json`, `payload-plan.json`, `governance-plan.json`, `final-observation-plan.json`, `provision-plan.json`, `seal-plan.json` (paths/hashes of scratch outputs or the historical checkpoint only).
`derive-measure.mjs` could not be replayed (it needs an unsealed candidate payload) — it is an unchanged Stage12 tool with path/label substitution only.

## Things in Stage12 tooling that would have blocked Stage13 (all addressed)

1. `derive-governance.py` literal Stage12 profile digest and issuedAt → CLI arguments (above).
2. `derive-post-seal.py` overwrote `verify-copy.py` → equality check against the pre-created copy.
3. Eight steps had no script in Stage12 (wrapper plan, profile publication, account-free recipe/plan, historical checkpoint + payload plan, durable-copy execution record, final-operation arguments + observation plan, observation publication + provision plan, launcher derivation) → seven new scripts + expected diff.
4. `derive-payload.py` first draft derived its environment from the basis record by root substitution, which would have carried `stage12-support-profiles.json` into the Stage13 env — caught by replay, fixed to an explicit environment checked key-for-key against the basis.
5. Generator glob initially treated `build-plan.json` as a template (KeyError) → excluded; and non-fresh template records initially lost their real hashes → fixed.

## Findings the lead should act on

- The preserved checkout is on branch `codex/chirality-change-lessons-20260910` at `769f8ef0` and does **not** contain `electron/runtime-autostart.ts`. The lead worktree is at `fdb8c8e18c57345d53a0cf6e3d816acaeded0b65` on `claude/chirality-v3-mvp-trial-ab05cb` (769f8ef0 is its ancestor; 86 Runtime/frontend files change; `RUN_LOG.md` is modified but uncommitted there). Both share `/Users/ryan/dev/chirality/.git`, so the frozen commit is already reachable from the preserved checkout: preflight 0a uses `git checkout --detach <FROZEN_COMMIT>` (the branch itself is checked out in the lead worktree).
- Between `769f8ef0` and `fdb8c8e1` none of the 15 static reuse inputs changes (empty `git diff` for `package.json`, both lockfiles, the three packaging scripts, `next.config.mjs`, `build/*`, the provisioner, the native-admission package) and no instruction sources change, so the Stage12 baseline should still pass after the advance and no `npm install` is needed. The instruction-bundle manifest is regenerated by the build; any drift will be caught at step 3.
- `com.chirality.runtime` is currently registered by the R3 plist (`ProgramArguments[0]` = R3 executable, `CHIRALITY_USER_DATA` = R3 userdata, `KeepAlive=always`). The R4 launcher `--check-only` therefore exits 70 until section B (quit GUI → `launchctl bootout` → remove/move the plist) is done; the new build's autostart then installs and bootstraps the R4 plist on first launch (plist absent ⇒ `launchctl print` exit 113 ⇒ guard PASS). Section B proposes `mv -n` of the plist into the Stage13 root (preserving evidence) with plain `rm` as the equivalent.
- `run-build.py --execute` requires `.next`, `dist-electron`, `dist-runtime` to exist in the frontend (it renames them aside); preflight 0d checks this.
- `verify-runtime-consumer.mjs` covers the same eight specifiers as Stage12; if the frozen commit adds new Runtime packages consumed by the frontend, the list is not extended automatically (the build still proves resolution for the listed ones).
- `execute-plan.py`, `run-*.py` and the derivers all refuse existing outputs; a failed step must be recorded and the stage abandoned or continued by the lead's decision — never by deleting Stage13 records.

## Scratchpad

Replay copies and the launcher preview live only under `/private/tmp/claude-501/…/249787c9-bff4-4fe1-912c-b475cefbd96a/scratchpad/` (replay/, launcher/).
