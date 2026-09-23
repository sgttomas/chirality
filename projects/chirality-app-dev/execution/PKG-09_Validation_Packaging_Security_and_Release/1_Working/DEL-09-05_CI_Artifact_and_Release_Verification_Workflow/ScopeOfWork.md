---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-05
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-035, SOW-036, SOW-072]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-05

## Current Codex MVP conformity

Codex is the sole MVP engine. Under D-GOV-43 topology A2 and D-APP-127, the App owns its Runtime service child and Runtime owns the stock Codex App Server child. Hosted supplier admission, per-root account consent, the LaunchAgent, packaged-basis hashing and supplier-containment evidence are retired subjects; they are not present-day qualification gates.

The App must preserve Codex-held credential custody and separation from other Codex clients, user-selected approval and sandbox policy, truthful event/approval presentation, and applicable renderer, attachment, secret-protection and package-executability controls. Historical Anthropic/Claude/Pi descriptions remain compatibility evidence and do not qualify the live Codex path.

Artifact identity must bind the selected candidate package version, App Info.plist and actual `Chirality-<candidate-version>-arm64.dmg`. Packaged executable behavior and instruction-root integrity require actual package evidence. Signing, notarization, minimum-OS and architecture inspection results must be recorded against that candidate; no result is inferred from a missing record.

Verification hooks: `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md` and `NATIVE_CHECKLIST.md` in the same folder, plus `frontend/package.json` registered packaging/security commands. These procedures supersede the retired Stage 9–13 spine; repeat affected checks when source, configuration or packaging changes invalidate earlier evidence. No publication or product acceptance follows from this text repair.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-05` in service of project scope [SOW-035, SOW-036, SOW-072] and package objectives [OBJ-008].

- **OUT-001** — A CI artifact and release verification workflow, local release-significant command sequence, stable validation artifact handling, manual macOS DMG verification checklist, and auditable requirement-to-evidence records for the current macOS 15+ arm64 target, with local unsigned/adhoc output distinguished from the D-GOV-43 signed/notarized consolidated candidate.
- **OUT-002** — The v3.0.0-rc.1 carrier outputs assigned to `DEL-09-05` by the applied decomposition row (`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` line 368 at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`): CI workflow and stable artifact evidence; WP-09 reviewed preparation/release runbook candidate; exact-candidate identity and custody checklist; separately authorized WP-11 owner/CHANGE execution record. Traceable to SOW-035, SOW-036, SOW-072 and OBJ-008.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-05 CI Artifact and Release Verification Workflow

> #### Datasheet: DEL-09-05 CI Artifact and Release Verification Workflow
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-09-05 |
> | DeliverableName | CI Artifact and Release Verification Workflow |
> | PackageID | PKG-09 |
> | PackageName | Validation, Packaging, Security, and Release |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | CI_CD_CHANGE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | Current Scope | Maintain CI premerge workflow, stable artifact upload, local command sequence, and manual release verification checklist. |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Covered scope items | SOW-035 Required local checks; SOW-036 Section 8/9 validation; SOW-072 macOS arm64 unsigned DMG release target | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 8/9, `DEL-09-05` and scope ledger rows |
> | Supported objective | OBJ-008 | `_CONTEXT.md` Traceability; decomposition `DEL-09-05` row |
> | Anticipated artifacts | CI workflow; stable artifact upload; release verification runbook | `_CONTEXT.md` Anticipated Artifacts; decomposition `DEL-09-05` row |
> | Local check command sequence | `npm run test`; `npm run typecheck`; `npm run harness:validate:premerge`; `npm run instruction-root:integrity`; `npm run desktop:dist` | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
> | Stable summary artifact | `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
> | Expected packaging outputs | `frontend/dist/Chirality-<candidate-version>-arm64.dmg`; `frontend/dist/mac-arm64/Chirality.app`; instruction-root integrity summary JSON | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
> | CI workflow baseline | Checkout repository; setup Node.js >=22.19.0; run `npm ci`; verify instruction-root assets; preflight validation script presence; start Next server; poll readiness; run premerge validation; verify stable summary artifact; upload summary artifact | `docs/PRD.md` Section 12.7 |
> | Release target | macOS 15+ Apple Silicon ordinary local unsigned/adhoc output; the consolidated candidate requires signature/notarization under D-GOV-43 | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |
> | Ownership disposition | `ResponsibleParty` remains `TBD` until a human assigns ownership; CI/release execution must not be delegated on an inferred owner. | `_CONTEXT.md` Identity and Source Authority; `Procedure.md` Prerequisites |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Source fidelity warning | `docs/PRD.md` has expected SHA `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` and observed SHA `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`; per dispatch brief, this is a source status. | `_REFERENCES.md`; dispatch brief |
> | CI provider implementation | GitHub Actions repository-root `.github/workflows/harness-premerge.yml`, owned by DEL-09-05; the project-local copy is not the executed workflow. | `docs/PRD.md` Section 12.7 |
> | Stable summary artifact path | The review target is `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | `docs/PRD.md` Sections 12.2 and 12.7; `docs/SPEC.md` Section 19.1 |
> | CI upload artifact identity | `harness-validation-summaries`; preserve actual retention configuration and run evidence instead of inventing a duration. | `docs/PRD.md` Section 12.7; `_SEMANTIC_LENSING.md` D-001 |
> | Security posture during verification | API keys must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts; outbound network access remains accepted K-NET-1 product transport and user-selected Codex network/sandbox policy. | `docs/CONTRACT.md` K-NET-1 and K-KEY-1 |
> | Dependency state | Declared upstream and downstream dependencies remain `TBD`; extracted `Dependencies.csv` v3.1 rows exist but readiness remains blocked until accepted dependency-edge or blocker disposition is recorded. | `_DEPENDENCIES.md` Extracted Dependency Register; `_SEMANTIC_LENSING.md` X-002 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Construct | Required Content |
> |---|---|
> | CI workflow | Implement or maintain a premerge workflow that executes the PRD Section 12.7 sequence and uploads the stable validation summary artifact. |
> | Local command sequence | Document a reproducible local sequence from `frontend/` that runs test, typecheck, premerge validation, instruction-root integrity, and desktop distribution checks. |
> | Stable artifact verification | Verify that `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` exists after relevant checks and is uploaded by CI. |
> | Manual release checklist | Verify macOS DMG architecture, minimum system version, signing posture, instruction-root assets, working-root selector availability, current K-NET-1 transports and user-selected Codex policy, applicable packaged S-6/S-8 checks, bundled Codex execution access, and current Runtime event/credential custody contract conformance. |
> | Evidence capture | Record command outcomes, artifact paths, and release-check findings in a release verification runbook or equivalent reviewable artifact. |
>


> Release-update maintenance must support an unauthenticated metadata check on manual request, normal GUI startup and every six hours while running, only at `https://api.github.com/repos/sgttomas/chirality-app/releases/latest`. Refuse credentials and redirects; validate stable release identity and exact `https://github.com/sgttomas/chirality-app/releases` destinations, compare versions without downgrading, and provide truthful availability/failure state. Opening a verified destination requires explicit system-browser handoff; no automatic install, restart or publishing. DEL-02-01 owns shell presentation.
>
> Authority: CONTRACT K-NET-1; owner direction in `execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/PRODUCT_GUIDANCE_AND_UPDATES.md` and `briefs/PUBLIC_RELEASE_UPDATES.md`, plus `execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/AUTOMATIC_UPDATES.md` (source commits 95b342519 / 7f1e9f387). Named verification: `frontend/src/__tests__/electron/app-update.test.ts`, `frontend/src/__tests__/components/app-update-provider.test.tsx`, `app-update-controls.test.tsx`, and candidate-bound native startup/cadence/browser evidence; capability map CAP-ELECTRON-030 / CAP-SHELL-014 / CAP-SHELL-015. No new execution result is asserted.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Used For | Status |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Governance and professional-boundary context | historical D-APP-38 source state; verify current candidate bytes |
> | REF-002 | `docs/CONTRACT.md` | Release, validation, network, key, packaging invariants | historical D-APP-38 source state; verify current candidate bytes |
> | REF-003 | `docs/SPEC.md` | Required checks, Section 8/9 validation, manual release verification | historical D-APP-38 source state; verify current candidate bytes |
> | REF-004 | `docs/TYPES.md` | Vocabulary for artifacts, validation, `desktop:dist`, and lifecycle terms | historical D-APP-38 source state; verify current candidate bytes |
> | REF-005 | `docs/PLAN.md` | Local check command sequence and expected package artifacts | historical D-APP-38 source state; verify current candidate bytes |
> | REF-006 | `docs/PRD.md` | CI acceptance, validation plan, manual release verification | historical D-APP-38 source state; verify current candidate bytes source status only — reconciled under D-APP-38 |
> | REF-007 | `../../workflows/software-decomp/WORKFLOW.md` | Decomposition method context | historical D-APP-38 source state; verify current candidate bytes |
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.

### CLM-034 — Historical assigned pathway — Applied decomposition v3 carrier assignment (SCA-APP-008 Gate 5, 2026-09-03)

> This applied assignment is preserved as dated pathway history. D-GOV-43/D-APP-127 supersede the G6a/Stage 9–13 mechanism; current follow-through is stated in REQ-003, CLM-019/023 and the retired-status detail below. Existing 3.0.0/3.0.1 releases do not authorize another release.

> ##### Applied decomposition row for DEL-09-05 at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`
>
> The accepted SCA-APP-008 Gate-5 application (PR #662) amended this deliverable's row. The row text below is transcribed verbatim from the applied decomposition and is the sole scope basis for the v3 outputs and requirements added on 2026-09-03; it adds no obligation beyond the row.
>
> | Column | Applied row text |
> |---|---|
> | Description | Maintain CI premerge and stable artifact verification and serve as the explicit release-operations carrier with a strict phase boundary: WP-09 may author and review the exact signing, nested-signing-order, fuses/entitlements, notarization/stapling/Gatekeeper, recovery/rollback, version-identity, custody, GitHub-prerelease, and download-backcheck runbook, but WP-11 may execute release acts only after Ryan Tufts names and rules the exact candidate at G6a. |
> | Principal outputs | CI workflow and stable artifact evidence; WP-09 reviewed preparation/release runbook candidate; exact-candidate identity and custody checklist; separately authorized WP-11 owner/CHANGE execution record |
> | Notes | WP-09 authoring/review is not a signing, notarization, publication, distribution, release-readiness, or lifecycle act. D-APP-97/F-APP-2 remain active through preparation. WP-11 execution is a later owner act requiring G6a and the exact owner artifact ruling; no automatic transition from preparation is permitted. macOS arm64 is the rc.1 target and a second target requires a post-rc.1 scope change. |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-09-05 CI Artifact and Release Verification Workflow

> #### Specification: DEL-09-05 CI Artifact and Release Verification Workflow
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies the CI premerge workflow, stable artifact upload behavior, local command sequence, and manual release verification checklist for `DEL-09-05 CI Artifact and Release Verification Workflow`.
>
> In scope:
>
> - Required local validation checks for release-significant changes.
> - CI execution of the premerge validation workflow.
> - Stable validation summary artifact verification and upload, distinguishing runtime premerge summaries from packaging/instruction-root summaries.
> - Manual release verification checklist for the current macOS arm64 release target with local/consolidated signing posture distinguished.
> - Documentation of evidence paths and runbook records needed for release review.
>
> Out of scope:
>
> - Feature implementation except test fixtures and packaging glue, per PKG-09 exclusions.
> - Section 8/9 test implementation details owned by sibling validation deliverables.
> - Network, API key, attachment, and renderer security implementation details owned by `DEL-09-06`.
> - Formal dependency-basis changes except through their owning process.
> - Windows/Linux release packaging unless approved by governed amendment.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ReqID | Requirement | Source |
> |---|---|---|
> | REQ-09-05-001 | The local release-significant check sequence MUST include `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, and `npm run instruction-root:integrity` from `frontend/`; current runtime-premerge evidence may be collected through `npm run validate:release-quality`, with explicit skip reasons for environment-dependent premerge. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7; ADQ-14 implementation evidence |
> | REQ-09-05-002 | The packaging check MUST include `npm run desktop:dist`. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1; `docs/PLAN.md` Section 7 |
> | REQ-09-05-003 | The expected packaging outputs MUST include `frontend/dist/Chirality-<candidate-version>-arm64.dmg`, `frontend/dist/mac-arm64/Chirality.app`, and `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
> | REQ-09-05-004 | CI MUST check out source, provision the supported Node floor, install dependencies, verify assets/scripts, establish the Runtime/project binding and Next readiness, run the registered premerge/release-quality chain, and verify/upload stable summaries. Retain a ten-step PRD mapping against the actual repository-root workflow. | `docs/PRD.md` Section 12.7 |
> | REQ-09-05-005 | Runtime premerge validation MUST verify and upload the stable Section 8 summary at `frontend/artifacts/harness/section8/latest/summary.json`; packaging/instruction-root review separately uses `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`; the runtime-premerge wrapper writes `frontend/artifacts/harness/release-quality/latest/summary.json` as derivative evidence. | `docs/PRD.md` FR-066 and Section 12.7; `docs/SPEC.md` Section 19.1; ADQ-14 implementation evidence |
> | REQ-09-05-006 | Manual packaged verification MUST bind arm64, minimum macOS 15+, required assets, working-root UI, current network/security scope, signature/notarization posture, lockfile-pinned Codex execution and applicable packaged S-6/S-8 to the actual candidate. SDK-era checks are historical compatibility. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
> | REQ-09-05-007 | macOS 15+ arm64; ordinary local output may be unsigned/adhoc, while the D-GOV-43 consolidated candidate requires verified signature, notarization and lockfile-pinned Codex identity. Publication remains a separate exact-candidate owner act. | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |
> | REQ-09-05-008 | Release-significant changes MUST pass required local checks before acceptance. | `docs/CONTRACT.md` K-VALIDATE-1 |
> | REQ-09-05-009 | Verification records MUST avoid writing API keys or secrets to project files, runtime event payloads, logs, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1 |
> | REQ-09-05-010 | Verification MUST record current K-NET-1 transports, user-selected Codex network/sandbox policy, renderer restrictions and update-metadata transport, without copying credentials or claiming unobserved enforcement. | `docs/CONTRACT.md` K-NET-1 |
> | REQ-09-05-011 | The release workflow MUST NOT represent Chirality as providing automated professional approval, code compliance, external validation, or solver ownership. | `docs/PRD.md` Section 12.1; `docs/DIRECTIVE.md` professional-boundary sections |
> | REQ-09-05-012 | The CI owner is DEL-09-05; the executed GitHub Actions file is repository-root `.github/workflows/harness-premerge.yml` and its upload is `harness-validation-summaries`. | `docs/PRD.md` Section 12.7 |
> | REQ-09-05-013 | Release evidence MUST map each requirement in this specification to a concrete evidence artifact, checklist row, or `TBD` blocker before workflow readiness is claimed. | `docs/CONTRACT.md` K-VALIDATE-1 and K-INVENT-1; `_SEMANTIC_LENSING.md` C-001 |
> | REQ-09-05-014 | CI review evidence MUST show whether each of the ten PRD Section 12.7 workflow steps is present, absent, or `TBD`. | `docs/PRD.md` Section 12.7; `_SEMANTIC_LENSING.md` F-001 |
> | REQ-09-05-015 | Release evidence MUST include explicit secret-redaction and accepted-network-scope inspection results for CI logs, release records, and packaged-app verification artifacts. | `docs/CONTRACT.md` K-KEY-1 and K-NET-1; `_SEMANTIC_LENSING.md` X-001 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or Governing Source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` K-PACKAGE-1, K-RELEASE-1, K-VALIDATE-1, K-NET-1, K-KEY-1 | Binding release, validation, packaging, network, and secret-handling invariants. |
> | `docs/SPEC.md` Sections 19.1 through 19.4 | Physical command sequence, validation surfaces, and manual release verification checklist. |
> | `docs/PRD.md` Sections 12.2, 12.7, and 12.8 | Product-level validation plan, CI acceptance, and release verification requirements. |
> | `docs/PLAN.md` Section 7 | Roadmap-level command and artifact expectations. |
> | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `DEL-09-05` row and scope ledger | Deliverable scope, SOW mapping, and anticipated artifacts. |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement | Verification Approach |
> |---|---|
> | REQ-09-05-001 | Run or inspect documented local command sequence from `frontend/`; confirm all four commands are present in the runbook. |
> | REQ-09-05-002 | Run or inspect `desktop:dist` packaging step in the local release sequence. |
> | REQ-09-05-003 | Confirm expected paths exist after relevant command execution or are explicitly marked as failed with diagnostic notes. |
> | REQ-09-05-004 | CI MUST check out source, provision the supported Node floor, install dependencies, verify assets/scripts, establish the Runtime/project binding and Next readiness, run the registered premerge/release-quality chain, and verify/upload stable summaries. Retain a ten-step PRD mapping against the actual repository-root workflow. |
> | REQ-09-05-005 | Confirm CI checks and upload the Section 8 premerge summary; confirm packaging/instruction-root evidence references the instruction-root summary; confirm the release-quality wrapper summary records both paths and any premerge skip. |
> | REQ-09-05-006 | Manual packaged verification MUST bind arm64, minimum macOS 15+, required assets, working-root UI, current network/security scope, signature/notarization posture, lockfile-pinned Codex execution and applicable packaged S-6/S-8 to the actual candidate. SDK-era checks are historical compatibility. |
> | REQ-09-05-007 | macOS 15+ arm64; ordinary local output may be unsigned/adhoc, while the D-GOV-43 consolidated candidate requires verified signature, notarization and lockfile-pinned Codex identity. Publication remains a separate exact-candidate owner act. |
> | REQ-09-05-008 | Confirm release-significant change gate requires passing local checks. |
> | REQ-09-05-009 | Inspect logs/artifacts for secret redaction; do not store API keys in release evidence. |
> | REQ-09-05-010 | Verification MUST record current K-NET-1 transports, user-selected Codex network/sandbox policy, renderer restrictions and update-metadata transport, without copying credentials or claiming unobserved enforcement. |
> | REQ-09-05-011 | Review runbook and CI/release notes for prohibited professional-approval or external-validation language. |
> | REQ-09-05-012 | The CI owner is DEL-09-05; the executed GitHub Actions file is repository-root `.github/workflows/harness-premerge.yml` and its upload is `harness-validation-summaries`. |
> | REQ-09-05-013 | Review the evidence matrix below and confirm every requirement has an artifact, checklist row, or unresolved blocker. |
> | REQ-09-05-014 | Review CI workflow evidence against the ten PRD Section 12.7 steps one by one. |
> | REQ-09-05-015 | Inspect release evidence for secret material and non-accepted network endpoints; record pass/fail/TBD for each inspection. |
>

### CLM-013 — Evidence Matrix

> ##### Evidence Matrix
>
> | Requirement | Required Evidence |
> |---|---|
> | REQ-09-05-001 | Local runbook row showing `npm run validate:release-quality` for runtime-premerge evidence and packaging/instruction-root rows for `npm run instruction-root:integrity`, or a `TBD` blocker. |
> | REQ-09-05-002 | Local runbook row showing `npm run desktop:dist`, or a `TBD` blocker. |
> | REQ-09-05-003 | Artifact-path evidence for the DMG, app bundle, and stable summary JSON, or failed/TBD path rows. |
> | REQ-09-05-004 | CI MUST check out source, provision the supported Node floor, install dependencies, verify assets/scripts, establish the Runtime/project binding and Next readiness, run the registered premerge/release-quality chain, and verify/upload stable summaries. Retain a ten-step PRD mapping against the actual repository-root workflow. |
> | REQ-09-05-005 | CI/runtime evidence referencing `frontend/artifacts/harness/section8/latest/summary.json` and `frontend/artifacts/harness/release-quality/latest/summary.json`; packaging evidence referencing `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. |
> | REQ-09-05-006 | Manual packaged verification MUST bind arm64, minimum macOS 15+, required assets, working-root UI, current network/security scope, signature/notarization posture, lockfile-pinned Codex execution and applicable packaged S-6/S-8 to the actual candidate. SDK-era checks are historical compatibility. |
> | REQ-09-05-007 | macOS 15+ arm64; ordinary local output may be unsigned/adhoc, while the D-GOV-43 consolidated candidate requires verified signature, notarization and lockfile-pinned Codex identity. Publication remains a separate exact-candidate owner act. |
> | REQ-09-05-008 | Gate record showing required local checks passed before release-significant acceptance, or an unresolved blocker. |
> | REQ-09-05-009 | Secret-redaction inspection row for logs, runtime records, SDK transcripts where applicable, and tool artifacts. |
> | REQ-09-05-010 | Verification MUST record current K-NET-1 transports, user-selected Codex network/sandbox policy, renderer restrictions and update-metadata transport, without copying credentials or claiming unobserved enforcement. |
> | REQ-09-05-011 | Boundary-language review row confirming no automated professional approval, code compliance, external validation, or solver-ownership claim. |
> | REQ-09-05-012 | The CI owner is DEL-09-05; the executed GitHub Actions file is repository-root `.github/workflows/harness-premerge.yml` and its upload is `harness-validation-summaries`. |
> | REQ-09-05-013 | Completed requirement-to-evidence matrix with unresolved entries carried as blockers. |
> | REQ-09-05-014 | Ten-step CI acceptance checklist tied to workflow evidence. |
> | REQ-09-05-015 | Secret and network inspection records tied to CI/release artifacts. |
>

### CLM-014 — Documentation

> ##### Documentation
>
> Required outputs for this deliverable:
>
> - CI workflow or workflow change implementing the premerge sequence.
> - Stable artifact upload behavior for the validation summary.
> - Local command sequence for release-significant validation.
> - Manual release verification checklist/runbook.
> - Reviewable evidence of command results, artifact paths, and unresolved `TBD` items.
> - ADQ-14 evidence: `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-14_Release_Quality_Validation_Wrapper.md`.
>
> Documentation notes:
>
> - REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes.
> - `ResponsibleParty` remains `TBD` until assigned by a human.
> - The workflow path and upload artifact name are source-defined above. Still-missing details, including observed retention, a release evidence filename, and the exact checker script path, remain `TBD` until bound to the candidate source or run.
>

### CLM-015 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.
>

### CLM-016 — D-APP-56 CI ownership amendment (2026-07-12)

> ##### D-APP-56 CI ownership amendment (2026-07-12)
>
> R4-P37 confirms DEL-09-05 as owner of `.github/workflows/harness-premerge.yml` and its `harness-validation-summaries` artifact. DEL-09-01 retains its Section 8 wrapper-preservation interest and verification contract but does not own the workflow.

- **REQ-001** — The deliverable shall maintain CI premerge and stable artifact verification and serve as the explicit release-operations carrier with a strict phase boundary.
- **REQ-002** — WP-09 may author and review the exact signing, nested-signing-order, fuses/entitlements, notarization/stapling/Gatekeeper, recovery/rollback, version-identity, custody, GitHub-prerelease, and download-backcheck runbook; authoring and review is not a signing, notarization, publication, distribution, release-readiness, or lifecycle act, and D-APP-97/F-APP-2 remain active through preparation.
- **REQ-003** — D-GOV-43/D-APP-127 supersede the retired Stage 9–13/G6a procedure. Prior exact-candidate release acts for 3.0.0/3.0.1 remain recorded history; a future release requires its own exact-candidate owner authorization and current checks, with no automatic transition from preparation.
- **REQ-004** — macOS arm64 remains the accepted target; adding another target requires its owning scope change.
- **AC-001** — Every DEL-09-05 requirement maps to a concrete artifact, checklist row, or explicit TBD blocker; all ten PRD Section 12.7 CI steps and each manual release item have present, absent, pass, fail, or TBD status; required local and packaging commands and stable summary paths are distinguished; secret-redaction, accepted network scope, release-target constraints, and professional-boundary checks are recorded without unsupported readiness claims.
- **AC-002** — The v3 outputs assigned by the applied decomposition row (CI workflow and stable artifact evidence, WP-09 reviewed preparation/release runbook candidate, exact-candidate identity and custody checklist, and a separately authorized WP-11 owner/CHANGE execution record) exist and satisfy REQ-001 through REQ-004, with each actual release act distinguished from preparation and bound to its own exact-candidate authorization and evidence; no new act is implied by this record.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-09-05 CI Artifact and Release Verification Workflow

> #### Procedure: DEL-09-05 CI Artifact and Release Verification Workflow
>

### CLM-018 — Purpose

> ##### Purpose
>
> Define the operational workflow to produce, verify, and use the CI artifact and release verification process for `DEL-09-05`.
>
> This procedure is grounded in `docs/PRD.md` Sections 12.2, 12.7, and 12.8; `docs/SPEC.md` Sections 19.1 through 19.4; `docs/PLAN.md` Section 7; and `docs/CONTRACT.md` release/security invariants.
>

### CLM-019 — Prerequisites

> Use repository-root `.github/workflows/harness-premerge.yml`, upload `harness-validation-summaries`, and the current PACKAGING_PROCEDURE.md and NATIVE_CHECKLIST.md under `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/`. Historical reviewed runbook candidates remain readable. Retention duration, actual missing native outputs and accountable performer are not invented. Check the active dependency register, package inputs and credential/network protections before relying on results. ResponsibleParty remains unassigned where no owning record assigns it.

### CLM-020 — Steps

> ##### Steps
>
> 1. Confirm source and scope.
>    - Verify this work remains scoped to `DEL-09-05`.
>    - Record the PRD hash mismatch as a source warning if still present.
>    - Keep `ResponsibleParty` as `TBD` unless a human assignment exists.
>
> 2. Define or review the local command sequence.
>    - From `frontend/`, use the runtime-premerge wrapper for the non-packaging evidence family:
>
> ```bash
> npm run validate:release-quality
> ```
>
>    - The wrapper expands to full test, typecheck, standalone Section 9, and premerge unless premerge is explicitly skipped with reason.
>    - For packaging/instruction-root evidence, include the source-defined packaging commands separately:
>
> ```bash
> npm run instruction-root:integrity
> npm run desktop:dist
> ```
>
> 3. Define or review the CI workflow sequence.
>    - Checkout repository.
>    - Setup Node.js >=22.19.0.
>    - Install dependencies with `npm ci`.
>    - Verify required instruction-root assets are present.
>    - Verify preflight validation script presence.
>    - Start the Next server.
>    - Poll readiness.
>    - Run `npm run harness:validate:premerge`.
>    - Verify `frontend/artifacts/harness/section8/latest/summary.json`.
>    - Upload the Section 8 premerge summary artifact.
>    - Record the source-defined repository workflow `.github/workflows/harness-premerge.yml` and upload artifact `harness-validation-summaries`; inspect the candidate run and actual retention setting without inventing a duration.
>
> 4. Verify stable artifact handling.
>    - Confirm the workflow checks for the stable Section 8 premerge summary artifact path.
>    - Confirm artifact upload uses a stable, reviewable name.
>    - Use the source-defined upload name `harness-validation-summaries`; retain the actual retention setting as unverified until observed in the candidate CI configuration or run.
>    - Distinguish runtime premerge, release-quality wrapper, and packaging/instruction-root summary paths from the CI-provider upload artifact name.
>
> 5. Execute or document packaging verification.
>    - Run or require `npm run desktop:dist` from `frontend/`.
>    - Confirm expected outputs:
>      - `frontend/dist/Chirality-<candidate-version>-arm64.dmg`
>      - `frontend/dist/mac-arm64/Chirality.app`
>      - `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`
>
> 6. Execute manual macOS DMG release verification.
>    - Confirm binary is arm64.
>    - Confirm `LSMinimumSystemVersion` is `15.0.0` or later.
>    - Verify signing posture for the actual candidate: ordinary local unsigned/adhoc versus consolidated signed/notarized under D-GOV-43.
>    - Confirm app resources contain required instruction-root assets.
>    - Confirm app launches and working-root selector is available.
>    - Confirm current K-NET-1 transports and user-selected Codex policy remain in force.
>    - Record actual packaged Codex S-6/S-8 outcomes or precise missing evidence.
>    - Confirm SDK subprocess or bundled binary is executable from package layout and not trapped inside `app.asar` without execution access.
>    - Verify current Runtime event persistence and Codex credential custody; legacy transcript decisions remain history.
>    - Record pass/fail/TBD separately for each manual checklist item.
>
> 7. Record release evidence.
>    - Record command results and artifact paths.
>    - Record the release verification runbook filename and evidence storage location; keep both `TBD` until human-approved.
>    - Map each specification requirement to an evidence artifact, checklist row, or unresolved blocker.
>    - Record all ten PRD Section 12.7 CI steps as present, absent, or `TBD`.
>    - Record pass/fail/TBD for each manual release verification item.
>    - Record secret-redaction and accepted-network-scope inspection outcomes for CI and release artifacts.
>    - Record accepted dependency-edge or blocker state before declaring workflow readiness.
>    - Record unresolved `TBD` items and conflicts.
>    - Do not record API keys or secret material.
>
> 8. Escalate human rulings.
>    - Request human assignment for `ResponsibleParty`.
>    - Request ruling for CI workflow path, artifact upload name/retention, and release evidence location.
>    - Request PRD hash mismatch disposition outside this run if strict source closure is required.
>

### CLM-021 — Verification

> ##### Verification
>
> | Check | Pass Condition |
> |---|---|
> | Local command sequence | Procedure or runbook includes the runtime-premerge wrapper plus separate packaging/instruction-root commands. |
> | CI workflow | Workflow includes all ten PRD Section 12.7 steps. |
> | Stable artifact | Section 8 premerge summary is verified/uploaded for CI; instruction-root summary is verified for packaging evidence; release-quality wrapper summary records command outcomes and skips. |
> | Packaging outputs | DMG, app bundle, and instruction-root integrity summary paths are checked. |
> | Manual release checklist | Each macOS DMG item is recorded as pass/fail/TBD. |
> | Security | Release evidence contains no API keys or secret material and does not broaden network posture. |
> | Professional boundary | Evidence and checklist do not claim automated professional approval, code compliance, external validation, or solver ownership. |
>

### CLM-022 — Records

> ##### Records
>
> Required records:
>
> - CI workflow or workflow change.
> - Stable artifact upload evidence.
> - Local command sequence/runbook.
> - Release-quality wrapper summary evidence.
> - Manual release verification checklist with pass/fail/TBD entries.
> - Release evidence summary with artifact paths and unresolved rulings.
> - Requirement-to-evidence matrix covering each `REQ-09-05-*` item.
> - CI ten-step review table covering PRD Section 12.7.
> - Secret-redaction and network-scope inspection records.
> - Dependency-edge or blocker disposition for release workflow readiness.
>
> Record constraints:
>
> - API keys and secret material must not be stored in project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts.
> - The PRD hash mismatch must remain visible as a source warning until separately resolved.
> - `Dependencies.csv` was produced by a prior dependency-recording run; P3 does not edit dependency files, and readiness still requires accepted dependency-edge or blocker disposition.
>

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.

- **VER-001** — Inspect the local command sequence, executed CI workflow and all ten required steps, stable Section 8, release-quality, and instruction-root summary handling, packaging outputs, manual macOS DMG checklist, requirement-to-evidence matrix, secret-redaction and network-scope inspections, release-target scope, professional-boundary language, and unresolved blockers.
- **VER-002** — Inspect the runbook candidate and custody checklist for the exact procedure content and phase boundary, confirm independent review of the candidate, and bind each actual release act to its exact-candidate authorization under the current D-GOV-43/D-APP-127 procedure; historical G6a/WP gates remain historical.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-09-05 CI Artifact and Release Verification Workflow

> #### Guidance: DEL-09-05 CI Artifact and Release Verification Workflow
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-025 — Purpose

> ##### Purpose
>
> This deliverable gives release operators and implementers a stable validation workflow for CI artifacts and manual release verification. It exists to connect required local checks, Section 8/9 validation surfaces, stable summary artifact handling, and macOS DMG release verification into one reviewable workflow for PKG-09.
>
> Source basis: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `DEL-09-05`; `docs/PRD.md` Sections 12.2, 12.7, and 12.8; `docs/SPEC.md` Sections 19.1 through 19.4.
>

### CLM-026 — Principles

> ##### Principles
>
> - Treat the local command sequence as the release-significant baseline: `test`, `typecheck`, `harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist` are the named commands in the accepted source slices.
> - Keep CI evidence stable and reviewable. The stable summary artifact path is `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`.
> - Separate CI automation from human release judgment. CI can run checks and upload artifacts, but it does not issue, certify, or professionally approve the work; only humans can author binding approval records, and release evidence remains review support until accepted.
> - Preserve current release boundaries. The accepted target is macOS 15+ Apple Silicon ordinary local unsigned/adhoc output; the consolidated candidate requires signature/notarization under D-GOV-43; expanding signing, notarization, or platform targets would alter governed release scope.
> - Keep security posture visible during release verification: network scope and key handling are release constraints, not optional implementation details.
> - Prefer `TBD` over invented implementation detail when workflow filename, artifact retention, or evidence format is not source-defined.
>

### CLM-027 — Considerations

> ##### Considerations
>
> | Topic | Guidance | Source |
> |---|---|---|
> | PRD source warning | REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes. | `_REFERENCES.md`; dispatch brief — reconciled under D-APP-38 |
> | CI workflow location | ASSUMPTION: Use GitHub Actions because the PRD names a GitHub workflow. Selected evidence path is named in the current construction/verification contract. | `docs/PRD.md` Section 12.7 |
> | Stable artifact path | Use the source-defined path exactly when verifying or uploading the instruction-root integrity summary. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
> | Section 8/9 scope | This deliverable should wire or verify the workflow; sibling deliverables own detailed validation additions and tests. | Decomposition PKG-09 rows |
> | Manual verification | The runbook should record pass/fail/TBD per checklist item, not collapse all DMG checks into one overall statement. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
> | Secret handling | Release logs and artifacts should be checked for accidental key material. API keys are non-project convenience state and must not enter project files or tool artifacts. | `docs/CONTRACT.md` K-KEY-1 |
> | Network posture | CI and packaged-app verification should not broaden network policy beyond loopback plus Anthropic API path without governed scope change. | `docs/CONTRACT.md` K-NET-1 |
> | Professional-boundary rationale | Treat CI pass results as technical evidence, not approval, because the directive and contract reserve reliance, issue, certification, and external validation decisions to accountable humans. | `docs/DIRECTIVE.md` Sections 3.1 and 3.2; `docs/CONTRACT.md` K-AUTH-1 and K-PROF-1 |
> | Release-target rationale | Apply the already-settled D-GOV-43 local/consolidated signing posture; platform expansion and new release acts retain their separate authority. | `docs/CONTRACT.md` K-RELEASE-1; `docs/SPEC.md` Section 19.4 |
>

### CLM-028 — Term Normalization

> Stable Section 8 summary: `frontend/artifacts/harness/section8/latest/summary.json`; release-quality derivative: `frontend/artifacts/harness/release-quality/latest/summary.json`; packaged instruction integrity: `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. These are different subjects. CI upload: `harness-validation-summaries` from repository-root `.github/workflows/harness-premerge.yml`. Current packaging and native runbooks are named in CLM-019. Retention, missing execution outputs and exact performer remain unknown unless source records establish them. Existing hosted CI and local signing/notarization/publication do not establish an attestation or hosted release job.

### CLM-029 — Trade-offs

> ##### Trade-offs
>
> | Decision Area | Trade-off | Recommendation |
> |---|---|---|
> | CI breadth vs runtime ownership | A broad CI job can catch release blockers, but Section 8/9 validation implementation belongs to sibling test deliverables. | Keep this deliverable focused on orchestration, artifact stability, and release checklist coverage. |
> | Artifact path stability vs historical retention | `latest/summary.json` gives a stable pointer, but release evidence may need immutable history. | Use the stable path for CI acceptance; add immutable release evidence only if a governing source or human ruling specifies it. |
> | Manual checklist vs automated packaging probes | Manual checks preserve release judgment, while automated probes reduce missed packaging issues. | Automate source-defined checks where practical, but keep a manual release verification checklist as required. |
> | PRD mismatch handling | Blocking on the mismatch would preserve strict source fidelity, but the dispatch brief gives an explicit ruling for this run. | Proceed with a recorded source warning and avoid treating the mismatch as fixed. |
>

### CLM-030 — Examples

> ##### Examples
>
> Example local verification command block:
>
> ```bash
> cd frontend
> npm run test
> npm run typecheck
> npm run harness:validate:premerge
> npm run instruction-root:integrity
> npm run desktop:dist
> ```
>
> Example CI acceptance checklist:
>
> | Step | Expected Evidence |
> |---|---|
> | Checkout and Node setup | CI log shows repository checkout and Node.js >=22.19.0 setup. |
> | Dependency install | CI log shows `npm ci` completed. |
> | Instruction-root assets | CI log or validation output confirms required assets are present. |
> | Premerge validation | CI log shows `npm run harness:validate:premerge` completed. |
> | Stable summary artifact | CI verifies `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. |
> | Artifact upload | CI uploads the summary artifact. |
>

### CLM-031 — Conflict Table (for human ruling)

> Earlier drafting source-state conflicts are historical at their recorded basis. Current reliance requires candidate-bound source verification through `execution/_Scripts/references_hash_tool.py`, with actual mismatch or authorized bypass retained. D-APP-38 did not guarantee perpetual MATCH. Apply settled D-GOV-43/D-APP-127 direction and retain substantive implementation/evidence gaps in governing scope and any selected graph; this record neither re-pins an accepted source nor certifies a new product result.

### CLM-032 — Open Items

> The CI workflow, upload identity and current packaging/native runbooks are named in CLM-019/028; those naming decisions are closed. Current open work is actual candidate-bound manual/CI/security evidence and current requirement mapping. Retention duration, accountable performer and missing result artifacts remain unknown unless source evidence establishes them. ResponsibleParty remains human-owned. Preserve immutable result identities when using mutable latest pointers; no new approval or release is implied.

### CLM-033 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-146/147 record repo-root `.github/workflows/harness-premerge.yml` as the executed workflow, indirect premerge via `validate:release-quality`, added typecheck/Vitest/instruction-root gates, and `harness-validation-summaries`; the project-local workflow is non-executing.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-035 SOW-036 SOW-072 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
| OUT-002 | SOW-035 SOW-036 SOW-072 OBJ-008 | CLM-034 REQ-001 REQ-002 REQ-003 REQ-004 | AC-002 | VER-002 | Reviewed runbook candidate and custody checklist bytes with independent review record; stable artifact evidence; WP-11 execution record only after G6a |

## Retired status detail (2026-09-23)

These clauses preserve operative meaning from the retired App status source. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R080:** Record actual 3.0.0 and 3.0.1 release identity and candidate evidence, distinguishing owner testimony from retained build and verification outputs.

- **APP-R081:** The old 2.0.0 to 3.0.0-rc.1 patch step is superseded. Current shipped-candidate identity and consistency proof remain required under REQ-003/CLM-019/023.
