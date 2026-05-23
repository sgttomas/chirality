# Specification: DEL-09-05 CI Artifact and Release Verification Workflow

## Scope

This deliverable specifies the CI premerge workflow, stable artifact upload behavior, local command sequence, and manual release verification checklist for `DEL-09-05 CI Artifact and Release Verification Workflow`.

In scope:

- Required local validation checks for release-significant changes.
- CI execution of the premerge validation workflow.
- Stable validation summary artifact verification and upload.
- Manual release verification checklist for the current macOS arm64 unsigned DMG release target.
- Documentation of evidence paths and runbook records needed for release review.

Out of scope:

- Feature implementation except test fixtures and packaging glue, per PKG-09 exclusions.
- Section 8/9 test implementation details owned by sibling validation deliverables.
- Network, API key, attachment, and renderer security implementation details owned by `DEL-09-06`.
- Direct creation of `Dependencies.csv` in this run.
- Windows/Linux release packaging unless approved by governed amendment.

## Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-09-05-001 | The local release-significant check sequence MUST include `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, and `npm run instruction-root:integrity` from `frontend/`. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
| REQ-09-05-002 | The packaging check MUST include `npm run desktop:dist`. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
| REQ-09-05-003 | The expected packaging outputs MUST include `frontend/dist/Chirality-0.1.0-arm64.dmg`, `frontend/dist/mac-arm64/Chirality.app`, and `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
| REQ-09-05-004 | The CI workflow MUST checkout the repository, set up Node.js 20, install dependencies with `npm ci`, verify required instruction-root assets, check preflight validation script presence, start the Next server, poll readiness, run `npm run harness:validate:premerge`, verify the stable summary artifact, and upload the summary artifact. | `docs/PRD.md` Section 12.7 |
| REQ-09-05-005 | The stable summary artifact path for validation review MUST be `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` unless a governed source updates that path. | `docs/PRD.md` Section 12.2 and 12.7; `docs/SPEC.md` Section 19.1 |
| REQ-09-05-006 | Manual macOS DMG release verification MUST check arm64 binary posture, `LSMinimumSystemVersion` `15.0.0` or later, unsigned/adhoc signing posture, required instruction-root assets in app resources, working-root selector availability, Anthropic-only network guardrails, packaged SDK-backed turn startup after R1, SDK subprocess execution access outside trapped `app.asar` layout, and accepted SDK transcript storage/mirroring behavior. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
| REQ-09-05-007 | Release validation MUST preserve current release target constraints: macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended. | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |
| REQ-09-05-008 | Release-significant changes MUST pass required local checks before acceptance. | `docs/CONTRACT.md` K-VALIDATE-1 |
| REQ-09-05-009 | Verification records MUST avoid writing API keys or secrets to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1 |
| REQ-09-05-010 | Verification MUST keep outbound network scope limited to explicit product scope: loopback plus Anthropic API path unless governed future scope expands it. | `docs/CONTRACT.md` K-NET-1 |
| REQ-09-05-011 | The release workflow MUST NOT represent Chirality as providing automated professional approval, code compliance, external validation, or solver ownership. | `docs/PRD.md` Section 12.1; `docs/DIRECTIVE.md` professional-boundary sections |
| REQ-09-05-012 | ASSUMPTION: The CI implementation target is a GitHub Actions workflow because `docs/PRD.md` Section 12.7 specifies "The GitHub workflow"; the exact workflow file path is TBD. | `docs/PRD.md` Section 12.7 |

## Standards

| Standard or Governing Source | Applicability |
|---|---|
| `docs/CONTRACT.md` K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1, K-NET-1, K-KEY-1 | Binding release, validation, packaging, network, and secret-handling invariants. |
| `docs/SPEC.md` Sections 19.1 through 19.4 | Physical command sequence, validation surfaces, and manual release verification checklist. |
| `docs/PRD.md` Sections 12.2, 12.7, and 12.8 | Product-level validation plan, CI acceptance, and release verification requirements. |
| `docs/PLAN.md` Section 7 | Roadmap-level command and artifact expectations. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `DEL-09-05` row and scope ledger | Deliverable scope, SOW mapping, and anticipated artifacts. |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-09-05-001 | Run or inspect documented local command sequence from `frontend/`; confirm all four commands are present in the runbook. |
| REQ-09-05-002 | Run or inspect `desktop:dist` packaging step in the local release sequence. |
| REQ-09-05-003 | Confirm expected paths exist after relevant command execution or are explicitly marked as failed with diagnostic notes. |
| REQ-09-05-004 | Review CI workflow definition for all ten PRD Section 12.7 steps. |
| REQ-09-05-005 | Confirm CI checks and upload reference the stable summary artifact path. |
| REQ-09-05-006 | Execute manual release checklist against the built DMG and record pass/fail/TBD for each item. |
| REQ-09-05-007 | Confirm release checklist and packaging metadata do not introduce non-macOS or signed/notarized release claims without amendment. |
| REQ-09-05-008 | Confirm release-significant change gate requires passing local checks. |
| REQ-09-05-009 | Inspect logs/artifacts for secret redaction; do not store API keys in release evidence. |
| REQ-09-05-010 | Confirm packaged-app and CI verification do not broaden network access beyond accepted policy. |
| REQ-09-05-011 | Review runbook and CI/release notes for prohibited professional-approval or external-validation language. |
| REQ-09-05-012 | Human or implementation review confirms exact CI workflow path and artifact naming. |

## Documentation

Required outputs for this deliverable:

- CI workflow or workflow change implementing the premerge sequence.
- Stable artifact upload behavior for the validation summary.
- Local command sequence for release-significant validation.
- Manual release verification checklist/runbook.
- Reviewable evidence of command results, artifact paths, and unresolved `TBD` items.

Documentation notes:

- `docs/PRD.md` is usable in this run only under the dispatch ruling that its hash mismatch is a source warning.
- `ResponsibleParty` remains `TBD` until assigned by a human.
- Any missing implementation-specific detail, including workflow path, artifact name, retention period, release evidence filename, and exact checker script path, remains `TBD`.
