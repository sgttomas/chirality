---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-09
package_id: PKG-02
decomposition_basis: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md@9f21e4b86c304343b92ccd9ef10895b28c1a4f48
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
---

# Scope of Work — DEL-02-09

## Purpose and Objective Traceability

This Scope of Work defines the production boundary for `DEL-02-09`,
Hosted Account and Consent Boundary, a `SECURITY_CONTROL` deliverable of
`PKG-02_Runtime_Product`. It serves project
scope item `SOW-104` and package objectives `OBJ-001`, `OBJ-002`, `OBJ-004`,
and `OBJ-007`, exactly as recorded in the applied deliverable register.

The accepted register row assigns this deliverable the per-root hosted-account
and consent boundary: `HostedEngineConsentPort`; root-private app-owned
`CODEX_HOME`; account/epoch and policy continuity; the `K-ROLE-2`
role-posture digest; Agent 0/1/2 role-entry parity with a labelled Agent 2/TASK
fallback; and the per-root three-posture command-network consent model. The
accepted Context Envelope is `M`.

The binding boundary is: **root-private account/consent boundary, ambient `~/.codex` excluded, labelled fallback**.
Consent never crosses root, account, or policy-digest drift, and hard
filesystem/network/process containment is unchanged.

The applied register records the anticipated write locus as `projects/chirality-runtime/**; projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/**`.
That locus is planning only and is not authorization to implement or write
there.

Current allocation is the runtime-project row in
`projects/chirality-runtime/execution/_Decomposition/RUNTIME_DELIVERABLE_REGISTER.csv`
and the approved exact `OWNERSHIP_OVERLAY.md` beside it. Actual application is
recorded at `projects/chirality-runtime/execution/_Coordination/MIGRATION_APPLICATION.md`.
Root retains instruction governance and D-GOV-20 boundary authority; Ryan Tufts
is the accountable human. Root-private account, consent and client-owned
responsibilities retain their meaning; runtime product relocation does not
reassign those boundaries.

## Deliverable Definition — Ontology

The six outputs below are the anticipated artifacts transcribed from the
applied register row and carrier `_CONTEXT.md`. Their detailed schemas and
implementation forms are not specified by the accepted sources and are not
invented by this Scope of Work.

- **OUT-001** — `HostedEngineConsentPort` contract.
- **OUT-002** — Root-private `CODEX_HOME` and account-continuity controls.
- **OUT-003** — `K-ROLE-2` digest schema.
- **OUT-004** — Agent 0/1/2 parity and labelled Agent 2/TASK fallback
  controls.
- **OUT-005** — Per-root three-posture consent-state model.
- **OUT-006** — Isolation, consent, and continuity tests.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — The applied register row and carrier `_CONTEXT.md` allocate
  `SOW-104` and `OBJ-001`, `OBJ-002`, `OBJ-004`, and `OBJ-007` to this
  deliverable and identify its type as `SECURITY_CONTROL` and Context Envelope
  as `M`.
- **CLM-002** — G0 A3 requires Agent 0/1/2 role entry always to be offered for
  Codex sessions. When `G-ROLE` cannot mechanically prove Agent-2
  non-delegation, explicit Agent 2/TASK remains offered and is labelled `role
  not mechanically enforced`; governed-workflow evidence from that posture is
  marked `instruction-asserted`. For the delegated-harness-native class,
  `K-SUBAGENT` non-delegation is instruction+config asserted, not
  mechanism-proven. Hard filesystem/network/process containment is unchanged.
- **CLM-003** — G0 A7 requires each canonical root to choose under consent
  among three command-network postures: no command network by default; ask per
  destination through `networkApprovalContext`; or labelled command network on
  with `network_access = true`.
- **REQ-001** — The hosted-account boundary shall use root-private app-owned
  `CODEX_HOME`; ambient `~/.codex` is excluded.
  Later binding disposition: D-GOV-36, `docs/governance_harness/_DECISIONS/D-GOV-36_managed_auth_custody_exception.md`,
  permits the daemon-owned exact trusted supplier authentication process for
  managed Codex authentication to use an explicitly configured built-in OS
  keyring under DEL-02-06/REQ-041's narrow custody exception. Each canonical
  root independently acquires authentication in its root-private app-owned
  context; cross-root credential copying, shared authenticated homes, ambient
  credentials, client/tool-worker credential access and plaintext fallback
  remain prohibited. Exact supplier, backend and process/storage boundary
  qualification is required before operational reliance; a custom adapter
  requires a demonstrated remaining gap.
  An account-only nonexecuting bootstrap auth namespace is permitted for
  sign-in before folder selection. It grants neither project/no-folder
  execution nor folder consent; bootstrap credentials are not copied into
  root contexts. Local profile/settings are neither client authority nor an
  additional cloud account. The target remains one OpenAI sign-in experience
  with independent folder consent; current documentation does not prove the
  actual multi-root experience. Authenticated project-scoped Unix control, no
  TCP control listener and operational/non-authoritative credential state
  remain unchanged. This does not accept B2 execution-context semantics.
  D-GOV-39 preserves that project-scoped baseline and recognizes the narrow
  dedicated authenticated account-only public Unix authority solely for
  nonexecuting bootstrap authentication, status/cancellation, and
  hosted-account lifecycle control or observation; project operations remain
  project-authorized. Account-only operations require their own accepted
  authenticated caller and operation authority, an active `HOST-P1` lease,
  current generations, and a compatible `ACCOUNT-WIRE-V1`/`POLICY-R1`
  contract and version/capability result, and cannot waive project
  prerequisites.
- **REQ-002** — The boundary shall preserve account/epoch and policy continuity,
  and consent shall not cross root, account, or policy-digest drift.
  Under D-GOV-36, global account switch/sign-out shall durably fence every
  hosted context in the active account generation. Local-model contexts are
  unaffected; folder disconnect is local to that folder. Retire tool/turn
  execution first, retain only necessary purpose-limited context for a
  separately authorized bounded remote-revoke attempt, then retire auth
  processes and clear local credentials, verifying cleanup. Ungranted,
  offline or impossible revoke proceeds to local cleanup with remote state
  unknown. Credentials shall not be retained indefinitely; no browser-wide
  or provider-global revocation is claimed. Human-approval assurance remains
  separate. Account binding and hosted readiness require one atomic current
  supplier snapshot containing both a stable opaque nonsecret account/user
  identifier and a stable opaque nonsecret provider-selected-workspace
  identifier. Provider-selected workspace means the supplier's current
  tenancy/workspace/account selection, never a folder, `canonicalRoot`,
  `projectId`, repository, window, caller hint, or other local locator. A
  partial, stale, absent, error, capability or version mismatch, or otherwise
  unqualified supplier or identity keeps
  `binding:{state:"unavailable",reason:"canonical-identity-producer-unavailable"}`
  and `hostedReady:false`; no fallback, mixed-version claim, project/no-folder
  execution, credential exposure, or private-supervisor access is permitted.
  These dispositions grant no implementation or operational act.
- **REQ-003** — The `K-ROLE-2` digest and role controls shall preserve the A3
  parity, label, and evidence-posture distinctions stated in `CLM-002` without
  changing hard filesystem/network/process containment.
- **REQ-004** — The per-root consent-state model shall preserve all three A7
  postures stated in `CLM-003`, with no command network as the default.
- **REQ-005** — In ask-per-destination posture,
  `networkApprovalContext` shall show host/protocol and shall preserve the
  caveat that a grant may unblock queued requests to the same destination;
  `acceptForSession` is allowed only by explicit user act.
- **REQ-006** — The labelled command-network-on posture shall use
  `network_access = true`.

A completion claim requires this deliverable's own accepted evidence for the
applicable outputs and requirements. The accepted sources specify no additional detailed per-output acceptance
criteria, implementation design, dependency set, schedule, or production tool.
The acceptance records below express only each inherited matrix evidence
expectation and its existing claim/requirement references for human review;
they add no threshold or implementation requirement. Nothing in this
Scope of Work lifts a hold, authorizes implementation, or creates dispatch
authority. Nine DEL-02-06 bindings remain held; R16-B separately disposed the
historical Tier-0 marker through continue-separate. The immutable compatibility
contract retains all ten historical markers, `root-runtime-1`, epoch 1.
DEL-02-06/REQ-027 remains specification, inventory and evidence planning only.
TM-ROOT-106 remains open; R18 closed TM-ROOT-122. No current implementation
identity, hold release or effective ownership transfer is supplied here. Acceptance of
this Scope of Work is itself a separate owner act against its exact bytes.

- **AC-001** — Own accepted evidence for the `HostedEngineConsentPort` contract within the account/consent boundary. Evaluation is HUMAN_REVIEW against CLM-001 REQ-001 REQ-002.
- **AC-002** — Own accepted evidence for root-private `CODEX_HOME`, ambient-home exclusion, continuity, and no cross-root/account/policy-digest consent. Evaluation is HUMAN_REVIEW against REQ-001 REQ-002.
- **AC-003** — Own accepted evidence for the `K-ROLE-2` digest schema and truthful role-posture distinctions. Evaluation is HUMAN_REVIEW against CLM-002 REQ-003.
- **AC-004** — Own accepted evidence for Agent 0/1/2 parity and the labelled Agent 2/TASK fallback without a mechanism-proven overclaim. Evaluation is HUMAN_REVIEW against CLM-002 REQ-003.
- **AC-005** — Own accepted evidence for the three postures, default, prompt content, grouping caveat, explicit-user-act condition, and labelled on-state. Evaluation is HUMAN_REVIEW against CLM-003 REQ-004 REQ-005 REQ-006.
- **AC-006** — Own accepted isolation, consent, and continuity evidence; no completion claim until that evidence is accepted. Evaluation is HUMAN_REVIEW against REQ-001 REQ-002 REQ-003 REQ-004 REQ-005 REQ-006.

## Production and Verification Method — Praxeology

The accepted sources allocate the artifact classes and boundary constraints,
but do not prescribe a production sequence, interface design, implementation
method, dependency, tool, schedule, or acceptance procedure. Those matters
remain for separately authorized and accepted later work; this Scope of Work does not
fill them by inference.

Verification evidence, when separately produced and accepted, must be the
deliverable's own evidence and must address only the accepted claims attached
to each output in the matrix below. `OUT-006` is the accepted artifact class
for isolation, consent, and continuity tests. G0 A7 additionally states that
`G-APPR` must prove prompt delivery and observe destination grouping
empirically at the exact pin; this Scope of Work neither performs that proof nor claims
its result.

No test result, contract candidate, schema candidate, or observed behavior can
accept this SOW, lift a hold, authorize implementation, create dispatch
authority, or change a lifecycle state.

## Governing Values and Decisions — Axiology

- **AX-001** — Historical source grounding is
  `plans/steers/chirality_app_v3_phase2_steer_root_2026-08-23.md`; the applied
  `DEL-02-09_Hosted_Account_and_Consent_Boundary` row in
  `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`; the
  carrier `_CONTEXT.md`;
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2
  `INIT-03`; and A3/A7 in
  `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`.
- **AX-002** — `INIT-03` carries the root-private account/consent slice with G0
  A3/A7, excludes ambient `~/.codex`, and does not itself create a Scope of
  Work, dependency, estimate, schedule, or activation state.
- **AX-003** — The anticipated write locus is a planning note, never write or
  implementation authority. Runtime implementation and any other act beyond
  these exact contract bytes require their own authority.
- **AX-004** — The A3 labelled fallback preserves truthful evidence
  calibration: `instruction-asserted` and `instruction+config asserted` are not
  restated as mechanism-proven.
- **AX-005** — The A7 consent model remains per canonical root. The default,
  prompt contents, destination-grouping caveat, explicit-user-act condition,
  and labelled on-state are preserved without adding another posture.
- **AX-006** — Unknown implementation and evaluation details remain
  unspecified rather than being inferred. The responsible party recorded in
  the applied register is Ryan Tufts; only the separate owner act can accept
  this SOW.

## Output and Evaluation Matrix

The matrix expresses each inherited evidence expectation as one acceptance
record for accountable-human review against its existing claim/requirement
references. Detailed acceptance procedure and implementation remain unspecified;
this normalization is neither a waiver nor a completion result. The tests
identified by OUT-006 and the G-APPR evidence named in the method remain the
inherited evidence classes, not newly executed tests.

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-104 OBJ-001 OBJ-002 OBJ-004 OBJ-007 | CLM-001 REQ-001 REQ-002 | AC-001 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims and requirements | Own accepted evidence for the `HostedEngineConsentPort` contract within the account/consent boundary |
| OUT-002 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | REQ-001 REQ-002 | AC-002 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims and requirements | Own accepted evidence for root-private `CODEX_HOME`, ambient-home exclusion, continuity, and no cross-root/account/policy-digest consent |
| OUT-003 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | CLM-002 REQ-003 | AC-003 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims and requirements | Own accepted evidence for the `K-ROLE-2` digest schema and truthful role-posture distinctions |
| OUT-004 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | CLM-002 REQ-003 | AC-004 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims and requirements | Own accepted evidence for Agent 0/1/2 parity and the labelled Agent 2/TASK fallback without a mechanism-proven overclaim |
| OUT-005 | SOW-104 OBJ-002 OBJ-004 | CLM-003 REQ-004 REQ-005 REQ-006 | AC-005 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims and requirements | Own accepted evidence for the three postures, default, prompt content, grouping caveat, explicit-user-act condition, and labelled on-state |
| OUT-006 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | REQ-001 REQ-002 REQ-003 REQ-004 REQ-005 REQ-006 | AC-006 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims and requirements | Own accepted isolation, consent, and continuity evidence; no completion claim until that evidence is accepted |
