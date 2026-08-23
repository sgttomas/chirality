# Phase-B exact quoted-raw deterministic validation

## Verdict

`BLOCKED_TERMINAL_SEMANTIC_WHITESPACE_REMAINDER`

The first remaining gate failed after applying exactly the authorized exemptions. The ordered matrix stopped. No repair or exemption expansion is authorized.

## Historical evidence identity before

- Historical executor `RETURN.md`: 16,439 bytes; SHA-256 `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399`.
- `desktop-pack.full.log`: 15,852 bytes; mode `0644`; SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`.

## Exact immutable raw-log inventory

Exactly these 15 untracked executor command captures were present, matched the accepted path/byte/hash identities, and were exempt from semantic whitespace validation. No other `*.log` path or file class was exempt.

| Bytes | SHA-256 | Exact exempt path under `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/` |
|---:|---|---|
| 40,411 | `385349664ef768432fe29b77187ffedfd01a02c1ea4c6a9682b71fed9c7ada14` | `app_hold.log` |
| 671 | `c7a8e08208ccd784d3d548e4b19cd9e4458927b081490d2261ece8383d971dd4` | `corpus.log` |
| 15,852 | `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2` | `desktop-pack.full.log` |
| 272 | `c01aed12ccf971f55d555fb76a228eb2bb6172e0cc99f3a2b3490a2d7f6a68d0` | `disposable-daemon.stderr.log` |
| 716 | `d311677a7d83ddca96e4442c8f7dbd8407180c2edb9670a3cf01634c3cd86d85` | `disposable-daemon.stdout.log` |
| 1,242 | `859126564c1046fcad755774b89a307d9b00ef2fb85ad356c5f7d43f85e4766e` | `disposable-precheck.log` |
| 145 | `200522b9040843bbc4eed6d781f1611b2d54f4f9dd5c8f285abe56688c49e422` | `electron-supply-chain.log` |
| 265 | `86763a2fc84d86f34ff2aadd64d6eed010f7a1a15f3e0b378f368965622eed27` | `focused.log` |
| 487 | `ec482e01748d566159a0886fa84f455a10200c06ef0cc0c890177bf9bea1cf8b` | `npm-test.local-socket-cure.log` |
| 9,888 | `b0e940374fc41342b2ca00bf9cee98187320c6559ca1b06321e427ecfc72eda2` | `npm-test.sandboxed.log` |
| 991 | `e3c37d4378ff23fae6cb6f2c0abc77126a9c3f2d3c6fbe067888a4f0c6811034` | `package_verify.log` |
| 422 | `e37aea43f5848789f77a4943204636989b97f3bc292ff832d9fee520d4580c73` | `pytest.log` |
| 165 | `4a31bf4f8309774e5a867718d8c267a06eb51477331b57abe1267abb839e969c` | `receipt.log` |
| 21,501 | `ad40c223a005f0cc4a58348b0a74c876b3d5126e391f6df165e59178f38d991f` | `self_check.log` |
| 137 | `6be4cb0a247e09985e6ce57668de3c06547f0a4e2400e257eae36da4584208a2` | `typecheck.log` |

Rationale: these are the exact immutable raw captures accepted by Amendment 03 and preserved by Amendment 04. Editing or normalizing them would destroy accepted evidence identity.

## Exact historical quotation exemption

The historical executor `RETURN.md` path, size, and hash matched before applying the line exemption. Lines 23, 24, and 25 were each verified to end in exact bytes `0x20 0x0a` and to quote, respectively, `desktop-pack.full.log` lines 16, 17, and 18. `git diff --no-index --check` returned `3` with exactly three diagnostic/following-line pairs, all at those three authorized lines. No other line in that file was exempt.

## Semantic whitespace remainder

**FAIL.** Candidate inventory at the gate comprised 61 files: 5 tracked modifications and 56 untracked files. Exactly 15 raw logs were exempt, leaving 46 non-raw candidates. All 46 were checked with tracked `git diff --check` or untracked `git diff --no-index --check` semantics.

Raw semantic result across non-raw candidates: six findings in four files. Filtering removed only the three authorized historical quotation findings. Three non-exempt findings remained:

```text
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-VALIDATE-02/ACTIVATION.md:13: new blank line at EOF.
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-VALIDATE-02/RETURN.md:111: new blank line at EOF.
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-VALIDATE-02/VALIDATION.md:111: new blank line at EOF.
```

Each file ends with exact tail bytes `0x0a 0x0a`. Their accepted identities remain unchanged:

| Bytes | SHA-256 | File |
|---:|---|---|
| 1,668 | `3c50905cd730925da6ccf9374b8880a09c48b893b2ac2effb5795f2789ec2cb2` | `instances/A2-PKG09-R20-PHASEB-VALIDATE-02/ACTIVATION.md` |
| 5,937 | `9620af4620e4cbaae32ce22e06b2cc214b81149fc67542a2d340278ce322caaf` | `instances/A2-PKG09-R20-PHASEB-VALIDATE-02/RETURN.md` |
| 8,126 | `ef06190377bbba777089b70635575ff3e67642fadbf62eb40f3b161d6cd76440` | `instances/A2-PKG09-R20-PHASEB-VALIDATE-02/VALIDATION.md` |

These files and EOF lines are not among Amendment 04's exact exemptions. No byte was changed.

## Validator-wrapper diagnostics

Two implementation attempts produced no validation verdict and made no repository mutation:

1. A zsh list-splitting wrapper grouped newline-delimited candidate paths incorrectly and stopped before a valid aggregate result.
2. A replacement wrapper stopped immediately because the system Bash is 3.2 and does not support associative arrays.

The final line-by-line method above is the controlling semantic-gate result. Neither diagnostic ran a prior/one-shot product gate or any later validation gate.

## Ordered terminal stop

The following still-unreached gates were not run:

- change-scope validator;
- formal final index refresh as an ordered gate;
- aggregate `git diff --check` under the exemptions;
- instruction-root integrity refresh;
- exact R20 root/plist/public/failed metadata-only absence refresh;
- exact R20 service exit-113/two-line not-found refresh;
- App containment and full/scoped porcelain;
- frontend `PROOF_REVISION..HEAD` stat;
- deterministic final candidate inventory/per-file/combined freeze;
- fresh overall review.

An intake and terminal-preservation observation found the index empty, but the ordered post-scope index gate was not reached and is not claimed as a gate PASS.

## Exact candidate inventory at the failed gate

The 61 candidate files were exactly the following. Brace notation below is an exact enumeration under the stated prefix, not a glob.

Tracked modifications (5):

- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
- run-root `CHAT_TRANSCRIPTION.md`
- run-root `HANDOFF_STATE.md`
- run-root `MANAGER_RETURN.md`
- run-root `RUNTIME_EVENTS.jsonl`

Untracked files (56):

- deliverable `_run_records/R20_LOGIN_PROOF_R19_FAILURE_CLEANUP_PARSER_REPAIR_AND_R20_STAGING_2026-08-23.md`;
- run-root `{AMENDMENT_02_PHASE_B_AUTHORIZATION.md, AMENDMENT_03_OWNER_OPTION1_CONTINUATION.md, AMENDMENT_04_EXACT_QUOTED_RAW_EXEMPTION.md, ORCHESTRATION_PLAN_V4.md, ORCHESTRATION_PLAN_V5.md, ORCHESTRATION_PLAN_V6.md, TM_CANDIDATE_TARGET_OS_HOST_OUTPUT_FIXTURES.md, WORK_GRAPH_V4.json, WORK_GRAPH_V5.json, WORK_GRAPH_V6.json}`;
- run-root `briefs/{A2-PKG09-R20-PHASEB-EXECUTE-01.md, A2-PKG09-R20-PHASEB-REVIEW-01.md, A2-PKG09-R20-PHASEB-REVIEW-02.md, A2-PKG09-R20-PHASEB-REVIEW-03.md, A2-PKG09-R20-PHASEB-VALIDATE-02.md, A2-PKG09-R20-PHASEB-VALIDATE-03.md}`;
- executor instance `{ACTIVATION.md, BASIS_AND_PREBUILD.md, DISPOSABLE_PRECHECK.md, PRE_FULL_SUITE_FREEZE.md, RETURN.md, SUPPLY_AND_PACKAGE_CHECKS.md, app_hold.exit-status.txt, app_hold.log, corpus.exit-status.txt, corpus.log, desktop-pack.exit-status.txt, desktop-pack.full.log, disposable-daemon.stderr.log, disposable-daemon.stdout.log, disposable-precheck.exit-status.txt, disposable-precheck.log, disposable-precheck.sh, electron-supply-chain.exit-status.txt, electron-supply-chain.log, focused.exit-status.txt, focused.log, npm-test.local-socket-cure.exit-status.txt, npm-test.local-socket-cure.log, npm-test.sandboxed.exit-status.txt, npm-test.sandboxed.log, package_verify.exit-status.txt, package_verify.log, pytest.exit-status.txt, pytest.log, receipt.exit-status.txt, receipt.log, self_check.exit-status.txt, self_check.log, typecheck.exit-status.txt, typecheck.log}`;
- prior validator instance `{ACTIVATION.md, RETURN.md, VALIDATION.md}`;
- current validator instance `ACTIVATION.md`.

Here “run-root” is `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/`; “executor instance” and “prior/current validator instance” are their exact directories under that run-root. Current `VALIDATION.md` and `RETURN.md` did not exist at gate time and are terminal evidence, not members of the 61-file gate inventory.

## Narrow owner disposition options

Either option requires new owner authority; neither was exercised:

1. Authorize a record-only repair removing exactly the one extra terminal LF from each of the three prior-validator evidence files, with preimage/postimage hashes recorded, then resume only the still-unreached gate sequence.
2. Authorize a byte-preserving exemption for exactly the final blank line in each of those three path/line identities, in addition to the already accepted 15 logs and executor-return lines 23–25, then resume only the still-unreached gate sequence.

No broader file, EOF, Markdown, or whitespace-class exemption is supportable from this run.

## Preservation after terminal stop

- Historical executor `RETURN.md`: 16,439 bytes; SHA-256 `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399`.
- `desktop-pack.full.log`: 15,852 bytes; mode `0644`; SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`.
- R20: `bc9d39ba804c59a4a1cc7b1b5de39785288e2fe6a8539ca2e3936c99c118303c`.
- `_STATUS.md`: `6c864ceebd8769c47519a3fba338dc2932667efa6ad590bc1fd25b62851feb48`.
- TM candidate: `45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8`.

No shared or historical byte changed. No normalized derivative, prior/one-shot rerun, network, proof, operator/private evidence, Git, Receipt, signing, distribution, deployment, or release action occurred.
