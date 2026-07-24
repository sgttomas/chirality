# Dialogue-Centred Concept Comparison

> **NON_AUTHORITATIVE — CONCEPT EVIDENCE**

## Recommendation

Select **Concept 2 — Collaborative Bench**.

It most directly expresses the product thesis:

- human and agent remain together in a durable central dialogue;
- the artifact being produced or inspected remains visibly beside them;
- focused artifact work can gain space without severing conversation;
- recorded agent workflow and parent–child hierarchy can be exposed in a quiet,
  canonical-evidence-only supervisory rail;
- full Agent Room supervision is available without turning it into the home
  screen.

Concept 1 is the safer and simpler implementation. Concept 3 is the most
inventive expression of artifacts emerging through dialogue. Concept 2 best
balances collaboration, professional artifact work, and optional orchestration
visibility.

## Weighted comparison

Scores use a five-point scale and the weights in `Evaluation_Rubric.md`.

| Criterion | Weight | 1 — Dialogue Studio | 2 — Collaborative Bench | 3 — Woven Dialogue |
|---|---:|---:|---:|---:|
| Dialogue centrality | 20 | 5 | 5 | 5 |
| Artifact collaboration | 20 | 4 | 5 | 5 |
| Context legibility | 10 | 5 | 5 | 5 |
| Supervisory visibility | 10 | 3 | 5 | 4 |
| Runtime truthfulness | 10 | 5 | 5 | 5 |
| Task continuity | 10 | 4 | 5 | 4 |
| Professional calm | 5 | 5 | 4 | 4 |
| Accessibility | 10 | 5 | 4 | 4 |
| Migration economy | 5 | 5 | 4 | 3 |
| **Weighted total** | **100** | **90** | **96** | **91** |

## Structural comparison

| Question | Dialogue Studio | Collaborative Bench | Woven Dialogue |
|---|---|---|---|
| Centre | Persistent dialogue column | Dialogue + active artifact pairing | Dialogue with inline work objects |
| Artifact focus | Widen right Desk | Expand artifact while retaining compact dialogue | Open focused viewer tied to exact thread anchor |
| Context | Explicit next-turn tray | Explicit attachments/context beside stable dialogue identity | Explicit context set plus provenance-bearing objects |
| Hierarchy | Separate Agent Room | Visible supervisory rail and expanded Agent Room | Separate Agent Room; returns link into dialogue |
| Strongest quality | Clarity and implementation economy | Complete product model | Work visibly emerging through conversation |
| Primary risk | Desk crowding and constrained artifact width | Responsive/layout complexity; rail may feel control-plane-like | Feed noise, status inference, virtualization/anchor complexity |
| `SOW-005` | Retire fixed matrix obligation | Modify to routing/compatibility semantics | Modify to routing/compatibility semantics |
| `DEL-08-02` | Modify | Modify | Modify |

## What is common to all three

- The real transcript and composer are central.
- Shared intent is not a stored UI object.
- Previewed material and agent-visible context are visibly distinct.
- Chat/session state remains mounted across adjacent surface changes.
- Agent hierarchy, where displayed, reflects canonical evidence only.
- Workbench and Pipeline are re-hosted without changing their semantics.
- Runtime APIs, routes, queries, SSE, providers, credentials, state migration,
  and old-UI compatibility remain unchanged.
- Local-model intent summarization is deferred.

## Why Concept 2 wins

Dialogue Studio gets the centre right but makes serious artifact work compete
inside one side Desk. Woven Dialogue captures the conversational emergence of
work beautifully, but it risks turning a professional workspace into a complex
rich-message feed and carries substantial anchor/virtualization complexity.

Collaborative Bench keeps the simplest essential relationship visible:

```text
human–agent dialogue  ↔  artifact being produced or examined
```

The optional supervisory rail adds exactly the capability the owner asked not
to lose: visible workflow and recorded parent–child hierarchy. Because it can
collapse completely and never owns authority, it supports rather than defines
the primary collaboration.

## Recommended freeze if selected

| Field | Concept 2 selection |
|---|---|
| Default | Balanced Bench |
| Dialogue | Anchored, minimum readable width, never unmounted by in-shell mode changes |
| Artifact | Adjacent active working area; explicit artifact-focus mode retains compact dialogue |
| Context | Exact next-turn attachment/context receipt; no automatic inclusion |
| Hierarchy | Collapsible canonical supervisory rail; expandable Agent Room |
| Workbench/Pipeline | Adjacent working-area modes with current query/act semantics |
| Chat controls | Persona, transcript, permissions, composer, Send, Interrupt in anchored dialogue |
| Activity | Compact left rail and selected-session evidence; raw detail expandable |
| Matrix | No target-shell matrix; legacy presentation retained for compatibility |
| Initial artifact ceiling | Current deliverable documents plus reachable evidence/materialized artifacts; no new arbitrary-file/Git API |
| Summarization | Explicitly deferred |
| Old UI | Retained until separate owner retirement decision |

## Implementation caution

Concept 2 must freeze stable dialogue identity separately from the adjacent
surface route before production work begins. It also needs responsive
prototypes at the packaged app's 1280×840 default and compact breakpoints
before broad component implementation.
