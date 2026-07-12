# Guidance: DEL-04-04 PersonaComposer from Instruction Root

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

DEL-04-04 exists to replace stub persona prompt behavior with a governed PersonaComposer that reads Chirality instruction-root materials and produces prompt context suitable for the SDK-backed runtime path. The value of the slice is not more prompt text by itself; it is making prompt composition deterministic, traceable, source-grounded, and bounded by Chirality-owned runtime policy.

Sources: `_CONTEXT.md` Deliverable Scope; decomposition DEL-04-04 row; `docs/DIRECTIVE.md` Sections 2.8-2.10; `docs/SPEC.md` Section 13.2.

## Principles

1. Chirality owns the prompt contract.
   The SDK may host generic model/tool-loop mechanics, but prompt/persona composition is a Chirality-owned product contract. Do not let SDK defaults, SDK transcript shape, vendor product assumptions, or ambient settings decide PersonaComposer behavior. Source: `docs/DIRECTIVE.md` Section 2.8; `docs/PLAN.md` approved vNext direction.

2. The instruction root is read authority, not a runtime write target.
   PersonaComposer may read release-managed governance and `agents/AGENT_<persona>.md` files, but ordinary project execution must not mutate those resources. Source: `docs/SPEC.md` Section 1.1; `docs/CONTRACT.md` K-ROOT-2.

3. Prompt text supports policy; it does not enforce policy.
   Include mode and tool-surface descriptions in prompt context, but rely on SDK options, denied tools, hooks, `canUseTool`, path policy, and Chirality overlays for enforcement. Source: `docs/CONTRACT.md` K-PERM-2 and K-PERM-3; `docs/SPEC.md` Sections 14.3 and 15.

4. Fingerprints should reflect real inputs.
   A boot fingerprint that only hashes persona name and mode is insufficient for the target behavior. It should reflect actual persona content, governance preface, mode, tool/policy inputs, settings-source posture, MCP server versions, and subagent policy version when those inputs exist. Source: `docs/SPEC.md` Section 13.2.

5. Keep provider-specific terms behind the adapter boundary.
   The composed prompt can mention the configured permitted tool surface, but public Chirality contracts and runtime events must remain provider-neutral. Source: `docs/DIRECTIVE.md` Section 2.10; `docs/SPEC.md` Section 10.3.

## Considerations

- Use `docs/TYPES.md` Section 3.4 for alias vocabulary unless a more specific accepted alias resolver exists by implementation time.
- Treat the working-root summary as contextual prompt material, not as instruction-root governance and not as project truth validation.
- Keep prompt assembly deterministic: stable section ordering, stable omitted-field behavior, and explicit handling for missing optional inputs.
- Prefer structured composer inputs over ad hoc strings so tests can isolate persona content, governance preface, mode, tool surface, and fingerprint material.
- If DEL-04-02 owns the final SDK option/tool-surface object, this deliverable should accept that resolved surface rather than reconstruct it.
- Resolve aliases locally only for the canonical vocabulary in `docs/TYPES.md` Section 3.4, or delegate when an accepted DEL-08-02 resolver/interface exists. The decision criterion is ownership: local handling is appropriate for stable source-defined mappings needed to reach `agents/AGENT_<persona>.md`; delegation is appropriate when the routing contract owns broader UI/matrix alias behavior or exposes a tested resolver.
- If DEL-08-01 or DEL-08-02 changes instruction-root packaging or alias contracts, update the composer through an explicit dependency note rather than local convention.

## Trade-offs

| Decision Area | Preferred Direction | Trade-off |
|---|---|---|
| Prompt detail vs. enforcement | Include concise governance/mode/tool reminders, but enforce with runtime policy. | Long prompts can drift into false reliance if not backed by hooks and permissions. |
| Direct alias handling vs. delegated resolver | Handle only source-defined alias mappings locally unless DEL-08-02 provides an accepted resolver/interface; then delegate to that resolver and keep missing-persona behavior visible. | Duplicating alias logic risks divergence with the routing contract; over-delegation can obscure missing persona failures if the resolver does not return canonical agent names and typed failures. |
| Fingerprint breadth | Hash real prompt and policy inputs that affect runtime behavior. | Broader fingerprints can churn when non-semantic metadata changes; define stable normalized inputs. |
| SDK-specific names in prompt | Keep SDK-specific names as adapter/tool metadata where necessary. | Overexposure can make Chirality appear SDK-shaped; underexposure can make tool context unclear. |

## Examples

TBD: Final prompt template examples require accepted implementation interfaces for PersonaComposer inputs, resolved tool surface, working-root summary shape, and boot metadata shape.

ASSUMPTION: A useful test fixture can vary one input at a time, such as agent instruction content, mode, and visible tool list, and assert the boot fingerprint changes for each supported input.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-001 | `docs/PRD.md` is listed as `MATCH`, but decomposition SOW rows cite PRD sections for persona and instruction-root scope. | `_REFERENCES.md` REF-006 | Decomposition SOW-017 / SOW-030 and `docs/PRD.md` Section 8.4 | Datasheet References; Specification PC-REQ-004, PC-REQ-006, PC-REQ-010, PC-REQ-011 | Treat PRD-derived details as source-state warnings; prefer matching `docs/SPEC.md`, `docs/CONTRACT.md`, `docs/DIRECTIVE.md`, `docs/TYPES.md`, and accepted decomposition where they overlap. | TBD — reconciled under D-APP-38 |

## Source-State Warning

REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-122 records accepted alias delegation to the shell persona resolver; the composer need not duplicate it. UPD-123 records DEP-04-04-004 retirement and corrected register counts.
