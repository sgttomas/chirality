# Guidance: DEL-09-06 Network, Key, Attachment, and Renderer Security Checks

## Purpose

This deliverable exists to keep validation, packaging, release, network, key, and instruction-root checks explicit and repeatable for PKG-09 release readiness. Its security checks should demonstrate that key material remains outside project truth, renderer/network access is bounded, provider endpoint selection is constrained, and attachment handling does not rely on client-supplied metadata.

Sources: `_CONTEXT.md` Traceability; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` OBJ-008 and DEL-09-06.

## Principles

1. Runtime code is the security boundary. Prompts and documentation can reinforce policy, but tests should target runtime behavior such as path containment, permission policy, hooks, redaction, and network controls.
   Source: `docs/PRD.md` Section 4, principles 18-19.

2. API keys are convenience state, not project truth. Treat any write of key material to working root, runtime events, logs, git-tracked execution files, SDK transcripts if avoidable, or tool artifacts as a release-blocking failure.
   Source: `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` FR-031 and NFR-002.

3. Renderer and provider network checks should be allowlist-oriented. The current shipped network posture is loopback plus Anthropic API path, with broader network access reserved for governed future scope.
   Source: `docs/CONTRACT.md` K-NET-1; `docs/SPEC.md` Section 16.3.

4. Attachment metadata from the browser is advisory only. Server-side validation must be the authority for path, type, symlink status, readability, regular-file status, and byte budgets.
   Source: `docs/PRD.md` FR-037; `docs/CONTRACT.md` K-ATTACH-1.

5. Failure behavior is part of the security surface. Tests should verify that partial attachment failures do not discard executable content and that total attachment failure without text returns the expected typed failure while preserving retry state where the UI is involved.
   Source: `docs/PRD.md` FR-040; `docs/SPEC.md` Section 16.1.

## Considerations

- The PRD reference is accessible but has the declared expected/observed hash mismatch. Per assignment, this is a source warning only; do not treat it as a blocker for P1/P2 drafting.
- Keep endpoint tests strict about credentials and ports. `https://api.anthropic.com` with credentials or a non-empty non-443 port is not equivalent to the accepted base URL.
- Prefer negative tests for sensitive paths: denied network URL, unsupported extension, symlink, directory, over-budget file, unreadable file, and redaction of realistic key-shaped strings.
- Avoid treating `allowedTools` or SDK permissions alone as sufficient. Chirality-owned overlays remain required for professional safety.
- Exact implementation file paths are `TBD` until implementation locations are confirmed by the relevant feature deliverables.

## Trade-offs

| Topic | Trade-off | Guidance |
|---|---|---|
| Unit tests vs integration tests | Unit tests isolate policy logic; integration tests prove route/Electron behavior. | Use both where the surface crosses Electron, SDK provider, or route boundaries. |
| Redaction assertions | Broad fixture scanning may produce false positives; narrow checks may miss variants. | Include representative key variants and verify both positive redaction and non-secret metadata retention. |
| Attachment retries | UI retry behavior may sit outside the resolver. | Keep resolver validation separate from route/UI retry preservation so failures are easier to localize. |
| Network policy | Provider execution requires Anthropic access, while renderer traffic must remain constrained. | Test renderer and Node/SDK provider policy as separate surfaces with a shared policy vocabulary. |

## Examples

| Example | Expected Result | Source |
|---|---|---|
| Base URL `https://api.anthropic.com` | Accepted when credentials are absent and port is empty or 443. | `docs/PRD.md` FR-032 |
| Base URL with embedded credentials | Rejected. | `docs/PRD.md` FR-032 |
| Renderer request to non-loopback, non-Anthropic URL | Cancelled and logged without secrets. | `docs/PRD.md` FR-033 |
| Attachment path points to symlink | Rejected before provider execution. | `docs/SPEC.md` Section 16.1; `docs/PRD.md` NFR-004 |
| One attachment fails, text or another valid attachment remains | Turn may proceed with warning. | `docs/SPEC.md` Section 16.1 |
| All attachments fail and text is empty | Request fails with `ATTACHMENT_FAILURE`. | `docs/SPEC.md` Section 16.1 |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| TBD | No source-content conflict identified during P1/P2. PRD hash mismatch remains a source warning only. | `_REFERENCES.md` REF-006 | Assignment instruction | All PRD-grounded sections | Treat PRD content as usable with warning for this run. | TBD |
