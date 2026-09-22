# Context: DEL-02-05 API Key UI and Runtime Feedback

## Identity

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| PackageID | PKG-02 |
| PackageName | Woven Dialogue Shell, Navigation, and Operator State |
| DeliverableID | DEL-02-05 |
| DeliverableName | API Key UI and Runtime Feedback |
| ResponsibleParty | TBD |
| Type | UX_UI_SLICE |
| ContextEnvelope | S |

## Package Scope

**ScopeDescription:** Dialogue-centred shell with an invariant centre dialogue,
left chat navigator, one-view-at-a-time right panel (files, document, workflows,
who is working, activity, session, settings), activity strip, composer context
line, account row and settings presentation, compatibility surfaces, and
non-authoritative local UI state.

**InclusionCriteria:** Human–agent dialogue, artifact collaboration, coordination presentation, and operator workflow behavior.

**Exclusions:** Runtime engine internals, canonical session/evidence ownership, arbitrary orchestration graphs, automatic intent inference, and project-control-plane authority.

## Deliverable Scope

Present the App account and runtime-feedback experience over the application-owned Runtime service and Codex's own account methods. The effective home shares user configuration/resources by reference with Chirality-private authentication. No credential read/copy/relay or renderer exposure is allowed; sign-out leaves another Codex client unchanged. Production S-8 and the affected-check rule replace retired hosted-consent, identity-supplier and G3/G-CSP/G4 admission gates (D-GOV-43/D-APP-127).

Provide selected-project attachments, typed actionable errors and retry-preserving drafts/attachments. App safeStorage states apply only where that storage is retained. Current role entry follows HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS with TASK delegated; exact old posture-label/account-indicator carrier differences remain keyed for source alignment.

## Anticipated Artifacts

Account row and Settings feedback; attachment picker/preview; canonical Runtime error display; retry-state tests; production S-8 credential-isolation evidence. DEL-09-06 retains attachment, credential-IPC, renderer and secret-protection checks.

## Traceability

| Field | Value |
|---|---|
| CoversScopeItems | SOW-013, SOW-019, SOW-023 |
| SupportsObjectives | OBJ-001, OBJ-008 |
| ContextEnvelopeNotes | Cohesive dialogue-input and runtime-feedback UI slice; DEL-09-06 retains server-side attachment, network, key, and renderer security validation. |

## Source Authority

This folder was scaffolded by ORCHESTRATOR from the accepted v3.2 SOFTWARE_DECOMP working surface. Downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership.

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-112 resolves the SOW-023 traceability delta in favor of inclusion because decomposition v3.2 explicitly maps SOW-023 to DEL-02-05; the new anchor is derivative traceability, not a lifecycle decision.
