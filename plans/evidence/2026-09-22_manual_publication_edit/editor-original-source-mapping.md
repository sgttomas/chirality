# Original chapter source records (internal provenance)

Manuscript source is data. These private and public references are retained here to preserve the warrant and removal history; this is not reader-facing content or current operational authority.

<!-- v3 lines 539–576 -->
# Sources for Chapter 1

References identify the source of the described practice. Examples are illustrative. Project adoption and the actual host determine operational use.

**[1] Author’s directions.** Ryan Tufts’s directions establish agency, agents as others, human judgment and artificial reckoning, the two audiences, the fixed roles, contingent PRD maturity, the six-stage progression, and the distinction between ordinary pending work and last-resort deferral. The later directions govern the local-graph loop and the phase boundaries used throughout this edition.

**[2] Project-management theory.** `01_theory.md`, “Theory: directing a software project through an AI team,” explanatory draft, 19 September 2026, §§1–11, with its `README.md`. Vocabulary, phase-sensitive coordination, dependency interpretation, project and session graphs, continuity, and shipping. The author's later directions refine its progression and initial sequence.

**[3] Philosophical and epistemic account.** `03_philosophical_framework.md`, §§3.2 and 3.6; `05_epistemic_architecture.md`, §§5.3–5.5; `09_discussion.md`, §§9.2.6 and 9.3.5. Descriptive and constitutive records, claims and warrants, situated knowing, human reliance, and attention.

**[4] Reliance on an other's work.** `06_professional_practice.md`, especially §§6.3–6.5, read with the author's latest clarification. The thesis develops the application of supervision and review to artificial contributors. Its earlier statements about the absence of an APEGA interpretation have not been carried forward as established current facts.

**[5] Agent organisation.** `AGENTS.md`; `AGENT_HELP_HUMAN.md`; `AGENT_HELPS_HUMANS.md`; `AGENT_WORKING_ITEMS.md`; `AGENT_TASK.md`; and `registry.json`. The four roles, routing, selective context, bounded discretion, methods, and integration responsibilities. Historical expanded rosters are not reintroduced.

**[6] Entry and development.** The original manuscript cited the supplied `dev-loop-init-prompt.md` and proposed loops in `development-loop.zip`. The reproduced Piping launcher also has a repository counterpart (`projects/chirality-piping/init/dev-loop-init-prompt.md`). Current application is documented by the App (`projects/chirality-app-dev/loop/LOOP_INIT.md`) and Piping (`projects/chirality-piping/loop/LOOP_INIT.md`) loop entries and the September 22 implementation record (`execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md`). Historical archive provenance and current project adoption are distinct; the timing of the phase model follows [1].

**[7] Scope change.** `WORKFLOW.md`, `contract.md`, and `method.md` for `scope-change`. Three grouped checkpoints, exact amendment and propagation, downstream ownership, stable identity, stateful closure, and affected-decision reopening. The chapter introduces this workflow without replacing its execution contract.

**[8] Example method.** `02_worked_example_method.md`, §§1–5 and 7–8. The distinction between illustrative explanation, reconstructed episodes, and general claims. The manual has not converted its constructed example into an empirical case study.

**[9] Local graph and reconciliation methods.** The original source was `development-loop.zip`. Current maintained counterparts are construct-local-work-graph (`workflows/construct-local-work-graph/WORKFLOW.md`), its graph template (`workflows/construct-local-work-graph/resources/work-graph-template.md`), and bounded-reconciliation (`workflows/bounded-reconciliation/WORKFLOW.md`), from the bundled `chirality-root` library. They support route selection, executable nodes, continuing state, and bounded comparison with warranted edits. The outline in Figure 1.4 quotes the loop's section names; the record specimen is illustrative. Source-qualified selection and in-flight adoption remain explicit.

**[10] APEGA professional practice standard.** *Relying on the Work of Others and Outsourcing*, May 2021, version 4.0, §3.1 and §§3.1.1–3.1.2, pp. 10–12. Consulted in its official publication on 22 September 2026. It sets out the supervision or thorough-review basis for taking professional responsibility and the examination and documentation involved. [Official standard](https://www.apega.ca/docs/default-source/pdfs/standards-guidelines/relying-on-the-work-of-others-and-outsourcing.pdf).

**[11] APEGA AI guidance.** “Guidance for Registrants Regarding the Use of Artificial Intelligence Tools,” published 23 March 2026, reproducing a practice notice first published in July 2025; read with the current Practice Notices page on 22 September 2026. Supports the limited regulatory statements made in the chapter. [Dated guidance](https://www.apega.ca/news/2026/03/23/guidance-for-registrants-regarding-the-use-of-artificial-intelligence-tools); [practice notices](https://www.apega.ca/about-apega/publications/standards-guidelines/practice-notices).

**[12] Systems-engineering account.** `07_se_design_analysis.md`, §§7.3–7.4 and 7.6–7.7; `04_architecture.md`, §§4.3–4.4. Configuration, verification and validation, decomposition, dependencies, and the distinction between stage gates and lifecycle states. Validation in the chapter concerns suitability for intended use; it does not redefine the formal professional-practice act bearing that name.

**[13] DBM terminology reference.** Government of Alberta, *Hub Development Plan Template*, item 4.2, “Project Design Details.” Used for the expansion “design basis memorandum,” not to prescribe PRD contents or the author's phase model. [Official template](https://www.alberta.ca/system/files/em-ets-cs-hub-development-plan-template-instructions.pdf).


**[14] Claim granularity.** `DELIVERABLE_CONCORDANCE_METHOD.md`, supplied Revision 2, §3.1. Decision-bound, depended-on, and named-verification tests distinguish stable production claims from incidental mechanism descriptions.

**[15] Task Management.** The supplied `task-management/WORKFLOW.md` and resources. Action Item registers, human promotion and disposition, invocation-local federation, controlled routing, and graceful absence. The method creates no standing development gate.


<a id="ch_2"></a>


<!-- v3 lines 1193–1237 -->
# Sources for Chapter 2

## Basis of the chapter

Sources below support the product-definition method and its comparison with DBM practice. Paths within an archive are relative to that archive's root. Examples and method-status qualifications are explained in the preface, Application note 2.A, and Appendix A.

`software-prd` is the proposed draft version 1 described in [14]. Application note 2.A records its unregistered standing, the repository review's source limitation, and the need to inspect the intended package before operational use. [14, 15]

**[1] Author's directions.** Ryan Tufts's directions for this manual establish the two audiences, the six-stage Conceptual–FEED–30%–60%–90%–100% correspondence, contingent PRD maturity, the initial sequence, the four roles, human judgment and artificial reckoning, and the treatment of agency and reliance. The software PRD method covers feature-sized and larger development projects; maintenance and stand-alone analysis remain outside its scope. These directions establish the account's intended framing and application.

**[2] Chapter 1 of this manual.** “From intention to an organised undertaking,” particularly §§1.5–1.10. Establishes examination of an other's work, the accepted basis, the course of development, the role relationships, change, and continuity. The editor example continues that chapter's constructed illustration.

**[3] Theory and philosophical account.** `01_theory.md`, §§1–3, 5–8, and 10; `03_philosophical_framework.md`, §§3.2 and 3.6; `05_epistemic_architecture.md`, §§5.3–5.5; `09_discussion.md`, §§9.2.6 and 9.3.5. Supports undertaking, situated knowing, claims and warrants, authoritative and descriptive records, continuity, and attention. The author's terminology and phase definitions govern their use here.

**[4] Agent organisation.** `AGENTS.md`; `AGENT_HELP_HUMAN.md`; `AGENT_HELPS_HUMANS.md`; `AGENT_WORKING_ITEMS.md`; `AGENT_TASK.md`; and `registry.json`. Supplies the complete role repertoire, bounded assignments, the relationship between design and implementation, method selection, and integration responsibility.

**[5] Development continuity.** The original source was the supplied launcher and proposed loops in `development-loop.zip`. Current counterparts are the App (`projects/chirality-app-dev/loop/LOOP_INIT.md`) and Piping (`projects/chirality-piping/loop/LOOP_INIT.md`) loop entries and local-graph construction method (`workflows/construct-local-work-graph/WORKFLOW.md`). Existing runs retain their selected methods and gates; Runtime and PEC retain separate project entry procedures. Method-specific handoffs, including PRD and decomposition transfers, remain distinct from ordinary continuation under adopted local-graph loops.

**[6] DBM publication management.** `workflows-DBM.zip`: `dbm-publisher/WORKFLOW.md`, `CONTRACT.md`, `PROCEDURE.md`, and `ACCEPTANCE.md`. Supplies the explicitly identified comparisons concerning source admission, examination of the subject, publication planning, section sizing and dispatch, post-authoring assessment, corrections, acceptance, and handoff. It governs its own DBM publication undertaking.

**[7] Bounded section production.** `workflows-DBM.zip`: `dbm-section-publish/WORKFLOW.md` and `CONTRACT.md`. Supports the discussion of section inputs, mapped authority, substantive body content, explicit uncertainty, source supersession, quality returns, and bounds on writing. The software method defines its own authoring assignments.

**[8] Package assembly and review.** `workflows-DBM.zip`: `dbm-publish/WORKFLOW.md` and `CONTRACT.md`; `dbm-postauthor-concordance/WORKFLOW.md` and `CONTRACT.md`; `dbm-draft-review/WORKFLOW.md` and `CONTRACT.md`. Supports complete package outputs, mechanical evidence preparation, candidate findings, human dispositions, and review status. The six finding categories are applied to PRD review by [14].

**[9] FEED decomposition.** `workflows-FEED.zip`: `project-decomp/WORKFLOW.md`, `resources/contract.md`, and `resources/method.md`; corresponding files under `software-decomp/`. Supplies three grouped checkpoints, accepted snapshots, canonical working packages, atomic scope, flat partitions, identifiers, coverage, variant-specific granularity, and the Context Envelope.

**[10] Setup and preparation.** `workflows-FEED.zip`: `project-setup/WORKFLOW.md`, `resources/contract.md`, and `resources/method.md`; `preparation/WORKFLOW.md` and its contract and method. Supports workspace inspection, coordination representation, declared writes, preservation of existing work, local records, optional Memory, and routing to preparation of the scope of work. Application note 2.B shows selected records and relationships; Chapter 3 develops their use.

Current repository setup discovers the source-qualified preparation skill (`.agents/skills/preparation/SKILL.md`); project-setup (`workflows/project-setup/resources/method.md`) records that selection and routes new PROJECT/SOFTWARE production to `scope-of-work`, `MODE=INIT`. Existing production formats retain their applicable transition treatment as described in Appendix A.

**[11] Local scope of work.** `workflows-FEED.zip`: `scope-of-work/WORKFLOW.md` and `resources/brief.md`, `tools.md`, and `checks.md`. Supplies `SOW_V1` initialization through `MODE=INIT`, source-grounded outputs, acceptance criteria, verification methods, exact criterion–method pairing, boundary ownership, qualified references, and fidelity of the derived review checklist. Lifecycle acts remain subject to the governing policy and explicit authority.

**[12] Tool reference.** `tools-FEED.zip`, especially `scaffolding/scaffold_deliverable.sh` and `source_audit/validate_prose.py`. Supports the stated structural behaviour of preparation and the limited kinds of evidence that mechanical checks supply. The presence of an implementation does not establish that it ran successfully in a project.

**[13] Management of change.** `scope-change/WORKFLOW.md` and its contract and method, supplied as `WORKFLOW.md`, `contract.md`, and `method.md` in the source set. Supplies amendment of accepted decomposition, three grouped decisions, supersession, accepted snapshots, affected-decision reopening, and downstream ownership. PRD revision is addressed by [14]; an amendment affecting accepted decomposition also follows the applicable scope-change method.

**[14] Software PRD method.** `workflow-drafts/software-prd/WORKFLOW.md`, with `resources/product-questions.md` and `resources/records-and-review.md`, draft version 1. Supplies applicability, proportionate intake, two grouped checkpoints, product-oriented questions, authoring and separate review, content-bound acceptance, continuation, amendment, and handoff to FEED. Its design notes and walkthroughs are supporting authoring evidence, not operational requirements or proof of successful reuse.

**[15] Workflow authoring method.** `create-workflow/WORKFLOW.md`, supplied under the filename `WORKFLOW.md` with frontmatter name `create-workflow`. Requires an inspectable proposed package, human review before registration, preserved source identity, and checks of structure and representative use. Creation of the package does not itself register or execute it.

**[16] Claim granularity.** `DELIVERABLE_CONCORDANCE_METHOD.md`, supplied Revision 2, §3.1. Supports the distinction between a stable production obligation and an incidental description of its mechanism. This principle does not waive an adopted requirement or replace a human decision.


<a id="ch_3"></a>


<!-- v3 lines 1906–1952 -->
# Sources for Chapter 3

This chapter develops the author's account of FEED and execution definition through the 30% gate. Its practical prescriptions are drawn from the supplied methods and standards. Short specimens illustrate their relationships and are not records of actual project decisions or execution. The selected workspace view is not an exhaustive scaffold inventory.

The procedures described here require an adopted project basis, applicable method versions, and the operations actually available in the host. The chapter does not enact workflow adoption, record a project gate, or change an operational file. The original archive citations preserve the manuscript's provenance; the repository comparison's review record, `MANUAL_REVIEW_v1.md`, cited in Appendix A identifies the current counterparts examined without asserting that unavailable archive bytes match them.

**[1] Author's directions.** Ryan Tufts's directions establish the two readerships, the Alberta engineering context, the four-role repertoire, human judgment and artificial reckoning, and the sequence from accepted PRD through decomposition, setup, execution definition, and detailed development. His latest clarification places construction of the initial DAG at the completion of the 30% phase, before passage through its gate. The 60% Deliverable examples were supplied for background understanding rather than required reproduction.

**[2] Software decomposition.** `workflows-FEED.zip`: `software-decomp/WORKFLOW.md` and `resources/contract.md` and `method.md`. SSOW, scope dispositions, Work Domain Packages, bounded-context Deliverables, Context Envelopes and exceptions, Scope Ledger, coverage, three grouped human checkpoints, immutable accepted snapshots, and final non-author audit.

**[3] Engineering project decomposition.** `workflows-FEED.zip`: `project-decomp/WORKFLOW.md` and `resources/contract.md` and `method.md`. Discipline-exclusive design Packages, artifact-kind Deliverables, repeated Artifacts, stable identity, coverage, companion registers, checkpoints, and accepted working-package control.

**[4] Project setup.** `workflows-FEED.zip`: `project-setup/WORKFLOW.md`, `resources/contract.md`, and the relevant PROJECT/SOFTWARE portions of `resources/method.md`. State inspection, source-qualified preparation, coordination representations, selected stage execution, production-contract preparation, and handoff. Its wider estimating and scheduling functions are outside this chapter's detailed treatment.

**[5] Structural preparation.** `workflows-FEED.zip`: `preparation/WORKFLOW.md`, `resources/contract.md`, and `resources/method.md`, principally tasks A–C. Read with the implementations of `scaffold_package.sh`, `scaffold_deliverable.sh`, and `write_status.sh` in `tools-FEED.zip/scaffolding/`. Exact creation and preservation rules, source-faithful local context, references, dependency declarations, status, and optional Memory.

The current repository counterpart is the preparation skill (`.agents/skills/preparation/SKILL.md`), selected through project-setup (`workflows/project-setup/resources/method.md`). Its structural write boundary remains distinct from production-content authoring.

**[6] Scope-of-work authoring.** `workflows-FEED.zip`: `scope-of-work/WORKFLOW.md` and `resources/brief.md`, `checks.md`, and `tools.md`, particularly the new-production INIT and read-only VERIFY provisions. Grounded authoring, write boundaries, output and evaluation relationships, exact criterion–method pairing, boundary-owner examination, deterministic checklist derivation, and return requirements.

**[7] Scope-of-work standard.** `DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`, especially §§1, 3–5, and 8. Canonical production-contract form, ordered headings, statement identifiers, evaluation matrix, checklist fidelity, and lifecycle meaning. The supplied file's activation notice makes operational effect conditional on approval of D-GOV-16. The repository's D-GOV-16 record (`docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`) records published approval on 12 July 2026. That activation does not establish every individual conversion, lifecycle transition, or later amendment; the active format and applicable adoption remain to be recovered for the Deliverable in use.

**[8] Local consistency review.** `worflows-FEED-2.zip`: `deliverable-consistency/WORKFLOW.md` and its resources. Single-Deliverable, scan-first examination, source-located findings, recommendation-first treatment, and authorised corrective writes. The supplied package matches its counterpart in the earlier FEED archive.

**[9] Cycle doctrine.** `CYCLE_DRIVEN_RESOLUTION.md`, Revision 0, 15 June 2026, §§1–6. Objective-relative graphs, SCC analysis, decompose/invert/merge/cut, human-gated cut and merge, non-gating unresolved cycle edges, proportional records, and event-driven re-derivation with project-local adoption.

**[10] Roles and runtime boundaries.** `AGENTS.md`, `AGENT_HELP_HUMAN.md`, `AGENT_HELPS_HUMANS.md`, `AGENT_WORKING_ITEMS.md`, `AGENT_TASK.md`, `registry.json`, and `AGENT_WORKFLOW_RUNTIME.md`, particularly Role configuration, Context selection and execution, and Coordination and evidence. The four roles, current routing, bounded briefs, effective permissions, method identity, and integration ownership. The runtime contract's implementation and adoption qualifications remain applicable; this chapter makes no claim about a live host.

**[11] Scope change.** The supplied `scope-change/WORKFLOW.md` and its contract and method. Three grouped checkpoints, impact and exact amendment, stable identity, propagation, independent poststate examination, accepted snapshots, and downstream obligations.

**[12] Session continuity.** The original source was the supplied `dev-loop-init-prompt.md` and proposed loops in `development-loop.zip`. Current counterparts are the Piping launcher (`projects/chirality-piping/init/dev-loop-init-prompt.md`), App loop (`projects/chirality-app-dev/loop/LOOP_INIT.md`), Piping loop (`projects/chirality-piping/loop/LOOP_INIT.md`), and construct-local-work-graph (`workflows/construct-local-work-graph/WORKFLOW.md`), with adoption recorded in the September 22 implementation record (`execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md`). Ordinary graph continuity applies within those loops and preserves the selected run's own outputs and gates. Directed SCC work precedes the first DAG; DAG-derived local graphs guide subsequent development in the author's phase model.

**[13] Theory and philosophical account.** `01_theory.md`, §§1–10; `03_philosophical_framework.md`, §§3.2 and 3.6; `05_epistemic_architecture.md`, §§5.3–5.5; and `09_discussion.md`, §§9.2.6 and 9.3.5. Purpose, commitments, records, warrants, situated human reliance, coordination, and attention. The preceding manual chapters provide the preceding development of these concepts.

**[14] Dependency extraction.** `worflows-FEED-2.zip`: `dependency-extract/WORKFLOW.md` and `resources/brief.md`, `tools.md`, and `checks.md`. Two-pass ANCHOR/EXECUTION extraction, evidence and target resolution, local register ownership, fixed v3.1 fields, direction, extraction and fulfilment states, non-destructive refresh, conservative uncertainty, and local QA.

**[15] Dependency closure examination.** `worflows-FEED-2.zip`: `audit-dep-closure/WORKFLOW.md` and `resources/contract.md` and `method.md`; read with `tools-FEED.zip/coordination/analyze_dep_closure.py` and `audit_dag.py`. Inventory, coverage, source validity, graph filters, missing and outside-scope targets, isolated nodes, SCCs, hubs, snapshots, and reproducibility. The tools' different input and authority assumptions require the selected project's adoption; this chapter does not silently unify them.

**[16] SCC case management.** `worflows-FEED-2.zip`: `scc-resolution-case/WORKFLOW.md` and `resources/brief.md`, `tools.md`, and `checks.md`. A bounded case under an existing PKG-00 control Deliverable, retained evidence and rulings, candidate remedies, owner-workflow handoffs, and closure supported by a subsequent DepClosure record.

**[17] Stable production claims.** `DELIVERABLE_CONCORDANCE_METHOD.md`, supplied Revision 2, §3.1. Decision, interface, and named-verification tests for claim granularity; mechanism descriptions as supporting evidence; human treatment of borderline commitments.

The current shared method (`docs/DELIVERABLE_CONCORDANCE_METHOD.md`) records Revision 2 under D-GOV-44 (`docs/governance_harness/_DECISIONS/D-GOV-44_concordance_claim_granularity.md`); in-flight runs retain their own pins until their owning adoption.


<a id="ch_4"></a>


<!-- v3 lines 2744–2790 -->
# Sources for Chapter 4

This chapter develops the author's method of steering detailed development through local work graphs. The numbered references distinguish author direction, the supplied loop proposal and current adopted counterparts, supporting methods, and the project-specific execution practices retained for their stated purpose. The documentary figures explain those sources; they record no actual dispatch, test, review, or acceptance.

**[1] Author's directions.** Ryan Tufts's clarification accompanying `development-loop.zip`: the loop is practised during the work toward 30%, initially through strongly directed SCC resolution; local graphs derived from the DAG characterise the 60% phase; project DAG revisions are common during detailed development; no further DAG change is anticipated on leaving 60%; the same graph method supports longer task and time horizons during 90%; development then gives way to user testing and debugging before the 100% publication pipeline. The same direction defines the five subjects of steering, ordinary continuation without a mandatory handoff, and the separation of agent Type and role from task-specific execution resources and expected performance per cost.

**[2] Development loops and adoption.** The original manuscript used `development-loop.zip`, `loop-1/loop/LOOP_INIT.md` and `loop-2/loop/LOOP_INIT.md`, as supplied proposals. The supplied v2 repository comparison additionally identifies the App loop (`projects/chirality-app-dev/loop/LOOP_INIT.md`) and Piping loop (`projects/chirality-piping/loop/LOOP_INIT.md`). Their adoption is recorded in the implementation record (`execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md`), its instruction-tranche manifest (`docs/governance_harness/tranche_manifests/ROOT-LOCAL-WORK-GRAPH-METHODS-20260922.yaml`), and routed notices. Both loops use sections 0–5 and persistent graph recovery. Runtime and PEC received notices; their loop procedures were not replaced. Read the current launcher and owning instructions for applicable entry and checks.

**[3] Agent responsibilities.** `AGENTS.md`, `AGENT_HELP_HUMAN.md`, `AGENT_HELPS_HUMANS.md`, `AGENT_WORKING_ITEMS.md`, `AGENT_TASK.md`, and `registry.json`. The fixed four-role repertoire, Agent 0/1/2 relationships, bounded initiative, selective context, parental coordination, integration responsibility, and declared capability ceilings. The manual follows the author's reservation of judgment for humans and use of reckoning for artificial agents.

**[4] Bounded software execution.** `worflows-FEED-2.zip/software-bounded-implementation/`: `WORKFLOW.md`, `execution.json`, and `resources/activation.md`, `brief.md`, `checks.md`, and `tools.md`. The six-step method, explicit writes and exclusions, profile-registered checks, scope validation, and the return of evidence and unresolved matters. The referenced profile contract and software-workflow tools must be available under the project's adopted basis before their operations are claimed.

**[5] Local graph construction.** `development-loop.zip/construct-local-work-graph/WORKFLOW.md` and `resources/work-graph-template.md`, complete. Intent and source direction, route selection, actual-state inspection, executable node definition, dependency checks, planned reconciliation, graph identity and maintenance, preferred location for a new graph, and recovery information. The manuscript condenses the template for explanation without prescribing another schema.

The current maintained counterpart is construct-local-work-graph (`workflows/construct-local-work-graph/WORKFLOW.md`) and its template (`workflows/construct-local-work-graph/resources/work-graph-template.md`), from the bundled `chirality-root` library.

**[6] Runtime relationships.** `AGENT_WORKFLOW_RUNTIME.md`, principally Role configuration, Context selection and execution, and Coordination and evidence. Method compatibility, source-qualified identity, supplied context, effective permissions, actual parentage, versioned amendments, and recorded returns. The source is prospective and distinguishes configuration from host enforcement and project adoption. No live provider capability is inferred from it.

**[7] Deliverable production contract.** `DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`, §§1, 3–5, and 8, read with the supplied `scope-of-work` package. The current `ScopeOfWork.md` production target, its Output and Evaluation Matrix, and the Remaining items in `_STATUS.md`. The standard's stated activation condition and the adopted lifecycle policy govern operational use; this chapter performs no status transition.

The repository's D-GOV-16 ruling (`docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`) records published approval on 12 July 2026; individual conversion and lifecycle acts remain separate. Existing production formats retain the compatibility described in Appendix A.

**[8] Scope amendment.** The supplied `scope-change/WORKFLOW.md`, `resources/contract.md`, and `resources/method.md`. Three grouped human decisions, exact amendment and propagation, stable identity, source lineage, independent poststate examination, and explicit downstream obligations. The amendment workflow retains its required handoff-state artifacts; those are distinct from ordinary session continuation.

**[9] Dependency meaning and revision.** `CYCLE_DRIVEN_RESOLUTION.md`, Revision 0, 15 June 2026, and the supplied dependency-extraction package. Objective-relative graphs, SCC treatment, non-gating unresolved cycle relationships, recorded remedies, and graph adoption and re-derivation rules. The doctrine specifies an event-driven trigger tied to decomposition revision or scope change. The author's current direction establishes that successor graphs can occur during 60%. A project's specific trigger and authority must support the particular revision; the chapter does not silently amend the doctrine.

**[10] Theory and philosophical account.** `01_theory.md`, especially §§6–10; `03_philosophical_framework.md`, §§3.2 and 3.6; `05_epistemic_architecture.md`, §§5.3–5.5; and `09_discussion.md`, §§9.2.6 and 9.3.5. Purpose, the two graph scales, readiness and closure, claims and warrants, situated judgment, integration responsibility, proportionate attention, and preservation of decisions and their consequences. These sources provide the explanatory basis, without establishing measured performance improvements.

**[11] Bounded reconciliation.** `development-loop.zip/bounded-reconciliation/WORKFLOW.md`, complete. Five steps from naming the completed work and affected Deliverables through bidirectional comparison, warranted document edits, checking, and return of remaining consequences. The chapter addresses the current Scope-of-Work arrangement. Routine edits remain bounded by the assignment and owning rules; project scope, lifecycle, acceptance, and pinned-basis changes retain their separate authority.

The current maintained counterpart is bounded-reconciliation (`workflows/bounded-reconciliation/WORKFLOW.md`), from the bundled `chirality-root` library.

**[12] Detailed development checks.** The earlier supplied `LOOP_INIT.md` supported the retained explanations of connected tests, protected criteria, exact-candidate evidence, independent review, backchecks, and integration. Current requirements are maintained in the App project instructions (`projects/chirality-app-dev/AGENTS.md#development-checks-and-evidence`), Piping project instructions (`projects/chirality-piping/AGENTS.md#software-checks`), and each project's `software-workflow.json`. The earlier loop remains dated provenance. Read the affected current checks for the actual candidate; the loop itself supplies orientation and traversal.

**[13] Package-based production.** `workflows-FEED.zip/project-setup/resources/package-activation.md`. The descriptive coordination postures, parent-mediated findings, examined returns, disjoint writes, and the manager's ownership of the combined result. This method applies when a package-based undertaking is selected; the general WORKING_ITEMS role also accepts other bounded undertakings.

The repository review cited in Appendix A identifies counterparts and their hashes; that comparison has not been repeated here, and unavailable original archives remain provenance references. Project-specific paths, permissions, command names, and review rules remain subject to the actual project and host. The manuscript describes a proposed course of work; it does not register a method, adopt a loop, issue a DAG, accept a Deliverable, or authorise release.

**[14] Claim granularity and information ownership.** `DELIVERABLE_CONCORDANCE_METHOD.md`, supplied Revision 2, §§2–3.1, and the supplied reconciliation contract. Stable claims, supporting mechanism evidence, Remaining ownership under the adopted method, and the separation of observation from scope authority.

The current shared method (`docs/DELIVERABLE_CONCORDANCE_METHOD.md`) and D-GOV-44 (`docs/governance_harness/_DECISIONS/D-GOV-44_concordance_claim_granularity.md`) establish the published Revision-2 default while preserving each in-flight run's own adoption.

**[15] Deferred concerns.** The author’s final definition and the supplied `task-management` workflow, contract, and method. Concerns without a present local-graph home are candidates for an owner-invoked sweep. Ordinary pending work remains in its graph. The register creates no standing entry gate, scope, or lifecycle authority.


<a id="ch_5"></a>


<!-- v3 lines 3678–3730 -->
# Sources for Chapter 5

Numbered references identify the chapter's basis. Cost and maintenance benefits are reasoned, conditional propositions, not measured findings. Figures are illustrative. Selected project instructions retain operational authority.

**[1] Author's directions.** Ryan Tufts's directions on the 30%, 60%, 90%, and 100% phases, local work graphs, continuing steering, Agent 0/1/2, and task-specific resource selection; and the directions on optimising the 90% phase, reserving deferral for work without a current local-graph home, using the term reconciliation, and conducting substantial agent-operated application tests under human direction. The reference workflows and tools illustrate possible methods. Reconciliation continues throughout. The explanations of earlier preparation and later maintenance develop these directions with [3], [6], [11], and [15–17].

**[2] Recurrent development.** `development-loop.zip`: `loop-1/loop/LOOP_INIT.md` and `loop-2/loop/LOOP_INIT.md`. Their six numbered sections, 0–5, cover orientation, graph construction or revision, ready work, execution and evidence, bounded reconciliation, and continuation or completion. Current graph state supports ordinary continuation. A separate handoff supplies recovery information when needed. The supplied archive is the historical source. Current App (`projects/chirality-app-dev/loop/LOOP_INIT.md`) and Piping (`projects/chirality-piping/loop/LOOP_INIT.md`) instructions establish this pattern in those two development loops, with selected-run pins and output contracts preserved. Runtime and PEC retain their own adopted procedures.

**[3] Construction of local undertakings.** `development-loop.zip/construct-local-work-graph/WORKFLOW.md` and `resources/work-graph-template.md`. Steering, route selection from the project DAG, current-state inspection, executable nodes, independent scopes, reconciliation, and continuation across sessions.

The current repository counterpart is construct-local-work-graph (`workflows/construct-local-work-graph/WORKFLOW.md`) with its template (`workflows/construct-local-work-graph/resources/work-graph-template.md`), from the bundled `chirality-root` library.

**[4] Agent organisation.** `AGENTS.md`; the four `AGENT_HELP_HUMAN.md`, `AGENT_HELPS_HUMANS.md`, `AGENT_WORKING_ITEMS.md`, and `AGENT_TASK.md` instructions; `registry.json`; and `AGENT_WORKFLOW_RUNTIME.md`, especially Role configuration, Context selection and execution, and Coordination and evidence. Roles, bounded responsibility, parental coordination, integration, permissions, and recorded decisions. The manual follows the author's use of judgment for humans and reckoning for artificial agents.

**[5] Bounded implementation.** `worflows-FEED-2.zip/software-bounded-implementation/`, with its brief, activation, checks, tools, and execution resources. Coherent changes, declared writes, authorised registered checks, scope validation, and evidence-bearing returns.

**[6] Production and evaluation basis.** `DELIVERABLE_SCOPE_OF_WORK_STANDARD.md`, §§1, 3–5, 8, and the checklist provisions of §10. `ScopeOfWork.md`, qualified OUT/REQ/AC/VER relationships, the Output and Evaluation Matrix, exact compilation of criteria, and Remaining as the delta against the production target. The repository's published D-GOV-16 ruling (`docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`) satisfies the standard's activation condition. Its PROJECT/SOFTWARE scope, bounded legacy transition, and lifecycle-neutral conversion limits remain material; the project must use its actual adopted production and lifecycle basis.

**[7] Bounded reconciliation.** `development-loop.zip/bounded-reconciliation/WORKFLOW.md`. Five ordered steps carry a bounded result into actual comparison, authorised edits, checks, and remaining consequences. This loop-level method is distinct from the activated corpus-concordance programme in [15–16]. Optional Memory remains non-authoritative context.

The current repository counterpart is bounded-reconciliation (`workflows/bounded-reconciliation/WORKFLOW.md`), selected by the App and Piping development loops from the bundled `chirality-root` library.

**[8] Local consistency examination.** `worflows-FEED-2.zip/deliverable-consistency/`, including its resources. A deterministic scan directs contextual examination of one Deliverable; the brief governs any resulting edits. Findings retain their input and reporting coverage.

**[9] Dependency examination.** `worflows-FEED-2.zip/audit-dep-closure/` and `CYCLE_DRIVEN_RESOLUTION.md`, Revision 0. Independent inventory, filters, coverage, read-only topology analysis, immutable snapshots, objective-relative SCC treatment, and event-driven graph revision.

**[10] Amendment and propagation.** The supplied `scope-change` entrypoint, contract, and method. Three grouped checkpoints, exact amendment, stable identity, affected ownership, propagation, poststate examination, and preservation of unaffected decisions.

**[11] Theory and philosophical account.** `01_theory.md`, particularly §§5–11; `03_philosophical_framework.md`, §§3.2 and 3.6; `05_epistemic_architecture.md`, §§5.3–5.5; and `09_discussion.md`, §§9.2.6 and 9.3.5. Readiness and closure, claims and warrants, accountable human reliance, integration, continuity, proportionate attention, and shipping. The maintenance discussion extends these relationships to subsequent work on the delivered product and states the conditions of that extension.

**[12] Examination and integration practice.** Root `AGENTS.md` and the testing, evidence, protected-check, independent-review, and integration sections of the supplied standalone `LOOP_INIT.md`, read with [2]. The older entry and routine-handoff rules are excluded. Current project instructions govern actual checks.

**[13] Illustrative software workflows.** `optimization-workflows.zip`: `software-repository-reconnaissance`, `software-test-planning`, `software-code-review`, and `software-defect-diagnosis`, with their brief, tools, checks, and execution resources. These combine bounded agent work with deterministic operations. These are optional method examples; they perform no lifecycle acceptance.

**[14] Illustrative tool implementations.** `optimization-tools.zip`, principally the seven `software_workflow/*.py` helpers; `practitioner_harness/README.md`; `retrieval/README.md`; and the local release-readiness helper. The inspected code supports the limited descriptions of manifest discovery, check selection including always-selected checks, command execution and service handling, structured comparison, scope checks, and generated-file hash comparison. Tool availability, qualification, and savings remain unverified. The release helper does not supply the publication workflow.

**[15] Deliverable concordance.** The supplied `DELIVERABLE_CONCORDANCE_METHOD.md`, Revision 2, labelled 22 September 2026, is the original manuscript's source. The current repository method (`docs/DELIVERABLE_CONCORDANCE_METHOD.md`) records shared-method ratification on 11 July and the Revision-2 claim-granularity amendment under D-GOV-44 (`docs/governance_harness/_DECISIONS/D-GOV-44_concordance_claim_granularity.md`) on 22 September. Its §§2–3 establish information homes and claim-level comparison; §3.1 gives the decision, interface, and named-verification tests and the default granularity-repair posture; §§4–7 distinguish lifecycle, activation, and adoption. D-GOV-44 preserves App `RUN_D128` Revision-1 and workflow pins pending its later adoption rider, and routes notices for the receiving loops to decide adoption. Shared publication, project adoption, and an in-flight run's method remain separate facts.

**[16] Corpus-reconciliation workflow.** The supplied `reconciliation/WORKFLOW.md`, `resources/contract.md`, and `resources/method.md` (uploaded as `WORKFLOW.md`, `contract.md`, and `method.md`). Activation, frozen discovery, calibration, bounded waves, independent verification, cross-package synthesis, grouped posture and packet decisions, authorised repairs, and final source-bound backcheck. The conditional reduction of third-layer reproduction is a narrowly specified representation-migration profile; its full coverage and escalation requirements remain intact. Numeric batch limits are not generalised into staffing rules.

**[17] Author-supplied run feedback.** The retrospective feedback accompanying the optimisation material. It describes uneven record drift, mechanism-level claims, incomplete decision propagation, missing evidence for off-code events, variation in agent verdicts, and measures proposed from that experience. The underlying ledgers, verdicts, and complete run history were not supplied for independent reconstruction. The chapter draws practical questions and mechanisms from the account without reproducing its statistics as measured benchmarks or claiming causal performance estimates.

**[18] Task Management.** The supplied `task-management/WORKFLOW.md`, `resources/contract.md`, and `resources/method.md` (received as `WORKFLOW.md`, `contract.md`, and `method.md`). Local Action Item ownership, human promotion and disposition, structured candidate harvesting, fenced execution surfaces, invocation-local read-only federation, trigger assessment, resolution through owning instruments, cross-loop notices, and workflow-specific closeout. The recorded generational cadence is non-binding. This method creates no mandatory loop-entry read, standing sweep, or additional development gate.

**[19] Register specimen.** The supplied `REGISTER.csv`, schema 1.0, read as an example of Action Item records. Its fields and recorded triggers illustrate source identity, outstanding human decisions, linked concerns, and prospective allocation. Its cited decisions and underlying evidence were not supplied as a complete live register environment. The chapter does not re-triage its rows, assert their current state, or adopt historical role labels from their prose.

**[20] Computer Use capability reference.** Anthropic, *Computer use tool*, Claude Platform documentation, consulted 22 September 2026: “Computer use tool” and “How computer use works.” This external primary source confirms the narrow capability description of screen observation and pointer/keyboard actions executed by an application-controlled environment. The test-management practice in §5.12 is developed from the author's direction and [4, 11, 12], not prescribed by the vendor documentation. No model, provider, host, or test environment is qualified by this manuscript. Reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool.

Appendix A retains the supplied repository comparison's identified basis; the original archive references do not imply that a complete source bundle is included. This chapter describes the supplied methods and creates no operational authority.


<a id="ch_6"></a>


<!-- v3 lines 3797–3811 -->
# Sources for Chapter 6

This chapter supplies the management connection to organisation-specific delivery arrangements. It prescribes no executable release pipeline, professional authentication procedure, or contractual closeout method. Its recommendations are an explanatory synthesis of the sources below.

**[1] Author’s directions.** Ryan Tufts’s phase correspondence and direction to keep the 100% treatment brief, allow established organisational workflows to append to the preceding account, and conclude the manual’s argument. Earlier directions include success, failure, suspension, reduction, and termination as possible project outcomes.

**[2] Project-management theory and developed practice.** `01_theory.md`, §§1–2 and 9–11, together with Chapter 5 of this manual, §§5.9–5.14. Candidate identity, bounded completion, accountable acceptance, continuity, shipping, and the conditional use of retained project records in maintenance.

**[3] Agent and method boundaries.** `AGENTS.md`, `AGENT_WORKING_ITEMS.md`, and `AGENT_WORKFLOW_RUNTIME.md`. Responsibility for integrated returns, effective permission, method selection, and the distinction between execution, acceptance, and release. These source instructions do not establish actual host capability or project adoption.

**[4] Reconciliation and unresolved obligations.** `DELIVERABLE_CONCORDANCE_METHOD.md`, supplied Revision 2, particularly §§2–4; the supplied reconciliation and task-management workflow packages; and the author’s retrospective feedback. Stable claims, current evidence, explicit ownership, last-resort allocation, and the limits of conclusions about events outside the examined record. The feedback is not an independently reconstructed performance study.


<a id="ch_7"></a>


<!-- v3 lines 3912–3928 -->
# Sources for Chapter 7

This conclusion states and evaluates the manual’s argument. Its recommendations and first-person assessments are editorial opinions developed from the author’s directions and sources, offered for his review. They are not empirical findings, institutional endorsements, or new operational requirements.

**[1] Author’s directions.** Ryan Tufts’s humanist agency framing, fixed role repertoire, six-stage model, expectations for 60% and 90%, continuing steering and reconciliation, optimisation aims, and permission to offer a concluding opinion on the manual’s reason for being.

**[2] Project-management theory.** `01_theory.md`, §§1–12, with `02_worked_example_method.md`, especially §§3–6 and 8. Purpose, the four perspectives, dependency interpretation, team construction, integration, continuity, attention, and the limits of performance claims drawn from a small or dependent case base.

**[3] Philosophical framework and its practical limits.** `03_philosophical_framework.md`, §§3.2, 3.5, and 3.6; `05_epistemic_architecture.md`, §§5.1 and 5.5; and `09_discussion.md`, §§9.2.6 and 9.3.5. Situated knowing, accountable reliance, the distinction between information and understanding, the continued human responsibility as capabilities improve, and the risk that process records displace attention from the work.

**[4] Agent responsibilities.** `AGENTS.md` and the four current role instructions, read with the runtime contract’s distinctions among role, method, brief, capability, and actual permission. The local-graph account has `development-loop.zip` and the author’s clarifications as its historical source, and the current App (`projects/chirality-app-dev/loop/LOOP_INIT.md`)/Piping (`projects/chirality-piping/loop/LOOP_INIT.md`) instructions and bundled graph/reconciliation methods as this edition’s repository application basis. Other loops retain their own adopted contracts.

**[5] Stable claims and continuing reconciliation.** `DELIVERABLE_CONCORDANCE_METHOD.md`, supplied Revision 2, §§2–3.1; the supplied bounded-reconciliation, reconciliation, and task-management methods; and the author’s two retrospective accounts. The account supports the distinctions and proposed mechanisms discussed here. No controlled productivity finding is inferred from the reported runs.


<a id="h_working_vocabulary"></a>

