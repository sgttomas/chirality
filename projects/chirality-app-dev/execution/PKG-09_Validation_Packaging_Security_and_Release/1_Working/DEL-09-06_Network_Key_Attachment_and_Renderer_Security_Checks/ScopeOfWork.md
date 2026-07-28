---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-06
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-019, SOW-020, SOW-022, SOW-023]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-06

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-06` in service of project scope [SOW-019, SOW-020, SOW-022, SOW-023] and package objectives [OBJ-008].

- **OUT-001** — A security-control evidence set covering renderer network allowlisting, Anthropic provider endpoint policy, API key storage, resolution and redaction, attachment validation and budgets, partial and total attachment failure behavior, retry preservation, and repeatable security-significant validation.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Datasheet: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-09-06 |
> | DeliverableName | Network, Key, Attachment, and Renderer Security Checks |
> | PackageID | PKG-09 |
> | PackageName | Validation, Packaging, Security, and Release |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | SECURITY_CONTROL |
> | ContextEnvelope | M |
> | ResponsibleParty | TBD |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary scope | Verify renderer allowlist, API key redaction/storage, provider endpoint policy, and attachment validation/retry behavior. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-06 |
> | Covered SOW items | SOW-019, SOW-020, SOW-022, SOW-023 | `_CONTEXT.md` Traceability; decomposition DEL-09-06 |
> | Supported objective | OBJ-008 | `_CONTEXT.md` Traceability; decomposition objective mapping |
> | Anticipated artifacts | Security tests; network guard tests; attachment resolver validation; key storage checks | `_CONTEXT.md` Anticipated Artifacts |
> | API key resolution order | UI safeStorage key first, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | `docs/PRD.md` Section 8.5, FR-030 |
> | API key storage path | `app.getPath('userData')/credentials/api-key.enc` | `docs/SPEC.md` Section 16.2 |
> | Allowed Anthropic base URL | `https://api.anthropic.com` with no credentials and port empty or 443. | `docs/PRD.md` Section 8.5, FR-032 |
> | Renderer network allowlist | Loopback plus Anthropic API path. | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1 |
> | Supported attachment extensions | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, `.csv` | `docs/SPEC.md` Section 16.1 |
> | Attachment size limits | 10 MB per file; 18 MB total raw bytes per turn. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` Section 8.6, FR-038 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Source warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | Assignment instruction; `_REFERENCES.md` REF-006 — reconciled under D-APP-38 |
> | Pass 3 source-state disposition | B-001 preserves REF-006 as warning-only source tension for all PRD-grounded security checks until a later human/source ruling records otherwise. | `_REFERENCES.md` REF-006; `Guidance.md` Conflict Table |
> | Security posture | API keys are non-project convenience state and must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` NFR-002 |
> | Attachment trust boundary | Client attachment metadata is non-authoritative; server revalidates attachment properties. | `docs/PRD.md` Section 8.6, FR-037; `docs/CONTRACT.md` K-ATTACH-1 |
> | Failure handling | Partial attachment failure is non-fatal when executable content remains; all attachments failing with empty text returns `ATTACHMENT_FAILURE`. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` Section 8.6, FR-040 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected Check Coverage | Source |
> |---|---|---|
> | Renderer network guard | Tests showing non-loopback/non-Anthropic renderer requests are cancelled and policy metadata excludes secrets. | `docs/PRD.md` FR-033; `docs/PRD.md` NFR-003 |
> | Provider endpoint policy | Tests showing accepted and rejected Anthropic base URL variants. | `docs/PRD.md` FR-032 |
> | API key storage and handoff | Tests showing safeStorage precedence, environment fallback, no project writes, and redacted logs/events. | `docs/PRD.md` FR-030, FR-031; `docs/SPEC.md` Section 16.2 |
> | Attachment resolver | Tests for path validation, regular-file check, symlink rejection, extension allowlist, readability, and byte budgets. | `docs/SPEC.md` Section 16.1 |
> | Retry behavior | Tests showing UI preserves draft/attachments after failed send where source scope requires retry preservation. | `docs/PRD.md` FR-040 |
>

### CLM-006 — References

> ##### References
>
> | RefID | Path | Status | Use |
> |---|---|---|---|
> | REF-002 | `docs/CONTRACT.md` | MATCH | Invariants K-NET-1, K-KEY-1, K-ATTACH-1, K-VALIDATE-1 |
> | REF-003 | `docs/SPEC.md` | MATCH | Section 16 attachment, API key, and network policy mechanics |
> | REF-005 | `docs/PLAN.md` | MATCH | Implementation sequencing context for key handoff and validation |
> | REF-006 | `docs/PRD.md` | MATCH status | Product requirements FR-030 through FR-040 and NFR security/privacy requirements — reconciled under D-APP-38 |
> | DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | accessible | DEL-09-06 scope and SOW/objective mapping |
>

### CLM-007 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | B-001 | Incorporated as an explicit warning-only source-state condition; no PRD-derived value was promoted beyond the existing REF-006 warning. |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Specification: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable defines validation checks for the security-sensitive surfaces named by DEL-09-06: renderer outbound network allowlisting, API key storage/redaction, Anthropic provider endpoint policy, and attachment validation/retry behavior.
>
> In scope:
>
> - Security tests and network guard tests for renderer and provider policy.
> - Attachment resolver validation for server-side file checks and failure behavior.
> - Key storage and redaction checks proving key material remains non-project convenience state.
> - Evidence sufficient to support PKG-09 security validation without a release-readiness claim.
>
> Out of scope:
>
> - Feature implementation except test fixtures and packaging glue, per PKG-09 package exclusions.
> - Broader network enablement, remote MCP, plugins, or non-Anthropic network tools without governed future scope.
> - Assignment of `ResponsibleParty`; it remains `TBD`.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-09-06-REQ-001 | API key resolution checks shall prove UI safeStorage precedence, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | Automated key storage/resolution tests. |
> | DEL-09-06-REQ-002 | Key material shall not be written to working root, project docs, logs, runtime event payloads, git-tracked execution files, or tool artifacts. | Redaction/storage tests and fixture scan. |
> | DEL-09-06-REQ-003 | Key material shall be stored with Electron `safeStorage` at `app.getPath('userData')/credentials/api-key.enc` when stored through UI. | Key storage tests or integration fixture. |
> | DEL-09-06-REQ-004 | Anthropic base URL validation shall accept only `https://api.anthropic.com` with no credentials and port empty or 443. | Provider endpoint policy tests. |
> | DEL-09-06-REQ-005 | Electron renderer outbound traffic shall be blocked except loopback and Anthropic API. | Renderer network guard tests using `webRequest.onBeforeRequest` behavior or equivalent test seam. |
> | DEL-09-06-REQ-006 | Renderer network policy logs shall include policy metadata without secrets. | Network guard log redaction assertions. |
> | DEL-09-06-REQ-007 | Node/SDK provider calls shall not silently broaden the product network policy. | Provider policy tests and SDK handoff assertions. |
> | DEL-09-06-REQ-008 | Attachment validation shall treat client metadata as non-authoritative and revalidate path, extension, file type, readability, symlink status, regular-file status, and size. | Attachment resolver validation tests. |
> | DEL-09-06-REQ-009 | Attachment resolver checks shall reject symlinks, directories, special files, unsupported extensions, unreadable files, files over 10 MB, and turns over 18 MB raw bytes. | Resolver negative-case fixtures. |
> | DEL-09-06-REQ-010 | Supported attachment extensions shall include `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, and `.csv`. | Resolver allowlist tests. |
> | DEL-09-06-REQ-011 | Partial attachment failure shall be non-fatal when executable content remains. | Route or resolver integration tests. |
> | DEL-09-06-REQ-012 | Total attachment failure with empty text shall reject the turn with `ATTACHMENT_FAILURE`. | Route or resolver integration tests. |
> | DEL-09-06-REQ-013 | UI-facing retry behavior shall preserve draft and attachments on failed send where attachment failure recovery is exercised. | UI or integration retry-preservation tests. |
> | DEL-09-06-REQ-014 | Required local checks must remain explicit and repeatable before security-significant evidence acceptance. | CI/premerge validation evidence. |
> | DEL-09-06-REQ-015 | Security-significant evidence shall include the source-named validation command family where applicable: `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist`; exact package-script spelling and output artifact paths remain `TBD` until implementation locations are selected. | Command output or CI artifact references tied to the selected implementation targets. |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Source | Applicability | Location |
> |---|---|---|
> | Product PRD security requirements | Governs FR-030 through FR-040 and NFR-002 through NFR-004. | `docs/PRD.md` Sections 8.5, 8.6, 11.1; hash status: MATCH status applies — reconciled under D-APP-38 |
> | Runtime/API specification | Governs attachment, key, and network mechanics. | `docs/SPEC.md` Section 16 |
> | Contract invariants | Governs security invariants for network, keys, attachments, and validation. | `docs/CONTRACT.md` K-NET-1, K-KEY-1, K-ATTACH-1, K-VALIDATE-1 |
> | SOFTWARE_DECOMP v3.2 | Defines deliverable scope and SOW/objective mapping. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-06 |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement IDs | Verification Approach | Evidence Artifact |
> |---|---|---|
> | REQ-001, REQ-002, REQ-003 | Unit/integration tests for key precedence, safeStorage use, environment fallback, and redaction. | Key storage checks; redaction fixtures |
> | REQ-004, REQ-007 | Unit/integration tests for base URL allowlist and SDK/provider endpoint handoff. | Provider endpoint policy tests |
> | REQ-005, REQ-006 | Electron network guard tests for allowed and denied URLs plus secret-free policy logs. | Network guard tests |
> | REQ-008, REQ-009, REQ-010 | Attachment resolver tests covering positive and negative file cases. | Attachment resolver validation |
> | REQ-011, REQ-012, REQ-013 | Route/UI integration tests for partial failure, total failure, and retry preservation. | Attachment retry/failure tests |
> | REQ-014, REQ-015 | Security-validation command output, including the source-named command family where applicable. | Premerge validation evidence; exact test file paths, package-script aliases, and artifact paths `TBD` |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required output evidence for this deliverable:
>
> - Security tests.
> - Network guard tests.
> - Attachment resolver validation.
> - Key storage checks.
> - C-001: exact test file paths and command names for key, provider, renderer, attachment, and retry checks remain `TBD` until implementation locations are confirmed.
> - D-001: current-run security-validation output remains `TBD`; the source-named command family is `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist` where applicable.
>

### CLM-014 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | C-001 | Converted to explicit `TBD` slots for exact test file paths and command names rather than inventing implementation locations. |
> | D-001 | Incorporated the source-named validation command family while retaining current-run output and exact artifact paths as `TBD`. |

- **AC-001** — Evidence verifies UI safeStorage and environment key precedence without secret leakage, only the accepted Anthropic endpoint and product network scope, secret-free renderer policy logs, server-side attachment type, path, symlink, readability and byte-budget enforcement, partial-failure continuation, ATTACHMENT_FAILURE on total failure with empty text, retry-state preservation where applicable, and repeatable validation; unselected implementation paths and unavailable outputs remain explicit TBD blockers.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Procedure: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>

### CLM-016 — Purpose

> ##### Purpose
>
> Produce and verify the DEL-09-06 security-control evidence set for renderer network allowlisting, API key storage/redaction, provider endpoint policy, and attachment validation/retry behavior.
>

### CLM-017 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Source |
> |---|---|
> | Accessible source corpus for DEL-09-06 | Available via `_REFERENCES.md`; PRD hash mismatch treated as source status |
> | ResponsibleParty | TBD |
> | Declared upstream dependencies | TBD; `_DEPENDENCIES.md` has no accepted dependency edges yet |
> | Test framework and exact command names | TBD; source corpus requires repeatable local checks but this deliverable folder does not identify exact commands |
> | Implementation paths for renderer guard, provider policy, key storage, and attachment resolver | TBD |
> | Implementation target slots | F-001 keeps renderer network guard, provider base URL validation, API key storage/resolution, redaction helper/logger, attachment resolver, and route/UI failure handling paths as explicit `TBD` slots until selected by implementation work. |
> | Security-validation command evidence | D-001 requires current-run command output or CI artifact references for the selected validation command family; exact output paths remain `TBD`. |
>

### CLM-018 — Steps

> ##### Steps
>
> 1. Confirm scope and source state.
>    - Verify DEL-09-06 covers SOW-019, SOW-020, SOW-022, and SOW-023.
>    - Record the PRD hash mismatch as a warning, not a blocker, for this run.
>
> 2. Identify implementation targets.
>    - Locate the renderer network guard, provider base URL validation, API key storage/resolution, redaction helper/logger, attachment resolver, and route/UI failure handling code.
>    - If a target cannot be located, mark the related test path `TBD` rather than inventing a path.
>    - Preserve the following implementation target path slots until confirmed: renderer network guard path `TBD`; provider base URL policy path `TBD`; API key storage/resolution path `TBD`; redaction helper/logger path `TBD`; attachment resolver path `TBD`; route/UI failure handling path `TBD`.
>
> 3. Build API key security checks.
>    - Test UI safeStorage precedence over environment fallback.
>    - Test fallback to `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`.
>    - Test no key material is written to working root, project docs, logs, runtime event payloads, git-tracked execution files, or tool artifacts.
>    - Test key status reports only non-secret source values: `ui`, `env`, or `none`.
>
> 4. Build provider endpoint checks.
>    - Accept only `https://api.anthropic.com` with no credentials and port empty or 443.
>    - Reject credentials, alternate hosts, alternate schemes, and non-empty non-443 ports.
>    - Verify provider/SDK calls do not broaden network policy silently.
>
> 5. Build renderer network guard checks.
>    - Test loopback traffic is allowed where product policy permits it.
>    - Test Anthropic API traffic is allowed where product policy permits it.
>    - Test non-loopback/non-Anthropic renderer requests are cancelled.
>    - Assert policy logs contain no key material or secrets.
>
> 6. Build attachment resolver checks.
>    - Test supported extensions: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, and `.csv`.
>    - Test path validation, regular-file status, symlink rejection, extension allowlist, file-type validation, readability, 10 MB per-file limit, and 18 MB total raw-byte limit.
>    - Test directories, special files, unsupported extensions, unreadable files, symlinks, and over-budget files fail before provider execution.
>
> 7. Build attachment failure/retry checks.
>    - Test partial attachment failure is non-fatal when executable content remains.
>    - Test all attachments failing with empty text returns `ATTACHMENT_FAILURE`.
>    - Test failed send preserves draft and attachments for retry where the UI participates.
>
> 8. Run repeatable validation.
>    - Execute the relevant unit/API/integration tests.
>    - Execute security-significant premerge checks where applicable, including `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist` when those source-named checks apply to the selected implementation surface.
>    - Record command output paths or summaries in the deliverable evidence location selected by the implementation task.
>

### CLM-019 — Verification

> ##### Verification
>
> | Check | Pass Criteria | Source |
> |---|---|---|
> | API key precedence | UI safeStorage, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | `docs/PRD.md` FR-030 |
> | API key secrecy | Key material absent from project files, logs, runtime events, and tool artifacts. | `docs/PRD.md` FR-031; `docs/CONTRACT.md` K-KEY-1 |
> | Base URL allowlist | Only accepted Anthropic URL form passes. | `docs/PRD.md` FR-032 |
> | Renderer network allowlist | Non-loopback/non-Anthropic renderer requests are canceled. | `docs/PRD.md` FR-033; `docs/SPEC.md` Section 16.3 |
> | Attachment validation | Server revalidates client metadata and rejects unsupported or unsafe files. | `docs/PRD.md` FR-037; `docs/SPEC.md` Section 16.1 |
> | Attachment budgets | 10 MB per file and 18 MB per turn raw-byte limits enforced. | `docs/SPEC.md` Section 16.1 |
> | Attachment failure handling | Partial failures can proceed; total failure with empty text returns `ATTACHMENT_FAILURE`; retry state is preserved where UI is involved. | `docs/PRD.md` FR-040; `docs/SPEC.md` Section 16.1 |
>

### CLM-020 — Records

> ##### Records
>
> - Security tests.
> - Network guard tests.
> - Attachment resolver validation.
> - Key storage checks.
> - Provider endpoint policy tests.
> - Redaction fixtures or scan output.
> - Validation command output or CI artifact reference.
> - X-001: exact artifact paths remain `TBD` for security tests, network guard tests, attachment resolver validation, key storage checks, provider policy tests, redaction fixtures, and validation command output until implementation locations and test commands are selected.
>

### CLM-021 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | F-001 | Converted to explicit implementation target path slots, all retained as `TBD` pending implementation-owner selection. |
> | X-001 | Converted to explicit evidence artifact path slots, all retained as `TBD` pending validation run and artifact-location selection. |

- **VER-001** — Run or inspect key precedence and redaction tests, provider endpoint and renderer network-guard tests, attachment allowlist, unsafe-file and budget fixtures, partial and total failure and retry tests, secret scans, and the applicable source-named validation command evidence, retaining unconfirmed paths or artifacts as TBD.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

> #### Guidance: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-023 — Purpose

> ##### Purpose
>
> This deliverable exists to keep validation, packaging, network, key, and instruction-root checks explicit and repeatable for PKG-09 security evidence. Its security checks should demonstrate that key material remains outside project truth, renderer/network access is bounded, provider endpoint selection is constrained, and attachment handling does not rely on client-supplied metadata.
>
> Sources: `_CONTEXT.md` Traceability; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` OBJ-008 and DEL-09-06.
>

### CLM-024 — Principles

> ##### Principles
>
> 1. Runtime code is the security boundary. Prompts and documentation can reinforce policy, but tests should target runtime behavior such as path containment, permission policy, hooks, redaction, and network controls.
>    Source: `docs/PRD.md` Section 4, principles 18-19.
>
> 2. API keys are convenience state, not project truth. Treat any write of key material to working root, runtime events, logs, git-tracked execution files, SDK transcripts if avoidable, or tool artifacts as a security-evidence blocker.
>    Source: `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` FR-031 and NFR-002.
>
> 3. Renderer and provider network checks should be allowlist-oriented. The current shipped network posture is loopback plus Anthropic API path, with broader network access reserved for governed future scope.
>    Source: `docs/CONTRACT.md` K-NET-1; `docs/SPEC.md` Section 16.3.
>
> 4. Anthropic provider access and renderer outbound allowlisting are related but separately enforced surfaces. Provider execution needs the approved Anthropic endpoint, while renderer traffic still needs Electron-level cancellation of non-loopback and non-Anthropic requests; evidence should not treat one control as proof of the other.
>    Source: `docs/PRD.md` FR-032 and FR-033; `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1.
>
> 5. Attachment metadata from the browser is advisory only. Server-side validation must be the authority for path, type, symlink status, readability, regular-file status, and byte budgets.
>    Source: `docs/PRD.md` FR-037; `docs/CONTRACT.md` K-ATTACH-1.
>
> 6. Failure behavior is part of the security surface. Tests should verify that partial attachment failures do not discard executable content and that total attachment failure without text returns the expected typed failure while preserving retry state where the UI is involved.
>    Source: `docs/PRD.md` FR-040; `docs/SPEC.md` Section 16.1.
>

### CLM-025 — Considerations

> ##### Considerations
>
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Keep endpoint tests strict about credentials and ports. `https://api.anthropic.com` with credentials or a non-empty non-443 port is not equivalent to the accepted base URL.
> - Prefer negative tests for sensitive paths: denied network URL, unsupported extension, symlink, directory, over-budget file, unreadable file, and redaction of realistic key-shaped strings.
> - Avoid treating `allowedTools` or SDK permissions alone as sufficient. Chirality-owned overlays remain required for professional safety.
> - Exact implementation file paths are `TBD` until implementation locations are confirmed by the relevant feature deliverables.
>

### CLM-026 — Trade-offs

> ##### Trade-offs
>
> | Topic | Trade-off | Guidance |
> |---|---|---|
> | Unit tests vs integration tests | Unit tests isolate policy logic; integration tests prove route/Electron behavior. | Use both where the surface crosses Electron, SDK provider, or route boundaries. |
> | Redaction assertions | Broad fixture scanning may produce false positives; narrow checks may miss variants. | Include representative key variants and verify both positive redaction and non-secret metadata retention. |
> | Attachment retries | UI retry behavior may sit outside the resolver. | Keep resolver validation separate from route/UI retry preservation so failures are easier to localize. |
> | Network policy | Provider execution requires Anthropic access, while renderer traffic must remain constrained. | Test renderer and Node/SDK provider policy as separate surfaces with a shared policy vocabulary. |
>

### CLM-027 — Examples

> ##### Examples
>
> | Example | Expected Result | Source |
> |---|---|---|
> | Base URL `https://api.anthropic.com` | Accepted when credentials are absent and port is empty or 443. | `docs/PRD.md` FR-032 |
> | Base URL with embedded credentials | Rejected. | `docs/PRD.md` FR-032 |
> | Renderer request to non-loopback, non-Anthropic URL | Cancelled and logged without secrets. | `docs/PRD.md` FR-033 |
> | Attachment path points to symlink | Rejected before provider execution. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` NFR-004 |
> | One attachment fails, text or another valid attachment remains | Turn may proceed with warning. | `docs/SPEC.md` Section 16.1 |
> | All attachments fail and text is empty | Request fails with `ATTACHMENT_FAILURE`. | `docs/SPEC.md` Section 16.1 |
>

### CLM-028 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | TBD | No source-content conflict identified during P1/P2. PRD hash status: MATCH remains a source status. | `_REFERENCES.md` REF-006 | Assignment instruction | All PRD-grounded sections | Treat PRD content as usable with warning for this run. | TBD — reconciled under D-APP-38 |
>

### CLM-029 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition |
> |---|---|
> | E-001 | Incorporated as a rationale principle distinguishing Anthropic provider endpoint access from renderer outbound allowlisting. |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-019 SOW-020 SOW-022 SOW-023 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
