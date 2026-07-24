# Woven Dialogue Package Returns

**RunID:** `APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23`
**Fan-in verdict:** `ACCEPTED_WITH_REVIEW_CORRECTIONS`
**Lifecycle effect:** none

## PKG-02 return

Implemented the rollback-safe `chirality.woven-workspace/v1` convenience-state
store and honest Work projection. The store can copy recognized legacy
file-tree geometry into Navigator geometry, records which fields were mapped,
and leaves legacy keys intact. Work displays only admitted items; absent plan
or task evidence is shown as absent rather than inferred.

The integration owner composed these pieces into the Navigator, the persistent
primary dialogue viewport, the Work/Agents coordination panel, and the
collapsible Activity Shelf. Switching the project root clears project-scoped
artifact and replay references without deleting the prior project's data.

## PKG-05 return

Implemented provider-neutral semantic projection of canonical UI events and a
GET-only selected-session replay boundary. Replay is bounded, identifies its
source session, suppresses foreign-session content, and does not expose send,
interrupt, permission, resume, boot, delete, or lifecycle actions. The primary
live dialogue remains mounted while the replay lens or an artifact is focused.

## PKG-08 return

Implemented exact-record hierarchy construction, presentation-only guarded
session selection, and an inert compatibility description for Pipeline
dispatch. Parentage is never inferred. Rooted sessions are shown as recorded;
detached, unresolved, and cyclic records remain visible in a separate unsafe
relationship group with their exact recorded parent identifiers and
availability status.

The established `ORCHESTRATE` compatibility alias remains mapped to
`PROJECT_SETUP`. No execution or delegation behavior was added.

## Integration return

The new Woven Dialogue shell is the default composition for `/`, `/chat`,
`/pipeline`, and `/workbench`. Existing query parameters continue to resolve,
and `?legacy=1` opens the preserved loop-first UI in a separate window so the
new shell's primary dialogue is not unmounted. No runtime contracts, public
event names, browser API shapes, credentials, model residency, dependencies,
or lifecycle behavior changed.
