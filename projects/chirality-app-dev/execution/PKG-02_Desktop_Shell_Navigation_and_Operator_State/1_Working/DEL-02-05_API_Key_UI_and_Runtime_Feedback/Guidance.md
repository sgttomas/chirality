# Guidance: DEL-02-05 API Key UI and Runtime Feedback

## Purpose

This deliverable gives operators a clear UI for API key status and runtime failure recovery while preserving Chirality's governance boundary: key material and runtime convenience state are useful for operation, but they are not project truth.

Sources: `_CONTEXT.md`; decomposition DEL-02-05 row; `docs/DIRECTIVE.md` Project Truth sections; `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` Sections 7.3 and 7.7.

## Principles

- Keep key material invisible. The UI may show whether a key comes from `ui`, `env`, or `none`, but must not display, log, or persist the key value. Sources: `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2.
- Separate user-facing feedback from runtime authority. UI messages can help the operator recover, but runtime policy remains in the engine/provider/session layers. Sources: `_CONTEXT.md` Exclusions; `docs/SPEC.md` Section 10 and Section 11.
- Preserve retry context. Runtime errors should not destroy draft prompt text or attachment state needed for retry. Sources: `docs/PRD.md` Section 7.3 and FR-020.
- Use stable browser-facing events. UI handling should consume the established SSE names, including `turn:error` and `process:exit`, instead of exposing SDK-specific message semantics. Sources: `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4.
- Treat the PRD hash mismatch as a source warning. Use PRD content conservatively and prefer corroborated SPEC/CONTRACT/TYPES statements for binding implementation detail. Source: `_REFERENCES.md` REF-006 and dispatch instruction.

## Considerations

- The API key UI is a presentation/control surface. Actual key storage, provider handoff, redaction, and network policy belong to adjacent runtime/security deliverables.
- Secure-storage unavailability needs a clear visible error because the PRD acceptance criteria explicitly require it, but the exact wording is not specified in the accessible source corpus.
- Typed runtime error copy should be actionable without leaking secret-bearing provider detail.
- The UI can show status and next steps, but should avoid language that suggests the app has approved, certified, or externally validated work.
- Retry preservation should account for both draft text and attachments; attachment server validation remains outside this deliverable.

## Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Detail vs. secrecy in key/error feedback | Prefer source/status and next-step text over raw provider details or key fragments. | `docs/CONTRACT.md` K-KEY-1 and K-EVENT-6 |
| UI convenience vs. project truth | Store only non-authoritative UI convenience state; never write API key material into project files. | `docs/DIRECTIVE.md`; `docs/TYPES.md` Section 1.7 |
| Error specificity vs. taxonomy ownership | Show typed actionable UI states, but do not invent canonical runtime error enums in this deliverable. | `_CONTEXT.md` Exclusions; decomposition package boundaries |
| Backward compatibility vs. runtime refactor | Preserve browser-facing SSE names while runtime internals move behind `TurnEngine`. | `docs/SPEC.md` Section 11; `docs/PRD.md` FR-071 |

## Examples

TBD: The accessible source corpus defines required status values and behavior, but does not provide approved UI copy examples, component names, screenshots, or visual states.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT001 | PRD source hash differs from expected scaffold hash, but dispatch says to treat mismatch as warning, not blocker. | `_REFERENCES.md` REF-006 | Dispatch instruction for this TASK run | All PRD-cited requirements | Use PRD only with warning; prefer corroborated SPEC/CONTRACT/TYPES for implementation detail. | TBD |
| CT002 | Deliverable covers API key UI/status, but SOW-019 primary package is PKG-09 with related implementation deliverables DEL-04-05 and DEL-09-06. | Decomposition DEL-02-05 row | Decomposition SOW ledger for SOW-019 | Specification scope and verification ownership | Treat DEL-02-05 as UI feedback surface only; leave storage/resolution/security enforcement to adjacent deliverables. | TBD |
