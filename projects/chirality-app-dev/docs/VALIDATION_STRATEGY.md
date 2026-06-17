# VALIDATION STRATEGY - Harness Runtime and Governance Evidence

**Status:** Draft governance support surface
**Date:** 2026-06-13
**Product:** Chirality desktop harness and bundled agent operating system
**Applies to:** app-dev governance, harness runtime, frontend validation, packaging evidence, and governed workspace workflows

## 1. Purpose

This document defines how Chirality App validation evidence is classified, collected, and interpreted. It routes evidence for app-dev work; it does not replace `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PRD.md`, `docs/PLAN.md`, source code, tests, accepted execution artifacts, decision records, or git history.

Validation evidence is software and governance evidence only. It is not lifecycle issuance, release publication authorization, professional approval, certification, sealing, authentication, code-compliance acceptance, or external validation for reliance.

## 2. Evidence Principles

Chirality separates five evidence classes:

| Evidence class | What it proves | What it does not prove |
|---|---|---|
| Static governance evidence | Control-plane links, stale-rule removal, plan/log consistency, decision-register routing, and clean documentation diffs. | Runtime behavior, release readiness, or human approval. |
| Runtime contract verification | Product-owned adapter, session, event, permission, SDK isolation, and tool-surface behavior under deterministic tests. | Professional adequacy or future SDK behavior after an untested upgrade. |
| Harness workflow validation | API and UI-facing harness workflows behave as expected against a running local app surface. | Full user acceptance, all platform packaging behavior, or release publication readiness. |
| Packaging and instruction-root evidence | Required instruction-root resources are present and packaged build commands complete where applicable. | Signed, notarized, published, or externally distributed release status. |
| Boundary and claims review | Network, API-key, redaction, professional-boundary, and product-identity constraints remain visible and enforced. | Legal advice, professional-practice advice, or code-compliance approval. |

Evidence must bind to the command run, working tree state or commit, affected files, generated artifacts where applicable, and skipped checks with reasons. A skipped check is acceptable only when the tranche scope makes the skip explicit and defensible.

## 3. Current Local Command Surface

Unless a tranche specifies narrower validation, app-dev validation commands are run from `frontend/`:

| Command | Evidence role |
|---|---|
| `npm run test` | Vitest unit and contract checks for API routes, runtime libraries, SDK mapping, tool descriptors, session events, UI helpers, script policies, and governance helpers. |
| `npm run typecheck` | TypeScript contract check for frontend and Electron entry surfaces. |
| `npm run harness:validate:premerge` | Running-app harness workflow validation with stable summary artifact at `frontend/artifacts/harness/section8/latest/summary.json`. Requires the harness API to be reachable. |
| `npm run harness:validate:section9` | Section 9 deterministic runtime-ID aggregation over targeted Vitest files with stable summary artifact at `frontend/artifacts/harness/section9/latest/summary.json`. |
| `npm run harness:validate:agentsdk-dev-turn` | Route-level opt-in `agentSdk` scripted dev-turn validation using the real SDK `query()` path and an offline scripted subprocess. |
| `npm run harness:validate:agentsdk-mcp-probe` | STAB-04 SDK/MCP behavior probe proving raw in-process MCP `mcp_message` calls, explicit `canUseTool`, and explicit hook callbacks remain distinct evidence paths. |
| `npm run harness:validate:agentsdk-packaged-proof` | STAB-02(d) no-live packaged SDK proof. Imports the SDK module from `app.asar.unpacked`, runs a scripted `query()` turn, records the resolved native subprocess command, and verifies controlled `CLAUDE_CONFIG_DIR`/`HOME` propagation. |
| `npm run instruction-root:integrity` | Instruction-root packaging/resource integrity check with summary artifact at `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. |
| `npm run proof:network-policy` | Network policy proof for the current shipped loopback plus Anthropic outbound policy. Use `-- --provider agentSdk --scripted-agent-sdk` for the STAB-02(c) dev proof, which runs the opt-in SDK adapter with an offline SDK subprocess and does not replace packaged subprocess evidence. |
| `npm run build` | Next/Electron build evidence for source and Electron entry surfaces. |
| `npm run desktop:pack` | Unsigned local macOS arm64 directory packaging plus instruction-root integrity. |
| `npm run desktop:dist` | Unsigned/unnotarized local-builder macOS arm64 DMG plus instruction-root integrity. |

Documentation-only governance tranches normally use static checks instead of frontend runtime commands. Runtime, SDK, permission, network, packaging, and release-significant tranches use the applicable gate family in `docs/RELEASE_QUALITY_GATES.md`.

Build, packaging, artifact, and release-evidence command details are recorded in `docs/BUILD_AND_RELEASE.md`.

## 4. Evidence Routing

| Change surface | Minimum evidence |
|---|---|
| Coordination, plans, decision-register pointers, or docs-only governance | `git diff --check` over affected docs/control-plane paths; targeted `rg` checks for retired rules or stale authority; link/path existence checks for new references; explicit no-runtime-code-change check. |
| Runtime engine contract, adapter, turn lifecycle, session events, or event schema | Focused Vitest coverage for touched runtime modules; `npm run typecheck`; broader `npm run test` when shared contracts move. |
| SDK options, permission overlay, tool descriptors, tool exposure, MCP wrappers, or hooks | Focused tests for options, permissions, descriptors, denied tools, unknown tools, and `npm run harness:validate:agentsdk-mcp-probe` when in-process SDK MCP behavior is load-bearing; `npm run typecheck`; broader tests when exposure semantics change. |
| Harness API, running workflow, session boot, SSE, interrupt, attachment, or validation behavior | Relevant unit/API tests; `npm run harness:validate:premerge` against a reachable local app; summary artifact review. |
| Network, API key, redaction, or provider policy | Relevant unit tests; `npm run proof:network-policy`; redaction or key-storage tests where touched. |
| UI workflow, professional-boundary copy, product identity, or navigation | Relevant component/library tests; targeted manual or browser review when layout/copy behavior changes; no prohibited professional/release claims. |
| Instruction-root, bundled resources, Electron packaging, release scripts, or distribution metadata | `npm run instruction-root:integrity`; `npm run build`; `npm run desktop:pack` or `npm run desktop:dist` when packaging behavior changes; `npm run harness:validate:agentsdk-packaged-proof` when packaged SDK resolver or transcript/HOME posture is in scope. |
| Future domain-engine adapters or operation proposals | Runtime tests plus explicit human-gate and professional-boundary review; no direct protected-domain writes unless a governed adapter workflow authorizes them. |

## 5. Evidence Artifacts

Machine-readable artifacts are preferred when available:

- harness premerge summary: `frontend/artifacts/harness/section8/latest/summary.json`;
- harness Section 9 summary: `frontend/artifacts/harness/section9/latest/summary.json`;
- instruction-root integrity summary: `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`;
- packaged SDK resolver/HOME proof summary: `frontend/artifacts/harness/packaged-agent-sdk/latest/summary.json`;
- test command output captured in terminal or run records when required by a tranche;
- plan/log closeout pointers in `plans/PLAN_2026-06-16_six_node_scc_resolution.md` and `plans/PLAN_COMPLETION_LOG.md`.

Evidence artifacts are derivative records. They support review and regression analysis, but they do not become decomposition truth, product requirements, lifecycle approval, release authorization, or professional acceptance.

## 6. Open Decisions

- Hosted CI provider, workflow location, and public/private data handling remain governed future decisions.
- Final release-label vocabulary, signing, notarization, publication, and attestation remain governed future decisions.
- Final coverage, performance, and platform-matrix thresholds remain `TBD`.
- Concrete provider/network implementation beyond the current shipped Anthropic path requires a bounded future implementation tranche and recorded decision evidence.
- D-APP-01 and D-APP-02 rule Pi pattern-corpus-only: no Pi adapter, fork, package import, Node 22 sidecar, runtime-floor migration, or spike work unless a future ruling explicitly reverses those boundaries.
