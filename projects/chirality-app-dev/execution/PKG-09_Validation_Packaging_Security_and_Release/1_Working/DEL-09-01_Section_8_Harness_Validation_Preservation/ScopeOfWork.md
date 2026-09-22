---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-01
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-035, SOW-036]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-01` in service of project scope [SOW-035, SOW-036] and package objectives [OBJ-008].

- **OUT-001** — Preserved Section 8 harness validation behavior and stable premerge summary evidence for DEL-09-01.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-01 Section 8 Harness Validation Preservation

> #### Datasheet: DEL-09-01 Section 8 Harness Validation Preservation
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-09-01 |
> | DeliverableName | Section 8 Harness Validation Preservation |
> | PackageID | PKG-09 |
> | PackageName | Validation, Packaging, Security, and Release |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | TEST_SUITE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-035, SOW-036 |
> | SupportsObjectives | OBJ-008 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary purpose | Preserve baseline harness validation, current local checks, and stable premerge summary behavior. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 8, DEL-09-01 |
> | Required local checks in scope | `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `npm run instruction-root:integrity`; packaging check `npm run desktop:dist` is release-scope context. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1 |
> | Premerge command | `npm run harness:validate:premerge` from `frontend/`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` FR-066; `frontend/package.json` scripts |
> | Stable Section 8 summary artifact | `frontend/artifacts/harness/section8/latest/summary.json`. | `docs/PRD.md` FR-066; `frontend/scripts/validate-harness-premerge.mjs` stableArtifactPath; `.github/workflows/harness-premerge.yml` Verify stable summary artifact |
> | Retained Section 8 wrapper IDs (compatibility coverage, not live Codex qualification) | `setup.server_reachable`; `regression.session_crud`; `section8.boot_error_taxonomy`; `section8.smoke_stream`; `section8.session_persistence_resume`; `section8.permissions_dontask`; `section8.interrupt_sigint`; `section8.sdk_native_stream`. | `frontend/scripts/validate-harness-premerge.mjs` REQUIRED_TEST_IDS; `frontend/scripts/validate-harness-section8.mjs` REQUIRED_CHECK_ORDER |
> | Legacy removed test ID | `regression.api_chat_reachability` must not appear in the premerge summary. | `frontend/scripts/validate-harness-premerge.mjs` LEGACY_REMOVED_TEST_ID |
> | CI workflow surface | The repository-root `.github/workflows/harness-premerge.yml`, owned by DEL-09-05, invokes the registered release-quality/premerge chain and uploads `harness-validation-summaries`. The App-local workflow copy is not the executed GitHub workflow. | `.github/workflows/harness-premerge.yml` |
>

### CLM-004 — Conditions

> The registered Section 8 wrapper must preserve its structural missing-script, missing-ID and retired-ID checks. Its retained SDK/permission/interrupt rows prove only their own compatibility subjects; current Codex qualification requires distinct source-bound Runtime/native evidence under D-APP-131 P08. Its live-path checks require a reachable Runtime binding and Next transport; starting Next alone does not establish Runtime readiness. The repository-root `.github/workflows/harness-premerge.yml` supplies a controlled Runtime binding for CI. Such stub evidence is distinct from production Codex/native evidence.
>
> Use the selected `HARNESS_PROJECT_ROOT` and binding rather than the removed examples/example-project path. In shared-runtime mode (`CHIRALITY_RUNTIME_PROJECT_ID`) automatic staging is skipped; record the actual root and effective environment. Named hooks: `frontend/scripts/validate-harness-section8.mjs`, `validate-harness-premerge.mjs`, and the DEL-09-05 CI workflow. No former provenance-summary result is a current pass. D-APP-38 MATCH remains historical.

### CLM-005 — Construction

> ##### Construction
>
> This deliverable should be implemented as a preservation-oriented test suite and validation wrapper guard, not as new harness feature implementation. The relevant construction surfaces are:
>
> - `frontend/package.json` script entries for `harness:validate:section8` and `harness:validate:premerge`.
> - `frontend/scripts/validate-harness-section8.mjs` for Section 8 scenario execution and summary generation.
> - `frontend/scripts/validate-harness-premerge.mjs` for required test ID enforcement, legacy ID exclusion, and stable summary artifact copying.
> - `.github/workflows/harness-premerge.yml` for CI readiness polling, wrapper execution, artifact verification, and upload.
> - `frontend/artifacts/harness/section8/latest/summary.json` as the stable local artifact produced by the premerge wrapper.
>

### CLM-006 — References

> ##### References
>
> - `docs/SPEC.md` Sections 19.1 and 19.2.
> - `docs/PRD.md` Sections 12.2 and 12.3; FR-066 and FR-068.
> - `docs/CONTRACT.md` K-VALIDATE-1.
> - `docs/TYPES.md` Section 12.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 7, 8, 10A.
> - `frontend/package.json`.
> - `frontend/scripts/validate-harness-premerge.mjs`.
> - `frontend/scripts/validate-harness-section8.mjs`.
> - `.github/workflows/harness-premerge.yml`.
> - `frontend/artifacts/harness/section8/latest/summary.json (candidate-bound result required)`.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-09-01 Section 8 Harness Validation Preservation

> #### Specification: DEL-09-01 Section 8 Harness Validation Preservation
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-008 — Scope

> ##### Scope
>
> DEL-09-01 covers preservation of the existing Section 8 harness validation surface, current local checks, and stable premerge summary behavior for PKG-09. It includes test runner preservation tests and premerge summary checks.
>
> Out of scope:
>
> - Feature implementation except test fixtures and packaging glue. Source: `_CONTEXT.md` Package Scope.
> - Section 9 runtime validation additions, except where Section 8 preservation must leave room for the Section 9 IDs listed by SPEC and PRD. Source: `docs/SPEC.md` Sections 19.2 and 19.3; `docs/PRD.md` Sections 12.3 and 12.4.
> - New professional approval, code compliance, external validation, or solver-truth claims. Source: `docs/CONTRACT.md` K-PROF-1 and K-DOMAIN-4.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL-09-01-REQ-001 | The frontend package must expose `harness:validate:section8` and `harness:validate:premerge` scripts. | `frontend/package.json` scripts | Inspect package scripts; execute wrapper in local/CI validation. |
> | DEL-09-01-REQ-002 | Required local release-significant checks must include `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, and `npm run instruction-root:integrity` from `frontend/`. | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1 | Release checklist and CI/premerge run records cite command outcomes. |
> | DEL-09-01-REQ-003 | The premerge wrapper must fail if `frontend/scripts/validate-harness-section8.mjs` is missing or unreadable. | `frontend/scripts/validate-harness-premerge.mjs` ensureReadableFile/scriptPath branch | Unit or script-level test covers missing script behavior, or wrapper execution proves readable script. |
> | DEL-09-01-REQ-004 | The registered premerge wrapper must preserve these Section 8 IDs as structural baseline/compatibility checks, without treating them as a blanket live Codex gate: `setup.server_reachable`, `regression.session_crud`, `section8.boot_error_taxonomy`, `section8.smoke_stream`, `section8.session_persistence_resume`, `section8.permissions_dontask`, `section8.interrupt_sigint`, `section8.sdk_native_stream`. | `frontend/scripts/validate-harness-premerge.mjs` REQUIRED_TEST_IDS; `frontend/scripts/validate-harness-section8.mjs` REQUIRED_CHECK_ORDER | Wrapper parses summary results and fails on missing IDs. |
> | DEL-09-01-REQ-005 | The premerge wrapper must reject the legacy removed ID `regression.api_chat_reachability` if it appears in the summary. | `frontend/scripts/validate-harness-premerge.mjs` LEGACY_REMOVED_TEST_ID | Deterministic wrapper fixture or script-level test verifies legacy-ID rejection without relying only on an end-to-end CI run. |
> | DEL-09-01-REQ-006 | `npm run harness:validate:premerge` must create or update `frontend/artifacts/harness/section8/latest/summary.json`. | `docs/PRD.md` FR-066; `frontend/scripts/validate-harness-premerge.mjs` stableArtifactPath; `.github/workflows/harness-premerge.yml` Verify stable summary artifact | Local command and CI workflow verify artifact readability. |
> | DEL-09-01-REQ-007 | CI premerge validation must run the wrapper after server readiness and upload the stable summary artifact. | `.github/workflows/harness-premerge.yml` | Pull request or workflow dispatch run verifies readiness poll, wrapper execution, artifact check, and upload step. |
> | DEL-09-01-REQ-008 | Section 8 validation shall preserve its registered baseline scenarios and summary IDs, including retained SDK-native/permission/interrupt checks. Each current Codex/Runtime reachability, ordering, permission, interrupt and resume obligation requires its own mapped source-bound result; retained IDs do not prove native qualification. | `docs/SPEC.md` Section 19.2; `docs/PRD.md` Section 12.3 | Required test IDs and summary content map to the listed behavior. |
> | DEL-09-01-REQ-009 | Unknown or unsupported factual details in validation preservation documents must remain `TBD`, `ASSUMPTION`, or conflict entries rather than invented requirements. | `docs/CONTRACT.md` K-INVENT-1; `skills/four-documents/SKILL.md` source-grounding rule | Document review checks for unsupported claims. |
> | DEL-09-01-REQ-010 | Current source reliance MUST verify the candidate PRD bytes and record mismatch or authorized bypass; the earlier D-APP-38 MATCH is historical and grants no current corpus re-pin. | Invoker runtime instruction; `_REFERENCES.md` REF-006 | Run record and documents record the warning without treating PRD as absent. — reconciled under D-APP-38 |
>

### CLM-010 — Standards

> ##### Standards
>
> - `docs/SPEC.md` is authoritative for validation checklist surfaces and Section 8/9 validation IDs.
> - `docs/PRD.md` is authoritative for product requirements and acceptance criteria, with the run-specific source warning that its observed SHA256 does not match `_REFERENCES.md`.
> - `docs/CONTRACT.md` is authoritative for invariant K-VALIDATE-1 and no-invention discipline.
> - `docs/TYPES.md` is authoritative for release and validation vocabulary.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` is authoritative for the DEL-09-01 package/deliverable assignment and SOW/objective mapping.
>

### CLM-011 — Verification

> ##### Verification
>
> | Requirement | Verification approach |
> |---|---|
> | DEL-09-01-REQ-001 through DEL-09-01-REQ-006 | Static review of `frontend/package.json` and validation scripts plus local execution of `npm run harness:validate:premerge` from `frontend/`; wrapper fixture tests should also cover missing required IDs and legacy-ID rejection deterministically. |
> | DEL-09-01-REQ-007 | CI workflow run on pull request or manual dispatch. |
> | DEL-09-01-REQ-008 | Compare required test IDs and Section 8 summary rows against SPEC/PRD behavior list. |
> | DEL-09-01-REQ-009 | Human review of document kit and test changes for unsupported facts. |
> | DEL-09-01-REQ-010 | Current source reliance MUST verify the candidate PRD bytes and record mismatch or authorized bypass; the earlier D-APP-38 MATCH is historical and grants no current corpus re-pin. |
>
> Current acceptance evidence boundary: the provenance summary can show expected Section 8 summary shape and the eight-row ID set, but current acceptance requires fresh evidence from `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `npm run instruction-root:integrity`, and, for desktop release packaging context, `npm run desktop:dist`. This deliverable records those evidence expectations without asserting that the commands passed in the current working tree.
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required artifacts for this deliverable:
>
> - Section 8 validation preservation tests.
> - Premerge summary checks.
> - Evidence of stable summary artifact generation at `frontend/artifacts/harness/section8/latest/summary.json`.
> - CI artifact upload evidence for the current `harness-validation-summaries` bundle.
> - Any residual `TBD`, `ASSUMPTION`, or source-warning notes carried forward into closure.
>

### CLM-013 — D-APP-56 CI ownership amendment (2026-07-12)

> ##### D-APP-56 CI ownership amendment (2026-07-12)
>
> R4-P37 assigns the repo-root CI workflow and uploaded validation-artifact ownership to DEL-09-05. DEL-09-01 retains a narrowed requirement that the CI validation chain preserve Section 8 through the release-quality wrapper: `.github/workflows/harness-premerge.yml` invokes `npm run validate:release-quality`, which invokes the premerge/Section 8 validation, and uploads `harness-validation-summaries`. DEL-09-01 does not own the workflow.

- **AC-001** — The DEL-09-01 preservation contract retains registered local-check and Section 8 structural coverage, retired-ID exclusion and a stable summary artifact. Acceptance records the actual checked candidate and separates retained compatibility rows from distinct current Codex/Runtime evidence; no blanket legacy-suite pass or unproved equivalence qualifies the live path.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-09-01 Section 8 Harness Validation Preservation

> #### Procedure: DEL-09-01 Section 8 Harness Validation Preservation
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define the operating procedure for preserving and verifying Section 8 harness validation behavior and stable premerge summary output for DEL-09-01.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> - Work from the repository root with frontend dependencies installed under `frontend/`.
> - The frontend server must be reachable at `HARNESS_BASE_URL`, defaulting to `http://127.0.0.1:3000`, before Section 8 validation runs.
> - `frontend/scripts/validate-harness-section8.mjs` must exist and be readable.
> - `frontend/package.json` must expose `harness:validate:section8` and `harness:validate:premerge`.
> - Current extracted dependency context records active upstream anchors for PKG-09, SOW-035, SOW-036, and OBJ-008, plus execution prerequisites for required local checks, `frontend/package.json`, `frontend/scripts/validate-harness-section8.mjs`, and `HARNESS_BASE_URL`. Closure remains `TBD` until dependency closure accepts the register. Source: `_DEPENDENCIES.md` Extracted Dependency Register and Lifecycle Summary.
> - REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes.
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Confirm the validation script surface.
>    - Inspect `frontend/package.json` for `harness:validate:section8` and `harness:validate:premerge`.
>    - Inspect `frontend/scripts/validate-harness-premerge.mjs` for `REQUIRED_TEST_IDS`, `LEGACY_REMOVED_TEST_ID`, and stable artifact path.
>
> 2. Start or verify the harness server.
>    - For local runs, establish the application-owned Runtime service/project binding and start the Next.js server through the supported workflow; record the binding and readiness result.
>    - For CI, preserve the readiness poll against `/api/harness/session/list?projectRoot=/tmp` before running the wrapper.
>
> 3. Run the premerge wrapper from `frontend/`.
>    - Command: `npm run harness:validate:premerge`.
>    - The wrapper should invoke `frontend/scripts/validate-harness-section8.mjs`.
>
> 4. Verify the Section 8 summary contents.
>    - Confirm status is `pass`.
>    - Confirm all required IDs are present:
>      - `setup.server_reachable`
>      - `regression.session_crud`
>      - `section8.boot_error_taxonomy`
>      - `section8.smoke_stream`
>      - `section8.session_persistence_resume`
>      - `section8.permissions_dontask`
>      - `section8.interrupt_sigint`
>      - `section8.sdk_native_stream`
>    - Confirm `regression.api_chat_reachability` is absent.
>    - Where practical, preserve deterministic fixture coverage for a missing required ID and for the retired legacy ID so those failure paths do not depend solely on a live CI run.
>
> 5. Verify stable artifact placement.
>    - Confirm `frontend/artifacts/harness/section8/latest/summary.json` exists and is readable after the wrapper completes.
>    - In CI, confirm the workflow uploads the same path as `harness-validation-summaries`.
>
> 6. Preserve required local checks for release-significant changes.
>    - Run or require evidence for:
>      - `npm run test`
>      - `npm run typecheck`
>      - `npm run harness:validate:premerge`
>      - `npm run instruction-root:integrity`
>    - Packaging release context additionally requires `npm run desktop:dist`.
>
> 7. Record outcomes.
>    - Capture command status, summary path, test count, any missing IDs, and the evidence location for each required local check.
>    - Record `TBD`, `ASSUMPTION`, or source-warning items instead of filling unsupported facts.
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Expected result | Source |
> |---|---|---|
> | Wrapper script exists | `frontend/scripts/validate-harness-premerge.mjs` readable | `frontend/scripts/validate-harness-premerge.mjs` |
> | Section 8 script exists | `frontend/scripts/validate-harness-section8.mjs` readable | `frontend/scripts/validate-harness-premerge.mjs` |
> | Required IDs | All eight accepted Section 8 IDs present | `frontend/scripts/validate-harness-premerge.mjs`; `docs/SPEC.md` Section 19.2 |
> | Legacy ID | `regression.api_chat_reachability` absent | `frontend/scripts/validate-harness-premerge.mjs` |
> | Stable summary | `frontend/artifacts/harness/section8/latest/summary.json` exists | `docs/PRD.md` FR-066; `.github/workflows/harness-premerge.yml` |
> | CI upload | `harness-validation-summaries` artifact uploaded from stable summary path | `.github/workflows/harness-premerge.yml` |
>

### CLM-019 — Records

> ##### Records
>
> - Local command transcript or CI job log for `npm run harness:validate:premerge`.
> - Stable summary JSON at `frontend/artifacts/harness/section8/latest/summary.json`.
> - CI artifact named `harness-validation-summaries`.
> - Any preservation test fixture outputs proving missing-ID rejection and legacy-ID rejection.
> - Current-run evidence for `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `npm run instruction-root:integrity`, and release-context `npm run desktop:dist` when desktop packaging acceptance is in scope.
> - REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes.

- **VER-001** — Inspect the source-bound contract and current run evidence for the required local checks; confirm the accepted Section 8 IDs, absence of the retired legacy ID, and readable stable summary artifact.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-09-01 Section 8 Harness Validation Preservation

> #### Guidance: DEL-09-01 Section 8 Harness Validation Preservation
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-021 — Purpose

> ##### Purpose
>
> DEL-09-01 exists to preserve the existing harness validation baseline while vNext runtime work proceeds. The deliverable should make it difficult for future changes to accidentally remove Section 8 coverage, rename the stable premerge artifact, reintroduce a retired legacy test ID, or let CI pass without the expected summary JSON.
>

### CLM-022 — Principles

> ##### Principles
>
> - Treat Section 8 as baseline preservation. New runtime behavior belongs in Section 9 validation unless the accepted sources explicitly amend Section 8.
> - Keep the premerge wrapper strict about summary shape and required IDs. This is the current enforcement point for `docs/PRD.md` FR-066 and `docs/CONTRACT.md` K-VALIDATE-1.
> - Preserve stable artifact location. CI and local workflows rely on `frontend/artifacts/harness/section8/latest/summary.json`.
> - Prefer deterministic validation scripts over manual inspection wherever possible. This follows `docs/DIRECTIVE.md` deterministic validation guidance and the existing frontend scripts.
> - Keep PRD historical D-APP-38 source state; verify current candidate bytes visible but non-blocking for this run, per invoker instruction. (reconciled under D-APP-38).
> - Do not treat a passing historical provenance summary as proof that current code still passes. It is useful evidence of the expected summary shape and ID set, not a substitute for rerunning validation.
> - Keep DEL-09-01 limited to preserving Section 8 baseline behavior. Section 9 runtime validation IDs, broader runtime additions, and release workflow expansion belong to DEL-09-02 and related PKG-09 deliverables unless accepted sources move that scope here.
>

### CLM-023 — Considerations

> The operative repository-root CI chain is owned by DEL-09-05 and publishes `harness-validation-summaries`. Confirm its actual run and candidate before relying on Section 8 or release-quality summaries; controlled CI and production Codex/native outcomes are distinct. Missing-ID negative fixtures and current post-A2 results remain open. `section8.sdk_native_stream` still checks the browser UIEvent envelope: full Codex notifications may be carried inside `harness:event`; the envelope itself is not retired. Preserve unfamiliar notifications and server-request handling under D-GOV-43. A named hook or historical stable summary is not a new test result.

### CLM-024 — Trade-offs

> ##### Trade-offs
>
> | Topic | Option | Trade-off |
> |---|---|---|
> | Required ID enforcement | Hard-code accepted Section 8 IDs in the wrapper | Strong regression protection, but source documents and script constants must be updated together if Section 8 scope changes. |
> | Stable artifact path | Preserve `frontend/artifacts/harness/section8/latest/summary.json` | Supports CI upload and downstream tooling; requires care to avoid stale artifact confusion. |
> | Historical summary evidence | Use provenance summary as shape evidence only | Avoids overstating stale evidence; requires reruns for current acceptance. |
> | Section 9 additions | Keep out of DEL-09-01 except compatibility awareness | Keeps this deliverable focused; future runtime validation must be handled by DEL-09-02 and related packages. |
>

### CLM-025 — Examples

> ##### Examples
>
> - Supported preservation check: assert that `validate-harness-premerge.mjs` fails when a required Section 8 ID is absent from a summary fixture.
> - Supported preservation check: assert that `validate-harness-premerge.mjs` fails if `regression.api_chat_reachability` appears in the summary.
> - Supported preservation check: run `npm run harness:validate:premerge` and verify `frontend/artifacts/harness/section8/latest/summary.json` is readable.
> - Not supported without amendment: broadening this deliverable into new Section 9 validation implementation.
>

### CLM-026 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | None | REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes. | `_REFERENCES.md` REF-006; invoker instruction | N/A | Datasheet Conditions; Specification Requirements; run record | Treat PRD as accessible with warning for this run. | TBD — reconciled under D-APP-38 |
>

### CLM-027 — Source Warnings

> Earlier drafting source-state conflicts are historical at their recorded basis. Current reliance requires candidate-bound source verification through `execution/_Scripts/references_hash_tool.py`, with actual mismatch or authorized bypass retained. D-APP-38 did not guarantee perpetual MATCH. Apply settled D-GOV-43/D-APP-127 direction and retain substantive implementation/evidence gaps in Remaining; this record neither re-pins an accepted source nor certifies a new product result.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-035 SOW-036 OBJ-008 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
