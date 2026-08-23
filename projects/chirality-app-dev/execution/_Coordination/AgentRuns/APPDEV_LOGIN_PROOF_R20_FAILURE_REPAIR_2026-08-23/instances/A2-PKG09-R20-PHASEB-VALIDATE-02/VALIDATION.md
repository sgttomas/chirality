# Phase-B Option 1 deterministic validation

## Verdict

`BLOCKED_TERMINAL_SEMANTIC_WHITESPACE_GATE`

The first continued semantic/new-file whitespace gate failed. Under the sealed terminal rule and Amendment 03's no-repair boundary, all later gates stopped and the fresh reviewer was not launched.

## Gate 1 — raw pack-log identity before

PASS: `desktop-pack.full.log` was 15,852 bytes, mode `0644`, SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`.

## Gate 2 — immutable raw-log exclusion inventory and rationale

PASS: exactly 15 dirty-candidate files ending in `*.log` were inventoried as immutable raw command captures and excluded from semantic whitespace validation. No other file class was excluded.

Rationale: the owner selected Option 1 to preserve raw terminal evidence byte-for-byte. Normalizing whitespace in a raw command capture would destroy its accepted identity. The exemption is therefore narrow, extension- and inventory-bounded, and does not exempt Markdown, JSON, JSONL, shell, or exit-status evidence.

| Bytes | SHA-256 | Excluded immutable raw capture |
|---:|---|---|
| 40,411 | `385349664ef768432fe29b77187ffedfd01a02c1ea4c6a9682b71fed9c7ada14` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/app_hold.log` |
| 671 | `c7a8e08208ccd784d3d548e4b19cd9e4458927b081490d2261ece8383d971dd4` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/corpus.log` |
| 15,852 | `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log` |
| 272 | `c01aed12ccf971f55d555fb76a228eb2bb6172e0cc99f3a2b3490a2d7f6a68d0` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/disposable-daemon.stderr.log` |
| 716 | `d311677a7d83ddca96e4442c8f7dbd8407180c2edb9670a3cf01634c3cd86d85` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/disposable-daemon.stdout.log` |
| 1,242 | `859126564c1046fcad755774b89a307d9b00ef2fb85ad356c5f7d43f85e4766e` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/disposable-precheck.log` |
| 145 | `200522b9040843bbc4eed6d781f1611b2d54f4f9dd5c8f285abe56688c49e422` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/electron-supply-chain.log` |
| 265 | `86763a2fc84d86f34ff2aadd64d6eed010f7a1a15f3e0b378f368965622eed27` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/focused.log` |
| 487 | `ec482e01748d566159a0886fa84f455a10200c06ef0cc0c890177bf9bea1cf8b` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/npm-test.local-socket-cure.log` |
| 9,888 | `b0e940374fc41342b2ca00bf9cee98187320c6559ca1b06321e427ecfc72eda2` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/npm-test.sandboxed.log` |
| 991 | `e3c37d4378ff23fae6cb6f2c0abc77126a9c3f2d3c6fbe067888a4f0c6811034` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/package_verify.log` |
| 422 | `e37aea43f5848789f77a4943204636989b97f3bc292ff832d9fee520d4580c73` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/pytest.log` |
| 165 | `4a31bf4f8309774e5a867718d8c267a06eb51477331b57abe1267abb839e969c` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/receipt.log` |
| 21,501 | `ad40c223a005f0cc4a58348b0a74c876b3d5126e391f6df165e59178f38d991f` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/self_check.log` |
| 137 | `6be4cb0a247e09985e6ce57668de3c06547f0a4e2400e257eae36da4584208a2` | `instances/A2-PKG09-R20-PHASEB-EXECUTE-01/typecheck.log` |

Every relative path above is under `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/`.

## Gate 3 — semantic/new-file whitespace

FAIL.

Method: enumerate exact Git porcelain entries; exclude only inventoried paths ending in `.log`; run `git diff --check -- <path>` for tracked candidates and `git diff --no-index --check -- /dev/null <path>` for untracked candidates. A no-index return of 1 with empty output is the expected changed-file result; any whitespace diagnostic or return greater than 1 is failure.

Exact counts at the gate:

- candidate entries: 52;
- excluded raw logs: 15;
- checked non-raw files: 37;
- tracked-diff files: 5;
- untracked no-index files: 32;
- failed files: 1;
- trailing-whitespace findings: 3.

The exact captured output is rendered below with `<SP>` representing the one final ASCII space byte that cannot be reproduced literally in this semantic evidence file:

```text
candidate_entries=52
excluded_raw_logs=15
checked_non_raw=37
tracked_diff_checked=5
untracked_no_index_checked=32
whitespace_errors=1
ERROR path=projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md rc=3
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md:23: trailing whitespace.
+projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log:16:   Generating static pages (6/24)<SP>
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md:24: trailing whitespace.
+projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log:17:   Generating static pages (12/24)<SP>
projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/RETURN.md:25: trailing whitespace.
+projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-PHASEB-EXECUTE-01/desktop-pack.full.log:18:   Generating static pages (18/24)<SP>
candidate_semantic_newfile_whitespace=FAIL
```

The historical executor `RETURN.md` is not a raw `*.log` capture, so it was correctly included by the approved Option 1 predicate. Its lines 23–25 quote the three raw progress lines with their literal trailing spaces. No byte was changed.

## Terminal stop and unfinished matrix

The following later gates were not run after the mandatory stop:

- change-scope validator;
- formal refreshed index-emptiness gate;
- `git diff --check` aggregate gate;
- instruction-root integrity refresh;
- exact R20 root/plist/public/failed metadata-only absence refresh;
- exact R20 service exit-113/two-line not-found refresh;
- App-only containment and full/scoped porcelain;
- frontend `PROOF_REVISION..HEAD` stat;
- deterministic final candidate inventory and per-file/combined hash freeze;
- fresh overall evidence-only review.

An intake-time Git metadata observation showed the index empty before this gate sequence, but the formal ordered index gate was not reached and is not claimed as PASS.

## Preservation confirmation after terminal stop

The raw pack log remained 15,852 bytes, mode `0644`, SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`. This read-only post-stop confirmation is preservation evidence, not execution of a later validation gate. No normalized derivative exists.

The three shared semantic files remained byte-identical to the accepted handoff:

- R20: `bc9d39ba804c59a4a1cc7b1b5de39785288e2fe6a8539ca2e3936c99c118303c`;
- `_STATUS.md`: `6c864ceebd8769c47519a3fba338dc2932667efa6ad590bc1fd25b62851feb48`;
- TM candidate: `45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8`.

No combined hash was generated because deterministic final freeze was downstream of the failed gate.

## Safe owner disposition options

1. Authorize a narrower Option 1B predicate that exempts only the three exact historical `RETURN.md` quotation lines in addition to the 15 inventoried raw logs, preserving all bytes.
2. Authorize a record-only repair replacing only the three historical trailing spaces in `RETURN.md` with an explicit visible marker such as `<SP>`, while preserving `desktop-pack.full.log` byte-for-byte and rerunning only the still-unreached gates.

Neither option is authorized by Amendment 03. Until a new ruling exists, Phase B remains blocked and review is not ready.
