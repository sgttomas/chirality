# Repaired signed trial: shortest rebuild plan

Current execution note: reviewed source commit `83b16175c` is packaged in the preserved stage10 candidate at `/private/tmp/chirality-local-human-trial-20260910-10`; stage09 remains historical. Stage10's fresh measurement recipe is ready at `stage10-measure-support-recipe.json` (SHA-256 `face9b778c9f80574b8f449c54dabb389f45eca5c9e8130705844c408b250de5`) and its planned invocation is `measure-support-invocation.planned.json` (SHA-256 `8a1d00a389edfa25099421a726b5cf0529d6ef8a1d4994cf47dd03a1c1ff2501`). The 599-entry recipe matches the stage10 checkpoint snapshot digest `12c6abfdb95356d0a5ecd272b9df6c8b4ef07cd26fee3a67860ecefef0da52e9`; no measurement was executed by preparation.

After each parent-executed phase, `/private/tmp/chirality-local-human-trial-20260910-10/derive-next-steps.mjs` prepares the next files with create-only writes and stops when fresh prerequisites are absent:

```sh
NODE=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node
DERIVE=/private/tmp/chirality-local-human-trial-20260910-10/derive-next-steps.mjs
"$NODE" "$DERIVE" prepare-profile
"$NODE" "$DERIVE" prepare-account-free
"$NODE" "$DERIVE" prepare-payload
"$NODE" "$DERIVE" prepare-governance "$ISSUED_AT" "$EXPIRES_AT"
"$NODE" "$DERIVE" prepare-seal
```

Use actual owner-selected issuance/expiry timestamps in the governance command. `prepare-account-free` requires fresh stage10 signature and correspondence evidence. `prepare-governance` requires the successful fresh observer output and all four stage10 worker-prerequisite files to carry the new support-profile digest; it does not silently reuse stage08 prerequisite bytes. `prepare-seal` computes the release-input digest with the maintained inspector. These modes derive recipes and planned invocation records only; the parent executes measurement, observation, payload binding, governance preparation, and sealing separately.

Execution is intentionally deferred to Agent 0. Preserve these existing roots byte-for-byte:

- `/private/tmp/chirality-local-human-trial-20260910-08`
- `/Users/ryan/Applications/Chirality Trial 20260910.app`
- `/Users/ryan/Library/Application Support/Chirality Trial 20260910`

Use these absent, separate targets:

```sh
REPO=/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality
FRONTEND="$REPO/projects/chirality-app-dev/frontend"
NODE=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node
STAGE=/private/tmp/chirality-local-human-trial-20260910-09
REPAIRED_APP='/Users/ryan/Applications/Chirality Trial 20260910 Repaired.app'
REPAIRED_DATA='/Users/ryan/Library/Application Support/Chirality Trial 20260910 Repaired'
INPUTS=/private/tmp/chirality-release-runtime-20260910/trial-preparation-inputs
SUPPLIER=/private/tmp/chirality-supplier-release-20260910-02/evidence/trial-supplier-build-04/artifact
```

Before starting, require both repair owners' focused tests/reviews to be complete, record `git status --short` plus SHA-256 for the nine repaired production/test sources, and require `STAGE`, `REPAIRED_APP`, and `REPAIRED_DATA` absent. The production changes currently requiring rebuilt artifacts are `electron/main.ts`, `electron/host-account-connection.ts`, `src/components/settings/runtime-settings.tsx`, `src/components/settings/settings-view.tsx`, `src/components/shell/account-popover.tsx`, and `src/components/shell/account-settings-controls.tsx`. Do not run a broad test suite after their focused validations.

1. Create `STAGE` as owner-private `0700`. Preserve failed `.next` trees rather than deleting them. The initial `npm run build` followed a foreign `.bin` symlink into the retained `/private/tmp/chirality-v3-adoption-20260909` dependency tree; it was not a source failure. The canonical local Next CLI build and canonical local Electron build subsequently passed without an install or source change. Preserve their logs and use those fresh `.next`, `dist-electron`, and `dist-runtime` outputs. The successful build environment was:

   ```sh
   cd "$FRONTEND"
   env HOME=/Users/ryan TMPDIR=/private/tmp NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 \
     PATH="/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:$FRONTEND/node_modules/.bin:/usr/bin:/bin:/usr/sbin:/sbin" \
     "$FRONTEND/node_modules/next/dist/bin/next" build
   ```

   Then run `"$NODE" "$FRONTEND/scripts/build-electron.mjs"` under the same environment. Do not run `npm install`, alter dependencies, or use the foreign `.bin` entrypoint.

2. Prepare a stage09 copy of the record-driven wrapper used by `/private/tmp/chirality-local-human-trial-20260910-08/wrapper-runner-03.mjs`. Its check must pin the new build outputs and current packaging/signing scripts, while retaining the already admitted unchanged inputs below. Replace only the schema/stage labels and stage08 output/checkpoint paths. Then run `--check` followed by `--execute`. The executed argv remains:

   ```sh
   "$NODE" ./scripts/pack-electron-with-supply.mjs --runtime-manifest v2
   ```

   Preserve the exact stage08 environment except:

   ```text
   CHIRALITY_ELECTRON_OUTPUT_DIRECTORY=/private/tmp/chirality-local-human-trial-20260910-09/output
   CHIRALITY_RUNTIME_V2_SIGNING_CHECKPOINT_FILE=/private/tmp/chirality-local-human-trial-20260910-09/nested-signed-checkpoint.json
   ```

   Retain Supplier source/digest `SUPPLIER`, `c1809bb57097f8a387e2b90ea0c7ea1c15599c1a5ac0aabb7b2b65d83cb039d8`, dependency digest `e83a525c2c38ce267abdaa0a25d26cab97baf9bc3acaa1c8e14e5ae86366b202`, Electron cache, identity/team/bundle, and current native addon. The Supplier staging cache is presently absent, so the wrapper can stage it normally and clean it. Do not reuse stage08's checkpoint: its app path, `app.asar`, payload snapshot, and nested signatures describe the old candidate.

3. Repeat the stage08 pre-payload measurements against the new candidate, using the same bounded record method and no new tests. Build `stage09-measure-support-recipe.json` from the immutable stage08 metadata but set the new `resourcesRoot` and replace `payloadEntries` with `inspectRuntimeV2PayloadSnapshot(newResourcesRoot).entries`. Run:

   ```sh
   env HOME="$STAGE/measure-home" TMPDIR="$STAGE/measure-tmp" PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 \
     "$STAGE/output/mac-arm64/Chirality.app/Contents/MacOS/Chirality" \
     --runtime-cli release measure-support --recipe "$STAGE/stage09-measure-support-recipe.json"
   ```

   Prepared inputs: recipe SHA-256 `3f0f7dd5d2cc4e09db428bbf1cc3ace52fffa7108d75caa9fe223241f8e63289`; planned invocation record SHA-256 `7e80e0f28ad72f11e2b2aad57bbe3c7583762631480646760e36ce98b68c971c`. The recipe's 599 entries reproduce the new checkpoint payload snapshot digest `94a9c79461e8f87adfdabecb3f0afd70550a3c866028e5725b973ea03f50b7cd`; all non-path/non-entry fields equal stage08. Measurement remains held pending the current GUI diagnostic. When authorized, save stdout as the one-element `stage09-support-profiles.json`. A fresh profile is required because `compiler.sourceDigest` includes `app.asar`; the old profile cannot be asserted unchanged.

4. Recreate only evidence that binds changed candidate bytes. Derive the stage09 signature evidence, nested native/Supplier source-correspondence record, and account-free observer recipe by replaying the successful stage08 record methods with stage09 paths, new checkpoint/signature hashes, and the new support-profile digest. Reuse the unchanged P2 XPC/grouped records. Run the exact observer command from `account-free-observer-invocation.json` with stage09 recipe/resources/runtime/evidence paths. This is the minimal fresh login evidence needed for the new profile; do not repeat Supplier04, native source qualification, XPC, grouped-process, or connected-source validation.

5. Bind the new payload using the exact stage08 payload invocation with stage09 checkpoint/profile paths:

   ```sh
   cd "$FRONTEND"
   "$NODE" ./scripts/pack-electron-with-supply.mjs --runtime-manifest v2 \
     --runtime-v2-phase payload --resume-checkpoint "$STAGE/nested-signed-checkpoint.json"
   ```

   Preserve the pre-bind checkpoint as `nested-signed-checkpoint.historical.json` using the stage08 create-only method. The command updates the live checkpoint to `payload-bound`; its new payload-manifest hash is the payload digest for the next step.

6. Derive a stage09 governance recipe from `stage08-governance-recipe.json`: replace the payload digest and support profile; use new login limb hashes from step 4; refresh only worker prerequisite snapshots whose evidence cites the rebuilt payload/signature/profile (`signed-payload-and-supply` and `trusted-app-and-account-host`). Reuse `native-enforcement-and-retirement` and `connected-source-contract` only after their recorded inputs/hash references compare unchanged. Keep the same recorded owner act, activation IDs, D36 gates, and still-valid expiry unless execution occurs after it. Prepare the create-only six files:

   ```sh
   "$NODE" "$REPO/projects/chirality-runtime/tools/provision-hosted-release-anchor-v2.mjs" \
     prepare-governance --recipe "$STAGE/inputs/stage09-governance-recipe.json" \
     --output "$STAGE/stage09-governance"
   ```

   Compute `CHIRALITY_RUNTIME_V2_INPUT_DIGEST` by calling the exported `inspectRuntimeV2ReleaseInputs({supportProfilesPath, governanceRoot}).digest`; do not carry forward stage08's `c943...` digest.

7. Seal once with the current scripts and stage09 paths. Use the exact environment in `seal-invocation.json`, substituting stage09 checkpoint/profile/governance and the newly computed input digest:

   ```sh
   cd "$FRONTEND"
   "$NODE" ./scripts/pack-electron-with-supply.mjs --target dir --runtime-manifest v2 \
     --runtime-v2-phase seal --resume-checkpoint "$STAGE/nested-signed-checkpoint.json"
   ```

   Require the sealed-result record, `codesign --verify --deep --strict --verbose=4`, dependency-boundary check, and inventory/payload/governance consistency. Do not rerun broad release proofs. If sealing mutates/signs the outer app and then fails only at the known completion boundary, preserve it and use the exact `verification-completion-invocation.json` method with the current `completeSignedRuntimeV2Verification`; never restart over that candidate.

8. Copy only to the repaired durable path and verify source/destination inventory equality:

   ```sh
   /usr/bin/ditto --rsrc --extattr --acl \
     "$STAGE/output/mac-arm64/Chirality.app" "$REPAIRED_APP"
   ```

   Run `observe-trial-seal --app "$REPAIRED_APP"` in isolated stage09 observer HOME/TMPDIR. Create `REPAIRED_DATA` as `0700`, save the observation as `0600`, and provision using the exact `provision-02-invocation.json` argv with repaired app/executable/runtime paths, stage09 governance, and the newly observed outer-inventory and observation SHA-256 values. This avoids the stage08 first-attempt parent-mode failure and leaves old userdata untouched.

9. For Agent 0's GUI checklist, launch the repaired executable with the isolated data binding:

   ```sh
   env CHIRALITY_USER_DATA="$REPAIRED_DATA" \
     "$REPAIRED_APP/Contents/MacOS/Chirality"
   ```

Material risks are limited: source must be frozen after concurrent repairs; stage09 support/governance cannot reuse old payload-bound hashes; every create-only output must be absent; and a second app with the same bundle identifier must be launched explicitly with `CHIRALITY_USER_DATA` after the old instance is quit so LaunchServices/single-instance routing cannot select the preserved app.

## Stage10 current execution state (2026-09-10)

Stage10 supersedes stage09 after the reviewed restart repair. The nested-signed checkpoint is `/private/tmp/chirality-local-human-trial-20260910-10/nested-signed-checkpoint.json`; source is frozen at reviewed commit `83b16175c`.

The successful fresh measurement produced `/private/tmp/chirality-local-human-trial-20260910-10/stage10-support-profiles.json` (SHA-256 `3e1bc3eb460d7c2570dc23b8c44eef6a648f1f7a04249b6cca42bde4dab3f8f8`) with sole profile digest `ffd2a6f390a2672688eb96a631b3f08ab95c4f5cc4d81eac9eced9cd2ad6113a`.

Read-only stage10 evidence regeneration passed the stage08 checks. `stage10-signature-evidence.json` (SHA-256 `291cc307bf9582a1db2cf16c6c3a86c19133eac945f79b4b31b654e006df7d0a`) records successful deep/strict codesign verification and display of the expected identifier, team, and designated requirement. `nested-binary-correspondence.json` (SHA-256 `f217c4aea32ec21c1a7a9939ce48e51be586d3050a079b20c34c622e1e7da381`) confirms identical native and Supplier file-backed sections and section membership; its load-command differences equal the accepted stage08 signing pattern.

Execute the observer exactly from `/private/tmp/chirality-local-human-trial-20260910-10/account-free-observer-invocation.planned.json` (SHA-256 `2a05a61090903cf61ef79cbb17e7274dcbdcb48c556769e5436a11b0803b6f25`). Its recipe is `stage10-account-free-observer-recipe.json` (SHA-256 `bfe342442325ee19d5aee1875841435ceed3bba346279d2421772916ec99947d`). After it passes, execute payload exactly from `payload-invocation.planned.json` (SHA-256 `3d932350d5bdccec70b601feb46b37bb011e0774fe75f1c24c5ffc5cb5ff0000`). Do not prepare governance until the live checkpoint is `payload-bound`, the successful observer output exists, and fresh prerequisite records bind the stage10 profile, payload, signature, and correspondence hashes.

Stage10 execution continuation: the observer passed all eight limbs on attempt 02; preserve the attempt-01 ENOENT logs. Payload passed and produced payload digest `2465bd5fde12af1a18ea9fe015030d2285511ae1049474ad39afdbd697b94206`. Governance preparation passed using recipe SHA-256 `f483051f8dfea760ab9350e45ba784763883726dafeed30ca6df6ac1e1a29f9d`, preserving the original expiry `2026-10-10T22:43:56.184Z` and all eighteen worker empirical limbs as pending human trial. The seal must use release-input digest `22491ba90fbc6496a49960986a7a242fccbe28f45d252f1104218ee0272204a2` and the exact plan `/private/tmp/chirality-local-human-trial-20260910-10/seal-invocation.planned.json` (SHA-256 `42e2fab615c0b6ec676d10dc74fa20b1c009cb2e21292567f3630e0eb20a8f57`). Its raw inspection and immutable pre-seal checkpoint are `release-inputs-inspection.json` (SHA-256 `6d8044d44b092cc4d6cb26cc0b853b422188aa6b9ad5b6551d18ded130033637`) and `payload-bound-checkpoint.historical.json` (SHA-256 `f2bf4166ae1b35b3751db0613fb6ab75308e02e44004f4838d3f4fd613d8023c`).

Stage10 final-path continuation: seal passed with verified inventory `4713110327d5038020f61f55bb64fceaee7702c55e0b63b5df1be1da44412ef8`. The create-only repaired durable copy passed 1,151-entry semantic roster equality, normalized extended-attribute equality, no shared inodes or destination hardlinks, and deep/strict codesign verification; record SHA-256 `12ff3933b2dd32670837269f906f5eea6c24aba1c302658316ca1773a4a2ceac`. Final observation passed all three checks; `/private/tmp/chirality-local-human-trial-20260910-10/trial-observation.json` SHA-256 is `e8cae9845546348dedd76c4e742b657f7c508e8d0da18bee3f8c380736bdea1c`. Execute final provisioning only from `provision-02-invocation.planned.json` (SHA-256 `8b259a92816e7405b78c8f92735243c61373891c7baed945d51d78e386712493`) after creating the repaired userdata parent and its `runtime` child as fresh, empty, real owner-501 directories with mode `0700`.

## Stage11 plan pending source freeze

Stage11 is a new candidate rooted at `/private/tmp/chirality-local-human-trial-20260910-11`. It must not alter the sealed Stage10 app, repaired userdata, runtime anchor, launcher, or Stage10 records. Commit `b2b32669c` is only the current basis: do not calculate source/build hashes or execute this plan until the account-loader `executablePath` repair and restart project-binding diagnosis are reviewed and the parent names the frozen commit.

1. Record the frozen commit and require a clean or explicitly inventoried source state. Recheck, rather than assume, that the package lock, materialized dependencies, admitted Supplier source/tree digest, raw native addon, signing scripts, entitlements, and runtime provisioner are byte-identical to the accepted Stage10 inputs. Any difference stops reuse and requires review of that specific input; it does not authorize installation, downloads, Supplier/native rebuilds, or broader testing.

2. Rebuild only the changed application outputs with canonical entrypoints. Remove or preserve-as-historical the old generated `.next` and Electron output so the new hashes cannot describe mixed output. Do not invoke `node_modules/.bin/next`, whose prior entry was a foreign symlink. From the frontend directory, use the Node 24.18.0 executable directly:

   ```sh
   env HOME=/Users/ryan TMPDIR=/private/tmp \
     PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin \
     NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 \
     /Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node \
     ./node_modules/next/dist/bin/next build
   ```

   Then run the current `scripts/build-electron.mjs` with the same canonical Node and production environment. Require both exits to be zero and record hashes of the frozen source, generated `.next`, Electron output, current packaging/signing scripts, entitlements, and provisioner before deriving the wrapper.

3. Derive a create-only Stage11 wrapper from the successful Stage10 `wrapper-plan.json` and `run-wrapper.py`. Replace the stage/run schema, output directory, checkpoint path, and every source/generated input hash with Stage11 values. Retain Supplier, native, dependency, Electron-cache, identity/team/bundle, and signing values only after step 1 proves their bytes unchanged. Execute the wrapper's check mode before its execution mode. The packaging argv remains `node ./scripts/pack-electron-with-supply.mjs --runtime-manifest v2`; output and checkpoint must point only into Stage11.

4. At the fresh `nested-signed` checkpoint, derive the measurement recipe from the Stage10 recipe by replacing only `resourcesRoot` and `payloadEntries` with a fresh `inspectRuntimeV2PayloadSnapshot(Stage11 Resources)` result. Execute `measure-support` using the packaged Stage11 executable with isolated, precreated owner-private `0700` measurement HOME/TMPDIR and the Stage10 system-only PATH. Save the successful JSON as a one-element Stage11 support-profile file. The profile, compiler source digest, and payload snapshot must be fresh because application code changed.

5. Regenerate the two candidate-bound read-only evidence records. Run deep/strict codesign verification and display against the Stage11 app and validate the expected identifier, team, and designated requirement. Run a Stage11 copy of the Stage10 Mach-O comparison utility against the accepted raw native/Supplier inputs and actual signed Stage11 binaries; require identical section membership and every file-backed section, with only the already accepted signing-related load-command pattern. Do not execute the Stage10 utility in place or overwrite its evidence.

6. Derive the Stage11 account-free recipe from the Stage10 semantic fields with a new run ID, new support-profile digest, actual Stage11 signed native/Supplier identities, and fresh signature/correspondence evidence hashes. Reuse the unchanged XPC and grouped-process records only after their bytes match the Stage10 recipe. Precreate empty real owner-501 mode-`0700` observer HOME, TMPDIR, and account-free runtime directories. Execute the observer once and require all eight limbs to pass before payload binding.

7. Preserve the nested-signed checkpoint, then run the exact Stage10 payload-phase argv/environment with Stage11 checkpoint/profile paths. Require exit zero and a live `payload-bound` checkpoint; preserve an immutable payload-bound checkpoint before sealing.

8. Refresh the four derivative worker-prerequisite files. `signed-payload-and-supply` and `trusted-app-and-account-host` bind the fresh Stage11 payload, profile, signature, correspondence, and measurement. `native-enforcement-and-retirement` and `connected-source-contract` retain their prior verified scope and limitations only after all retained evidence bytes are rehashed; replace their profile digest and account-free evidence paths/hashes with Stage11 values. No record may claim worker qualification: all eighteen worker empirical limbs remain pending human trial.

9. Derive governance from the Stage10 recipe using the Stage11 payload/profile, eight fresh observer hashes, and four Stage11 prerequisite hashes. Preserve the existing owner reference, activation IDs, D36 gates, and original expiry `2026-10-10T22:43:56.184Z`; set a fresh issue time before that expiry. The governance output path must be absent and its parent must be a real owner-private directory. Prepare the six files, calculate a fresh `inspectRuntimeV2ReleaseInputs` digest from the actual Stage11 profile and six governance files, and save the raw inspection separately.

10. Seal with the exact Stage10 seal argv/environment adapted to Stage11 and the fresh release-input digest. The plan must include the immutable payload-bound checkpoint, profile, both entitlements, three current packaging/signing/finalization scripts, raw release-input inspection, and all six governance files. Require the signed-runtime result to be verified, plus deep/strict codesign and focused dependency-boundary checks. Use verification completion only if the known post-sign completion boundary recurs; never restart packaging over a signed candidate.

11. Copy with create-only `ditto --rsrc --extattr --acl` to a new durable app path. Verify equal semantic rosters and normalized extended attributes, zero shared source/destination inodes, no destination hardlink groups, and deep/strict codesign. Run `observe-trial-seal` against that durable app using precreated isolated `0700` observer HOME/TMPDIR. Provision only after creating a new empty real owner-501 mode-`0700` userdata parent and runtime child, binding the actual observation hash and observed outer inventory. Create a separate guarded launcher from the Stage10 repaired launcher by changing only the selected Stage11 app path, userdata path, and usage filename; run `--check-only` and do not launch it during preparation.

The remaining prerequisites are: the reviewed frozen source commit; confirmation that the restart project-binding diagnosis is closed; current input-hash comparison for dependencies/Supplier/native and the packaging/provisioning tools; and explicit new durable app, userdata, and launcher paths. Stage11 GUI testing also requires the parent to stop the Stage10 instance and confirm the shared `com.chirality.runtime` service is absent immediately before launching Stage11. The original expiry must still be in the future when governance is prepared and when the trial is used.

### Stage11 pre-build state

The create-only private Stage11 root `/private/tmp/chirality-local-human-trial-20260910-11` and `build-tmp` exist as mode `0700`. The selected durable paths are:

- `/Users/ryan/Applications/Chirality Trial 20260910 R2.app`
- `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R2`
- `/Users/ryan/Applications/Launch Chirality Trial 20260910 R2.command`

They remain absent and must stay create-only. Read-only comparison record `stage11-unchanged-input-comparison.json` (SHA-256 `b2544ecc769238d87162cf400f68d232854e368c8fe6ef3a80a4a1361ae8a44f`) confirms all Stage10 reusable file identities remain unchanged, including both lockfiles, raw native addon, admitted Supplier executable, package metadata, instruction manifest, Electron cache, packaging/signing/finalization scripts, entitlements, and provisioner. The recomputed dependency resolution digest remains `e83a525c2c38ce267abdaa0a25d26cab97baf9bc3acaa1c8e14e5ae86366b202`; the Supplier tree digest remains `c1809bb57097f8a387e2b90ea0c7ea1c15599c1a5ac0aabb7b2b65d83cb039d8`; the raw native addon remains `fa40fc23eb6d9a4de857652c314de4d2d89a6f2547fc24da0f48fcdf04a184f4`. `build/icon.icns` is the sole expected changed packaging input, so generated Next/Electron/runtime outputs require replacement.

The gated runner is `/private/tmp/chirality-local-human-trial-20260910-11/run-build.py` (SHA-256 `f22a96c2f1cbb3e2ff0f8b5236331515622d7c250983df74f2f7bbb13aa579d1`) with plan `stage11-build-plan.json` (SHA-256 `49196406c3717f35262c4b46782eeaf2416b2e42a18f46055c2ad824c6e11b70`). It uses the canonical Next CLI path through Node, then `scripts/build-electron.mjs`, under one exact production environment. It moves the prior `.next`, `dist-electron`, and `dist-runtime` directories into create-only Stage11 historical storage before execution, captures separate stdout/stderr and command timing/hashes, writes one invocation record, and stops before Electron if Next fails. It refuses a non-full commit, HEAD mismatch, any tracked or untracked frontend source state, changed reusable inputs, changed dependency/Supplier digests, linked Next CLI, or pre-existing durable paths.

After the parent accepts the source review and names the full frozen commit, run:

```sh
python3 /private/tmp/chirality-local-human-trial-20260910-11/run-build.py \
  --check --expected-commit <FULL_REVIEWED_FROZEN_COMMIT>
python3 /private/tmp/chirality-local-human-trial-20260910-11/run-build.py \
  --execute --expected-commit <FULL_REVIEWED_FROZEN_COMMIT>
```

The current pre-freeze check correctly refuses execution because the account/restart repair remains uncommitted in the frontend. No build has run.

### Stage11 frozen build and packaging wrapper

Source is frozen clean at `81a81a6f3c9973264cc741086c4fc81fd6e1e983`. The canonical build invocation `build-invocation.json` (SHA-256 `72d9472b84adf0ddea4b843873da16c9a069388411df491193c94f93f4d5dbc9`) reports `status: succeeded`, `exit: 0`, and zero exits for both direct Node-to-Next and Electron builds. Preserve its five build log files unchanged.

The create-only Stage11 packaging plan is `/private/tmp/chirality-local-human-trial-20260910-11/wrapper-plan.json` (SHA-256 `e5d62c8005cfb11769a68e13d4540da678e7a283d3ebb70b186840c7a8273114`). It binds 30 current inputs, including the actual build invocation/logs, fresh `.next`, Electron and runtime outputs, new icon, both lockfiles, admitted Supplier/native, instruction manifest, Electron cache, package/config files, entitlements, and current packaging/signing/finalization scripts. The wrapper is `run-wrapper.py` (SHA-256 `71460af31041912451b09bb20e02c51de779118deaff14659b9fe868e0d83557`). Its check mode passed against the frozen commit and absent Stage11 output/checkpoint. After review, execute exactly:

```sh
python3 /private/tmp/chirality-local-human-trial-20260910-11/run-wrapper.py --execute
```

The wrapper records stdout, stderr, timing, status, and exit; success is impossible on an exception. It must create only the Stage11 output and nested-signed checkpoint and must not touch the installed Stage10 trial.

### Stage11 nested-signed and measurement state

The Stage11 wrapper succeeded and produced the fresh nested-signed checkpoint. Measurement recipe SHA-256 `02f88ee58d0a6aac2bc3df07625ba6638e0e14fb87a2320b0b01357db7eb9452` bound 599 entries and payload snapshot `a5e33ddff23eee70a1520087b8003f37bf6c341e05c518da547031b79cdf9a6b`; measurement then passed. The one-element support-profile file SHA-256 is `de27df95a458cf804ea3f720ddaa924c5ca7a568cf0c4dcaff76d2aa41fda211`, with profile digest `c59bc9a92ad34e12a1aa88d335c8981ba5b5d39cf9b4fac9c5c3143e81dae5fc`.

Fresh read-only signature evidence SHA-256 is `2618c473912ed5d98513a2340845afc795eaf6907eec1d1ee546344fa1c24f32`; Mach-O correspondence SHA-256 is `b7ad7f074592d4e5ccc1f91b272f0b9063437c7827c90d45a999835afff4abbd`. Execute account-free observation only from `account-free-observer-plan.json` (SHA-256 `a7f5cf321a125c5517465f0cef8c65f9df88019ceea99b52c53174a967c42fe0`) with the already empty mode-`0700` observer and runtime directories. After all eight limbs pass, execute payload only from `payload-plan.json` (SHA-256 `c4f3a39936a7bb2a0f3cdc492b5760011c309809c03f5e742088d05f0ac78701`); the preserved nested-signed snapshot SHA-256 is `9ac4c3780a7483bd27addc50662c41cf44f70c2fe323973dcb78725ef56c4c33`.

### Stage11 payload, governance, and seal preparation

The account-free observer passed all eight limbs and payload binding passed with payload digest `44a896401b2d90759838f6f58fabd83c4d8d3a30730a34c00c86633d99d1979d`. Governance passed using the original expiry. The fresh release-input digest is `4888bc0fb67c5d9531f0e51e4e1cec5db77e263b6483bbd15d5e27ccac664e90`; raw inspection SHA-256 is `ac16199d431fabc4b6a7cb9ec1cdb11b1e34ed74c417354292ea78b6a3cd9798`. The immutable payload-bound checkpoint SHA-256 is `d114baabbbb950468f5bcef19dbb6e29cefc17d2dacaa7e21bf64b981c9ab7b2`. Execute sealing only from `/private/tmp/chirality-local-human-trial-20260910-11/seal-plan.json` (SHA-256 `de5da6074a2f813461c757fbf520a3a82717ef4c0a26cd39c7451fda2fa2d463`).

Stage11 seal execution passed after the parent generic runner adapted its preflight to read `requiredSetup.existingPaths` entries by their `path` field; the seal argv/environment and candidate were unchanged, and there was no native failure or retry. The R2 create-only copy then passed 1,151-entry roster equality, equal normalized xattrs, zero shared inodes, zero destination hardlink groups, and deep/strict codesign verification. Copy verification SHA-256 is `44b9eae3a795f261f54d65d0472f150ff2de8c92e8a06c2a59cba0dafbd1e404`. Execute the final observation from `final-observation-plan.json` (SHA-256 `9b4fc4e12f8aeeb828521578bb4d0cc788f3b6d8c38ae226d9468c294cb548b5`), whose `existingPaths` are consistently strings.

Stage11 R2 provisioning passed. The published anchor SHA-256 is `6449f3c0ae8012bbc5e31325e108081fff1ee9f248491a3bfbaddb0e5bef1cca`; the published observation SHA-256 is `f53d33db1692b0a3a8b5393839792c978de5874776d573f2833aff49afe711f9`, binding outer inventory `bbe797bc1172ebf327706c3d4778677c9428eeec85d0100cc66f9a6c1a830bf8`. Runtime directories are owner-501 mode `0700`; anchor and observation are regular nonsymlink, single-link, owner-501 mode `0600`. The guarded R2 launcher is `/Users/ryan/Applications/Launch Chirality Trial 20260910 R2.command` (SHA-256 `6db55c635c6d21ba6ab8bc9b55bc81775583fcb002cf562bfb982988f5eb6dc0`); check-only passed. It differs from the preserved repaired launcher only in the R2 app path, R2 userdata path, and usage filename.

## Stage12 R3 plan pending Runtime review and freeze

Stage12 preserves the installed Stage11/R2 app, userdata, runtime anchor, launcher, and all Stage11 evidence. Its create-only durable paths are `/Users/ryan/Applications/Chirality Trial 20260910 R3.app`, `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R3`, and `/Users/ryan/Applications/Launch Chirality Trial 20260910 R3.command`. The original governance expiry remains `2026-10-10T22:43:56.184Z` and the permission/scope claims remain unchanged.

The App hydration repair and Runtime three-file repair are independently reviewed and frozen at repository HEAD `a120bd6b36a27b8fd83d49e6e1947c6a0708bdcb`. The Stage12 runner requires that exact full HEAD and a clean Runtime/frontend source state.

Planning files are under `/private/tmp/chirality-local-human-trial-20260910-12`: `build-plan.json` (SHA-256 `9d6cd306e3bbb1014748ad0e3fcf19d26fe7173753a0d9be1f18c274d26c4959`), `run-build.py` (SHA-256 `6d800ee41babb3d2879d3792b154fc4e2bde132136cb314731336dbeb0e52f36`), emitted-Runtime consumer verifier (SHA-256 `c4a6680d2605a2bf8e6525e83472a3d752273a863d2397f3869465e352ed7cbb`), admitted-input check (SHA-256 `4aa6394694ecaca710dd8c3984ad80c81fe4f7e916696e0df22f1205179e12bb`), and Stage11 static reuse baseline (SHA-256 `55fb9df66cccdba19a8eb702fb44814daf2c7b8baada4d84cbeb6a68d5ddcfe1`). No Stage12 build or operational directory exists beyond this private planning root. The runner initializes failure, assigns success only after both output inventories complete, and forces exit `1` for any exception, so an archive, subprocess, log, or inventory exception cannot produce a successful invocation. All eight Runtime incremental build-info files live inside the archived package `dist` directories; after those directories move, `tsc -b --clean` tolerates the missing outputs and the following `tsc -b` has no retained `.tsbuildinfo`, forcing fresh emitted packages.

After the Runtime commit, the exact dependency order is:

1. Run `run-build.py --check --expected-commit <FULL_RUNTIME_REPAIR_HEAD>`. It requires a clean Runtime/frontend tree, absent R3 durable paths and Stage12 execution outputs, unchanged Stage11 packaging/security inputs, dependency digest `e83a525c...`, Supplier tree `c1809bb5...`, raw Supplier `87162386...`, and raw native addon `fa40fc23...`.
2. Run the same command with `--execute`. It moves old Runtime `dist` directories and App `.next`/Electron/runtime outputs to create-only Stage12 historical roots, then invokes the canonical TypeScript CLI with `tsc -b --clean` followed by one `tsc -b --pretty false`. This rebuilds emitted Runtime packages without running `node-gyp` or changing the admitted native addon.
3. Before App compilation, the consumer-resolution command proves every selected frontend `node_modules/@chirality/*` link resolves to the current repository package and each selected Runtime import resolves to a freshly emitted regular file under that package's `dist` directory. Its exact Node 24 invocation includes `--experimental-import-meta-resolve`, which is required for the explicit frontend parent URL because the verifier itself resides under `/private/tmp`; a read-only probe passed for all eight targets, including the App-consumed `@chirality/runtime-daemon/hosted` and the release provisioner. Any stale or foreign resolution stops the build.
4. Only after that proof, invoke canonical Next once through Node and `node_modules/next/dist/bin/next build`, then invoke `scripts/build-electron.mjs` once. The runner is fail-fast, records partial archives and every command/log, and can record success only after all five commands return zero.
5. Derive the Stage12 wrapper from the successful Stage11 wrapper using the Stage12 build invocation/logs, complete fresh emitted-Runtime inventory, fresh Next/Electron/runtime outputs, current icon, and the frozen commit. Retain admitted Supplier/native/dependency and unchanged packaging/security hashes only from the successful preflight.
6. Repeat the narrow Stage11 candidate-binding sequence with Stage12 paths: wrapper check/execute; fresh 599-entry payload snapshot and packaged measurement; read-only signature and Mach-O correspondence; one eight-limb account-free observation; payload bind; four refreshed derivative prerequisites retaining all eighteen worker limbs as pending; governance with the original expiry; fresh release-input digest; seal; create-only R3 copy and equality check; final seal observation; private R3 provisioning; three-line guarded launcher derivation and check-only. Do not repeat source qualification, Supplier/native builds, XPC/grouped tests, broad release proofs, or any GUI launch during preparation.

Execution commands after the final reviewed commit are:

```sh
python3 /private/tmp/chirality-local-human-trial-20260910-12/run-build.py \
  --check --expected-commit a120bd6b36a27b8fd83d49e6e1947c6a0708bdcb
python3 /private/tmp/chirality-local-human-trial-20260910-12/run-build.py \
  --execute --expected-commit a120bd6b36a27b8fd83d49e6e1947c6a0708bdcb
```

### Stage12 frozen build and packaging wrapper

The Stage12 build completed with `status: succeeded`, exit `0`, and zero exits for all five commands at frozen HEAD `a120bd6b36a27b8fd83d49e6e1947c6a0708bdcb`. The actual build invocation SHA-256 is `cd54d3f626f451aadc637f659e8f4cc74f5c40bb933743c6764bd060379ac8b1`; it inventories 464 fresh emitted Runtime files and 303 fresh App generated files. Preserve its ten command logs unchanged.

The prepared wrapper plan is `/private/tmp/chirality-local-human-trial-20260910-12/wrapper-plan.json` (SHA-256 `15de4118f3c1e104e20484cf9b61980953c314651ff6f987b3faf9315666b88d`) and its runner is `run-wrapper.py` (SHA-256 `2c94f48a01983f89ab91aebef9a20d7535ae0345576dfa4c0c597015d145a687`). The plan binds 792 inputs: 14 unchanged wrapper inputs, all 464 fresh Runtime emitted files, all 303 fresh App generated files, the actual build invocation, and its ten logs. It retains the previously admitted dependency/Supplier/native values and changes only the Stage12 output and checkpoint paths. Check mode passed read-only; no wrapper execution occurred.

After parent review, run:

```sh
python3 /private/tmp/chirality-local-human-trial-20260910-12/run-wrapper.py --check
python3 /private/tmp/chirality-local-human-trial-20260910-12/run-wrapper.py --execute
```

### Stage12 R3 completion

Stage12 completed from frozen source `a120bd6b36a27b8fd83d49e6e1947c6a0708bdcb`. The fresh measured support-profile digest is `358a762bac8397db573c4bfdb852d406721faa8f909b4b0e4a757ee08cfb8306`; all eight account-free limbs passed. Payload digest `6be4bde080f6825e21bb64f33ba7e4d1b16c5d7e61df5859a5647bac4519eb79` was governed with all eighteen worker empirical limbs still pending human trial and the original expiry `2026-10-10T22:43:56.184Z`. The sealed outer inventory is `75aa3f6a63fc6e2776ad9f8267dcb6afa69514d4d0cb513c689485abf51791ad`.

The create-only R3 copy passed 1,151-entry semantic roster equality, normalized-xattr equality, zero shared inodes, zero destination hardlink groups, and deep/strict codesign verification. Final observation SHA-256 `090285564dcbd0e980b9eca1dcd47ea23819a2bc04d4d3492e64c901e1462fc2` passed all three checks. Provisioning published anchor SHA-256 `2bdd0cfa0b3054055b8a16ecd2c995badc9d93dc3f007d8fee623378560f7221` and the same observation under the owner-private R3 runtime directory.

The guarded launcher `/Users/ryan/Applications/Launch Chirality Trial 20260910 R3.command` has SHA-256 `d1c0813b9fc20fd65080aa6be6dbd4c70a5e2bde787fd31378eb251c5049b493`; `--check-only` passed without launching. Its exact diff from the preserved R2 launcher changes only the App executable path, userdata path, and usage label. The R2 launcher and installation remain preserved.

Owner subsequently authorized merging PR765 as unfinished source integration. These records are included in the merge; HANDOFF.md is the current entry point. Account setup remains incomplete and publishing remains unapproved.
