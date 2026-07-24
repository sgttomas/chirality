# Concept Comparison and Recommendation

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

## Headline

All three concepts can fit the accepted Gate-2 envelope. Concept B is the most
governance-forward but the least aligned with the owner's stated current
priority. Concept A is the clearest artifact-first correction. Concept C best
holds the intended long-term product model, provided Workroom—not the last
visited surface—is the initial default.

**Recommendation:** select an explicit **Workroom-default hybrid**:

- Concept C's peer Workroom and Agent Room architecture;
- Concept A's Workroom-first startup and artifact emphasis;
- one shared activity shelf;
- contextual chat as a supporting dock/panel;
- Agent Room one deliberate action away and able to occupy the full workspace;
- no Agent-Room-first foyer.

This is a selection of Concept C with one explicit default-behavior refinement,
not a fourth concept.

## Weighted comparison

Scores use a five-point scale against `Evaluation_Rubric.md`. Weighted totals
are normalized to 100.

| Criterion | Weight | A — Workroom first | B — Agent Room first | C — Hybrid peers |
|---|---:|---:|---:|---:|
| Artifact primacy | 20 | 5 | 3 | 5 |
| Supervisory clarity | 15 | 4 | 5 | 5 |
| Runtime truthfulness | 15 | 5 | 4 | 5 |
| Task continuity | 15 | 4 | 4 | 5 |
| Migration safety | 10 | 5 | 4 | 5 |
| Professional calm | 10 | 5 | 3 | 5 |
| Accessibility | 10 | 4 | 4 | 4 |
| Implementation economy | 5 | 4 | 3 | 3 |
| **Weighted total** | **100** | **91** | **77** | **95** |

The numerical difference between A and C is not decisive by itself. C wins
because it treats supervised agent work as a first-class professional surface
without making it the first thing the user must confront.

## Structural comparison

| Question | A — Workroom first | B — Agent Room first | C — Hybrid peers |
|---|---|---|---|
| Default | Artifact canvas | Session/evidence room | Workroom recommended |
| Agent Room | Secondary top-level view | Home/foyer | Peer full-workspace surface |
| Chat | Bottom supporting dock | Persistent operator dock | Contextual panel/dock |
| Artifact continuity | Strongest | Good after centre switch | Strongest with cross-links |
| Empty/new project | Immediately useful | Potentially sparse | Immediately useful |
| Runtime limitations | Naturally unobtrusive | Most visible constraint | Explicit but contained |
| Supervising several sessions | Adequate | Strongest | Strong |
| Risk | Agent Room underweighted | Process dominates product | Greater implementation breadth |
| Matrix disposition | Retire SOW-005; modify DEL-08-02 | Modify both | Modify both |

## Common architecture selected regardless of concept

- Project Navigator and Artifact Canvas become separate responsibilities.
- Workbench and Pipeline are re-hosted contextual functions, not permanent
  product taxonomies.
- Chat remains mounted during active turns but no longer displaces artifacts.
- Agent Room is a rebuildable projection, never evidence authority.
- Raw transcript/tools/events live behind semantic activity.
- Existing providers, routes, queries, APIs, SSE, secure settings, and stored
  values remain compatible.
- `WorkspaceLayoutV2`, `ArtifactRef`, explicit `ContextSet`, and pure
  `OperatorProjection` are frozen before parallel implementation.

## Why not Concept A unchanged?

Concept A most directly fixes the current UI. Its weakness is product
positioning: describing Agent Room as secondary could let it remain a richer
version of today's sidebar streams. The desired spatial control room should be
able to occupy the full professional workspace when supervision is the work.
Concept C provides that without changing the startup priority.

## Why not Concept B?

Concept B is technically careful and would make runtime truth exceptionally
legible. It nevertheless organizes the product around process before artifact.
New projects would open to a sparse room, and today's missing global run
discovery/live cross-client subscription would shape the entire home
experience. It recreates, in a more disciplined form, the system-first problem
the redesign is meant to solve.

## Recommended freeze

| Decision field | Recommended selection |
|---|---|
| Primary home | Workroom |
| Desktop shell | Shared frame; Navigator + Canvas + contextual Inspector; shared Activity Shelf |
| Agent Room | Peer full-workspace surface, one action away |
| Compact shell | One primary region at a time with accessible region switcher |
| Artifact model | Persistent tabs, two-up compare, recent/pinned references |
| Context | Explicit visible context set; selection never silently transmits content |
| Chat | Contextual dock/panel, mounted while active, collapsed by default |
| Workbench | Context preparation inspector/focus view |
| Pipeline | Run action sheet/focus view preserving dispatch semantics |
| Activity | Collapsible shared shelf, semantic summary first |
| Initial artifacts | Markdown/text, deliverable, Git diff, agent return/evidence, validation, session/replay |
| State | Versioned v2 convenience state; retain v1 and existing keys |
| Matrix | Remove fixed visual requirement from target IA; retain routing/alias compatibility |
| Old UI | Compatibility-only until separate owner retirement act |
| Deferred | Runtime expansion, arbitrary graphs, scheduling, control plane, PDF/drawing/rich editing |

## Decomposition recommendation

Under the recommended selection:

- `SOW-005`: **MODIFY** to govern provider-neutral role/routing overview and
  legacy query/matrix compatibility, without a fixed 3x4 visual.
- `DEL-08-02`: **MODIFY** to retain alias, routing, validation, unavailable-
  persona, and launch-guard semantics. It does not own the new shell or Agent
  Room projection.
- `DEL-05-04`: narrow modification for the rebuildable Agent Room projection.
- `DEL-02-01`: shell integration owner.
- `DEL-02-02`: Workbench/Pipeline presentation consumer.
- `DEL-08-03`: dispatch semantic owner.

## Principal implementation tradeoff

The recommended hybrid is broader than Concept A. Control scope by making the
first implementation read-only and slicing it:

1. shared frame, state types, and projection types;
2. Workroom Navigator/Canvas;
3. Agent Room session/evidence projection;
4. re-hosted Chat/Workbench/Pipeline/settings;
5. accessibility, performance, and packaged parity.

The current shell remains the rollback path throughout.
