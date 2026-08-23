# A2-PKG09-R19-EXECUTE-01 return

Status: `BLOCKED_VALIDATION_REPAIR_REQUIRED`

## Basis and containment

- HEAD/build revision: `d6861ae8251e2a81078577d4496e949735ff199d`
- Frontend tree: `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`
- Branch: `codex/app-login-proof-r19-staging`
- `origin/main`: `8635e40995b05f494ae35c6083dabdd50068bb52`
  (newer; not synchronized)
- Final porcelain inventory before RETURN: 23 entries, all under
  `projects/chirality-app-dev/`; one tracked status modification and 22
  untracked candidate/evidence files
- Index: empty
- `git diff --check`: PASS
- Proof root/plist/public destination: absent

## Supply, build, and package

- `npm run electron:supply-chain`: exactly 1; exit 0; exact verified directory
  `/Users/ryan/Library/Caches/chirality/electron-dist`
- `npm run desktop:pack`: exactly 1; ordinary network-denied sandbox; no
  escalation/retry; exit 0
- Exact custom line: `using custom electronDist directory  electronDist=/Users/ryan/Library/Caches/chirality/electron-dist`
- No observed case-insensitive download/GitHub/release-assets indicator
- Embedded dependency boundary: PASS
- Instruction-root: pass, 43 files, exact build revision
- Package: `frontend/dist/mac-arm64/Chirality.app`
- Main SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- Packaged CLI SHA-256:
  `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`
- Package identity/arm64/ad-hoc/no-team posture: PASS with calibrated strict
  codesign diagnostic
- Instruction summary / manifest SHA-256:
  `1ff8adf9bccc1bd108a4321d4637b8d31b0f443f5fd1f1a8f75e120e54bc9c84` /
  `bd2e1e825f570bc8e77ad3b0e0a3093f12f9ac1005ef15f22bdfa3abc6dd340b`
- Packaged main module SHA-256:
  `64b99b9a0c661dc53fe71aa6fed184a52220d8c61b4cc41989149c8a672b2947`;
  exact R17 103-byte guard present

Evidence limitation: `desktop-pack.full.log` freezes the complete gating
phases and result but replaces Electron Builder's single approximately 8-KiB
`duplicate dependency references` console field with an explicit suppression
marker. The complete raw field remains in the execution-tool transcript. No
second pack is authorized. Fresh review must disposition whether this durable
copy is sufficient or requires a manager-owned evidence repair that does not
rerun packaging.

## Empirical precheck and cleanup

- Direct packaged-daemon attempt count: exactly 1
- Local-socket-permitted command:
  `/bin/zsh projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R19_STAGING_2026-08-23/instances/WI-PKG09-R19-STAGING-01/executor/empirical-precheck.sh`
- No external network request/tool
- Exact argv and three required environment values frozen
- PID 16906 matched exact executable/argv
- Exact socket: Unix socket; 67 UTF-8 bytes
- Packaged authenticated CLI `project list --json`: exact `[]`
- Graceful SIGTERM product shutdown: exit 0
- Process/socket/runtime-data/exact root cleanup: PASS
- stdout / stderr SHA-256:
  `ee065b0a0739f74358e1e6d168c4cdc14a28481bdb629bcc6bfa0140b9a648d1` /
  `845c90a6010b99eebd1c956d4389cc07ba46e6e4759226ce89209c92cd5869cc`

## R19 and status

- R19:
  `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R19_OFFLINE_EXACT_MERGE_BUILD_AND_LOGIN_PROOF_STAGING_2026-08-23.md`
- R19 SHA-256: `2ad62425782250c473f388102736d5353f83ce13ece9baed82ea17776ea19cb9`
- `_STATUS.md` SHA-256:
  `852bb42d8d593f9f34beec1b834b37b2a223669718a2f29112a985a69eadaf8a`
- Seven procedure blocks: exact cwd/prefix and `/bin/zsh -n` PASS 7/7
- Scoped later-docs-only HEAD portability: PASS without live Git mutation
- No procedure block executed
- DEL-09-04: `IN_PROGRESS`, unproved

## Full-suite diagnostic and cure

1. Ordinary sandbox exact `npm test`: exactly 1; exit 1; 22 failed / 1,245
   passed / 4 skipped. Twenty-one failures are the established
   `ENVIRONMENT_SANDBOX_SOCKET_DENIAL` set. The separate synthetic PID 4242
   SIGKILL-absence failure is retained without environmental classification.
2. Exact local-socket-permitted `npm test`: exactly 1; exit 1; 1 failed /
   1,266 passed / 4 skipped. The 21 socket failures and synthetic-PID failure
   cleared. The retained failure is Pi/oMLX wire success-case timeout before
   expected `tool:result`, classified by product output as
   `PROVIDER_PROTOCOL_FAILURE` status 504.
3. No full-suite rerun occurred. No source/test/package change occurred.
   Frontend tree and all frozen semantic hashes matched; the pre-amendment
   21,477-byte semantic candidate diff matched exact SHA-256
   `9b1479182347b34f5624e852ab4a0b2070cc11f5457b8f390e73095523a69e44`
   before/after the two runs.

## Held checks and blocker

Because the sole authorized cure is not PASS, the executor failed closed and
did not run further focused tests, typecheck, optionless live preflight,
APP-HOLD scan, repository self-check, practitioner pytest, receipt validator,
or repeat package/integrity checks. Fresh review and PR-CI `full_test` plus
typecheck remain unobserved. No Receipt 190, Git stage/commit/push/PR/merge,
network, GUI, proof, operator, signing, notarization, distribution, or release
act occurred.

Required manager action: inspect the retained 504 evidence and source/history,
then select a bounded repair/re-review cycle. Any targeted reproduction or
additional full-suite execution requires a new parent disposition. The passed
supply, sole offline build, package, packaged guard, empirical health,
cleanup, and staged-procedure evidence remain independently usable but do not
constitute terminal WP-02 acceptance.

## Derivative status

R19, the ignored unsigned package, generated instruction-root artifacts,
empirical logs, and this return are derivative evidence bound to exact source
revision `d6861ae8251e2a81078577d4496e949735ff199d`. They do not replace source
truth and make no proof, lifecycle, release-readiness, or reliance claim.
