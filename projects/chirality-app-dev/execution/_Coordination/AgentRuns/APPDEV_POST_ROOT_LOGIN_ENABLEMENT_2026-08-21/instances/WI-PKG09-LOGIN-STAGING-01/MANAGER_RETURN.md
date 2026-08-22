# WI-PKG09-LOGIN-STAGING-01 — Manager return

- Verdict: `VALIDATED_PASS`
- Run / node: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21` / `N3`
- Package / deliverable: `PKG-09` / `DEL-09-04`
- Manager: `WORKING_ITEMS`
- Exact build commit and current HEAD:
  `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Deliverable effect: owner procedure staged; DEL-09-04 remains `IN_PROGRESS`
- Current agent blocker: none

## Accepted package and evidence

- App:
  `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- Main executable SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- Build command: exact `npm run desktop:pack` from
  `projects/chirality-app-dev/frontend`; exit `0`.
- Package posture: local unsigned/adhoc `--dir`, arm64, app ID
  `com.chirality.app`, version `2.0.0`, minimum macOS `15.0.0`; no DMG or
  artifact-proof label.
- Packaged dependency boundary: `PASS`.
- Instruction-root summary:
  `projects/chirality-app-dev/frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`,
  SHA-256
  `1028e49effe50da36cef27e7d2e05a5fcf1dc0369bc418f3c05e683c4d61cd82`,
  `status: pass`, `gitSha` equal to the build commit, 43 checked files.
- Instruction-root manifest SHA-256:
  `d3ce01d5172ce1c0dbe23ff091ce74f397bef9b87da887361e615a06b3762d45`.
- HELP_HUMAN source/bundle SHA-256:
  `0285715cbe41ac2c8b7bfd8b6dbd56ad1f0cbb1a970a4f7afed290fc30d1e981`;
  equal size, `match: true`, independent `cmp` PASS.
- Calibrated integrity field retained:
  `sourceCompleteness.status: needs_remediation` for the absent candidate
  `examples` asset while required comparison status remains satisfied.
- Frontend proof: the command below returned no output at manager return, and
  scoped staged/unstaged/porcelain frontend checks were empty:

  ```sh
  git diff --stat 1b375af4f1219ecfc00fc2755854aa7fd4220901..HEAD -- projects/chirality-app-dev/frontend
  ```

## Concrete staged owner values

```text
PROOF_APP=/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app
PROOF_REVISION=1b375af4f1219ecfc00fc2755854aa7fd4220901
PROOF_ROOT=/private/tmp/chirality-login-proof-owner-2a38b15f-07de-48c4-87ef-ccd246bd92fa
PROOF_LABEL=com.chirality.ci.runatload.login.owner.2a38b15f-07de-48c4-87ef-ccd246bd92fa
```

At return, `PROOF_ROOT` and the proof plist are absent and `PROOF_LABEL` is
unloaded (`launchctl print` not found). The complete separate preparation and
post-login capture copy-paste blocks, each with an explicit absolute repository
cwd, are in
`DEL-09-04.../_run_records/R13_POST_ROOT_LOGIN_PROOF_ENABLEMENT_2026-08-21.md`.
Neither block was executed.

## Failure, retry, and review disposition

- Executor attempt 1 compiled successfully and stopped on an operational
  Electron cache miss / sandbox DNS `ENOTFOUND` while Electron Builder sought
  the tracked Electron `43.2.0` arm64 artifact.
- A fresh executor reran the same tracked command with narrow network
  escalation for that locked artifact only. It passed. No `npm install`,
  package/dependency/lockfile change, alternate package command, or provider
  expansion occurred.
- Fresh review 1 found one record-only defect: both owner blocks omitted an
  explicit repository-root cwd. Manager repair cycle 1 added the exact absolute
  `cd` to each separate block.
- Fresh review 2 checked 100% of the node and passed all 12 matrix items with no
  finding. No second repair cycle was required.
- Runtime summary:
  `instances/WI-PKG09-LOGIN-STAGING-01/RUNTIME_SUMMARY.json`, status `PASS`, 15
  events, 6 complete sessions. Native token/context occupancy was unavailable
  and is recorded as the telemetry limitation.

## Containment and hard fences

The operator `com.chirality.runtime` job, its plist, and the CLI launcher were
read-only observed before/after and unchanged. The packaged GUI was not
launched. No proof prepare/capture, bootstrap/kickstart, logout/login, operator
deployment, signing, notarization, distribution, publication, release-readiness,
issuance, reliance, staging, commit, push, PR, receipt, or shared completion
action occurred.

The first later authorized GUI launch may idempotently rewrite the CLI launcher
under the accepted owner baseline. R13 records that as an expected
operator-facing effect, not a park condition and not an action authorized here.

## Persistent changed paths

- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
  - reviewed SHA-256:
    `a165df5d236aba3131f9742579d002f31659dfb6fbf20ae548be62788fe26667`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R13_POST_ROOT_LOGIN_PROOF_ENABLEMENT_2026-08-21.md`
  - reviewed SHA-256:
    `34311c2367bbe09458e6db6d981481c5f276729cd46e27ac4d3365b5c110483b`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21/instances/WI-PKG09-LOGIN-STAGING-01/**`

Generated ignored outputs were regenerated only under
`frontend/{.next,dist-electron,dist-runtime,dist,artifacts}`. No tracked
frontend path changed.

## Handoff, remaining acts, and rerun triggers

Derivative status: R13, executor/review returns, telemetry, app output, and
instruction-root files are derivative evidence bound to the accepted build
commit. They do not replace source truth.

Next owner: HELP_HUMAN may accept Node 3, preserve its build commit and staged
procedure identity in the after-the-fact receipt, and route exact project-only
Git closeout with Node 3 ordered after Nodes 1 and 2. Before final fan-in,
rerun the frontend commit-to-HEAD proof; any frontend change requires a new
package build and fresh identity evidence. Before owner execution, choose new
proof values if the staged root, label, or plist is no longer unique and absent.

Actual preparation, logout/login, capture, proof acceptance, and separate
operator deployment remain owner acts. DEL-09-04 is not closed by this node and
remains `IN_PROGRESS`; no release or issuance claim follows.
