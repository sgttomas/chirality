# DEL-09-04 macOS 26 login-identity detector repair

- Date: `2026-08-22`
- Run: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- Accepted basis / current HEAD: `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Branch: `codex/app-login-proof-macos26-repair`
- Result: `IMPLEMENTED AND LOCALLY VALIDATED — UNCOMMITTED, UNBUILT, UNPROVED`
- Deliverable state: `IN_PROGRESS`

This bounded repair replaces only the failed login-session detector and its
tests. It preserves the existing prepare/capture ownership, cleanup,
redaction, default-protection, no-bootstrap, and no-kickstart behavior. No
frontend build or package command ran in this node.

## Repair

The source no longer invokes `osascript`, JXA, CoreGraphics, or
`CGSessionCopyCurrentDictionary`. It now derives the current GUI login identity
only from:

1. `/usr/bin/stat -f %Su:%u /dev/console`; and
2. the top-level `/bin/launchctl print gui/<current-uid>` login domain.

The detector fails closed unless the console owner is a real non-loginwindow
user matching the current account, console/process/account UIDs agree, the
domain identifier and security-context UID agree with that UID, domain type is
exactly `login`, session is exactly `Aqua`, and exactly one positive safe
integer `handle` agrees with exactly one security-context `asid`. Duplicate,
ambiguous, malformed, incomplete, mismatched, command-failure, signal, and any
stderr-bearing result is rejected.

Prepare now stores a salted SHA-256 identity digest; the salt remains in the
private capture state. The digest changes when the validated handle/security
identifier changes, while capture retains the prior fail-closed rejection of
an unchanged login identity.

An optionless `preflight` command was added. Argument parsing returns to this
route before session-root resolution, it refuses every option, and it executes
only the two read-only inspections above. Its public result contains no raw
username or session handle, creates no session root, and exposes no
service/job-level or mutating `launchctl` operation.

## Exact source and test diff

Pre-record source/test diff:

```text
204  36  projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs
313  10  projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts
```

- source SHA-256:
  `64031e7aab464d1178f2e94d3a1451444594b050318181aafd4d2805bbb8aa98`
- focused-test SHA-256:
  `76d3d2a36ee47f327bbecb09c1fc2832480086855a116477988eccb0a4487631`

The 46-case focused suite covers live-shaped output, malformed console/domain
output, wrong console and security UID, non-login and non-Aqua domains,
duplicate/ambiguous identifiers, mismatched handle/`asid`, command failure and
stderr-bearing partial success, preflight option refusal/no mutation/no root,
digest transition, unchanged capture identity, and the existing proof/cleanup
boundaries. It also directly covers non-Darwin and account-identity rejection,
setup/loginwindow console identities, signaled inspection commands, trailing
top-level output, and incomplete top-level/security-context braces. Every
negative preflight case asserts no PASS result, packaged install, service-level
or mutating `launchctl` operation, or session-root creation.

## Live read-only preflight

Host identity observed with `sw_vers`:

```text
ProductName: macOS
ProductVersion: 26.6.2
BuildVersion: 25G83
```

The following command ran from `projects/chirality-app-dev/frontend`:

```sh
node scripts/run-packaged-launchagent-login-proof.mjs preflight
```

It exited `0` with schema
`chirality-packaged-launchagent-login-proof-preflight/v1`, status `PASS`, mode
`READ_ONLY_PREFLIGHT`, all five account/domain consistency booleans true,
`mutationsPerformed: false`, `sessionRootCreated: false`, and
`serviceOrJobInspection: false`. The returned identity was only the salted
SHA-256 digest
`d3cf84677084d647e3987f101b07cbc583620e7f049f59f22d1a6212145a1cae`;
no raw username or session handle was emitted.

The explicitly proposed future proof root was absent immediately before and
after preflight, proving the route created no state:

```text
/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20
```

No LaunchAgent directory, proof/operator service, operator launcher, GUI, or
prepared/capture state was inspected or mutated.

## Checks

| Check | Result |
|---|---|
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | PASS |
| focused Vitest file | PASS — 46/46 |
| `npm run typecheck` | PASS |
| sandboxed `npm test` diagnostic | expected environment failure — 21 tests could not bind loopback/Unix sockets (`EPERM`) |
| unrestricted final rerun of exact `npm test` | PASS — 1,245 passed / 4 skipped |
| live optionless preflight | PASS |
| APP-HOLD `scan --require-register-match` | PASS — exit 0 at the existing baseline |
| practitioner harness `self-check` | PASS — exit 0 at the existing baseline |
| source/test `git diff --check` | PASS |

The sandboxed full-suite failure is not a product result: its exact rerun with
local socket permission passed. No network or provider route was used.

## Staging boundary and handoff

The following unique values are proposed only. The root was confirmed absent;
the label was not created, targeted, or queried:

```text
PROOF_ROOT=/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20
PROOF_LABEL=com.chirality.ci.runatload.login.owner.macos26.00bc8f1a-0045-48a2-970f-be120cf7fc20
```

Exact `PROOF_REVISION` and `PROOF_APP` are unavailable until these repaired
bytes are committed and a later unsigned rebuild passes. Therefore this record
does not emit an executable prepare block. The next bounded step is fresh
review, then Git integration and a separately authorized unsigned rebuild. A
later staged owner procedure must use the resulting exact commit and package.
Prepare, logout/login, capture, proof acceptance, and operator deployment
remain owner acts.

This record and the preflight result are derivative validation evidence tied
to the accepted basis and current dirty repair bytes. They do not replace
source truth or establish release, signing, notarization, distribution,
publication, release-readiness, issuance, or reliance.
