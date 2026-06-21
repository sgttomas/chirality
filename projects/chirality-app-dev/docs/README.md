# Chirality App Dev Docs

This `docs/` package is the app-dev governance and runtime-planning set for the Chirality desktop harness and bundled agent operating system.

The central project stance is:

> Provider-adapter-general, contract-owned, and Chirality-governed.

This docs package defines why the app exists, what must remain true, how the runtime is staged, and how validation, release-quality, build, and agentic workflow evidence are routed. It is an index and guidance surface; it is not a lifecycle approval, release authorization, professional approval, certification, sealing, authentication, or code-compliance claim.

## Document Map

| File | Role | Use |
|---|---|---|
| `DIRECTIVE.md` | Founding directive | Intent, filesystem truth, provider-adapter posture, human authority, professional boundaries, and stop rules. |
| `CONTRACT.md` | Invariant catalog | Binding constraints for runtime, provider/SDK adapters, permissions, events, packaging, network, release, agents, and future domain engines. |
| `SPEC.md` | Technical specification | Runtime mechanics, file structures, project surfaces, validation surfaces, and future platform mechanics. |
| `TYPES.md` | Vocabulary and identities | Canonical terms, identifiers, states, runtime records, and type targets. |
| `PRD.md` | Product requirements | Current product scope, functional requirements, milestones, known gaps, and accepted implementation direction. |
| `PLAN.md` | Strategic roadmap | Strategic runtime roadmap and sequencing rationale; not the active queue. |
| `WHAT-IS-AN-AGENT.md` | Agent model explainer | Operational definition of agents, bounded agent layers, and human accountability posture. |
| `VALIDATION_STRATEGY.md` | Validation strategy | Evidence classes, command routing, evidence artifacts, and open validation decisions. |
| `RELEASE_QUALITY_GATES.md` | Release-quality gates | Gate routing for governance, runtime, permissions, harness workflow, network, UI/claims, packaging, and future domain adapters. |
| `ISSUE_READINESS_PROFILES.md` | Issue-readiness profiles | Per-class evidence required before a `CHECKING -> ISSUED` transition (D-APP-34/36/37). |
| `BUILD_AND_RELEASE.md` | Build and release guide | Local command map, artifact locations, evidence profiles, packaging review, and future CI/release decisions. |
| `AGENTIC_DEVELOPMENT_WORKFLOW.md` | Agentic workflow | Authority map, current loop, tranche selection, TASK discipline, validation routing, and closeout expectations. |
| `BOUNDARY_REVIEW_CHECKLISTS.md` | Boundary review checklists | Product/professional-boundary and scope-boundary checklist package for DEL-01-03 and DEL-01-04. |
| `harness/reliance_boundary_register.md` | Reliance-boundary register | DEL-01-02 boundary rows, enforcement matrix, Section 9 test index, and residual-risk notes. |
| `harness/runtime_evidence_reconciliation.md` | Runtime evidence reconciliation | ADQ-04 PKG-03/PKG-04 evidence refresh, implementation crosswalk, current Section 9 IDs, and deferred residuals. |
| `MANIFEST.json` | Docs manifest | Machine-readable index of the docs package and key linked control-plane surfaces. |

## Coordination Pointers

Ordinary agentic work enters through:

1. `/Users/ryan/ai-env/projects/chirality/agents/AGENT_WORKING_ITEMS.md`;
2. `execution/_Coordination/_COORDINATION.md`;
3. `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`;
4. `execution/_Coordination/_LATEST.md`;
5. `execution/_Coordination/_DECISIONS/_REGISTER.md`.

The active autonomous development queue is `plans/PLAN_2026-06-20_autonomous_development_queue.md`,
released by D-APP-39. The D-APP-19 deliverable-inspection program
(`plans/PLAN_2026-06-20_deliverable_inspection_and_development_evidence.md`) is complete, and the
P0 governance cluster from its roadmap was applied 2026-06-20 (commit `a5ccfc591`): D-APP-37
PKG-10 status-truth repair, D-APP-34/36 issue-readiness profiles (`docs/ISSUE_READINESS_PROFILES.md`),
and the D-APP-38 reference-integrity model (authority-doc corpus `v1` reconciled via
`execution/_Reconciliation/References/reconcile_authority_corpus.py`). The loop-first pivot, live
packaged `agentSdk` read-tool proof, R6 Extensibility & MCP Boundary Maturity, Runtime Stabilization,
and SCC-resolution plans are completed closed history. `docs/PLAN.md` remains strategic roadmap
context, and `plans/PLAN_2026-06-13_runtime_completion.md` is retired runtime completion history.
Current state is discovered from the authoritative surfaces named by `_COORDINATION.md`, including
dependency/SCC snapshots under `execution/_Reconciliation/DepClosure/**`; there is no active
`NEXT_INSTANCE_STATE.md`.

## How Agents Should Use This Package

1. Use `DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, `TYPES.md`, and `PRD.md` for governance and product authority.
2. Use `PLAN.md` for strategic roadmap context, not ordinary tranche selection.
3. Use `VALIDATION_STRATEGY.md`, `RELEASE_QUALITY_GATES.md`, and `BUILD_AND_RELEASE.md` to select validation and evidence expectations.
4. Use `AGENTIC_DEVELOPMENT_WORKFLOW.md` for the agentic loop map, while following `_COORDINATION.md` for current entry protocol.
5. Use `MANIFEST.json` as an index only.
6. Treat unknowns as `TBD`, proposals as `PROPOSAL`, assumptions as `ASSUMPTION`, and human-gated decisions as unresolved until recorded in the decision register.

## Status

The active queue is `plans/PLAN_2026-06-20_autonomous_development_queue.md`. The live packaged
`agentSdk` read-tool proof, R6 Extensibility & MCP Boundary Maturity, Runtime Stabilization, and
SCC-resolution plans are completed history. Current runtime implementation truth remains in source,
tests, validation artifacts, and git history. Current coordination state is discovered rather than
tracked in a separate next-instance state file.
