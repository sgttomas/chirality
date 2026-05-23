# Datasheet: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-09-06 |
| DeliverableName | Network, Key, Attachment, and Renderer Security Checks |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | SECURITY_CONTROL |
| ContextEnvelope | M |
| ResponsibleParty | TBD |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary scope | Verify renderer allowlist, API key redaction/storage, provider endpoint policy, and attachment validation/retry behavior. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-06 |
| Covered SOW items | SOW-019, SOW-020, SOW-022, SOW-023 | `_CONTEXT.md` Traceability; decomposition DEL-09-06 |
| Supported objective | OBJ-008 | `_CONTEXT.md` Traceability; decomposition objective mapping |
| Anticipated artifacts | Security tests; network guard tests; attachment resolver validation; key storage checks | `_CONTEXT.md` Anticipated Artifacts |
| API key resolution order | UI safeStorage key first, then `ANTHROPIC_API_KEY`, then `CHIRALITY_ANTHROPIC_API_KEY`. | `docs/PRD.md` Section 8.5, FR-030 |
| API key storage path | `app.getPath('userData')/credentials/api-key.enc` | `docs/SPEC.md` Section 16.2 |
| Allowed Anthropic base URL | `https://api.anthropic.com` with no credentials and port empty or 443. | `docs/PRD.md` Section 8.5, FR-032 |
| Renderer network allowlist | Loopback plus Anthropic API path. | `docs/SPEC.md` Section 16.3; `docs/CONTRACT.md` K-NET-1 |
| Supported attachment extensions | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.pdf`, `.txt`, `.md`, `.csv` | `docs/SPEC.md` Section 16.1 |
| Attachment size limits | 10 MB per file; 18 MB total raw bytes per turn. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` Section 8.6, FR-038 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source warning | PRD source is accessible but has the run-declared expected/observed hash mismatch; this run treats the mismatch as a warning only. | Assignment instruction; `_REFERENCES.md` REF-006 |
| Security posture | API keys are non-project convenience state and must not be written to project files, logs, runtime events, SDK transcripts if avoidable, or tool artifacts. | `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` NFR-002 |
| Attachment trust boundary | Client attachment metadata is non-authoritative; server revalidates attachment properties. | `docs/PRD.md` Section 8.6, FR-037; `docs/CONTRACT.md` K-ATTACH-1 |
| Failure handling | Partial attachment failure is non-fatal when executable content remains; all attachments failing with empty text returns `ATTACHMENT_FAILURE`. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` Section 8.6, FR-040 |

## Construction

| Component | Expected Check Coverage | Source |
|---|---|---|
| Renderer network guard | Tests showing non-loopback/non-Anthropic renderer requests are cancelled and policy metadata excludes secrets. | `docs/PRD.md` FR-033; `docs/PRD.md` NFR-003 |
| Provider endpoint policy | Tests showing accepted and rejected Anthropic base URL variants. | `docs/PRD.md` FR-032 |
| API key storage and handoff | Tests showing safeStorage precedence, environment fallback, no project writes, and redacted logs/events. | `docs/PRD.md` FR-030, FR-031; `docs/SPEC.md` Section 16.2 |
| Attachment resolver | Tests for path validation, regular-file check, symlink rejection, extension allowlist, readability, and byte budgets. | `docs/SPEC.md` Section 16.1 |
| Retry behavior | Tests showing UI preserves draft/attachments after failed send where source scope requires retry preservation. | `docs/PRD.md` FR-040 |

## References

| RefID | Path | Status | Use |
|---|---|---|---|
| REF-002 | `docs/CONTRACT.md` | MATCH | Invariants K-NET-1, K-KEY-1, K-ATTACH-1, K-VALIDATE-1 |
| REF-003 | `docs/SPEC.md` | MATCH | Section 16 attachment, API key, and network policy mechanics |
| REF-005 | `docs/PLAN.md` | MATCH | Implementation sequencing context for key handoff and validation |
| REF-006 | `docs/PRD.md` | HASH_MISMATCH warning | Product requirements FR-030 through FR-040 and NFR security/privacy requirements |
| DECOMP | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | accessible | DEL-09-06 scope and SOW/objective mapping |
