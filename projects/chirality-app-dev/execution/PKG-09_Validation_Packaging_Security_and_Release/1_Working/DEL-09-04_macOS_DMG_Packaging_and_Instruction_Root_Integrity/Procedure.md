# Procedure: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

## Purpose

Define the operational steps to produce the macOS arm64 unsigned DMG and assemble evidence that instruction-root resources and SDK subprocess packaging posture are valid for the packaged app.

## Prerequisites

- ResponsibleParty: TBD.
- Work from `frontend/` for local validation and packaging commands.
- Node.js `>=20` is available.
- Dependencies have been installed with `npm ci`.
- Required instruction-root assets are present or missing assets are tracked as blockers.
- Declared upstream dependencies: TBD - no accepted dependency edges have been extracted yet.
- Source warning: `_REFERENCES.md` marks `docs/PRD.md` as `HASH_MISMATCH`; assignment says to treat this as warning only for this run.

## Steps

1. Confirm release target remains macOS 15+ Apple Silicon (`arm64`) unsigned/unnotarized local-builder DMG.
2. From `frontend/`, run required pre-packaging checks or confirm accepted evidence already exists:
   - `npm run test`
   - `npm run typecheck`
   - `npm run harness:validate:premerge`
   - `npm run instruction-root:integrity`
3. If `instruction-root:integrity` reports missing required assets, stop release readiness and record the missing assets as P0 blockers.
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
   - verify the SDK subprocess/bundled binary can be found from package layout;
   - verify it is not trapped inside `app.asar` without execution access;
   - verify execution does not require secret leakage or broader network policy.
9. Confirm packaged app preserves release-relevant runtime guardrails:
   - working-root selector is available;
   - Anthropic-only network guardrails remain in force;
   - SDK-backed turn can start in packaged app after R1.
10. Record all command outputs, artifact paths, summary JSON, and residual blockers in the integrity/package evidence bundle.

## Verification

| Check | Pass Criteria | Requirement Link |
|---|---|---|
| Local checks | Required commands exit zero or accepted evidence explains non-run state. | DEL-09-04-REQ-002, DEL-09-04-REQ-006 |
| DMG artifact | `frontend/dist/Chirality-0.1.0-arm64.dmg` exists after `desktop:dist`. | DEL-09-04-REQ-003 |
| App bundle artifact | `frontend/dist/mac-arm64/Chirality.app` exists after `desktop:dist`. | DEL-09-04-REQ-004 |
| Integrity summary | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` exists and indicates required assets are present, or blockers are recorded. | DEL-09-04-REQ-005, DEL-09-04-REQ-007 |
| macOS target | Binary architecture is arm64 and minimum macOS target is `15.0.0` or later. | DEL-09-04-REQ-001 |
| Signing posture | Codesign evidence matches unsigned/adhoc local-builder scope. | DEL-09-04-REQ-001 |
| SDK subprocess | Packaged SDK subprocess/binary is locatable and executable from app bundle/package layout. | DEL-09-04-REQ-008 |
| Network guardrails | Packaged validation preserves Anthropic-only network policy. | DEL-09-04-REQ-009 |

## Records

Required records:

- Command transcript or run record for pre-packaging checks.
- `desktop:dist` command transcript or equivalent build evidence.
- DMG and app bundle artifact listing/checksum.
- Instruction-root integrity `summary.json`.
- SDK subprocess packaging probe output.
- Manual release verification notes for architecture, minimum OS, signing posture, resource inclusion, working-root selector, network policy, and SDK packaged execution.
- Blocker list for `TBD` or failed items, including missing instruction-root assets and PRD hash mismatch disposition.
