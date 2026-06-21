# Specification: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

## Scope

This deliverable defines validation checks for the security-sensitive surfaces named by DEL-09-06: renderer outbound network allowlisting, API key storage/redaction, Anthropic provider endpoint policy, and attachment validation/retry behavior.

In scope:

- Security tests and network guard tests for renderer and provider policy.
- Attachment resolver validation for server-side file checks and failure behavior.
- Key storage and redaction checks proving key material remains non-project convenience state.
- Evidence sufficient to support PKG-09 security validation without a release-readiness claim.

Out of scope:

- Feature implementation except test fixtures and packaging glue, per PKG-09 package exclusions.
- Broader network enablement, remote MCP, plugins, or non-Anthropic network tools without governed future scope.
- Assignment of `ResponsibleParty`; it remains `TBD`.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| DEL-09-06-REQ-001 | API key resolution checks shall prove UI safeStorage precedence, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | Automated key storage/resolution tests. |
| DEL-09-06-REQ-002 | Key material shall not be written to working root, project docs, logs, runtime event payloads, git-tracked execution files, or tool artifacts. | Redaction/storage tests and fixture scan. |
| DEL-09-06-REQ-003 | Key material shall be stored with Electron `safeStorage` at `app.getPath('userData')/credentials/api-key.enc` when stored through UI. | Key storage tests or integration fixture. |
| DEL-09-06-REQ-004 | Anthropic base URL validation shall accept only `https://api.anthropic.com` with no credentials and port empty or 443. | Provider endpoint policy tests. |
| DEL-09-06-REQ-005 | Electron renderer outbound traffic shall be blocked except loopback and Anthropic API. | Renderer network guard tests using `webRequest.onBeforeRequest` behavior or equivalent test seam. |
| DEL-09-06-REQ-006 | Renderer network policy logs shall include policy metadata without secrets. | Network guard log redaction assertions. |
| DEL-09-06-REQ-007 | Node/SDK provider calls shall not silently broaden the product network policy. | Provider policy tests and SDK handoff assertions. |
| DEL-09-06-REQ-008 | Attachment validation shall treat client metadata as non-authoritative and revalidate path, extension, file type, readability, symlink status, regular-file status, and size. | Attachment resolver validation tests. |
| DEL-09-06-REQ-009 | Attachment resolver checks shall reject symlinks, directories, special files, unsupported extensions, unreadable files, files over 10 MB, and turns over 18 MB raw bytes. | Resolver negative-case fixtures. |
| DEL-09-06-REQ-010 | Supported attachment extensions shall include `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, and `.csv`. | Resolver allowlist tests. |
| DEL-09-06-REQ-011 | Partial attachment failure shall be non-fatal when executable content remains. | Route or resolver integration tests. |
| DEL-09-06-REQ-012 | Total attachment failure with empty text shall reject the turn with `ATTACHMENT_FAILURE`. | Route or resolver integration tests. |
| DEL-09-06-REQ-013 | UI-facing retry behavior shall preserve draft and attachments on failed send where attachment failure recovery is exercised. | UI or integration retry-preservation tests. |
| DEL-09-06-REQ-014 | Required local checks must remain explicit and repeatable before security-significant evidence acceptance. | CI/premerge validation evidence. |
| DEL-09-06-REQ-015 | Security-significant evidence shall include the source-named validation command family where applicable: `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist`; exact package-script spelling and output artifact paths remain `TBD` until implementation locations are selected. | Command output or CI artifact references tied to the selected implementation targets. |

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| Product PRD security requirements | Governs FR-030 through FR-040 and NFR-002 through NFR-004. | `docs/PRD.md` Sections 8.5, 8.6, 11.1; hash mismatch warning applies |
| Runtime/API specification | Governs attachment, key, and network mechanics. | `docs/SPEC.md` Section 16 |
| Contract invariants | Governs security invariants for network, keys, attachments, and validation. | `docs/CONTRACT.md` K-NET-1, K-KEY-1, K-ATTACH-1, K-VALIDATE-1 |
| SOFTWARE_DECOMP v3.2 | Defines deliverable scope and SOW/objective mapping. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-06 |

## Verification

| Requirement IDs | Verification Approach | Evidence Artifact |
|---|---|---|
| REQ-001, REQ-002, REQ-003 | Unit/integration tests for key precedence, safeStorage use, environment fallback, and redaction. | Key storage checks; redaction fixtures |
| REQ-004, REQ-007 | Unit/integration tests for base URL allowlist and SDK/provider endpoint handoff. | Provider endpoint policy tests |
| REQ-005, REQ-006 | Electron network guard tests for allowed and denied URLs plus secret-free policy logs. | Network guard tests |
| REQ-008, REQ-009, REQ-010 | Attachment resolver tests covering positive and negative file cases. | Attachment resolver validation |
| REQ-011, REQ-012, REQ-013 | Route/UI integration tests for partial failure, total failure, and retry preservation. | Attachment retry/failure tests |
| REQ-014, REQ-015 | Security-validation command output, including the source-named command family where applicable. | Premerge validation evidence; exact test file paths, package-script aliases, and artifact paths `TBD` |

## Documentation

Required output evidence for this deliverable:

- Security tests.
- Network guard tests.
- Attachment resolver validation.
- Key storage checks.
- C-001: exact test file paths and command names for key, provider, renderer, attachment, and retry checks remain `TBD` until implementation locations are confirmed.
- D-001: current-run security-validation output remains `TBD`; the source-named command family is `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist` where applicable.

## Pass 3 Disposition Notes

| ItemID | Disposition |
|---|---|
| C-001 | Converted to explicit `TBD` slots for exact test file paths and command names rather than inventing implementation locations. |
| D-001 | Incorporated the source-named validation command family while retaining current-run output and exact artifact paths as `TBD`. |
