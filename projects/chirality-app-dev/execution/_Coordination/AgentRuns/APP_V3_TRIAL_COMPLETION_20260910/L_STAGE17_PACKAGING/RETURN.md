# L_STAGE17_PACKAGING — RETURN (Type 2 TASK, Fable 5.1)

## Outcome

COMPLETE through step 25. The Stage17 (R8) tooling was derived from the completed Stage16 (R7) tooling by `derive-stage17-from-stage16.py` (43 derived files, zero baseline changes), and preflight 0b–0e plus steps 1–25 of the derived `STAGE17_PROCEDURE.md` were executed in order with every gate verified. All three durable writes exist. Step 26 (launcher guard check) is deferred to the lead because it is only meaningful after section B. No gate failed; no step was re-run; no partial output was left behind.

Frozen source: `dc8a3ee12bd45c06fe69bbb804602a674a3583bc` on `claude/chirality-v3-mvp-trial-ab05cb` (Stage16 froze `78cb5b266b3f8a92596ced5fbd535b155bc29c7d`).

Stage17 root: `/private/tmp/chirality-local-human-trial-20260910-17` (mode 700, uid 501; every file create-only).

## Admitted digests

| Item | Value |
|---|---|
| Frozen commit | `dc8a3ee12bd45c06fe69bbb804602a674a3583bc` |
| Outer inventory sha256 (`<OUTER_INVENTORY_SHA256>`, sealed result `inventorySha256`; also observed on the R8 app at step 22 and provisioned into the anchor at step 24) | `5bee50e7cb5939f9e680801de79ff7e236f7b080057f8ea9f04005e45f5b65be` |
| Payload digest (`payloadManifest.sha256`, size 88536; governance recipe `payloadDigest`) | `a2b74ad58f8f41791a580d85bd0f1a46627061a84c0420a83e2444f45660aa82` |
| Support-profile identity: `profileDigest` (`<PROFILE_DIGEST>`) | `9bdc138b890e8fd70144ff13cabd4e37677aa37d3f959ed12344aaa8d6342400` |
| Support-profile identity: sha256 of `stage17-support-profiles.json` (1892 bytes; = checkpoint `supportProfilesIdentity.sha256`) | `d84ba53b00cd4c9ad317e1f2c915acd8c0787945052842a95de5bd29a2463c52` |
| Support profile `kernelHelperContractDigest` / compiler `sourceDigest` (both moved from Stage16 because the Runtime source changed) | `a65fa6a6bfd6bca77a44d9871d5c58ec7e13db476cf59b41716bec12cdd753bb` / `a710051fba4de25f8dedff0ab03553787965c720b4e6c155a7f0e14b9da4a30b` |
| Sealed result file `nested-signed-checkpoint.json.sealed.json` sha256 (488 bytes, mode 400) | `336f35e6d07c9343e18d084b1e5328c734f272785e676cf865cf36c9898fbf6c` |
| Sealed result `peerRequirementSha256` | `8ef4b07368d9bedbf4016b6dc9c6dcf5dec8741cf3246c466e7e36b68ceff69c` |
| Release input digest (`CHIRALITY_RUNTIME_V2_INPUT_DIGEST`, step 16) | `256c9b5b354815ceb393bf629d61c550c1e7d01a819b7badbbf69f913da85656` |
| Payload snapshot digest (steps 5–7, 599 entries) | `daed2bc8b859d79828d600d494b628548dbbc20c7697e06e2d76da247bbc7c67` |
| R8 app path | `/Users/ryan/Applications/Chirality Trial 20260910 R8.app` |
| R8 app inventory sha (durable-copy verification `sealedInventorySha256`; 1151 entries source = destination, roster digest `40c6fadbdfb0952cf1c55c528cb7f977add7eeef126c06670ebf575c70a8d4f2`) | `5bee50e7cb5939f9e680801de79ff7e236f7b080057f8ea9f04005e45f5b65be` |
| R8 app `mainCodeDirectoryHash` (step 22) | `9f6d16b86cc8051ed975e75ba88db5299459be22` |
| Trial observation sha256 (`trial-observation.json` = `final-observation.stdout`, 811 bytes; = provisioned `trial-seal-observation.json`) | `15961def6677cb408ae3cd09c976b172c31471a80da215e4b19e4a35d6a1c330` |
| R8 release anchor (`…R8/runtime/release-authority/v2/release-anchor.json`, 910 bytes, disposition `created`) | `0fb4543a34dc4edf878c2b7a65a5a4c9c56c42ffbbee30ec73acab40cfaed64f` |
| R8 launcher `/Users/ryan/Applications/Launch Chirality Trial 20260910 R8.command` (3303 bytes, mode 700; equals the expected identity computed at derivation) | `e63670fec18de1e394f89f0599b7fac885cd55320f6754423e9f716a4720e540` |
| R7 launcher source (unchanged) | `c0db24b2a760fd0cff0e3d5908dcdf9a6211531867d7322d00962f25f9a4369e` |
| `launcher-r7-r8.diff` (= expected diff) | `59011ac9926fd666e74e6e14e0f13b307151d19d15f303c775141facdb9a03d8` |
| Signed in-app native addon / supplier (support profile `nativeAdmission.sha256` / `supplier.sha256`; = `compare-macho.summary.json` `final`) | `ec786e289dff0bbd22ab0b4447795da1a47065dcad761a812f1fdeec12e31c10` / `065a17aa22423d69369ce62abe368891c7d6d3f6ac12f88641aceef265dfd1af` (757506928 bytes) |
| Unchanged admitted digests (checked at step 1) | dependency resolution `e83a525c2c38ce267abdaa0a25d26cab97baf9bc3acaa1c8e14e5ae86366b202`; Supplier tree `0513989b14af3a7c45cdf9caaf67be0c9e40a1e8e2d2388428f91e34244b8a34`; Supplier executable `eecbc73eea2d472cfefb285dcee6d7ca46024668c2e8d907a1452053c7745189`; native addon `fa40fc23eb6d9a4de857652c314de4d2d89a6f2547fc24da0f48fcdf04a184f4`; governance expiry `2026-10-10T22:43:56.184Z` |
| Governance issued-at (step 14, real time) | `2026-09-11T09:59:06.000Z` |
| Account-free observer runId | `0c020d32-fd1a-4738-9f4c-e1db6d322114` (observation sha `a27dfbb7bdb5ce911a8518be87035417805c253b9ebd2230e834c79094cc1f52`) |
| Signature evidence `checkpointSha256` (= `nested-signed-checkpoint.historical.json`) | `e5d943a6c4a8f8ded0eabd13f71b34baefd5f62cdac05eea43e1af47f2ccc3d7` |
| Derivation manifest `stage17-derivation-manifest.json` | `a5d21e77106be1bec80cf83c3be038fcdd8f2949b451619a2ec2a74547864c2f` (30022 bytes) |
| `STAGE17_PROCEDURE.md` | `d10f12638266421b926a72dbc122f0ca3f9685f429aab3a961fadf9d944b0606` |

## Derivation

`/private/tmp/chirality-local-human-trial-20260910-17/derive-stage17-from-stage16.py` (20115 bytes, mode 700, sha256 in the inventory) is the Stage16 script with:

- RULES shifted one stage (35 ordered rules): `20260910-16→17`, `20260910-15→16`, `stage16→17`, `stage15→16`, `Stage16→17`, `Stage15→16`, `Chirality Trial 20260910 R7→R8` then `R6→R7`, `-r7-build→-r8-build`, `R7/R6 durable`, `create-only R7→R8`, `awaiting-R7-→R8-`, `R7 userdata→R8`, `R7 copy→R8`, `launcher-r6-r7→launcher-r7-r8`, `r7-first-launch→r8`, `R7/R6 launcher`, `'R6'→'R7'`, `R7/R6 registration`, `running R7/R6 trial`, `R7/R6 app`, `R7/R6 executable`, `R7 provisioning→R8`, `retired-r6-→retired-r7-`, `first GUI launch of R7→R8`, `retires the R6→R7`, `Stage16 (R7)→Stage17 (R8)`, `Stage15 / R6→Stage16 / R7`, `Stage/R6/schema→Stage/R7/schema`. Applied in order so a value shifts exactly once.
- HEX_MAP: `b273afc8…` (R6 launcher) → `c0db24b2…` (R7 launcher, verified against the real file), and `c0db24b2…` (expected R7) → `e63670fe…` (expected R8, computed from the real R7 launcher bytes by the same three-reference sed derivation; the guard confirmed exactly those three references changed). Single-pass lookup, so no double mapping. KEEP_HEX unchanged (5 digests).
- SEMANTIC_PATCHES: only `STAGE17_PROCEDURE.md` (1 patch): the Stage16 title + "Stage16 note" paragraph (post-RULES anchor, unique) replaced by a Stage17 header naming `dc8a3ee1…`, the three-commit delta from the brief (`packages/core/src/runtime-service.ts` boot under the persisted permission mode, `tests/hosted-bootstrap-integration.test.ts`, `tests/runtime-v3-api.test.ts`, coordination records), "none of the 15 baseline inputs changed, no `npm install` needed", plain `derive-governance.py` at step 14, section B retiring the R7 registration. Exactly the deviations the Stage16 RETURN recorded are carried: the two Stage15-only `derive-wrapper.py` patches remain dropped (no anchor exists in Stage16's script either), the survivor guard for `SUPPLIER_MAP`/build04/`c1809bb5…` is kept, the extra guard refusing any `derive-governance-build05` reference outside the procedure is kept, and the manifest records `stage16FrozenCommit`. Nothing else was dropped or added.
- Stage16 static reuse baseline (15 inputs) re-identified from the real files: **no changes** (`baselineChanges: []`); emitted as `stage16-static-reuse-baseline.json` (schema `chirality.stage17-stage16-static-reuse-baseline/v1`), byte-identical to Stage16's `stage15-static-reuse-baseline.json` except the schema line. Also confirmed by `git diff --name-only 78cb5b266..dc8a3ee12` over the baseline paths (empty; the full delta is the six files named in the brief).
- Templates: 19 under `templates/` (prior-stage Stage16 basis hashes recomputed from the real Stage16 files; Stage17-only values are placeholders).
- Post-derivation checks: no stray `R6`, `20260910-15`, `Stage15`/`stage15` in any derived script/diff/plan/procedure/template; diffs of every derived script against its Stage16 original show only the intended label/path/digest shifts (the derive script's own diff against the Stage16 derive script likewise shows only the shift plus the docstring). The Stage16 root's `retired-r6-com.chirality.runtime.plist` (section B evidence written by the lead) is not a derivation input and was not read.

## Preflight and step gates

| Step | Gate | Result |
|---|---|---|
| 0a (verify only) | preserved checkout detached (no symbolic ref) at `dc8a3ee12…`; `git status --porcelain -uall -- projects/chirality-runtime projects/chirality-app-dev/frontend` empty | PASS |
| 0b | R8 app, R8 userdata, R8 launcher all "No such file or directory" | PASS |
| 0c | stage root `700 501`; only derived tooling present (`templates/` with 19 entries, `STAGE17_PROCEDURE.md`, `launcher-r7-r8.expected.diff`, `stage16-static-reuse-baseline.json`, `build-plan.json`, `stage17-derivation-manifest.json`, 20 scripts, derive script) | PASS |
| 0d | `.next`, `dist-electron`, `dist-runtime` present | PASS |
| 0e | supplier `codex` (761918056), electron zip (122090802), two P2 records, `login.keychain-db` listed (read-only `ls -l`) | PASS |
| 1 | `run-build.py --check`: `status PASS`, `frozenCommit dc8a3ee12…`, `dependencyResolutionDigest e83a525c…`, exit 0 | PASS |
| 2 | `run-build.py --execute`: exit 0; `build-invocation.json` schema `chirality.stage17-r8-build-invocation/v1`, `succeeded`, 5 commands exit 0, 464 emitted / 303 generated; consumer resolution lists 8 specifiers into fresh `packages/*/dist`; checkout still at the frozen commit with a clean Runtime/frontend tree | PASS |
| 3 | `derive-wrapper.py`: 14 static + 464 + 303 + 11 records = 792; plan schema `chirality.direct-trial-wrapper/v1` | PASS |
| 4 | `run-wrapper.py --check`: PASS, 792 inputs | PASS |
| 5 | `run-wrapper.py --execute`: exit 0; invocation `succeeded`; checkpoint `nested-signed`, `dependencyDigest e83a525c…`, `supplierDigest 0513989b…`, appPath `$S/output/mac-arm64/Chirality.app` | PASS |
| 6 | `derive-measure.mjs`: `payloadSnapshotDigest daed2bc8…` = checkpoint `payloadSnapshotDigest`; 599 entries | PASS |
| 7 | `--check` PASS; `--execute` exit 0, invocation `succeeded`, stdout one `chirality-runtime-support-profile/v2` object | PASS |
| 8 | `derive-profile.py`: `profileDigest 9bdc138b…` | PASS |
| 9 | codesign verify/display exit 0; `Identifier=com.chirality.app`, `TeamIdentifier=8A7JL35U4S`, peer requirement recorded; native 0 load-command differences; supplier differences exactly index 4 `0x19` (72 B) and index 27 `0x1d` (16 B), identical pattern to Stage16 (`nested-binary-correspondence.json`); 729 nested signatures | PASS |
| 10 | `derive-account-free.py`: `supportProfileDigest 9bdc138b…` = `<PROFILE_DIGEST>` | PASS |
| 11 | invocation `succeeded`; schema `chirality-account-free-login-observation-result/v1`; 8 limbs (exact-supplier, keyring-backend, plaintext-fallback-absent, process-containment, storage-isolation, provider-network, bounded-protocol-purpose, retirement) all attempted+passed | PASS |
| 12 | `derive-payload.py` exit 0 (historical checkpoint `e5d943a6…`; plan schema `chirality.stage17-payload-plan/v1`) | PASS |
| 13 | invocation `succeeded`; checkpoint `payload-bound`; `supportProfilesIdentity.sha256 d84ba53b…` = sha256 of `stage17-support-profiles.json` | PASS |
| 14 | `derive-governance.py --issued-at 2026-09-11T09:59:06.000Z`: `payloadDigest a2b74ad5…` = checkpoint `payloadManifest.sha256`; four `worker-prerequisites/*.json`; "No account/model functional qualification; eighteen worker empirical limbs pending human trial." and "All eighteen worker empirical limbs remain pending-human-trial." preserved verbatim | PASS |
| 15 | invocation `succeeded`; six governance files present under `stage17-governance/` | PASS |
| 16 | `derive-seal.mjs`: `governanceCount 6`, release input digest `256c9b5b…` | PASS |
| 17 | invocation `succeeded`; sealed `verified: true`, appPath `$S/output/mac-arm64/Chirality.app`, `inventorySha256 5bee50e7…` | PASS |
| 18 | `derive-post-seal.py` exit 0; `verify-copy.py` equals its Stage16 derivation; R8 app still absent; plan argv is the create-only `ditto --rsrc --extattr --acl` to the R8 path | PASS |
| 19 | `execute-durable-copy.py`: `succeeded`, exit 0, empty stdout/stderr (first durable write) | PASS |
| 20 | `verify-copy.py`: 1151/1151 entries, `semanticDifferenceCount 0`, `sourceDestinationSameInodeCount 0`, `destinationHardlinkGroupCount 0`, `xattrsEqual true`, `codesignVerifyExit 0` | PASS |
| 21 | `derive-final.py observation` exit 0; `expectedOuterInventorySha256 5bee50e7…`; args `awaiting-R8-post-seal-observation`; plan `observe-trial-seal --app …R8.app` | PASS |
| 22 | invocation `succeeded`; schema `chirality-runtime-trial-seal-observation/v1`; `outerInventorySha256 5bee50e7…`; `signed-app`, `fuses-and-asar`, `signed-peer-identity-binding` attempted+passed | PASS |
| 23 | `derive-final.py provision` exit 0; `trial-observation.json` byte-identical to `final-observation.stdout` (cmp) | PASS |
| 23b | R8 userdata and `runtime` created `700 501` (second durable write) | PASS |
| 24 | invocation `succeeded`, exit 0, empty stderr; anchor `created` at `…R8/runtime/release-authority/v2/release-anchor.json` with `trial-seal-observation.json` beside it | PASS |
| 25 | `derive-launcher.sh`: "R8 launcher created"; R8 launcher `e63670fe…` (expected), mode 700, 3303 bytes; `launcher-r7-r8.diff` equals expected diff (cmp) (third durable write). Launcher NOT run. | PASS |
| 26 | launcher guard check | DEFERRED to the lead (only meaningful after section B) |

## Baseline changes

None. All 15 entries of the Stage16 static reuse baseline are byte-identical at the Stage17 frozen commit; `stage17-derivation-manifest.json` records `baselineChanges: []`.

## Deviations from the Stage16 procedure

1. Derivation: exactly the Stage16 deviations were carried (the Stage15-only `derive-wrapper.py` patches stay dropped, both guards kept, `stage16FrozenCommit` manifest field); the procedure-header patch was carried in Stage17 form. No other script differs from its Stage16 original beyond the RULES/HEX_MAP substitutions.
2. Carried stale text in `STAGE17_PROCEDURE.md` (conventions line `S13=`, "Stage16 / R3", "Durable R4 paths", "R3 userdata", the `fdb8c8e18…`/`769f8ef0…` commit references, "R4 guarded launcher"/"references R3" comments in `derive-launcher.sh`, "Stage15 had 464 emitted" at step 3 now reading "Stage16 had") is inherited exactly as Stage16 inherited it and is flagged as non-gate text in the Stage17 header.
3. Two of my own gate probes were initially aimed at the wrong record shape (gate 3 read `emittedRuntimeFiles` instead of the printed `freshEmittedRuntimeFiles`; gate 11 treated `limbs` as a list instead of a keyed object). In both cases the `&&` chain halted before the next step, no output was created, the gate was then verified against the correct record and found passing, and the procedure resumed at the next step. No step was executed twice and no partial record exists.
4. The derive script was syntax-checked with an in-memory `ast.parse` (no `__pycache__` was produced; none exists under the stage root). `git diff`/`git log`/`git status`/`rev-parse`/`symbolic-ref` reads were run against the preserved checkout and the lead worktree (read-only).
5. Step 14 `--issued-at` is the real UTC time `2026-09-11T09:59:06.000Z` (precedes the fixed expiry).
6. Tool stdout for steps 1–25 was captured into this session's scratchpad (`/private/tmp/claude-501/…/scratchpad/step*.stdout`) so gate probes could parse it; those are duplicates of terminal output only, every procedure record lives in the stage root as designed.

## Durable writes and protected paths

Created: `/Users/ryan/Applications/Chirality Trial 20260910 R8.app` (step 19; codesign `--verify --deep --strict` exit 0 re-checked after step 25), `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R8` + `/runtime` with the provisioned `release-authority/v2/{release-anchor.json,trial-seal-observation.json}` (steps 23b/24), `/Users/ryan/Applications/Launch Chirality Trial 20260910 R8.command` (step 25).

Untouched (verified after step 25): no file under the Stage15 or Stage16 roots is newer than the Stage17 derive script; R6 launcher `b273afc8…` and R7 launcher `c0db24b2…` unchanged; R7 app has no files newer than the derivation; R7 userdata was not opened by this task (its GPU caches and `runtime/` entries newer than the derivation were written by the running R7 trial itself, GUI pid 62897 / daemon pid 62929 still live, and its release anchor still carries its 02:59 mtime); the preserved checkout is still detached at `dc8a3ee12…` with a clean Runtime/frontend tree (its `dist/`, `.next`, `dist-electron`, `dist-runtime` were replaced only by `run-build.py --execute`, with the Stage16 trees moved aside under `prebuild-*`); the lead worktree has no changes other than this untracked `L_STAGE17_PACKAGING/` directory. No GUI app launched, no `.app` opened, no `Launch … .command` run, section B not run, `~/Library/LaunchAgents` not read or written, no `security` command, no keychain enumeration, no git commit, no publishing. No account email appears in any record or in this return: the stage-root records contain `@` only as npm scopes and `package@version` tokens; the only email-like strings anywhere under the root are third-party package metadata inside the sealed app (`app.asar.unpacked/node_modules/@img/*/package.json`) and the supplier's bundled skill spec inside the observer's private home.

## Left for the lead

- Section B (quit the R7 GUI, `bootout` the `com.chirality.runtime` job, retire the R7 registration plist as `retired-r7-com.chirality.runtime.plist` in the Stage17 root), then step 26 (`'/Users/ryan/Applications/Launch Chirality Trial 20260910 R8.command' --check-only` → `Launch guard PASS`), then the first guarded launch of R8 (B5) and the post-launch `launchctl`/`plutil` verification.
- Governance limitations carried unchanged: independent post-build review of Supplier build05 pending; eighteen worker empirical limbs pending human trial.
- The Stage17 `templates/` are informational (placeholders resolved by the real step records now present in the stage root).

## Stage17 root inventory

Mode is octal; directories show their recursive entry count. `output/` (the sealed `mac-arm64/Chirality.app`, 1151 entries) is identified by the sealed `inventorySha256` and the durable-copy verification rather than per-file rows; `build-tmp/`, `prebuild-runtime-dist/`, `prebuild-app-generated/` are step 2 build scratch and the Stage16 trees moved aside.

| path | size | mode | sha256 | origin |
|---|---|---|---|---|
| `/private/tmp/chirality-local-human-trial-20260910-17/STAGE17_PROCEDURE.md` | 28751 | 600 | `d10f12638266421b926a72dbc122f0ca3f9685f429aab3a961fadf9d944b0606` | derivation (text-copy + header patch) |
| `/private/tmp/chirality-local-human-trial-20260910-17/account-free-observer-invocation.json` | 4718 | 600 | `387f9169ce6a192e80d7cab9b81d7216b1d2fbe95929d922c58909d24ec2622d` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-17/account-free-observer-plan.json` | 4640 | 600 | `0bf0e9077d62de369b8164d328c5b6871c9c2baebfb8bd3db31120db5f1b396d` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-17/account-free-observer.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-17/account-free-observer.stdout` | 1435 | 644 | `a068e1fbc712370ca98fe987f0f679de936d1ce2fe472c19e8d77adf1fc10b39` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-17/account-free-runtime/` | 119 entries | 700 | `-` | step 10 (dir) / step 11 (evidence) |
| `/private/tmp/chirality-local-human-trial-20260910-17/build-invocation.json` | 226807 | 600 | `41f3d90c86cae8c67b3eb630ca65e9150ec45ff1d01e5a0ae16b9fcc13229644` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/build-plan.json` | 3549 | 600 | `c9fb744d6a9acef84538c588cb7389715e76e5e0a69014b396ad6e2353b91b7b` | derivation (json-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/build-tmp/` | 3 entries | 700 | `-` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/check-admitted.mjs` | 964 | 700 | `384439c56158d5f9f60b45062185fa4d8d35be8d8a8169bbe92d19c1cfe5a8e0` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/compare-macho.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/compare-macho.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/compare-macho.stdout` | 1295 | 644 | `5ecfea69075a2ac311c6765e25baf6bd5be8ec170335fdd3e7dda0f039165ddb` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/compare-macho.summary.json` | 1365 | 600 | `beffd91e7369fa2ba29e5830b0286af759995be76cea77eda64a0405cd17b129` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/compare_macho.py` | 3558 | 700 | `05bad954b0d6398bc15a92f00210093e96c6b6a7d366c4957d6ec61a851ae289` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-account-free.py` | 5299 | 700 | `4be68f1b927de9f717eb05d01cc4aa99b2c3e7d2f11502ac861a8840f49c5b88` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-final.py` | 8114 | 700 | `a7ed404356c6ab63cfcb1d2108b35e493a586f69d9f17412692ad1ebf4bcf2a8` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-governance.py` | 7141 | 700 | `6b9ef023a12ddd77f91d1e174c52d4a0386049ca76b5485524ceac1e43c6dcca` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-launcher.sh` | 2470 | 700 | `fa12b28eb0d77b102fc85855e2eb4299a9ac23fc75e788a1cce8f9ae4d82e99b` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-measure.mjs` | 2717 | 700 | `ab6576b783bcc716f9bc01d87122a600ccf378aced1ff6e391bb4cf2baa1f4e3` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-payload.py` | 5061 | 700 | `db1e1da71262be9b82ab97f67eebecf4333da2b854657be5af03a65ec0d6dca6` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-post-seal.py` | 2785 | 700 | `920697c11aad9874e40d681ccb3f0d3330bd74819b364c5a9817f84e23da359b` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-profile.py` | 1704 | 700 | `27e4a34f1ccb08a95d29cfb3540235d6b3b6879a3f760ce0b57b43412c1735f9` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-seal.mjs` | 3933 | 700 | `eccd6cc68bbd118879ed4c6b61f2d8d70d5f33241d35e5c1cf632eb103d2ff67` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-stage17-from-stage16.py` | 20115 | 700 | `000b228322c4ede0c14d80edace4ff4fafbb4f74a50995fee0ff09502fbb5544` | authored by this task (adapted from Stage16 derive-stage16-from-stage15.py) |
| `/private/tmp/chirality-local-human-trial-20260910-17/derive-wrapper.py` | 5015 | 700 | `f01ae4e58f059caa8658ad7532fa7fbc1a49971d617956d13f387d44a256a8eb` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/durable-copy-invocation.json` | 1717 | 600 | `3913a9c11959122d5f3cd033719985be724ff365772df60590e642b3f9f273c4` | step 19 |
| `/private/tmp/chirality-local-human-trial-20260910-17/durable-copy-plan.json` | 1608 | 600 | `53fefc8291f44352cf414aefbe0f3ed7d9bdf60a51c3df174a6ba07468610c07` | step 18 |
| `/private/tmp/chirality-local-human-trial-20260910-17/durable-copy-verification.json` | 1456 | 600 | `8952efb71ded3a6a4d0d2df830f5c0579ba605b4d94f62e2d2f7752a6b8544da` | step 20 |
| `/private/tmp/chirality-local-human-trial-20260910-17/electron-build.stderr` | 303 | 644 | `9940b93770c997bbafd32402a8e0cec530c8c3d5aaf27f4d70c7b3d75e3d3395` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/electron-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/execute-durable-copy.py` | 2495 | 700 | `ad6537ae621c7e589fe26da1eba0a825e74665424df4ccd0848ebe66c44b7aab` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/execute-plan.py` | 1648 | 700 | `6bb43c956c5af0fdc5c0f7a71afa73a669de9dfc0d339796bfc2e5f8318c40b5` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/final-observation-invocation.json` | 3903 | 600 | `03ccbee046dbb86530164dd39b3e3a09857688a982869f8e8e7eaffba968f7e7` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-17/final-observation-plan.json` | 3824 | 600 | `74a23315747c4d0700b6422e783434f954ce68535a8ac049fa49316ddcb65c34` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-17/final-observation.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-17/final-observation.stdout` | 811 | 644 | `15961def6677cb408ae3cd09c976b172c31471a80da215e4b19e4a35d6a1c330` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-17/final-observer-home/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-17/final-observer-tmp/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-17/generate-candidate-evidence.py` | 4011 | 700 | `f49c87d77597867b08d6f1820e5c596fbf4a79448215bc2f72dd0ea005713b5f` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/governance-invocation.json` | 4267 | 600 | `0a7067607093da4ec025bde822df9341d6d68b1debcf4f7b3df0a7ec2d8a024d` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-17/governance-plan.json` | 4188 | 600 | `b0c08cb097f288438d362610a4650c84bf53e87bcdff1b949e027509c1fd46ec` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-17/governance.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-17/governance.stdout` | 801 | 644 | `1a5b53e1a3a486e57a9313f33db56761cee50509206b12176b21d49d2748ff3e` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-17/launcher-r7-r8.diff` | 992 | 600 | `59011ac9926fd666e74e6e14e0f13b307151d19d15f303c775141facdb9a03d8` | step 25 |
| `/private/tmp/chirality-local-human-trial-20260910-17/launcher-r7-r8.expected.diff` | 992 | 600 | `59011ac9926fd666e74e6e14e0f13b307151d19d15f303c775141facdb9a03d8` | derivation (text-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/measure-home/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-17/measure-support-invocation.json` | 2966 | 600 | `ef47377e41d54d2740f3379e9bbe7cb33b767efe44e40a7d820b4b1edded5e1b` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-17/measure-support-plan.json` | 2716 | 600 | `8a6104b0b7a52a63a37f96368bb1a830b738ddf18e511c390771a2b37821efdf` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-17/measure-support.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-17/measure-support.stdout` | 1562 | 644 | `a1076a1b4cf73e802c086f67d17d959968a62fa0d0dac879c840923aeea904ed` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-17/measure-tmp/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-17/nested-binary-correspondence.json` | 45037 | 644 | `f3c4c6338a5e7ae38113e5fcfb32662b75b23b4fbdca67d66c9132e7098304c8` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/nested-signed-checkpoint.historical.json` | 275289 | 600 | `e5d943a6c4a8f8ded0eabd13f71b34baefd5f62cdac05eea43e1af47f2ccc3d7` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-17/nested-signed-checkpoint.json` | 275552 | 600 | `5be28625dc03204c0bd724dc0356ba7d74ec3c265f5a801f082d8c15b84278f7` | step 5 (rewritten in place at step 13 to payload-bound) |
| `/private/tmp/chirality-local-human-trial-20260910-17/nested-signed-checkpoint.json.sealed.json` | 488 | 400 | `336f35e6d07c9343e18d084b1e5328c734f272785e676cf865cf36c9898fbf6c` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-17/next-build.stderr` | 830 | 644 | `c1edc0e79edff3986a881d754b4beb0100e4798d27dd0de4259e891b3a1683ec` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/next-build.stdout` | 4637 | 644 | `f09be823bb2316b8f01f2070d4c555094cb1716f83a8cd6c4ab472503db34c97` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/observer-home/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-17/observer-tmp/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-17/output/` | 1155 entries | 755 | `-` | step 5 (output/mac-arm64/Chirality.app; identity = sealed inventorySha256) |
| `/private/tmp/chirality-local-human-trial-20260910-17/payload-bound-checkpoint.historical.json` | 275552 | 600 | `5be28625dc03204c0bd724dc0356ba7d74ec3c265f5a801f082d8c15b84278f7` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-17/payload-invocation.json` | 4773 | 600 | `590f705e6a4e915dc7dc10b889ed1a7c958ce915f2d4fe5152eef1fcd04c43ec` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-17/payload-plan.json` | 4694 | 600 | `c44d02480e7f7fde6bfbda77cac64715733d575029e103db3f823933febc8407` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-17/payload.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-17/payload.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-17/prebuild-app-generated/` | 483 entries | 700 | `-` | step 2 (Stage16 .next/dist-electron/dist-runtime moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-17/prebuild-runtime-dist/` | 478 entries | 700 | `-` | step 2 (Stage16 dist trees moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-17/provision-invocation.json` | 6188 | 600 | `dfc9cff5e5acadee38ccb6cda7dfde4b68d19c7f9140193cad1585584aa83da9` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-17/provision-plan.json` | 6110 | 600 | `0c3ac331229d2f96fe617c4a242586ec6154c08195675e21ae0d8c32123a966d` | step 23 |
| `/private/tmp/chirality-local-human-trial-20260910-17/provision.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-17/provision.stdout` | 995 | 644 | `933b0d0291c4a44c026cfafb41622e9b64a38095f9c4666aa4880137bbe63eec` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-17/release-inputs-inspection.json` | 169309 | 600 | `9c2af0e36f8f36f92e40cdf18da8cb3cec32c662589af8e3289be8bb4b892b7c` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-17/run-build.py` | 6264 | 700 | `6edf83eb47d795da45fe157b5934a1982ace2b1a61c52339bbe0be6cdbd6d0ef` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/run-measure.py` | 2571 | 700 | `e6ed447472f8219c1809d6901437148c74fd2fbd3f91cc3296e6621b2ae80bbc` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/run-wrapper.py` | 3143 | 700 | `1370f293c07c71fd30e168abcbce24e3a220d0336bb7671ae9db95c35cc8f06b` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/runtime-build.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/runtime-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/runtime-clean.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/runtime-clean.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/runtime-consumer-resolution.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/runtime-consumer-resolution.stdout` | 3850 | 644 | `51989b3c693be790983f580cb34fb9ff7243de0edc8022ca22d2d16f30352c69` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-17/seal-invocation.json` | 7092 | 600 | `3eba28e7e8ce97803d3727fe89aba0ad8ae86d6e7e8977ead14aee8b8f1e7418` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-17/seal-plan.json` | 7013 | 600 | `dd2cb26907acbc841fcf46b86f8f34882e398649ef81db96a2b9383ce0fd2dd4` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-17/seal.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-17/seal.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-17/signature-display.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/signature-display.stderr` | 1079 | 644 | `c568d2cf39d7e1ce87284401067bfee43430ab6f001f061ea0b8e1c3d7365ddd` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/signature-display.stdout` | 118 | 644 | `3b2f91085ad953a851afeba4befd0f4e32557a97cb1a94957e8847b428936d52` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/signature-verify.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/signature-verify.stderr` | 3004 | 644 | `ad1271ed5805ac5f41f141ed8de41e5424ae208d62f82eb58237e5699f7e0168` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/signature-verify.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage16-static-reuse-baseline.json` | 4137 | 600 | `60f66322ca0201e0d83ff0138cb4ff8210d2d5677516e2fc057c212eaab0767e` | derivation (re-identified baseline) |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-account-free-observer-recipe.json` | 1697 | 600 | `608cf033ff5c774bce66ba30893a45fb3010b032e8f73efa0ee888c8cf661f27` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-derivation-manifest.json` | 30022 | 600 | `a5d21e77106be1bec80cf83c3be038fcdd8f2949b451619a2ec2a74547864c2f` | derivation |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-final-operation-arguments-sealed.json` | 1563 | 600 | `0ab1a1f7ab9232e6d01d42dee632cc7dba701ee50439a247def3ce377ddd0523` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-governance/` | 6 entries | 700 | `-` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-governance-recipe.json` | 3967 | 600 | `6aee7a30a847c95fb477d972d4d1a98ad7f37c272a9eaefc8679525372407363` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-measure-support-recipe.json` | 108217 | 600 | `cb8a0982a1519df0565cb928a32e2997d5dbcb5e09834d28ffd34a00ab96cf13` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-signature-evidence.json` | 1433 | 600 | `a6571a09385de067d8083cb9aff3d70babbed84c62d2f0fc6610db51d80daabc` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-17/stage17-support-profiles.json` | 1892 | 600 | `d84ba53b00cd4c9ad317e1f2c915acd8c0787945052842a95de5bd29a2463c52` | step 8 |
| `/private/tmp/chirality-local-human-trial-20260910-17/templates/` | 19 entries | 700 | `-` | derivation (19 templates) |
| `/private/tmp/chirality-local-human-trial-20260910-17/trial-observation.json` | 811 | 600 | `15961def6677cb408ae3cd09c976b172c31471a80da215e4b19e4a35d6a1c330` | step 23 |
| `/private/tmp/chirality-local-human-trial-20260910-17/verify-copy.py` | 3453 | 700 | `42d3900809161e5616df2c26308b82356b1a701df55ac1dd918287da03bc28f4` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/verify-runtime-consumer.mjs` | 2178 | 700 | `6d58377b6a5ac835c10f3e1f8ba32698fa36e761175b64fdfca4a77db9f8979c` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-17/worker-prerequisites/` | 4 entries | 700 | `-` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-17/wrapper-invocation.json` | 229303 | 600 | `c2a78bfd095769539ad3c4f67657e29e9dfcb9dc959d053d1917efb98ba1a4db` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-17/wrapper-plan.json` | 228849 | 600 | `879fd352e56e5d2a7e24b226d01285648664867d4fe5b2a5dc377f5090f8e647` | step 3 |
| `/private/tmp/chirality-local-human-trial-20260910-17/wrapper.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-17/wrapper.stdout` | 14860 | 644 | `ad36e6ee3b9ff7b97d8e35c3c70e02394446d75800247f86a69fbf737cf42229` | step 5 |
