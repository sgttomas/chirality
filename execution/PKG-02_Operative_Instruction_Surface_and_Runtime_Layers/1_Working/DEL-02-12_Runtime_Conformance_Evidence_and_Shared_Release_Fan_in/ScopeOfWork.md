---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-12
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@75c4e2ba401a6f5ad0c2f38846c39db6ab157405
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
status: DRAFT_AWAITING_OWNER_ACCEPTANCE
---

# Scope of Work — DEL-02-12

## Purpose and Objective Traceability

This draft Scope of Work defines the candidate production contract for
`DEL-02-12`, Runtime Conformance Evidence and Shared-Release Fan-in, a
`TEST_SUITE` deliverable of
`PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`. It serves project
scope item `SOW-104` and package objectives `OBJ-001`, `OBJ-002`, `OBJ-004`,
and `OBJ-007`. The applied register assigns Context Envelope `M`.

The accepted boundary is **conformance/source-identity/shared-release fan-in with all ten bindings held**. The deliverable produces Root/client conformance
and shared-release evidence fan-in for the versioned runtime contract, binds
`source_identity` only to exact accepted implementation bytes at G0.5, and
keeps every compatibility binding held until its named act.

This draft is grounded only in:

- the applied `DEL-02-12` row in
  `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`;
- this carrier's `_CONTEXT.md`;
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2,
  `INIT-06`; and
- the accepted G0 carriage in
  `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, rulings A3 and A7.

The anticipated write locus is `runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/**`.
That locus is an accepted planning note, never authorization.

## Deliverable Definition — Ontology

The applied register and carrier context identify seven anticipated outputs:

- **OUT-001 — Root and client conformance matrix.** The matrix records the
  conformance evidence available for the Root and each named client without
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
  draft neither supplies such an act nor lifts a hold.

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

All ten DEL-02-06 compatibility bindings remain `HELD_UNAVAILABLE`:

| # | Held binding | Required named act remains separate |
|---:|---|---|
| 1 | `binding_groups.2_source_and_release_identities.source_identity` | Exact Root implementation source bytes/hashes accepted at G0.5 |
| 2 | `binding_groups.2_source_and_release_identities.release_identity` | Exact release identity at G6a |
| 3 | `binding_groups.4_conformance_or_migration_evidence.clients[0]` — App | App-owned conformance at G5 and exact-release rerun at G7 |
| 4 | `binding_groups.4_conformance_or_migration_evidence.clients[1]` — Root CLI | Root CLI conformance at G5/G7 |
| 5 | `binding_groups.5_root_semantic_and_regression_evidence` | Accepted Root implementation/check evidence at G5/G7 |
| 6 | `binding_groups.6_census_relationship_routing_notice_and_findings.notice` | Release-fan-in notice after implementation/client evidence |
| 7 | `binding_groups.6_census_relationship_routing_notice_and_findings.tier_0_relationship` | Independent Tier-0 owner act |
| 8 | `binding_groups.8_accountable_human_acts.implementation_act` | Exact implementation activation at G0.5 |
| 9 | `binding_groups.8_accountable_human_acts.cutover_act` | Accountable-human cutover after G2–G5 fan-in |
| 10 | `binding_groups.8_accountable_human_acts.release_act` | Exact-artifact release act at G6a |

## Production and Verification Method — Praxeology

Production, if separately authorized, assembles the seven outputs from exact
accepted evidence and preserves the evidence class, identity, and authority
boundary of every input. It does not infer a dependency, interface, tool,
schedule, implementation method, dispatch, activation, acceptance, or hold
lift from this draft.

- **PRX-001 — Conformance fan-in.** Prepare the Root/client conformance matrix
  from separately accepted evidence, leaving missing or unaccepted evidence
  explicit.
- **PRX-002 — Exact identity binding.** Prepare the source-identity packet only
  when exact accepted implementation bytes at G0.5 exist; otherwise preserve
  `source_identity` as `HELD_UNAVAILABLE`.
- **PRX-003 — Role-evidence calibration.** Exercise Agent 0/1/2 parity and the
  labelled fallback, then classify each claim as `instruction-asserted`,
  instruction+config asserted, or mechanism-proven without upgrading the
  observed evidence class.
- **PRX-004 — Command-network proof.** Exercise the three accepted G0 A7
  postures at the exact pin, record prompt delivery and the explicit-user act
  for `acceptForSession`, and observe destination grouping empirically.
- **PRX-005 — Shared-release fan-in.** Assemble the available separately
  accepted evidence and report unresolved inputs without making an
  accountable-human release disposition.
- **PRX-006 — Hold backcheck.** Reconcile the fan-in against all ten named
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
  every output or method stated here are planning content. This draft grants
  no write, implementation, dispatch, activation, reliance, cutover, or
  release authority.
- **AX-006 — Separate SOW acceptance.** This document remains
  `DRAFT_AWAITING_OWNER_ACCEPTANCE`. The owner separately accepts, corrects,
  or declines its exact bytes; `_STATUS.md` remains `OPEN`.

## Output and Evaluation Matrix

| Output | Scope/objective trace | Grounded evaluation condition | Evidence expectation | Boundary |
|---|---|---|---|---|
| OUT-001 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Root and client entries identify accepted evidence and leave absent or unaccepted results unresolved | Root and client conformance matrix | Does not create client authority or satisfy a held client binding without its accepted evidence |
| OUT-002 | SOW-104; OBJ-001, OBJ-004, OBJ-007 | `source_identity` refers only to exact accepted implementation bytes at G0.5 | Exact source-identity evidence packet | Repository, planning, release, and version-like identities are not substitutes |
| OUT-003 | SOW-104; OBJ-001, OBJ-002, OBJ-004 | Agent 0/1/2 role-entry parity and the explicit labelled Agent 2/TASK fallback are evidenced | Parity and labelled-fallback fixtures | The fallback remains labelled `role not mechanically enforced` |
| OUT-004 | SOW-104; OBJ-001, OBJ-004 | Evidence classes remain truthful and hard containment remains unchanged | Claim-calibration matrix and hard-containment crosschecks | Instruction+config assertion is not mechanism proof |
| OUT-005 | SOW-104; OBJ-002, OBJ-004 | All three G0 A7 postures, prompt delivery, explicit-user `acceptForSession`, and empirical grouping are covered at the exact pin | G-APPR exact-pin proof | OpenAI service endpoints remain separate from command-network authority |
| OUT-006 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Separately accepted evidence is assembled with unresolved inputs visible | Shared-release evidence fan-in | Fan-in completeness is not release authority |
| OUT-007 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Every one of the ten bindings remains `HELD_UNAVAILABLE` absent its separately accepted named act | Ten-binding hold-aware disposition | No hold lift, implementation authority, release authority, or dispatch authority |
