# Agent 2 return — A2-PKG09-MACOS26-IMPLEMENT-01

- Result: `PASS`
- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- ParentInstanceID: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- ChildInstanceID: `A2-PKG09-MACOS26-IMPLEMENT-01`
- Accepted basis / current HEAD: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Branch: `codex/app-login-proof-macos26-repair`
- Package / deliverable: `PKG-09` / `DEL-09-04`

## Outcome

The macOS 26.6.2 detector defect is repaired in the authorized live source and
test paths. The JXA/CoreGraphics dependency is removed. The replacement
fail-closes over `/dev/console` owner metadata plus only the top-level GUI login
domain, stores a salted SHA-256 identity digest, preserves the unchanged-session
capture rejection, and provides an optionless strictly read-only `preflight`
route.

R14 records the failed owner attempt with attribution calibrated as
owner-reported. R15 records the exact implementation, validation, live
preflight, macOS build identity, no-mutation boundary, and proposed future
root/label. DEL-09-04 remains `IN_PROGRESS`, unproved, and unbuilt after repair.

## Implementation requirements satisfied

- `/usr/bin/osascript`, JXA, CoreGraphics, and
  `CGSessionCopyCurrentDictionary` are absent from the product script.
- Console owner must be a real non-loginwindow account matching the current
  account; console, process/account, GUI identifier, and security-context UIDs
  must agree.
- Domain type must be exactly `login`, session exactly `Aqua`, and exactly one
  positive safe-integer handle must agree with exactly one security-context
  `asid`.
- Duplicate, ambiguous, malformed, incomplete, mismatched, unsafe-integer,
  command-failure, signaled, and stderr-bearing results fail closed.
- Prepared/captured identities use the same private random salt; public stored
  identity is only SHA-256 and changes with the validated handle/security ID.
- Preflight parses before any session-root resolution, accepts no option, runs
  only `stat` on `/dev/console` and `launchctl print gui/<uid>`, emits no raw
  username or handle, and creates no root or other state.
- Prepare/capture, proof ownership, cleanup, redaction, default protection,
  no-bootstrap, and no-kickstart behavior outside the detector remains intact.

## Commands and results

| Command / check | Result |
|---|---|
| `sw_vers` | PASS — macOS `26.6.2`, build `25G83` |
| `/usr/bin/stat -f 'owner=%Su uid=%u' /dev/console` | PASS — live shape confirmed; raw owner omitted from this record |
| top-level `/bin/launchctl print gui/<uid>` shape inspection | PASS — macOS 26 login-domain shape confirmed; raw handle omitted |
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | PASS |
| `npx vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | PASS — 34/34 |
| `npm run typecheck` | PASS |
| sandboxed `npm test` diagnostic | FAIL — 21 loopback/Unix-socket fixture binds returned sandbox `EPERM`; 1,211 passed / 4 skipped |
| unrestricted final rerun of exact `npm test` | PASS — 152 files passed / 1 skipped; 1,233 tests passed / 4 skipped |
| `node scripts/run-packaged-launchagent-login-proof.mjs preflight` | PASS — schema/mode calibrated below |
| manager read-only `stat` plus one-level `find` of the old R13 proof root | PASS — exists, empty, mode `0700`; no mutation; no plist/job inference |
| `python3 execution/_Scripts/app_hold.py scan --require-register-match` | PASS — exit 0 at existing 53-contract baseline |
| `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | PASS — exit 0 at existing baseline |
| receipt-ledger validator used for declared loop cursor | PASS |
| forbidden-detector source scan | PASS — no `osascript`, CoreGraphics, or `CGSessionCopyCurrentDictionary` |
| `git diff --check -- projects/chirality-app-dev` | PASS |
| proposed-root absence before/after preflight and at final check | PASS |
| staged index | empty |

The full-suite diagnostic failure is classified `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`.
The exact suite passed when granted local socket permission; no source change
occurred between attempts.

## Live preflight

Public preflight fields:

```text
schema=chirality-packaged-launchagent-login-proof-preflight/v1
status=PASS
mode=READ_ONLY_PREFLIGHT
consoleOwnerMetadata=true
topLevelGuiLoginDomain=true
serviceOrJobInspection=false
currentAccountMatchesConsoleOwner=true
uidConsistent=true
loginDomain=true
aquaSession=true
identifierConsistent=true
identitySha256=d3cf84677084d647e3987f101b07cbc583620e7f049f59f22d1a6212145a1cae
mutationsPerformed=false
sessionRootCreated=false
```

The explicit proposed root was absent immediately before, immediately after,
and at final validation:

```text
/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20
```

Proposed label, not created, targeted, or queried:

```text
com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20
```

No raw username or session handle is retained in this return.

## Changed paths and hashes

| Path | SHA-256 |
|---|---|
| `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs` | `64031e7aab464d1178f2e94d3a1451444594b050318181aafd4d2805bbb8aa98` |
| `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `2a056beaef71be5999356c88134bc9517c487560201c13ce87df92028830f73d` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md` | `60935dd8f411cedba895007a6b5dd493e3bcf9fb2b4fb76161117576b3596be0` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R14_MACOS26_LOGIN_IDENTITY_PREPARE_FAILURE_2026-08-22.md` | `7a124d6cdbc519c32d573664eca4f8f4d0327fdae2b92a90b0fe8ad16cf08234` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R15_MACOS26_LOGIN_IDENTITY_REPAIR_2026-08-22.md` | `115738c94d75bf3f15d81e02e95a4e9f33ff68ce3f1448c495bb3784c047dd2b` |
| this `executor/RETURN.md` | self-referential hash intentionally omitted |

Pre-record source/test numstat was `427` insertions and `46` deletions across
exactly the two authorized frontend paths.

## Containment

This executor wrote exactly the two frontend paths, DEL-09-04 `_STATUS.md`,
R14, R15, and this unique `executor/RETURN.md`. The other untracked RunID-root,
manager-instance, and brief files were already present at executor start and
belong to the parent manager. The index is empty. No path outside
`projects/chirality-app-dev/` is changed or staged.

No build/package, GUI launch, prepare, capture, logout/login, LaunchAgents
directory access, service/job-level query, operator service/launcher access,
bootstrap, kickstart, network/provider, staging, commit, push, PR, or shared
loop/receipt/completion write occurred.

## Claim boundary, derivative status, and blockers

R14, R15, this return, and the live preflight are derivative evidence tied to
accepted basis `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1` and the current dirty repair
bytes. They do not replace source truth. This return establishes local repair
validation only. It establishes no packaged-app identity, login auto-start
proof, lifecycle acceptance, release readiness, signing, notarization,
distribution, publication, issuance, or reliance.

Blockers: none for implementation fan-in. Fresh evidence-only review remains
mandatory. Exact `PROOF_REVISION` and `PROOF_APP` remain unavailable until the
reviewed repair is committed and the separately authorized later unsigned
rebuild passes.

## Rerun requirements

- Fresh reviewer: inspect 100% of the source/test/status/R14/R15 diff and this
  evidence, including parser ambiguity, command allowlist, no-mutation
  preflight, capture identity transition, claim calibration, and containment.
- If source or tests change, rerun syntax, focused Vitest, full `npm test`,
  typecheck, live preflight with root absence checks, APP-HOLD, practitioner
  self-check, forbidden-detector scan, and `git diff --check`.
- If only records change, rerun APP-HOLD, practitioner self-check, hashes,
  exact containment, and `git diff --check`.
- Do not use R13's old package/procedure for the repaired proof. After commit,
  a separately authorized node must rebuild the unsigned app and bind a new
  exact proof revision/app before staging any executable owner procedure.
