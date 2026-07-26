# Frozen-Basis Manifest — Chirality Program tandem review

Provenance: transcribed verbatim from the owner's dispatch message of 2026-07-26 (the
embedded frozen-basis manifest). The transcription below is the sealed review basis for
both reviewers. Where any doubt arises, the frozen commit governs.

Review freeze: `da31c19b5656dd74615e308c4215688971d33dc9`
Product-basis commit: `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`
Charter: `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html`
Charter SHA-256: `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`
Verified by the supervising manager at dispatch: the two commits exist; `git diff
--name-only aeadf5304 da31c19b5` lists only the charter; the charter's SHA-256 at the
freeze matches the value above.

===============================================================================
EMBEDDED FROZEN-BASIS MANIFEST (verbatim)
===============================================================================

Status and identity

- The review corpus is frozen at commit:
  da31c19b5656dd74615e308c4215688971d33dc9
- The product inventory was established at:
  aeadf5304435e1a4d8b4a26306da9ad4d4519eb6
- Product files were unchanged between these commits.
- Mutable pointers are navigation aids, not independent authority.
- Candidate documents, proposals, historical snapshots, run evidence, and plans are not accepted basis unless a governing instrument expressly gives them that status.
- The charter is non-governing reviewer guidance. Its architectural propositions are questions to test, not facts to presume.

Cross-product control surfaces

- Tier-0 decision register:
  _DomainEngines/_DECISIONS/_REGISTER.md
- The register contains 23 D-T0 decisions.
- Particularly relevant decisions:
  - D-T0-01: framework-root contract precedence
  - D-T0-07: Tier-0 ownership of contract versioning
  - D-T0-09: flow-a.contract.v0.1.0
  - D-T0-15: PEC fences F-PEC-1 through F-PEC-4
  - D-T0-19: PEC/App bridge lane and cross-loop D-APP minting grant
  - D-T0-23: shared-runtime convergence, with App and PEC as distinct clients

Consulted-only context

- The domain packs are consulted-only context. They are not additional products under review, but their pins, notices, and drift may reveal effects of Root/App/PEC architecture:
  - domains/chirality
  - domains/chirality-app-dev
  - domains/chirality-piping
  - domains/piping-design
- Chirality Piping is a situated-product exemplar and a test of notice and inheritance coverage. It is not a fourth reviewed product.
- SOLVER Engine may illuminate historical lineage but is not governing evidence.
- Resource governance is candidate program architecture described only by the charter. It is optional, as PEC is optional. It may consume accepted system information to provide estimates, sequencing, locks or freezes, budgets, usage, cost, and forecast monitoring. It is not accepted Root, App, or PEC scope, a source of authority, a system of record, or a correctness dependency.
- App UI/API semantic-parity work is owner-directed future work but has not yet been established through a repository instrument. It is not accepted basis.

-------------------------------------------------------------------------------
1. CHIRALITY ROOT
-------------------------------------------------------------------------------

Accepted PRD

- File:
  docs/PRD_ROOT.md
- Revision 5
- SHA-256 prefix:
  82f7ea2944e7
- Adopted by D-GOV-22 on 2026-07-25.
- Exact adopted candidate bytes are preserved at:
  execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md
- docs/PRD_ROOT.md consists of a pointer block followed by the adopted candidate.
- D-GOV-26 and D-GOV-27 supersede PRD §5.2 O-1's six-member instruction-surface enumeration. The authoritative enumeration is docs/SPEC.md §0.2.1, with eight members including CLAUDE.md and .github/workflows/.
- The PRD body alone therefore contains deliberately superseded wording; reviewers must follow the pointer and governing instruments.

Root authority chain

- docs/DIRECTIVE.md
- docs/CONTRACT.md
- docs/SPEC.md
- docs/TYPES.md
- docs/PLAN.md
- Relevant invariants include K-AUTH-1, K-AUTH-2, K-WRITE-2, K-AGENTS-1, and K-DOMAIN-1 through K-DOMAIN-4.
- DIRECTIVE §1's earlier genus statement was superseded through D-GOV-23.

Accepted decomposition

- File:
  execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md
- Version 1.0
- SHA-256 prefix:
  14067a7d97c9
- Accepted by D-GOV-25.
- Headline counts:
  - 6 packages
  - 45 deliverables
  - 103 scope items
  - 7 objectives
- Registers:
  - execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv
  - execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv
  - execution/_Decomposition/chirality_root_objective_register_v1_0.csv
  - execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv
  - execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv
- The accepted candidate was subsequently augmented by accepted D-GOV-25 dispositions and D-GOV-27 objective/responsibility propagation without changing package, deliverable, scope-item, or objective counts.
- Relevant SHA roles:
  - ec62af070… = AcceptedCandidateSHA
  - ea0ad7a56… = CandidateMergeSHA
  - 653fabc9b… = D-GOV-25 EffectiveSHA and the SOW basis
  - 31b8dc94a… = D-GOV-26 EffectiveSHA and work-graph accepted basis
- The decomposition header itself calls ea0ad7a56… "EffectiveSHA," conflicting with the accepting decision's more precise role assignment.

Root scopes of work

- 45 live ScopeOfWork.md files under:
  execution/PKG-01_* through execution/PKG-06_*
- All 45 are INITIALIZED.
- All pin decomposition basis 653fabc9b3e8…
- The contracts were accepted through the owner's merge of PR #354.
- AC-* and VER-* statements remain marked CANDIDATE within all 45 contracts.
- Their candidate status is expressed through varied prose rather than one deterministic metadata field.
- Governing standard:
  docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md

Root decisions and current state

- Decision register:
  docs/governance_harness/_DECISIONS/_REGISTER.md
- Highest decision:
  D-GOV-27
- Particularly relevant:
  - D-GOV-09: ratification of the documentary authority chain
  - D-GOV-14: standards ratification
  - D-GOV-16: ScopeOfWork standard
  - D-GOV-20: Root-owned shared runtime and per-user daemon
  - D-GOV-21: Root working-root exception
  - D-GOV-22: Root PRD adoption
  - D-GOV-23 and D-GOV-24: genus supersession and propagation
  - D-GOV-25: decomposition acceptance
  - D-GOV-26: owner-gated closeout
  - D-GOV-27: initialization and closing rulings
- D-GOV-27 still contains an unbackfilled EffectiveSHA placeholder. Receipt 52 records this debt.
- Current navigation:
  execution/_Coordination/LOOP_INIT.md
  → execution/_Coordination/CURRENT_WORKPLAN.md
  → execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md
  → execution/_Coordination/LOOP_RECEIPTS.md
- Receipt 52 acts as the current initialization handoff.
- The named current workplan is marked ACTIVE even though its goal is complete and no successor has opened.
- Root guard state is under:
  execution/_harness/
- G1–G4 are passing; all work-graph nodes remain pending.

Root integration and drift surfaces

- Root runtime doctrine and agent index:
  AGENTS.md
- Generic runtime charter:
  runtime/README.md
- Relevant standards:
  - docs/WORKFLOW_COMPONENT_STANDARD.md
  - docs/DECOMPOSITION_STANDARD.md
  - docs/SOFTWARE_WORKFLOW_PROFILE.md
- domains/chirality/_Sources/Source_Manifest.csv pins Root AGENTS.md, governance documents, agent contracts, and skill contracts.
- Recomputed state at the product-basis commit:
  - 126 CLEAN
  - 93 DRIFT
  - 6 MISSING
- The six missing ACTIVE-pinned agent files are:
  - agents/AGENT_CONTEXT_TRANSPOSE.md
  - agents/AGENT_DECOMP_BASE.md
  - agents/AGENT_ORCHESTRATOR.md
  - agents/AGENT_SCHEDULING.md
  - agents/AGENT_SKILLMAKER.md
  - agents/AGENT_TOOLMAKER.md
- Routed Root-doctrine notice coverage is uneven:
  - App holds several notices.
  - domains/chirality lacks D-GOV-26.
  - Piping received no D-GOV doctrine notices.
  - PEC received no D-GOV doctrine notices.
- This is a live test of the agent-index change-notice and downstream-detection architecture.

Do not mistake for current Root basis

- docs/governance_harness/_PROPOSALS/**
- PRD candidate revisions 1–4
- Ruled proposal packets whose authority resides in decision records
- The not-adopted D-GOV-17 model-capability proposal
- execution/_Coordination/HANDOFF_STATE.md as the current initialization handoff: it belongs to the superseded Stage-2 arc, although it still records a parked Root compatibility-retirement lane
- Historical workplans and PLAN_INDEX
- Deliberately retained stale fixtures already dispositioned by an owner ruling
- ScopeOfWork copies inside AgentRuns and Evaluation snapshots
- plans/** as product authority

Root conditions reviewers should assess, not silently normalize

1. D-GOV-27 EffectiveSHA remains unbound.
2. Decomposition SHA-role terminology conflicts across surfaces.
3. Accepted post-candidate decomposition amendments lack one supplied verifying diff.
4. OI-011 appears stale after its resolution condition was met.
5. Receipt 52 acts as handoff without a dedicated initialization HANDOFF_STATE file.
6. CURRENT_WORKPLAN points to a completed but still ACTIVE workplan.
7. Root AGENTS.md predates the Root decomposition and does not identify its six packages or 45 deliverables.
8. Candidate AC/VER status is machine-opaque.
9. Root initialization recorded unresolved instrument conflicts involving AGENT_TASK absolute-path fields, validate_id_format.sh, the SOW validator's prefix set, and tools/REGISTRY.md.
10. PRD §5.2 O-1 remains superseded only through the pointer/instrument mechanism.

-------------------------------------------------------------------------------
2. CHIRALITY APP
-------------------------------------------------------------------------------

Product identity

- Root:
  projects/chirality-app-dev/
- Registered through:
  projects/chirality-app-dev/chirality.project.json
- It is a registered project loop, not a domain engine.

Accepted PRD basis

- File:
  projects/chirality-app-dev/docs/PRD.md
- SHA-256 prefix:
  ef638f43ccae
- The document has no stated version number.
- Its identity of record is its exact pin in AUTHORITY_CORPUS.json v17.
- It was not adopted through one PRD ruling; it reflects accumulated D-APP rulings, including D-APP-72, D-APP-73, and D-APP-74.
- The synchronized six-document corpus consists of:
  - DIRECTIVE.md
  - CONTRACT.md
  - SPEC.md
  - TYPES.md
  - PLAN.md
  - PRD.md
- docs/MANIFEST.json is stale. Use the v17 authority-corpus pin, not that manifest, for identity.

Accepted decomposition

- File:
  projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md
- Version 3.2
- SHA-256 prefix:
  952d3cbf81b0
- Header records Gates 1–7 as PASSED and acceptance through "implicit human approval per user instruction."
- No separate gate-acceptance ruling file exists.
- It was amended in place through SCA-APP-003/D-APP-73 and SCA-APP-004/D-APP-74 with topology preserved.
- Headline counts:
  - 78 scope items
  - 10 packages
  - 51 decomposition deliverables
  - 10 objectives
- The required-or-deferred contract_invariant_coverage_register.csv is absent, and no deferral ruling was found.
- The latest decomposition coverage package closes with WARNINGS and states READY_FOR_IMPLEMENTATION_HANDOFF.

App scopes of work

- 53 live ScopeOfWork.md files and 53 _STATUS.md files:
  - 51 decomposition deliverables
  - 2 PKG-00 control deliverables
- All 53 are IN_PROGRESS following D-APP-54.
- None is ISSUED.
- Open work is expressed through each contract's "Remaining" section.
- The queue convention was retired.
- F-APP-4 fences CHECKING to ISSUED.

App decisions and current state

- Decision register:
  projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md
- The register describes itself as non-governing tracking.
- It contains 74 RULED rows through D-APP-74.
- Particularly relevant:
  - D-APP-38: authority-corpus model
  - D-APP-48 through D-APP-50: contract pull, mirrors, and headless transport
  - D-APP-53 and D-APP-54: queue retirement and lifecycle rebaseline
  - D-APP-56, D-APP-57, D-APP-60, D-APP-61, D-APP-64: governance and delegation changes
  - D-APP-65: PKG-09 and piping transport parked
  - D-APP-70 and D-APP-71: ownership slate
  - D-APP-72: Pi/oMLX second engine
  - D-APP-73: shared-runtime extraction
  - D-APP-74: Woven Dialogue information architecture
- Current navigation:
  projects/chirality-app-dev/loop/LOOP_INIT.md
  → projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md
  → projects/chirality-app-dev/loop/LOOP_RECEIPTS.md
- Receipt 91 records the daemon-as-service tranche as executed and the owner merge of PR #333 as terminal.
- The associated run handoff still says PENDING_PR_AND_OWNER_MERGE.
- SCA-APP-004 is the latest scope-change pointer and is marked GOVERNANCE_PROPAGATED_IMPLEMENTATION_PENDING.

App integration and drift surfaces

- Authority corpus:
  projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json
- Version 17 pins the six App documents plus Root SOFTWARE_DECOMP and DOMAIN_ENGINE agent instructions.
- Those v17 pins were clean at the freeze.
- D-APP-48's 12-file SHA-pinned harness-contract pull is 12/12 stale after the shared-runtime tranche rewrote those files to deprecation shims without repinning.
- domains/chirality-app-dev/_Sources/Source_Manifest.csv recomputed state:
  - 119 CLEAN
  - 129 DRIFT
  - 219 MISSING
- Runtime/client seams include:
  - frontend/src/lib/runtime-client/daemon-harness-port.ts
  - frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts
  - frontend/electron/runtime-host.ts
  - frontend/docs/harness/runtime_engine_contract.md
  - docs/harness/reliance_boundary_register.md
- App's project AGENTS.md carries frontmatter status "draft" while operating as an active overlay.

Do not mistake for current App basis

- The charter's proposed semantic-parity SCA
- _LATEST.md or _REGISTER.md as independent authority
- Retired NEXT_INSTANCE, dispatch, workspace-manifest, and source-audit surfaces
- Completed or retired plans
- Unselected design-option packages
- Historical SCA snapshots
- The orphan PKG-03_Harness_Runtime_Core evidence tree as a registered package
- Evaluation and reconciliation snapshots as decomposition truth
- Undispositioned notices as adopted authority
- Build outputs, staging trees, session stores, or the separate public App repository

App conditions reviewers should assess, not silently normalize

1. No repository instrument presently establishes the proposed App UI/API semantic-parity work.
2. The PRD has no internal version and contains duplicate §17 numbering.
3. Decomposition acceptance rests on "implicit human approval" rather than a separate ruling.
4. contract_invariant_coverage_register.csv is neither present nor explicitly deferred.
5. The D-APP-48 contract mirror is 12/12 stale.
6. D-APP-49 mirror obligations may no longer describe the rehomed architecture.
7. An orphan PKG-03/DEL-03-06 evidence tree exists outside the decomposition.
8. The decomposition count of 51 and filesystem count of 53 require the PKG-00 explanation.
9. Receipt 91 lacks the terminal PR merge SHA.
10. Root-doctrine notices remain undispositioned, including one notice that misidentifies its stale target.
11. The project AGENTS.md overlay remains marked draft.
12. The latest run handoff and terminal receipt disagree about whether the PR merge is pending.

-------------------------------------------------------------------------------
3. PEC
-------------------------------------------------------------------------------

Product identity

- Root:
  projects/pec/
- PEC is the optional Chirality coordination plane.
- It provides a deterministic, rebuildable projection plus ephemeral presence.
- No governed act may require PEC.

Accepted PRD

- File:
  projects/pec/docs/PRD.md
- Version 2.1
- SHA-256 prefix:
  de0a969cad15
- Version 2.0 was adopted by D-PEC-58.
- The directed-bootstrap clarification to v2.1 was adopted by D-PEC-61.
- Product invariants are PEC-K-01 through PEC-K-11.
- The PRD does not make every described capability an immediate implementation mandate.

Accepted decomposition

- File:
  projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md
- Revision 1.2
- SHA-256 prefix:
  3e5be4e453ed
- Revision 1.0 was accepted by D-PEC-60.
- SCA-001/D-PEC-61 established directed FULL_GRAPH self-bootstrap.
- SCA-002/D-PEC-64 completed objective mapping and produced revision 1.2.
- Registers:
  - Deliverables.csv
  - ScopeLedger.csv
  - Companion_Inventory.csv
  - ContextBudgetQA.csv
- Headline counts:
  - 11 packages, PKG-00 through PKG-10
  - 64 deliverables
  - 94 scope-ledger rows
- Read execution/_Decomposition/_LATEST.md as the handoff pointer, not as decomposition truth independent of the accepted files.

PEC scopes of work and dependency state

- 32 of 64 deliverables have validated ScopeOfWork.md contracts at INITIALIZED.
- The remaining 32 P2–P4 deliverables remain OPEN without SOWs by deliberate sequencing.
- Their absence is not, by itself, a coverage gap.
- All 64 deliverables have local Dependencies.csv files.
- There is no central dependency register by owner decision.
- Current calibrated dependency state:
  - 254 rows
  - 135 ANCHOR rows
  - 119 EXECUTION rows
  - 62 graph nodes
  - 119 edges
  - 2 orphans
  - 0 strongly connected components
  - 0 waiver sidecars
  - strict validation clean
- Advisory blocker state:
  - 24 BLOCKED
  - 40 UNBLOCKED
- Blocker state is visibility, not work authority.

PEC decisions and current state

- Decision register:
  projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md
- Particularly relevant:
  - D-PEC-57: coordination-plane pivot
  - D-PEC-58: PRD v2 adoption
  - D-PEC-59: instruction/profile changes
  - D-PEC-60: decomposition acceptance
  - D-PEC-61: PRD v2.1 and FULL_GRAPH
  - D-PEC-62: scaffold and local dependency registers
  - D-PEC-63: SOW initialization wave
  - D-PEC-64: SCA-002 and revision 1.2
  - D-PEC-65: register-evidence repair
  - D-PEC-66: edge decline, DEL-10-10 repair, and QA dispositions
- F-PEC-1 through F-PEC-4 remain in force.
- F-PEC-1 fences source work; each build tranche requires its own owner-ruled packet.
- Phase 1.3 established:
  - INITIALIZED as the activation threshold
  - deliverable-local dependency storage
  - the DAG exhibit as frozen gate provenance
- Current status:
  projects/pec/docs/STATUS.md
- Current coordination:
  projects/pec/execution/_Coordination/_COORDINATION.md
- Current calibrated numbers are in coordination item 9, superseding item 8.
- Latest domain-engine receipt:
  _DomainEngines/pec/LOOP_RECEIPTS.md, Receipt 112
- Next owner gates concern P1 build-slice packets followed by WORKING_ITEMS ownership.

PEC integration surfaces

- Project overlay:
  projects/pec/AGENTS.md
- Domain-engine profile:
  _DomainEngines/profiles/pec.yaml
- The profile records that full supersession remains pending the v2 implementation shape.
- Root shared-runtime doctrine:
  D-GOV-20 and D-T0-23
- PEC is a distinct client of the Root runtime.
- PEC PKG-07 and PKG-08 contain the principal shared-runtime and API-facing seams.

Do not mistake for current PEC basis

- The frozen v0.4 prototype under core/, server/, web/, agent-sidecar/, tools/, and fixtures/
- Archived PRD v1 material
- PRD v2 candidate placement
- The frozen DAG exhibit as the live dependency register
- Executed setup plans, seed/wave/repair working files, AgentRuns, or historical scope-change evidence
- Advisory blocker output as authority
- Historical status lines rather than each _STATUS.md file's Current State field

PEC conditions reviewers should assess, not silently normalize

1. The PEC domain-engine profile still awaits full v2 supersession.
2. Only 32 deliverables are initialized; the other 32 are intentionally deferred.
3. Recorded REVIEW residuals remain:
   - DEL-08-02 CLM-002/AX-006 provenance text
   - DEL-08-01 AC-005's second clause being reachable only through AC-007's HUMAN_REVIEW row
   - DEL-00-03 CLM-001 being unreferenced in its matrix
4. These residuals are already recorded and should be assessed in context, not presented as newly discovered facts.
5. The frozen DAG exhibit's older 120-edge/255-row figures are superseded by the live 119-edge/254-row local-register state.

-------------------------------------------------------------------------------
4. SHARED METHOD AND RUNTIME LAYERS
-------------------------------------------------------------------------------

Shared ScopeOfWork method layer

- skills/scope-of-work/
- tools/scope_of_work/
- tools/validation/validate_decomposition_registers.py
- docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md

Version-skew condition

- The shared SOW method changed through amendments v1–v6.1.
- PEC's 32 SOWs were repaired and validated under the current method.
- Root's 45 SOWs passed before the v6/v6.1 QA-item-20 harmonization.
- A current-tool rerun over Root may produce tool-drift findings rather than proving that the accepted historical validation was false.
- Reviewers must identify the tool basis whenever relying on a validator PASS.

Shared runtime

- Root owns the generic runtime under runtime/.
- App and PEC are distinct clients of it under D-GOV-20 and D-T0-23.
- Runtime transport does not confer project authority.
- Project adapters retain their own gates, permissions, data boundaries, and evidence.
- The review should test whether ownership and integration seams are sufficiently explicit to prevent Root, App, PEC, and future domain applications from silently absorbing one another's responsibilities.

-------------------------------------------------------------------------------
5. BASIS-WIDE CONDITIONS
-------------------------------------------------------------------------------

Treat the following as disclosed conditions whose consequences must be assessed. Disclosure does not exempt them from criticism, but reviewers should distinguish validation from redundant rediscovery.

1. D-GOV-27's EffectiveSHA is unbound.
2. Root decomposition SHA-role language conflicts across surfaces.
3. Root's live decomposition includes accepted amendments over its accepted candidate without one supplied verifying diff.
4. Root's initialization handoff is Receipt 52 rather than a dedicated current HANDOFF_STATE file.
5. Root's current workplan is complete but still marked ACTIVE.
6. Root AC/VER candidate status is not deterministically represented.
7. App PRD identity depends on corpus v17 rather than an internal version.
8. App decomposition acceptance provenance is weaker than Root or PEC.
9. App lacks its required-or-deferred invariant-coverage register.
10. App's D-APP-48 pinned mirror is entirely stale.
11. App's domain source manifest is heavily drifted.
12. Root's Chirality domain source manifest contains extensive drift and six missing ACTIVE pins.
13. Root-doctrine change notices have not reached or been dispositioned consistently by downstream loops.
14. PEC's 32 absent P2–P4 SOWs are deliberate sequencing, not an accidental gap.
15. Root and PEC have different SOW validation-era identities.
16. Domain packs are consulted-only context but contain evidence about downstream drift and notice effectiveness.
17. Piping is consulted-only as a situated-product and notice-coverage exemplar.
18. The proposed App semantic-parity change is not yet an accepted instrument.
19. Resource governance is optional candidate architecture, not accepted scope.
20. The charter's program model is reviewer guidance to challenge, not evidence to cite as proof.

===============================================================================
END EMBEDDED FROZEN-BASIS MANIFEST
===============================================================================
