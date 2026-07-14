---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-05
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
project_scope_refs: [SOW-035, SOW-036, SOW-072]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-05

## Purpose and Objective Traceability

This migration candidate defines `DEL-09-05` in service of project scope [SOW-035, SOW-036, SOW-072] and package objectives [OBJ-008].

- **OUT-001** — A CI artifact and release verification workflow, local release-significant command sequence, stable validation artifact handling, manual macOS DMG verification checklist, and auditable requirement-to-evidence records for the current macOS 15+ Apple Silicon unsigned or unnotarized local-builder release target.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-05 CI Artifact and Release Verification Workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"02a648068432032291c9bb8cb3e0cbd94cf0d62bb6bf71e55f53341164fa8e33","target_id":"CLM-001"} -->
#### Datasheet: DEL-09-05 CI Artifact and Release Verification Workflow

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":19,"line_start":5,"source_sha256":"02a648068432032291c9bb8cb3e0cbd94cf0d62bb6bf71e55f53341164fa8e33","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-09-05 |
| DeliverableName | CI Artifact and Release Verification Workflow |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | CI_CD_CHANGE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| Current Scope | Maintain CI premerge workflow, stable artifact upload, local command sequence, and manual release verification checklist. |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":33,"line_start":20,"source_sha256":"02a648068432032291c9bb8cb3e0cbd94cf0d62bb6bf71e55f53341164fa8e33","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Covered scope items | SOW-035 Required local checks; SOW-036 Section 8/9 validation; SOW-072 macOS arm64 unsigned DMG release target | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 8/9, `DEL-09-05` and scope ledger rows |
| Supported objective | OBJ-008 | `_CONTEXT.md` Traceability; decomposition `DEL-09-05` row |
| Anticipated artifacts | CI workflow; stable artifact upload; release verification runbook | `_CONTEXT.md` Anticipated Artifacts; decomposition `DEL-09-05` row |
| Local check command sequence | `npm run test`; `npm run typecheck`; `npm run harness:validate:premerge`; `npm run instruction-root:integrity`; `npm run desktop:dist` | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
| Stable summary artifact | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
| Expected packaging outputs | `frontend/dist/Chirality-0.1.0-arm64.dmg`; `frontend/dist/mac-arm64/Chirality.app`; instruction-root integrity summary JSON | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
| CI workflow baseline | Checkout repository; setup Node.js 20; run `npm ci`; verify instruction-root assets; preflight validation script presence; start Next server; poll readiness; run premerge validation; verify stable summary artifact; upload summary artifact | `docs/PRD.md` Section 12.7 |
| Release target | macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |
| Ownership disposition | `ResponsibleParty` remains `TBD` until a human assigns ownership; CI/release execution must not be delegated on an inferred owner. | `_CONTEXT.md` Identity and Source Authority; `Procedure.md` Prerequisites |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":44,"line_start":34,"source_sha256":"02a648068432032291c9bb8cb3e0cbd94cf0d62bb6bf71e55f53341164fa8e33","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Source fidelity warning | `docs/PRD.md` has expected SHA `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` and observed SHA `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`; per dispatch brief, this is a source status. | `_REFERENCES.md`; dispatch brief |
| CI provider implementation | ASSUMPTION: GitHub Actions is the intended CI surface because `docs/PRD.md` Section 12.7 names "The GitHub workflow"; exact workflow file path is TBD. | `docs/PRD.md` Section 12.7 |
| Stable summary artifact path | The review target is `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | `docs/PRD.md` Sections 12.2 and 12.7; `docs/SPEC.md` Section 19.1 |
| CI upload artifact identity | The CI workflow must upload the stable summary artifact, but the CI upload artifact name, retention period, and workflow file path are `TBD` until source-defined or human-approved. | `docs/PRD.md` Section 12.7; `_SEMANTIC_LENSING.md` D-001 |
| Security posture during verification | API keys must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts; outbound network access remains loopback plus Anthropic API path unless amended. | `docs/CONTRACT.md` K-NET-1 and K-KEY-1 |
| Dependency state | Declared upstream and downstream dependencies remain `TBD`; extracted `Dependencies.csv` v3.1 rows exist but readiness remains blocked until accepted dependency-edge or blocker disposition is recorded. | `_DEPENDENCIES.md` Extracted Dependency Register; `_SEMANTIC_LENSING.md` X-002 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":54,"line_start":45,"source_sha256":"02a648068432032291c9bb8cb3e0cbd94cf0d62bb6bf71e55f53341164fa8e33","target_id":"CLM-005"} -->
##### Construction

| Construct | Required Content |
|---|---|
| CI workflow | Implement or maintain a premerge workflow that executes the PRD Section 12.7 sequence and uploads the stable validation summary artifact. |
| Local command sequence | Document a reproducible local sequence from `frontend/` that runs test, typecheck, premerge validation, instruction-root integrity, and desktop distribution checks. |
| Stable artifact verification | Verify that `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` exists after relevant checks and is uploaded by CI. |
| Manual release checklist | Verify macOS DMG architecture, minimum system version, signing posture, instruction-root assets, working-root selector availability, current shipped Anthropic network guardrails, SDK-backed packaged turn startup after R1, SDK subprocess execution access, and SDK transcript storage/mirroring decision conformance. |
| Evidence capture | Record command outcomes, artifact paths, and release-check findings in a release verification runbook or equivalent reviewable artifact. |

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":66,"line_start":55,"source_sha256":"02a648068432032291c9bb8cb3e0cbd94cf0d62bb6bf71e55f53341164fa8e33","target_id":"CLM-006"} -->
##### References

| RefID | Source | Used For | Status |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Governance and professional-boundary context | MATCH |
| REF-002 | `docs/CONTRACT.md` | Release, validation, network, key, packaging invariants | MATCH |
| REF-003 | `docs/SPEC.md` | Required checks, Section 8/9 validation, manual release verification | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary for artifacts, validation, `desktop:dist`, and lifecycle terms | MATCH |
| REF-005 | `docs/PLAN.md` | Local check command sequence and expected package artifacts | MATCH |
| REF-006 | `docs/PRD.md` | CI acceptance, validation plan, manual release verification | MATCH source status only — reconciled under D-APP-38 |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context | MATCH |

<!-- sow-source-end -->

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":69,"line_start":67,"source_sha256":"02a648068432032291c9bb8cb3e0cbd94cf0d62bb6bf71e55f53341164fa8e33","target_id":"CLM-007"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-09-05 CI Artifact and Release Verification Workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-008"} -->
#### Specification: DEL-09-05 CI Artifact and Release Verification Workflow

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":24,"line_start":5,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-009"} -->
##### Scope

This deliverable specifies the CI premerge workflow, stable artifact upload behavior, local command sequence, and manual release verification checklist for `DEL-09-05 CI Artifact and Release Verification Workflow`.

In scope:

- Required local validation checks for release-significant changes.
- CI execution of the premerge validation workflow.
- Stable validation summary artifact verification and upload, distinguishing runtime premerge summaries from packaging/instruction-root summaries.
- Manual release verification checklist for the current macOS arm64 unsigned DMG release target.
- Documentation of evidence paths and runbook records needed for release review.

Out of scope:

- Feature implementation except test fixtures and packaging glue, per PKG-09 exclusions.
- Section 8/9 test implementation details owned by sibling validation deliverables.
- Network, API key, attachment, and renderer security implementation details owned by `DEL-09-06`.
- Direct creation of `Dependencies.csv` in this run.
- Windows/Linux release packaging unless approved by governed amendment.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":44,"line_start":25,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-010"} -->
##### Requirements

| ReqID | Requirement | Source |
|---|---|---|
| REQ-09-05-001 | The local release-significant check sequence MUST include `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, and `npm run instruction-root:integrity` from `frontend/`; current runtime-premerge evidence may be collected through `npm run validate:release-quality`, with explicit skip reasons for environment-dependent premerge. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7; ADQ-14 implementation evidence |
| REQ-09-05-002 | The packaging check MUST include `npm run desktop:dist`. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
| REQ-09-05-003 | The expected packaging outputs MUST include `frontend/dist/Chirality-0.1.0-arm64.dmg`, `frontend/dist/mac-arm64/Chirality.app`, and `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
| REQ-09-05-004 | The CI workflow MUST checkout the repository, set up Node.js 20, install dependencies with `npm ci`, verify required instruction-root assets, check preflight validation script presence, start the Next server, poll readiness, run `npm run harness:validate:premerge`, verify the stable summary artifact, and upload the summary artifact. | `docs/PRD.md` Section 12.7 |
| REQ-09-05-005 | Runtime premerge validation MUST verify and upload the stable Section 8 summary at `frontend/artifacts/harness/section8/latest/summary.json`; packaging/instruction-root review separately uses `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`; the runtime-premerge wrapper writes `frontend/artifacts/harness/release-quality/latest/summary.json` as derivative evidence. | `docs/PRD.md` FR-066 and Section 12.7; `docs/SPEC.md` Section 19.1; ADQ-14 implementation evidence |
| REQ-09-05-006 | Manual macOS DMG release verification MUST check arm64 binary posture, `LSMinimumSystemVersion` `15.0.0` or later, unsigned/adhoc signing posture, required instruction-root assets in app resources, working-root selector availability, current shipped Anthropic network guardrails, packaged SDK-backed turn startup after R1, SDK subprocess execution access outside trapped `app.asar` layout, and accepted SDK transcript storage/mirroring behavior. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
| REQ-09-05-007 | Release validation MUST preserve current release target constraints: macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended. | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |
| REQ-09-05-008 | Release-significant changes MUST pass required local checks before acceptance. | `docs/CONTRACT.md` K-VALIDATE-1 |
| REQ-09-05-009 | Verification records MUST avoid writing API keys or secrets to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1 |
| REQ-09-05-010 | Verification MUST keep outbound network scope limited to explicit product scope: loopback plus Anthropic API path unless governed future scope expands it. | `docs/CONTRACT.md` K-NET-1 |
| REQ-09-05-011 | The release workflow MUST NOT represent Chirality as providing automated professional approval, code compliance, external validation, or solver ownership. | `docs/PRD.md` Section 12.1; `docs/DIRECTIVE.md` professional-boundary sections |
| REQ-09-05-012 | ASSUMPTION: The CI implementation target is a GitHub Actions workflow because `docs/PRD.md` Section 12.7 specifies "The GitHub workflow"; the exact workflow file path is TBD. | `docs/PRD.md` Section 12.7 |
| REQ-09-05-013 | Release evidence MUST map each requirement in this specification to a concrete evidence artifact, checklist row, or `TBD` blocker before workflow readiness is claimed. | `docs/CONTRACT.md` K-VALIDATE-1 and K-INVENT-1; `_SEMANTIC_LENSING.md` C-001 |
| REQ-09-05-014 | CI review evidence MUST show whether each of the ten PRD Section 12.7 workflow steps is present, absent, or `TBD`. | `docs/PRD.md` Section 12.7; `_SEMANTIC_LENSING.md` F-001 |
| REQ-09-05-015 | Release evidence MUST include explicit secret-redaction and accepted-network-scope inspection results for CI logs, release records, and packaged-app verification artifacts. | `docs/CONTRACT.md` K-KEY-1 and K-NET-1; `_SEMANTIC_LENSING.md` X-001 |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":54,"line_start":45,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-011"} -->
##### Standards

| Standard or Governing Source | Applicability |
|---|---|
| `docs/CONTRACT.md` K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1, K-NET-1, K-KEY-1 | Binding release, validation, packaging, network, and secret-handling invariants. |
| `docs/SPEC.md` Sections 19.1 through 19.4 | Physical command sequence, validation surfaces, and manual release verification checklist. |
| `docs/PRD.md` Sections 12.2, 12.7, and 12.8 | Product-level validation plan, CI acceptance, and release verification requirements. |
| `docs/PLAN.md` Section 7 | Roadmap-level command and artifact expectations. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `DEL-09-05` row and scope ledger | Deliverable scope, SOW mapping, and anticipated artifacts. |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":74,"line_start":55,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-012"} -->
##### Verification

| Requirement | Verification Approach |
|---|---|
| REQ-09-05-001 | Run or inspect documented local command sequence from `frontend/`; confirm all four commands are present in the runbook. |
| REQ-09-05-002 | Run or inspect `desktop:dist` packaging step in the local release sequence. |
| REQ-09-05-003 | Confirm expected paths exist after relevant command execution or are explicitly marked as failed with diagnostic notes. |
| REQ-09-05-004 | Review CI workflow definition for all ten PRD Section 12.7 steps. |
| REQ-09-05-005 | Confirm CI checks and upload the Section 8 premerge summary; confirm packaging/instruction-root evidence references the instruction-root summary; confirm the release-quality wrapper summary records both paths and any premerge skip. |
| REQ-09-05-006 | Execute manual release checklist against the built DMG and record pass/fail/TBD for each item. |
| REQ-09-05-007 | Confirm release checklist and packaging metadata do not introduce non-macOS or signed/notarized release claims without amendment. |
| REQ-09-05-008 | Confirm release-significant change gate requires passing local checks. |
| REQ-09-05-009 | Inspect logs/artifacts for secret redaction; do not store API keys in release evidence. |
| REQ-09-05-010 | Confirm packaged-app and CI verification do not broaden network access beyond accepted policy. |
| REQ-09-05-011 | Review runbook and CI/release notes for prohibited professional-approval or external-validation language. |
| REQ-09-05-012 | Human or implementation review confirms exact CI workflow path and artifact naming. |
| REQ-09-05-013 | Review the evidence matrix below and confirm every requirement has an artifact, checklist row, or unresolved blocker. |
| REQ-09-05-014 | Review CI workflow evidence against the ten PRD Section 12.7 steps one by one. |
| REQ-09-05-015 | Inspect release evidence for secret material and non-accepted network endpoints; record pass/fail/TBD for each inspection. |

<!-- sow-source-end -->

### CLM-013 — Evidence Matrix

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":94,"line_start":75,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-013"} -->
##### Evidence Matrix

| Requirement | Required Evidence |
|---|---|
| REQ-09-05-001 | Local runbook row showing `npm run validate:release-quality` for runtime-premerge evidence and packaging/instruction-root rows for `npm run instruction-root:integrity`, or a `TBD` blocker. |
| REQ-09-05-002 | Local runbook row showing `npm run desktop:dist`, or a `TBD` blocker. |
| REQ-09-05-003 | Artifact-path evidence for the DMG, app bundle, and stable summary JSON, or failed/TBD path rows. |
| REQ-09-05-004 | CI workflow review table with all ten PRD Section 12.7 steps marked present, absent, or `TBD`. |
| REQ-09-05-005 | CI/runtime evidence referencing `frontend/artifacts/harness/section8/latest/summary.json` and `frontend/artifacts/harness/release-quality/latest/summary.json`; packaging evidence referencing `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. |
| REQ-09-05-006 | Manual macOS DMG checklist with a pass/fail/TBD row for each source-defined check. |
| REQ-09-05-007 | Release-target row confirming macOS 15+ Apple Silicon unsigned/unnotarized local-builder scope, or governed amendment reference. |
| REQ-09-05-008 | Gate record showing required local checks passed before release-significant acceptance, or an unresolved blocker. |
| REQ-09-05-009 | Secret-redaction inspection row for logs, runtime records, SDK transcripts where applicable, and tool artifacts. |
| REQ-09-05-010 | Network-scope inspection row confirming loopback plus Anthropic API path only, or governed amendment reference. |
| REQ-09-05-011 | Boundary-language review row confirming no automated professional approval, code compliance, external validation, or solver-ownership claim. |
| REQ-09-05-012 | Human or implementation ruling for CI workflow path, upload artifact name, and retention period. |
| REQ-09-05-013 | Completed requirement-to-evidence matrix with unresolved entries carried as blockers. |
| REQ-09-05-014 | Ten-step CI acceptance checklist tied to workflow evidence. |
| REQ-09-05-015 | Secret and network inspection records tied to CI/release artifacts. |

<!-- sow-source-end -->

### CLM-014 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":111,"line_start":95,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-014"} -->
##### Documentation

Required outputs for this deliverable:

- CI workflow or workflow change implementing the premerge sequence.
- Stable artifact upload behavior for the validation summary.
- Local command sequence for release-significant validation.
- Manual release verification checklist/runbook.
- Reviewable evidence of command results, artifact paths, and unresolved `TBD` items.
- ADQ-14 evidence: `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-14_Release_Quality_Validation_Wrapper.md`.

Documentation notes:

- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- `ResponsibleParty` remains `TBD` until assigned by a human.
- Any missing implementation-specific detail, including workflow path, artifact name, retention period, release evidence filename, and exact checker script path, remains `TBD`.

<!-- sow-source-end -->

### CLM-015 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":115,"line_start":112,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-015"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.

<!-- sow-source-end -->

### CLM-016 — D-APP-56 CI ownership amendment (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":118,"line_start":116,"source_sha256":"e4879c4a4b6108632ffcc55e1a534c3e85b4a1e5cc5f31671f3c9c2a4f7b9201","target_id":"CLM-016"} -->
##### D-APP-56 CI ownership amendment (2026-07-12)

R4-P37 confirms DEL-09-05 as owner of `.github/workflows/harness-premerge.yml` and its `harness-validation-summaries` artifact. DEL-09-01 retains its Section 8 wrapper-preservation interest and verification contract but does not own the workflow.
<!-- sow-source-end -->

- **AC-001** — Every DEL-09-05 requirement maps to a concrete artifact, checklist row, or explicit TBD blocker; all ten PRD Section 12.7 CI steps and each manual release item have present, absent, pass, fail, or TBD status; required local and packaging commands and stable summary paths are distinguished; secret-redaction, accepted network scope, release-target constraints, and professional-boundary checks are recorded without unsupported readiness claims.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-09-05 CI Artifact and Release Verification Workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"a32c1e14e60d08e282eadf04499383debf53ac741894a9e81aaef2cc6fea7c18","target_id":"CLM-017"} -->
#### Procedure: DEL-09-05 CI Artifact and Release Verification Workflow

<!-- sow-source-end -->

### CLM-018 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":8,"line_start":3,"source_sha256":"a32c1e14e60d08e282eadf04499383debf53ac741894a9e81aaef2cc6fea7c18","target_id":"CLM-018"} -->
##### Purpose

Define the operational workflow to produce, verify, and use the CI artifact and release verification process for `DEL-09-05`.

This procedure is grounded in `docs/PRD.md` Sections 12.2, 12.7, and 12.8; `docs/SPEC.md` Sections 19.1 through 19.4; `docs/PLAN.md` Section 7; and `docs/CONTRACT.md` release/security invariants.

<!-- sow-source-end -->

### CLM-019 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":23,"line_start":9,"source_sha256":"a32c1e14e60d08e282eadf04499383debf53ac741894a9e81aaef2cc6fea7c18","target_id":"CLM-019"} -->
##### Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable context and references are present in the deliverable folder. | Present |
| `ResponsibleParty` is assigned. | TBD |
| Declared upstream dependency edges are accepted. | TBD |
| CI provider and workflow path are confirmed. | ASSUMPTION: GitHub Actions; path TBD |
| CI upload artifact name and retention period are confirmed. | TBD |
| Release verification runbook filename and evidence storage location are confirmed. | TBD |
| Local development environment can run commands from `frontend/`. | TBD |
| Required instruction-root assets are present. | To be verified by workflow |
| API keys and secrets are excluded from project files, logs, runtime events, and artifacts. | Required by `docs/CONTRACT.md` K-KEY-1 |
| Network scope remains loopback plus Anthropic API path unless amended. | Required by `docs/CONTRACT.md` K-NET-1 |

<!-- sow-source-end -->

### CLM-020 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":99,"line_start":24,"source_sha256":"a32c1e14e60d08e282eadf04499383debf53ac741894a9e81aaef2cc6fea7c18","target_id":"CLM-020"} -->
##### Steps

1. Confirm source and scope.
   - Verify this work remains scoped to `DEL-09-05`.
   - Record the PRD hash mismatch as a source warning if still present.
   - Keep `ResponsibleParty` as `TBD` unless a human assignment exists.

2. Define or review the local command sequence.
   - From `frontend/`, use the runtime-premerge wrapper for the non-packaging evidence family:

```bash
npm run validate:release-quality
```

   - The wrapper expands to full test, typecheck, standalone Section 9, and premerge unless premerge is explicitly skipped with reason.
   - For packaging/instruction-root evidence, include the source-defined packaging commands separately:

```bash
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
   - Verify `frontend/artifacts/harness/section8/latest/summary.json`.
   - Upload the Section 8 premerge summary artifact.
   - Record the exact workflow file path, CI upload artifact name, and retention period; keep each value `TBD` until source-defined or human-approved.

4. Verify stable artifact handling.
   - Confirm the workflow checks for the stable Section 8 premerge summary artifact path.
   - Confirm artifact upload uses a stable, reviewable name.
   - Mark artifact upload name and retention as `TBD` until source-defined or human-approved.
   - Distinguish runtime premerge, release-quality wrapper, and packaging/instruction-root summary paths from the CI-provider upload artifact name.

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
   - Confirm current shipped Anthropic network guardrails remain in force.
   - Confirm SDK-backed harness turn can start in packaged app after R1.
   - Confirm SDK subprocess or bundled binary is executable from package layout and not trapped inside `app.asar` without execution access.
   - Confirm SDK transcript storage/mirroring follows the accepted R1 storage decision.
   - Record pass/fail/TBD separately for each manual checklist item.

7. Record release evidence.
   - Record command results and artifact paths.
   - Record the release verification runbook filename and evidence storage location; keep both `TBD` until human-approved.
   - Map each specification requirement to an evidence artifact, checklist row, or unresolved blocker.
   - Record all ten PRD Section 12.7 CI steps as present, absent, or `TBD`.
   - Record pass/fail/TBD for each manual release verification item.
   - Record secret-redaction and accepted-network-scope inspection outcomes for CI and release artifacts.
   - Record accepted dependency-edge or blocker state before declaring workflow readiness.
   - Record unresolved `TBD` items and conflicts.
   - Do not record API keys or secret material.

8. Escalate human rulings.
   - Request human assignment for `ResponsibleParty`.
   - Request ruling for CI workflow path, artifact upload name/retention, and release evidence location.
   - Request PRD hash mismatch disposition outside this run if strict source closure is required.

<!-- sow-source-end -->

### CLM-021 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":111,"line_start":100,"source_sha256":"a32c1e14e60d08e282eadf04499383debf53ac741894a9e81aaef2cc6fea7c18","target_id":"CLM-021"} -->
##### Verification

| Check | Pass Condition |
|---|---|
| Local command sequence | Procedure or runbook includes the runtime-premerge wrapper plus separate packaging/instruction-root commands. |
| CI workflow | Workflow includes all ten PRD Section 12.7 steps. |
| Stable artifact | Section 8 premerge summary is verified/uploaded for CI; instruction-root summary is verified for packaging evidence; release-quality wrapper summary records command outcomes and skips. |
| Packaging outputs | DMG, app bundle, and instruction-root integrity summary paths are checked. |
| Manual release checklist | Each macOS DMG item is recorded as pass/fail/TBD. |
| Security | Release evidence contains no API keys or secret material and does not broaden network posture. |
| Professional boundary | Evidence and checklist do not claim automated professional approval, code compliance, external validation, or solver ownership. |

<!-- sow-source-end -->

### CLM-022 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":132,"line_start":112,"source_sha256":"a32c1e14e60d08e282eadf04499383debf53ac741894a9e81aaef2cc6fea7c18","target_id":"CLM-022"} -->
##### Records

Required records:

- CI workflow or workflow change.
- Stable artifact upload evidence.
- Local command sequence/runbook.
- Release-quality wrapper summary evidence.
- Manual release verification checklist with pass/fail/TBD entries.
- Release evidence summary with artifact paths and unresolved rulings.
- Requirement-to-evidence matrix covering each `REQ-09-05-*` item.
- CI ten-step review table covering PRD Section 12.7.
- Secret-redaction and network-scope inspection records.
- Dependency-edge or blocker disposition for release workflow readiness.

Record constraints:

- API keys and secret material must not be stored in project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts.
- The PRD hash mismatch must remain visible as a source warning until separately resolved.
- `Dependencies.csv` was produced by a prior dependency-recording run; P3 does not edit dependency files, and readiness still requires accepted dependency-edge or blocker disposition.

<!-- sow-source-end -->

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":135,"line_start":133,"source_sha256":"a32c1e14e60d08e282eadf04499383debf53ac741894a9e81aaef2cc6fea7c18","target_id":"CLM-023"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.
<!-- sow-source-end -->

- **VER-001** — Inspect the local command sequence, executed CI workflow and all ten required steps, stable Section 8, release-quality, and instruction-root summary handling, packaging outputs, manual macOS DMG checklist, requirement-to-evidence matrix, secret-redaction and network-scope inspections, release-target scope, professional-boundary language, and unresolved blockers.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-09-05 CI Artifact and Release Verification Workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-024"} -->
#### Guidance: DEL-09-05 CI Artifact and Release Verification Workflow

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-025 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":10,"line_start":5,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-025"} -->
##### Purpose

This deliverable gives release operators and implementers a stable validation workflow for CI artifacts and manual release verification. It exists to connect required local checks, Section 8/9 validation surfaces, stable summary artifact handling, and macOS DMG release verification into one reviewable workflow for PKG-09.

Source basis: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `DEL-09-05`; `docs/PRD.md` Sections 12.2, 12.7, and 12.8; `docs/SPEC.md` Sections 19.1 through 19.4.

<!-- sow-source-end -->

### CLM-026 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":19,"line_start":11,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-026"} -->
##### Principles

- Treat the local command sequence as the release-significant baseline: `test`, `typecheck`, `harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist` are the named commands in the accepted source slices.
- Keep CI evidence stable and reviewable. The stable summary artifact path is `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`.
- Separate CI automation from human release judgment. CI can run checks and upload artifacts, but it does not issue, certify, or professionally approve the work; only humans can author binding approval records, and release evidence remains review support until accepted.
- Preserve current release boundaries. The accepted target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended; expanding signing, notarization, or platform targets would alter governed release scope.
- Keep security posture visible during release verification: network scope and key handling are release constraints, not optional implementation details.
- Prefer `TBD` over invented implementation detail when workflow filename, artifact retention, or evidence format is not source-defined.

<!-- sow-source-end -->

### CLM-027 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":33,"line_start":20,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-027"} -->
##### Considerations

| Topic | Guidance | Source |
|---|---|---|
| PRD source warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; dispatch brief — reconciled under D-APP-38 |
| CI workflow location | ASSUMPTION: Use GitHub Actions because the PRD names a GitHub workflow. Exact file path remains TBD. | `docs/PRD.md` Section 12.7 |
| Stable artifact path | Use the source-defined path exactly when verifying or uploading the instruction-root integrity summary. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
| Section 8/9 scope | This deliverable should wire or verify the workflow; sibling deliverables own detailed validation additions and tests. | Decomposition PKG-09 rows |
| Manual verification | The runbook should record pass/fail/TBD per checklist item, not collapse all DMG checks into one overall statement. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
| Secret handling | Release logs and artifacts should be checked for accidental key material. API keys are non-project convenience state and must not enter project files or tool artifacts. | `docs/CONTRACT.md` K-KEY-1 |
| Network posture | CI and packaged-app verification should not broaden network policy beyond loopback plus Anthropic API path without governed scope change. | `docs/CONTRACT.md` K-NET-1 |
| Professional-boundary rationale | Treat CI pass results as technical evidence, not approval, because the directive and contract reserve reliance, issue, certification, and external validation decisions to accountable humans. | `docs/DIRECTIVE.md` Sections 3.1 and 3.2; `docs/CONTRACT.md` K-AUTH-1 and K-PROF-1 |
| Release-target rationale | Keep the macOS 15+ Apple Silicon unsigned/unnotarized local-builder target unchanged until amendment because it is the current release invariant and manual release verification target. | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |

<!-- sow-source-end -->

### CLM-028 — Term Normalization

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":42,"line_start":34,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-028"} -->
##### Term Normalization

| Term | Meaning | Current Disposition |
|---|---|---|
| Stable summary artifact | The source-defined validation summary at `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | Defined by `docs/PRD.md` Sections 12.2 and 12.7 and `docs/SPEC.md` Section 19.1. |
| CI upload artifact | The CI-provider artifact that uploads the stable summary artifact. | Name and retention period are `TBD`. |
| Release verification runbook | The reviewable record of local command results, CI workflow evidence, artifact paths, manual checklist rows, security checks, and unresolved rulings. | Filename is `TBD`. |
| Release evidence location | The final storage location for runbook and supporting release evidence. | Location is `TBD`; immutable snapshot policy remains open. |

<!-- sow-source-end -->

### CLM-029 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":51,"line_start":43,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-029"} -->
##### Trade-offs

| Decision Area | Trade-off | Recommendation |
|---|---|---|
| CI breadth vs runtime ownership | A broad CI job can catch release blockers, but Section 8/9 validation implementation belongs to sibling test deliverables. | Keep this deliverable focused on orchestration, artifact stability, and release checklist coverage. |
| Artifact path stability vs historical retention | `latest/summary.json` gives a stable pointer, but release evidence may need immutable history. | Use the stable path for CI acceptance; add immutable release evidence only if a governing source or human ruling specifies it. |
| Manual checklist vs automated packaging probes | Manual checks preserve release judgment, while automated probes reduce missed packaging issues. | Automate source-defined checks where practical, but keep a manual release verification checklist as required. |
| PRD mismatch handling | Blocking on the mismatch would preserve strict source fidelity, but the dispatch brief gives an explicit ruling for this run. | Proceed with a recorded source warning and avoid treating the mismatch as fixed. |

<!-- sow-source-end -->

### CLM-030 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":75,"line_start":52,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-030"} -->
##### Examples

Example local verification command block:

```bash
cd frontend
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run instruction-root:integrity
npm run desktop:dist
```

Example CI acceptance checklist:

| Step | Expected Evidence |
|---|---|
| Checkout and Node setup | CI log shows repository checkout and Node.js 20 setup. |
| Dependency install | CI log shows `npm ci` completed. |
| Instruction-root assets | CI log or validation output confirms required assets are present. |
| Premerge validation | CI log shows `npm run harness:validate:premerge` completed. |
| Stable summary artifact | CI verifies `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. |
| Artifact upload | CI uploads the summary artifact. |

<!-- sow-source-end -->

### CLM-031 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":81,"line_start":76,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-031"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-09-05-001 | PRD hash status: MATCH exists, but dispatcher instructs this run to treat it as source status. | `_REFERENCES.md` REF-006 hash status: MATCH | Dispatch brief PRD MATCH ruling | All PRD-grounded sections | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | TBD — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-032 — Open Items

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":89,"line_start":82,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-032"} -->
##### Open Items

- TBD: Exact CI workflow path.
- TBD: Stable upload artifact name and retention period.
- TBD: Release verification runbook filename and final evidence storage location.
- TBD: Human assignment for `ResponsibleParty`.
- TBD: Whether immutable release evidence snapshots are required in addition to the stable `latest/summary.json` pointer.

<!-- sow-source-end -->

### CLM-033 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":92,"line_start":90,"source_sha256":"d71ed351fe1f150fa24056df8e2b05566ebd6a20b81ad6923fba521c23050839","target_id":"CLM-033"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-035 SOW-036 SOW-072 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
