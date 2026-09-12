# L_STAGE16_PACKAGING — RETURN (Type 2 TASK, Fable 5.1)

## Outcome

COMPLETE through step 25. The Stage16 (R7) tooling was derived from the completed Stage15 (R6) tooling by `derive-stage16-from-stage15.py` (43 derived files, zero baseline changes), and preflight 0b–0e plus steps 1–25 of the derived `STAGE16_PROCEDURE.md` were executed in order with every gate verified. All three durable writes exist. Step 26 (launcher guard check) is deferred to the lead because it is only meaningful after section B. No gate failed; no step was re-run; no partial output was left behind.

Frozen source: `78cb5b266b3f8a92596ced5fbd535b155bc29c7d` on `claude/chirality-v3-mvp-trial-ab05cb` (Stage15 froze `d7cf6439d603b9fdf6a58adf9e4e47e3fa0d8bdb`).

Stage16 root: `/private/tmp/chirality-local-human-trial-20260910-16` (mode 700, uid 501; every file create-only).

## Admitted digests

| Item | Value |
|---|---|
| Frozen commit | `78cb5b266b3f8a92596ced5fbd535b155bc29c7d` |
| Outer inventory sha256 (`<OUTER_INVENTORY_SHA256>`, sealed result `inventorySha256`; also observed on the R7 app at step 22 and provisioned into the anchor at step 24) | `0dcc882cd8c6cb825346adcb8b8a127b8af60dcd8da79fa8977e561ff309ca8d` |
| Payload digest (`payloadManifest.sha256`, size 88536; governance recipe `payloadDigest`) | `d18d1081783db57280886ccdb4ed8f371ab3db129ff8ea8f19ed178239e52c8c` |
| Support-profile identity: `profileDigest` (`<PROFILE_DIGEST>`) | `1b188cbec94a3e0740475c74f8ae96a9f55f51e4a7a622f8632b8d95a2c1e156` |
| Support-profile identity: sha256 of `stage16-support-profiles.json` (= checkpoint `supportProfilesIdentity.sha256`) | `7dbf7768818d02ac651b079afe03bf2b35381156fbbac9a66b8e1d7312a9e475` |
| Support profile `kernelHelperContractDigest` / compiler `sourceDigest` | `7ab3af70ba6614a70f067ad95dfe6a3b653ca905c942066f49300e60141d4671` / `c46fab58b4cf3fd466b460f4c4b7c27f4857db6e3375b627cdccf3d5503baf4a` |
| Sealed result file `nested-signed-checkpoint.json.sealed.json` sha256 (488 bytes, mode 400) | `ae87d66ee4fdaede5107bff6e9817ee166e4662d51d53a886992deab5d2dbe9a` |
| Sealed result `peerRequirementSha256` | `8ef4b07368d9bedbf4016b6dc9c6dcf5dec8741cf3246c466e7e36b68ceff69c` |
| Release input digest (`CHIRALITY_RUNTIME_V2_INPUT_DIGEST`, step 16) | `3632f5f252299518fdb5c2772fd1fc44c7b1ed4fffe7326ffea51d3999f93ada` |
| Payload snapshot digest (steps 6–7, 599 entries) | `2871895a0025a4ef1ca17c1ece543a59a216da6dd4d625666aae50d8389369ee` |
| R7 app path | `/Users/ryan/Applications/Chirality Trial 20260910 R7.app` |
| R7 app inventory sha (durable-copy verification `sealedInventorySha256`; 1151 entries source = destination, roster digest `a9e54e428e7aeb556443b1f6a7ebcf91b519828f062317553c4a47e69f846f2e`) | `0dcc882cd8c6cb825346adcb8b8a127b8af60dcd8da79fa8977e561ff309ca8d` |
| R7 app `mainCodeDirectoryHash` (step 22) | `4d38fe04212777a298921d20700efc7ffeeb7dfa` |
| Trial observation sha256 (`trial-observation.json` = `final-observation.stdout`, 811 bytes) | `077b0dd52f5a0b7767de9fbe22c7090930baa0668242d9da1c4e6558a57cb427` |
| R7 release anchor (`…R7/runtime/release-authority/v2/release-anchor.json`, 910 bytes, disposition `created`) | `b0773733c6fcf279ce05ceb405a620b3648d61a5f8b3bf5b4c5157b11790c63e` |
| R7 launcher `/Users/ryan/Applications/Launch Chirality Trial 20260910 R7.command` (3303 bytes, mode 700) | `c0db24b2a760fd0cff0e3d5908dcdf9a6211531867d7322d00962f25f9a4369e` |
| R6 launcher source (unchanged) | `b273afc8a6f25628f765caa394e1d55bb2a226099d3653823ee55a9a780d3e0b` |
| `launcher-r6-r7.diff` (= expected diff) | `56212bf1744c01d79ee4fb5209b0fc4c6de690bd798f1c476bbb59f424285c0f` |
| Signed in-app native addon / supplier (support profile `nativeAdmission.sha256` / `supplier.sha256`) | `57e9f3eb252ace45eb20a5068c33e9b87ea6def6556becaff4d3078616a115b2` / `b0b9a79a12a3bf5aff2f70f0998735b25031a3b1b2713e2831a8e7a3b4f27949` (757506928 bytes) |
| Unchanged admitted digests (checked at step 1) | dependency resolution `e83a525c2c38ce267abdaa0a25d26cab97baf9bc3acaa1c8e14e5ae86366b202`; Supplier tree `0513989b14af3a7c45cdf9caaf67be0c9e40a1e8e2d2388428f91e34244b8a34`; Supplier executable `eecbc73eea2d472cfefb285dcee6d7ca46024668c2e8d907a1452053c7745189`; native addon `fa40fc23eb6d9a4de857652c314de4d2d89a6f2547fc24da0f48fcdf04a184f4`; governance expiry `2026-10-10T22:43:56.184Z` |
| Governance issued-at (step 14, real time) | `2026-09-11T08:57:18.000Z` |
| Account-free observer runId | `b3730a41-1d1c-427c-b346-70c5afe9bd8f` (observation sha `6fb439251ee4b1841aa56ee28e539c2e9776217dbb7ad0a77c3ce4258ed4964c`) |
| Derivation manifest `stage16-derivation-manifest.json` | `0fa72f38db3c15fc9f93fff9cf8baf19b7fb222a3d58d7aa86cb2a9d868e1b34` (30022 bytes) |
| `STAGE16_PROCEDURE.md` | `eae8b72d0bcd83cf54ced114119a5a48838695a6a781e9ca878b3ddace09fc05` |

## Derivation

`/private/tmp/chirality-local-human-trial-20260910-16/derive-stage16-from-stage15.py` (19280 bytes, mode 700, sha256 in the inventory) is the Stage15 script with:

- RULES shifted one stage (35 ordered rules): `20260910-15→16`, `20260910-14→15`, `stage15→16`, `stage14→15`, `Stage15→16`, `Stage14→15`, `Chirality Trial 20260910 R6→R7` then `R5→R6`, `-r6-build→-r7-build`, `R6/R5 durable`, `create-only R6→R7`, `awaiting-R6-→R7-`, `R6 userdata→R7`, `R6 copy→R7`, `launcher-r5-r6→launcher-r6-r7`, `r6-first-launch→r7`, `R6/R5 launcher`, `'R5'→'R6'`, `R6/R5 registration`, `running R6/R5 trial`, `R6/R5 app`, `R6/R5 executable`, `R6 provisioning→R7`, `retired-r5-→retired-r6-`, `first GUI launch of R6→R7`, `retires the R5→R6`, `Stage15 (R6)→Stage16 (R7)`, `Stage14 / R5→Stage15 / R6`, `Stage/R5/schema→Stage/R6/schema`. Applied in order so a value shifts exactly once.
- HEX_MAP: `1cfcc6cb…` (R5 launcher) → `b273afc8…` (R6 launcher, verified against the real file), and `b273afc8…` (expected R6) → `c0db24b2…` (expected R7, computed from the real R6 launcher bytes by the same three-reference sed derivation; the guard confirmed exactly those three references changed). Single-pass lookup, so no double mapping. KEEP_HEX unchanged (5 digests).
- SEMANTIC_PATCHES: only `STAGE16_PROCEDURE.md` (1 patch): the Stage15 title + "Stage15 note" paragraph (post-RULES anchor, unique) replaced by a Stage16 header naming `78cb5b26…`, the four-commit delta from the brief with the touched files, "none of the 15 baseline inputs changed, no `npm install` needed", plain `derive-governance.py` at step 14, section B retiring the R6 registration. The two Stage15-only `derive-wrapper.py` patches (dropping the Stage14 build04→build05 remap) were **dropped**: Stage15's `derive-wrapper.py` already lacks that remap, so their anchors do not exist; the survivor guard for `SUPPLIER_MAP`/build04/`c1809bb5…` is kept and an extra guard refuses any `derive-governance-build05` reference outside the procedure. Manifest additionally records `stage15FrozenCommit`.
- Stage15 static reuse baseline (15 inputs) re-identified from the real files: **no changes** (`baselineChanges: []`); emitted as `stage15-static-reuse-baseline.json` (schema `chirality.stage16-stage15-static-reuse-baseline/v1`). Also confirmed by `git diff --name-only d7cf6439d..78cb5b266` over the baseline paths (empty) and by hashing the untracked `node_modules/.cache/chirality-instruction-root/instruction-bundle-manifest.json`.
- Templates: 19 under `templates/` (prior-stage Stage15 basis hashes recomputed from the real Stage15 files; Stage16-only values are placeholders).
- Post-derivation checks: no stray `R5`, `20260910-14`, `Stage14`/`stage14` in any derived script/diff/plan; diffs of every derived script against its Stage15 original show only the intended label/path/digest shifts.

## Preflight and step gates

| Step | Gate | Result |
|---|---|---|
| 0a (verify only) | preserved checkout detached (no symbolic ref) at `78cb5b266…`; `git status --porcelain -uall -- projects/chirality-runtime projects/chirality-app-dev/frontend` empty | PASS |
| 0b | R7 app, R7 userdata, R7 launcher all "No such file or directory" | PASS |
| 0c | stage root `700 501`; only derived tooling present (`templates/`, `STAGE16_PROCEDURE.md`, `launcher-r6-r7.expected.diff`, `stage15-static-reuse-baseline.json`, `build-plan.json`, `stage16-derivation-manifest.json`, 20 scripts, derive script) | PASS |
| 0d | `.next`, `dist-electron`, `dist-runtime` present | PASS |
| 0e | supplier `codex` (761918056), electron zip (122090802), two P2 records, `login.keychain-db` listed (read-only `ls -l`) | PASS |
| 1 | `run-build.py --check`: `status PASS`, `frozenCommit 78cb5b266…`, `dependencyResolutionDigest e83a525c…`, exit 0 | PASS |
| 2 | `run-build.py --execute`: exit 0; `build-invocation.json` schema `chirality.stage16-r7-build-invocation/v1`, `succeeded`, 5 commands exit 0, 464 emitted / 303 generated; consumer resolution lists 8 specifiers into fresh `packages/*/dist` | PASS |
| 3 | `derive-wrapper.py`: 14 static + 464 + 303 + 11 records = 792 | PASS |
| 4 | `run-wrapper.py --check`: PASS, 792 inputs | PASS |
| 5 | `run-wrapper.py --execute`: exit 0; invocation `succeeded`; checkpoint `nested-signed`, `dependencyDigest e83a525c…`, `supplierDigest 0513989b…`, appPath `$S/output/mac-arm64/Chirality.app` | PASS |
| 6 | `derive-measure.mjs`: `payloadSnapshotDigest 2871895a…` = checkpoint `payloadSnapshotDigest`; 599 entries | PASS |
| 7 | `--check` PASS; `--execute` exit 0, invocation `succeeded`, stdout one `chirality-runtime-support-profile/v2` object | PASS |
| 8 | `derive-profile.py`: `profileDigest 1b188cbe…` | PASS |
| 9 | codesign verify/display exit 0; `Identifier=com.chirality.app`, `TeamIdentifier=8A7JL35U4S`, peer requirement recorded; native 0 load-command differences; supplier differences exactly index 4 `0x19` (72 B) and index 27 `0x1d` (16 B), same as Stage15; 729 nested signatures | PASS |
| 10 | `derive-account-free.py`: `supportProfileDigest 1b188cbe…` = `<PROFILE_DIGEST>` | PASS |
| 11 | invocation `succeeded`; schema `chirality-account-free-login-observation-result/v1`; 8 limbs (exact-supplier, keyring-backend, plaintext-fallback-absent, process-containment, storage-isolation, provider-network, bounded-protocol-purpose, retirement) all attempted+passed | PASS |
| 12 | `derive-payload.py` exit 0 (historical checkpoint `f529300b…`) | PASS |
| 13 | invocation `succeeded`; checkpoint `payload-bound`; `supportProfilesIdentity.sha256 7dbf7768…` = sha256 of `stage16-support-profiles.json` | PASS |
| 14 | `derive-governance.py --issued-at 2026-09-11T08:57:18.000Z`: `payloadDigest d18d1081…` = checkpoint `payloadManifest.sha256`; limitation "No account/model functional qualification; eighteen worker empirical limbs pending human trial." and "All eighteen worker empirical limbs remain pending-human-trial." preserved verbatim in `worker-prerequisites/*.json` (files differ from Stage15 only by fresh digests/paths) | PASS |
| 15 | invocation `succeeded`; six governance files present | PASS |
| 16 | `derive-seal.mjs`: `governanceCount 6`, release input digest `3632f5f2…` | PASS |
| 17 | invocation `succeeded`; sealed `verified: true`, appPath `$S/output/mac-arm64/Chirality.app`, `inventorySha256 0dcc882c…` | PASS |
| 18 | `derive-post-seal.py` exit 0; `verify-copy.py` equals its Stage15 derivation; R7 app still absent | PASS |
| 19 | `execute-durable-copy.py`: `succeeded`, exit 0, empty stdout/stderr (first durable write) | PASS |
| 20 | `verify-copy.py`: 1151/1151 entries, `semanticDifferenceCount 0`, `sourceDestinationSameInodeCount 0`, `destinationHardlinkGroupCount 0`, `xattrsEqual true`, `codesignVerifyExit 0` | PASS |
| 21 | `derive-final.py observation` exit 0; `expectedOuterInventorySha256 0dcc882c…` | PASS |
| 22 | invocation `succeeded`; schema `chirality-runtime-trial-seal-observation/v1`; `outerInventorySha256 0dcc882c…`; `signed-app`, `fuses-and-asar`, `signed-peer-identity-binding` attempted+passed | PASS |
| 23 | `derive-final.py provision` exit 0; `trial-observation.json` byte-identical to `final-observation.stdout` (cmp) | PASS |
| 23b | R7 userdata and `runtime` created `700 501` (second durable write) | PASS |
| 24 | invocation `succeeded`, exit 0, empty stderr; anchor `created` at `…R7/runtime/release-authority/v2/release-anchor.json` | PASS |
| 25 | `derive-launcher.sh`: "R7 launcher created"; R7 launcher `c0db24b2…` (expected), mode 700, 3303 bytes; `launcher-r6-r7.diff` equals expected diff (cmp) (third durable write). Launcher NOT run. | PASS |
| 26 | launcher guard check | DEFERRED to the lead (only meaningful after section B) |

## Baseline changes

None. All 15 entries of the Stage15 static reuse baseline are byte-identical at the Stage16 frozen commit; `stage16-derivation-manifest.json` records `baselineChanges: []`.

## Deviations from the Stage15 procedure

1. Derivation: the two Stage15-only `derive-wrapper.py` semantic patches were dropped (no anchor exists in Stage15's script); the procedure-header patch was carried in Stage16 form; two extra guards and a `stage15FrozenCommit` manifest field were added. No other script differs from its Stage15 original beyond the RULES/HEX_MAP substitutions.
2. Carried stale text in `STAGE16_PROCEDURE.md` (conventions line `S13=`, "Stage15 / R3", "Durable R4 paths", "R3 userdata", the `fdb8c8e18…`/`769f8ef0…` commit references, "R4 guarded launcher"/"references R3" comments in `derive-launcher.sh`) is inherited exactly as Stage15 inherited it from Stage14 and is flagged as non-gate text in the Stage16 header.
3. Two of my own gate probes were initially aimed at the wrong file (gate 9 looked for the `0x19/0x1d` pattern in `compare-macho.stdout` instead of `nested-binary-correspondence.json`; gate 14 looked for the eighteen-limb limitation in the recipe instead of `worker-prerequisites/*.json`). In both cases the `&&` chain halted before the next step, no output was created, the gate was then verified against the correct record and found passing, and the procedure resumed at the next step. No step was executed twice and no partial record exists.
4. `python3 -m py_compile` was run on the derive script before execution (no `__pycache__` was produced). `git diff`/`git log`/`git status`/`rev-parse` reads were run against the preserved checkout (read-only).
5. Step 14 `--issued-at` is the real UTC time `2026-09-11T08:57:18.000Z` (precedes the fixed expiry).

## Durable writes and protected paths

Created: `/Users/ryan/Applications/Chirality Trial 20260910 R7.app` (step 19; codesign `--verify --deep --strict` exit 0), `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R7` + `/runtime` with the provisioned `release-authority/v2/{release-anchor.json,trial-seal-observation.json}` (steps 23b/24), `/Users/ryan/Applications/Launch Chirality Trial 20260910 R7.command` (step 25).

Untouched (verified after step 25): no file under the Stage14 or Stage15 roots is newer than the Stage16 derive script; R5 launcher `1cfcc6cb…` and R6 launcher `b273afc8…` unchanged; R6 app has no files newer than the derivation; R6 userdata not opened for writing; the preserved checkout is still at `78cb5b266…` with a clean Runtime/frontend tree (its `dist/`, `.next`, `dist-electron`, `dist-runtime` were replaced only by `run-build.py --execute`, with the Stage15 trees moved aside under `prebuild-*`); the lead worktree has no changes other than this untracked `L_STAGE16_PACKAGING/` directory. No GUI app launched, no `.app` opened, no `Launch … .command` run, section B not run, `~/Library/LaunchAgents` not read or written, no `security` command, no keychain enumeration, no git commit, no publishing. No account email appears in any record or in this return (all stdout records contain no `@`).

## Left for the lead

- Section B (quit the R6 GUI, `bootout` the `com.chirality.runtime` job, retire the R6 registration plist as `retired-r6-com.chirality.runtime.plist`), then step 26 (`'/Users/ryan/Applications/Launch Chirality Trial 20260910 R7.command' --check-only` → `Launch guard PASS`), then the first guarded launch of R7 (B5) and the post-launch `launchctl`/`plutil` verification.
- Governance limitations carried unchanged: independent post-build review of Supplier build05 pending; eighteen worker empirical limbs pending human trial.
- The Stage16 `templates/` are informational (placeholders resolved by the real step records now present in the stage root).

## Stage16 root inventory

Mode is octal; directories show their recursive entry count. `output/` (the sealed `mac-arm64/Chirality.app`, 1151 entries) is identified by the sealed `inventorySha256` and the durable-copy verification rather than per-file rows; `build-tmp/`, `prebuild-runtime-dist/`, `prebuild-app-generated/` are step 2 build scratch and the Stage15 trees moved aside.

| path | size | mode | sha256 | origin |
|---|---|---|---|---|
| `/private/tmp/chirality-local-human-trial-20260910-16/STAGE16_PROCEDURE.md` | 28662 | 600 | `eae8b72d0bcd83cf54ced114119a5a48838695a6a781e9ca878b3ddace09fc05` | derivation (text-copy + header patch) |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-observer-invocation.json` | 4718 | 600 | `4a075d387b4abc02cc91ad587f9f04bd53b52d329dd0e40eda291d40b7611427` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-observer-plan.json` | 4640 | 600 | `d0ea9f3eec0211b9c32d4c8c60a94b8620d80b412fd57ac6cc487b2f5b872a0e` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-observer.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-observer.stdout` | 1435 | 644 | `51cbbf1fb85a08a66fbad5648dd8e6fb1ac67cbf8e0556ec723d308b261ee1d7` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/` | 119 entries | 700 | `-` | step 10 (dir) / step 11 (evidence) |
| `/private/tmp/chirality-local-human-trial-20260910-16/build-invocation.json` | 226805 | 600 | `475f90e8f4e62efb09e896d0f33427c2e757e429c2aca09de84e73126b3ef66b` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/build-plan.json` | 3549 | 600 | `e1c3bfff56baa90f89408efda8f038688a0df9f8281568b9f618b8e1f590f82e` | derivation (json-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/build-tmp/` | 3 entries | 700 | `-` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/check-admitted.mjs` | 964 | 700 | `384439c56158d5f9f60b45062185fa4d8d35be8d8a8169bbe92d19c1cfe5a8e0` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/compare-macho.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/compare-macho.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/compare-macho.stdout` | 1295 | 644 | `01c3a8f7465bfbb1450863832ccbb732e1f11efb3f88f0d30a4a493c1ceeb6fe` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/compare-macho.summary.json` | 1365 | 600 | `c54ec7d2c8d4053637eb731e0618d167d9ce09b542e136c8dc3627836d3b6663` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/compare_macho.py` | 3558 | 700 | `bb7aed1936a2ef93a08754758b21aad53fb5f2ba22507af8e1ece21a5dbf85e1` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-account-free.py` | 5299 | 700 | `c5cb5a773132e7ef473a7b06c4d889e659230f8fed06110bdd87fa715eeab215` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-final.py` | 8114 | 700 | `60ba95f6e20b3ac4603553c701832f9dbd38b304e832d3a03eb803500be43ae3` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-governance.py` | 7141 | 700 | `97790690c67a4956ce1e69bbc2b78892acb4810903da2411bd56ff1257db987a` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-launcher.sh` | 2470 | 700 | `fb58ea6f67a1d1840f559c32da997d7f494c609d2649290b01c9e2409ae95a90` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-measure.mjs` | 2717 | 700 | `6eb4bc056d01029b7c2eabfc9cdf69609e86ab8efb89b8773fa3faaffa9f03ec` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-payload.py` | 5061 | 700 | `cb959cbbc9e0674ccad5abe5c247fea71579b2a97195a2fd15b00881529add3b` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-post-seal.py` | 2785 | 700 | `fc8976000e45b6338ba850bc23fb622bb4da14670932718558314d30a219ca89` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-profile.py` | 1704 | 700 | `0edf396da06bfbcac40de647659720c4277d38b44411f534b140bcf33acbd973` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-seal.mjs` | 3933 | 700 | `39b212cc777db39e6574ae005c1b5a5e67a6951b14cdefc1e5a0bda7bf46a453` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-stage16-from-stage15.py` | 19280 | 700 | `a9545090605ca71f903c21e984b5adfe89dbf7a2acc79c724fed975e3a816248` | authored by this task (adapted from Stage15 derive-stage15-from-stage14.py) |
| `/private/tmp/chirality-local-human-trial-20260910-16/derive-wrapper.py` | 5015 | 700 | `b035bd37022aa6e5461284cbc854a90fad7995279a8424893007797765cad6b0` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/durable-copy-invocation.json` | 1718 | 600 | `6082674734a81452e7368ea8d9903cd268cad42e414ae44012917e5cba105ef8` | step 19 |
| `/private/tmp/chirality-local-human-trial-20260910-16/durable-copy-plan.json` | 1608 | 600 | `ef359d24a160423b2a368acc87d62e171c91c9ff849fd37230eec250324297d7` | step 18 |
| `/private/tmp/chirality-local-human-trial-20260910-16/durable-copy-verification.json` | 1456 | 600 | `e67d22a63fa146214ba833c7055d07ec69aa214f392d9e09ea357ed4f152a6d4` | step 20 |
| `/private/tmp/chirality-local-human-trial-20260910-16/electron-build.stderr` | 303 | 644 | `e0419472c96b0d0d564e409287291c920ebc098da41d346ca909db3e6b7aa5a8` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/electron-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/execute-durable-copy.py` | 2495 | 700 | `a63cce10cc5fb828ab634ec91fce7b878b523c5f0bf1a8f10f16c5923c11572d` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/execute-plan.py` | 1648 | 700 | `6bb43c956c5af0fdc5c0f7a71afa73a669de9dfc0d339796bfc2e5f8318c40b5` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/final-observation-invocation.json` | 3903 | 600 | `a57ec1327aa5f0ed3f26266c81aba26d5a057584cb4d1db83c30ecf93e689e3d` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-16/final-observation-plan.json` | 3824 | 600 | `204237597e14f4219ce02bbab0940bdce4f755ec214e0a21f1e205ddb34d9f97` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-16/final-observation.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-16/final-observation.stdout` | 811 | 644 | `077b0dd52f5a0b7767de9fbe22c7090930baa0668242d9da1c4e6558a57cb427` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-16/final-observer-home/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-16/final-observer-tmp/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-16/generate-candidate-evidence.py` | 4011 | 700 | `7d284809d6c0cde248fca6977aca2059f62a9d8dc4794c457cfa7f16ebc5aeb5` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/governance-invocation.json` | 4266 | 600 | `1e926dea27ca67fb1a1fac519de3311a57d14e9792fd38a9a8b0468e67acc147` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/governance-plan.json` | 4188 | 600 | `fa8d80b7d56b6d0eaf1410cbc5375b60da73edbb645079eefd361f1703e079eb` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-16/governance.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/governance.stdout` | 801 | 644 | `aeeabe4385e66293e9e6784d4f2598522e0d409929de2fd7a350ab0c6a3df7a0` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/launcher-r6-r7.diff` | 992 | 600 | `56212bf1744c01d79ee4fb5209b0fc4c6de690bd798f1c476bbb59f424285c0f` | step 25 |
| `/private/tmp/chirality-local-human-trial-20260910-16/launcher-r6-r7.expected.diff` | 992 | 600 | `56212bf1744c01d79ee4fb5209b0fc4c6de690bd798f1c476bbb59f424285c0f` | derivation (text-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/measure-home/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-16/measure-support-invocation.json` | 2966 | 600 | `ad093d4d7be0ba58597809bc8ae44e63f25821eca7b1158498931b8310114a6a` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-16/measure-support-plan.json` | 2716 | 600 | `5a7f4618c605d8ac488ce0ba6a24739eb6039f8fbee22fd5c67d05c8d640fc5f` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-16/measure-support.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-16/measure-support.stdout` | 1562 | 644 | `0a16020d95e34d292d290ce92adecb597cd2ee5907d6f8a300a5279cea3536da` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-16/measure-tmp/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-16/nested-binary-correspondence.json` | 45037 | 644 | `10b530ea35d7948f026c17ed26e8bf929e0904e4a1b46e45f821d62d5230a6fd` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/nested-signed-checkpoint.historical.json` | 275289 | 600 | `f529300b4210f1b461afc140aecb787e32a51eb5d45fcac6e5e7e667226dd6a8` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-16/nested-signed-checkpoint.json` | 275552 | 600 | `de84fafea24124572d95f2db9ed2d089bfabb18bf61b1b84c1370e8413edf47f` | step 5 (rewritten in place at step 13 to payload-bound) |
| `/private/tmp/chirality-local-human-trial-20260910-16/nested-signed-checkpoint.json.sealed.json` | 488 | 400 | `ae87d66ee4fdaede5107bff6e9817ee166e4662d51d53a886992deab5d2dbe9a` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-16/next-build.stderr` | 830 | 644 | `39f1259ec43f28876ad3d8bdd268a298fd9c6f82faa229065a126b334e9ef797` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/next-build.stdout` | 4637 | 644 | `f09be823bb2316b8f01f2070d4c555094cb1716f83a8cd6c4ab472503db34c97` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/observer-home/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-16/observer-tmp/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-16/output/` | 1155 entries | 755 | `-` | step 5 (output/mac-arm64/Chirality.app; identity = sealed inventorySha256) |
| `/private/tmp/chirality-local-human-trial-20260910-16/payload-bound-checkpoint.historical.json` | 275552 | 600 | `de84fafea24124572d95f2db9ed2d089bfabb18bf61b1b84c1370e8413edf47f` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-16/payload-invocation.json` | 4772 | 600 | `dec9a144fa700fe53d3d916bbde19a694642d7381a6872927aedff003e5d894e` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-16/payload-plan.json` | 4694 | 600 | `4bb61db33c9f364ef536f538fe56863e1f4eac5191e87ce82adb66f4f0659150` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-16/payload.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-16/payload.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-16/prebuild-app-generated/` | 483 entries | 700 | `-` | step 2 (Stage15 .next/dist-electron/dist-runtime moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-16/prebuild-runtime-dist/` | 478 entries | 700 | `-` | step 2 (Stage15 dist trees moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-16/provision-invocation.json` | 6190 | 600 | `d94efa9d9d207e7b27aa0cab1ef4ef798b80c261f0939dabb0055c562ca6a47a` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-16/provision-plan.json` | 6110 | 600 | `d26e09f7e94186328342d9f74472bf7ceb9f2edde5e13915f6fb2499197cc94f` | step 23 |
| `/private/tmp/chirality-local-human-trial-20260910-16/provision.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-16/provision.stdout` | 995 | 644 | `808bd1755d3a33034e17328b3118777f2121a14aed4714ed529b9d8575e724bc` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-16/release-inputs-inspection.json` | 169316 | 600 | `4fd45e7458b8b01a1b031bceceef8cbec81571a8d0da05fba6d9bdbf7a592115` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-16/run-build.py` | 6264 | 700 | `7c6fa8add44c0009cd7af7e649782020cf8bf60410a31da5b10adae8e440caff` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/run-measure.py` | 2571 | 700 | `d28d1450fc51a943a7e1ddacabc34bbe47f449e686982dfbc8d8271e2eab2a0d` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/run-wrapper.py` | 3143 | 700 | `cebac9e9a71aaaecdb7e75206f7d95659238bfe5b5ca34d992386c0cd0fc2e3c` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/runtime-build.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/runtime-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/runtime-clean.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/runtime-clean.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/runtime-consumer-resolution.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/runtime-consumer-resolution.stdout` | 3850 | 644 | `f21cd467217a7928abc8ef9acd8ab7a3c98a9e07da521b3541175781121c982f` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-16/seal-invocation.json` | 7090 | 600 | `4e0bcb6aa2d34c717c6852fac4a28125f02e79f50dda7920164ba2e39bc630d2` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-16/seal-plan.json` | 7013 | 600 | `aa6cd2de4993e5f3b4efb1342e650e5dcd54ae810b204eeb452e5c240b278ca0` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-16/seal.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-16/seal.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-16/signature-display.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/signature-display.stderr` | 1079 | 644 | `a11922d66e5afab9ba833008535f93531b944dda82494bcd26df07af4f395fc9` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/signature-display.stdout` | 118 | 644 | `3b2f91085ad953a851afeba4befd0f4e32557a97cb1a94957e8847b428936d52` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/signature-verify.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/signature-verify.stderr` | 3004 | 644 | `c2bbf8b3e0d12d48f664a3fe8a37ba950e5a9cc2071d9be282dc0c19ad4b04cf` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/signature-verify.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage15-static-reuse-baseline.json` | 4137 | 600 | `42cbf67196b8452fba21778efec6472e8a08c9f2c77141888677a4d5043c26f5` | derivation (re-identified baseline) |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-account-free-observer-recipe.json` | 1697 | 600 | `8084603b21c7106f99bed12d04e709a3bea4b031efad100d8426290bbf2e39ca` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-derivation-manifest.json` | 30022 | 600 | `0fa72f38db3c15fc9f93fff9cf8baf19b7fb222a3d58d7aa86cb2a9d868e1b34` | derivation |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-final-operation-arguments-sealed.json` | 1563 | 600 | `a2b9b3c66632bf9d5d4b80e7ef184586e6835c0919b260679b8910d0dfd101fe` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance/` | 6 entries | 700 | `-` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance-recipe.json` | 3967 | 600 | `cefca7211e8fd0a46f45b2cde8cb5e009c535fc8f8a25807f7f0946612737fc2` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-measure-support-recipe.json` | 108217 | 600 | `47fe8344072aec5c04e0cebf7b39bea7e09320f5348a67c55a47452e2cae7e33` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-signature-evidence.json` | 1433 | 600 | `c3f9d814c382c2496e266eb98f9fddf6b106349eecde7eac95dfd70ae33aa8dc` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-support-profiles.json` | 1892 | 600 | `7dbf7768818d02ac651b079afe03bf2b35381156fbbac9a66b8e1d7312a9e475` | step 8 |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/` | 19 entries | 700 | `-` | derivation (19 templates) |
| `/private/tmp/chirality-local-human-trial-20260910-16/trial-observation.json` | 811 | 600 | `077b0dd52f5a0b7767de9fbe22c7090930baa0668242d9da1c4e6558a57cb427` | step 23 |
| `/private/tmp/chirality-local-human-trial-20260910-16/verify-copy.py` | 3453 | 700 | `5757f9375532d99353d67f5e86697e556fa21061e2311592bc31d8ded986ea58` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/verify-runtime-consumer.mjs` | 2178 | 700 | `4f38d0d1218b15bc79c7ac19fcdf13d3cc4826752cbc463626b1a3a917103cf0` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-16/worker-prerequisites/` | 4 entries | 700 | `-` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-16/wrapper-invocation.json` | 229305 | 600 | `ba03b9d073ec19d86cf92e2f79d799e29b83b4a60fe8f7dc124199c6b7f9f337` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-16/wrapper-plan.json` | 228849 | 600 | `5627ad54b8bcbc642d1813f40ba388471bde68d2e12cddb9e7a12453b6151760` | step 3 |
| `/private/tmp/chirality-local-human-trial-20260910-16/wrapper.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-16/wrapper.stdout` | 14860 | 644 | `176092de56bd15a940cb50575cabb84776d621fa2ff330c81262eec4d656efaf` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/account-free-observer-invocation.template.json` | 5514 | 600 | `c590927e37f98d9c03815d15e566ad5e0d1a62116d2e2e662c2e975ee7ba4bd0` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/account-free-observer-plan.template.json` | 5045 | 600 | `59918999a3c7b6ea830a721e3f53f368be79c8157f13c9320d584a716e7cae07` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/build-invocation.template.json` | 9401 | 600 | `a0c75e0aaf9e8190c0f3dc4273117a8a8472f20e468a4ba434c38a1e061eb822` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/durable-copy-invocation.template.json` | 2289 | 600 | `a363455d7da11e1b3e5091698c6b46fc4db1e473f7e0168ddd03b6ebca90e62d` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/durable-copy-plan.template.json` | 1894 | 600 | `ea525da723890be8c78dc0fd8314717677ffbdd4a431e66c51dc2d77b43d5d50` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/final-observation-invocation.template.json` | 4638 | 600 | `038cf3cfd8b295c0480930a4d2cee91346fe41b7f0fb8cfe52a080b51b2d151d` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/final-observation-plan.template.json` | 4284 | 600 | `1d0f3805f95307b3e3b4672171cf3533f83ab1c1d621121b7dd9cb0c599c0449` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/governance-invocation.template.json` | 5031 | 600 | `19fa220ad985a07a4d5938c7b7c4308455bf7c04b8e8049fa65d8e4f8b203ba2` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/governance-plan.template.json` | 4649 | 600 | `2d921ce9a69c836515373cdcc8a805bba5a99e96cb6e3ba1cf8df95efff8545c` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/measure-support-invocation.template.json` | 3436 | 600 | `f5684b42919022214489e86dbc046815208b1838dad57fa8141ae7b3a5d786fe` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/measure-support-plan.template.json` | 3003 | 600 | `7d206bac1a492ded6d2f865df67faa6204ce8236e423f6caa5b0a72e60ca4ebb` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/payload-invocation.template.json` | 5343 | 600 | `944a5e2a43b225318fc1b1107d003b42a043912f349c97a63ebff346d6be420b` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/payload-plan.template.json` | 5029 | 600 | `0b53d9b7a7dc1359a00399d4d3205c90dd552e1a2aaff0371156e0272accb84c` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/provision-invocation.template.json` | 6982 | 600 | `5bef4f849c0583472dec1787b094f8ed35ed93b29cdb66b2a128581a0cd1d1d3` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/provision-plan.template.json` | 6708 | 600 | `2fb994925a48f60633ed24e8f266d557bfeeb7d13b58e012a4b6a540bb7597a9` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/seal-invocation.template.json` | 7698 | 600 | `2fc5b8f90dccfdac134dba3b11a5a0e1a2dfa138978c7e09e5d5e84288159316` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/seal-plan.template.json` | 7335 | 600 | `df93723415c512cca48ebeb9b2f6e2895660f195e25f2aa5baec289c7d736ada` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/wrapper-invocation.template.json` | 10823 | 600 | `5c9b83a3843b1c365a77796c7ac0785dfb31c0e02bf929407fcfe051ee1653ff` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/templates/wrapper-plan.template.json` | 10030 | 600 | `fe67ae54560af9eb59c1940f5fcaaa4b607ce0f0cffbf149c53494662727c6d2` | derivation (template) |
| `/private/tmp/chirality-local-human-trial-20260910-16/worker-prerequisites/connected-source-contract.json` | 4337 | 600 | `39a08556ee400c586a6bc8fce20937a583bb4953af78587caee99bd7f58802e1` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-16/worker-prerequisites/native-enforcement-and-retirement.json` | 2146 | 600 | `1cd8662b3af0740c0c9cf3845a9b23ea1d2bbf40428788e4df426fbf44ec3d48` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-16/worker-prerequisites/signed-payload-and-supply.json` | 2084 | 600 | `0dcd2ba34391decb0b5e1efe26009a3350517df311e4e86f295a392a75c5894a` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-16/worker-prerequisites/trusted-app-and-account-host.json` | 1878 | 600 | `b7eab278302da51205543d45081ad42d45d498e34ccfb898a304805e68f97df5` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance/login-owner-act` | 2979 | 600 | `d52aa1c4cd33f5d86592edc34ddc7e6e859702d23ca38e8f50d859598d002ac7` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance/login-purpose-acceptance.json` | 628 | 600 | `c28a9830b05de0f9af607a65a8e9acc91a3bb8a23f556734f250ff61ac3fba1b` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance/login-purpose-record.json` | 1912 | 600 | `b7fa185806f16b323f465c25f3d1d681a0dda296d8846d56ec554e35c8b0d24c` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance/worker-owner-act` | 2979 | 600 | `d52aa1c4cd33f5d86592edc34ddc7e6e859702d23ca38e8f50d859598d002ac7` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance/worker-purpose-acceptance.json` | 629 | 600 | `19d54dea1429d9a7f7aa1982f998a6fba57f81c85d8d90632ab0867e4cbae226` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/stage16-governance/worker-purpose-record.json` | 2255 | 600 | `c8a1df269fd492151b79e0a01fc9df8c77eb858b65ef3361e07918239a47bfc3` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/bounded-protocol-purpose.json` | 392 | 600 | `4f432d9010ed1f796bbf8c204428f024392deb26b0a1680a524f81acb94a0d2c` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/exact-supplier.json` | 1123 | 600 | `6a40e1d13c79c8192a923e796eec2b16a41b976f59d4ed6cdd063da5ea53e24e` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/keyring-backend.json` | 399 | 600 | `887bb83354fe1532a821be5bba1c26d5572c4b174fb80be8a81150ed9dca8b35` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/observation.json` | 4837 | 600 | `6fb439251ee4b1841aa56ee28e539c2e9776217dbb7ad0a77c3ce4258ed4964c` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/plaintext-fallback-absent.json` | 1101 | 600 | `2c43f4d18433decd1f2ddc2e140a6a70806e973745e0b0412b6ba4d192c6a0d6` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/process-containment.json` | 2255 | 600 | `d3642724fdf0bbe1fa5ee6e1d62910aa29004e3e1fb26205eea888839d5f9784` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/provider-network.json` | 374 | 600 | `1ca99cb3e255f7f09796aecb0cc3247c43edb2441673ed87bf08a82f4274e31c` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/retirement.json` | 272 | 600 | `7c71540f85fa141daba393b41e75f2ca3e8292e973e9b6be406ef36dff4b5806` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/evidence/storage-isolation.json` | 1190 | 600 | `1ce86b6d5bcec39f3ceb8ef5725ae709114ba1f660d4a890ffc63f874c6ba61f` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/goals_1.sqlite` | 32768 | 644 | `8e5384a66355f763709e0cbf619d8926529af15a63154a23013ab00fcd84cb76` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/goals_1.sqlite-shm` | 32768 | 644 | `2ea1cb79d0c8fae4add42f5e10ac5a7ee647746450845e78fceb0d4e725c1d24` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/goals_1.sqlite-wal` | 74192 | 644 | `62e9ac24924f5bd354859f9a484534ce6f32eaf6d1cb0dfb2dcaec857acc7d5e` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/installation_id` | 36 | 644 | `49f94f6350a383a8d42fd3b7301fce605afe510a69070a3282e9d16a602a4af2` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/logs_2.sqlite` | 49152 | 644 | `ffb58e56c107a117c946813a5e03c21c7fb361adb1a4dd731f1a8c016ddc66c9` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/memories_1.sqlite` | 40960 | 644 | `a87fd03ad892847e4c4d94af04cb9461952061f048ef034e5248384074eee1ba` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/memories_1.sqlite-shm` | 32768 | 644 | `1d122ef04e2d5e21b0a1aacac9b4c2c14854ab619ce16592a80e83ff7fb6d28d` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/memories_1.sqlite-wal` | 61832 | 644 | `d22e84742968a65d1170ebe27f01c890edf5d4867406f7aeae25ca89b2f43ef8` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/queue_1.sqlite` | 36864 | 644 | `5d691f488965b8339acc2308a6068fbb211908eeb2db2e21c084eb558c37fe5a` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/queue_1.sqlite-shm` | 32768 | 644 | `691e8d4a8baf0af83d025b82096ed7a47d65bbc4fd64d2a2521943762d82c2ac` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/queue_1.sqlite-wal` | 82432 | 644 | `e145d2211f090e9536ea552e783697317e9480dd1dc76cce4e264ffd5bbb0691` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/.codex-system-skills.marker` | 17 | 644 | `cde876953bb31239588763ae17da4d65611ec0f75393e2867c011c59d6a6ba4c` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/LICENSE.txt` | 10776 | 644 | `4dd13869245e356246a5b770723247bbb80a8f07a181d1d3d873a1734297cdb9` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/SKILL.md` | 19201 | 644 | `681ddb4ad6d06a2acc78a3535b583f8d0c1ea800ecda3d56370d3310fd2cd4ba` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/agents/openai.yaml` | 275 | 644 | `9ca574af14580dc7a2a3dc37a1796d17f93cb8850be66501f0799ef8603e9dc0` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/assets/imagegen-small.svg` | 2889 | 644 | `cff5f34f57ff60b3ee92eaedd17b15e96dd4b9e776df3e78936c9e00d42be294` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/assets/imagegen.png` | 1711 | 644 | `95952f644064eb9e890f98d8db07216347186526e4c41ad66d3420629eb86e20` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/references/cli.md` | 9655 | 644 | `ecfc2e09261a0feb3482517a5fa0ff410cb7d1958e3cbd2ac6b61586f5b81405` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/references/codex-network.md` | 1779 | 644 | `c88298ca4481f6116a16fa7987434fc977f8b311c1bbc0c3d862ffd0c5981148` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/references/image-api.md` | 6072 | 644 | `dc975d7af8a4888967251a0276014b4a71ea30455294944b762256373ce3e569` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/references/prompting.md` | 8282 | 644 | `b210b051c775860267080941eba968212bf0ac7fce581d75c5dcc217d8293f8b` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/references/sample-prompts.md` | 17617 | 644 | `70474177d151855b175c6133de2aae1d90b7f146b0dab50ec830972c47d72183` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/scripts/image_gen.py` | 34271 | 644 | `35e8f9fa47deca111e46c63c4ac2008e09198ef664c0926a9dfdcd6745aa37ed` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/imagegen/scripts/remove_chroma_key.py` | 13836 | 644 | `3f7b9b14ad5c90f37618bc1c16a039a2076abca12ddc41b3ae470e2b1cad6c0e` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/LICENSE.txt` | 10776 | 644 | `4dd13869245e356246a5b770723247bbb80a8f07a181d1d3d873a1734297cdb9` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/SKILL.md` | 5446 | 644 | `7cb8fa1b2a0c635b5c61ffe1da7b8594a7ea0fce5b71e8d523e2025d88b2a05e` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/agents/openai.yaml` | 370 | 644 | `44b9efac6be1bae32d869aa2942fecbe4dcae82682ee03e4120f2f9b7d4658ec` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/assets/openai-small.svg` | 1091 | 644 | `45be1f0757eb18889eefb1e7db79668ef46a275dc4e0e78e8df5ebd7f6cdeadc` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/assets/openai.png` | 1429 | 644 | `156cc84d7332bfe95b310350bd470b690d22aa33d65340cc6c2e06022946194c` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/codex-self-knowledge.md` | 7417 | 644 | `8c8fb00e6e5cb1977924f5164684a6095427fa828bbc765225f17d9aeb79a912` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/latest-model.md` | 2094 | 644 | `f25e351e522dd6e30e82d482f31f44c992e794b11031cdcb6ac7c0e6b20c9d5d` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/mcp-diagnostics.md` | 2318 | 644 | `49bbd2f73df7bbd7f86c80425dea4da2d301c22046080399a36bfc0ca49509e9` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/model-migration.md` | 5054 | 644 | `5f20c38fbbb10319767b216d91ba74bae49c68fc1bfd6d1abd7c9b4cc9cb9ab0` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/model-selection.md` | 1344 | 644 | `ba2d164abbca30435a460a0bc3a7d82398dce2bdf092705c98ba55b3f3af38a8` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/official-docs.md` | 3337 | 644 | `7962f2dce55089b93bde4115bb89fd42f20993c1597a2b13edd4956f463875b9` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/prompting-guide.md` | 15747 | 644 | `db913884cfe0fabf29bee1a139918f56e299decfa0a14d61c48596f23f76621d` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/upgrade-guide.md` | 1050 | 644 | `ed1b75a89b8ec4d67787774ef6c4e8b98eace16c63348f42e969e6ffa67cb656` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/references/upgrading-to-gpt-5p6-sol.md` | 23093 | 644 | `9a918a0c8dd051d574f2fd0309201afa8a9b9c08241c11ca1fb0ac2f4724e7ac` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/scripts/fetch-codex-manual.mjs` | 16085 | 644 | `f53eb6d2f286e9efcc397e8bee93a938e37296c90953e4e06e94899ef1b6c363` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/scripts/resolve-latest-model-info` | 1038 | 644 | `7354dbb030ca0736dd633a7ca1b930cf640abd40370725dea3a458cb51d49523` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/openai-docs/scripts/resolve-latest-model-info.cjs` | 3937 | 644 | `eeb1bb486018e16b37edfc06b1a37179dbc672982d501040d4f7142f29dd2e64` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/SKILL.md` | 11467 | 644 | `71b95b8219644f95d633721e7f7cd3c469edfc8fe50f8415d400dfb2d74bc7b9` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/agents/openai.yaml` | 339 | 644 | `fecaf35d692bd3d33d1a065648258d12e393afa9055d78adf6e57b42f4142f6d` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/assets/plugin-creator-small.svg` | 1319 | 644 | `6591bf8ea9bb9435890dbdea299e0d2bd05f3aa893a335d26e4c535e93c8e7fb` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/assets/plugin-creator.png` | 1563 | 644 | `a4024b0306ddb05847e1012879d37aaf1e658205199da596f5145ed7a88d9162` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/references/installing-and-updating.md` | 6000 | 644 | `91c4781d48568fcc708b45566b08fb610ad1c88672720ae512f9525a1cf9cb20` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/references/plugin-json-spec.md` | 9179 | 644 | `eeb640130f69636affaa299d4170d5a7ae6a0ff978296ddf75c409ce6dd87b91` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/scripts/create_basic_plugin.py` | 11495 | 644 | `46f532721079f6de6443f30f9362d77f1d879f57c0559250ef9433867414eb93` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/scripts/identifier_validation.py` | 784 | 644 | `a6d51ce4a9a7e8f85626ff5808a467a67574e7f8cdf1167ffb467c5f67e57223` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/scripts/read_marketplace_name.py` | 1644 | 644 | `ba24e6d91eed6f778bde022a967be335c6253983b5ecd1c5e30c8483385887fd` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py` | 3043 | 644 | `97c5ecab5ad85d871f0ebfc9bdf25d4b9e1a1680128fd3deb18a8c64f15f85c5` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/plugin-creator/scripts/validate_plugin.py` | 21533 | 644 | `6ff4bc1cc8ca94827c30c8299951efdac900ff38a5069c03e9a6554fc194a723` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/review-agent/SKILL.md` | 2661 | 644 | `07079efd0dc76f05fade424e5dfb048dce1de2df7626e1a4f56292a4f3f92228` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/review-agent/agents/openai.yaml` | 252 | 644 | `4d867a46d15e36ac880176484aae160f59855340c6059b2ea6ab9fbc9af084de` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/SKILL.md` | 15311 | 644 | `6656e54755638e8efcf275a472b9672eaa8a9a1b9e59dc210e275b03b59e1e66` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/agents/openai.yaml` | 183 | 644 | `d07d21b93fcf3d4dc8d9a3399c05fc226a49a333a96d3e1c68b451b8dd9eade6` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/assets/skill-creator-small.svg` | 1319 | 644 | `6591bf8ea9bb9435890dbdea299e0d2bd05f3aa893a335d26e4c535e93c8e7fb` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/assets/skill-creator.png` | 1563 | 644 | `a4024b0306ddb05847e1012879d37aaf1e658205199da596f5145ed7a88d9162` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/license.txt` | 11358 | 644 | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/references/openai_yaml.md` | 2356 | 644 | `ffac39318e408108141d40f820968e59f70434a891694f9bf1d25be8237b150c` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/scripts/generate_openai_yaml.py` | 6619 | 644 | `ddaf9abdfb3e762ed3c82571e9c607ce964188f49f2146281beb2cb8a553a93d` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/scripts/init_skill.py` | 10160 | 644 | `bc04fae1e671aa1e5104212674e7f22c9665a791fafa2fc2b3897187a89801b2` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-creator/scripts/quick_validate.py` | 4227 | 644 | `1fd66498c219616fd9249eacdf16c458412ea9065a9d887fd716aeef03907762` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/LICENSE.txt` | 11358 | 644 | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/SKILL.md` | 3367 | 644 | `d68b77e5bbb34dedab89d134da52855f140fc4b4299b80104f534e3b9e98f8ee` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/agents/openai.yaml` | 221 | 644 | `5ce223d8b1070b82c42298538f1b8d376f788eb9e7a42a987e8c094070d73f0e` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/assets/skill-installer-small.svg` | 923 | 644 | `3928703ff00dc1a681e7a22401843b7edcbd4b2051651ce4c43b75f7e140504e` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/assets/skill-installer.png` | 1086 | 644 | `d0a230b1a79b71b858b7c215a0fbb0768d6459c14ea4ef80c61592629bf0e605` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/scripts/github_utils.py` | 659 | 644 | `61c1bbe2ae217433b4b6f9f09f21aca4df52c12598068343ade719f706e4859b` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/scripts/install-skill-from-github.py` | 11790 | 644 | `3569ac8c0b3a525515c2e0e27c4f48e6aef9f2ff04029dcb3f622b280fa8c25e` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/skills/.system/skill-installer/scripts/list-skills.py` | 2967 | 644 | `e4e1f78ca3d045827f2a05cfd99fae57cc7c1a1bfeba8704029108834debff35` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/state_5.sqlite` | 4096 | 644 | `4eeb710c739848e62f0d53d04057e17375b4af741c9b441f2a546f6ed860c79f` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/state_5.sqlite-shm` | 32768 | 644 | `2e7d6a7a8f78d2a2079bbf54dcf20a880b7fc516014ac2618301ccdada59c491` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-16/account-free-runtime/account-free-observations/b3730a41-1d1c-427c-b346-70c5afe9bd8f/private/home/state_5.sqlite-wal` | 1734552 | 644 | `0e9ab2312e5fafd9cc4e199ae315a9924075621d96ba3cd8301db9846874c78d` | step 11 |
