# L_STAGE18_PACKAGING — RETURN (Type 2 TASK, Fable 5.1)

## Outcome

COMPLETE through step 25. The Stage18 (R9) tooling was derived from the completed Stage17 (R8) tooling by `derive-stage18-from-stage17.py` (43 derived files, zero baseline changes), and preflight 0b–0e plus steps 1–25 of the derived `STAGE18_PROCEDURE.md` were executed in order with every gate verified. All three durable writes exist. Step 26 (launcher guard check) is deferred to the lead because it is only meaningful after section B. No gate failed; no step was re-run; no partial output was left behind.

Frozen source: `684ef914d088ac33cefdf1519810af4e69020d79` on `claude/chirality-v3-mvp-trial-ab05cb` (Stage17 froze `dc8a3ee12bd45c06fe69bbb804602a674a3583bc`).

Stage18 root: `/private/tmp/chirality-local-human-trial-20260910-18` (mode 700, uid 501; every file create-only).

## Admitted digests

| Item | Value |
|---|---|
| Frozen commit | `684ef914d088ac33cefdf1519810af4e69020d79` |
| Outer inventory sha256 (`<OUTER_INVENTORY_SHA256>`, sealed result `inventorySha256`; also observed on the R9 app at step 22 and provisioned into the anchor at step 24) | `8a3da519f535e6d51af49fd4afad3ee8de5cc577b9005776cf84b543d9d67d53` |
| Payload digest (`payloadManifest.sha256`, size 88536; governance recipe `payloadDigest`) | `6c019d7441a70142064b59c49822d644870c275400e93fb873ad6cd8072176ae` |
| Support-profile identity: `profileDigest` (`<PROFILE_DIGEST>`) | `88826eeb8fa1db7f6dac22be1e8ee8c417600e94bb8bc68b7c45079df2167787` |
| Support-profile identity: sha256 of `stage18-support-profiles.json` (1892 bytes; = checkpoint `supportProfilesIdentity.sha256`) | `b47dcc48b33d005f3b1e40873edd87cb2322c86f3ea318563c2cd59df739c5fc` |
| Support profile `kernelHelperContractDigest` / compiler `sourceDigest` (both moved from Stage17 because the Runtime source changed) | `2607633f881c82346ecab41b4418180ee0167cef952f6b6b142832c9668a183f` / `a43817c0e7bb61b9092d254db88fafb29fbb822227c0ddb42c1502b11d4adf3e` |
| Sealed result file `nested-signed-checkpoint.json.sealed.json` sha256 (488 bytes, mode 400) | `786dd6c1ca8820526dc685e1356ace929b8694caceb33d0eec44c3b466808127` |
| Sealed result `peerRequirementSha256` (unchanged from Stage17) | `8ef4b07368d9bedbf4016b6dc9c6dcf5dec8741cf3246c466e7e36b68ceff69c` |
| Release input digest (`CHIRALITY_RUNTIME_V2_INPUT_DIGEST`, step 16) | `617c74535798185bc55acbc556b7becca7ef2ca06064d4b71de424502c919dc8` |
| Payload snapshot digest (steps 5–7, 599 entries) | `8ef92abfccde8912be1eba159b84a1d30e20c04889f544477b07f36ed64afc58` |
| R9 app path | `/Users/ryan/Applications/Chirality Trial 20260910 R9.app` |
| R9 app inventory sha (durable-copy verification `sealedInventorySha256`; 1151 entries source = destination, roster digest `0cbd5f143b5cfd6a8cb1ce3322d6c740ce3c4284cb2c384350b8f822525135e5`) | `8a3da519f535e6d51af49fd4afad3ee8de5cc577b9005776cf84b543d9d67d53` |
| R9 app `mainCodeDirectoryHash` (step 22) | `6727fd4168b90bf915e1a20ec99e3adca8e1b448` |
| Trial observation sha256 (`trial-observation.json` = `final-observation.stdout`, 811 bytes; = provisioned `trial-seal-observation.json`) | `6f81db546cb5a7eefbdf1917f021e0e0c1862990e4079af0929cd02d0af4a644` |
| R9 release anchor (`…R9/runtime/release-authority/v2/release-anchor.json`, 910 bytes, disposition `created`) | `47be887704705af6fdbe3e26115f3e7c1ab7ddeaabfd8c1f3b3b29edd52bfc54` |
| R9 launcher `/Users/ryan/Applications/Launch Chirality Trial 20260910 R9.command` (3303 bytes, mode 700; equals the expected identity computed at derivation) | `8fbbc9120ad7363bdb9c715416d8c721315d63d65ff01d24cdb09ecbc37a3b4b` |
| R8 launcher source (unchanged) | `e63670fec18de1e394f89f0599b7fac885cd55320f6754423e9f716a4720e540` |
| `launcher-r8-r9.diff` (= expected diff) | `05645c7bad6d5e3e1bd55dde3f771794fe1cad650c34bb33a21e06932c2b029b` |
| Signed in-app native addon / supplier (support profile `nativeAdmission.sha256` / `supplier.sha256`; = `compare-macho.summary.json` `final`) | `3f6a3fafbfec7d525b7855c8284bb7bc30998d7db616aa7fc17f37baeedfbcae` / `be5567a3d80f0a78301180fa7774b825106f87c775a48ae230c961a5e6156288` (757506928 bytes) |
| Unchanged admitted digests (checked at step 1) | dependency resolution `e83a525c2c38ce267abdaa0a25d26cab97baf9bc3acaa1c8e14e5ae86366b202`; Supplier tree `0513989b14af3a7c45cdf9caaf67be0c9e40a1e8e2d2388428f91e34244b8a34`; Supplier executable `eecbc73eea2d472cfefb285dcee6d7ca46024668c2e8d907a1452053c7745189`; native addon `fa40fc23eb6d9a4de857652c314de4d2d89a6f2547fc24da0f48fcdf04a184f4`; governance expiry `2026-10-10T22:43:56.184Z` |
| Governance issued-at (step 14, real time) | `2026-09-11T14:25:29.000Z` |
| Account-free observer runId | `4d8b32bc-6e77-41a5-a850-20887fc0c8e8` (observation `account-free-observer.stdout`, 1435 bytes, sha256 `a6d71e7bd93a7f464d3c6c38d942e4e0f5b7e2188b70d7875f51bf3e6413c7cb`) |
| Signature evidence `checkpointSha256` (= `nested-signed-checkpoint.historical.json`) | `9f1df202161a63cc818aaf9727e6208bd24167305dccd53618e259470cf515a1` |
| Derivation manifest `stage18-derivation-manifest.json` | `5aaaa21b24e5e6437433c17c277012d1b9c98901451ed019fb7beb4ff6e609eb` (30022 bytes) |
| `STAGE18_PROCEDURE.md` | `c98ca06e63250b2433f4e7c61014b4c0eee0a7ebe3771f6ad9e60bcd9d6583a6` |

## Derivation

`/private/tmp/chirality-local-human-trial-20260910-18/derive-stage18-from-stage17.py` (20249 bytes, mode 700, sha256 in the inventory) is the Stage17 script with:

- RULES shifted one stage (35 ordered rules): `20260910-17→18`, `20260910-16→17`, `stage17→18`, `stage16→17`, `Stage17→18`, `Stage16→17`, `Chirality Trial 20260910 R8→R9` then `R7→R8`, `-r8-build→-r9-build`, `R8/R7 durable`, `create-only R8→R9`, `awaiting-R8-→R9-`, `R8 userdata→R9`, `R8 copy→R9`, `launcher-r7-r8→launcher-r8-r9`, `r8-first-launch→r9`, `R8/R7 launcher`, `'R7'→'R8'`, `R8/R7 registration`, `running R8/R7 trial`, `R8/R7 app`, `R8/R7 executable`, `R8 provisioning→R9`, `retired-r7-→retired-r8-`, `first GUI launch of R8→R9`, `retires the R7→R8`, `Stage17 (R8)→Stage18 (R9)`, `Stage16 / R7→Stage17 / R8`, `Stage/R7/schema→Stage/R8/schema`. Applied in order so a value shifts exactly once. (`Stage17 (R8)` and `Stage16 / R7` cannot match once the earlier `Stage17→18`/`Stage16→17` rules have run, exactly as their Stage17 counterparts could not, and are carried unchanged; `Stage/R7/schema→Stage/R8/schema` does apply, rewriting the one comment in `derive-post-seal.py`. A residue grep for `(R8)` and `Stage17 / R8` over the derived files finds nothing outside the derive script's own docstring, rule table and anchor text.)
- HEX_MAP: `c0db24b2…` (R7 launcher) → `e63670fe…` (R8 launcher, verified against the real file), and `e63670fe…` (expected R8) → `8fbbc912…` (expected R9, computed from the real R8 launcher bytes by the same three-reference sed derivation; the guard confirmed exactly those three references changed). Single-pass lookup, so no double mapping. KEEP_HEX unchanged (5 digests).
- Constants: `FROZEN_COMMIT` = `684ef914…`, `STAGE17_FROZEN_COMMIT` = `dc8a3ee1…`, `STAGE16_FROZEN_COMMIT` = `78cb5b26…` (needed by the anchor); `STAGE15_FROZEN_COMMIT` and the `STAGE16_HEADER` constant are dropped exactly as the Stage17 script dropped `STAGE14_FROZEN_COMMIT` and `STAGE15_HEADER`. The diff of the two derive scripts has the same line structure as the Stage16→Stage17 derive-script diff.
- SEMANTIC_PATCHES: only `STAGE18_PROCEDURE.md` (1 patch): the Stage17 title + "Stage17 note" paragraph (post-RULES anchor, unique) replaced by a Stage18 header naming `684ef914…`, the three-commit delta from the brief (`packages/daemon/src/hosted-private-composition.ts`: a materialized v2 hosted admission now records the command-network consent its DelegatedRuntime turns require, attributed to the ceremony's provider-network consent; `tests/d36-v2-connected.test.ts`; coordination records), "none of the 15 baseline inputs changed, no `npm install` needed", plain `derive-governance.py` at step 14, section B retiring the R8 registration. Exactly the deviations the Stage17 RETURN recorded are carried: the two Stage15-only `derive-wrapper.py` patches remain dropped (no anchor exists in Stage17's script either), the survivor guard for `SUPPLIER_MAP`/build04/`c1809bb5…` is kept, the extra guard refusing any `derive-governance-build05` reference outside the procedure is kept, and the manifest records `stage17FrozenCommit`. Nothing else was dropped or added.
- Stage17 static reuse baseline (15 inputs) re-identified from the real files: **no changes** (`baselineChanges: []`); emitted as `stage17-static-reuse-baseline.json` (schema `chirality.stage18-stage17-static-reuse-baseline/v1`), byte-identical to Stage17's `stage16-static-reuse-baseline.json` except the schema line. Also confirmed by `git diff --name-only dc8a3ee12 684ef914d` (exactly the five files named in the brief: the Stage17 brief and return, `RUN_LOG.md`, `hosted-private-composition.ts`, `tests/d36-v2-connected.test.ts`; none is a baseline path).
- Templates: 19 under `templates/` (prior-stage Stage17 basis hashes recomputed from the real Stage17 files; Stage18-only values are placeholders).
- Post-derivation checks: no stray `R7`, `20260910-16`, `Stage16`/`stage16` in any derived script/diff/plan/procedure/template (the manifest legitimately records the Stage17 source paths and the rule strings); diffs of every derived script against its Stage17 original show only the intended label/path/digest shifts (`check-admitted.mjs` and `execute-plan.py` are byte-identical); the derive script's own diff against the Stage17 derive script shows only the shift plus the docstring. The Stage17 root's `retired-r7-com.chirality.runtime.plist` (section B evidence written by the lead) is not a derivation input and was not read.

## Preflight and step gates

| Step | Gate | Result |
|---|---|---|
| 0a (verify only) | preserved checkout detached (no symbolic ref) at `684ef914…`; `git status --porcelain -uall -- projects/chirality-runtime projects/chirality-app-dev/frontend` empty | PASS |
| 0b | R9 app, R9 userdata, R9 launcher all "No such file or directory" | PASS |
| 0c | stage root `700 501`; only derived tooling present (27 entries: `templates/` with 19 entries, `STAGE18_PROCEDURE.md`, `launcher-r8-r9.expected.diff`, `stage17-static-reuse-baseline.json`, `build-plan.json`, `stage18-derivation-manifest.json`, 20 scripts, derive script) | PASS |
| 0d | `.next`, `dist-electron`, `dist-runtime` present | PASS |
| 0e | supplier `codex` (761918056), electron zip (122090802), two P2 records, `login.keychain-db` listed (read-only `ls -l`) | PASS |
| 1 | `run-build.py --check`: `status PASS`, `frozenCommit 684ef914…`, `dependencyResolutionDigest e83a525c…`, exit 0 | PASS |
| 2 | `run-build.py --execute`: exit 0; `build-invocation.json` schema `chirality.stage18-r9-build-invocation/v1`, `succeeded`, 5 commands exit 0, 464 emitted / 303 generated; consumer resolution lists 8 specifiers into fresh `packages/*/dist`; checkout still at the frozen commit with a clean Runtime/frontend tree | PASS |
| 3 | `derive-wrapper.py`: 14 static + 464 + 303 + 11 records = 792; plan `schemaVersion` `chirality.direct-trial-wrapper/v1` | PASS |
| 4 | `run-wrapper.py --check`: PASS, 792 inputs | PASS |
| 5 | `run-wrapper.py --execute`: exit 0; invocation `succeeded`; checkpoint `nested-signed`, `dependencyDigest e83a525c…`, `supplierDigest 0513989b…`, appPath `$S/output/mac-arm64/Chirality.app` | PASS |
| 6 | `derive-measure.mjs`: `payloadSnapshotDigest 8ef92abf…` = checkpoint `payloadSnapshotDigest`; 599 entries | PASS |
| 7 | `--check` PASS; `--execute` exit 0, invocation `succeeded`, stdout one `chirality-runtime-support-profile/v2` object | PASS |
| 8 | `derive-profile.py`: `profileDigest 88826eeb…` | PASS |
| 9 | codesign verify/display exit 0; `Identifier=com.chirality.app`, `TeamIdentifier=8A7JL35U4S`, peer requirement recorded; native 0 load-command differences; supplier differences exactly index 4 `0x19` (72 B) and index 27 `0x1d` (16 B), identical pattern to Stage17 (`nested-binary-correspondence.json`); 729 nested signatures | PASS |
| 10 | `derive-account-free.py`: `supportProfileDigest 88826eeb…` = `<PROFILE_DIGEST>` | PASS |
| 11 | invocation `succeeded`; schema `chirality-account-free-login-observation-result/v1`; 8 limbs (exact-supplier, keyring-backend, plaintext-fallback-absent, process-containment, storage-isolation, provider-network, bounded-protocol-purpose, retirement) all attempted+passed | PASS |
| 12 | `derive-payload.py` exit 0 (historical checkpoint `9f1df202…` = the nested-signed checkpoint bytes; plan schema `chirality.stage18-payload-plan/v1`) | PASS |
| 13 | invocation `succeeded`; checkpoint `payload-bound`; `supportProfilesIdentity.sha256 b47dcc48…` = sha256 of `stage18-support-profiles.json` | PASS |
| 14 | `derive-governance.py --issued-at 2026-09-11T14:25:29.000Z`: `payloadDigest 6c019d74…` = checkpoint `payloadManifest.sha256`; four `worker-prerequisites/*.json`; "No account/model functional qualification; eighteen worker empirical limbs pending human trial." (`signed-payload-and-supply.json`) and "All eighteen worker empirical limbs remain pending-human-trial." (`connected-source-contract.json`) preserved verbatim; recipe differs from Stage17's only in digests and `issuedAt` | PASS |
| 15 | invocation `succeeded`; six governance files present under `stage18-governance/` | PASS |
| 16 | `derive-seal.mjs`: `governanceCount 6`, release input digest `617c7453…` | PASS |
| 17 | invocation `succeeded`; sealed `verified: true`, appPath `$S/output/mac-arm64/Chirality.app`, `inventorySha256 8a3da519…` | PASS |
| 18 | `derive-post-seal.py` exit 0; `verify-copy.py` equals its Stage17 derivation; R9 app still absent; plan argv is the create-only `ditto --rsrc --extattr --acl` to the R9 path | PASS |
| 19 | `execute-durable-copy.py`: `succeeded`, exit 0, empty stdout/stderr (first durable write) | PASS |
| 20 | `verify-copy.py`: 1151/1151 entries, `semanticDifferenceCount 0`, `sourceDestinationSameInodeCount 0`, `destinationHardlinkGroupCount 0`, `xattrsEqual true`, `codesignVerifyExit 0` | PASS |
| 21 | `derive-final.py observation` exit 0; `expectedOuterInventorySha256 8a3da519…`; args `awaiting-R9-post-seal-observation`; plan `observe-trial-seal --app …R9.app` | PASS |
| 22 | invocation `succeeded`; schema `chirality-runtime-trial-seal-observation/v1`; `outerInventorySha256 8a3da519…`; `signed-app`, `fuses-and-asar`, `signed-peer-identity-binding` attempted+passed | PASS |
| 23 | `derive-final.py provision` exit 0; `trial-observation.json` byte-identical to `final-observation.stdout` (cmp) | PASS |
| 23b | R9 userdata and `runtime` created `700 501` (second durable write) | PASS |
| 24 | invocation `succeeded`, exit 0, empty stderr; anchor `created` at `…R9/runtime/release-authority/v2/release-anchor.json` with `trial-seal-observation.json` beside it | PASS |
| 25 | `derive-launcher.sh`: "R9 launcher created"; R9 launcher `8fbbc912…` (expected), mode 700, 3303 bytes; `launcher-r8-r9.diff` equals expected diff (cmp) (third durable write). Launcher NOT run. | PASS |
| 26 | launcher guard check | DEFERRED to the lead (only meaningful after section B) |

## Baseline changes

None. All 15 entries of the Stage17 static reuse baseline are byte-identical at the Stage18 frozen commit; `stage18-derivation-manifest.json` records `baselineChanges: []`.

## Deviations from the Stage17 procedure

1. Derivation: exactly the Stage17 deviations were carried (the Stage15-only `derive-wrapper.py` patches stay dropped, both guards kept, `stage17FrozenCommit` manifest field); the procedure-header patch was carried in Stage18 form. No other script differs from its Stage17 original beyond the RULES/HEX_MAP substitutions.
2. Carried stale text in `STAGE18_PROCEDURE.md` (conventions line `S13=`, "Stage17 / R3", "Durable R4 paths", "R3 userdata", `STAGE13_PROCEDURE.md` in 0c, the `fdb8c8e18…`/`769f8ef0…` commit references, "R4 guarded launcher"/"references R3" comments in `derive-launcher.sh`, "Stage17 had 464 emitted" at step 3) is inherited exactly as Stage17 inherited it and is flagged as non-gate text in the Stage18 header.
3. Five of my own gate probes were initially aimed at the wrong record shape or used a faulty shell test: 0c counted 28 root entries instead of the correct 27; gate 3 read a `schema` key where the wrapper plan carries `schemaVersion`; gate 9 looked for `commandDifferences` (twice) where the correspondence record carries `loadCommandDifferences`; gate 14 searched the governance recipe for the limitation strings that live in `worker-prerequisites/`; gate 18's `ls | grep` absence test returned `ls`'s exit under `pipefail`. In every case the `&&` chain halted before the next step, no output was created (verified: the observer directories and the R9 app were still absent when the chain resumed), the gate was then verified against the correct record and found passing, and the procedure resumed at the next step. No step was executed twice and no partial record exists.
4. The derive script was syntax-checked with an in-memory `ast.parse` (no `__pycache__` was produced; none exists under the stage root). `git diff`/`git log`/`git status`/`rev-parse`/`symbolic-ref`/`ls-files` reads were run against the preserved checkout and the lead worktree (read-only).
5. Step 14 `--issued-at` is the real UTC time `2026-09-11T14:25:29.000Z` (precedes the fixed expiry).
6. Tool stdout for steps 1–25 was captured into this session's scratchpad (`/private/tmp/claude-501/…/scratchpad/step*.stdout`) so gate probes could parse it; those are duplicates of terminal output only, every procedure record lives in the stage root as designed.
7. For the untouched-paths verification I ran a read-only `ls -l` of the R8 release anchor and a read-only `pgrep -fl` of the R8 processes; the R8 userdata was not otherwise opened.

## Durable writes and protected paths

Created: `/Users/ryan/Applications/Chirality Trial 20260910 R9.app` (step 19; codesign `--verify --deep --strict` exit 0 re-checked after step 25), `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R9` + `/runtime` with the provisioned `release-authority/v2/{release-anchor.json,trial-seal-observation.json}` (steps 23b/24), `/Users/ryan/Applications/Launch Chirality Trial 20260910 R9.command` (step 25).

Untouched (verified after step 25): no file under the Stage16 or Stage17 roots is newer than the Stage18 derive script; R7 launcher `c0db24b2…` and R8 launcher `e63670fe…` unchanged; R8 app has no files newer than the derivation; R8 userdata was not opened beyond the read-only anchor listing (its release anchor still carries its 04:00 mtime; the running R8 trial, GUI pid 93411 / daemon pid 93449, is still live); the preserved checkout is still detached at `684ef914…` with a clean Runtime/frontend tree (its `dist/`, `.next`, `dist-electron`, `dist-runtime` were replaced only by `run-build.py --execute`, with the Stage17 trees moved aside under `prebuild-*`); the lead worktree has no changes other than this untracked `RETURN.md` (the Stage18 `BRIEF.md` is already tracked at the frozen commit). No GUI app launched, no `.app` opened, no `Launch … .command` run, section B not run, `~/Library/LaunchAgents` not read or written, no `security` command, no keychain enumeration, no git commit, no publishing. No account email appears in any record or in this return: the stage-root records contain `@` only as npm scopes and `package@version` tokens; the only email-like strings anywhere under the root (excluding the sealed app and build scratch) are two files of the supplier's bundled skill library inside the observer's private home (`account-free-runtime/…/private/home/skills/.system/…`), the same class Stage17 reported.

## Left for the lead

- Section B (quit the R8 GUI, `bootout` the `com.chirality.runtime` job, retire the R8 registration plist as `retired-r8-com.chirality.runtime.plist` in the Stage18 root), then step 26 (`'/Users/ryan/Applications/Launch Chirality Trial 20260910 R9.command' --check-only` → `Launch guard PASS`), then the first guarded launch of R9 (B5) and the post-launch `launchctl`/`plutil` verification.
- Governance limitations carried unchanged: independent post-build review of Supplier build05 pending; eighteen worker empirical limbs pending human trial.
- The Stage18 `templates/` are informational (placeholders resolved by the real step records now present in the stage root).

## Stage18 root inventory

Mode is octal; directories show their recursive entry count. `output/` (the sealed `mac-arm64/Chirality.app`, 1151 entries) is identified by the sealed `inventorySha256` and the durable-copy verification rather than per-file rows; `build-tmp/`, `prebuild-runtime-dist/`, `prebuild-app-generated/` are step 2 build scratch and the Stage17 trees moved aside.

| path | size | mode | sha256 | origin |
|---|---|---|---|---|
| `/private/tmp/chirality-local-human-trial-20260910-18/STAGE18_PROCEDURE.md` | 28798 | 600 | `c98ca06e63250b2433f4e7c61014b4c0eee0a7ebe3771f6ad9e60bcd9d6583a6` | derivation (text-copy + header patch) |
| `/private/tmp/chirality-local-human-trial-20260910-18/account-free-observer-invocation.json` | 4718 | 600 | `0ea5c8e91b9594ae92c8a03aa35684e83b61395ba5c0a545f6430f039677b1af` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-18/account-free-observer-plan.json` | 4640 | 600 | `d2e93f0fdb8f468e3cd07cbfa498e4989c921ddd8abfeb2a0e8128c28cb5db15` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-18/account-free-observer.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-18/account-free-observer.stdout` | 1435 | 644 | `a6d71e7bd93a7f464d3c6c38d942e4e0f5b7e2188b70d7875f51bf3e6413c7cb` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-18/account-free-runtime/` | 120 entries | 700 | `-` | step 10 (dir) / step 11 (evidence) |
| `/private/tmp/chirality-local-human-trial-20260910-18/build-invocation.json` | 226807 | 600 | `e1d5bfbdf187e217d5d8396d7853c149cdf144c48c3402759f8228a0b004e3d7` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/build-plan.json` | 3549 | 600 | `ba5b22a695891a267b6a583854879d15b8f8a5d80e152efe5180b9ac62ae986c` | derivation (json-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/build-tmp/` | 3 entries | 700 | `-` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/check-admitted.mjs` | 964 | 700 | `384439c56158d5f9f60b45062185fa4d8d35be8d8a8169bbe92d19c1cfe5a8e0` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/compare-macho.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/compare-macho.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/compare-macho.stdout` | 1295 | 644 | `a649fa07e77b22399bb93a9fb9dea9a964b7fd67fe50b2aee53685f07c4a626a` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/compare-macho.summary.json` | 1365 | 600 | `74a8c6876ae0fad42923b2b6c700d1e85c85ba16a07d1e20469c1a92c24dafda` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/compare_macho.py` | 3558 | 700 | `e1caac109f3f6f73886761f32cff34dfd5953100e1c44047edb2240d7a00cabf` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-account-free.py` | 5299 | 700 | `8118b39a622e31bb7912da5006ee22802c67a65129352ef4c6ad6645d2f1f91e` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-final.py` | 8114 | 700 | `6eb0d8c9956aa98d29b6f670c44f3d8b2c62f33d17c9811d472a5c12374475fa` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-governance.py` | 7141 | 700 | `90cde883798c76f7fd6f54fcb9f197d5dd4f593c6a200b867ef0418c741a7ae2` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-launcher.sh` | 2470 | 700 | `1c0551c1fe18c5f97d4d7b824f9d0ec49a3d2c49d5d00b499ad37c6919c15a47` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-measure.mjs` | 2717 | 700 | `5cda998c0e0d0e784129cc6011cecde7dacaa0eae96263844533af195b9b42f1` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-payload.py` | 5061 | 700 | `bc91ef45202c13485aa6948bec48a7fcc7bae14498cb74d56ecbb1cf208d32a8` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-post-seal.py` | 2785 | 700 | `e6a2449ccce544f15902c5f241dbf79870752432a9c92c9c26f0aaa774a1758f` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-profile.py` | 1704 | 700 | `2f6053964298d0acebf0b09367bac545fdebf6825f746d37be3eefbc5bea7970` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-seal.mjs` | 3933 | 700 | `c363be19309a838d8a32c30a555fa7d3fea6534806c4b6303551e3d76c8f6468` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-stage18-from-stage17.py` | 20249 | 700 | `60cc1530de08816be7152cb1b328884d503bd98c8bcfd53a0a89fcf710151b4f` | authored by this task (adapted from Stage17 derive-stage17-from-stage16.py) |
| `/private/tmp/chirality-local-human-trial-20260910-18/derive-wrapper.py` | 5015 | 700 | `7e0cd53301523ce0b4578d08870f7064cd7ad42b47c9b81d7b3383d2c7523fb4` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/durable-copy-invocation.json` | 1717 | 600 | `6fa27305c81742141f3e79bf79de1a7836cfd114f18a57dceb715facb7740ec0` | step 19 |
| `/private/tmp/chirality-local-human-trial-20260910-18/durable-copy-plan.json` | 1608 | 600 | `cf98909df0dcda508ca78fa914d012016e4bc23fa071ac914c9e66435cfda795` | step 18 |
| `/private/tmp/chirality-local-human-trial-20260910-18/durable-copy-verification.json` | 1456 | 600 | `69c47d84ac91187934a7728e0652df2752f67a1d129b4b322f16ab8ec443e10f` | step 20 |
| `/private/tmp/chirality-local-human-trial-20260910-18/electron-build.stderr` | 303 | 644 | `a0c9fa095c59a7ee1cc0b98edaddeaa031014278c41cab266139a751e45541d4` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/electron-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/execute-durable-copy.py` | 2495 | 700 | `2e7905c84bc19efc651c8ed53fc7149436278e862efb49143daf21cd8fb1ab3f` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/execute-plan.py` | 1648 | 700 | `6bb43c956c5af0fdc5c0f7a71afa73a669de9dfc0d339796bfc2e5f8318c40b5` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/final-observation-invocation.json` | 3904 | 600 | `83212da3d00857da019fed9a2f709778895f9c3de391c21cc1837885cc3d0ca8` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-18/final-observation-plan.json` | 3824 | 600 | `0232a5ed995494d7c23317510555637d70651c4603ab35aa41ba6c02fb432306` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-18/final-observation.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-18/final-observation.stdout` | 811 | 644 | `6f81db546cb5a7eefbdf1917f021e0e0c1862990e4079af0929cd02d0af4a644` | step 22 |
| `/private/tmp/chirality-local-human-trial-20260910-18/final-observer-home/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-18/final-observer-tmp/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-18/generate-candidate-evidence.py` | 4011 | 700 | `566e2ac8d738eaf031c144960f3d3a830ae5127d1f0c43c6f96b4d987b3efc51` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/governance-invocation.json` | 4266 | 600 | `f5527c7108ab039b48f4a6e6a061033baefee1e1245d60f8d079cd7d60730b06` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-18/governance-plan.json` | 4188 | 600 | `7cd87fadabf618fba7f1c166a97ab0058c5be9142b1f21e5b5d13242dbd19016` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-18/governance.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-18/governance.stdout` | 801 | 644 | `490f0968485ae504bae49d73501e21998c1f02b4208f442ccd880b14424fdc4a` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-18/launcher-r8-r9.diff` | 992 | 600 | `05645c7bad6d5e3e1bd55dde3f771794fe1cad650c34bb33a21e06932c2b029b` | step 25 |
| `/private/tmp/chirality-local-human-trial-20260910-18/launcher-r8-r9.expected.diff` | 992 | 600 | `05645c7bad6d5e3e1bd55dde3f771794fe1cad650c34bb33a21e06932c2b029b` | derivation (text-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/measure-home/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-18/measure-support-invocation.json` | 2967 | 600 | `ef3af6bc6533e959444e6db4e4c88c1d1195f4814dc0932fb425cfbd4096ea35` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-18/measure-support-plan.json` | 2716 | 600 | `446bd4b19f131b4181bf819d81e73beee7e2fe751145e653cc3d649029931348` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-18/measure-support.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-18/measure-support.stdout` | 1562 | 644 | `d573159b4c269455fc0dd4441b5fd49f65330ca9d9ad79213c792e186ab73ad4` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-18/measure-tmp/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-18/nested-binary-correspondence.json` | 45037 | 644 | `4fcd7afa5b0248e0fffba41dfdb4bcace061a5d720c808b7715d12af0c45a8ad` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/nested-signed-checkpoint.historical.json` | 275289 | 600 | `9f1df202161a63cc818aaf9727e6208bd24167305dccd53618e259470cf515a1` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-18/nested-signed-checkpoint.json` | 275552 | 600 | `fa7d0c69e772ea7459522df77e602e4569e48fd84b0b3a88f4227dd57cb5fdc1` | step 5 (rewritten in place at step 13 to payload-bound) |
| `/private/tmp/chirality-local-human-trial-20260910-18/nested-signed-checkpoint.json.sealed.json` | 488 | 400 | `786dd6c1ca8820526dc685e1356ace929b8694caceb33d0eec44c3b466808127` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-18/next-build.stderr` | 830 | 644 | `98c788348dd0116f0039b48155e26c4d39f85c5a5b84fd7bdec040cb78c44028` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/next-build.stdout` | 4637 | 644 | `f09be823bb2316b8f01f2070d4c555094cb1716f83a8cd6c4ab472503db34c97` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/observer-home/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-18/observer-tmp/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-18/output/` | 1155 entries | 755 | `-` | step 5 (output/mac-arm64/Chirality.app; identity = sealed inventorySha256) |
| `/private/tmp/chirality-local-human-trial-20260910-18/payload-bound-checkpoint.historical.json` | 275552 | 600 | `fa7d0c69e772ea7459522df77e602e4569e48fd84b0b3a88f4227dd57cb5fdc1` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-18/payload-invocation.json` | 4773 | 600 | `1255795a6f943b053dcc49c74cd4e7a28da92f815e31384ea382bed2ea114668` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-18/payload-plan.json` | 4694 | 600 | `c96a5829b5efd3925bd7d7f1075a91bf26cac60191011b35e72b471b6842c57a` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-18/payload.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-18/payload.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-18/prebuild-app-generated/` | 483 entries | 700 | `-` | step 2 (Stage17 .next/dist-electron/dist-runtime moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-18/prebuild-runtime-dist/` | 478 entries | 700 | `-` | step 2 (Stage17 dist trees moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-18/provision-invocation.json` | 6189 | 600 | `bf3d218b52bb35ad9407f20d3c5ca15056046071e41bb4e0b0d51dd156c021fe` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-18/provision-plan.json` | 6110 | 600 | `80e8755634edd4cdccb705ee410db9da7645c266cd83044c582709db87ce1dba` | step 23 |
| `/private/tmp/chirality-local-human-trial-20260910-18/provision.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-18/provision.stdout` | 995 | 644 | `7fb168fd0eef09a2164dfa87fe8b49c7f33b2533ffc7dd293ab134031ff4dd57` | step 24 |
| `/private/tmp/chirality-local-human-trial-20260910-18/release-inputs-inspection.json` | 169308 | 600 | `65ca20e4cd69c89e9fe096701255e8591330297eed466864acb3e9ce7d181702` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-18/run-build.py` | 6264 | 700 | `a338a3a33172e68411f7577ee484543a7c0be1038c474bc4114620650f26ac85` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/run-measure.py` | 2571 | 700 | `14142d65d1b5d1f8ea2476052415f9b99577726fd811ce734c441be451de5adc` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/run-wrapper.py` | 3143 | 700 | `84a97093bf53a8871e8baf3055cc152acf03e339a5b020c288d9e9eeab43b3b9` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/runtime-build.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/runtime-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/runtime-clean.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/runtime-clean.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/runtime-consumer-resolution.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/runtime-consumer-resolution.stdout` | 3850 | 644 | `4a0756007a986bb86d67ba2835e221a6613b6fc06093a81197b5e1134f76f15d` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-18/seal-invocation.json` | 7091 | 600 | `2515c3f919f3b3cb477285a4054191c73a887a8040115db6a4e61ce5273588b2` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-18/seal-plan.json` | 7013 | 600 | `b7435f74b5b1ccad5f6c151c9d9e8c569ee291437f02bdf44138b604e3d908dc` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-18/seal.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-18/seal.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-18/signature-display.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/signature-display.stderr` | 1079 | 644 | `b2ab91d06b6717f95de468730a61b42be3d13632417db81f3e47ff6a57a9ea45` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/signature-display.stdout` | 118 | 644 | `3b2f91085ad953a851afeba4befd0f4e32557a97cb1a94957e8847b428936d52` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/signature-verify.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/signature-verify.stderr` | 3004 | 644 | `7f708eed2d33cb9b567a5e15455991d7fec9f92571e5c0feef2539814b218e29` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/signature-verify.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage17-static-reuse-baseline.json` | 4137 | 600 | `18bcbf63f912992346c1fe0f3b73c7528d7ae77eb3fe1f1a014ecdb6af60efa6` | derivation (re-identified baseline) |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-account-free-observer-recipe.json` | 1697 | 600 | `2c474178b643fe936ac31f54243fd71d19d47bf03a6caea3451c064b0eb69a24` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-derivation-manifest.json` | 30022 | 600 | `5aaaa21b24e5e6437433c17c277012d1b9c98901451ed019fb7beb4ff6e609eb` | derivation |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-final-operation-arguments-sealed.json` | 1563 | 600 | `0576af1d00c5af207f015c4b0ef79fcdd7b4bba6e6eef8c98cdd0c93d91e49e4` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-governance/` | 6 entries | 700 | `-` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-governance-recipe.json` | 3967 | 600 | `b123708b1a47c289aee2cc892d130f4c319e1ca3308c085f7eec6f95bcf8143b` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-measure-support-recipe.json` | 108217 | 600 | `3f4c38f3728b3e16547730a4124b419675bd78968bd6bf094794058e9191cd17` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-signature-evidence.json` | 1433 | 600 | `4f754298cf27fb7596d6afbd9cdd1b88ce1926af7815a9e730d739966c840deb` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-18/stage18-support-profiles.json` | 1892 | 600 | `b47dcc48b33d005f3b1e40873edd87cb2322c86f3ea318563c2cd59df739c5fc` | step 8 |
| `/private/tmp/chirality-local-human-trial-20260910-18/templates/` | 19 entries | 700 | `-` | derivation (19 templates) |
| `/private/tmp/chirality-local-human-trial-20260910-18/trial-observation.json` | 811 | 600 | `6f81db546cb5a7eefbdf1917f021e0e0c1862990e4079af0929cd02d0af4a644` | step 23 |
| `/private/tmp/chirality-local-human-trial-20260910-18/verify-copy.py` | 3453 | 700 | `5efd1650b5359d84d03b9a6e6688790c8774af6cef80b520cbd6d97ce6775deb` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/verify-runtime-consumer.mjs` | 2178 | 700 | `dec5f27349a57d128ba63f65605ed51b20944eda146430f914a2353b5e6ee841` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-18/worker-prerequisites/` | 4 entries | 700 | `-` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-18/wrapper-invocation.json` | 229302 | 600 | `0b8c54c890c60e452b34cbe59080fe744051ee22dca5280f502899fbac43ee65` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-18/wrapper-plan.json` | 228849 | 600 | `202973f7bc07a791ea0487d4f0c38e682266446193e2574c96410f58a1004bbe` | step 3 |
| `/private/tmp/chirality-local-human-trial-20260910-18/wrapper.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-18/wrapper.stdout` | 14860 | 644 | `e0e4c3fe17a1bab00bb32535deb8e4073b34fc6a2f7b7c786dbd1fb3f4017e1d` | step 5 |
