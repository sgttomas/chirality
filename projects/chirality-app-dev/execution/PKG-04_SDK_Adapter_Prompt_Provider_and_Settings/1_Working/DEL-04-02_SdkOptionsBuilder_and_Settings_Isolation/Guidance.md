# Guidance: DEL-04-02 SdkOptionsBuilder and Settings Isolation

## Purpose

`SdkOptionsBuilder` exists to keep SDK request construction deterministic, explicit, and governed while Chirality adopts the Claude Agent SDK as a replaceable implementation substrate. It should translate Chirality-owned session state, resolved runtime options, prompt/tool policy, settings posture, and resume metadata into SDK-facing options without allowing SDK defaults or ambient settings to redefine product behavior.

Sources: `docs/DIRECTIVE.md` Section 2.8; `docs/CONTRACT.md` Section 1.4; `docs/SPEC.md` Sections 12-15; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-04-02.

## Principles

1. Determinism before convenience.
   For the same session, persona, mode, option set, SDK version, MCP server set, and policy input, the builder should produce stable option values, stable tool ordering, and stable visible metadata. Sources: `docs/CONTRACT.md` K-TOOL-1; `docs/PRD.md` Section 8.13, HASH_MISMATCH.

2. Settings isolation is a release boundary.
   Shipped builds use `settingSources: []`. Development-only project settings require explicit environment enablement and must not include `user` or `local` sources. Sources: `docs/SPEC.md` Section 12.2; `docs/CONTRACT.md` K-SDK-1.

3. Policy adequacy is checked before option construction.
   The builder should not normalize missing governed policy into permissive SDK defaults. If required settings, tool, permission, hook, MCP, or subagent policy inputs are absent, explicitly unresolved, or contradictory, the builder should fail closed or return a structured integration error before constructing SDK options. Sources: `docs/CONTRACT.md` K-RELIANCE-2, K-PERM-1 through K-PERM-3, K-MCP-1, K-HOOK-1; `docs/PLAN.md` R2.

4. `allowedTools` is not a safety boundary.
   Treat `allowedTools` as SDK auto-approval posture, not as the complete restriction mechanism. Restricted modes require deny rules, disallowed tools, hooks, `canUseTool`, `dontAsk`, or the PKG-06 overlay as applicable. Sources: `docs/CONTRACT.md` K-PERM-3; `docs/SPEC.md` Section 14.3.

5. Adapter metadata is allowed; public semantic leakage is not.
   SDK-specific names and SDK package version may appear in adapter-local metadata and safe runtime metadata, but they are evidence about the runtime adapter, not public Chirality product-version authority. Public Chirality APIs, canonical events, and governance records remain Chirality-owned. Sources: `docs/CONTRACT.md` K-ENGINE-4; `docs/TYPES.md` Section 9.

6. Prefer explicit unknowns over plausible SDK detail.
   Exact SDK TypeScript option fields that are not confirmed by local accepted source or the SDK probe should remain `TBD`. This is a review guard, not a drafting omission: premature property names can make an unverified SDK version look authoritative. Sources: `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1; `docs/PLAN.md` R0; `docs/PRD.md` KG-021, HASH_MISMATCH.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Fallback implementation | Keep fallback resolution pure and testable. Emit warnings for unknown option keys; do not let unknown fields affect behavior. | `docs/SPEC.md` Section 13.1 |
| Settings posture | Make shipped/development posture an explicit input or environment-derived policy, then record the selected posture in safe metadata. Shipped option construction should omit ambient settings by using `settingSources: []`; development project settings should be admitted only by the explicit development policy path. | `docs/SPEC.md` Sections 12.2, 12.4 |
| Tool registry | Resolve requested tool names against a deterministic registry of SDK built-ins and Chirality MCP tools. Unknown names should fail before SDK request construction. | `docs/SPEC.md` Section 14.3 |
| Hooks and permissions | Accept hook/callback/deny policy inputs, but do not overclaim that this slice fully implements PKG-06 permission semantics. | `_CONTEXT.md` ContextEnvelopeNotes; `docs/PLAN.md` R2 |
| Resume and session linkage | Include resume/session fields only through the engine/session contract and safe adapter metadata. SDK transcripts remain secondary to Chirality events. | `docs/CONTRACT.md` K-SDK-3; `docs/SPEC.md` Section 12.4 |
| Subagents | Treat subagent option construction as policy-gated and fail-closed until the governance bridge supplies restricted child definitions. | `docs/CONTRACT.md` K-SUBAGENT-1, K-SUBAGENT-2; `docs/PRD.md` KG-027, HASH_MISMATCH |
| PRD hash state | Use `docs/PRD.md` requirements with caution because `_REFERENCES.md` reports `HASH_MISMATCH`; do not use PRD-only details to override matching higher-authority sources. | `_REFERENCES.md`; `docs/DIRECTIVE.md` Section 0 |

## Trade-offs

| Trade-off | Preferred Direction | Rationale |
|---|---|---|
| SDK defaults vs explicit options | Prefer explicit Chirality options and recorded posture. | Prevents ambient settings and SDK defaults from becoming product semantics. |
| Early tool exposure vs controlled sequence | Prefer read-only and registered tools first; defer write/bash/subagent execution until overlays and hooks are active. | Matches roadmap sequence and avoids permission boundary overclaiming. |
| Rich SDK metadata vs provider-neutral core | Keep SDK metadata local to adapter/runtime metadata, with public APIs and canonical events in Chirality terms. | Preserves engine replaceability and conformance testing. |
| Immediate exact SDK field design vs probe-backed API | Use `TBD` for exact fields until SDK version/probe confirms current TypeScript APIs. | Avoids encoding stale or guessed upstream SDK behavior. |

## Examples

### Example Fallback Trace

```text
Input:
  opts.model = TBD
  environment CHIRALITY_GLOBAL_MODEL = set
  instruction-root model default = available
  runtime default = available

Expected resolution:
  model = CHIRALITY_GLOBAL_MODEL
  warning list = none unless unknown option keys are present

Source:
  docs/SPEC.md Section 13.1
```

### Example Settings Posture

```text
Shipped build:
  settingSources = []
  visible metadata includes settings-source posture = "shipped-empty"

Development-only explicit project settings:
  settingSources = ['project']
  visible metadata includes settings-source posture = "development-project"
  user/local setting sources remain forbidden

Source:
  docs/SPEC.md Section 12.2
```

### Example Tool Resolution

```text
Requested tools:
  Read
  mcp__chirality__status_read
  unknown_tool

Expected result:
  Read maps to registered SDK built-in if available.
  mcp__chirality__status_read maps to registered Chirality MCP tool.
  unknown_tool returns structured validation error before SDK request construction.

Source:
  docs/SPEC.md Sections 14.1-14.3
```

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONFLICT-DEL-04-02-001 | `docs/PRD.md` is locally accessible and highly relevant, but `_REFERENCES.md` reports `HASH_MISMATCH` against the expected SHA. | `_REFERENCES.md` Authoritative Source Corpus | `docs/PRD.md` Sections 8.4, 8.12, 8.13, 10.3.1 | All PRD-cited requirements and guidance | Treat PRD content as source-state warning: use when consistent with higher-authority matching sources, mark PRD-only exact details as TBD or assumption until source state is accepted. | TBD |
