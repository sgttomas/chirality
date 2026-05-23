# Procedure: DEL-04-01 SDK Probe and Version-Pinned Adoption Decision

## Purpose

Define the operational steps to produce and verify the SDK probe notes, version-pinned adoption decision, fallback criteria, and residual-risk notes for DEL-04-01.

This procedure is for producing the deliverable artifact. It does not authorize implementation of SDK-backed runtime code or exposure of new user-visible tools.

## Prerequisites

| Prerequisite | Status / Note | Source |
|---|---|---|
| Accepted decomposition row for DEL-04-01 | Present in SOFTWARE_DECOMP v3.2. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Source corpus | Accessible; `docs/PRD.md` has REF-006 `HASH_MISMATCH`. | `_REFERENCES.md` |
| Upstream dependencies | TBD: no accepted dependency edges have been extracted yet. | `_DEPENDENCIES.md` |
| SDK probe environment | TBD: package version, subprocess availability, Electron packaging posture, and test harness are not yet recorded. | Source gap |
| Runtime contract expectations | Required before SDK adapter production default. | `docs/SPEC.md` Section 10; `docs/PLAN.md` R1 |
| Reliance-boundary expectations | Required for P0 boundaries and fallback decisions. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1 |

## Steps

1. Confirm source-state before final closure.
   - Re-check `_REFERENCES.md` and resolve or explicitly accept the REF-006 `docs/PRD.md` hash mismatch.
   - If unresolved, keep PRD-derived conclusions marked as draft/source-warning material.

2. Prepare the probe matrix.
   - Include package version, `query()` message sequence, `settingSources`, permission mapping, `canUseTool`, hooks, in-process MCP, agents, resume, `SessionStore`, `CLAUDE_CONFIG_DIR`, interrupt behavior, Electron packaging, API key environment handling, branding/product identity, fallback triggers, and residual risks.
   - Source: `docs/PLAN.md` R0 and `docs/PRD.md` R0.

3. Record version evidence.
   - Capture exact `@anthropic-ai/claude-agent-sdk` version under evaluation.
   - Capture Claude Code subprocess version where knowable.
   - Mark unknowns as `TBD`; do not infer a version from roadmap text.
   - Source: `docs/SPEC.md` Section 12.4; `docs/CONTRACT.md` K-SDK-2.

4. Probe SDK message behavior.
   - Run a controlled `query()` sequence in the intended adapter environment.
   - Record observed message categories, ordering, terminal states, and error/interrupt behavior.
   - Determine whether each required message can map to stable `UIEvent` and `HarnessEvent` contracts.
   - Source: `docs/SPEC.md` Sections 9 and 10.3.

5. Probe settings isolation.
   - Verify shipped-like options use `settingSources: []`.
   - Verify `user` and `local` setting sources are not used in shipped builds.
   - If development-only project settings are used, require explicit environment configuration.
   - Source: `docs/SPEC.md` Section 12.2.

6. Probe permissions and tool exposure.
   - Test `permissionMode`, `allowedTools`, `disallowedTools`, `canUseTool`, and hooks.
   - Confirm that `allowedTools` is not treated as a restriction boundary.
   - Confirm denied tools are blocked by policy, hooks, SDK deny rule, or human gate and are recorded before allowing/denying when applicable.
   - Source: `docs/SPEC.md` Sections 14.3 and 15.1; `docs/CONTRACT.md` K-PERM-1 through K-PERM-3.

7. Probe MCP and hook behavior.
   - Test in-process Chirality MCP exposure only under controlled validation.
   - Confirm MCP tools are not bypasses and remain subject to permission, hook, path, redaction, and event logging policy.
   - Confirm required hooks for path containment, instruction-root protection, symlink write rejection, and write budget are feasible where applicable.
   - Source: `docs/SPEC.md` Sections 14.2 and 15.2; `docs/CONTRACT.md` K-MCP-1.

8. Probe sessions, storage, transcripts, and resume.
   - Record SDK session ID, resume mode, transcript path or store key, SDK config dir, `SessionStore`, and `CLAUDE_CONFIG_DIR` behavior.
   - Prefer project-controlled transcript placement or mirroring when reliable.
   - If SDK writes outside project-controlled storage, cross-reference the path or store key and record residual risk while keeping Chirality JSONL canonical.
   - Source: `docs/SPEC.md` Sections 8.4 and 12.4.

9. Probe API key environment handling and redaction.
   - Confirm key precedence and active-turn handoff behavior.
   - Confirm key material is redacted from logs, events, SDK transcripts if avoidable, and tool artifacts.
   - Source: `docs/SPEC.md` Section 12.3; `docs/CONTRACT.md` K-KEY-1.

10. Probe Electron packaging.
    - Validate that a packaged build can start an SDK-backed harness turn.
    - Record subprocess/binary execution path, `asarUnpack`, signing, environment, and transcript/storage effects.
    - Source: `docs/PRD.md` KG-025; `docs/PLAN.md` R0.

11. Draft the version-pinned adoption decision.
    - State `ADOPT`, `ADOPT_WITH_RESIDUAL_RISK`, or `FALLBACK`.
    - Cite probe evidence for each P0 reliance boundary.
    - Keep the SDK privileged as implementation substrate, not product identity or governance authority.
    - Source: `docs/DIRECTIVE.md` Sections 2.8 through 2.11.

12. Draft fallback criteria and residual-risk notes.
    - Include SDK API drift, settings leakage, allowed-tools misconception, transcript location, Electron packaging, SDK security boundary, subagent inherited permissions, session mirror reliability, product-identity drift, platform dependency, reliance-boundary ambiguity, and engine adapter lock-in.
    - Source: `docs/PRD.md` KG-021 through KG-032.

13. Route downstream work.
    - Send implementation requirements to DEL-04-02 through DEL-04-05 as appropriate.
    - Keep this deliverable as the documentation/probe decision slice.
    - Source: decomposition rows for PKG-04.

## Verification

| Check | Pass Criteria |
|---|---|
| Source-state check | REF-006 hash mismatch is resolved, accepted, or carried as a closure blocker. |
| Probe coverage | Every required probe topic from R0 has an evidence row or `TBD` blocker. |
| Version pin | Exact SDK package version is recorded before adoption. |
| Contract boundary | Decision states that SDK-specific identifiers remain adapter metadata and Chirality contracts stay product-owned. |
| Settings isolation | Shipped posture uses `settingSources: []`. |
| Permissions | Deny-first behavior is verified; `allowedTools` is not treated as restriction. |
| Sessions/transcripts | SDK transcript/store linkage is recorded without replacing Chirality audit JSONL. |
| Interrupts | Success, failure, interruption, and cancellation terminal behavior is evidenced or flagged. |
| Packaging | Packaged app SDK turn is proven or recorded as fallback/residual risk. |
| Fallback criteria | Any unverifiable P0 reliance boundary has an explicit fallback trigger. |

## Records

Required records:

- SDK probe matrix and notes.
- Version-pinned adoption decision.
- Fallback criteria.
- Residual-risk notes.
- Source-state warning or resolution for REF-006.
- Traceability to SOW-018, SOW-044, SOW-046, OBJ-004, OI-001, and OI-002.

TBD records:

- Exact SDK version.
- Exact Claude Code subprocess version, if knowable.
- Exact transcript/store decision.
- Exact Electron packaging result.
- Exact adoption verdict.
