# Agent 2 remediation return — A2-PKG09-MACOS26-REMEDIATE-01

- Result: `PASS`
- RunID: `APPDEV_LOGIN_PROOF_MACOS26_REPAIR_2026-08-22`
- ParentInstanceID: `WI-PKG09-MACOS26-LOGIN-REPAIR-01`
- ChildInstanceID: `A2-PKG09-MACOS26-REMEDIATE-01`
- Repair cycle: `1`
- Accepted implementation basis / current HEAD:
  `9bfe529352afb8bb43a8f0c6afd9a4b3945453b1`
- Accepted review finding: `F-01` from `review/REVIEW.md` SHA-256
  `adc3de73ed0ab46043ad599c9dbac34078c2982a7db9b9c8a7a42ce5a30b64d8`
- Branch: `codex/app-login-proof-macos26-repair`
- Package / deliverable: `PKG-09` / `DEL-09-04`

## Outcome

F-01 is repaired in the authorized focused-test path. Twelve direct cases now
cover every previously missing fail-closed class:

1. non-Darwin platform;
2. root/zero process UID;
3. process UID versus current-account UID mismatch;
4. current-account usernames `root`, `loginwindow`, and `_mbsetupuser`;
5. `_mbsetupuser` console ownership, distinct from the retained direct
   `loginwindow` console-owner case;
6. signaled `/usr/bin/stat`;
7. signaled top-level `launchctl print gui/<uid>`;
8. trailing output after the top-level domain's closing brace;
9. an unclosed top-level brace; and
10. unclosed security-context/top-level braces.

The focused suite increased from 34 to 46 cases. A shared negative-preflight
assertion proves for every negative table entry that the call throws and
returns no PASS result, never executes the packaged app/install route, never
issues a service-level or mutating `launchctl` operation, and never creates the
session root. Existing tests and product behavior remain preserved.

No product source changed in this remediation. The new direct tests exposed no
product defect, so the stop condition for product-source expansion did not
fire.

## Commands and results

| Command / check | Result |
|---|---|
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | PASS |
| `npx vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | PASS — 46/46 |
| `npm run typecheck` | PASS |
| sandboxed `npm test` diagnostic | expected environment failure — 21 local loopback/Unix-socket fixture failures; 1,224 passed / 4 skipped |
| unrestricted exact rerun of `npm test` | PASS — 152 files passed / 1 skipped; 1,245 tests passed / 4 skipped |
| optionless live `preflight` | PASS on macOS 26.6.2 build 25G83; calibrated read-only/no-root fields retained |
| proposed-root absence before and after live preflight | PASS |
| `python3 execution/_Scripts/app_hold.py scan --require-register-match` | PASS — exit 0 at the 53-contract baseline |
| `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | PASS — exit 0 at the existing baseline |
| forbidden product-source scan | PASS — no `osascript`, CoreGraphics, or `CGSessionCopyCurrentDictionary` |
| `git diff --check -- projects/chirality-app-dev` | PASS |
| exact containment | PASS — remediation writes are only the four declared paths below |
| staged index | empty |

The sandboxed full-suite result retains the accepted
`ENVIRONMENT_SANDBOX_SOCKET_DENIAL` classification. The exact suite passed
with local socket permission and no intervening source or test change.

The live preflight executed only the optionless product route. Its public
result retained schema
`chirality-packaged-launchagent-login-proof-preflight/v1`, status `PASS`, mode
`READ_ONLY_PREFLIGHT`, `serviceOrJobInspection: false`,
`mutationsPerformed: false`, and `sessionRootCreated: false`. The proposed
future root remained absent before and after:

```text
/private/tmp/chirality-login-proof-owner-macos26-00bc8f1a-0045-48a2-970f-be120cf7fc20
```

## Remediation writes and hashes

| Path | SHA-256 |
|---|---|
| `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `76d3d2a36ee47f327bbecb09c1fc2832480086855a116477988eccb0a4487631` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/R15_MACOS26_LOGIN_IDENTITY_REPAIR_2026-08-22.md` | `0ffc3995b6ad3e599c62c5dd7e05d4f29de66a0492da9e8f8bbb009e496c03e7` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md` | `f4f020921f3ef6fdc9fd145436cbfbcd562672def9748ce58aadf69c81a03fce` |
| this `remediation-01/RETURN.md` | self-referential hash intentionally omitted |

The product script remains byte-identical to the frozen implementation at
SHA-256
`64031e7aab464d1178f2e94d3a1451444594b050318181aafd4d2805bbb8aa98`.
The updated source/test numstat is `204/36` plus `313/10`; only the focused test
portion changed during remediation. R15 and `_STATUS.md` changed only stale
test count, test hash, test numstat, and the directly supported coverage claim.

## Containment and fences

This remediator wrote only the focused test, R15, `_STATUS.md`, and this unique
return. R14, the product source, the original executor return, the original
review, all shared loop/receipt/completion surfaces, and all other paths were
read-only. All live dirty paths remain under `projects/chirality-app-dev/`; the
index is empty.

No build/package, prepare, capture, logout/login, GUI, proof execution,
LaunchAgents directory, service/job-level query, operator service/launcher,
bootstrap, kickstart, network/provider, staging, commit, push, PR, publication,
signing, notarization, distribution, release-readiness, issuance, or reliance
action occurred.

## Derivative status, blockers, and rerun requirements

R15, `_STATUS.md`, and this return are derivative validation evidence tied to
the accepted implementation basis and current dirty repair bytes. They do not
replace source truth or establish packaged-app identity, login auto-start
proof, lifecycle acceptance, or release status.

Blockers: none for remediation fan-in. A fresh full evidence-only review is
still mandatory after manager acceptance.

If source or tests change, rerun syntax, focused Vitest, full `npm test`,
typecheck, live optionless preflight with proposed-root absence before/after,
APP-HOLD, practitioner self-check, the forbidden-source scan, hashes, exact
containment, and `git diff --check`. After the reviewed repair is committed, a
separately authorized node must rebuild the unsigned app and bind the exact
revision/app before any new executable owner procedure is staged.
