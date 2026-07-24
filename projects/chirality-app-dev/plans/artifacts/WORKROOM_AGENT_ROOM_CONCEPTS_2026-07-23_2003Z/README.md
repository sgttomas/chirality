# Workroom and Agent Room Concepts

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

**Evidence basis:** `3c9ff297a4037d509bc930d1f607daf56769804d`
**Scope ceiling:** SCA-APP-004 Gate-2 assessment accepted by the owner on
2026-07-23.

This packet compares three possible information architectures before the
owner selects the design basis for Gate 3:

1. Concept A — Workroom-first;
2. Concept B — Agent-Room-first;
3. Concept C — hybrid Workroom with a peer Agent Room.

These documents do not amend decomposition, authority, runtime contracts, or
production code. They do not authorize retirement of the current interface.

## Common constraints

- The shared runtime remains the only owner of engines, credentials, sessions,
  delegation, canonical events, interruption, and model residency.
- Project adapters remain the source of files, artifacts, deliverables,
  protected paths, deterministic acts, and domain gates.
- Runtime events explain activity but do not accept or approve work.
- UI projections are rebuildable convenience state, never project truth.
- Existing routes, query parameters, browser APIs, SSE events, provider
  composition, and stored operator state remain compatible.
- The Agent Room represents only current runtime capability.

## Packet contents

- `Journey_Audit.md` — task-based diagnosis of the live interface.
- `Salvage_Assessment.md` — current and published component evidence.
- `Concept_A_Workroom_First.md`
- `Concept_B_Agent_Room_First.md`
- `Concept_C_Hybrid.md`
- `Evaluation_Rubric.md`
- `Concept_Comparison.svg`
- `Concept_Comparison.png`
- `Method_and_Attribution.md`
- `Comparison_and_Recommendation.md`
- `Owner_Decision_Memo.md`
