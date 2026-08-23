# A2-PKG09-R19-REVIEW-01 fresh evidence review

Status: `BLOCKED_REPAIR_CYCLE_1_REQUIRED`

## Review boundary

This was a genuinely fresh, evidence-only Agent 2 review of the frozen R19
candidate. I made no change to reviewed bytes and did not run a full suite,
targeted reproduction, build, package, empirical daemon, network/provider,
preflight, proof, GUI, LaunchAgent, or lifecycle command. Review inspection
was limited to source and Git history, hashes, package metadata and archive
bytes, JSON parsing, shell syntax, whitespace, containment, exact-path
absence, diff, and index checks permitted by the sealed brief.

Frozen inputs matched exactly:

- executor `RETURN.md` SHA-256:
  `67c0b63e1ec0412b7eede13e6cbcc023bc77a32b7fc8fabe8ae33f3d1324740e`
- R19 SHA-256:
  `2ad62425782250c473f388102736d5353f83ce13ece9baed82ea17776ea19cb9`
- `_STATUS.md` SHA-256:
  `852bb42d8d593f9f34beec1b834b37b2a223669718a2f29112a985a69eadaf8a`

## Required matrix

| Gate | Result | Evidence and disposition |
|---|---|---|
| basis and Git posture | PASS | HEAD is exact `d6861ae8251e2a81078577d4496e949735ff199d`; frontend tree is exact `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`; branch is `codex/app-login-proof-r19-staging`; `origin/main` is newer at `8635e40995b05f494ae35c6083dabdd50068bb52`; no merge/rebase/cherry-pick/revert head exists; no unauthorized sync occurred; frontend diff-stat from the build revision and scoped frontend porcelain are empty; index is empty. |
| containment and inventory | PASS | Before this review file, porcelain contained 25 file-level entries: one tracked `_STATUS.md` modification and 24 untracked App files, all under `projects/chirality-app-dev/`. No staged path exists. |
| supply and single offline package | PASS, subject to Finding R19-REV-01 | Retained evidence records one successful `npm run electron:supply-chain` and one successful ordinary-network-denied `npm run desktop:pack`, custom `electronDist`, no retry, no download indicator, dependency-boundary PASS, and instruction-root pass. The pack exit file is exact `0\n`. The durable pack log is not complete; see Finding R19-REV-01. |
| package identity | PASS | Read-only inspection confirms `com.chirality.app`, versions `2.0.0`/`2.0.0`, minimum macOS `15.0.0`, main mode `0755`, Mach-O arm64, main SHA-256 `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`, runtime CLI mode `0755`, and CLI SHA-256 `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`. Codesign display is ad-hoc/linker-signed with no team, sealed resources, or internal requirements. |
| instruction-root and packaged R17 guard | PASS | Summary/manifest hashes are `1ff8adf9bccc1bd108a4321d4637b8d31b0f443f5fd1f1a8f75e120e54bc9c84` / `bd2e1e825f570bc8e77ad3b0e0a3093f12f9ac1005ef15f22bdfa3abc6dd340b`; both name exact build revision and the summary passes 43 current-byte comparisons. Read-only `app.asar` inspection confirms packaged `dist-electron/main.js` is 1,379,498 bytes at SHA-256 `64b99b9a0c661dc53fe71aa6fed184a52220d8c61b4cc41989149c8a672b2947`, with one `103` declaration and the single macOS `Buffer.byteLength(socketPath, "utf8")` guard and measured/maximum diagnostic. |
| empirical daemon | PASS | Retained frozen script/logs support exactly one direct packaged `--runtime-daemon` attempt, exact three environment values, PID 16906 and exact executable/argv identity, Unix socket at the exact 67-byte path, authenticated packaged-CLI `project list --json` result `[]`, SIGTERM through `runtime-daemon-signal`, exit 0, and bounded cleanup. Daemon stdout/stderr hashes match `ee065b0a0739f74358e1e6d168c4cdc14a28481bdb629bcc6bfa0140b9a648d1` / `845c90a6010b99eebd1c956d4389cc07ba46e6e4759226ce89209c92cd5869cc`. The exact root, proof plist, and public destination remain absent. No LaunchAgent/default-operator or external-network act is evidenced. |
| staged owner procedure | PASS | The seven procedure blocks preserve exact R19 app/hash/revision/root/label/plist/service/public values, fresh-tab repo cwd and `set -euo pipefail`, empty scoped frontend diff rather than HEAD equality, exact 67/103 byte checks, exact launchctl 113/two-line absence text, optionless read-only preflight with unchanged absences, prepare and `PREPARED`/`proofClaimed:false`/revision checks, owner logout/login boundary, capture, PASS/revision checks, exactly three public files with 0700/0600 modes and hashes, private-state exclusion, and the exact hash-printing owner handoff. All shell fences parse together under `/bin/zsh -n`; retained extraction records 7/7. The later-docs-only HEAD reasoning is sound. No block was executed. |
| sandbox diagnostic | NOT PASS, correctly retained | Exact diagnostic is exit 1 at 22 failed / 1,245 passed / 4 skipped. Twenty-one failures are the established TCP/Unix `listen EPERM` set and remain `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`. The separate synthetic-PID-4242 SIGKILL-absence assertion is not assigned that classification. |
| local-socket cure | NOT PASS, accepted as classified evidence only | Exactly one retained cure is exit 1 at 1 failed / 1,266 passed / 4 skipped. It cleared all 21 socket denials and the synthetic-PID assertion. It must not be represented as a passing suite. The sole remaining Pi/oMLX failure is classified below. No rerun is required by this review. |
| semantic identity | PASS | Current hashes match every frozen source/test/package hash in `PRE_CURE_FREEZE.md` and `POST_CURE_IDENTITY.md`. The relevant Pi/oMLX test, adapter, and fake-loopback sources have no diff between the R18 basis `f59105d...` and R19 build revision. The frozen pre/post 21,477-byte semantic candidate diff is consistently recorded at SHA-256 `9b1479182347b34f5624e852ab4a0b2070cc11f5457b8f390e73095523a69e44`; later R19/status blocker calibration explains the current 23,243-byte semantic diff at SHA-256 `56eec3ee9efb6411c392629b3c33e9f88da8081c23f4420ac7e1a44ca2440b77`. |
| retained/held validation | CALIBRATED | JSON and JSONL parse, `git diff --check`, new-file no-index whitespace, App containment, exact absences, and empty index pass in this review. The executor correctly held focused tests, typecheck, live preflight, APP-HOLD, self-check, practitioner pytest, receipt validator, and repeat package/integrity checks after the cure failure. This review does not upgrade them. Future PR-CI `full_test` and typecheck are not yet observed in R19 evidence. |
| claim and lifecycle fences | BLOCKED on Finding R19-REV-02 | DEL-09-04 remains `IN_PROGRESS` and unproved; no R19 procedure/proof, Receipt 190, Git integration, signing, notarization, deployment, distribution, release-readiness, issuance, or reliance act is evidenced. R19's top-level `Result` nevertheless says `PASS` while its validation section and executor return correctly hold the tranche. |

## Pi/oMLX 504 classification

Classification: `PRE_EXISTING_TEST_HARNESS_TIMING_FLAKE_ENVIRONMENT_LIMITATION`.
It is not supported as an R19 product/source defect.

The failing case uses a local scripted HTTP loopback with two immediately
scripted SSE responses. Its test-only adapter factory overrides the production
default provider-stream timeout from 120,000 ms to 200 ms. Git commit
`4575c73f7abf776a8cb95a3dab9db22a6a1125b4` introduced that 200 ms value
explicitly as suite-speed tuning, reducing it from 750 ms; the commit recorded
the full suite passing. The same relevant test/adapter/loopback sources are
unchanged between the R18 basis and R19, and the retained R18 exact
local-socket-permitted full suite passed 1,267 / 4 with those bytes. In R19,
the test took 1,187 ms and the 200 ms test deadline fired before the expected
`tool:result`. The product correctly failed closed as
`PROVIDER_PROTOCOL_FAILURE`, status 504, rather than producing a false
success. This evidence supports scheduler/full-suite contention against an
intentionally short test-only timeout.

The R19 cure remains `NOT PASS`; this classification does not infer or rename
it as PASS. It permits retained-evidence acceptance without another run or a
product change. A later test-maintenance item may separate the intentional
hung-stream deadline from success-path pacing, but that is outside R19 and is
not a product blocker. Independent PR-CI remains the future confirmation of
record.

## Actionable findings

### R19-REV-01 — durable package log is incomplete

`executor/desktop-pack.full.log` line 83 replaces Electron Builder's complete
approximately 8-KiB `duplicate dependency references` value with a prose
suppression marker. Its current SHA-256 is
`a15031aa4ae1dc640075409858eb0c8e7602858fa0f49c5115b0ac244162bec6`.
The frozen brief requires disposition against the owner's complete-full-log
gate. A file named and cited as the full durable log cannot meet that gate
while a command-output field exists only in an ephemeral execution-tool
transcript. The field may be non-gating semantically, but its omission is an
evidence-completeness defect.

Narrow repair: without rerunning packaging, recover the exact omitted raw
field byte-for-byte from the retained execution-tool transcript and restore it
at the suppression marker, preserving every other log byte. Freeze the current
log as the preimage (hash above), the recovered field's byte count/hash, the
restored whole-log byte count/hash, and a prefix/suffix identity proof. Amend
only claims whose evidence pointer/hash or completeness statement changes,
then obtain fresh evidence-only re-review.

### R19-REV-02 — R19 top-level result overclaims terminal PASS

R19 line 7 says `Result: PASS — UNSIGNED OFFLINE PACKAGE REBUILT; OWNER
PROCEDURE STAGED ONLY`, while the same record later calls the failed cure an
unresolved validation blocker and states proportional validation/fresh review
are held. The executor return is correctly
`BLOCKED_VALIDATION_REPAIR_REQUIRED`. A prominent unqualified `PASS` is not
claim-calibrated to that frozen state.

Narrow repair: change only the top-level result (and any directly dependent
summary wording) to distinguish the passed build/package/precheck/procedure
subscope from the blocked tranche validation. Preserve the cure as `NOT PASS`,
preserve the 504 classification above, and make no proof, lifecycle, or
release claim. Re-freeze R19/status/return hashes as applicable and obtain
fresh evidence-only re-review.

## Terminal verdict

`BLOCKED_REPAIR_CYCLE_1_REQUIRED`

The retained Pi/oMLX 504 is a supported pre-existing test-harness timing
flake/environment limitation and does not require a rerun or product repair.
The tranche cannot receive `VALIDATED_PASS` until the exact durable package log
is restored from retained bytes and R19's top-level result is claim-calibrated,
followed by fresh evidence-only re-review. No other actionable product,
procedure, containment, cleanup, proof, or lifecycle finding was identified.
