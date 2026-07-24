# Woven Dialogue Independent Review

**Verdict:** `PASS_AFTER_CORRECTION`
**Review posture:** read-only independent review followed by serialized root
fan-in

## Review coverage

Two independent reviewers examined:

- the provider-neutral projection and selected-session replay boundary;
- recorded parentage, attribution, currency, diagnostics, and incomplete
  hierarchy behavior;
- preservation of the primary live dialogue;
- Navigator and coordination-panel semantics;
- route and legacy-UI compatibility;
- landmarks, controls, narrow-window ordering, and operator-facing language.

## Corrections made during review

- Foreign-session replay events are suppressed and disclosed instead of being
  rendered in the selected session.
- Detached, unresolved, and cyclic session records remain visible and expose
  exact recorded parent identifiers without inferred placement.
- Agent cards expose source, currency, observation time, diagnostics, approval
  and return references, and recorded model selection using non-overstated
  labels.
- Session discovery refreshes when the primary session changes or streaming
  state crosses a boundary.
- Project-root changes clear project-scoped workspace references.
- Legacy UI opens separately so it cannot unmount the primary dialogue.
- Work/Agents and Activity controls use complete button semantics.
- Narrow layouts place Dialogue before Navigator in reading and focus order.
- Provider-specific empty-state wording was replaced with provider-neutral
  language.

The final boundary backcheck returned `PASS`: unsafe relationship cards expose
the exact recorded `parentSessionId`, state whether the parent record is
available, and remain under an explicit non-hierarchical disclosure.

## Preserved limits

The Agent Room describes only sessions discoverable through the existing
runtime surfaces. It does not imply arbitrary agent graphs, direct child
messaging, scheduling, automatic model routing, or project-control authority.
Work remains empty unless admitted project evidence is supplied.
