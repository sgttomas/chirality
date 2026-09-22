---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-04
package_id: PKG-03
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-012, SOW-015]
package_objective_refs: [OBJ-002, OBJ-003]
---

# Scope of Work — DEL-03-04

## Purpose and Objective Traceability

This Scope of Work defines `DEL-03-04` in service of project scope [SOW-012, SOW-015] and package objectives [OBJ-002, OBJ-003].

- **OUT-001** — App interrupt/terminal conformance and disconnect-continuity evidence for Runtime-owned lifecycle, true-terminal lock release, replay and secret protection.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

> #### Datasheet: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-03-04 |
> | DeliverableName | Interrupt, Cancel, and Terminal Outcome Handling |
> | PackageID | PKG-03 |
> | PackageName | Runtime Engine Contract and Turn Lifecycle |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-012, SOW-015 |
> | SupportsObjectives | OBJ-002, OBJ-003 |
> | AnticipatedArtifacts | App interrupt forwarding tests; Runtime terminal/lock and disconnect-continuity conformance evidence; current event/replay/redaction fixtures |
>

### CLM-003 — Attributes

The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn.

Every accepted turn requires durable recoverable input and a truthful terminal outcome; the Runtime session store holds canonical evidence and native thread linkage. Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Required Handling | Source |
> |---|---|---|
> | User interrupt | `POST /api/harness/interrupt` aborts the active provider request, yields interrupted `process:exit`, and persists `turn.interrupted` for explicit user interruption. | `docs/PRD.md` Section 8.3, FR-019; `docs/PRD.md` Section 7.4; D-APP-40 |
> | Client disconnect | Unsubscribe the browser stream without interrupting or releasing the active turn. Reattach by sequence to continuing/completed state (D-GOV-43; SPEC §11). | `docs/SPEC.md` Section 11 |
> | Runtime/provider failure after input acceptance | Accepted input remains recoverable and replay shows terminal failure/cancellation status. | `docs/PRD.md` Section 7.10 |
> | Concurrent turn attempt | Must not create a second active turn for the same session; return `TURN_IN_PROGRESS`. | `docs/PRD.md` Section 8.3, FR-018 |
> | Malformed trailing event log write | Replay ignores malformed trailing lines and preserves valid prior events. | `docs/SPEC.md` Section 9.2; `docs/PRD.md` Section 7.10 |
> | Secret-bearing error or payload | Runtime events, logs, tool artifacts, and provider errors must redact secrets and avoid storing API keys. | `docs/CONTRACT.md` Section 1.5, K-EVENT-6; `docs/SPEC.md` Section 9.2 |
>

### CLM-005 — Interrupt and durable terminal evidence

Explicit user interruption must reach the active Runtime turn, release turn ownership on termination, and preserve a truthful terminal outcome. Accepted input and attachment references must remain recoverable after failure. A disconnected renderer stops receiving frames; disconnection by itself must not cancel the turn or release active-turn ownership. Reattachment must expose the continuing or completed turn consistently.

Malformed-tail tolerance, unique event identity, append-only records, and the surviving secret-protection requirement remain verification obligations. No compatibility mapper or legacy SDK test substitutes for evidence on the live Codex path; the redaction gap is retained under P-12.

Verification hooks: `projects/chirality-runtime/tests/app-owned-composition.test.ts`, `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/daemon.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

### CLM-006 — References

> ##### References
>
> - `docs/CONTRACT.md` Section 1.4 and 1.5, especially K-ENGINE-1 through K-ENGINE-4 and K-EVENT-2 through K-EVENT-6.
> - `docs/SPEC.md` Sections 8.4, 9, 10, 11, 17.1, 19.2, and 19.3.
> - `docs/TYPES.md` Sections 7.1 through 7.4.
> - `docs/PRD.md` Sections 5, 6.1, 7.4, 7.10, 8.3, and 8.12. Earlier D-APP-38 MATCH/warning statements are dated observations; consult current _REFERENCES.md observed bytes separately from accepted corpus pins.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-03 / DEL-03-04 and SOW-012 / SOW-015 rows.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

> #### Specification: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling
>

### CLM-008 — Scope

App scope is forwarding explicit interrupt and verifying the Runtime-owned lifecycle. Prove durable accepted input, truthful terminal outcomes, terminal lock release, malformed-tail replay tolerance and secret protection. Disconnect only unsubscribes; it is not a cancellation test subject. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-03-04-REQ-001 | The implementation shall preserve the `/api/harness/interrupt` route as the public interrupt endpoint for active turns. | `docs/SPEC.md` Section 17.1; `docs/PRD.md` Section 8.3, FR-019 |
> | DEL-03-04-REQ-002 | Interrupt handling shall abort the active provider/model request for the target session when one exists. | `docs/PRD.md` Section 8.3, FR-019; `docs/SPEC.md` Section 10.1 |
> | DEL-03-04-REQ-003 | Interrupt handling shall yield an interrupted `process:exit` browser-facing event where an active SSE turn stream is present. | `docs/PRD.md` Section 8.3, FR-019; `docs/PRD.md` Section 7.4 |
> | DEL-03-04-REQ-004 | Client disconnect SHALL unsubscribe only. Runtime retains the active turn and lock; reattachment recovers ongoing/completed state without resending the prompt. | `docs/SPEC.md` Section 11 |
> | DEL-03-04-REQ-005 | Runtime failure after `turn.accepted` shall leave accepted user input recoverable and shall persist a terminal failure or cancellation status. | `docs/PRD.md` Section 7.10; `docs/CONTRACT.md` Section 1.5, K-EVENT-2 and K-EVENT-3 |
> | DEL-03-04-REQ-006 | Every accepted turn shall terminate durably with a success, failure, cancellation, or interruption outcome. | `docs/CONTRACT.md` Section 1.5, K-EVENT-3; decomposition SOW-015 |
> | DEL-03-04-REQ-006A | Explicit user interruption SHALL persist turn.interrupted under D-APP-40. Disconnect is not a cancellation. System shutdown/restart terminal taxonomy remains a specific contract-alignment task; preserve the actual reason without recoding history. | D-APP-40; `docs/SPEC.md` Section 9.3; `docs/TYPES.md` Section 7.3 |
> | DEL-03-04-REQ-007 | Terminal outcomes SHALL remain truthful and durable; preserve original upstream Codex signals alongside normalized outcomes, with secret redaction before every sink. | `docs/CONTRACT.md` Section 1.4, K-ENGINE-4; `docs/SPEC.md` Section 10.3 |
> | DEL-03-04-REQ-008 | Terminal event records shall follow the versioned `HarnessEvent` shape: `schemaVersion`, `eventId`, `sessionId`, optional `turnId`, optional `parentEventId`, `timestamp`, `type`, and `data`. | `docs/SPEC.md` Section 9.1; `docs/TYPES.md` Section 7.3 |
> | DEL-03-04-REQ-009 | Terminal event writes shall append newline-delimited JSONL, use unique event IDs, avoid secrets, and remain replayable when a malformed trailing line exists. | `docs/SPEC.md` Section 9.2 |
> | DEL-03-04-REQ-010 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` Section 11 |
> | DEL-03-04-REQ-011 | Release active-turn state at completion, interrupt, failure or other terminal cancellation; a renderer disconnect MUST NOT release or cancel the continuing turn. | `docs/PRD.md` Section 8.3, FR-018 and FR-019; decomposition SOW-012 |
> | DEL-03-04-REQ-012 | Terminal outcome handling shall redact secrets and avoid storing API keys in runtime events, logs, provider errors, or tool artifacts. | `docs/CONTRACT.md` Section 1.5, K-EVENT-6; `docs/SPEC.md` Section 9.2 |
> | DEL-03-04-REQ-013 | Normalize upstream terminal signals for truthful presentation and durable outcomes while preserving original upstream event identity/payload subject to structural redaction. | `docs/SPEC.md` Section 10.3; `docs/TYPES.md` Section 7.4 |
> | DEL-03-04-REQ-014 | Expose observable Runtime active-turn state sufficient to prove terminal release and disconnect continuity; use the Runtime turn-state route and TurnRegistry as verification loci. | Decomposition anticipated artifacts; `docs/PRD.md` Section 8.3, FR-018 |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | Product-owned runtime boundary | Terminal behavior belongs behind `AgentEnginePort` / `RuntimeEngineContract`; SDK APIs do not define public semantics. | `docs/CONTRACT.md` Section 1.4, K-ENGINE-1; `docs/SPEC.md` Section 10 |
> | Runtime event and audit mirror contract | Terminal outcomes are persisted as Chirality `HarnessEvent`s in append-only JSONL. | `docs/CONTRACT.md` Section 1.5; `docs/SPEC.md` Section 9 |
> | Browser SSE compatibility contract | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | `docs/SPEC.md` Section 11 |
> | Route adapter rule | The application-owned Runtime service owns admission, one active turn per session, accepted-input persistence and durable terminal outcomes. The App route validates and forwards requests over the retained socket API and loopback HTTP/SSE channel. A renderer disconnect only unsubscribes; the turn and lock remain with Runtime until its terminal outcome. Explicit Stop interrupts the turn. | `docs/SPEC.md` Section 10.4 |
> | Source-state status | `docs/PRD.md` was reconciled in an earlier D-APP-38 snapshot; consult current `_REFERENCES.md` observations and the accepted corpus separately. | `_REFERENCES.md` REF-006; D-APP-38 |
>

### CLM-011 — Verification

Verify explicit Stop during an active turn, terminal durability and lock release after completion/failure/interruption; separately verify disconnect preserves the active turn and replay by sequence. Exercise unique IDs, append-only writes, malformed trailing JSONL and accepted-input recovery on the Runtime store. Redaction checks must cover events, logs, provider errors, artifacts and renderer delivery on the live path. System-shutdown/restart taxonomy is a specific remaining alignment task. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-012 — Documentation

Required artifacts are current interrupt and disconnect-continuity tests, terminal-mapping evidence, malformed-tail replay results, and sink-specific redaction checks. Documentation must distinguish D-APP-40 user interruption from non-user cancellation and record the current system-shutdown/restart reason mapping. Current loci are the Runtime coordinator/TurnRegistry/store and App forwarding tests, not a legacy mapper-only result. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-013 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

The 2026-07-12 UPD-117 observation concerned the earlier App lifecycle. Current observability is the Runtime turn-state route and `projects/chirality-runtime/packages/daemon/src/turn-registry.ts`; prove terminal release and disconnect continuity using the tests in CLM-011.

- **AC-001** — The DEL-03-04 outputs preserve the public interrupt route and SSE compatibility, release active-turn state at true terminals while preserving disconnect continuity, persist truthful terminal outcomes for accepted turns, and structurally redact secrets on the current Runtime path.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

> #### Procedure: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling
>

### CLM-015 — Purpose

Produce App forwarding and verification evidence over Runtime-owned interruption, durable terminals and true-terminal lock release. Disconnect is subscription cleanup only; verify reattachment by sequence. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-016 — Prerequisites

Use current SPEC §§9–11, D-GOV-43/D-APP-127 and the extracted `Dependencies.csv`; read each real edge instead of assuming missing extraction. App consumes the Runtime engine boundary, coordinator/TurnRegistry and canonical session store. Coordinate contract/locking with DEL-03-01/02, stream fixtures with DEL-03-03 and durability with PKG-05. Formal edge amendments remain outside this record repair.

### CLM-017 — Steps

1. Bind current App forwarding and Runtime coordinator/store source identities.
2. Build a trigger matrix for completion, explicit Stop, failure and system cancellation; record disconnect separately as subscription-only.
3. Verify accepted input is durable before execution and each true terminal releases ownership with truthful durable outcome.
4. Disconnect and reattach by sequence; prove continued work and no duplicate prompt.
5. Verify explicit user interruption under D-APP-40 and keep the system-shutdown/restart taxonomy gap visible.
6. Test append-only unique event records, malformed trailing writes and replay recovery.
7. Test structural redaction before events, logs, artifacts and renderer output; no legacy test substitutes for this live-path proof.
8. Preserve exact source/results and unmet checks.

Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-018 — Verification

Required checks: explicit Stop reaches the active turn; completion/failure/interrupt produce durable terminals and release the lock; disconnect preserves ongoing work; sequence replay restores current state; malformed trailing JSONL leaves prior valid records recoverable; secret fixtures are structurally redacted before every sink. Record system-shutdown/restart taxonomy separately until aligned. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-019 — Records

Preserve source-bound interrupt, terminal, disconnect/replay and malformed-tail results, unique-ID/append evidence, current mapper taxonomy and redaction outputs for each sink. Keep the D-APP-40 ruling as user-interruption authority; old disconnect-cancellation and fixed-event tests are historical. Link Section 9 checks that actually cover the current Runtime subject.

- **VER-001** — Verify current interrupt, true-terminal release, disconnect/replay continuity, malformed-tail tolerance, structural redaction and extensible-event checks in CLM-011/018.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling

> #### Guidance: DEL-03-04 Interrupt, Cancel, and Terminal Outcome Handling
>

### CLM-021 — Purpose

Make accepted-turn persistence, explicit interruption, terminal release and replay testable on the Runtime-owned lifecycle. Closing the renderer does not cancel work; an accepted turn still requires a durable terminal outcome. Preserve complete upstream events, secret protection and the professional boundary. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-022 — Principles

Persist accepted input before execution and a truthful terminal outcome after it. Release ownership at true termination; renderer disconnect preserves active work. Preserve complete upstream events and structural secret protection together. Runtime records explain activity but do not approve, issue or certify deliverables. Verification hooks: `projects/chirality-runtime/tests/turn-hardening.test.ts`, `projects/chirality-runtime/tests/turn-registry.test.ts`, `projects/chirality-runtime/tests/app-owned-composition.test.ts`, and `frontend/src/__tests__/api/harness/turn-registry-routes.test.ts`. These are named checks, not a claim that this record repair ran them or supplied missing live evidence.

### CLM-023 — Considerations

SPEC §11 requires unsubscribe without interruption and sequence-based reattachment. Explicit Stop remains a user interruption under D-APP-40. The separate system-shutdown/restart taxonomy difference remains open for current contract alignment. Malformed trailing JSONL must not erase valid history and secret-bearing payloads must be redacted at each sink. Current observed reference state lives in `_REFERENCES.md`; historical hash statements do not establish currentness.

### CLM-024 — Trade-offs

Runtime centralizes true terminal cleanup; transport cleanup only detaches the renderer. Preserve the accepted D-APP-40 user-interruption meaning and keep system cancellation mapping explicit. Failures must not falsely claim durable records; any retry must preserve unique event identity and avoid duplicate terminal outcomes. A changed accepted outcome taxonomy or durability guarantee requires its owning decision.

### CLM-025 — Examples

> ##### Examples
>

### CLM-026 — User interrupt during active stream

> ###### User interrupt during active stream
>
> 1. A turn has already persisted `turn.accepted`.
> 2. The user calls `/api/harness/interrupt`.
> 3. The active provider/model request is aborted.
> 4. The browser stream receives interrupted `process:exit`.
> 5. The active-turn lock is released.
> 6. A terminal runtime outcome is persisted as `turn.interrupted`.
>
> Sources: `docs/PRD.md` Section 7.4 and Section 8.3; `docs/CONTRACT.md` Section 1.5.
>

### CLM-027 — Client disconnect

1. A renderer is subscribed to an active Runtime turn.
2. It disconnects; only its subscription ends.
3. Runtime keeps the active turn and lock and continues recording events.
4. Reattachment by sequence recovers missed activity and the current/terminal state without resending the prompt.
5. Malformed-tail tolerance preserves prior valid records.

Verify with SPEC §11/§9.2 and the current Runtime/App tests in CLM-018.

### CLM-028 — Provider failure after acceptance

> ###### Provider failure after acceptance
>
> 1. Accepted user input is already durable.
> 2. Provider/model execution fails.
> 3. Terminal failure is mapped into Chirality-owned `HarnessEvent` form.
> 4. Browser error/exit behavior remains SSE-compatible.
> 5. Runtime replay can reconstruct accepted input and terminal failure/cancellation status.
>
> Sources: `docs/PRD.md` Section 7.10; `docs/SPEC.md` Section 9.
>

### CLM-029 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | DEL-03-04-CONFLICT-001 | Resolved by D-APP-40: explicit user interruption is a durable `turn.interrupted` terminal outcome; `turn.cancelled` is reserved for non-user cancellation. | `execution/_Coordination/_DECISIONS/D-APP-40_RULING_2026-06-21.md` | `docs/SPEC.md` Section 9.3; `docs/TYPES.md` Section 7.3; `docs/PRD.md` Section 8.3 FR-022 after ADQ-05 reconciliation | `Datasheet.md` Conditions; `Specification.md` Requirements and Verification; `Procedure.md` Steps and Verification | Apply D-APP-40 Option B. | Ruled 2026-06-21 |
>

### CLM-030 — Source-State Notes

Reference observations must be bound to actual source bytes in `_REFERENCES.md`; the accepted corpus pin is not refreshed by this repair. Current interrupt/terminal evidence loci are the Runtime coordinator, TurnRegistry and store plus App forwarding tests in CLM-011. Live redaction, malformed-tail and system-cancellation checks remain open where no current result is recorded.

### CLM-031 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

The repeated 2026-07-12 UPD-117 note is historical. Current observability and verification are the Runtime turn-state route, TurnRegistry and CLM-011/018 checks; old RunningHarnessTurn.cancel and disconnect-cancellation evidence do not establish current continuity.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-012 SOW-015 OBJ-002 OBJ-003 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
