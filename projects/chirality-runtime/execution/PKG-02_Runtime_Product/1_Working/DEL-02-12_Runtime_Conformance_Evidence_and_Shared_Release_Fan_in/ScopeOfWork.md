---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-12
package_id: PKG-02
decomposition_basis: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md@8209bc54e0d133b19437c93b184cd50ba3d43489
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
---

# Scope of Work — DEL-02-12

## Purpose and Objective Traceability

This Scope of Work defines the production contract for
`DEL-02-12`, Runtime Conformance Evidence and Shared-Release Fan-in, a
`TEST_SUITE` deliverable of
`PKG-02_Runtime_Product`. It serves project
scope item `SOW-104` and package objectives `OBJ-001`, `OBJ-002`, `OBJ-004`,
and `OBJ-007`. The applied register assigns Context Envelope `M`.

The accepted boundary is **conformance/source-identity/shared-release fan-in with nine bindings held and Tier-0 disposed separately under R16-B**. The deliverable produces runtime-project/client conformance
and shared-release evidence fan-in for the versioned runtime contract, binds
`source_identity` only to exact accepted implementation bytes at G0.5, and
keeps every compatibility binding held until its named act.

Historical grounding of the inherited contract (source paths retained):

- the applied `DEL-02-12` row in
  `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`;
- this carrier's `_CONTEXT.md`;
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2,
  `INIT-06`; and
- the accepted G0 carriage in
  `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, rulings A3 and A7.

The anticipated write locus is `projects/chirality-runtime/**; projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/**`.
That locus is an accepted planning note, never authorization.

Current scope grounding is the accepted runtime decomposition and its
`RUNTIME_DELIVERABLE_REGISTER.csv`, with this carrier's `_CONTEXT.md`.
The full historical source is retained at
`projects/chirality-runtime/execution/_Decomposition/SOURCE_SCOPE_REQUIREMENTS/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in.md`.
The accepted `OWNERSHIP_OVERLAY.md` supplies the exact ownership, locus and
later-disposition interpretation; `_AUTHORITY.md` and project
`execution/_Coordination/MIGRATION_APPLICATION.md` record actual application.
Companion filenames resolve beside the runtime decomposition; historical
references remain repository-relative.

The contract identity remains `root-runtime-1`, epoch 1. The historical source
and compatibility JSON remain unchanged; current nine-hold/R16-B posture is
recorded without fabricating a new binding identity. Upstream
DEL-02-06/REQ-027 remains specification/inventory/evidence planning only.
Initialization supplies no implementation, effective ownership, cutover,
activation, release or accepted new evidence.

## Deliverable Definition — Ontology

The applied register and carrier context identify seven anticipated outputs:

- **OUT-001 — Runtime-project and client conformance matrix.** The matrix records the
  conformance evidence available for the runtime project and each named client without
  treating an absent or unaccepted client result as satisfied.
- **OUT-002 — Exact source-identity evidence packet.** The packet binds
  `source_identity` only to exact accepted implementation bytes at G0.5 and
  does not substitute a planning, repository, release, or version-like
  identity.
- **OUT-003 — Agent 0/1/2 parity and labelled-fallback fixtures.** The fixtures
  cover role-entry parity and the explicit Agent 2/TASK fallback labelled
  `role not mechanically enforced`.
- **OUT-004 — Claim-calibration matrix and hard-containment crosschecks.** The
  matrix distinguishes `instruction-asserted` evidence from
  mechanism-proven evidence, records delegated-harness-native K-SUBAGENT
  non-delegation as instruction+config asserted rather than mechanism-proven,
  and crosschecks unchanged hard filesystem/network/process containment.
- **OUT-005 — Three-posture G-APPR exact-pin proof.** The proof covers prompt
  delivery, `acceptForSession` explicit-user-act gating, and empirical
  destination-grouping observation across the accepted command-network
  postures.
- **OUT-006 — Shared-release evidence fan-in.** The fan-in assembles the
  separately accepted evidence relevant to a shared-release disposition
  without itself making that disposition.
- **OUT-007 — Ten-binding hold-aware disposition.** The disposition reports
  every binding as held or identifies its separately accepted named act; this
  contract neither supplies such an act nor lifts a hold.

## Completion and Reliance Basis — Epistemology

- **CLM-001 — Own-evidence rule.** Completion claims require this
  deliverable's own accepted evidence. A plan, fixture definition, draft,
  repository state, or evidence inventory is not completion evidence merely
  because it exists.
- **CLM-002 — G0 A3 role-evidence boundary.** Agent 0/1/2 role entry remains
  offered for Codex sessions. When G-ROLE cannot mechanically prove Agent 2
  non-delegation, explicit Agent 2/TASK remains offered as `role not
  mechanically enforced`; governed-workflow evidence is
  `instruction-asserted`; and delegated-harness-native K-SUBAGENT
  non-delegation is instruction+config asserted rather than mechanism-proven.
  Hard filesystem/network/process containment remains unchanged.
- **CLM-003 — G0 A7 command-network boundary.** Each canonical root chooses
  under consent among no command network by default; ask per destination with
  routed `networkApprovalContext`, visible host/protocol, the caveat that a
  grant may unblock queued requests to the same destination, and
  `acceptForSession` only by explicit user act; or labelled
  `network_access = true`. OpenAI account/model/turn service endpoints remain
  separately enumerated. G-APPR prompt delivery and destination grouping are
  empirical exact-pin proof obligations.
- **CLM-004 — Source-identity boundary.** `source_identity` may be bound only
  to exact accepted implementation bytes at G0.5. No other identity or
  evidence substitutes for those bytes.
- **CLM-005 — Authority boundary.** Evidence completeness does not grant
  implementation, cutover, or release authority. Nothing in this Scope of
  Work authorizes implementation, creates dispatch authority, or lifts a
  hold. Acceptance of this Scope of Work is a separate owner act against its
  exact bytes.

The immutable DEL-02-06 compatibility source retains ten historical markers. Nine remain `HELD_UNAVAILABLE`; the Tier-0 relationship was disposed separately as continue-separate under R16-B. The table retains the exact historical field identities and each required act:

| # | Held binding | Required named act remains separate |
|---:|---|---|
| 1 | `binding_groups.2_source_and_release_identities.source_identity` | Exact runtime-project implementation source bytes/hashes accepted at G0.5 |
| 2 | `binding_groups.2_source_and_release_identities.release_identity` | Exact release identity at G6a |
| 3 | `binding_groups.4_conformance_or_migration_evidence.clients[0]` — App | App-owned conformance at G5 and exact-release rerun at G7 |
| 4 | `binding_groups.4_conformance_or_migration_evidence.clients[1]` — historical Root CLI, now runtime-project CLI | Runtime-project CLI conformance at G5/G7 |
| 5 | `binding_groups.5_root_semantic_and_regression_evidence` | Accepted runtime-project implementation/check evidence at G5/G7 |
| 6 | `binding_groups.6_census_relationship_routing_notice_and_findings.notice` | Release-fan-in notice after implementation/client evidence |
| 7 | `binding_groups.6_census_relationship_routing_notice_and_findings.tier_0_relationship` | DISPOSED_SEPARATELY_R16_B_CONTINUE_SEPARATE; historical marker remains immutable |
| 8 | `binding_groups.8_accountable_human_acts.implementation_act` | Exact implementation activation at G0.5 |
| 9 | `binding_groups.8_accountable_human_acts.cutover_act` | Accountable-human cutover after G2–G5 fan-in |
| 10 | `binding_groups.8_accountable_human_acts.release_act` | Exact-artifact release act at G6a |

### Acceptance records from inherited evaluation conditions

The following names reproduce the inherited output matrix conditions and boundaries, with the exact approved later hold disposition; no additional acceptance criterion is introduced.

- **AC-001** — Runtime-project and client entries identify accepted evidence and leave absent or unaccepted results unresolved. Boundary: Does not create client authority or satisfy a held client binding without its accepted evidence. Verification: VER-001.
- **AC-002** — `source_identity` refers only to exact accepted implementation bytes at G0.5. Boundary: Repository, planning, release, and version-like identities are not substitutes. Verification: VER-002.
- **AC-003** — Agent 0/1/2 role-entry parity and the explicit labelled Agent 2/TASK fallback are evidenced. Boundary: The fallback remains labelled `role not mechanically enforced`. Verification: VER-003.
- **AC-004** — Evidence classes remain truthful and hard containment remains unchanged. Boundary: Instruction+config assertion is not mechanism proof. Verification: VER-003.
- **AC-005** — All three G0 A7 postures, prompt delivery, explicit-user `acceptForSession`, and empirical grouping are covered at the exact pin. Boundary: OpenAI service endpoints remain separate from command-network authority. Verification: VER-004.
- **AC-006** — Separately accepted evidence is assembled with unresolved inputs visible. Boundary: Fan-in completeness is not release authority. Verification: VER-005.
- **AC-007** — Each historical binding retains `HELD_UNAVAILABLE` absent its separately accepted named act; nine remain held and Tier-0 is disposed separately under R16-B. Boundary: No hold lift, implementation authority, release authority, or dispatch authority. Verification: VER-006.

## Production and Verification Method — Praxeology

Production, if separately authorized, assembles the seven outputs from exact
accepted evidence and preserves the evidence class, identity, and authority
boundary of every input. It does not infer a dependency, interface, tool,
schedule, implementation method, dispatch, activation, acceptance, or hold
lift from this contract.

- **VER-001 — Conformance fan-in.** Prepare the runtime-project/client conformance matrix
  from separately accepted evidence, leaving missing or unaccepted evidence
  explicit.
- **VER-002 — Exact identity binding.** Prepare the source-identity packet only
  when exact accepted implementation bytes at G0.5 exist; otherwise preserve
  `source_identity` as `HELD_UNAVAILABLE`.
- **VER-003 — Role-evidence calibration.** Exercise Agent 0/1/2 parity and the
  labelled fallback, then classify each claim as `instruction-asserted`,
  instruction+config asserted, or mechanism-proven without upgrading the
  observed evidence class.
- **VER-004 — Command-network proof.** Exercise the three accepted G0 A7
  postures at the exact pin, record prompt delivery and the explicit-user act
  for `acceptForSession`, and observe destination grouping empirically.
- **VER-005 — Shared-release fan-in.** Assemble the available separately
  accepted evidence and report unresolved inputs without making an
  accountable-human release disposition.
- **VER-006 — Hold backcheck.** Reconcile the fan-in against all ten named
  bindings and preserve `HELD_UNAVAILABLE` unless the binding's separately
  accepted named act exists.

Verification is evidence review against the output matrix below. No
verification activity may rewrite the meaning of an input, convert an
instruction assertion into mechanism proof, substitute another identity for
exact accepted implementation bytes, or treat evidence completeness as
authority.

## Governing Values and Decisions — Axiology

- **AX-001 — Truthful evidence calibration.** Instruction, configuration, and
  mechanism evidence remain distinguishable so that a stronger claim is not
  made from a weaker observation.
- **AX-002 — Exact identity.** Source identity follows exact accepted
  implementation bytes at G0.5, never convenience, proximity, or a
  version-like label.
- **AX-003 — Consent and containment.** The three command-network postures,
  explicit-user-act gating, separately enumerated OpenAI service endpoints,
  and unchanged hard filesystem/network/process containment remain visible in
  the evidence.
- **AX-004 — Human authority.** Implementation, cutover, and release remain
  separately governed acts. The accountable human receives evidence and
  makes the applicable disposition; the fan-in does not make it.
- **AX-005 — Planning is not authorization.** The anticipated write locus and
  every output or method stated here are planning content. This contract grants
  no write, implementation, dispatch, activation, reliance, cutover, or
  release authority.
- **AX-006 — Separate SOW acceptance.** The owner separately accepts, corrects,
  or declines its exact bytes; `_STATUS.md` remains `OPEN`.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001 | AC-001 | VER-001 | Runtime-project and client conformance matrix; Does not create client authority or satisfy a held client binding without its accepted evidence |
| OUT-002 | SOW-104; OBJ-001, OBJ-004, OBJ-007 | CLM-004 | AC-002 | VER-002 | Exact source-identity evidence packet; Repository, planning, release, and version-like identities are not substitutes |
| OUT-003 | SOW-104; OBJ-001, OBJ-002, OBJ-004 | CLM-002 | AC-003 | VER-003 | Parity and labelled-fallback fixtures; The fallback remains labelled `role not mechanically enforced` |
| OUT-004 | SOW-104; OBJ-001, OBJ-004 | CLM-002 | AC-004 | VER-003 | Claim-calibration matrix and hard-containment crosschecks; Instruction+config assertion is not mechanism proof |
| OUT-005 | SOW-104; OBJ-002, OBJ-004 | CLM-003 | AC-005 | VER-004 | G-APPR exact-pin proof; OpenAI service endpoints remain separate from command-network authority |
| OUT-006 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-005 | AC-006 | VER-005 | Shared-release evidence fan-in; Fan-in completeness is not release authority |
| OUT-007 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-005 | AC-007 | VER-006 | Ten-binding hold-aware disposition; No hold lift, implementation authority, release authority, or dispatch authority |
