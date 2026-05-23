# Guidance: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

## Purpose

Use this deliverable to keep the governing document set coherent while the Chirality App runtime moves toward the vNext SDK-privileged, contract-owned, Chirality-governed architecture. The work is not to add runtime implementation detail for its own sake. The work is to preserve the governance boundaries that make implementation acceptable: human authority, local filesystem project truth, accepted git history, runtime auditability, reliance-boundary ownership, product identity, and professional-boundary posture.

## Principles

1. Human approval remains non-delegable. Agents, SDKs, tools, validators, runtime events, and domain adapters may assist, draft, record, diagnose, or validate in limited ways, but they do not approve or issue work for reliance.
2. Filesystem project truth controls. If a decision matters for reliance, it belongs in a proper versioned project file or accepted artifact, not only in chat, runtime logs, UI state, SDK transcripts, model context, caches, or hidden memory.
3. Runtime audit records explain execution. They support replay, diagnosis, and review, but they are not approval records and do not make work code-compliant, safe for reliance, issued, or professionally adequate.
4. Reliance boundaries are product semantics. They must be documented, implemented, and tested in Chirality terms. Do not treat prompt instructions, SDK defaults, or visible tool settings alone as sufficient boundary enforcement.
5. Chirality product identity must remain explicit. SDK usage may be an implementation detail, but it must not redefine public APIs, UI events, persisted events, copy, or governance language as SDK-shaped behavior.
6. Source uncertainty must remain visible. Use `TBD`, `ASSUMPTION`, `PROPOSAL`, source warnings, and human-ruling-needed records instead of smoothing over unsupported claims.

## Considerations

| Area | Guidance |
|---|---|
| Authority order | Start with `docs/DIRECTIVE.md`, then `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and `docs/PRD.md`; use decomposition and agent instructions for scoped execution context. |
| PRD hash mismatch | Treat current `docs/PRD.md` as readable but source-warned. Do not use the mismatch to block this P1/P2 run, but do require a human ruling or accepted bypass before relying on the mismatched hash as clean source state. |
| Accepted git history | When governance notes become acceptance evidence, bind them to a git SHA or equivalent immutable evidence. Content changes after approval require review again. |
| Runtime implementation detail | Include runtime specifics only when they prove or preserve a boundary, such as accepted-turn persistence, event canonicality, settings isolation, permission denial, path containment, or SDK transcript non-authority. |
| Scope discipline | Keep remote MCP, plugins, broad tool search, shipped bypass, Windows/Linux packaging, retired PKG-08 scope, and domain-operation execution out of this deliverable except as boundary examples. |
| Responsible party | Keep `ResponsibleParty` as `TBD` until a human assigns ownership. |

## Trade-offs

| Trade-off | Recommended posture |
|---|---|
| Faster runtime delivery vs. governance completeness | Prefer a smaller runtime slice that preserves human gates, audit, path policy, settings isolation, and product-owned contracts. |
| SDK convenience vs. product-owned semantics | Use SDK mechanics only behind Chirality-owned contracts, mappers, events, permission overlay, hooks, and fallback criteria. |
| Audit richness vs. approval clarity | Preserve rich runtime records while making clear that approval is a separate human-authored project record. |
| Local-first truth vs. convenience state | Permit convenience state only when explicitly non-authoritative and unable to override governance. |
| Broad guidance vs. executable deliverable | Keep this deliverable at governance-alignment level; send implementation-specific requirements to the owning runtime packages unless required for a boundary check. |

## Examples

| Situation | Acceptable treatment |
|---|---|
| SDK transcript contains a useful event detail | Record or import the relevant detail into Chirality `HarnessEvent` form or a governed project artifact before treating it as reliance evidence. |
| A document says a runtime event proves approval | Mark as nonconforming; runtime events explain work and do not approve work. |
| A UI copy change implies Chirality certifies professional adequacy | Mark as nonconforming; preserve draft/decision-support posture and human authority. |
| A dependency or source fact is plausible but unsupported | Mark `TBD` or `ASSUMPTION`; do not promote it to a requirement. |
| A lower-authority artifact conflicts with the directive or contract | Surface the conflict and propose that the higher-authority source controls until a governed change updates the record. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| DEL-01-01-C001 | `docs/PRD.md` expected hash differs from observed hash. Dispatch says treat as source warning, not blocker. | `_REFERENCES.md` REF-006 expected/actual hash row | Dispatch instruction for this TASK run | Datasheet References; Specification Standards; Procedure source checks | Use observed `docs/PRD.md` only with source-warning status until human accepts the hash mismatch or updates the reference record. | TBD |
| DEL-01-01-C002 | Dispatch path used package label `PKG-01_Governance_and_Product_Boundaries`, but the existing deliverable folder and `_CONTEXT.md` use `PKG-01_Product_Governance_and_Reliance_Boundaries`. | TASK dispatch assignment path | Existing deliverable folder, `_CONTEXT.md`, and SOFTWARE_DECOMP v3.2 package name | Run record; all document Identification sections | Use stable IDs `PKG-01` and `DEL-01-01` plus existing `_CONTEXT.md`/decomposition package name; ask human to correct the stale dispatch label if needed. | TBD |

## Human Rulings Needed

| Ruling ID | Needed decision |
|---|---|
| DEL-01-01-R001 | Accept, bypass, or update the PRD hash mismatch in REF-006. |
| DEL-01-01-R002 | Confirm whether the stale dispatch package-label path should be corrected in ORCHESTRATOR coordination state. |
| DEL-01-01-R003 | Assign `ResponsibleParty`, if ownership is ready. |
| DEL-01-01-R004 | Define final filenames and destinations for governance consistency notes, human-authority checklist, project-truth checklist, document diff checklist, and acceptance checklist. |
