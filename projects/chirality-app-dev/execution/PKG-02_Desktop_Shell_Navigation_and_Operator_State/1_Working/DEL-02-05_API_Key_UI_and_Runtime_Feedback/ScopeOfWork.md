---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-05
package_id: PKG-02
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-013, SOW-019, SOW-023]
package_objective_refs: [OBJ-001, OBJ-008]
---

# Scope of Work — DEL-02-05

## Purpose and Objective Traceability

This Scope of Work defines `DEL-02-05` in service of project scope [SOW-013, SOW-019, SOW-023] and package objectives [OBJ-001, OBJ-008].

- **OUT-001** — API-key UI and runtime-feedback contract for DEL-02-05, traceable to SOW-013, SOW-019, SOW-023, OBJ-001, and OBJ-008.
- **OUT-002** — Current account/Settings, attachment, typed-feedback and retry-state outputs for SOW-013, SOW-019, SOW-023 and OBJ-001/008, as adapted by D-GOV-43/D-APP-127. Codex credential custody and production S-8 replace the retired hosted-consent/supplier mechanisms.

**D-APP-80 concordance note (2026-07-28):** SOW-023 is supported here
through the selected-working-root attachment UI, including multi-select
preview, remove/clear controls, and retry-preserving draft and attachment
failure state. DEL-09-06 retains attachment, network, key, and renderer
security validation.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

Provide the App account and runtime-feedback experience, selected-project attachment controls, typed errors, and retry-preserving failure state. Codex owns credentials and the account login/logout methods. Chirality presents its own sign-in state without reading, copying, or relaying credentials; its sign-out must leave other Codex clients unchanged.

The effective Codex home shares the user configuration and resources by reference while keeping authentication and model-cache state private to Chirality. The user selects approval and sandbox policy for each project/turn. Retired hosted admission, root-private account consent, brokerage generations, model residency, and external local-model-server status are not current live-login prerequisites.

The account row and right-panel Settings retain their accepted presentation ownership. Labels and current state must be truthful, with unavailable or fixture state distinguished from verified live login. DEL-09-06 retains attachment, credential-IPC, renderer, and other surviving security verification. Broader role and exact account-indicator conflicts are accounted separately; this repair does not silently decide those rows.

Verification hooks: the production S-8 account check in `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md` and `projects/chirality-runtime/tests/app-owned-composition.test.ts`. Native outcomes require their actual recorded evidence.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131.

### Current acceptance obligations

1. Present one app-wide account using Codex-held credentials and Codex's login/logout flow. The effective home shares user configuration/resources by reference while keeping authentication private to Chirality. Per-root hosted consent and unchanged root-private login semantics are superseded by D-APP-127; user-selected project/turn permission policy remains explicit.
2. D-APP-108 Q7 permits a local-model-server status indicator and excludes an OpenAI/API service-health indicator. The later Codex account row shows authentication/account state, which is distinct from API service health. Verify truthful local-model status where shown and Codex account state without reopening Q7; D-APP-127 retires local-model residency as a live-login prerequisite.
3. The account row and right-panel Settings retain their accepted presentation loci. Account/runtime feedback and appearance controls must be truthful; fixture/unavailable state does not establish live readiness. Legacy key-storage panels, per-root account groups, supplier qualification and G3/G-CSP/G4 are not current live-login prerequisites under D-APP-127. Surviving attachment, renderer, credential separation and secret-protection guarantees remain required.
4. Live-login evidence follows the production S-8 check and the affected-check rule after invalidating source, configuration or packaging changes. The retired Root DEL-02-09 shared-login admission is not an awaited dependency. This wording does not supply a missing native result.
5. Current direct entry is HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS; TASK is delegated under Root/App instructions and D-APP-131 P06. Older Agent 0/1/2 and posture labels are dated carrier wording; verify truthful role/write-scope accountability without reopening the four-role ruling or claiming authority-corpus acceptance.

Basis: D-GOV-43 / topology A2 and D-APP-127; claim-level application D-APP-131. Verification hook: production S-8 in `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md`; unresolved Q7/role and native-result keys remain in the R5 accounting.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-02-05-V3-05. Ruled
questions applied here: Q7, Q8. Alignment writes WI-016, WI-017, WI-018, WI-019,
WI-020 performed in run `APP_SCA_APP_010_SEATING_2026-09-04`; dependency writes
DEP-007, DEP-008 were performed under D-APP-109/D-APP-110 on 2026-09-05; the extracted register now exists. No lifecycle, Checking Approval SHA,
dependency-acceptance, product, or release act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-02-05 API Key UI and Runtime Feedback

> #### Datasheet: DEL-02-05 API Key UI and Runtime Feedback
>
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-02-05 |
> | DeliverableName | API Key UI and Runtime Feedback |
> | PackageID | PKG-02 |
> | PackageName | Woven Dialogue Shell, Navigation, and Operator State |
> | ResponsibleParty | TBD |
> | Type | UX_UI_SLICE |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ContextEnvelope | S |
>

### CLM-003 — Attributes

Codex owns account credentials and login/logout. The App account row and right-panel Settings use the application-owned Runtime service and Codex account methods; the effective home shares user configuration/resources by reference and keeps Chirality auth private. The App must never read, copy or relay credentials, expose them in the renderer or persist them as project truth. Sign-out must leave another Codex client unchanged. S-8 on the production path, repeated after the consolidated signed build and affected changes, is the live-login evidence.

Typed runtime feedback preserves actionable error information, draft text and attachments for retry. Full upstream events remain inspectable under SPEC §11; old turn:error/process:exit names are compatibility evidence, not a closed protocol. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-004 — Conditions

Codex owns account credentials and login/logout. The App account row and right-panel Settings use the application-owned Runtime service and Codex account methods; the effective home shares user configuration/resources by reference and keeps Chirality auth private. The App must never read, copy or relay credentials, expose them in the renderer or persist them as project truth. Sign-out must leave another Codex client unchanged. S-8 on the production path, repeated after the consolidated signed build and affected changes, is the live-login evidence.

Runtime errors preserve retry context. Structural redaction applies to events, logs, artifacts and every renderer-facing error. Retained App safeStorage reports missing/storageUnavailable/decryptFailed/available only where that storage is still used; it is not Codex credential custody. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

### CLM-005 — Construction

Provide truthful account state, typed actionable errors and retry-preserving draft/attachment state through the current account row/Settings and ChatPanel. `HarnessErrorType` is consumed from `@chirality/runtime-contracts`; UI must not redefine it. Verify with `frontend/src/__tests__/components/settings-view-codex.test.tsx`, `chat-panel-failed-send.test.ts`, and `chat-panel-native-attachments.test.tsx` in the same directory, plus production S-8. Live structural redaction remains a separate required result.

### CLM-006 — References

> ##### References
>
> - `_CONTEXT.md`
> - `_DEPENDENCIES.md`
> - `_REFERENCES.md`
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
> - `docs/CONTRACT.md`
> - `docs/DIRECTIVE.md`
> - `docs/PLAN.md`
> - Earlier D-APP-38 observations are historical; consult current `_REFERENCES.md` observed hashes separately from accepted corpus pins.
> - `docs/SPEC.md`
> - `docs/TYPES.md`
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-112 resolves the SOW-023 traceability delta in favor of inclusion because decomposition v3.2 explicitly maps SOW-023 to DEL-02-05; the new anchor is derivative traceability, not a lifecycle decision.

### CLM-028 — Applied decomposition v3 carrier assignment (SCA-APP-008 Gate 5, 2026-09-03)

The earlier D-APP-56 key/SSE observations are dated compatibility history. Current account custody and presentation are governed by D-GOV-43/D-APP-127 and the controlling section; current verification is CLM-012 and production S-8.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-02-05 API Key UI and Runtime Feedback

> #### Specification: DEL-02-05 API Key UI and Runtime Feedback
>

### CLM-009 — Scope

Codex owns account credentials and login/logout. The App account row and right-panel Settings use the application-owned Runtime service and Codex account methods; the effective home shares user configuration/resources by reference and keeps Chirality auth private. The App must never read, copy or relay credentials, expose them in the renderer or persist them as project truth. Sign-out must leave another Codex client unchanged. S-8 on the production path, repeated after the consolidated signed build and affected changes, is the live-login evidence.

Scope also includes attachment selection/preview and typed actionable runtime errors with drafts/attachments retained for retry. Runtime engine internals, credential handling internals and security implementation remain with their owners; this UI consumes truthful results. Historical Anthropic-key convenience controls do not establish a live Codex prerequisite. Verification hooks: `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `woven-dialogue-controls.test.tsx`, and `chat-panel-folder-binding.test.tsx` in the same test directory. Current D-APP-36 render/browser evidence remains required; named checks are not reported results.

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Priority | Source |
> |---|---|---:|---|
> | DEL-02-05-R01 | Codex owns account credentials and login/logout. The App account row and right-panel Settings use the application-owned Runtime service and Codex account methods; the effective home shares user configuration/resources by reference and keeps Chirality auth private. The App must never read, copy or relay credentials, expose them in the renderer or persist them as project truth. Sign-out must leave another Codex client unchanged. S-8 on the production path, repeated after the consolidated signed build and affected changes, is the live-login evidence. | P0 | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
> | DEL-02-05-R02 | Display truthful Codex account state without credential material. Retained ui/env/none values describe legacy key compatibility only, not the live sign-in contract. | P0 | `docs/PRD.md` Section 7.7; `docs/SPEC.md` Section 16.2 |
> | DEL-02-05-R03 | Codex credential custody and effective-home separation govern current sign-in; the legacy Anthropic key-precedence chain is not a live Codex gate. | P0 | `docs/PRD.md` FR-030; `docs/SPEC.md` Section 12.3 |
> | DEL-02-05-R04 | Report unavailable/error sign-in truthfully. Where App safeStorage remains used, expose its typed failure without leaking secrets. | P0 | `docs/PRD.md` Section 7.7 |
> | DEL-02-05-R05 | Runtime errors shown in the UI must be typed and actionable, mapped to title, message, and next-step text. | P1 | `docs/PRD.md` FR-020; decomposition SOW-013 |
> | DEL-02-05-R06 | Runtime error states must preserve draft prompt content and attachments for retry. | P1 | `docs/PRD.md` Section 7.3 and FR-020 |
> | DEL-02-05-R07 | Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. | P0 | `docs/SPEC.md` Section 11; `docs/TYPES.md` Section 7.4 |
> | DEL-02-05-R08 | UI surfaces must not treat API keys, runtime logs, UI state, SDK transcripts, or chat drafts as authoritative project truth. | P0 | `docs/DIRECTIVE.md` Project Truth sections; `docs/TYPES.md` Section 1.7; `docs/CONTRACT.md` K-FS-1 and K-KEY-1 |
> | DEL-02-05-R09 | Any user-facing provider/SDK error detail exposed by this UI must be redacted for secrets. | P0 | `docs/PRD.md` FR-075 and NFR-002; `docs/CONTRACT.md` K-EVENT-6 |
> | DEL-02-05-R10 | Consume the canonical HarnessErrorType from @chirality/runtime-contracts; do not redefine Runtime taxonomy. Preserve typed actionable errors and upstream evidence subject to redaction. | P1 | `projects/chirality-runtime/packages/contracts/src/types.ts`; `projects/chirality-runtime/packages/contracts/src/errors.ts`; `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md` |
>

### CLM-011 — Standards

D-GOV-43/D-APP-127 govern current credential custody, private authentication and user-selected policy. K-EVENT-6 requires structural redaction at every sink; UI convenience state and credentials are never project truth. SPEC §11 requires complete upstream event preservation. S-8 and current typed-error/retry tests verify distinct obligations.

### CLM-012 — Verification

Verify S-8 sign-in/sign-out on the production path and after the consolidated signed build, with another Codex client unchanged and credentials absent from every sink. Check truthful unavailable/error states, canonical Runtime error imports, actionable error text and preserved draft/attachment retry state. Check current full-event presentation and sink-specific redaction. Retained safeStorage/key-precedence tests establish compatibility only. Hooks: settings-view-codex, chat-panel-failed-send and chat-panel-native-attachments component tests; Runtime app-owned-composition and codex-effective-home tests; production NATIVE_CHECKLIST.md S-8.

### CLM-013 — Documentation

Required artifacts are the account row/Settings feedback, canonical typed-error display and retry-preserving ChatPanel draft/attachment state. Verification loci are named in CLM-012; error enum is HarnessErrorType in @chirality/runtime-contracts. Retained safeStorage needs truthful typed errors where used. Missing live redaction/native outcomes stay open.

- **REQ-001** — Present Codex-owned account/login/logout through the App-owned Runtime service; share user configuration/resources by reference with Chirality-private authentication. The App never reads/copies/relays credentials, exposes them in the renderer, or treats account state as project truth. No retired hosted-consent/identity supplier gate is recreated.
- **REQ-002** — Where App safeStorage is still used, distinguish missing, storageUnavailable, decryptFailed and available. These are not a substitute for truthful Codex account state.
- **REQ-003** — Present the user-selected Codex approval/sandbox policy for the project/turn. A mode label does not establish actual enforcement or grant normative authority; retired per-root command-network consent is history.
- **REQ-004** — Current direct entry is HELP_HUMAN, HELPS_HUMANS or WORKING_ITEMS; TASK is delegated. Preserve scope/accountability and truthful enforcement limits. Exact older posture-label/carrier differences remain keyed for source alignment; no authority-corpus acceptance is inferred.
- **REQ-005** — Live-login claims require current production S-8 evidence, including credential separation and another Codex client's unchanged state, repeated after the consolidated signed build and invalidating changes. Fixture/unavailable state is labelled truthfully. DEL-09-06 retains attachment, credential-IPC, renderer and secret-protection checks; retired HOST-P1/POLICY-R1/ACCOUNT-WIRE-V1 and G3/G-CSP/G4 admission subjects are not current gates.

- **AC-001** — The Scope of Work preserves and traces all legacy source content to SOW-013, SOW-019, SOW-023, OBJ-001, and OBJ-008 without adding scope, reliance claims, lifecycle meaning, or obligations.

- **AC-002** — Account/Settings, attachment, typed-feedback and retry outputs satisfy REQ-001 through REQ-005 on the current Codex path, with source-bound S-8 and surviving security evidence; UI fixtures alone establish no live readiness.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-02-05 API Key UI and Runtime Feedback

> #### Procedure: DEL-02-05 API Key UI and Runtime Feedback
>
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define the working procedure to produce and verify the API key UI and runtime feedback slice for DEL-02-05 without expanding into runtime engine internals or dependency extraction.
>

### CLM-016 — Prerequisites

Dependency extraction ran under D-APP-109/D-APP-110 on 2026-09-05. `Dependencies.csv` is the formal extracted register; consult each edge and gate directly. This record repair neither changes an edge nor infers satisfaction from implementation. The current account service, canonical Runtime errors, ChatPanel retry state and S-8 evidence are the prerequisites. Retired consent/supplier gates are not awaited. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

### CLM-017 — Steps

1. Bind current account row/Settings and Runtime account method source identities.
2. Verify truthful account/unavailable states without credential material in renderer or project truth.
3. Execute production S-8 for sign-in/out isolation and another Codex client unchanged, repeating after the consolidated signed build and invalidating changes.
4. Verify canonical HarnessErrorType display with actionable title/message/next step.
5. Verify draft/attachment retry state and supported attachment controls.
6. Verify structural redaction before every sink and full upstream event preservation.
7. Retained App safeStorage states remain compatibility checks only where used. Record actual results and missing native/redaction evidence. Hooks: current settings-view-codex, chat-panel-failed-send and chat-panel-native-attachments tests plus Runtime codex-effective-home/app-owned-composition and S-8.

### CLM-018 — Verification

Execute the current account, typed-error, attachment/retry and redaction verification in CLM-012. Legacy key-precedence/SSE-name fixtures remain source-bound compatibility evidence only. Live S-8 and sink-specific secret checks remain required.

### CLM-019 — Records

Preserve current account/Settings, canonical error, attachment and retry implementation/test references; actual S-8 and sink-redaction outcomes; source/candidate identity; and unchanged accepted reference pins. Legacy key-precedence/hosted-consent proof records stay historical. Missing evidence is not an assumed pass.

### CLM-020 — Evidence Binding Table

Preserve actual source/candidate identities, canonical error-import review, component/integration outputs and production S-8 witness with credential isolation. VER-001 source-conversion evidence remains separately required before its reliance; VER-002 is current account/transport/security verification, not retired hosted-admission proof.

- **VER-001** — Run deterministic schema validation, source mapping, parity, checklist derivation, and render stability checks, followed by human review against the accepted legacy basis.

- **VER-002** — Verify current account/Settings behavior, canonical errors, attachment/retry state and production S-8 credential isolation, with surviving security/redaction checks and affected-check reruns after invalidating changes.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-02-05 API Key UI and Runtime Feedback

> #### Guidance: DEL-02-05 API Key UI and Runtime Feedback
>
> Historical D-APP-56 source observation (2026-07-12): the then-current REF-006 matched. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.
>

### CLM-022 — Purpose

> ##### Purpose
>
> This deliverable gives operators a clear UI for API key status and runtime failure recovery while preserving Chirality's governance boundary: key material and runtime convenience state are useful for operation, but they are not project truth.
>
> Sources: `_CONTEXT.md`; decomposition DEL-02-05 row; `docs/DIRECTIVE.md` Project Truth sections; `docs/CONTRACT.md` K-KEY-1; `docs/PRD.md` Sections 7.3 and 7.7.
>

### CLM-023 — Principles

Codex owns account credentials and login/logout. The App account row and right-panel Settings use the application-owned Runtime service and Codex account methods; the effective home shares user configuration/resources by reference and keeps Chirality auth private. The App must never read, copy or relay credentials, expose them in the renderer or persist them as project truth. Sign-out must leave another Codex client unchanged. S-8 on the production path, repeated after the consolidated signed build and affected changes, is the live-login evidence. Preserve upstream Codex method names, identifiers and payloads in the extensible event representation, normalize known items for presentation, and keep unfamiliar notifications inspectable. Structural secret redaction is required before persistence, logging, artifacts and renderer delivery; upstream preservation does not waive it. Typed actionable failures preserve retry state and never convert runtime/UI data into project truth. D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment.

### CLM-024 — Considerations

> ##### Considerations
>
> - The API key UI is a presentation/control surface. Actual key storage, provider handoff, redaction, and network policy belong to adjacent runtime/security deliverables.
> - Secure-storage unavailability needs a clear visible error because the PRD acceptance criteria explicitly require it, but the exact wording is not specified in the accessible source corpus.
> - Typed runtime error copy should be actionable without leaking secret-bearing provider detail.
> - The UI can show status and next steps, but should avoid language that suggests the app has approved, certified, or externally validated work.
> - Retry preservation should account for both draft text and attachments; attachment server validation remains outside this deliverable.
>

### CLM-025 — Trade-offs

The App receives Runtime service/App Server outcomes, displays typed actionable failure without secrets and retains draft/attachments for retry. It consumes canonical Runtime errors and full upstream events, rather than relying on the retired App TurnEngine path. Verify with CLM-012 current tests and S-8.

### CLM-026 — Examples

Current example: the user signs into Chirality through Codex; account state is shown without credentials, and sign-out leaves another Codex client unchanged. A failed send displays a typed actionable error and retains the draft/attachments for retry. Verify with CLM-012 checks and S-8; UI fixtures do not prove live qualification.

### CLM-027 — Conflict Table (for human ruling)

D-APP-38 established the reference-observation model. Earlier MATCH and hash-warning assertions are dated source snapshots. Read current observed hashes in `_REFERENCES.md` separately from the accepted authority-corpus pins; this repair does not refresh accepted pins or certify a corpus amendment. D-GOV-43/D-APP-127 settle current Codex custody, user-selected policy and extensible events. The exact account-indicator/old posture-label carrier differences remain explicit alignment work; they do not restore retired per-root consent or local-model residency gates.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-013 SOW-019 OBJ-001 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
| OUT-002 | SOW-013 SOW-019 SOW-023 OBJ-001 OBJ-008 | CLM-028 REQ-001 REQ-002 REQ-003 REQ-004 REQ-005 | AC-002 | VER-002 | Current account/typed-feedback fixtures, canonical contract checks, production S-8 and surviving attachment/renderer/credential/redaction evidence |
