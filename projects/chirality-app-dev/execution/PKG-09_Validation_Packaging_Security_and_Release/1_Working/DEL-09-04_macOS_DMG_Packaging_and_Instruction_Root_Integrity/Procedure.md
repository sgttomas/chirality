# Procedure: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

## Purpose

Define the operational steps to produce the macOS arm64 unsigned DMG and assemble evidence that instruction-root resources and SDK subprocess packaging posture are valid for the packaged app.

## Prerequisites

- ResponsibleParty: TBD.
- Work from `frontend/` for local validation and packaging commands.
- Node.js `>=20` is available.
- Dependencies have been installed with `npm ci`.
- Required instruction-root assets are present or missing assets are tracked as blockers.
- Dependency state: `Dependencies.csv` v3.1 currently contains 9 ACTIVE rows; six rows remain `SatisfactionStatus=TBD`, so dependency closure remains open until accepted evidence resolves them.
- Evidence bundle custody: ResponsibleParty remains TBD; until assigned, route release evidence bundle ownership through the package owner or human-appointed release reviewer.
- Source warning: `_REFERENCES.md` marks `docs/PRD.md` as `HASH_MISMATCH`; assignment says to treat this as warning only for this run.

## Steps

1. Confirm release target remains macOS 15+ Apple Silicon (`arm64`) unsigned/unnotarized local-builder DMG.
2. From `frontend/`, run required pre-packaging checks or confirm accepted evidence already exists. Non-run evidence is acceptable only when it identifies the command, source run or artifact, timestamp/version, pass verdict, and any blockers:
   - `npm run test`
   - `npm run typecheck`
   - `npm run harness:validate:premerge`
   - `npm run instruction-root:integrity`
3. If `instruction-root:integrity` reports missing required assets, stop packaging-evidence acceptance and record the missing assets as P0 blockers.
4. From `frontend/`, run `npm run desktop:dist`.
5. Confirm expected packaging outputs:
   - `frontend/dist/Chirality-0.1.0-arm64.dmg`
   - `frontend/dist/mac-arm64/Chirality.app`
   - `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`
6. Inspect the packaged app for macOS release posture:
   - binary is `arm64`;
   - `LSMinimumSystemVersion` is `15.0.0` or later;
   - signing posture is unsigned/adhoc as scoped.
7. Inspect packaged resources for required instruction-root assets.
8. Run or review the SDK subprocess packaging probe:
   - record the probe command, package path, expected result, observed result, and evidence path;
   - verify the SDK subprocess/bundled binary can be found from package layout;
   - verify it is not trapped inside `app.asar` without execution access;
   - verify execution does not require secret leakage or broader network policy.
9. Confirm packaged app preserves packaging-relevant runtime guardrails:
   - working-root selector is available;
   - current shipped Anthropic network guardrails remain in force;
   - `TBD`: human/source ruling must decide whether SDK-backed turn start after R1 blocks DEL-09-04 closure or is deferred to a broader packaged-app validation workflow.
10. Record all command outputs, artifact paths, summary JSON, probe output, checksums or deterministic artifact identifiers, and residual blockers in the integrity/package evidence bundle.

## Verification

| Check | Pass Criteria | Requirement Link |
|---|---|---|
| Local checks | Required commands exit zero or accepted evidence explains non-run state. | DEL-09-04-REQ-002, DEL-09-04-REQ-006 |
| DMG artifact | `frontend/dist/Chirality-0.1.0-arm64.dmg` exists after `desktop:dist`. | DEL-09-04-REQ-003 |
| App bundle artifact | `frontend/dist/mac-arm64/Chirality.app` exists after `desktop:dist`. | DEL-09-04-REQ-004 |
| Integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` exists and states a pass verdict, or all failed/missing assets are enumerated as blockers. | DEL-09-04-REQ-005, DEL-09-04-REQ-007 |
| macOS target | Binary architecture is arm64 and minimum macOS target is `15.0.0` or later. | DEL-09-04-REQ-001 |
| Signing posture | Codesign evidence matches unsigned/adhoc local-builder scope. | DEL-09-04-REQ-001 |
| SDK subprocess | Packaged SDK subprocess/binary probe records command, package path, expected result, observed result, and shows the binary is locatable and executable from app bundle/package layout. | DEL-09-04-REQ-008 |
| Network guardrails | Packaged validation preserves current shipped Anthropic network policy. | DEL-09-04-REQ-009 |

## Records

Required records:

| Record | Required content |
|---|---|
| Pre-packaging command transcript | Command, cwd, timestamp/version, exit status, and accepted non-run evidence basis if substituted. |
| `desktop:dist` evidence | Command transcript or build run record plus output paths. |
| DMG artifact identity | `frontend/dist/Chirality-0.1.0-arm64.dmg` listing plus checksum or deterministic artifact identifier. |
| App bundle artifact identity | `frontend/dist/mac-arm64/Chirality.app` listing and inspected release posture. |
| Instruction-root integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` with pass verdict or blocker list. |
| SDK subprocess packaging probe | Probe command, package path, expected result, observed result, output path, and blocker state if failed. |
| Manual package verification notes | Architecture, minimum OS, signing posture, resource inclusion, working-root selector, network policy, and SDK packaged execution scope. |
| Evidence bundle custody | ResponsibleParty or routing placeholder; currently `TBD` until human assignment. |
| Blocker list | All `TBD` or failed items, including missing instruction-root assets, dependency rows with `SatisfactionStatus=TBD`, PRD hash mismatch disposition, and unresolved SDK-backed turn-start scope. |
