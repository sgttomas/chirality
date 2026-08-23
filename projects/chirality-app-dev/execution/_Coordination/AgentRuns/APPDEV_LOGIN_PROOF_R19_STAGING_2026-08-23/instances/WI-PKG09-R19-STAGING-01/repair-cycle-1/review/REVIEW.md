# A2-PKG09-R19-REVIEW-R1-01 fresh repair-cycle review

Status: `VALIDATED_PASS_WITH_RETAINED_TEST_LIMITATION`

## Review boundary

This was a genuinely fresh, evidence-only Agent 2 review of repair cycle 1
and the complete R19 candidate. I changed no reviewed byte. I did not run a
test, package, build, empirical precheck, preflight, network/provider, proof,
GUI, LaunchAgent/plist, default-operator, or lifecycle command. Inspection was
limited to retained execution records, hashes, exact byte comparisons, source
and Git diffs/history, JSON/JSONL parsing, whitespace/no-index checks,
containment, inventory, exact-path absence, and index state.

The frozen inputs match exactly:

- repair return SHA-256:
  `4c606d4e7b8798e6998e61e781c377b3e159e6e0868b6fddd684a69cc7d013c0`
- repaired R19 SHA-256:
  `0d0a1246d0473a9e6bc6d5e0dd6e44f3eba64ecfee5c0244603fb4aeab768234`
- unchanged `_STATUS.md` SHA-256:
  `852bb42d8d593f9f34beec1b834b37b2a223669718a2f29112a985a69eadaf8a`
- unchanged original executor return SHA-256:
  `67c0b63e1ec0412b7eede13e6cbcc023bc77a32b7fc8fabe8ae33f3d1324740e`
- immutable original review SHA-256:
  `253ae21c59f5de81e80a67541a38df1e881c3ef6d2a3973f21d4c8b06ed19712`

## Repair verification

| Check | Result | Exact observation |
|---|---|---|
| deterministic preimage | PASS | The gzip is 2,127 bytes at `b9ba318019fbd8bb6565c6c463df6cddd823ab04a16e0f10e25bd5e86c287c52`, has zero mtime and no-name flags, and a fresh `gzip -n` stream of its decompressed bytes has that same hash. It decompresses to the exact 6,737-byte old log at `a15031aa4ae1dc640075409858eb0c8e7602858fa0f49c5115b0ac244162bec6`. |
| original transcript field | PASS | The retained Codex execution event `exec-df1a0a3b-c9af-4dc0-b3fa-b3836070813a` is unique at `2026-08-23T06:21:41.991Z`; it records `/bin/zsh -lc npm run desktop:pack`, the exact frontend cwd, exit 0, 15,638 stdout bytes, and empty stderr. Its unique raw dependency field is 9,588 bytes at `0f1611f07c7a52900d89bd60f8702986555435a632305542e73b400f29e155b3`, including the terminal LF. |
| replacement containment | PASS | The old marker begins at offset 4,693 and is exactly 227 bytes. The 4,693-byte prefix is unchanged at `87e9bf6a4a5030db4064423b61452c527702c0db40268566ffaf016e3927dea4`; the 1,817-byte suffix is unchanged at `88b7ba67b0b63a7224c90c42c5d6ba4567b60bd0c397ada84bd4578cb82f612a`. No byte outside the replacement changed. |
| restored log | PASS | The restored log is 16,098 bytes at `2c0229474bad89dce1ced7e1303a2cd5b5bff0d0df3624dd5cd850baf1cb2db8`. The transcript field and restored inserted bytes are identical; the field occurs exactly once and the suppression marker occurs zero times. |
| R19 calibration | PASS | The exact top result is `SUBSCOPE PASS / TRANCHE VALIDATION NOT PASS — UNSIGNED OFFLINE PACKAGE, EMPIRICAL PRECHECK, AND OWNER-PROCEDURE STAGING PASSED; RETAINED FULL-SUITE CURE REMAINS NON-PASS`. The complete-log size/hash/field pointers are exact, dependent wording retains the cure as `NOT PASS`, and no proof, product, lifecycle, release, or reliance overclaim remains. |

The local session inventory contains exactly one R19 `npm run desktop:pack`
execution and exactly two R19 `npm test` executions: the sandbox diagnostic
and the one local-socket cure. No rerun is present.

## Complete retained matrix

| Gate | Result | Evidence and disposition |
|---|---|---|
| basis and Git posture | PASS | HEAD/build revision is exact `d6861ae8251e2a81078577d4496e949735ff199d`; frontend tree is `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`; branch is `codex/app-login-proof-r19-staging`; `origin/main` is newer at `8635e40995b05f494ae35c6083dabdd50068bb52` and was not synchronized. The scoped build-revision-to-HEAD frontend diff and frontend porcelain are empty; operation heads and index are absent. |
| supply, package, and guard | PASS | The restored complete pack log retains Electron Builder 26.15.3, Electron 43.2.0 arm64, the exact custom `electronDist`, zero case-insensitive download/GitHub/release-assets indicator, dependency `PASS`, instruction-root `pass`, exact revision, and exit 0. Main executable is 33,968 bytes/mode 0755 at `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`; packaged CLI is 75,460 bytes/mode 0755 at `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`. Summary/manifest remain `1ff8adf9...` / `bd2e1e82...`, exact revision, 43 files. Retained packaged-main inspection and unchanged 1,379,498-byte `dist-electron/main.js` hash `64b99b9a...` support the single 103-byte UTF-8 fail-closed guard. |
| empirical daemon and cleanup | PASS | Script hash is `47893a0a...`; stdout/stderr hashes remain `ee065b0a...` / `845c90a6...`. Retained evidence supports one exact direct packaged-daemon attempt, three exact environment values, PID/argv identity, the 67-byte Unix socket, authenticated packaged-CLI result `[]`, `runtime-daemon-signal`, exit 0, and bounded cleanup. Exact root, proof plist, and public destination are currently absent/non-links. |
| staged R19 owner procedure | PASS | Retained 7/7 syntax and structural evidence preserves the exact package/revision/root/label/service/public values, scoped frontend-tree gate, 67/103-byte checks, fail-closed absence/service checks, non-claiming prepare state, owner logout/login boundary, capture and exact-revision PASS checks, three-file 0700/0600 preservation, private-state exclusion, and exact hash-bearing owner handoff. No block was executed. |
| semantic identity | PASS | Every frozen package/source/test hash in `PRE_CURE_FREEZE.md` and `POST_CURE_IDENTITY.md` matches current bytes. The Pi/oMLX test, adapter, and fake-loopback sources have no diff from the R18 basis to the R19 build revision. The frozen pre/post 21,477-byte semantic candidate diff remains supported at `9b1479182347b34f5624e852ab4a0b2070cc11f5457b8f390e73095523a69e44`; later documentation-only blocker/repair calibration does not alter frontend bytes. |
| DEL state and fences | PASS | DEL-09-04 remains `IN_PROGRESS` and unproved. R19 is derivative staging evidence only. No R19 proof, Receipt 190, signing, notarization, deployment, distribution, publication, release-readiness, issuance, reliance, or Git-integration act is evidenced. Future PR-CI `full_test` plus typecheck remains unobserved. |
| hygiene and containment | PASS | Before this review file, porcelain contained 35 entries: one tracked `_STATUS.md` modification and 34 untracked files, all App-contained. The run root contained 33 files. Three JSON/JSONL files parse, tracked `git diff --check` is empty, all 34 candidate untracked files have no no-index whitespace finding, and the index is empty. |

## Retained non-PASS validation limitation

The ordinary-sandbox diagnostic remains `NOT PASS`: exit 1 at 22 failed /
1,245 passed / 4 skipped. Twenty-one failures are the established TCP/Unix
`listen EPERM` set classified `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`; the
separate synthetic-PID-4242 SIGKILL-absence assertion is not assigned that
classification.

The sole local-socket cure also remains `NOT PASS`: exit 1 at 1 failed / 1,266
passed / 4 skipped. It cleared all 21 socket denials and the synthetic-PID
failure. The sole retained Pi/oMLX success-case failure took 1,187 ms and
reached the fail-closed `PROVIDER_PROTOCOL_FAILURE` / status 504 path before
the expected `tool:result`. The test uses two immediate scripted loopback SSE
responses with a test-only 200 ms turn timeout. Commit
`4575c73f7abf776a8cb95a3dab9db22a6a1125b4` deliberately reduced that value
from 750 ms for suite pacing and recorded a passing suite; the relevant bytes
are unchanged from the R18 basis, whose retained local-socket run passed.

Classification remains
`PRE_EXISTING_TEST_HARNESS_TIMING_FLAKE_ENVIRONMENT_LIMITATION`. The evidence
does not support an R19 product/source defect, and the product correctly
failed closed instead of returning false success. This classification accepts
the retained evidence; it does not rename either run as PASS and does not
replace the future independent PR-CI confirmation.

## Findings and terminal verdict

No actionable finding remains. `R19-REV-01` and `R19-REV-02` are closed
exactly. The terminal verdict is:

`VALIDATED_PASS_WITH_RETAINED_TEST_LIMITATION`
