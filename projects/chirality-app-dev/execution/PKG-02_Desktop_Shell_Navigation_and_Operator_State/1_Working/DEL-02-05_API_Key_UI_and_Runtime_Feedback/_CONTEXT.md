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

Provide API key entry/status UI, secure-storage feedback, selected-working-root
attachment controls, typed runtime errors, and retry-preserving failure states;
serve as the explicit App account/consent UX carrier by consuming
`HostedEngineConsentPort`, presenting one app-wide account and explaining
per-folder consent over the root-private app-owned `CODEX_HOME`, presenting
login/logout/account and consent/revocation state, distinguishing `missing`,
`storageUnavailable`, `decryptFailed`, and `available`, and offering the three
per-root command-network postures: no command network by default, ask per
destination with host/protocol context and the queued-request caveat plus
explicit-user-only `acceptForSession`, or labelled command network on through
`network_access = true`. Agent 0/1/2 role entry remains available for Codex
sessions; Agent 2/TASK is labelled `role not mechanically enforced` when G-ROLE
fails, and the product posture is labelled `Opt-in Preview`.

Applied decomposition row L311 (SCA-APP-010 Gate 5, 2026-09-04) notes: Explicit
App account/consent UX carrier; Root retains account/consent semantics. No
ambient `~/.codex` read or project-truth secret persistence. DEL-09-06 retains
server-side attachment, network, key, credential-IPC, and renderer security
validation. Live claims remain gated by the accepted Root/App account/consent
contract, G3, G-CSP, and G4. Presenting the account as app-wide (SCA-APP-010
SR-19) does not change the port's per-root login semantics; the root-private
login home is Root-owned and the shared-login amendment routes through Root
DEL-02-09 (OI-008).

## Anticipated Artifacts

API key and account settings panel; account row and popover; Settings view
account and folder groups; `HostedEngineConsentPort` UI adapter; per-root login
and command-network consent controls; attachment picker and preview chips; typed
storage/runtime error display; consent/revocation and retry-state tests

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
