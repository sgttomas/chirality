# PLAN — Active Roadmap

This document is the active roadmap for planned work in the Chirality project execution system.

---

## 1. Current Architectural Direction

The current direction is:

- **`TASK` is the canonical Type 2 shell** for new bounded workflows.
- **Profiles stay small and rare.** `DELIVERABLE_TASK` remains the main compatibility profile; any additional profile must justify shell-level behavior rather than method prose.
- **Method logic moves into skills.** Recurring bounded execution methods should be expressed as repo-native skills with the four canonical skill documents.
- **Deterministic steps move into tools.** Validation, normalization, reporting, and repeatable transforms should be implemented as deterministic helpers under `tools/`.
- **Human-facing orchestration stays in Type 1 personas.** Type 1 agents own workflow composition, scope selection, batching, consolidation, and gate-controlled human interaction.
- **The existing `ORCHESTRATOR` pipeline is grandfathered.** The working `ORCHESTRATOR` path and its retained subordinate task-family agents remain valid while the rest of the Type 2 layer is rationalized.

This document tracks that direction at a high level. Implementation details are governed through issue, branch, and release records rather than private planning folders.

---

## 2. Active Roadmap Themes

| Theme | Status |
|-------|--------|
| Type 2 rationalization toward `TASK` + skills + tools | Active |
| Audit workflow normalization | Active |
| Evaluation workflow normalization | Active |
| TOOL_POLICY Tier 1 structural validator hardening | Ready |
| Drawing-extract architecture + tool hardening | Active |
| Hypergraph regression-hardening fixtures | Active |
| DOMAIN knowledge indexing follow-on | Active |

Unsplit backlog items still on the roadmap:

- Frontend normalization of matrix/pipeline selectors to the canonical post-wrapper architecture
- R11 tool-contract enforcement beyond current TOOL_POLICY coverage
- Content-hash enforcement for `_REFERENCES.md`
- Deliverable-level lock semantics for concurrent task execution
- Staleness-propagation tooling over dependency edges and baseline SHAs

---

## 3. Roadmap Detail

### Architecture and Governance

- Reduce remnant standalone Type 2 agents outside the grandfathered `ORCHESTRATOR` pipeline by moving bounded methods into `TASK` skills.
- Expand deterministic validation for skill tool-policy structure and R11/R12 tool-contract enforcement.

### Workflow Normalization

- Migrate audit execution out of standalone Type 2 agents into `TASK` skills, with a human-facing audit manager only where interaction gates require it.
- Preserve `EVALUATION` as a Type 1 manager while migrating evaluation specialists into `TASK` skills.

### Drawing Extraction

- Keep the drawing-extract pipeline target-aware, with deterministic tool contracts for per-page stubs, crop preparation, assembly, and validation.
- Harden drawing-extract tools around schema stability, path conventions, and reproducible validation fixtures.

### Focused Engineering Follow-ons

- DOMAIN knowledge indexing follow-on work.
- Hypergraph regression-hardening fixtures.
- KTY/object-ledger support fixtures for dependency and aggregation edge cases.

---

## 4. Historical Record

Completed migration slices, hardening notes, and pre-refactor roadmap narratives are historical records rather than the active roadmap surface.

---
