# Procedure: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

## Purpose

Produce and verify the DEL-09-06 security-control evidence set for renderer network allowlisting, API key storage/redaction, provider endpoint policy, and attachment validation/retry behavior.

## Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Accessible source corpus for DEL-09-06 | Available via `_REFERENCES.md`; PRD hash mismatch treated as source warning only |
| ResponsibleParty | TBD |
| Declared upstream dependencies | TBD; `_DEPENDENCIES.md` has no accepted dependency edges yet |
| Test framework and exact command names | TBD; source corpus requires repeatable local checks but this deliverable folder does not identify exact commands |
| Implementation paths for renderer guard, provider policy, key storage, and attachment resolver | TBD |
| Implementation target slots | F-001 keeps renderer network guard, provider base URL validation, API key storage/resolution, redaction helper/logger, attachment resolver, and route/UI failure handling paths as explicit `TBD` slots until selected by implementation work. |
| Release-readiness command evidence | D-001 requires current-run command output or CI artifact references for the selected validation command family; exact output paths remain `TBD`. |

## Steps

1. Confirm scope and source state.
   - Verify DEL-09-06 covers SOW-019, SOW-020, SOW-022, and SOW-023.
   - Record the PRD hash mismatch as a warning, not a blocker, for this run.

2. Identify implementation targets.
   - Locate the renderer network guard, provider base URL validation, API key storage/resolution, redaction helper/logger, attachment resolver, and route/UI failure handling code.
   - If a target cannot be located, mark the related test path `TBD` rather than inventing a path.
   - Preserve the following implementation target path slots until confirmed: renderer network guard path `TBD`; provider base URL policy path `TBD`; API key storage/resolution path `TBD`; redaction helper/logger path `TBD`; attachment resolver path `TBD`; route/UI failure handling path `TBD`.

3. Build API key security checks.
   - Test UI safeStorage precedence over environment fallback.
   - Test fallback to `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`.
   - Test no key material is written to working root, project docs, logs, runtime event payloads, git-tracked execution files, or tool artifacts.
   - Test key status reports only non-secret source values: `ui`, `env`, or `none`.

4. Build provider endpoint checks.
   - Accept only `https://api.anthropic.com` with no credentials and port empty or 443.
   - Reject credentials, alternate hosts, alternate schemes, and non-empty non-443 ports.
   - Verify provider/SDK calls do not broaden network policy silently.

5. Build renderer network guard checks.
   - Test loopback traffic is allowed where product policy permits it.
   - Test Anthropic API traffic is allowed where product policy permits it.
   - Test non-loopback/non-Anthropic renderer requests are cancelled.
   - Assert policy logs contain no key material or secrets.

6. Build attachment resolver checks.
   - Test supported extensions: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, and `.csv`.
   - Test path validation, regular-file status, symlink rejection, extension allowlist, file-type validation, readability, 10 MB per-file limit, and 18 MB total raw-byte limit.
   - Test directories, special files, unsupported extensions, unreadable files, symlinks, and over-budget files fail before provider execution.

7. Build attachment failure/retry checks.
   - Test partial attachment failure is non-fatal when executable content remains.
   - Test all attachments failing with empty text returns `ATTACHMENT_FAILURE`.
   - Test failed send preserves draft and attachments for retry where the UI participates.

8. Run repeatable validation.
   - Execute the relevant unit/API/integration tests.
   - Execute release-significant premerge checks where applicable, including `npm run test`, `npm run typecheck`, `npm run harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist` when those source-named checks apply to the selected implementation surface.
   - Record command output paths or summaries in the deliverable evidence location selected by the implementation task.

## Verification

| Check | Pass Criteria | Source |
|---|---|---|
| API key precedence | UI safeStorage, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | `docs/PRD.md` FR-030 |
| API key secrecy | Key material absent from project files, logs, runtime events, and tool artifacts. | `docs/PRD.md` FR-031; `docs/CONTRACT.md` K-KEY-1 |
| Base URL allowlist | Only accepted Anthropic URL form passes. | `docs/PRD.md` FR-032 |
| Renderer network allowlist | Non-loopback/non-Anthropic renderer requests are canceled. | `docs/PRD.md` FR-033; `docs/SPEC.md` Section 16.3 |
| Attachment validation | Server revalidates client metadata and rejects unsupported or unsafe files. | `docs/PRD.md` FR-037; `docs/SPEC.md` Section 16.1 |
| Attachment budgets | 10 MB per file and 18 MB per turn raw-byte limits enforced. | `docs/SPEC.md` Section 16.1 |
| Attachment failure handling | Partial failures can proceed; total failure with empty text returns `ATTACHMENT_FAILURE`; retry state is preserved where UI is involved. | `docs/PRD.md` FR-040; `docs/SPEC.md` Section 16.1 |

## Records

- Security tests.
- Network guard tests.
- Attachment resolver validation.
- Key storage checks.
- Provider endpoint policy tests.
- Redaction fixtures or scan output.
- Validation command output or CI artifact reference.
- X-001: exact artifact paths remain `TBD` for security tests, network guard tests, attachment resolver validation, key storage checks, provider policy tests, redaction fixtures, and validation command output until implementation locations and test commands are selected.

## Pass 3 Disposition Notes

| ItemID | Disposition |
|---|---|
| F-001 | Converted to explicit implementation target path slots, all retained as `TBD` pending implementation-owner selection. |
| X-001 | Converted to explicit evidence artifact path slots, all retained as `TBD` pending validation run and artifact-location selection. |
