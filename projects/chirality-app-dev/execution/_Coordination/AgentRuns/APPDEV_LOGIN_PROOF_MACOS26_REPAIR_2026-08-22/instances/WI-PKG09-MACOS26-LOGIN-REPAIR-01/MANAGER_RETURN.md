# WORKING_ITEMS manager return — DEL-09-04 macOS 26 repair

- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- InstanceID: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- Branch: `codex/app-login-proof-macos26-repair`
- Accepted basis and current HEAD: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Manager verdict: `VALIDATED_PASS`
- Deliverable state: `IN_PROGRESS`, unproved, uncommitted, and unbuilt

## Outcome

The macOS 26 login-session identity probe is repaired and locally validated.
The implementation removes the JXA/CoreGraphics dependency and uses only
read-only `/dev/console` metadata plus the top-level `launchctl print
gui/<uid>` domain. It fails closed unless the current account, console user,
UID, Aqua login domain, handle, security UID, and `asid` are singular and
consistent. The private capture state holds a salted SHA-256 identity digest,
so a later capture can reject an unchanged login session without publishing a
raw username or session identifier.

The optionless `preflight` route passed live on macOS `26.6.2` (`25G83`). It
reported read-only success without creating a session root or inspecting or
mutating a service/job. No package build, prepare, capture, logout/login, GUI
launch, bootstrap, kickstart, deployment, signing, notarization, publication,
or release-readiness act occurred.

## Failure record and lifecycle boundary

R14 records the owner Terminal prepare failure exactly as:

```text
Current GUI login-session identity is not valid JSON
```

The owner-reported attempt failed before prepare and created no plist or job;
the old proof root was separately confirmed by the manager as an empty mode
`0700` directory. These facts do not establish login proof or acceptance.
R15 records the repaired dirty bytes and local validation only. DEL-09-04
remains `IN_PROGRESS` and unproved, with no lifecycle, proof-acceptance,
deployment, issuance, or publication claim.

## Validation and review

| Check | Result |
|---|---|
| source syntax | PASS |
| focused Vitest | PASS — 46/46 |
| frontend typecheck | PASS |
| unrestricted exact full Vitest rerun | PASS — 1,245 passed / 4 skipped |
| live optionless preflight | PASS on macOS 26.6.2 |
| proposed-root absence before/after/final | PASS |
| APP-HOLD register-match scan | PASS |
| practitioner harness self-check | PASS |
| `git diff --check -- projects/chirality-app-dev` | PASS |
| App-only write containment | PASS |
| Git index | empty |

Fresh review cycle 1 found one consolidated coverage gap, F-01. A distinct
bounded repair session added direct negative tests for non-Darwin, root UID,
process/account UID mismatch, invalid/setup account identities, signaled
inspection commands, trailing output, and incomplete braces. Product source
bytes stayed frozen. A second fresh reviewer reran the complete 14-item matrix
and all 12 added negative classes and returned PASS with no findings.

Evidence identities:

- source SHA-256: `64031e7aab464d1178f2e94d3a1451444594b050318181aafd4d2805bbb8aa98`
- focused-test SHA-256: `76d3d2a36ee47f327bbecb09c1fc2832480086855a116477988eccb0a4487631`
- DEL status SHA-256: `f4f020921f3ef6fdc9fd145436cbfbcd562672def9748ce58aadf69c81a03fce`
- R14 SHA-256: `7a124d6cdbc519c32d573664eca4f8f4d0327fdae2b92a90b0fe8ad16cf08234`
- R15 SHA-256: `0ffc3995b6ad3e599c62c5dd7e05d4f29de66a0492da9e8f8bbb009e496c03e7`
- first review SHA-256: `adc3de73ed0ab46043ad599c9dbac34078c2982a7db9b9c8a7a42ce5a30b64d8`
- remediation return SHA-256: `c0d35ab67934859fd542eac421d84f9a111876de6f3253f47d859be100dbe3c6`
- cycle-2 review SHA-256: `0e14a15a94a10870b430965a6ef32fcfbed93175efa8bf09ce84b2db161b1d8d`

## Proposed future proof identity

These values are proposed only. The root remains nonexistent and the label
was not created, queried, loaded, bootstrapped, or kickstarted:

```text
PROOF_ROOT=/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20
PROOF_LABEL=com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20
```

Exact `PROOF_REVISION` and `PROOF_APP` remain unavailable because this node was
explicitly stopped before Git integration and the unsigned rebuild. No
copy-paste prepare block is emitted on incomplete values.

## Changed paths

Product and deliverable surfaces:

- `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R14_MACOS26_LOGIN_IDENTITY_PREPARE_FAILURE_2026-08-22.md`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R15_MACOS26_LOGIN_IDENTITY_REPAIR_2026-08-22.md`

Manager run root:

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/CHAT_TRANSCRIPTION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/ORCHESTRATION_PLAN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/WORK_GRAPH.json`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/ACTIVATION_AND_WORK_GRAPH.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/RUNTIME_EVENTS.jsonl`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/briefs/A2-PKG09-MACOS26-IMPLEMENT-01.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/briefs/A2-PKG09-MACOS26-REMEDIATE-01.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/briefs/A2-PKG09-MACOS26-REVIEW-01.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/briefs/A2-PKG09-MACOS26-REVIEW-02.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/executor/RETURN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/remediation-01/RETURN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/review/REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/review-cycle-1/REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/MANAGER_RETURN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22/instances/WI-PKG09-MACOS26-LOGIN-REPAIR-01/RUNTIME_SUMMARY.json` (generated at closeout)

No path outside `projects/chirality-app-dev/` changed, and nothing is staged.

## Derivative status and handoff

R14, R15, the test reports, live preflight evidence, reviews, and this return
are derivative validation evidence tied to the accepted basis and dirty repair
bytes; they do not replace source truth.

The next step is manager/owner acceptance and Git integration. Only after an
exact repair commit exists may a separately authorized node rebuild the
unsigned `Chirality.app`, verify it, and stage a new procedure using exact
`PROOF_REVISION` and `PROOF_APP`. Prepare, logout/login, capture, proof
acceptance, and operator deployment remain owner acts.

No blockers remain for Git integration of this bounded repair.
