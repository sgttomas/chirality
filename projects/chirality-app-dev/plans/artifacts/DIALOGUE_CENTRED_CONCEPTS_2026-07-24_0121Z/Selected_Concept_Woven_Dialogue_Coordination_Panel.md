# Selected Concept — Woven Dialogue with Work/Agents Coordination Panel

> **OWNER-SELECTED CONCEPT BASIS — NOT YET DECOMPOSITION OR IMPLEMENTATION AUTHORITY**

**Selected:** 2026-07-23
**SCA:** `SCA-APP-004`

## Product model

Dialogue is the primary workspace. Artifacts emerge through and remain linked
to dialogue. Work and Agents are two coordination lenses around that dialogue,
not alternative sources of truth.

```text
┌────────────────┬────────────────────────────────┬──────────────────────┐
│ NAVIGATOR      │ SELECTED DIALOGUE              │ COORDINATION PANEL   │
│                │                                │ [Work] [Agents]      │
│ Threads        │ Human ↔ primary agent          │                      │
│ Artifacts      │ or selected-session replay     │ workflow / task list │
│ Deliverables   │                                │          or          │
│ Files          │ Conversation                   │ agent hierarchy      │
│                │ Inline artifacts and returns   │                      │
│                │ Composer / permissions         │                      │
├────────────────┴────────────────────────────────┴──────────────────────┤
│ ACTIVITY SHELF: tools · tests · events · evidence · diagnostics       │
└───────────────────────────────────────────────────────────────────────┘
```

## Woven Dialogue

The centre renders the real human/agent conversation. Reference, proposal,
diff, validation, permission, return, and evidence objects may appear inline
only when backed by explicit project or runtime data. Each object exposes
provenance and may enter a focused viewer that returns to the exact dialogue
anchor.

Visible material is not automatically model context. The next-turn context
receipt sits with the composer and lists the exact references included in the
outgoing turn.

## Work view

The Work tab shows structured work only when it exists. It may combine several
classes, but never flatten their authority:

| Work class | Meaning |
|---|---|
| Governed project plan | Accepted project truth read from an admitted project source. |
| Human-approved execution plan | Approved bounded execution basis with its evidence reference. |
| Agent working plan | Agent-authored proposal or operational plan; not project authority. |
| Runtime task/checklist | Ephemeral execution state reported by the runtime or tool. |
| Inferred conversational possibility | Not rendered as structured work unless explicitly materialized. |

Every plan/task item identifies source, responsible/assigned agent when
recorded, status basis, related artifact/evidence, and currency. If no
structured plan exists, the panel says so rather than synthesizing one from
prose.

## Agents view

The Agents tab shows current and recent recorded sessions:

- role and bounded assignment where recorded;
- canonical parent–child hierarchy;
- engine, provider, actual model, and residency attribution when present;
- running, waiting, permission-needed, interrupted, failed, or terminal state;
- last meaningful evidence-backed activity;
- related task, return, and artifacts when recorded.

Every hierarchy edge equals canonical parentage. There are no editable edges,
empty spawn seats, inferred children, scheduling controls, or model controls.

Selecting a recorded session replaces the central region's visible content
with a clearly labelled replay lens:

- the primary human-facing session remains mounted and retains its composer;
- the replay lens is read-only and does not resume, switch, merge with, or
  mutate the primary live session;
- the header says whether the view is live, replayed, bounded, or stale;
- `Return to primary dialogue` remains persistently available;
- each session preserves its own scroll and selection;
- switching never transfers the primary draft, context receipt, permissions,
  interruption state, or session identity to the selected session.

## Cross-linking

- Select a task → highlight its recorded responsible agent.
- Select a recorded session → highlight its recorded task/work item.
- Select a return → open its originating dialogue object.
- Select an artifact → show recorded task/agent/provenance links.
- Select failed validation → link to the relevant artifact, task, and dialogue
  evidence when recorded.

Missing relationships remain unknown rather than being inferred semantically.

## Relocated Inspector responsibilities

- Next-turn context: composer context receipt.
- Artifact provenance: inline object and focused viewer.
- Model attribution: primary-dialogue or selected-replay header.
- Permissions: inline at the requesting turn.
- References: inline objects and focused artifact view.
- Raw tools/events: Activity Shelf.

This leaves the right panel dedicated to coordination.

## Runtime ceiling

The first implementation may show only session/replay/parentage, evidence, and
work/task data available through existing contracts. The current bounded
Agent 1 → optional read-only Agent 2 pilot is the only guaranteed hierarchy.
General plans, arbitrary task trees, direct child messaging, global AgentRun
discovery, and live cross-client observation remain evidence-conditional or
future scope.

Honest empty/currency states include:

- `No structured plan recorded.`
- `No delegated child recorded.`
- `Replay loaded — not a resumed dialogue.`
- `Refreshed at …`
- `Relationship not recorded.`
- `Bounded projection — open canonical evidence for detail.`

## Local-model summarization

A frequently refreshed local-model summary of conversational intent remains an
interesting future experiment only. It is not part of the selected concept,
not authoritative, and not required for implementation.

## Selection consequence

This selection supersedes the first concept recommendation and the unmodified
Woven Dialogue proposal as decision candidates. Gate 3 must now preview exact
decomposition wording. Production implementation remains blocked until Gates
3–5 are approved and executed.
