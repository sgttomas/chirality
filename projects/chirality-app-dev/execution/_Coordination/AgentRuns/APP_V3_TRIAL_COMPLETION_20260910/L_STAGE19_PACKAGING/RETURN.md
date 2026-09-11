# L_STAGE19_PACKAGING — RETURN (Type 2 TASK, Fable 5.1)

## Outcome

STOPPED AT STEP 22 (first failed gate). The Stage19 (R10) tooling was derived from the completed Stage18 (R9) tooling by `derive-stage19-from-stage18.py` (43 derived files, zero baseline changes), and preflight 0b–0e plus steps 1–21 of the derived `STAGE19_PROCEDURE.md` were executed in order with every gate verified, including the first durable write (step 19: the R10 app). Step 22 (`execute-plan.py final-observation`, the `observe-trial-seal` observer against the R10 app) exited 1 with `Hosted release provisioning failed: Verified App account host is unavailable`; its invocation record is `status: failed`. Per the brief the procedure stopped there: steps 23–25 were not started, the second and third durable writes (R10 userdata, R10 launcher) do not exist, and the partial step-22 records were left in place (failed-attempts convention). Step 26 is deferred to the lead. No step was re-run.

Root cause (read-only source inspection, see "Failed gate" below): a Runtime source change inside the Stage18→Stage19 delta (commit `b1d0802da`, "Revalidate the issued packaged basis by identity at a single boundary") makes `inspectHostAccountSignedPeerIdentity` `lstat` the four signed-app files and throw `PACKAGED_APP_PATH_INVALID` for any symlink; `Contents/Frameworks/Electron Framework.framework/Electron Framework` is a symlink (`-> Versions/Current/Electron Framework`) in every Electron bundle, the R9 app included. The R10 app itself is well-formed (strict codesign verify exit 0; durable copy verified 1151/1151 against the sealed inventory). This is a defect in the frozen source, not in the derivation or the packaging steps.

Frozen source: `5360827a34fc1449b4734bd76ec4af650bc2cb8d` on `claude/chirality-v3-mvp-trial-ab05cb` (Stage18 froze `684ef914d088ac33cefdf1519810af4e69020d79`).

Stage19 root: `/private/tmp/chirality-local-human-trial-20260910-19` (mode 700, uid 501; every file create-only).

## Admitted digests

| Item | Value |
|---|---|
| Frozen commit | `5360827a34fc1449b4734bd76ec4af650bc2cb8d` |
| Outer inventory sha256 (`<OUTER_INVENTORY_SHA256>`, sealed result `inventorySha256`; = durable-copy verification `sealedInventorySha256`; NOT yet observed on the R10 app at step 22, NOT provisioned) | `ae49789e4ae06666de1c0ee336bf112f892533b85489ebb6f44f82e18ada7fbe` |
| Payload digest (`payloadManifest.sha256`, size 88536; governance recipe `payloadDigest`) | `885ff24390dd8efd15ad91588af18e4745a71651270e86d21733f0abec1d87a1` |
| Support-profile identity: `profileDigest` (`<PROFILE_DIGEST>`) | `9416d7f9cc7063329807dfe1e87d48cec9e3d15b63285546fb67ec27dfb18651` |
| Support-profile identity: sha256 of `stage19-support-profiles.json` (1892 bytes; = checkpoint `supportProfilesIdentity.sha256`) | `3b9378d3451155a02d3dbf73042a6838c273ed4238848a8d3f6f185f9ebc1135` |
| Support profile `kernelHelperContractDigest` / compiler `sourceDigest` (both moved from Stage18 because the Runtime source changed, as the brief expected) | `b12f845a14a0bf95c614334f778e11c4f267d4a6a55edcfa7a3ba69a5f582206` / `3983efb04484350a7102a6b663365e00e544c0482d8ce591d1eb54e5e137f403` |
| Sealed result file `nested-signed-checkpoint.json.sealed.json` sha256 (488 bytes, mode 400; `verified: true`) | `4e16159b623df60377a8702027a7db2b61db8e9722c2104ac54b55f81e919819` |
| Sealed result `peerRequirementSha256` (unchanged from Stage18) | `8ef4b07368d9bedbf4016b6dc9c6dcf5dec8741cf3246c466e7e36b68ceff69c` |
| Release input digest (`CHIRALITY_RUNTIME_V2_INPUT_DIGEST`, step 16) | `0767ebc605f770c264554de254baacc3a77e5cc2e6d6b8fd29b673fd1d761a98` |
| Payload snapshot digest (steps 5–7, 599 entries) | `87ef181c8f03e55983412c7a2b263a05ae9cdabaab487183f125114ccb34d57a` |
| R10 app path | `/Users/ryan/Applications/Chirality Trial 20260910 R10.app` (exists; step 19 durable write) |
| R10 app inventory sha (durable-copy verification `sealedInventorySha256`; 1151 entries source = destination, roster digest `c6a3aee3718469740e0ad5c4d4e5c4f41ea106d5ef0a8efdd69b650ec9010d5c`) | `ae49789e4ae06666de1c0ee336bf112f892533b85489ebb6f44f82e18ada7fbe` |
| R10 app `mainCodeDirectoryHash` | not recorded (step 22 produced no observation) |
| Trial observation sha256 | none (step 22 failed; `final-observation.stdout` is empty, `trial-observation.json` not created) |
| R10 release anchor | none (step 24 not reached; R10 userdata not created) |
| R10 launcher `/Users/ryan/Applications/Launch Chirality Trial 20260910 R10.command` | NOT CREATED (step 25 not reached). Expected identity computed at derivation from the real R9 launcher bytes: `0950daa9d6597c02aa70f2eafddb26fb2212093775248379a79441968fe0b467` (recorded in the manifest, `derive-launcher.sh` and `STAGE19_PROCEDURE.md` step 25) |
| R9 launcher source (unchanged, verified before and after) | `8fbbc9120ad7363bdb9c715416d8c721315d63d65ff01d24cdb09ecbc37a3b4b` |
| `launcher-r9-r10.expected.diff` (996 bytes) | `c8607851b35fb990d465e4451765974a10552e52aae1066d03f7d4381dfbc331` |
| Signed in-app native addon / supplier (support profile `nativeAdmission.sha256` / `supplier.sha256`; = `compare-macho.summary.json` `final`) | `4ad863bdb3328d3722655294c961134d26153032ea968c5374ff2a8d39663be8` / `84e46f3681c5f31597ba9dd20d1537de59b3416495a4a4242acb8759d53c9d88` (757506928 bytes) |
| Unchanged admitted digests (checked at step 1) | dependency resolution `e83a525c2c38ce267abdaa0a25d26cab97baf9bc3acaa1c8e14e5ae86366b202`; Supplier tree `0513989b14af3a7c45cdf9caaf67be0c9e40a1e8e2d2388428f91e34244b8a34`; Supplier executable `eecbc73eea2d472cfefb285dcee6d7ca46024668c2e8d907a1452053c7745189`; native addon `fa40fc23eb6d9a4de857652c314de4d2d89a6f2547fc24da0f48fcdf04a184f4`; governance expiry `2026-10-10T22:43:56.184Z` |
| Governance issued-at (step 14, real time) | `2026-09-11T16:01:18.000Z` |
| Account-free observer runId | `dcfd5acf-2732-4dd5-9cac-cfc6f96a550a` (observation `account-free-observer.stdout`, 1435 bytes, sha256 `05c7882413444723b42c6b071d5de04066764289ff8fa8284fa629941a099e4a`) |
| Signature evidence `checkpointSha256` (= `nested-signed-checkpoint.historical.json`) | `32a05958e48dca30e79d6024786857cb993dbdeb9c00a5629415fb0922d69039` |
| Derivation manifest `stage19-derivation-manifest.json` | `71d2dab26c1acfafc943997997075c14cd665bc3007ca202ed56e98761fe5dfa` (30042 bytes) |
| `STAGE19_PROCEDURE.md` | `a9a8b088024f2ffad75c593949dbdfcd28e876c7f115fafcd8e424f2bce9834c` |

## Derivation

`/private/tmp/chirality-local-human-trial-20260910-19/derive-stage19-from-stage18.py` (21605 bytes, mode 700, sha256 in the inventory) is the Stage18 script with:

- RULES shifted one stage (35 ordered rules): `20260910-18→19`, `20260910-17→18`, `stage18→19`, `stage17→18`, `Stage18→19`, `Stage17→18`, `Chirality Trial 20260910 R9→R10` then `R8→R9`, `-r9-build→-r10-build`, `R9/R8 durable`, `create-only R9→R10`, `awaiting-R9-→R10-`, `R9 userdata→R10`, `R9 copy→R10`, `launcher-r8-r9→launcher-r9-r10`, `r9-first-launch→r10`, `R9/R8 launcher`, `'R8'→'R9'`, `R9/R8 registration`, `running R9/R8 trial`, `R9/R8 app`, `R9/R8 executable`, `R9 provisioning→R10`, `retired-r8-→retired-r9-`, `first GUI launch of R9→R10`, `retires the R8→R9`, `Stage18 (R9)→Stage19 (R10)`, `Stage17 / R8→Stage18 / R9`, `Stage/R8/schema→Stage/R9/schema`. Applied in order so a value shifts exactly once: every `R9→R10` rule precedes its `R8→R9` counterpart, so the `R10` text produced first is never re-matched by an `R8` pattern, and no rule has an `R1`-prefixed pattern, so `R10` is never touched by a later rule. (`Stage18 (R9)` and `Stage17 / R8` cannot match once the earlier `Stage18→19`/`Stage17→18` rules have run, exactly as their Stage18 counterparts could not, and are carried unchanged; `Stage/R8/schema→Stage/R9/schema` does apply, rewriting the one comment in `derive-post-seal.py`. A residue grep for `\bR8\b`, `20260910-17`, `Stage17`/`stage17`, `(R9)`, `Stage18 / R9`, `R1[0-9][0-9]` and `launcher-r8` over every derived file finds nothing outside the manifest, the derive script's own docstring/rule table/anchor text, and the intentional Stage19 header sentence.)
- HEX_MAP: `e63670fe…` (R8 launcher) → `8fbbc912…` (R9 launcher, verified against the real file), and `8fbbc912…` (expected R9) → `0950daa9…` (expected R10, computed from the real R9 launcher bytes by the same three-reference sed derivation; the guard confirmed exactly those three references changed). Single-pass lookup, so no double mapping. KEEP_HEX unchanged (5 digests).
- Constants: `FROZEN_COMMIT` = `5360827a…`, `STAGE18_FROZEN_COMMIT` = `684ef914…`, `STAGE17_FROZEN_COMMIT` = `dc8a3ee1…` (needed by the anchor); `STAGE16_FROZEN_COMMIT` and the `STAGE17_HEADER` constant are dropped exactly as the Stage18 script dropped `STAGE15_FROZEN_COMMIT` and `STAGE16_HEADER`. The diff of the two derive scripts has exactly the same hunk structure (same line numbers) as the Stage17→Stage18 derive-script diff.
- SEMANTIC_PATCHES: only `STAGE19_PROCEDURE.md` (1 patch): the Stage18 title + "Stage18 note" paragraph (post-RULES anchor, unique) replaced by a Stage19 header naming `5360827a…`, the ten-commit / 34-file (639/98) delta from the brief (login-latency merge: `exact-supply.ts` hashing once per process and revalidating by filesystem identity, the six files dropping duplicate before/after revalidations, `hosted-bootstrap.ts` admission without blocking the status poll; R9 first-turn repairs: new `retirement-failure.ts`, the five files keeping the turn's own failure with the retirement diagnostic as its cause, `codex-session.ts` interrupting an expired turn, `PACKAGED_REQUEST_TIMEOUT_MS` 90 s / `PACKAGED_TURN_TIMEOUT_MS` 30 min, `hosted-identity-binding.ts` lineage successors, fenced ready admission retired as sign-in required; three frontend files; tests; coordination records), "none of the 15 baseline inputs changed, no `npm install` needed", the expected `kernelHelperContractDigest`/`sourceDigest` movement, plain `derive-governance.py` at step 14, section B retiring the R9 registration. Exactly the deviations the Stage18 RETURN recorded are carried: the two Stage15-only `derive-wrapper.py` patches remain dropped (no anchor exists in Stage18's script either), the survivor guard for `SUPPLIER_MAP`/build04/`c1809bb5…` is kept, the extra guard refusing any `derive-governance-build05` reference outside the procedure is kept, and the manifest records `stage18FrozenCommit`. Nothing else was dropped or added.
- Stage18 static reuse baseline (15 inputs) re-identified from the real files: **no changes** (`baselineChanges: []`); emitted as `stage18-static-reuse-baseline.json` (schema `chirality.stage19-stage18-static-reuse-baseline/v1`), byte-identical to Stage18's `stage17-static-reuse-baseline.json` except the schema line. Also confirmed by `git diff --name-only 684ef914d 5360827a3` (39 files, 34 of them Runtime/frontend, exactly matching the brief's `--stat`; none is a baseline path).
- Templates: 19 under `templates/` (prior-stage Stage18 basis hashes recomputed from the real Stage18 files; Stage19-only values are placeholders).
- Post-derivation checks: diffs of every derived script, the expected launcher diff and `build-plan.json` against their Stage18 originals were normalized through the same RULES/HEX_MAP and every one of the 139 changed lines is exactly the intended shift (`check-admitted.mjs` and `execute-plan.py` are byte-identical to Stage18's). The Stage18 root's `retired-r8-com.chirality.runtime.plist` (section B evidence written by the lead) is not a derivation input and was not read.

## Preflight and step gates

| Step | Gate | Result |
|---|---|---|
| 0a (verify only) | preserved checkout detached (no symbolic ref) at `5360827a…`; `git status --porcelain -uall -- projects/chirality-runtime projects/chirality-app-dev/frontend` empty | PASS |
| 0b | R10 app, R10 userdata, R10 launcher all "No such file or directory" | PASS |
| 0c | stage root `700 501`; only derived tooling present (27 entries: `templates/` with 19 entries, `STAGE19_PROCEDURE.md`, `launcher-r9-r10.expected.diff`, `stage18-static-reuse-baseline.json`, `build-plan.json`, `stage19-derivation-manifest.json`, 20 scripts, derive script) | PASS |
| 0d | `.next`, `dist-electron`, `dist-runtime` present | PASS |
| 0e | supplier `codex` (761918056), electron zip (122090802), two P2 records, `login.keychain-db` listed (read-only `ls -l`) | PASS |
| 1 | `run-build.py --check`: `status PASS`, `frozenCommit 5360827a…`, `dependencyResolutionDigest e83a525c…`, exit 0 | PASS |
| 2 | `run-build.py --execute`: exit 0; `build-invocation.json` schema `chirality.stage19-r10-build-invocation/v1`, `succeeded`, 5 commands exit 0, 468 emitted / 303 generated (Stage18 had 464; the four extra are the new `retirement-failure.ts` outputs); consumer resolution lists 8 specifiers into fresh `packages/*/dist`; checkout still at the frozen commit with a clean Runtime/frontend tree | PASS |
| 3 | `derive-wrapper.py`: 14 static + 468 + 303 + 11 records = 796; plan `schemaVersion` `chirality.direct-trial-wrapper/v1` | PASS |
| 4 | `run-wrapper.py --check`: PASS, 796 inputs | PASS |
| 5 | `run-wrapper.py --execute`: exit 0; invocation `succeeded`; checkpoint `nested-signed`, `dependencyDigest e83a525c…`, `supplierDigest 0513989b…`, appPath `$S/output/mac-arm64/Chirality.app` | PASS |
| 6 | `derive-measure.mjs`: `payloadSnapshotDigest 87ef181c…` = checkpoint `payloadSnapshotDigest`; 599 entries | PASS |
| 7 | `--check` PASS; `--execute` exit 0, invocation `succeeded`, stdout one `chirality-runtime-support-profile/v2` object | PASS |
| 8 | `derive-profile.py`: `profileDigest 9416d7f9…` | PASS |
| 9 | codesign verify/display exit 0; `Identifier=com.chirality.app`, `TeamIdentifier=8A7JL35U4S`, peer requirement recorded; native 0 load-command differences; supplier differences exactly index 4 `0x19` (72 B) and index 27 `0x1d` (16 B), identical pattern to Stage18 (`nested-binary-correspondence.json`); 729 nested signatures | PASS |
| 10 | `derive-account-free.py`: `supportProfileDigest 9416d7f9…` = `<PROFILE_DIGEST>` | PASS |
| 11 | invocation `succeeded`; schema `chirality-account-free-login-observation-result/v1`; 8 limbs (exact-supplier, keyring-backend, plaintext-fallback-absent, process-containment, storage-isolation, provider-network, bounded-protocol-purpose, retirement) all attempted+passed | PASS |
| 12 | `derive-payload.py` exit 0 (historical checkpoint `32a05958…` = the nested-signed checkpoint bytes; plan schema `chirality.stage19-payload-plan/v1`) | PASS |
| 13 | invocation `succeeded`; checkpoint `payload-bound`; `supportProfilesIdentity.sha256 3b9378d3…` = sha256 of `stage19-support-profiles.json` | PASS |
| 14 | `derive-governance.py --issued-at 2026-09-11T16:01:18.000Z`: `payloadDigest 885ff243…` = checkpoint `payloadManifest.sha256`; four `worker-prerequisites/*.json`; "eighteen worker empirical limbs pending human trial" and "All eighteen worker empirical limbs remain pending-human-trial." preserved verbatim; recipe differs from Stage18's only in digests, `issuedAt` and stage labels | PASS |
| 15 | invocation `succeeded`; six governance files present under `stage19-governance/` | PASS |
| 16 | `derive-seal.mjs`: `governanceCount 6`, release input digest `0767ebc6…` | PASS |
| 17 | invocation `succeeded`; sealed `verified: true`, appPath `$S/output/mac-arm64/Chirality.app`, `inventorySha256 ae49789e…` | PASS |
| 18 | `derive-post-seal.py` exit 0; `verify-copy.py` equals its Stage18 derivation; R10 app still absent; plan argv is the create-only `ditto --rsrc --extattr --acl` to the R10 path | PASS |
| 19 | `execute-durable-copy.py`: `succeeded`, exit 0, empty stdout/stderr (first durable write) | PASS |
| 20 | `verify-copy.py`: 1151/1151 entries, `semanticDifferenceCount 0`, `sourceDestinationSameInodeCount 0`, `destinationHardlinkGroupCount 0`, `xattrsEqual true`, `codesignVerifyExit 0` | PASS |
| 21 | `derive-final.py observation` exit 0; `expectedOuterInventorySha256 ae49789e…`; args `awaiting-R10-post-seal-observation`; plan `observe-trial-seal --app …R10.app` | PASS |
| 22 | `execute-plan.py final-observation`: observer exit 1; invocation `status: failed` (3.35 s); `final-observation.stdout` empty; `final-observation.stderr` = `Hosted release provisioning failed: Verified App account host is unavailable` | **FAIL — procedure stopped** |
| 23 / 23b / 24 / 25 | not started (no `trial-observation.json`, no `provision-plan.json`, no R10 userdata, no R10 launcher, no `launcher-r9-r10.diff`) | NOT RUN |
| 26 | launcher guard check | DEFERRED to the lead (only meaningful after section B; also moot until a launcher exists) |

## Failed gate: step 22 evidence

- Records: `/private/tmp/chirality-local-human-trial-20260910-19/final-observation-invocation.json` (3902 bytes, `status: failed`, `exit: 1`, sha256 `125512fb5d3272efd7c4885be6a4068e8f1a0ecf7c0c87df3bbb7405f3dbcab3`), `final-observation.stderr` (77 bytes, sha256 `16662e2d37598de06c781c7fd069d6238abd6aaa4ca57daf9012d7ea0a070921`), `final-observation.stdout` (0 bytes). `final-observer-home/` and `final-observer-tmp/` are still empty.
- The Stage19 plan is the Stage18 plan with only the stage root, schema label and the R10 app path changed (argv `provision-hosted-release-anchor-v2.mjs observe-trial-seal --app '/Users/ryan/Applications/Chirality Trial 20260910 R10.app'`, `HOME`/`TMPDIR` under the stage root, same `PATH`/`LANG`, same `cwd`, same 300 s timeout); the Stage18 run of the same plan shape succeeded in 4.4 s. The difference is the frozen Runtime source that the tool loads from the preserved checkout's fresh `packages/*/dist`.
- Message origin (read-only grep at the frozen commit): `packages/daemon/src/host-account-release.ts:21`, `unavailable(reason)` → `RuntimeError("ENGINE_UNAVAILABLE", "Verified App account host is unavailable", 503, { reason })`. The tool's `catch` prints only `error.message`, so the `reason` code is not in stderr.
- Delta responsible (read-only `git diff 684ef914d 5360827a3 -- …/host-account-release.ts`, `git log -S`): commit `b1d0802da` ("Revalidate the issued packaged basis by identity at a single boundary") added to `inspectHostAccountSignedPeerIdentity`, after the codesign/fuse/asar checks, an `observedFiles` capture that `lstat`s `input.executablePath`, `paths.framework`, `paths.plist` and `paths.asar` and throws `unavailable("PACKAGED_APP_PATH_INVALID")` when `!info.isFile() || info.isSymbolicLink()`. `paths.framework` is `Contents/Frameworks/Electron Framework.framework/Electron Framework`, which is a symlink (`-> Versions/Current/Electron Framework`) in the R10 app and identically in the R9 app (standard Electron framework-bundle layout; the pre-delta code only `readFile`d it, which follows the link). The `observedFiles` field did not exist at `684ef914d` (`git show` count 0). Consequence: at `5360827a…` the `observe-trial-seal` observer rejects every correctly built Electron app; the same function is also on the daemon's own `verifyHostAccountPackagedIdentity` path, so the lead should expect the packaged R10 runtime to fail its own signed-peer check at launch even if the observer were bypassed.
- Not done: no re-run of step 22, no diagnostic invocation of the observer, no source edits, no commits.

## Baseline changes

None. All 15 entries of the Stage18 static reuse baseline are byte-identical at the Stage19 frozen commit; `stage19-derivation-manifest.json` records `baselineChanges: []`.

## Deviations from the Stage18 procedure

1. Derivation: exactly the Stage18 deviations were carried (the Stage15-only `derive-wrapper.py` patches stay dropped, both guards kept, `stage18FrozenCommit` manifest field); the procedure-header patch was carried in Stage19 form. No other script differs from its Stage18 original beyond the RULES/HEX_MAP substitutions.
2. Carried stale text in `STAGE19_PROCEDURE.md` (conventions line `S13=`, "Stage18 / R3", "Durable R4 paths", "R3 userdata", `STAGE13_PROCEDURE.md` in 0c, the `fdb8c8e18…`/`769f8ef0…` commit references, "R4 guarded launcher"/"references R3" comments in `derive-launcher.sh`, "Stage18 had 464 emitted" at step 3) is inherited exactly as Stage18 inherited it and is flagged as non-gate text in the Stage19 header.
3. Two of my own gate probes were initially aimed at the wrong record shape: gate 9 read `index`/`cmd` at the top of each `loadCommandDifferences` entry where they live under `source`/`final`; gate 11 iterated `limbs` as a list of dicts where the observation carries a dict keyed by limb name. In both cases the `&&` chain halted before the next step, no output was created (verified: the observer directories were still absent before step 10 was started; `nested-signed-checkpoint.historical.json`/`payload-plan.json` were absent before step 12 was started), the gate was then verified against the correct record and found passing, and the procedure resumed at the next step. No step was executed twice and no partial record exists from a probe error. (The trailing step-13 and step-25 probes in those chains reported missing files only because the chain had already halted; the launcher script never ran.)
4. The derive script was syntax-checked with an in-memory `ast.parse` (no `__pycache__` was produced; none exists under the stage root). `git diff`/`git log`/`git show`/`git status`/`rev-parse`/`symbolic-ref` reads were run against the preserved checkout and the lead worktree (read-only); after the failure, the frozen source files named above were read from the preserved checkout (read-only) to locate the message.
5. Step 14 `--issued-at` is the real UTC time `2026-09-11T16:01:18.000Z` (precedes the fixed expiry).
6. Tool stdout for steps 1–21 was captured into this session's scratchpad (`/private/tmp/claude-501/…/scratchpad/step*.stdout`) so gate probes could parse it; those are duplicates of terminal output only, every procedure record lives in the stage root as designed.
7. For the untouched-paths verification I ran a read-only `ls -l` of the R9 release anchor directory and a read-only `pgrep -fl` of the R9 processes; the R9 userdata was not otherwise opened (its `hosted-bootstrap` private directory, `hosted-identity-binding.json` and `runtime/auth` were not read).
8. After the failure I additionally ran a read-only `ls -l` of the four signed-app paths in the R10 and R9 apps and a `codesign --verify --deep --strict` of the R10 app (exit 0) to characterize the failure; neither modifies anything.

## Durable writes and protected paths

Created: `/Users/ryan/Applications/Chirality Trial 20260910 R10.app` (step 19; strict codesign verify exit 0; verified against the sealed inventory at step 20). NOT created: `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R10` (step 23b not reached), `/Users/ryan/Applications/Launch Chirality Trial 20260910 R10.command` (step 25 not reached).

Untouched (verified after the stop): no file under the Stage17 or Stage18 roots is newer than the Stage19 derive script; R8 launcher `e63670fe…` and R9 launcher `8fbbc912…` unchanged; R9 app has no files newer than the derivation; R9 userdata was not opened beyond the read-only anchor listing (its `release-anchor.json`/`trial-seal-observation.json` still carry their 08:28 mtimes; the R9 daemon, pid 35885 `--runtime-daemon`, is still live); the preserved checkout is still detached at `5360827a…` with a clean Runtime/frontend tree (its `dist/`, `.next`, `dist-electron`, `dist-runtime` were replaced only by `run-build.py --execute`, with the Stage18 trees moved aside under `prebuild-*`); the lead worktree has no changes other than this untracked `RETURN.md`. No GUI app launched, no `.app` opened, no `Launch … .command` run, section B not run, `~/Library/LaunchAgents` not read or written, no `security` command, no keychain enumeration, no git commit, no publishing. No account email appears in any record or in this return: an email-pattern grep over the stage root (excluding the sealed app and build scratch, and the supplier's bundled skill library inside the observer's private home, the same class Stage18 reported) finds nothing.

## Left for the lead

- Decide the disposition of the step-22 failure: the frozen commit `5360827a…` cannot pass `observe-trial-seal` (and, by the same code path, the daemon's own signed-peer identity check) against any Electron bundle because `host-account-release.ts` now `lstat`-rejects the `Electron Framework` symlink. A source fix (resolve the framework path through `realpath`/`stat`, or capture the identity of the link target) and a new freeze, hence a Stage20 derivation, look necessary; the Stage19 root, its sealed `output/` and the R10 app remain in place as the failed-attempt record. If the lead prefers to reuse the R10 app under a repaired observer, note that the sealed inventory `ae49789e…` binds the app bytes but the anchor/observation were never produced.
- Section B (quit the R9 GUI, `bootout` the `com.chirality.runtime` job, retire the R9 registration plist as `retired-r9-com.chirality.runtime.plist` in the Stage19 root) and step 26 remain the lead's, but neither should proceed until a build passes step 22 and a launcher exists.
- Governance limitations carried unchanged: independent post-build review of Supplier build05 pending; eighteen worker empirical limbs pending human trial.
- The Stage19 `templates/` are informational (placeholders resolved by the real step records now present in the stage root; the step 22–24 templates have no corresponding real records).

## Stage19 root inventory

Mode is octal; directories show their recursive entry count. `output/` (the sealed `mac-arm64/Chirality.app`, 1151 entries) is identified by the sealed `inventorySha256` and the durable-copy verification rather than per-file rows; `build-tmp/`, `prebuild-runtime-dist/`, `prebuild-app-generated/` are step 2 build scratch and the Stage18 trees moved aside.

| path | size | mode | sha256 | origin |
|---|---|---|---|---|
| `/private/tmp/chirality-local-human-trial-20260910-19/STAGE19_PROCEDURE.md` | 30099 | 600 | `a9a8b088024f2ffad75c593949dbdfcd28e876c7f115fafcd8e424f2bce9834c` | derivation (text-copy + header patch) |
| `/private/tmp/chirality-local-human-trial-20260910-19/account-free-observer-invocation.json` | 4718 | 600 | `a250cb07ee71e771fb313bedf7eebf6b70ea3759e0b42271034c92fb2c90af5f` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-19/account-free-observer-plan.json` | 4640 | 600 | `7d2f60f79436a59708de5cadb50e3b8377c16265f8e193bee90cd31958201209` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-19/account-free-observer.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-19/account-free-observer.stdout` | 1435 | 644 | `05c7882413444723b42c6b071d5de04066764289ff8fa8284fa629941a099e4a` | step 11 |
| `/private/tmp/chirality-local-human-trial-20260910-19/account-free-runtime/` | 119 entries | 700 | `-` | step 10 (dir) / step 11 (evidence) |
| `/private/tmp/chirality-local-human-trial-20260910-19/build-invocation.json` | 227911 | 600 | `b8e2299120277b8b155619449599732752b0fec3ca3f1c1483ff3075e361e5da` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/build-plan.json` | 3553 | 600 | `44ab92e5d134094de9f8182443eb0e952b40b470c0bd94141bdcc22cf11058d6` | derivation (json-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/build-tmp/` | 3 entries | 700 | `-` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/check-admitted.mjs` | 964 | 700 | `384439c56158d5f9f60b45062185fa4d8d35be8d8a8169bbe92d19c1cfe5a8e0` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/compare-macho.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/compare-macho.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/compare-macho.stdout` | 1295 | 644 | `8b0a96a39e4cf4c2c7896816e0f2a0dcb78f2cba1d60de1879a0b244a62cee7f` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/compare-macho.summary.json` | 1365 | 600 | `71902c292241034b7b0aab6ac2ff260839c837a1033018879d11af093212ce2f` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/compare_macho.py` | 3558 | 700 | `ba13a118cdd3ac1bbed0feb040ce810ebdbc4c8f2e9db82626f8bdca95a6bea3` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-account-free.py` | 5299 | 700 | `d33b57fe996cb2a8eb6d23e07db47c6b630d7b22ce7b675d29b47e2cb91197e4` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-final.py` | 8123 | 700 | `51bf9de487d1ee7da86ff9d37736182a1ac642f233e7797d0b37109e0c62892a` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-governance.py` | 7141 | 700 | `277fb77b200be99341a46838fcdc2f9cfe4e6601c663dabecc8e861b52785fd3` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-launcher.sh` | 2483 | 700 | `240a11f490d8e0d048979f10ec450af5b6ac6364d5fa0eb803a42dc9c0f2b7bd` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-measure.mjs` | 2717 | 700 | `a2ffaa41078377c1e3f178fdcedb434d4fa3ce3c345be49971f4ec1e2fc30229` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-payload.py` | 5061 | 700 | `f9fe9ab6f33a59fcdaebee7503b1daf4a39d56cb5fc3431c53df16cbc1876baa` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-post-seal.py` | 2789 | 700 | `c10f559206c1e75532fb7f5ed6635336d36e661a2ba3fb82462803d3382f1957` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-profile.py` | 1704 | 700 | `7467d9bcc7396f77a7e9514941d17f573d5a1ad55dc7b32d47c553024b8db395` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-seal.mjs` | 3933 | 700 | `4f1ca1a32934fd212e00fdb6c4b8a6169327e53908b8e02b81e4feca128b2a80` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-stage19-from-stage18.py` | 21605 | 700 | `b8568717df29613cfeef1cd2ba4f61779ade3a3d0f157c99619869180cbe822a` | authored by this task (adapted from Stage18 derive-stage18-from-stage17.py) |
| `/private/tmp/chirality-local-human-trial-20260910-19/derive-wrapper.py` | 5015 | 700 | `e4cad58743feb08ae32595c9ef14b7e37a5fd4beb66515a6e44ab0c227c3f812` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/durable-copy-invocation.json` | 1721 | 600 | `26327131376c69bc12d93c1327609b598e72f2ab45aa75c367eaf39a86428b14` | step 19 |
| `/private/tmp/chirality-local-human-trial-20260910-19/durable-copy-plan.json` | 1610 | 600 | `5402c293e5835bf410019af17fc4f807ff371402809f1244c31432fc2911b767` | step 18 |
| `/private/tmp/chirality-local-human-trial-20260910-19/durable-copy-verification.json` | 1457 | 600 | `1aaf2772bdd416977d8c7e0bbee3546e7d2a2c1f914bcda9a1103524395f363d` | step 20 |
| `/private/tmp/chirality-local-human-trial-20260910-19/electron-build.stderr` | 303 | 644 | `954b592c6b4f4eec78b05db8136f4a6d4e7924baa7d4ef6a8f3d4a84200d3e5c` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/electron-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/execute-durable-copy.py` | 2497 | 700 | `74f8ec05c2a84889cee10256902dc8686a2d5deab7b45b35f40e761846e533d1` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/execute-plan.py` | 1648 | 700 | `6bb43c956c5af0fdc5c0f7a71afa73a669de9dfc0d339796bfc2e5f8318c40b5` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/final-observation-invocation.json` | 3902 | 600 | `125512fb5d3272efd7c4885be6a4068e8f1a0ecf7c0c87df3bbb7405f3dbcab3` | step 22 (FAILED, status failed, exit 1) |
| `/private/tmp/chirality-local-human-trial-20260910-19/final-observation-plan.json` | 3826 | 600 | `508af2bfebf994cae6f4e6b12851acfc15784c2246f2a3227e7cdc721a4d70ae` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-19/final-observation.stderr` | 77 | 644 | `16662e2d37598de06c781c7fd069d6238abd6aaa4ca57daf9012d7ea0a070921` | step 22 (FAILED; the one-line failure message) |
| `/private/tmp/chirality-local-human-trial-20260910-19/final-observation.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 22 (FAILED; empty) |
| `/private/tmp/chirality-local-human-trial-20260910-19/final-observer-home/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-19/final-observer-tmp/` | 0 entries | 700 | `-` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-19/generate-candidate-evidence.py` | 4011 | 700 | `f880018fa61395960628b2b7431407123a213569eb1c4fecec83d5d028b18e4d` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/governance-invocation.json` | 4266 | 600 | `650f607d2c733af2e7221c264263e6515ee330ff287be7b1d7a4c2ae6f520b2a` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-19/governance-plan.json` | 4188 | 600 | `e08ba40a054b45b1e44e02dd9c4791c159a1829dc76dea693ceb429ca0332813` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-19/governance.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-19/governance.stdout` | 801 | 644 | `8af16c9e87738966ded892484625bad7ead55429fe9f881c43fe05074d935209` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-19/launcher-r9-r10.expected.diff` | 996 | 600 | `c8607851b35fb990d465e4451765974a10552e52aae1066d03f7d4381dfbc331` | derivation (text-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/measure-home/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-19/measure-support-invocation.json` | 2967 | 600 | `a76983724b07b0b58644a3e31d830aaf992c4c2e367f8fd0b740974b5a3867e9` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-19/measure-support-plan.json` | 2716 | 600 | `0ac6bf31dbcb894a2d0eb63958891e44adce06fb374e16416357c74953783f57` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-19/measure-support.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-19/measure-support.stdout` | 1562 | 644 | `da10468d87fc07d8558738ed6a4c41af40e3eddff21523c206e5c130114e047c` | step 7 |
| `/private/tmp/chirality-local-human-trial-20260910-19/measure-tmp/` | 0 entries | 700 | `-` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-19/nested-binary-correspondence.json` | 45037 | 644 | `3a2e8ede05f85262fe6680ee857d9d15f6ca48d941a5db85f64674aa5b84f6dc` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/nested-signed-checkpoint.historical.json` | 275289 | 600 | `32a05958e48dca30e79d6024786857cb993dbdeb9c00a5629415fb0922d69039` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-19/nested-signed-checkpoint.json` | 275552 | 600 | `3e02090711aeb7e2d0ea00a7ffca1fb2554c166bfaa079d73480c71f773fe457` | step 5 (rewritten in place at step 13 to payload-bound) |
| `/private/tmp/chirality-local-human-trial-20260910-19/nested-signed-checkpoint.json.sealed.json` | 488 | 400 | `4e16159b623df60377a8702027a7db2b61db8e9722c2104ac54b55f81e919819` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-19/next-build.stderr` | 830 | 644 | `e341bf7d65caaf43a3dbd762d6083ae7566d309034756c0a23157f80659a92ad` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/next-build.stdout` | 4637 | 644 | `19895c501608320a97a854fad863bcd577efb07e7df5ccef59c3fa8b80129750` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/observer-home/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-19/observer-tmp/` | 0 entries | 700 | `-` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-19/output/` | 1155 entries | 755 | `-` | step 5 (output/mac-arm64/Chirality.app; identity = sealed inventorySha256) |
| `/private/tmp/chirality-local-human-trial-20260910-19/payload-bound-checkpoint.historical.json` | 275552 | 600 | `3e02090711aeb7e2d0ea00a7ffca1fb2554c166bfaa079d73480c71f773fe457` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-19/payload-invocation.json` | 4773 | 600 | `b93e892292423874841361acb6215de93527117ef314e7d5ebfccc354aea6959` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-19/payload-plan.json` | 4694 | 600 | `f794b1e0e4aedf7ee798fe0488de20b9d5691600b8b16055861b07b627941502` | step 12 |
| `/private/tmp/chirality-local-human-trial-20260910-19/payload.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-19/payload.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 13 |
| `/private/tmp/chirality-local-human-trial-20260910-19/prebuild-app-generated/` | 483 entries | 700 | `-` | step 2 (Stage18 .next/dist-electron/dist-runtime moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-19/prebuild-runtime-dist/` | 478 entries | 700 | `-` | step 2 (Stage18 dist trees moved aside) |
| `/private/tmp/chirality-local-human-trial-20260910-19/release-inputs-inspection.json` | 169323 | 600 | `6d4c1af7127bf9a755bf95a6d23a4ac46db5c07b5ee6655a2cdc314e9065eeb7` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-19/run-build.py` | 6266 | 700 | `4854bbbb6dc8fa9fd297b03971879b16f521739f2e4c6fe9bf7f8fe21859f1e9` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/run-measure.py` | 2571 | 700 | `9774358a89fd48d5fd0d2aab87edc5d28208315aa80f194f08f8240658624cf2` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/run-wrapper.py` | 3143 | 700 | `b1117dff5cbef3aa7c102e2816100a3c6b8fef3aed450d46dd3529e37f1696b9` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/runtime-build.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/runtime-build.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/runtime-clean.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/runtime-clean.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/runtime-consumer-resolution.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/runtime-consumer-resolution.stdout` | 3850 | 644 | `aaeacb16d2811d1d73e8ac8b2b2a6046c60c1ba3b04f09a22c71c4ff7af9234f` | step 2 |
| `/private/tmp/chirality-local-human-trial-20260910-19/seal-invocation.json` | 7092 | 600 | `8124b6cb03c6648f7760a04e3b81c8d22e7f730c41f00333dd3ca8974d4d67b9` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-19/seal-plan.json` | 7013 | 600 | `11fe0d5cd91ff3c6e573916bd0b0bac915abad67aa4f9c0c9fbef8a8b428373b` | step 16 |
| `/private/tmp/chirality-local-human-trial-20260910-19/seal.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-19/seal.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 17 |
| `/private/tmp/chirality-local-human-trial-20260910-19/signature-display.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/signature-display.stderr` | 1079 | 644 | `3e5ec3f64a5807c4c3e70e8cfa8318f4ef91172316ac52944cb73ea447a37d7a` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/signature-display.stdout` | 118 | 644 | `3b2f91085ad953a851afeba4befd0f4e32557a97cb1a94957e8847b428936d52` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/signature-verify.exit` | 2 | 600 | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/signature-verify.stderr` | 3004 | 644 | `ee5cad449ee9db24c4e4789e73cd16282454e3191bcaf00aef13cb4f4cfac10e` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/signature-verify.stdout` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage18-static-reuse-baseline.json` | 4137 | 600 | `ed2227838acc2dc36b2e638617ce920c1fb2ee206d903858f21cb30bd481d875` | derivation (re-identified baseline) |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-account-free-observer-recipe.json` | 1697 | 600 | `0b3bbb62a660ab0f6eb11e35774b500d97f7e5c45a8e4de04ef0b29b2d1fbf66` | step 10 |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-derivation-manifest.json` | 30042 | 600 | `71d2dab26c1acfafc943997997075c14cd665bc3007ca202ed56e98761fe5dfa` | derivation |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-final-operation-arguments-sealed.json` | 1570 | 600 | `06d4820ef381ea88ddd6023aec394bae42b62f8e50f6382076632fe6e9f2221a` | step 21 |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-governance/` | 6 entries | 700 | `-` | step 15 |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-governance-recipe.json` | 3967 | 600 | `34dda500cf85498128a92a30704d2b9bc915fecb1c504ba6aedb7205f50c94a0` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-measure-support-recipe.json` | 108217 | 600 | `8dd51f962d0976b3275a359e9f670cf3407bde8117367382a7305b3532614dce` | step 6 |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-signature-evidence.json` | 1433 | 600 | `a0239c1ca00c55ae09c2ee99d2902bbbd21c93b24d5b91661abf332169125196` | step 9 |
| `/private/tmp/chirality-local-human-trial-20260910-19/stage19-support-profiles.json` | 1892 | 600 | `3b9378d3451155a02d3dbf73042a6838c273ed4238848a8d3f6f185f9ebc1135` | step 8 |
| `/private/tmp/chirality-local-human-trial-20260910-19/templates/` | 19 entries | 700 | `-` | derivation (19 templates) |
| `/private/tmp/chirality-local-human-trial-20260910-19/verify-copy.py` | 3455 | 700 | `47f8066c294e159bbf739a787a34a30b434bf991130799635067a58452010e3b` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/verify-runtime-consumer.mjs` | 2178 | 700 | `a369007ebb131f6bac5f1912a006f63ac9a5a188bdebdf91da01c39e07a2a59b` | derivation (script-copy) |
| `/private/tmp/chirality-local-human-trial-20260910-19/worker-prerequisites/` | 4 entries | 700 | `-` | step 14 |
| `/private/tmp/chirality-local-human-trial-20260910-19/wrapper-invocation.json` | 230410 | 600 | `12c551f8d3a6a18abf3e42cdf0c985c5219efbeef2a44962d6d73bee6fad93bd` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-19/wrapper-plan.json` | 229956 | 600 | `81a6b953dd73fbc1a96c774b8dc4039deefeba4ed7025d3496f08553edc2ae7b` | step 3 |
| `/private/tmp/chirality-local-human-trial-20260910-19/wrapper.stderr` | 0 | 644 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | step 5 |
| `/private/tmp/chirality-local-human-trial-20260910-19/wrapper.stdout` | 14860 | 644 | `6b45fce5750ab00db27843131381fa38a550bebf9cb728379fde96fef25bf1e1` | step 5 |
