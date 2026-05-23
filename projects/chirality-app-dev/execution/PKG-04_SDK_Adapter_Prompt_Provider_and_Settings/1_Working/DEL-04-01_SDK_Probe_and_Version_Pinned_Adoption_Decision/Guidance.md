# Guidance: DEL-04-01 SDK Probe and Version-Pinned Adoption Decision

## Purpose

This deliverable creates the evidence package for deciding whether Chirality can adopt the Claude Agent SDK as a version-pinned, replaceable runtime substrate for R1. The decision must preserve Chirality-owned runtime contracts, audit records, settings isolation, permission semantics, transcript canonicality, product identity, and fallback control.

Source grounding: `docs/DIRECTIVE.md` Section 2.8 through 2.11; `docs/PLAN.md` R0/R1; decomposition row for `DEL-04-01`.

## Principles

1. Chirality contracts come first.
   SDK APIs, message names, tool names, session IDs, and transcript paths are adapter metadata. `AgentEnginePort`, `UIEvent`, `HarnessEvent`, session storage, permission decisions, and governance records remain Chirality-owned. Sources: `docs/SPEC.md` Section 10.3; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-5.

2. Probe before adoption.
   R0 exists to validate SDK assumptions before R1 implementation details harden. The probe should produce a positive adoption decision only where behavior is observed, recorded, and compatible with conformance expectations. Sources: `docs/PLAN.md` R0; `docs/PRD.md` R0.

3. Product-critical reliance boundaries need enforceable surfaces.
   Prompt text and opaque SDK defaults are insufficient for P0 audit, filesystem, lifecycle, transcript, settings, subagent, and human-gate boundaries. Sources: `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1 and K-RELIANCE-2.

4. Settings isolation is a release boundary.
   Shipped SDK builds must use `settingSources: []`; user and local setting sources are not allowed in shipped builds. Source: `docs/SPEC.md` Section 12.2.

5. Permission restrictions require more than `allowedTools`.
   `allowedTools` can auto-approve but is not by itself a restriction boundary. The probe should explicitly test deny rules, mode policy, hooks, and `canUseTool` behavior. Sources: `docs/SPEC.md` Section 14.3; `docs/CONTRACT.md` K-PERM-3.

6. SDK transcripts assist but do not govern.
   SDK transcript placement and mirroring may support resume/debugging, but the Chirality audit JSONL remains canonical unless SDK content is imported into `HarnessEvent` form. Sources: `docs/SPEC.md` Section 8.4; `docs/CONTRACT.md` K-SDK-3.

## Considerations

- Treat `docs/PRD.md` as source-state warning material until REF-006 hash mismatch is resolved or accepted. Corroborated PRD claims may remain draft context where matching MATCH sources independently support the same control, but closure should not rely on PRD-only wording until the source-state conflict is ruled on.
- The decomposition marks this as a documentation/probe slice with no new user tool exposure. Keep implementation changes out of this deliverable and route code work to downstream DEL-04-02 through DEL-04-05.
- Open issue OI-001 makes SDK viability, message categories, settings behavior, hooks, permissions, MCP, sessions, and packaging empirical questions. Do not convert unknown probe results into requirements that pretend the answer is already known.
- Open issue OI-002 leaves transcript placement unresolved. The acceptable outcomes are project-controlled `SessionStore`, `CLAUDE_CONFIG_DIR`, both, or cross-reference to default path with residual risk, per the decomposition and source corpus.
- Packaging risk is not limited to the SDK package dependency. The probe must consider SDK subprocess/binary execution in Electron and any built-app path constraints.
- Fallback threshold is a human-governed TBD: if a product-critical reliance boundary cannot be observed, enforced, and recorded in Chirality terms, the adoption decision should either select `FALLBACK` or explicitly assign `ADOPT_WITH_RESIDUAL_RISK` to an accountable approver.

## Trade-offs

| Decision Area | Prefer | Watch For | Source |
|---|---|---|---|
| Runtime mechanics | SDK handles generic model/tool loop when verified. | SDK defaults redefining product semantics. | `docs/DIRECTIVE.md` Section 2.8; `docs/PLAN.md` R0/R1 |
| Event model | Chirality maps SDK messages into stable UI/runtime events. | Browser or persisted event contracts becoming SDK-shaped. | `docs/SPEC.md` Sections 9 and 10.3 |
| Tool permissions | Deny-first overlay with hooks and callbacks. | Mistaking `allowedTools` for restriction. | `docs/SPEC.md` Sections 14.3 and 15.1 |
| Session storage | Project-controlled transcript/store linkage where reliable. | SDK default transcript path becoming de facto canonical. | `docs/SPEC.md` Section 8.4; `docs/PRD.md` KG-024 |
| Settings | `settingSources: []` in shipped builds. | Ambient `.claude` or user/local settings entering product behavior. | `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1 |
| Adoption | Version-pinned SDK path with conformance tests. | SDK API drift, packaging failures, or unverifiable reliance boundaries. | `docs/CONTRACT.md` K-SDK-2; `docs/PRD.md` KG-021 through KG-032 |

## Residual-Risk Appraisal Method

Residual-risk notes should evaluate each unresolved SDK adoption issue against three questions:

1. Can Chirality observe the behavior in project-owned records or adapter metadata?
2. Can Chirality enforce or fail closed at a product-owned boundary rather than relying on prompt text or opaque SDK defaults?
3. Can a human reviewer distinguish `ADOPT_WITH_RESIDUAL_RISK` from `FALLBACK` using version-pinned probe evidence?

Apply the method to SDK API drift, settings leakage, allowed-tools misconception, transcript location, Electron packaging, SDK security boundary, subagent inherited permissions, session mirror reliability, product-identity drift, platform dependency, reliance-boundary ambiguity, and engine adapter lock-in. Sources: `docs/DIRECTIVE.md` Sections 2.8 through 2.11; `docs/CONTRACT.md` K-ENGINE-5, K-RELIANCE-1, K-RELIANCE-2, and K-SDK-2; `docs/PLAN.md` R0/R1 and Section 8.

## Examples

TBD: no completed SDK probe notes are available in the accessible source corpus.

Example evidence rows the final probe notes should contain:

| Probe Topic | Evidence to Capture | Accept / Fallback Question |
|---|---|---|
| SDK version | Package name, exact version, lockfile evidence, subprocess version when knowable. | Can this version be pinned and regression-tested? |
| Messages | Observed message categories and sequence from `query()`. | Can all required categories map to stable `UIEvent` and `HarnessEvent` records? |
| Settings | Effective `settingSources` behavior in shipped-like and dev-only modes. | Can shipped builds avoid ambient user/local settings? |
| Permissions | Behavior of `permissionMode`, `allowedTools`, `disallowedTools`, `canUseTool`, and hooks. | Can deny-first policy be verified in Chirality terms? |
| Session storage | SDK session ID, resume behavior, transcript path/store key, `SessionStore`, `CLAUDE_CONFIG_DIR`. | Can SDK transcripts remain secondary and traceable? |
| Packaging | Built Electron app starts SDK-backed turn and can execute required subprocess/binary. | Does packaging require fallback or release blocker? |

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| SRC-001 | `docs/PRD.md` is authoritative in role but `_REFERENCES.md` reports `HASH_MISMATCH`; content based on PRD should not be closed without source-state confirmation. | `_REFERENCES.md` REF-006 | `docs/PRD.md` R0/R1 and KG-021 through KG-032 | Datasheet References; Specification Requirements and Verification; Guidance Considerations | Use corroborated PRD claims as draft context where they match MATCH sources; require human/source refresh before closure. | TBD |
