# Procedure: DEL-09-05 CI Artifact and Release Verification Workflow

## Purpose

Define the operational workflow to produce, verify, and use the CI artifact and release verification process for `DEL-09-05`.

This procedure is grounded in `docs/PRD.md` Sections 12.2, 12.7, and 12.8; `docs/SPEC.md` Sections 19.1 through 19.4; `docs/PLAN.md` Section 7; and `docs/CONTRACT.md` release/security invariants.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable context and references are present in the deliverable folder. | Present |
| `ResponsibleParty` is assigned. | TBD |
| Declared upstream dependency edges are accepted. | TBD |
| CI provider and workflow path are confirmed. | ASSUMPTION: GitHub Actions; path TBD |
| Local development environment can run commands from `frontend/`. | TBD |
| Required instruction-root assets are present. | To be verified by workflow |
| API keys and secrets are excluded from project files, logs, runtime events, and artifacts. | Required by `docs/CONTRACT.md` K-KEY-1 |
| Network scope remains loopback plus Anthropic API path unless amended. | Required by `docs/CONTRACT.md` K-NET-1 |

## Steps

1. Confirm source and scope.
   - Verify this work remains scoped to `DEL-09-05`.
   - Record the PRD hash mismatch as a source warning if still present.
   - Keep `ResponsibleParty` as `TBD` unless a human assignment exists.

2. Define or review the local command sequence.
   - From `frontend/`, include:

```bash
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run instruction-root:integrity
npm run desktop:dist
```

3. Define or review the CI workflow sequence.
   - Checkout repository.
   - Setup Node.js 20.
   - Install dependencies with `npm ci`.
   - Verify required instruction-root assets are present.
   - Verify preflight validation script presence.
   - Start the Next server.
   - Poll readiness.
   - Run `npm run harness:validate:premerge`.
   - Verify `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`.
   - Upload the summary artifact.

4. Verify stable artifact handling.
   - Confirm the workflow checks for the stable summary artifact path.
   - Confirm artifact upload uses a stable, reviewable name.
   - Mark artifact upload name and retention as `TBD` until source-defined or human-approved.

5. Execute or document packaging verification.
   - Run or require `npm run desktop:dist` from `frontend/`.
   - Confirm expected outputs:
     - `frontend/dist/Chirality-0.1.0-arm64.dmg`
     - `frontend/dist/mac-arm64/Chirality.app`
     - `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`

6. Execute manual macOS DMG release verification.
   - Confirm binary is arm64.
   - Confirm `LSMinimumSystemVersion` is `15.0.0` or later.
   - Confirm signing posture is unsigned/adhoc as scoped.
   - Confirm app resources contain required instruction-root assets.
   - Confirm app launches and working-root selector is available.
   - Confirm Anthropic-only network guardrails remain in force.
   - Confirm SDK-backed harness turn can start in packaged app after R1.
   - Confirm SDK subprocess or bundled binary is executable from package layout and not trapped inside `app.asar` without execution access.
   - Confirm SDK transcript storage/mirroring follows the accepted R1 storage decision.

7. Record release evidence.
   - Record command results and artifact paths.
   - Record pass/fail/TBD for each manual release verification item.
   - Record unresolved `TBD` items and conflicts.
   - Do not record API keys or secret material.

8. Escalate human rulings.
   - Request human assignment for `ResponsibleParty`.
   - Request ruling for CI workflow path, artifact upload name/retention, and release evidence location.
   - Request PRD hash mismatch disposition outside this run if strict source closure is required.

## Verification

| Check | Pass Condition |
|---|---|
| Local command sequence | Procedure or runbook includes all source-defined local commands. |
| CI workflow | Workflow includes all ten PRD Section 12.7 steps. |
| Stable artifact | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` is verified and uploaded. |
| Packaging outputs | DMG, app bundle, and instruction-root integrity summary paths are checked. |
| Manual release checklist | Each macOS DMG item is recorded as pass/fail/TBD. |
| Security | Release evidence contains no API keys or secret material and does not broaden network posture. |
| Professional boundary | Evidence and checklist do not claim automated professional approval, code compliance, external validation, or solver ownership. |

## Records

Required records:

- CI workflow or workflow change.
- Stable artifact upload evidence.
- Local command sequence/runbook.
- Manual release verification checklist with pass/fail/TBD entries.
- Release evidence summary with artifact paths and unresolved rulings.

Record constraints:

- API keys and secret material must not be stored in project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts.
- The PRD hash mismatch must remain visible as a source warning until separately resolved.
- `Dependencies.csv` is not produced by this P1/P2 four-documents run.
