# Phase-B executor terminal return / handoff

## Identity and verdict

- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`
- ChildInstanceID: `A2-PKG09-R20-PHASEB-EXECUTE-01`
- Mode: delegated-harness-native ephemeral-generalist Agent 2; role not mechanically enforced; evidence instruction-asserted; K-SUBAGENT instruction+config asserted.
- Final executor verdict: **BLOCKED**.
- Review readiness: **NO**. The sealed-brief terminal rule stopped the run on the first unexplained nonzero validation gate.
- Proof procedure blocks executed: **no**.
- Receipt-191, Git mutation, proof, signing, notarization, release, distribution, and external-network acts: **none**.
- Default operator surfaces (`com.chirality.runtime` and related default service/domain): **not queried or touched**.
- Owner Desktop prior evidence and the prior private proof root were not read, listed, traversed, or statted. Only the sealed-brief metadata-only exact-root absence gates and the authorized disposable precheck were used.

## Terminal failure — exact preserved evidence

The combined mechanical validation command exited `1` immediately after its candidate-whitespace predicate. Its exact captured output is:

```text
syntax=PASS
fixture_fidelity=PASS bytes=3049 sha256=9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531
json_files_valid=5 jsonl_files_valid=1
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log:16:   Generating static pages (6/24) 
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log:17:   Generating static pages (12/24) 
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log:18:   Generating static pages (18/24) 
candidate_whitespace=FAIL
```

The effective failing whitespace operation was the recursive candidate scan over the R20/status/TM candidate set **and the whole executor instance directory**, followed by `candidate_whitespace=FAIL` and `exit 1` when a match existed. The complete composite shell source was not separately persisted, so a byte-exact reconstruction of its unexpanded command text would be an unsupported claim. The exact path-expanded matches and exit are preserved above. The defect is in check construction: immutable copied terminal evidence (`desktop-pack.full.log`) was included in a candidate-semantic whitespace gate.

Exact byte context for each matched line ends in `29 20 0a` (`)` + one ASCII space + LF). There are exactly three such lines and no other line ending in a single ASCII space in the raw log.

- Preserved raw log: 15,852 bytes; SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`.
- Hypothetical normalization only (not written): remove the one ASCII space immediately before LF on lines 16–18; 15,849 bytes; SHA-256 `323378988774f6174b94a1cbeb90dc09d06d407a2faf6f1da3d955a9630076d6`.
- Recoverability: complete. The raw log remains unchanged in this instance, so either a normalized derivative can be deterministically regenerated while retaining the raw hash, or raw logs can be excluded from a semantic-candidate whitespace predicate.

No repair, rerun, or continuation was performed after the terminal decision. This `RETURN.md` is the only post-decision write.

## Completed / unfinished gate matrix

| Gate | Result | Frozen evidence |
|---|---|---|
| Instruction/context intake and Agent-2 activation | PASS | Root/App instructions, software profile, complete CHAT, Amendment 02, Plan/Graph V4, sealed brief, declared source/evidence read in sequence. |
| Git/basis identity | PASS | branch `codex/app-login-proof-r20-repair`; HEAD `cb008dc5d6aa9b249639c91f3453a18609530d0f`; parent `a702dd6ec5005b361c8c023b12b599a425e5e2b8`; frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`. |
| APP-HOLD reliance | PASS | register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint `5604717a7b0950f19850ac9542fd38a98cb883c7b7de2bd968d582abfed5dba7`; 53 records. |
| Prebuild ignored-output inventory | PASS | 465 ignored paths; sorted-list SHA-256 `bd7c06b9e614e5b69682f712dc65051ff50111693a798396978d842b9a9578e8`; `dist` 1,444,900 KiB, `dist-electron` 3,840 KiB, `.next` 199,836 KiB, `artifacts` 956 KiB. |
| `npm run electron:supply-chain` exact once | PASS | exit `0`; 145-byte log SHA-256 `200522b9040843bbc4eed6d781f1611b2d54f4f9dd5c8f285abe56688c49e422`. |
| `npm run desktop:pack` exact once, ordinary network-denied | PASS | exit `0`; no retry/escalation; 15,852-byte preserved log SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`; custom `electronDist` count 1; download/GitHub/release-assets indicator count 0. |
| Embedded dependency/instruction gates | PASS | dependency boundary PASS; runtime-source proof PASS; instruction root pass, 43 files, revision `cb008dc5d6aa9b249639c91f3453a18609530d0f`; summary SHA-256 `3a9666d40235dfbaedf16dc3da29b0bc541b64298ae2faec05dcb27a202d3b36`; manifest SHA-256 `c5b2bf101de6412ae63fd19ba76cac6c73cffa156357551c4203a54ce771135b`. |
| Package identity | PASS | `com.chirality.app`, version `2.0.0`/`2.0.0`, minimum macOS `15.0.0`; arm64 main 33,968 bytes/mode 0755/SHA-256 `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`; CLI 75,460 bytes/mode 0755/SHA-256 `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`; ad-hoc linker-only signing diagnostic and calibrated strict exit 1. |
| Packaged main socket guard | PASS | 1,379,516 bytes; SHA-256 `bfcf16002fc5132d0d96c68a5574927bfd0593b1ce905e71bea72a957bfc4ce1`; exact 103-byte guard present. |
| Exact disposable precheck exact once | PASS | pre/post exact-root metadata-only absence PASS; PID `48351`; 67-byte exact Unix socket; packaged CLI returned exact `[]`; SIGTERM daemon exit `0`; final exact root absent. Precheck log SHA-256 `859126564c1046fcad755774b89a307d9b00ef2fb85ad356c5f7d43f85e4766e`; stdout `d311677a7d83ddca96e4442c8f7dbd8407180c2edb9670a3cf01634c3cd86d85`; stderr `c01aed12ccf971f55d555fb76a228eb2bb6172e0cc99f3a2b3490a2d7f6a68d0`. |
| Fresh R20 label/destination absence gates | PASS | UUID `bf0d2e6c-f705-446e-8e4f-a073c6645933`; exact label `com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933`; root/plist/public/failed destinations absent and non-symlink. |
| Exact service read-only gate | PASS | `launchctl print gui/501/<exact-label>` exit `113`; exact text `Bad request.` then `Could not find service "com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933" in domain for user gui: 501`. |
| R20 record / minimal status / TM candidate authorship | COMPLETED PRE-REVIEW | Current hashes below. R20 keeps owner-reported R19 facts claim-calibrated and R20 documentation-only. |
| Staged-block shell-safety audit | PASS AFTER PRE-REVIEW REPAIR | Confirmed premature `stat '{}'` command substitution in the failure-capture block; repaired to destination/failed-log directory mode checks plus a `find ... ! -perm 600` count. Static audit: 7 blocks, exact `cd` then `set -euo pipefail`, `zsh -n` 7/7, no analogous premature substitution, no forbidden bootstrap/kickstart/default-operator/open tokens. No block executed. |
| Ordinary-sandbox `npm test` exact once | EXPECTED ENVIRONMENT DIAGNOSTIC | exit `1`; 21 failed, 1261 passed, 4 skipped; failures classified `ENVIRONMENT_SANDBOX_SOCKET_DENIAL` (`listen EPERM` TCP/Unix). Log SHA-256 `b0e940374fc41342b2ca00bf9cee98187320c6559ca1b06321e427ecfc72eda2`. |
| Sole local-socket cure `npm test` exact once | PASS | exit `0`; 1282 passed, 4 skipped; log SHA-256 `ec482e01748d566159a0886fa84f455a10200c06ef0cc0c890177bf9bea1cf8b`; no extra full-suite run. |
| Focused repair suite | PASS | 72/72, exit `0`; log SHA-256 `86763a2fc84d86f34ff2aadd64d6eed010f7a1a15f3e0b378f368965622eed27`. |
| Typecheck | PASS | exit `0`; log SHA-256 `6be4cb0a247e09985e6ce57668de3c06547f0a4e2400e257eae36da4584208a2`. |
| Receipt validator | PASS | VALID through frozen Receipt-52; exit `0`; log SHA-256 `4a31bf4f8309774e5a867718d8c267a06eb51477331b57abe1267abb839e969c`. |
| Authority-corpus status | PASS | v18, 8 MATCH, no drift; exit `0`; log SHA-256 `c7a8e08208ccd784d3d548e4b19cd9e4458927b081490d2261ece8383d971dd4`. |
| Self-check | PASS WITH EXISTING BASELINE | exit `0`; INFO 14 / NA 1 / REVIEW 4 / WARN 43; log SHA-256 `ad40c223a005f0cc4a58348b0a74c876b3d5126e391f6df165e59178f38d991f`. |
| Practitioner tests | PASS | 350 passed; exit `0`; log SHA-256 `e37aea43f5848789f77a4943204636989b97f3bc292ff832d9fee520d4580c73`. |
| Package verifier | PASS | exit `0`; log SHA-256 `e3c37d4378ff23fae6cb6f2c0abc77126a9c3f2d3c6fbe067888a4f0c6811034`. |
| Live Step-0 read-only re-audit | PASS | optionless preflight and before/after absence/service checks passed; no job inspection or mutation. |
| Mechanical block syntax | PASS | 7 blocks; exact shell-order and `zsh -n` checks passed. |
| Fixture fidelity | PASS | 3,049 bytes; SHA-256 `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`. |
| JSON / JSONL validity | PASS | 5 JSON files and 1 JSONL file valid. |
| Candidate whitespace predicate | **FAIL — TERMINAL** | Incorrectly scanned immutable `desktop-pack.full.log`; exact three matches and exit `1` preserved above. |
| Remaining composite checks after failure | **NOT RUN** | Candidate-semantic-only whitespace resolution; change-scope validator; final index refresh; `git diff --check`; final instruction-root refresh; final exact-root absence refresh; final containment/porcelain refresh; final deterministic diff/freeze. |
| Reviewer dispatch / acceptance | **NOT READY / NOT RUN** | Blocked before final freeze. |

## Semantic hashes

Pre-full-suite semantic freeze (the explicit suite basis):

- Deterministic R20/status/TM binary-diff concatenation: 27,465 bytes; SHA-256 `c4781102cff88dd7ca9216cda604400c70bf895ec9a451b0d86825831d34fc25`.
- R20: `f21831c0ac7e5827dcaf610049dad8e0af2e64b476ae4126ae827380ae922161`.
- `_STATUS.md`: `d7e3846cfdc105d06145751f2355cef7fb0447c855fd0086f79d1d1bf34862e4`.
- TM candidate: `45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8`.

Current shared-candidate hashes captured at terminal freeze, after recording suite results and the pre-review shell-safety repair, with no further shared-file write:

- R20: `bc9d39ba804c59a4a1cc7b1b5de39785288e2fe6a8539ca2e3936c99c118303c`.
- `_STATUS.md`: `6c864ceebd8769c47519a3fba338dc2932667efa6ad590bc1fd25b62851feb48`.
- TM candidate: `45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8`.
- A new deterministic combined-diff hash was intentionally not generated after the terminal failure.

Frozen source/test/package inputs remained:

```text
17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc  package.json
717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458  package-lock.json
e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457  scripts/verify-electron-dist.mjs
08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db  scripts/pack-electron-with-supply.mjs
f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306  scripts/run-packaged-launchagent-login-proof.mjs
6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18  src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531  exact fixture
39dfaa0e5acb70bf10bd0d58320bdf20f9d98ed7cc835f25123124201177dff7  electron/runtime-host.ts
78c64ce5b676c40c4cc498afe279e2d3b58f46c8f6f23842f342e730c50d40b8  runtime-host socket-path test
```

## Dirty inventory, containment, and index

Last completed containment checks before the terminal predicate:

- Scoped frontend tracked/untracked porcelain: empty; only ignored generated build outputs present.
- `git diff --stat cb008dc5d6aa9b249639c91f3453a18609530d0f..HEAD -- projects/chirality-app-dev/frontend`: empty.
- Index: empty (`git diff --cached --name-only` produced no paths) at the last completed index gate; it was not refreshed after the terminal exit.

Exact project-scoped dirty inventory captured at freeze:

```text
 M .../DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md
 M .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/CHAT_TRANSCRIPTION.md
 M .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/RUNTIME_EVENTS.jsonl
?? .../DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R20_LOGIN_PROOF_R19_FAILURE_CLEANUP_PARSER_REPAIR_AND_R20_STAGING_2026-08-23.md
?? .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/AMENDMENT_02_PHASE_B_AUTHORIZATION.md
?? .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/ORCHESTRATION_PLAN_V4.md
?? .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/TM_CANDIDATE_TARGET_OS_HOST_OUTPUT_FIXTURES.md
?? .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/WORK_GRAPH_V4.json
?? .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PHASEB-EXECUTE-01.md
?? .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PHASEB-REVIEW-01.md
?? .../APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/{ACTIVATION.md,BASIS_AND_PREBUILD.md,DISPOSABLE_PRECHECK.md,PRE_FULL_SUITE_FREEZE.md,SUPPLY_AND_PACKAGE_CHECKS.md,app_hold.exit-status.txt,app_hold.log,corpus.exit-status.txt,corpus.log,desktop-pack.exit-status.txt,desktop-pack.full.log,disposable-daemon.stderr.log,disposable-daemon.stdout.log,disposable-precheck.exit-status.txt,disposable-precheck.log,disposable-precheck.sh,electron-supply-chain.exit-status.txt,electron-supply-chain.log,focused.exit-status.txt,focused.log,npm-test.local-socket-cure.exit-status.txt,npm-test.local-socket-cure.log,npm-test.sandboxed.exit-status.txt,npm-test.sandboxed.log,package_verify.exit-status.txt,package_verify.log,pytest.exit-status.txt,pytest.log,receipt.exit-status.txt,receipt.log,self_check.exit-status.txt,self_check.log,typecheck.exit-status.txt,typecheck.log}
```

`RETURN.md` itself is the sole additional path created by this terminal freeze. Manager-authored CHAT/runtime/amendment/plan/graph/brief paths were not modified by this executor. No file was staged or committed.

## Exact R20 destinations and state

- Label: `com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933`
- Service: `gui/501/com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933`
- Private root: `/private/tmp/ch-r18-91499728-51dd`
- Plist: `/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933.plist`
- Public evidence: `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-public-evidence`
- Failed evidence: `/Users/ryan/Desktop/chirality-login-proof-owner-macos26-r20-bf0d2e6c-f705-446e-8e4f-a073c6645933-failed-evidence`
- At the last completed live Step-0 audit, all four filesystem destinations were absent/non-symlink and the exact service was absent with exit `113`. The proof block was not executed.

## Narrow owner disposition options

Either option requires explicit owner/manager authorization and a new bounded continuation; this executor did neither:

1. Preserve `desktop-pack.full.log` byte-for-byte and its raw SHA-256, exclude immutable raw `*.log` evidence from the semantic-candidate whitespace predicate, then run only the checks that were not reached. This is the narrower evidence-preserving option.
2. Preserve the raw log and raw SHA-256, additionally create a clearly named normalized derivative that removes only the three documented CR-progress trailing spaces (expected derivative SHA-256 `323378988774f6174b94a1cbeb90dc09d06d407a2faf6f1da3d955a9630076d6`), and direct candidate whitespace validation to semantic files plus the derivative rather than the raw capture.

The one-shot supply verifier, one-shot package build, exact-once disposable precheck, and two full-suite attempts must not be repeated merely to resolve this validation-scope defect. The continuation must begin from the preserved hashes and explicitly record the owner's chosen raw-log policy.
