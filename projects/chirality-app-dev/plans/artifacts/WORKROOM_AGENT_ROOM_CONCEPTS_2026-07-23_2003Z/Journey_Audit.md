# Current Journey Audit

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

**Evidence basis:** `3c9ff297a4037d509bc930d1f607daf56769804d`

## Diagnosis

The live interface is operationally capable but makes the chat loop the
default mental model. Files, deliverables, sessions, evidence, tools,
subagents, Workbench controls, Pipeline controls, and toolkit settings compete
inside a single right-hand tab strip. This reduces screen switching compared
with the former route-shaped UI, but it does not establish a durable object of
work.

The user can reach important information; the interface does not consistently
preserve what the user is looking at while another concern is inspected.

## Journey 1 — Find a deliverable and understand its state

### Current path

1. Select or verify the Working Root.
2. Open the right workspace sidebar.
3. Choose `Document`.
4. Choose a deliverable from a select control.
5. Choose `_STATUS.md` or another document.
6. Read the document in the narrow sidebar.
7. Switch to another tab to inspect files, losing the document view.

### Friction

- Deliverables are not a primary navigation collection.
- The selected artifact is constrained to a sidebar.
- Comparing status, context, dependencies, and source evidence requires
  serial tab switching.
- The artifact is subordinate to an idle or unrelated chat surface.

### Desired outcome

The deliverable appears in the Navigator, opens as a persistent canvas tab,
and retains links to its package, control documents, implementation evidence,
and relevant agent returns.

## Journey 2 — Read or compare an artifact while a turn runs

### Current path

1. Start the turn in the central chat surface.
2. Open `Files` or `Document` in the right sidebar.
3. Inspect the artifact in the available narrow region.
4. Switch to `Transcript`, `Tools`, or `Subagents` to monitor progress.
5. Reopen the artifact afterward.

### Friction

- The artifact and operational state compete for one sidebar.
- No persistent tab or side-by-side comparison model exists.
- The user must visually follow token/event activity to understand progress.

### Desired outcome

The artifact stays open in the canvas; a bounded Agent Room and collapsible
activity shelf show semantic progress without replacing it.

## Journey 3 — Launch a TASK-scoped Pipeline action

### Current path

1. Navigate to `/pipeline` or open the Pipeline sidebar tab.
2. Select category and task-scope controls.
3. Supply or inherit query parameters such as `category`, `taskScopeMode`,
   `scopeKey`, and `targetDeliverableKey`.
4. Return to the chat loop for execution feedback.

### Friction

- The distinction between configuring dispatch and supervising execution is
  spatially weak.
- Route mode, persona, and sidebar placement are implementation concepts the
  user must understand.

### Desired outcome

Pipeline becomes a bounded action sheet or inspector attached to the current
artifact/context. Its DECOMP/PREP/TASK/AUDIT semantics remain explicit, while
the resulting session appears in the Agent Room.

## Journey 4 — Review an agent return and its evidence

### Current path

1. Open `Sessions`.
2. Choose `Open`, which hydrates the bounded shared event buffer.
3. Move among `Transcript`, `Tools`, and `Subagents`.
4. Infer parentage, result, model attribution, and relevant evidence from
   separate views.

### Friction

- `Open` means replay hydration, not resuming a conversation.
- Hydration replaces the current bounded event buffer.
- The UI presents event categories rather than a coherent return.
- Canonical evidence and projection are not clearly distinguished.

### Desired outcome

A session or agent return opens as an evidence-linked artifact. The Agent Room
shows role, objective, parentage, actual engine/provider/model, last meaningful
activity, terminal result, and interruption state. Raw transcript/tool events
remain expandable.

## Journey 5 — Recover work after relayout or restart

### Current path

1. Pane widths/collapse state load from `chirality.layout.v1`.
2. Project root, toolkit settings, and chat drafts load from separate keys.
3. Sidebar tab and open artifacts are not represented as a coherent workspace.

### Friction

- Persistence is pane-oriented, not work-oriented.
- There is no tab/pinned/recent artifact state model.
- A replayed session can overwrite the visible event projection.

### Desired outcome

A versioned workspace state restores pane geometry, open/pinned artifacts,
selected session projection, and collapsed regions without becoming
authoritative. Existing v1 state remains rollback-safe.

## Journey 6 — Interrupt a running turn

### Current path

1. Observe the running state in chat.
2. Use the chat interruption control.
3. Inspect transcript/tools/subagent tabs for the outcome.

### Friction

- The control is bound to the chat surface rather than the governed running
  session.
- Terminal and tool cleanup evidence is dispersed.

### Desired outcome

Interrupt remains a runtime action but is available on the corresponding
Agent Room card and in the supporting chat surface. The terminal outcome and
canonical evidence are linked and unambiguous.

## Cross-journey findings

- The current provider/API layer is reusable; the principal defect is
  information architecture.
- Artifact persistence is the missing organizing concept.
- Chat should remain available but cease to occupy the default largest region.
- Semantic operator state is more useful than raw event-category tabs.
- The design must keep honest labels: replay is replay, projection is
  projection, and a visible session is not automatically an accepted AgentRun.
