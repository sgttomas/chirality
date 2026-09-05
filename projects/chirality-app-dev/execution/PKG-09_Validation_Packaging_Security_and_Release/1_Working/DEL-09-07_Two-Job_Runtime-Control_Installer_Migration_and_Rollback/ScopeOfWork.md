---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-07
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@740569598f9d00440636b8ea25264127f418e4ec
project_scope_refs: [SOW-080]
package_objective_refs: [OBJ-008]
---

# Scope of Work — DEL-09-07

## Purpose and Objective Traceability

Define the App-side Two-Job Runtime-Control Installer Migration and Rollback
contribution to PKG-09 Validation, Packaging, Security, and Release. This
MIGRATION_SCRIPT deliverable has Context Envelope M and responsible party TBD.
SOW-080 assigns its installer transaction, staging, inspection, and recovery
evidence; OBJ-008 requires explicit, repeatable validation and packaging checks.
This initial contract describes the stable production target. Its creation
does not assert that the target has been implemented or accepted.

Source keys below are repo-root-relative and refer to the committed basis in
frontmatter:

- [D] `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, SOW-080, OBJ-008, DEL-09-07, DEC-024, OI-003 and OI-007.
- [C] This deliverable's `_CONTEXT.md`, Description, Anticipated Artifacts, and Authority Boundaries.
- [S] `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-009_2026-09-04_0944_App_V3_Pathway_Seating/Amendment_Actions.csv`, actions 7, 8, 11, 13–15; `Propagation_Plan.md` §§1, 7; `DOWNSTREAM_HANDOFFS.csv`, rows 3–9. These are dated scope-change history; their prior dispatch restrictions are not new initialization authority.
- [R7] Root `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/ScopeOfWork.md`, supervisor/control and two-job launch contract.
- [R11] Root `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/ScopeOfWork.md`, retirement/restart and journal contract.
- [I] `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-107_RULING_DEL_09_07_SOW_INITIALIZATION_2026-09-04.md`, authorization for PROJECT_SETUP initialization, with acceptance remaining separate.

Root-qualified deliverables in this contract refer to the `execution/` paths
above, never similarly numbered App deliverables. The earlier SCA-APP-008
Carrier Map WP-03 and pathway-seating MAPPING S-2 explain the historical gap;
the landed [D] assigns this work to DEL-09-07.

## Deliverable Definition — Ontology

- **OUT-001** — App-side two-job installer/migration script or transaction artifact that stages the two Root-owned launchd jobs through Root-owned runtime-control IPC. Supports SOW-080 and OBJ-008. Sources: [D], [C], [S].
- **OUT-002** — App installer transaction journal that records the transaction evidence necessary to explain staging and its outcome while consuming accepted Root state semantics. Supports SOW-080 and OBJ-008. Sources: [D] DEL-09-07 anticipated artifacts; [R11].
- **OUT-003** — Effective-state inspector and its observations for the staged two-job transaction. Supports SOW-080 and OBJ-008. Sources: [D], [C].
- **OUT-004** — Rollback, upgrade, uninstall, and cleanup fixtures and evidence for the App installer transaction. Supports SOW-080 and OBJ-008. Sources: [D], [C], [S].

The journal and inspector are App integration outputs. Neither establishes a
second runtime broker or an alternative source of Root runtime/storage truth.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — [D] seats the App installer integration and names Root `DEL-02-07` as supervisor/runtime-control owner and Root `DEL-02-11` as storage/retirement/restart semantic owner. [R7] carries daemon-plus-supervisor topology, authenticated purpose-limited private Unix control, and sole-daemon broker constraints; [R11] carries prepared/committed/reconciliation-required retirement journal state, exactly-once terminalization, and conditional resume. Consequential generic-runtime implementation belongs to Root `DEL-02-06` under [D] OI-007. App `DEL-09-04` owns DMG packaging and App `DEL-09-05` owns release-operations preparation and separately authorized execution under their [D] rows.
- **REQ-001** — OUT-001 shall cover staging the two Root-owned launchd jobs through the accepted Root-owned runtime-control IPC boundary. Exact names, calls, and installation transitions remain governed by TBD-001; this contract does not derive them from the topology alone. Sources: [D], [R7].
- **REQ-002** — OUT-002 shall provide transaction evidence for OUT-001, and OUT-003 shall report effective state so the resulting state can be inspected against the transaction outcome. The App journal shall use the applicable accepted Root semantics identified under TBD-002. Sources: [D], [C], [R11].
- **REQ-003** — OUT-004 shall cover rollback, upgrade, uninstall, and cleanup of the App two-job transaction with fixtures and recorded outcomes; expected states and preservation/removal rules shall be grounded in the routed Root contracts before execution. Sources: [D], [C]; TBD-002 and TBD-003.
- **REQ-004** — This deliverable shall perform no act owned by another deliverable: Root `DEL-02-07` owns supervisor/control semantics, Root `DEL-02-11` owns storage/retirement/restart semantics, Root `DEL-02-06` owns consequential generic-runtime implementation, App `DEL-09-04` owns DMG production, and App `DEL-09-05` owns release-operations preparation and separately authorized execution; each excluded act resolves to its owner in CLM-001. This boundary permits App conformance evidence and installer integration without transferring those acts. Sources: [D], [R7], [R11].
- **AC-001** — The transaction artifact and its trace show staging of both Root-owned jobs through the accepted control boundary, with all concrete interface choices bound to the routed Root contract rather than invented locally. Verified by VER-001 against REQ-001 and REQ-004.
- **AC-002** — The journal and effective-state evidence identify the transaction outcome and observed resulting state using the accepted semantic basis; incomplete or unresolved state is recorded without a successful-completion inference. Verified by VER-002 against REQ-002.
- **AC-003** — Fixtures and evidence account for each of rollback, upgrade, uninstall, and cleanup, comparing observed outcomes with contract-grounded expected states and preservation/removal rules. Verified by VER-003 against REQ-003.
- **AC-004** — The output/evidence review confirms the owner boundaries in REQ-004 and records any unresolved Root contract or gate as a limit on completion. Verified by VER-004 against REQ-004.
- **TBD-001** — Root routing must identify the accepted two-job identities, launchd installation domain/paths, permitted App-facing runtime-control entry and request/response/error contract. [R7] states that its purpose-limited supervisor socket is never renderer- or CLI-callable; that socket is not assumed to be the App entry. Owner: Root supervisor/control workflow, routed to the App integration owner before implementation.
- **TBD-002** — The exact App installer journal schema, persistence location, transaction/Root-state correspondence, interruption and reconciliation behavior, and effective-state inspection contract are not specified by [D]. [R11]'s retirement journal is context, not automatic permission to reuse or alter its schema. Owner: App integration owner with Root supervisor/storage owners before implementation and expected-outcome approval.
- **TBD-003** — Supported source installation versions, failure/rollback cases, upgrade/uninstall preservation and cleanup rules, and concrete fixture inputs await the accepted Root contracts and App implementation tranche. Owner: App integration owner with Root semantic owners before verification execution. This is completion detail within the named behaviors, not authority for new behaviors or release acts.

OI-003 requires transaction verification after adapter adoption and Root
control/storage semantics land; OI-007 requires named Root gates and separately
authorized App tranches. The Root SOWs describe semantic constraints but do
not by themselves prove routed implementation readiness. F-APP-2, D-APP-97,
G5 fan-in, and G6a exact-candidate release gates remain applicable. No local
test or contract validation closes those gates. Initialization acceptance and
deliverable completion are distinct: this draft can describe known scope
with explicit TBDs while implementation and completion remain gated.

## Production and Verification Method — Praxeology

For a separately authorized production tranche, bind the routed Root contract
versions, resolve the applicable TBDs with their named owners, then realize
the App transaction and collect its inspection and recovery evidence. Retain
the source bindings and observed outcomes with the deliverable evidence so
review can distinguish defined behavior from unproved expectations. No exact
implementation sequence, tooling, host operation, or scheduling is selected
by this initialization.

- **VER-001** — Inspect the installer transaction and trace both job-staging paths to the accepted Root control contract. Check the caller boundary and compare concrete interface choices with that source. Evidence: artifact/source trace and verification observations for AC-001.
- **VER-002** — Exercise the authorized transaction fixtures and compare journal outcome and inspector observations with accepted expected state, including any unresolved/reconciliation outcome carried by the routed contract. Evidence: source-bound fixture records, journal excerpts, and effective-state observations for AC-002.
- **VER-003** — Exercise the contract-grounded rollback, upgrade, uninstall, and cleanup fixtures in the separately authorized environment; compare actual outcomes and preservation/removal evidence with the expected rules. Evidence: per-behavior fixture inputs, results, and discrepancy dispositions for AC-003.
- **VER-004** — Review all four outputs against CLM-001 and the declared completion gates. Account for each excluded act and its owner, unresolved TBD, and claim limitation. Evidence: owner-boundary and completion-limits review for AC-004.

These methods describe how to verify the seated outputs. They authorize no
execution now and add no numerical acceptance threshold. The deterministic
SOW validator and generated REVIEW checklist test contract structure; they
do not substitute for these future production verification methods.

## Governing Values and Decisions — Axiology

- **AX-001** — Preserve one runtime owner and observable App integration: [D] OI-007 and [R7] retain the daemon as sole runtime broker; App evidence must not claim ownership or access beyond the routed interface.
- **AX-002** — Recovery claims require evidence for the named transaction behavior; [D] makes rollback, upgrade/uninstall, and cleanup explicit deliverable outputs rather than inferred packaging success.
- **AX-003** — DEC-024 seats SOW-080 without implementation or release authority. F-APP-2 and D-APP-97 remain active; signing, notarization, publication, distribution, and release-readiness claims require their separate owner/release pathway. [D] assigns the release-operations carrier to App DEL-09-05, with WP-11 execution requiring Ryan Tufts's G6a exact-candidate ruling.
- **AX-004** — [I] authorizes this PROJECT_SETUP initialization while preserving the OPEN lifecycle and separate exact-byte owner acceptance. Historical SCA dispatch language is retained as history and does not revoke that later direction. S-6 and the nine-node SCC remain separate; no edge ordering or resolution is inferred here.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-080; OBJ-008 | REQ-001; REQ-004; CLM-001 | AC-001 | VER-001 | Both job paths traced to accepted Root contract and caller boundary |
| OUT-002 | SOW-080; OBJ-008 | REQ-002 | AC-002 | VER-002 | Journal outcome compared with accepted expectations |
| OUT-003 | SOW-080; OBJ-008 | REQ-002 | AC-002 | VER-002 | Effective-state observations compared with accepted expectations |
| OUT-004 | SOW-080; OBJ-008 | REQ-003 | AC-003 | VER-003 | Rollback, upgrade, uninstall and cleanup fixture inputs/results and preservation/removal evidence |
| OUT-001 | SOW-080; OBJ-008 | REQ-004; CLM-001 | AC-004 | VER-004 | Owner-boundary check covering all four outputs and explicit completion limits |
