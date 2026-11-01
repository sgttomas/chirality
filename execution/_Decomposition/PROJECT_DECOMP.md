# Chirality Library — Group 2 decomposition candidate

**Status:** PROPOSAL — reviewed by Agent 0; awaiting owner Group 2 decision.
**Revision:** G2-candidate-2, 2026-10-31. Agent 0 review annotations; proposed
scope allocations, package boundaries and deliverable definitions are unchanged.
**Method origin:** `chirality-root:bundled:workflow:project-decomp`.

Five flat Packages and eight Deliverables are proposed below. They organize work
by the use it must support: finding the library basis, maintaining and reconciling
holdings, operating its tools, establishing local execution, and independent reuse
and publication. The three accepted output forms guide concrete artifact kinds;
they do not determine the partition. A checked revision of an existing holding
can supply the result. No new companion, universal tool or global graph is proposed.

## 1. Accepted basis and current authority

The owner said: **“I approve this normalized scope, vocabulary and objective
basis.”** Agent 0 recorded that decision in the immutable Group 1 snapshot.
This author resolved [_LATEST_GROUP1.md](_LATEST_GROUP1.md), read the
[decision](checkpoint_snapshots/GROUP1-20261031T231127Z/DECISION.md),
[manifest](checkpoint_snapshots/GROUP1-20261031T231127Z/ACCEPTED_MANIFEST.csv)
and [handoff](checkpoint_snapshots/GROUP1-20261031T231127Z/HANDOFF_STATE.md), and
verified all three manifest entries before using the
[accepted payload](checkpoint_snapshots/GROUP1-20261031T231127Z/PROJECT_DECOMP.md).

| Basis | Identity / use |
|---|---|
| Accepted Group 1 | `GROUP1-20261031T231127Z`; payload SHA-256 `dd80227079e29e65a73da4c1650295aeb6e65f45940427bf0b698b6a5e1edddd`. DECISION.md supplies acceptance; submitted proposal wording in the snapshot is historical. |
| Accepted product intent | [docs/PRD.md](../../docs/PRD.md), revision 2026-10-31, SHA-256 `95c3c25ee36d4d4ddadf54d266a47a2ee58c6b37fbbdef75ad20a97986a718ca`, originally fixed at `d5ca6594ce6010c94c7981fe35cc540a822e9aa8`. |
| Current inspection basis | `cd81b47b6ba1a29a606caec3d1be691f4691c4e7`, branch `codex/library-decomposition-20261031`. Repository observations in §6 refer to this commit, not a global census. |
| Selected method | [Workflow](../../workflows/project-decomp/WORKFLOW.md), [contract](../../workflows/project-decomp/resources/contract.md), [Group 2 method](../../workflows/project-decomp/resources/method.md). Same bytes as the original Group 1 method basis. |
| Authority and entry | [AGENTS.md](../../AGENTS.md), [TASK](../../agents/AGENT_TASK.md), [Root entry](../_Coordination/LOOP_INIT.md), and this assignment. Owner steering retains Agent 0 coordination/review and this directly managed Type 2 author; no Type 1 layer is introduced. |
| Historical transition | PR #1778; [recovery route](../../projects/FROZEN.md#pre-library-root-execution); tag `archive/pre-library-execution-2026-10-31` at `f80f1510fb50799764720303b86c36da64b75d19`. Reset already executed; retention only, no repeated removal job. |

The accepted snapshot's relative links resolve from its original source path,
`execution/_Decomposition/PROJECT_DECOMP.md`, at its recorded basis. The working
document below uses that same original locality. Scope statements, classifications,
source mappings, objective meanings, vocabulary and qualifications are preserved;
only stage-status wording is refreshed. Group 2 allocations are proposed additions.

Group 1 acceptance does not accept this structure or authorize setup. No Group 2
snapshot/pointer, Group 3 audit, production locality, ScopeOfWork or dependency
binding is created. The preparer changes only this canonical working document.
Agent 0 owns integration and checkpoint presentation. Owner acceptance, releases,
commitment changes and additional archive disposition retain their authorities.

## 2. Vocabulary map

| CanonicalTerm | Synonyms / nearby terms | Practical meaning and source |
|---|---|---|
| Library holding | Material, library content | Principles, publications, roles, workflows, tool-use instructions, executable tools, formats, reference information and execution; not only code or instructions. PRD §1, §2.3. |
| Instructions | Guidance for action | Roles, workflows, maintenance procedures and tool-use guidance describing how a contribution can proceed and within what conditions. PRD R02, R04–R06; owner output-form clarification. |
| Descriptive and explanatory material | Account, definition, reference information | Information about what exists, what is known, its relationships, reasons and warrant, including state descriptions, evidence and accounts of commitments. PRD R02, R08–R12; owner output-form clarification. |
| Executable tools | Program, query, validator, transformation | Repeatable operations supplied as executable behavior, with declared inputs, outputs, dependencies, effects and limits. Tool-use instructions are a related information output. PRD R05, R13, R17; owner output-form clarification. |
| Artifact / output form | Maintained result, anticipated output | A tangible new or revised result of a later deliverable. The three forms in §2.1 guide its meaning and evaluation; concrete artifact kinds and their allocation belong to Group 2. Selected decomposition contract; PRD R07–R08. |
| Selected basis | Source revision, edition in use | Identified material actually governing a use or review. A proposed replacement or a newer examined publication does not silently replace it. R06, R15–R16. |
| Maintenance | Add, revise, reconcile, integrate, recover | Authorized changes to holdings and their maintenance means using applicable methods, actual capabilities and proportionate checks. R04–R06. No standing audit/backlog is implied. |
| Consumption | Consult, invoke, copy, embed | Independent use through files, Git, archives or documented interfaces. Local authority, operational data, adaptations, adoption and release remain with the consumer. R13, §2.3. |
| Scope item / SSOW | Normalized atomic scope / structured scope | One independently classifiable commitment or boundary, with stable SOW identity and source warrant. This SSOW was accepted at Group 1. Selected contract, PRD §6.2. |
| Objective | Success condition, product outcome | Testable intended improvement. Accepted OBJ identifiers map to accepted O references; they do not replace or amend them. PRD §2.1, §6.2. |
| Deliverable / local goal | Bounded contribution | A meaningful intended improvement, scope, outputs and evaluative evidence connected to product objectives. A directory, activity or requirement alone is not a deliverable. R07. No deliverables were defined at Group 1; §8 now proposes them. |
| Work locality | Execution locality, local work | Future accepted locality containing ScopeOfWork.md, deliverable.yaml and Work/. It references maintained outputs at their actual homes. Older Design/ references in adopting products mean Work/. R08; AGENTS.md. |
| Dependency condition | Need, input/use condition | Consumer-owned input plus intended use/condition, case/trigger and source or unresolved binding. Distinct uses, preliminary/final use, reciprocity and holds remain distinct. Not a supplier commitment or inferred whole-deliverable finish-to-start relation. R09. |
| Execution | Maintenance work and its retained material | Local goals, reasoning, evidence, conditions and authorized action within the library. Does not mean a new agent runtime or automated project manager. R07–R10, §1. |
| Publication (holding) | Manuscript, manual, course, edition | Material prepared for an audience, which can contain instructions and descriptive/explanatory content. Its audience, edition and maintained home do not make it a separate fundamental output form. PRD §1, §2.3, R11; owner output-form clarification. |
| Publishing (act) | Release, making a version available | Owner publication of identified material from a verified revision; named versions are the downstream default. Proposed, integrated, published, examined and adopted retain distinct standing. R15–R16, A7. |
| Check-in | Review and integration | Integration within the actual repository grant at the checked revision; it neither publishes a release nor accepts the product for the owner. R14–R15. |
| Custody | Exclusive maintenance holding, lock | Exceptional reservation of an item and operation, with holder and release/recovery condition and honest enforcement limits. Readers normally retain checked-in material; timeout alone grants no disposal authority. R14. |
| Source declaration | Stated relationship, owning declaration | What the source or consumer actually declares, with provenance and use limits. Queries derive views from these declarations. R03, R09–R10. |
| Inferred relationship | Hypothesis, discovered connection | An interpretive result labelled separately from a declaration, unknown or search limit. It creates no binding or supplier obligation. Local views can be partial, cyclic and revised. R03, R10. |
| Historical source | Archive, earlier basis | Recoverable identified evidence with its original meaning. It is neither current instruction nor a standing backlog and does not reactivate frozen work. R02, R12, §§5–6. |

### 2.1 Accepted output forms

The owner-confirmed distinction guides what the proposed deliverables produce:

| Form | Typical expression in this library | Evaluation emphasis |
|---|---|---|
| Instructions | Role descriptions, workflows, maintenance procedures, tool-use guidance | Whether the intended reader or agent can use the guidance under its stated conditions, with adequate decisions, resources and limits |
| Descriptive and explanatory material | Definitions, reference models, publication content, scope and dependency descriptions, state information and evidence | Whether meaning is clear, claims are warranted, relationships and qualifications are preserved, and the account fits its intended use |
| Executable tools | Queries, validators, transformations and other repeatable operations | Whether the documented behavior, outputs, dependencies, effects and failure handling hold when exercised |

The first two are information outputs. These forms describe the function of the
material, not a file extension, directory or fixed package partition. A file or
cohesive artifact can contain more than one form; evaluate its claims accordingly.
The four perspectives remain applicable across all forms rather than assigning
one perspective to each type.

Publications express instructions and explanations for their readers. Execution
contains particular descriptions, commitments, evidence and applicable working
guidance about maintaining the library. Neither its location nor a publication's
delivery format creates an additional fundamental output type.

Group 2 defines concrete artifact kinds and bounded deliverables from scope,
objectives and semantic coupling. It may identify a closely connected set of
outputs where the result requires one, such as a tool and its necessary usage
instructions. This does not prescribe three packages, one deliverable per form,
or an output of every form for each goal. A revised existing holding can be the
complete output; no new document, program or companion is required merely to
populate the structure. Conditional tooling remains subject to SOW-0033.

## 3. Accepted objectives

The five OBJ identities retain the five accepted O outcomes and their evaluative
meaning. Their statements and PRD mappings below are unchanged from Group 1.
Proposed `MappedDeliverables` are derived from §4 and shown in §9. Evaluation
remains future work; structural mapping is not evidence of satisfaction.

| ObjectiveID | Statement / testable outcome | PRD mapping | Evaluative basis (future evidence, not a present pass) |
|---|---|---|---|
| OBJ-001 | A maintainer entering with a bounded undertaking can locate the applicable holdings, instructions, source basis, execution work and unresolved conditions. | O1 | A1; A5's maintenance of the entry. Test purposeful discovery and source distinctions without a global graph. |
| OBJ-002 | A maintainer can carry authorized changes, including changes to maintenance means, through preparation, verification, review, integration and recovery using usable library instructions and tools. | O2 | A2, A4, A5. An actual instruction/tool change and its reusable procedure must both be demonstrated; a walkthrough alone proves no executable behavior. |
| OBJ-003 | A scoped change leaves affected definitions, warranted claims, actions, values, publications and work coherent for their uses, or exposes a consequential unresolved conflict for owner disposition. | O3 | A4, A5, A7. Preserve earlier editions and scoped adopted contracts; a repair alone does not establish maintenance-method availability. |
| OBJ-004 | Accepted local goals support evidence-directed action, meaningful input/use conditions, evolving reasoning and coordinated integration within the wider product without a complete graph. | O4 | A3, A8. Demonstrate an actual condition and a finding that revises the route; continue unaffected work and inspect affected uses. |
| OBJ-005 | Independent consumers can obtain identified material, inspect consequential changes and choose adoption, while maintainers preserve history, prepare publication and recover retained work. | O5 | A6, A7, A8. Named-contract compatibility, publication preparation and recovery establish different claims; consumer adoption and owner release remain separate. |

## 4. Scope ledger with proposed allocation

`IN`, `OUT` and `TBD` retain their accepted Group 1 meanings. Every scope item
has exactly one proposed accountable Package home. Only IN items receive
production Deliverable allocation. A Package home for an exclusion/reservation
makes its boundary accountable; it does not activate that scope. SOW-0026 maps
only to preservation of the completed transition's source/recovery conditions.

The first four columns, objective mapping and substantive qualifications are
unchanged from the accepted basis. SourceRef refers to the PRD unless another
source is named. The SOW-0011 note is refreshed solely for checkpoint standing.
This table is the canonical scope-to-Package/Deliverable mapping. Deliverable
cards and §9 summarize it for review and must agree with it.

| ScopeItemID | InOutStatus | ScopeItemStatement and qualifications | SourceRef | PackageID | DeliverableID(s) | ObjectiveID(s) | OpenIssue / notes |
|---|---|---|---|---|---|---|---|
| SOW-0001 | IN | Maintain a locatable starting route from a bounded undertaking to the selected basis, applicable role/repository instructions, relevant holdings and execution. Initialization selects no undertaking; the entry is itself maintainable. | R01; O1; A1, A5; §6.1 | PKG-01 | DEL-01-01_library-discovery-guide | OBJ-001, OBJ-002 | FALSE. Current entry is an input, not evidence of full A1 satisfaction. |
| SOW-0002 | IN | Make holdings locally intelligible and searchable through purpose, applicability, standing, resources, outputs and limits; distinguish explanation, instruction, example, proposal and history, preserving resources/notices when copied. Principles and publications retain maintained source homes. | R02; §1; §2.3; A1, A6 | PKG-01 | DEL-01-01_library-discovery-guide | OBJ-001, OBJ-003, OBJ-005 | FALSE. Categories remain with the material; no new central registry. |
| SOW-0003 | IN | Support purposeful search, reference following and structured queries with source identity, declared/inferred/unknown relationships and search limits visible. Retain or deliberately migrate consumed indexes, checking/regenerating from owning sources; read selected material. | R03; §5; A1 | PKG-01 | DEL-01-01_library-discovery-guide | OBJ-001, OBJ-003, OBJ-005 | FALSE. Views may be incomplete, cyclic and revised. |
| SOW-0004 | IN | Provide usable maintenance instructions for adding or revising holdings with purpose, scope, destination, relevant material, source identity and checks. Reuse/connect applicable methods rather than prescribe a new method per operation. | R04, “Add or revise a holding”; §2.2; A2 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002 | FALSE. Classify affected existing means as usable, needing connection/repair or absent during bounded work. |
| SOW-0005 | IN | Support organization, relocation or retirement using actual references/consumers, replacement or historical standing, recovery and deletion authority. | R04, “Organize, relocate or retire”; §5 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003, OBJ-005 | FALSE. Specific archival removals beyond the completed reset remain SOW-0032. |
| SOW-0006 | IN | Support diagnosis and reconciliation of conflicting claims, source meaning and observed behavior, identifying the owning material, evidence and repair scope. | R04, “Diagnose and reconcile”; R11; A4 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003 | FALSE. Reusable procedure and its result are distinct obligations. |
| SOW-0007 | IN | Support assessment of connected changes across relevant inputs, uses and consequences in instructions, tools, publications and execution, bounded by the authorized undertaking. | R04, “Assess connected change”; R11; §2.2 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003 | FALSE. Discovery of further consequences does not silently expand commitments. |
| SOW-0008 | IN | Support review and integration with proportionate scrutiny, the actual checked revision, findings, updates to owning text and the repository change procedure. | R04, “Review and integrate”; R12; R14; A2 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003 | FALSE. Root's grant does not transfer through library consumption. |
| SOW-0009 | IN | Align tool-use instructions with actual commands/interfaces, dependencies, outputs, write effects, failure behavior and limits. Use available selected-library tools for repeatable operations; state unavailable capabilities and permitted fallbacks, repairing necessary reusable procedure at its source. | R05; R17; §6.1; A2 | PKG-03 | DEL-03-01_maintenance-toolkit | OBJ-002 | FALSE. Existing deliverables CLI requires Git, HEAD and declared dependencies; file-only/namespace adapters are not assumed. |
| SOW-0010 | IN | Maintain entry, roles, methods, tools and execution under the existing authorized basis; review replacement means, preserve the usable preceding basis and adopt only after verification with actual authority. | R06; R04, “Change the maintenance means”; A5 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-001, OBJ-002, OBJ-003 | FALSE. Proposed instructions do not authorize themselves or alter their own review basis. |
| SOW-0011 | IN | Establish an accepted decomposition of bounded contributions with meaningful intended improvements, scope, outputs and evaluative evidence mapped to product objectives, without directory/requirement-driven partitioning or conflicting change ownership. | R07; §2.2; §6.2–6.3; A3 | PKG-04 | DEL-04-01_execution-decomposition | OBJ-001, OBJ-002, OBJ-004 | FALSE. Group 1 basis accepted; Group 2 structure is proposed here; later independent final audit and decomposition acceptance remain outstanding. |
| SOW-0012 | IN | Set up accepted localities using the library's applicable tools: ScopeOfWork.md for goal, accepted scope/objective references, outputs, boundaries, acceptance criteria and verification; deliverable.yaml for actual needs/conditions and useful source/code/check pointers; Work/ for reasoning, evidence, alternatives, consequential attempts, unresolved conditions and local outputs with maturity explicit. | R08; §6.2–6.3; A3, A8 | PKG-04 | DEL-04-02_local-execution-contracts | OBJ-001, OBJ-002, OBJ-004 | FALSE. Future execution/PKG-nn/DEL-nn-nn/ only after accepted scope; maintained outputs retain source homes and unchanged declarations stay unchanged. |
| SOW-0013 | IN | Author consumer-local needs after scope exists, identifying input, intended use/condition, trigger/case and source or unresolved binding. Preserve distinct conditions, preliminary/final use, reciprocal relations and technical holds; judge suitability from evidence. | R09; §6.1–6.2; A3 | PKG-04 | DEL-04-02_local-execution-contracts | OBJ-004 | FALSE. No inferred supplier commitments or whole-deliverable finish-to-start constraints; presence, merge and structural checks do not establish suitability. |
| SOW-0014 | IN | Support authorized local action from goals, evidence and actual input conditions, revising understanding/routes and neighborhoods as findings emerge, continuing unaffected work and checking affected uses with one integration owner. | R10; A3; §4 closing paragraphs | PKG-04 | DEL-04-02_local-execution-contracts | OBJ-002, OBJ-003, OBJ-004 | FALSE. Commitment/acceptance changes and reserved decisions return to the owner; local completion must serve the product. |
| SOW-0015 | IN | Derive relationship queries and undertaking-specific views from owning declarations, reporting basis, scope, unknowns and partial coverage while preserving actual live-metadata selection and project-root reference semantics. | R03; R10; §6.1–6.2 | PKG-03 | DEL-03-01_maintenance-toolkit | OBJ-001, OBJ-004 | FALSE. No second manual progress graph or required global DAG. |
| SOW-0016 | IN | Reconcile affected definitions/relationships, warranted claims, actions and values together, recording consequential reasoning in owning work and reconciling affected guidance/publications or identifying an edition's earlier basis. Preserve historical identities and scoped adopted contracts. | R11; §2.3; A4, A5 | PKG-02 | DEL-02-02_shared-meaning-reference | OBJ-002, OBJ-003 | FALSE. Four perspectives do not require four reports/approvals; library definitions remain distinct from product runtime enforcement. |
| SOW-0017 | IN | Verify the actual candidate proportionately and distinguish content, behavior and consumer-interface claims. Numerical meaning, persistence, permissions and destructive changes require focused regression checks and independent scrutiny; reuse applicable evidence and expose missing evidence as unverified. | R12; §4; A2, A4–A6 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-003, OBJ-004 | FALSE. Applicable checks attach to actual future changes, not a blanket product-verification run in this stage. |
| SOW-0018 | IN | Make unfinished work recoverable from its locality and review record: source basis, usable result, checks, unresolved conditions and next needed action. Add at most one replaceable recovery note only if needed. | R12; R04, “Recover or continue”; A8 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-004, OBJ-005 | FALSE. A labelled recovery case is allowed by A8; past records create no new authority or standing backlog. |
| SOW-0019 | IN | Provide independent paths to consult, invoke or copy identified material through ordinary files, Git, archives and documented interfaces, retaining resources/licenses/source basis and distinguishing local adaptations. | R13; R17; A6 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-005 | FALSE. Reading the library does not require Git; executable tools declare their own dependencies. |
| SOW-0020 | IN | Check affected named consumer interfaces at an explicit maintained-contract/fixture revision and supply a supported path or coordinated adapter before incompatible change. | R13; §2.2–2.3; §6.1; A6 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-003, OBJ-005 | FALSE. Needed input: affected named contract/fixtures at a specified basis, used when an interface change is selected; concrete selection unresolved until that scope is defined. Private evidence stays local; adoption/release are independent. |
| SOW-0021 | IN | Support exceptional exclusive custody through an existing lock/coordination mechanism stating holder, item, reserved operation and release/recovery condition with honest enforcement limits; resolve interruption through the authorized maintainer. | R14; A8 | PKG-02 | DEL-02-01_maintenance-procedures | OBJ-002, OBJ-005 | FALSE. Readers normally retain checked-in material; elapsed time never authorizes disposal. No new lock service is prescribed. |
| SOW-0022 | IN | Prepare named publication candidates from verified revisions with source identity, notices, dependencies, limitations and recoverable commit/edition routes; preserve owner publication authority and independent consumer adoption. | R15; R04, “Prepare publication and inspect updates”; A7 | PKG-05 | DEL-05-02_publication-candidate | OBJ-003, OBJ-005 | FALSE. Named publications are downstream default; explicitly following main is development. A merge is not release. Actual release is not this task's work. |
| SOW-0023 | IN | Explain consequential old/new basis, reason, meaning/use and migration effects in existing review/publication notes, and exercise polling/inspection via existing release/diff facilities. | R16; R04, “Prepare publication and inspect updates”; A7 | PKG-05 | DEL-05-02_publication-candidate | OBJ-003, OBJ-005 | FALSE. Interests stay local; examined is not adopted; partial/failed checks do not prove no change. Scheduling, delivery and unattended operation require actual configuration/authority; no new notice register. |
| SOW-0024 | IN | Preserve standalone repository use and existing Git/search/review/release/validation/scheduling foundations, classifying affected capabilities as usable, needing connection/repair or absent and implementing only necessary changes. | §1; §2.2; R17 | PKG-03 | DEL-03-01_maintenance-toolkit | OBJ-001, OBJ-002, OBJ-005 | FALSE. Optional bespoke tooling remains conditional under SOW-0033; no permanent capability census. |
| SOW-0025 | IN | Keep ordinary library use independent of undisclosed sibling checkouts, dated run directories, private inputs and credentials; use cleared public fixtures/summaries and required credential/private-term checks for public changes. | R17; §2.3; §6.3; A6, A7 | PKG-05 | DEL-05-01_consumer-use-guide | OBJ-002, OBJ-005 | FALSE. Private consumer inventory need not be read for this stage. |
| SOW-0026 | IN | Preserve traceability and recoverability of the authorized pre-library execution transition and original consumer-pinned history, including the App's historical SWBPIPE source bytes, without reinstating prior structure, commitments or lifecycle state. | §2.2; §5; §6.1, §6.3 step 2; R12, R15 | PKG-05 | DEL-05-02_publication-candidate | OBJ-003, OBJ-005 | FALSE. Transition already executed in PR #1778; archive identity verified here. Retention is the ongoing constraint; no repeat removal or migrated backlog. Selected archive bytes must be verified before future reliance. |
| SOW-0027 | OUT | Require a new App, agent runtime, hosted service or compulsory companion as the library product or a prerequisite for repository use. | §1; §2.3; R17 | PKG-03 |  | OBJ-001, OBJ-002, OBJ-005 | FALSE. Optional, justified thin support is distinct; see SOW-0033. |
| SOW-0028 | OUT | Establish a standing global audit, central relationship graph, subscriber/notice registry, automated project management or a complete DAG/global census requirement. | §2.3; R03, R10, R16 | PKG-01 |  | OBJ-001, OBJ-004, OBJ-005 | FALSE. Existing consumed indexes and bounded derived views remain in scope. |
| SOW-0029 | OUT | Transfer Root grants, execution authority or runtime policy to consumers, perform independent consumer product work, or require their production adoption/release to accept a verified library interface. | §2.3; R11, R13, R15 | PKG-05 |  | OBJ-003, OBJ-005 | FALSE. App v4 and SWBPIPE remain independent; coordination conveys no owner authority. |
| SOW-0030 | OUT | Reactivate, develop or verify frozen App v3, Runtime or PEC through decomposition, recovery or library maintenance. | §2.3; §6.3; AGENTS.md | PKG-02 |  | OBJ-003, OBJ-005 | FALSE. Explicit reactivation would be a separate authorized change. |
| SOW-0031 | OUT | Publish private knowledge, consumer operational data or credentials in library artifacts, examples or fixtures. | §2.3; R17; §6.3 | PKG-05 |  | OBJ-005 | FALSE. Cleared public evidence may support compatibility claims; generic evidence cannot establish named-consumer compatibility. |
| SOW-0032 | TBD | Further archival disposition of plans/, _DomainEngines/ and additional removals, if specifically authorized. | §2.3; §5 | PKG-02 |  | OBJ-003, OBJ-005 | TRUE — Q-01. Retain pending specific owner disposition; historical classification alone authorizes no deletion. No writes there in this undertaking. |
| SOW-0033 | TBD | Add bespoke tooling or a thin companion, including a file-only query interface or namespace adapter, only where a selected consumer/maintenance need demonstrates a gap in existing means. | §1; R17; §6.1 | PKG-03 |  | OBJ-002, OBJ-004, OBJ-005 | TRUE — Q-02. No gap or implementation selected here; neither availability nor a new product commitment is assumed. |

## 5. Accepted-intent coverage

This table checks representation of accepted requirements and acceptance criteria.
It claims **no implementation completion or product acceptance**. The ledger's
qualifications and the PRD remain governing; compact mapping does not replace them.

| PRD requirement | Scope representation |
|---|---|
| R01 | SOW-0001 |
| R02 | SOW-0002, SOW-0019 |
| R03 | SOW-0003, SOW-0015, SOW-0028 |
| R04 | Add/revise: SOW-0004; organize/relocate/retire: SOW-0005; diagnose/reconcile: SOW-0006; connected change: SOW-0007; review/integrate: SOW-0008; publication/update inspection: SOW-0022/0023; recover/continue: SOW-0018; change maintenance means: SOW-0010 |
| R05 | SOW-0009 |
| R06 | SOW-0010 |
| R07 | SOW-0011 |
| R08 | SOW-0012 |
| R09 | SOW-0013 |
| R10 | SOW-0014, SOW-0015 |
| R11 | SOW-0006, SOW-0007, SOW-0016, SOW-0029 |
| R12 | SOW-0017, SOW-0018, SOW-0026 |
| R13 | SOW-0019, SOW-0020, SOW-0029 |
| R14 | SOW-0008, SOW-0021 |
| R15 | SOW-0022, SOW-0026 |
| R16 | SOW-0023, SOW-0028 |
| R17 | SOW-0009, SOW-0024, SOW-0025, SOW-0027, SOW-0031, SOW-0033 |

| Criterion | Scope representation | Claim/evidence boundary retained for later evaluation |
|---|---|---|
| A1 | SOW-0001–0003, SOW-0015 | Bounded entry/discovery case with provenance and unresolved conditions; no central graph prerequisite. |
| A2 | SOW-0004, SOW-0008–0010, SOW-0017 | Actual instruction/tool change through integration and available reusable maintenance procedure. |
| A3 | SOW-0011–0015 | Requires accepted/set-up local scope, actual use condition, changed route/understanding and examined neighboring uses. Group 1 alone cannot establish it. |
| A4 | SOW-0006, SOW-0007, SOW-0016, SOW-0017 | Scoped inconsistency resolved, including publication where affected; warrant, use and values checked with historical qualifications. |
| A5 | SOW-0001, SOW-0010, SOW-0016, SOW-0017 | Maintain entry/instructions/tools under existing basis; verify both changed holding and maintenance means with preceding basis/authority preserved. |
| A6 | SOW-0002, SOW-0017, SOW-0019, SOW-0020, SOW-0025 | Obtain/use identified material and check a named consumer contract/fixtures at a specified revision, including resources/notices. Generic walkthrough is insufficient. |
| A7 | SOW-0022–0025 | Identifiable publication candidate, meaningful change account and exercised inspection against prior basis; release/adoption not implied. |
| A8 | SOW-0012, SOW-0018, SOW-0021 | Recover real retained work or a labelled case; verify custody release/recovery and actual enforcement where applicable. |

PRD §2.2 is covered by SOW-0001–0026; §2.3 boundaries by SOW-0002/0012/0016,
SOW-0025 and SOW-0027–0032. Section 5 is preserved in the pending Group 2 decision, SOW-0003/0026/0032 and the absence of new platform/schema decisions.
Section 6's source conditions, method order and future locality convention are
preserved in §§1/4/8 here and SOW-0009–0015/0020/0026/0033. The already executed
§6.3 step 2 is retained as history, not reassigned future transition work.

## 6. Representative holdings and bounded findings

These source inspections establish useful starting points and specific connection
or repair needs, not implementation completion. Existing good material is reused;
“not established” below is not a claim that nothing exists elsewhere. No private
consumer repository, historical execution backlog or frozen product was opened.

| Observed source at current basis | What exists / what needs connecting or repairing | Proposed contribution |
|---|---|---|
| [README](../../README.md), Root entry, [workflow guide](../../workflows/README.md) | Entry links already distinguish the library, independent projects and frozen recovery. Workflow source identity, selected-resource loading and generated indexes are documented. Connect these routes to the accepted local execution and a bounded worked discovery route; no new universal catalog. | DEL-01-01_library-discovery-guide |
| [create-workflow](../../workflows/create-workflow/WORKFLOW.md), [change](../../workflows/change/WORKFLOW.md), [Root change skill](../../.agents/skills/chirality-change/SKILL.md), [bounded-reconciliation](../../workflows/bounded-reconciliation/WORKFLOW.md), [coordinated-knowledge-work](../../workflows/coordinated-knowledge-work/WORKFLOW.md) | Reusable authoring, review/integration, local reconciliation and recovery practices exist. Connect them into the library's maintenance route and establish the R04 operation coverage and R14 custody case. The inspected route does not yet demonstrate a complete custody or library update-inspection procedure. | DEL-02-01_maintenance-procedures; consumer update inspection belongs to DEL-05-02_publication-candidate |
| [runtime reference](../../docs/AGENT_WORKFLOW_RUNTIME.md), [boundaries](../../docs/PRODUCT_BOUNDARIES.md), [compatibility reference](../../docs/COMPATIBILITY_FORMATS.md) | Existing scoped/historical contracts coexist with statements such as “The Runtime project owns production discovery” and project methods “cannot weaken Root governance.” Their intended applicability needs explicit comparison with independent adoption and frozen Runtime standing; do not erase adopted contracts. | DEL-02-02_shared-meaning-reference; scoped applicability reconciliation, not a runtime redesign |
| [thesis architecture §4.2](../../docs/thesis/04_architecture.md), [manual entry](../../docs/alignment-manual/README.md) and its current v9 source's vocabulary/recovery/edition passages | Explanations already describe local conditions, derived views, current source homes, recoverability and edition identity. Reuse these as explanatory basis; reconcile only claims affected by the selected boundary/setup changes. A whole thesis/manual/course rewrite is not evidenced. | DEL-02-02_shared-meaning-reference; DEL-01-01_library-discovery-guide links the current editions |
| [setup](../../workflows/project-setup/WORKFLOW.md), [preparation](../../.agents/skills/preparation/SKILL.md) and [scaffold contract](../../.agents/skills/preparation/references/scaffold-contract.md), [package helper](../../tools/scaffolding/scaffold_package.sh), [deliverable helper](../../tools/scaffolding/scaffold_deliverable.sh) | Concrete mismatch: helpers create labelled package/DEL paths and lifecycle folders/control stubs; preparation requires those files. [Minimum-fileset check](../../tools/validation/check_min_viable_fileset.sh) requires four legacy control files. The accepted Root locality does not. A supported current path must be selected/repaired before live setup; preserve separately scoped legacy callers. | DEL-03-01_maintenance-toolkit owns executable support and direct usage contract; DEL-02-01_maintenance-procedures owns selection/authority guidance; DEL-04-02_local-execution-contracts consumes the verified path |
| [scope-of-work](../../workflows/scope-of-work/WORKFLOW.md) and [tool policy](../../workflows/scope-of-work/resources/tools.md) | INIT already authors source-grounded SOW_V1 directly and uses existing validators/checklist tools. The tool policy also requires hashing `_STATUS.md`, and other modes retain historical lifecycle obligations. Establish an applicable new-Root INIT route without silently importing these requirements or removing historical compatibility. | Same three contributions as setup; no wholesale conversion or lifecycle revival |
| [deliverables guide](../../tools/deliverables/README.md) and [loader](../../tools/deliverables/cli.py) `load`, [local graph method](../../workflows/construct-local-work-graph/WORKFLOW.md), [need authoring](../../workflows/dependency-extract/WORKFLOW.md) | Consumer-local conditions, Git/HEAD/PyYAML requirements, working-file discovery and project-root path semantics already exist. Loader walks live deliverable.yaml files and verifies local identity; views remain derived and do not judge suitability. Reuse and verify on adopted localities before proposing repairs. | DEL-03-01_maintenance-toolkit; DEL-04-02_local-execution-contracts |
| [workflow utility guide](../../tools/workflow_runtime/README.md), [manual rendering route](../../docs/alignment-manual/README.md#read-and-render), [LICENSE](../../LICENSE.md), recovery reference | Identified method resources, explicit host enforcement limits, source-derived publication rendering, notices and recovery routes exist. General library acquisition, selected-consumer qualification and polling need a joined usable path; their end-to-end sufficiency was not exercised here. | DEL-05-01_consumer-use-guide; DEL-05-02_publication-candidate |

## 7. Proposed flat Packages

Each Package includes design within the one discipline named below. These are
work disciplines, not staffing tiers or new role types. Related instructions and
evidence for a software tool remain part of software engineering; runtime/product
engineering is excluded. Publications retain the subject's meanings and source
homes; technical publishing packages only their identified delivery and use.

| PackageID | Name / purpose | Discipline | Inclusion criteria and boundaries |
|---|---|---|---|
| PKG-01 | Library access — find and interpret the selected basis from a bounded undertaking | Information architecture | Entry/navigation, local intelligibility and purposeful discovery. Owns SOW-0028's no-central-census boundary. Does not implement query algorithms or rewrite every holding. |
| PKG-02 | Maintenance practice and shared meaning — make changes operable, coherent and recoverable | Knowledge engineering | Maintenance procedure set and reconciled meaning/applicability reference set. Owns frozen-work and extra-removal boundaries. No tool implementation, publication release or general content audit. |
| PKG-03 | Executable maintenance support — make selected repeatable operations fit the current library contract | Software engineering | Existing selected scaffolding, validation, resolution/query utilities and their direct usage instructions. Owns standalone-use and conditional-tooling boundaries. No new App/service, optional companion allocation, consumer runtime or global query system. |
| PKG-04 | Root local execution — turn accepted product scope into usable local goals and conditions | Project planning | Decomposition design and the resulting local contract/work set. No code relocation, new lifecycle regime or authoritative global dependency network. Owns actual local setup/use, not implementation of its supporting tools. |
| PKG-05 | Independent reuse and publication — make identified material usable, inspectable and recoverable by consumers | Technical publishing | Consumer-use/compatibility guide and versioned publication package, notices, change inspection and historical routes. Owns no-transferred-authority/private-publication boundaries. No consumer product development, imposed adoption, owner release act or new archival removals. |

PKG-01 and PKG-05 differ by use: finding material within a selected basis versus
obtaining and assessing a transferable version. PKG-02 separates the maintenance
method and meaning of holdings from PKG-03's executable behavior. PKG-04 produces
particular Root commitments and working conditions rather than a reusable method
or another software platform. These partitions cross the five objectives and the
three output forms; neither set has been converted one-for-one into Packages.

## 8. Proposed Deliverables and anticipated artifacts

`ResponsibleParty` for each Deliverable is **TBD — a Root contributor assigned by
Agent 0**; the discipline/function is specified below. No current Type 2 author
or consumer is silently assigned future implementation. Agent 0 remains the
integration owner for the broader undertaking. Q-03 records this staffing gap.

The eight full IDs below are canonical PROJECT identities. Future native YAML
and ScopeOfWork bindings use their numeric DEL prefixes, and localities use
`execution/PKG-nn/DEL-nn-nn/`; descriptive suffixes remain in the accepted identity,
not an extra phase hierarchy. No path in that future convention is created now.
Each card's artifact list belongs only to that card's Deliverable. Artifact kind
is a coherent set; sections, commands, files, cases and editions are instances
within it, not automatically separate Deliverables. Supporting verification is
kept in the actual review record or local Work/ when needed, not extra receipt
sets. Instructions, descriptions and executable behavior are evaluated according
to their respective claims.

### DEL-01-01_library-discovery-guide — A usable route into the selected library

- **ParentPackageID:** PKG-01. **Type:** Library navigation and discovery guide.
  **ResponsibleParty:** TBD — information architecture contributor.
- **Local goal:** Given a bounded maintenance brief, a maintainer can find the
  applicable holding, method, source standing, execution locality and unresolved
  conditions without treating an index or inferred relationship as authority.
- **CoversScopeItems:** SOW-0001, SOW-0002, SOW-0003.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-003, OBJ-005.
- **Anticipated artifacts:** A connected/revised entry and local navigation set
  in README.md, execution/_Coordination/LOOP_INIT.md and selected owning indexes;
  concise directed-search instructions and a bounded discovery example attached
  to that route. Include purpose/applicability/standing/resources/outputs/limits
  for the holdings actually traversed. Existing workflow and publication indexes
  stay at their homes and are regenerated only when their owning sources change.
  These are guide components, principally instructions and explanations.
- **Evaluation:** A1 walkthrough from an actual selected brief, checking source
  distinctions, search limits and required resources/notices. Establish separately
  whether any invoked command behaved as claimed; no complete-inventory claim.
- **Needed inputs / use conditions:** Before wiring a current-work link, consume
  the accepted execution identities and actual usable locality from
  DEL-04-01_execution-decomposition / DEL-04-02_local-execution-contracts; a
  proposed path alone cannot claim active work. For method discovery, consume
  workflows/README.md, catalog/index and selected package metadata/resources at
  the inspected revision (R01–R03). For publication links, resolve the edition at
  docs/alignment-manual/README.md or docs/thesis/README.md; pin it when a claim
  relies on exact content. Existing-entry work can proceed before new locality
  links become available.
- **Boundary:** This guide supplies navigation and provenance. The meaning of a
  disputed shared claim is reconciled by DEL-02-02_shared-meaning-reference;
  query behavior by DEL-03-01_maintenance-toolkit. It claims no consumer adoption.

### DEL-02-01_maintenance-procedures — Carry and recover an authorized holding change

- **ParentPackageID:** PKG-02. **Type:** Library maintenance procedure set.
  **ResponsibleParty:** TBD — maintenance-method contributor.
- **Local goal:** A maintainer can add/revise, organize/retire, diagnose, assess
  connected change, review/integrate and recover a holding, including its own
  maintenance means, using an available method with actual authority and evidence.
- **CoversScopeItems:** SOW-0004, SOW-0005, SOW-0006, SOW-0007, SOW-0008,
  SOW-0010, SOW-0017, SOW-0018, SOW-0021.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-003, OBJ-004, OBJ-005.
- **Anticipated artifacts:** Connected/revised applicable workflow/skill/role
  guidance at its existing homes, beginning with create-workflow, change,
  bounded-reconciliation, coordinated-knowledge-work and the Root change skill;
  explicit selection of proportionate content/behavior/interface checks and
  treatment of unavailable capabilities; an exceptional custody/recovery procedure
  using an existing coordination/locking mechanism with holder, item, operation,
  release/recovery condition and truthful enforcement limits. Publication/update
  inspection refers to DEL-05-02_publication-candidate's path. Repair selected
  setup/ScopeOfWork instruction clauses identified in §6; retain a usable current
  basis until replacements are checked and adopted. No workflow per operation.
- **Evaluation:** A2 and A5 through an actual authorized instruction/tool repair
  under the preceding method; the known current-locality repair is a candidate
  case, not yet executed. A8 via retained work or a labelled interrupted-custody
  case that tests recovery and the mechanism's limits. Keep source/review evidence
  sufficient to repeat or recover the case; do not create a routine case register.
- **Needed inputs / use conditions:** When a method directs a command, consume
  its verified command/dependency/write/failure contract from
  DEL-03-01_maintenance-toolkit or the selected existing tool source (R05–R06).
  For the actual maintenance case, use the authorized diff, checked revision and
  review evidence for that change; case revision is TBD until work is selected.
  For custody, use the actual repository/host coordination mechanism available
  for that operation; specific holder and mechanism are TBD, and no enforcement
  claim is permitted until examined (R14). For semantic repair use the scoped
  applicability basis of DEL-02-02_shared-meaning-reference; content disagreement
  cannot be resolved by replacing a check or applying proposed instructions to
  their own review.
- **Boundary:** General procedure and authority clauses belong here; code and
  direct invocation truth belong to DEL-03-01_maintenance-toolkit. Shared-file
  changes use one designated editor/integrator per change. No frozen verification,
  extra removals, commitments or new permissions are authorized by this procedure.

### DEL-02-02_shared-meaning-reference — Make library and adopted-product meanings explicit

- **ParentPackageID:** PKG-02. **Type:** Shared concept and applicability reference set.
  **ResponsibleParty:** TBD — knowledge/reference contributor.
- **Local goal:** A maintainer or consumer can distinguish reusable library
  definitions and current Root practice from scoped adopted contracts, historical
  runtime policy and explanatory editions, and use the affected claims coherently.
- **CoversScopeItems:** SOW-0016.
  **SupportsObjectives:** OBJ-002, OBJ-003.
- **Anticipated artifacts:** Warranted revisions/qualifications in the affected
  sections of docs/AGENT_WORKFLOW_RUNTIME.md, docs/PRODUCT_BOUNDARIES.md and
  docs/COMPATIBILITY_FORMATS.md; consequential updates or explicit earlier-basis
  qualifications in affected thesis/manual passages at their maintained homes.
  The initial comparison is the §6 reusable-versus-Root/frozen-runtime wording
  and current execution representation. Preserve original invariant identities,
  consumer-adopted meanings and retained editions. A scoped reference clarification
  can be the whole output; no new ontology, universal manual or four-report set.
- **Evaluation:** A4's scoped inconsistency/applicability case with definitions,
  warranted claims, described actions and governing values examined together;
  affected guidance and publication claims agree or expose a genuine retained
  conflict. The raw wording in §6 identifies the comparison, not a prior ruling
  that all historical statements should be rewritten. ScopeOfWork must bind the
  selected case and evidentiary test; mere cosmetic edits do not establish A4.
- **Needed inputs / use conditions:** Use accepted PRD §§2.3/6.1, current AGENTS,
  the relevant cited reference passages and their original adopted source meaning
  before changing applicability. For a claim about executable behavior, require
  observed evidence from the selected operation/DEL-03-01_maintenance-toolkit;
  documentation alone cannot establish it. If a named consumer adopted a disputed
  clause, its exact maintained contract/basis is needed before incompatible change;
  that external source is TBD, carried by DEL-05-01_consumer-use-guide. Preserve
  the existing scoped contract while the binding is unresolved. Publications use
  their explicit edition/source, not just a mutable “current” link.
- **Boundary:** This is a bounded reference improvement, not a global coherence
  audit or a rewrite of every publication. Runtime implementation, professional
  acceptance and consumer policy stay outside Root's change authority.

### DEL-03-01_maintenance-toolkit — Support current localities with actual reusable tools

- **ParentPackageID:** PKG-03. **Type:** Executable maintenance utility set with usage contract.
  **ResponsibleParty:** TBD — software contributor.
- **Local goal:** Existing repeatable setup, validation and query operations
  support the adopted Root locality and meaningful local conditions, with commands
  whose inputs, dependencies, effects, failure handling and limits are accurate.
- **CoversScopeItems:** SOW-0009, SOW-0015, SOW-0024.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-004, OBJ-005.
- **Anticipated artifacts:** Bounded revisions to the selected existing
  tools/scaffolding helpers and applicable fileset checks, paired with the
  preparation skill's direct tool-use instructions, to provide the accepted
  flat locality without required legacy phase/control scaffolding. Establish
  applicability of tools/scope_of_work validation/INIT helpers and repair only
  demonstrated incompatibilities. Reuse tools/deliverables and workflow-runtime
  utilities; amend their code/README/checks only for an actual connected defect.
  Retain meaningful focused regression cases in maintained tool tests. This is a
  set of existing utilities and necessary usage information, not a new unified
  framework. A new helper is considered only if the existing route demonstrably
  cannot meet the bounded need; SOW-0033 has no production allocation.
- **Evaluation:** Exercise current-locality creation, rerun preservation and
  identity/path/schema checks in an authorized isolated fixture before live setup;
  targeted regression and independent scrutiny for persistence/containment changes.
  Exercise live-metadata selection, distinct conditions, partial/unknown/cyclic
  views and project-root references where affected. Check actual invocation and
  failure/absence behavior with declared Git/HEAD/PyYAML or other dependencies.
  Do not alter expected results merely to pass or broaden into frozen products.
- **Needed inputs / use conditions:** Accepted R08 locality and Group 1 output
  definitions supply the target contract; existing scaffold/validator sources and
  any affected legacy caller contract supply preservation conditions before a
  helper changes. Exact affected caller fixtures are selected from the bounded
  diff; undiscovered callers stay an uncertainty, not assumed absent. The final
  accepted DEL identities and selected setup scope from
  DEL-04-01_execution-decomposition are required before live creation, though
  current-contract fixture repairs can be developed under separately authorized
  maintenance work. Named external compatibility evidence is required before any
  incompatible exported interface change (DEL-05-01_consumer-use-guide).
- **Boundary:** The executable behavior/direct usage contract is owned here;
  DEL-02-01_maintenance-procedures supplies the governing method and
  DEL-04-02_local-execution-contracts performs particular setup/use. No file-only
  query adapter, companion, graph service or new host enforcement is presumed.

### DEL-04-01_execution-decomposition — An accepted design for Root's local goals

- **ParentPackageID:** PKG-04. **Type:** Project decomposition design package.
  **ResponsibleParty:** TBD — decomposition contributor, coordinated by Agent 0.
- **Local goal:** Root has bounded, coherent contributions linked to accepted
  product objectives and usable as the basis for local contract authoring/setup.
- **CoversScopeItems:** SOW-0011.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-004.
- **Anticipated artifacts:** The maintained PROJECT_DECOMP.md and only necessary
  companion tables, finalized through project-decomp's actual Group 2 decision,
  independent Group 3 audit and final owner acceptance; accepted snapshots and
  pointers only when their real decisions occur. This continuing decomposition
  already supplies part of the output. Group 1 is not repeated, and a new
  decomposition project is not recursively created to produce this one.
- **Evaluation:** Coverage, identity/coupling, boundaries, concrete outputs and
  unresolved choices checked against the accepted basis; separate final audit and
  owner decision before downstream setup. Acceptance is not authored by the
  implementation contributor. This Group 2 proposal is partial work toward that
  result, not a claim that the deliverable is already complete.
- **Needed inputs / use conditions:** Consume the verified Group 1 snapshot for
  structure, then the actual accepted Group 2 snapshot for final audit; method
  resources fix the ordering (PRD §6.2–6.3). An auditor's actual independent return
  and the owner's final decision are required for the downstream accepted basis;
  both are pending, no fabricated bindings. Current source changes must be checked
  for which accepted decisions they affect; do not reopen unaffected identities.
- **Boundary:** Produces the decomposition basis, not local ScopeOfWork contracts,
  production files or general project-management automation. The existing
  authorized decomposition proceeds before its own future locality exists.

### DEL-04-02_local-execution-contracts — Use local goals, conditions and reasoning in Root

- **ParentPackageID:** PKG-04. **Type:** Local execution contract and work set.
  **ResponsibleParty:** TBD — execution-planning contributor.
- **Local goal:** Accepted, activated Root contributions have usable local
  commitments and evidence-informed input/use conditions, and can choose and
  revise action while checking their effects on neighboring uses.
- **CoversScopeItems:** SOW-0012, SOW-0013, SOW-0014.
  **SupportsObjectives:** OBJ-001, OBJ-002, OBJ-003, OBJ-004.
- **Anticipated artifacts:** For each accepted/activated DEL, the particular
  ScopeOfWork.md, deliverable.yaml and Work/ locality using the numeric path
  convention. ScopeOfWork carries accepted scope/objectives, outputs, boundaries,
  criteria and verification; YAML carries actual consumer needs/conditions and
  useful code/check/source references; Work/ carries current reasoning, evidence,
  alternatives, consequential attempts and unresolved conditions with maturity
  explicit. Distinct DEL localities are instances of this contract/work kind,
  not new decomposition Deliverables. Their continuing content ownership passes
  to the contributor responsible for that local goal; this setup contribution
  does not control everyone's subsequent work.
- **Evaluation:** After authorized setup, apply applicable ScopeOfWork validation
  and `python3 -m tools.deliverables --project . check`, then inspect relevant
  neighborhoods and assess actual conditions. Demonstrate A3 on a real authorized
  local action whose evidence changes its route/understanding, examining affected
  uses; retain recovery information sufficient for A8. These checks do not mark
  suitability automatically and do not require a complete graph.
- **Needed inputs / use conditions:** The final accepted decomposition and
  selected activation scope are necessary before materialization (PRD §6.3), from
  DEL-04-01_execution-decomposition and actual owner/coordinator steering.
  Consume the checked current-locality path from DEL-03-01_maintenance-toolkit
  and applicable authoring/authority route from DEL-02-01_maintenance-procedures;
  the observed legacy mismatch holds live setup, not all planning work. Each
  consumer's specific needs are authored from its accepted scope and relevant
  sources; unknown suppliers remain unknown. A3 requires an actual authorized
  change and evidence, not synthetic empty YAML; select that case with the owning
  contributor when execution starts.
- **Boundary:** No legacy phase folders or lifecycle records are silently adopted.
  Setup does not alter source commitments to fit a validator or move code and
  publications into Work/. Unchanged declarations stay unchanged. No second
  progress graph or upstream supplier commitment is manufactured.

### DEL-05-01_consumer-use-guide — Obtain and qualify an identified library selection

- **ParentPackageID:** PKG-05. **Type:** Consumer-use and compatibility guide.
  **ResponsibleParty:** TBD — technical publishing contributor.
- **Local goal:** A consumer can consult, invoke or copy selected library material
  with the required resources/notices and actual basis, and assess a claimed
  interface against a named maintained contract without adopting Root authority.
- **CoversScopeItems:** SOW-0019, SOW-0020, SOW-0025.
  **SupportsObjectives:** OBJ-002, OBJ-003, OBJ-005.
- **Anticipated artifacts:** A documented files/Git/archive use path, resource and
  notice requirements, source/adaptation distinctions and compatibility limits
  in the existing README and selected tool/workflow/reference guides; add a small
  owning guide only if those homes cannot make the route usable. Named-consumer
  qualification evidence at a specified revision, with cleared public fixtures
  or summaries and private evidence retained locally. Supported path/adapter
  guidance before incompatibility; implementation of a necessary existing-tool
  repair remains DEL-03-01_maintenance-toolkit. No new adapter allocation occurs
  through this guide.
- **Evaluation:** A6 obtains and uses identified material without an undisclosed
  checkout/private dependency; resources/notices remain present. Check claimed
  compatibility against the actual named maintained contract/fixture revision.
  Generic examples and Root component tests do not substitute. Public-boundary
  and credential/private-term checks apply to the actual distribution candidate.
- **Needed inputs / use conditions:** The selected export/use surface and its
  resources/licenses at the candidate revision are required before qualification.
  PRD R13/A6 require a named consumer contract/fixtures; **consumer, source location
  and exact revision are TBD (Q-04)** until the actual interface is selected and
  authorized evidence is available. App v4/SWBPIPE are possible independent
  consumers, not assigned suppliers; no private inventory is required now. Before
  an incompatible change, require an evidenced supported path or coordinated
  adapter, with the consumer's authority preserved. Without that input, ordinary
  guide work continues but the named compatibility claim remains unverified.
- **Boundary:** Consumers own data, adoption, product implementation and release.
  No undisclosed private input becomes a public build/use dependency; no external
  project write, contact or verification is authorized by this proposal alone.

### DEL-05-02_publication-candidate — An inspectable version and a recoverable change account

- **ParentPackageID:** PKG-05. **Type:** Versioned library publication package.
  **ResponsibleParty:** TBD — technical publishing contributor.
- **Local goal:** The owner can review an identifiable publication candidate and
  meaningful change account, and consumers can inspect changes from their actual
  basis while retaining recoverable source/edition history and independent adoption.
- **CoversScopeItems:** SOW-0022, SOW-0023, SOW-0026.
  **SupportsObjectives:** OBJ-003, OBJ-005.
- **Anticipated artifacts:** A named candidate from a selected verified library
  revision, its required resources/notices/dependencies/limitations and meaningful
  old/new change account in the existing publication/review route; documented
  polling/inspection using ordinary release/diff facilities, including failed or
  partial inspection, examined-versus-used basis and migration consequences.
  Source-preserving edition/render outputs only for the selected publication
  form, using existing rendering tools if applicable. Preserve the existing
  archive recovery route and original consumer pins; do not repeat the reset or
  remove plans/ or _DomainEngines/. Copies/renders are derivative of the named
  maintained source, not new source homes.
- **Evaluation:** A7 exercises the actual documented inspection against a prior
  identified basis, checking no-change/changed/partial-or-failed reporting as
  applicable. Verify the candidate's real delivery form and source/notice/resource
  completeness. For any historical bytes actually relied on, verify reachability
  and selected content, reusing applicable prior preservation evidence. This is
  candidate preparation, never an owner release or claimed consumer adoption.
- **Needed inputs / use conditions:** Require a selected verified candidate
  revision, prior comparison basis and affected-holdings change descriptions;
  exact candidate/version label and comparison revision are TBD until preparation
  (Q-05). The consumer path and declared compatibility limits from
  DEL-05-01_consumer-use-guide must match the candidate before it is proposed for
  publication. Retained edition sources and archive references must identify the
  historical basis relied on; the reset's accepted preservation evidence is an
  input, not authority for a fresh global history audit. Scheduling or external
  delivery only applies if separately selected with actual configuration/authority.
- **Boundary:** Publication describes and packages selected verified holdings.
  It does not author all their underlying claims or reopen every edition; affected
  meaning changes route to their owning contribution. A merge is not publication.

## 9. Interfaces, grouping reasons and acceptance coverage

These are bounded use conditions and integration responsibilities, not an execution
DAG, supplier appointments or finish-to-start promises. Source availability and
suitability must be assessed for the specific case. Preliminary and final uses
may differ; no Package completion gate is inferred from an input named above.

| Interface / possible overlap | Proposed treatment |
|---|---|
| Entry and consumer guide both touch README or an owning index | DEL-01-01_library-discovery-guide owns navigation meaning; DEL-05-01_consumer-use-guide supplies obtaining/copying/use conditions. Agent 0 assigns one editor for a shared change and checks the combined result. No directory is exclusively owned by a DEL. |
| Reference, instruction and tool changes share locality/authority terms | DEL-02-02_shared-meaning-reference establishes the warranted applicability; DEL-02-01_maintenance-procedures changes method/authority clauses; DEL-03-01_maintenance-toolkit changes executable support/direct usage. A single coordinated diff may serve all; file overlap does not license competing writes. |
| Setup must use means that need repair, while those means may later have a locality | Existing authorized Root maintenance procedure can repair selected means at their actual source before materialization. The accepted decomposition supplies target identity/scope; a verified tool/method path is needed before live setup. Record that actual checked change in the resulting locality later; no recursive setup or fabricated completion. |
| A repaired output versus available maintenance procedure | Tool/reference authors produce the changed holding; DEL-02-01_maintenance-procedures must establish reusable procedure and A2/A5 evidence. One actual case may support both; reuse its checked evidence rather than create duplicate reports. |
| Historical retention versus retirement authority | PKG-05 retains source/edition routes and existing pins (SOW-0026); PKG-02 accounts for SOW-0030/0032 exclusions/reservations. Neither creates removal scope. |
| Generic reusable library surface versus named consumer interface | DEL-05-01_consumer-use-guide requires the actual contract/fixture basis before its compatibility claim. A library component pass cannot qualify an unknown consumer; consumer adoption and release do not gate a verified library interface. |
| Content meaning versus versioned delivery | DEL-02-02_shared-meaning-reference owns scoped semantic clarification; DEL-05-02_publication-candidate packages/checks identified source and explains changes. Historical editions retain earlier-basis qualifications; no blanket re-render or new release authority. |

All Packages are design-scoped to one discipline. PKG-02's procedure set and
reference set are different artifact kinds (action guidance versus definitions/
applicability); PKG-04's decomposition and local contracts are design basis versus
particular commitments/work; PKG-05's consumer guide and publication package are
use/compatibility instructions versus a versioned transferable result. PKG-01 and
PKG-03 each have one kind-level Deliverable. There is no sheet/file/command/edition
per Deliverable rule. Scope is partitioned by accountable outcome, while each
contribution remains subject to the applicable authority, coherence, evidence and
public-boundary constraints regardless of those constraints' Package home.

### Objective-to-Deliverable view

Derived from the canonical ledger; shared objectives indicate purpose, not input
edges. Every accepted objective has proposed production support.

| ObjectiveID | MappedDeliverables |
|---|---|
| OBJ-001 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-03-01_maintenance-toolkit, DEL-04-01_execution-decomposition, DEL-04-02_local-execution-contracts |
| OBJ-002 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-02-02_shared-meaning-reference, DEL-03-01_maintenance-toolkit, DEL-04-01_execution-decomposition, DEL-04-02_local-execution-contracts, DEL-05-01_consumer-use-guide |
| OBJ-003 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-02-02_shared-meaning-reference, DEL-04-02_local-execution-contracts, DEL-05-01_consumer-use-guide, DEL-05-02_publication-candidate |
| OBJ-004 | DEL-02-01_maintenance-procedures, DEL-03-01_maintenance-toolkit, DEL-04-01_execution-decomposition, DEL-04-02_local-execution-contracts |
| OBJ-005 | DEL-01-01_library-discovery-guide, DEL-02-01_maintenance-procedures, DEL-03-01_maintenance-toolkit, DEL-05-01_consumer-use-guide, DEL-05-02_publication-candidate |

### Proposed evidentiary contributions to PRD acceptance

These are evaluations of the accepted criteria, not new or amended criteria.
One authorized case can establish several claims, with limitations explicit.

| PRD criterion | Principal proposed result / evidence |
|---|---|
| A1 | DEL-01-01_library-discovery-guide's bounded route, using actual local conditions from DEL-04-02_local-execution-contracts and query limits from DEL-03-01_maintenance-toolkit |
| A2 | DEL-02-01_maintenance-procedures's actual maintenance case; DEL-03-01_maintenance-toolkit's current-locality repair is a concrete candidate |
| A3 | DEL-04-01_execution-decomposition's accepted goal mappings plus DEL-04-02_local-execution-contracts's actual action/condition and revised understanding with affected uses examined |
| A4 | DEL-02-02_shared-meaning-reference's scoped applicability/meaning reconciliation, using DEL-02-01_maintenance-procedures's evidence and review route |
| A5 | DEL-02-01_maintenance-procedures's change to maintenance means under the preceding basis, supported by the actual affected tool/entry change; no self-authorization |
| A6 | DEL-05-01_consumer-use-guide's identified copy/use case and named-contract qualification; Q-04 remains unresolved |
| A7 | DEL-05-02_publication-candidate's real delivery form and exercised prior-basis inspection, with DEL-05-01_consumer-use-guide's resource/notice/compatibility limits |
| A8 | DEL-02-01_maintenance-procedures's recovery/custody case and DEL-04-02_local-execution-contracts's actual retained basis/conditions; custody enforcement must be observed, not assumed |

## 10. Decisions proposed, findings and open matters

Group 1 decisions are already accepted. The choices below propose the Group 2
structure and its treatment of exceptions; they are not owner rulings. No
substantive change to the Group 1 basis is proposed or needed to prepare this
structure. An actual later conflict reopens only the affected decisions through
the applicable authority.

| Ref | Proposal / finding | Consequence and next treatment |
|---|---|---|
| G2-01 | Five flat Packages partition scope by intended use, not O/R labels, directories or the three forms. §7 gives discipline and boundaries. | Owner confirms/corrects the partition at Group 2. Every OUT/TBD item has an accountable home without production allocation. |
| G2-02 | Eight kind-level Deliverables group semantically coupled artifacts and verification. A revised holding is sufficient; repeated files/cases are instances. | Owner confirms/corrects goals and anticipated results. No general application, three-output checklist or one-workflow-per-operation mandate. |
| G2-03 | SOW-0011 maps to the ongoing decomposition itself; SOW-0026 maps to historical preservation within publication preparation. | Neither is restarted as a duplicate project/removal job. Existing accepted work/evidence remains usable. |
| F-01 | Known applicability mismatch: phase/control scaffolding and unconditional status references conflict with the selected current Root locality when used as its setup route (§6). | DEL-03-01_maintenance-toolkit and DEL-02-01_maintenance-procedures must establish a compatible selected path before DEL-04-02_local-execution-contracts performs live setup. This is an implementation prerequisite, not a blocker to proposing Group 2. Do not weaken validators or fabricate control files to pass. |
| F-02 | Shared reference wording needs bounded applicability reconciliation with independent consumer authority and frozen Runtime standing (§6). | DEL-02-02_shared-meaning-reference preserves historical/adopted contracts and compares the affected guidance/publication claims. No wholesale reference or publication rewrite is justified. |
| Q-01 | RESERVED — SOW-0032, PKG-02: additional plans/, _DomainEngines/ or archival removals. | Retain unless the owner specifically changes disposition. No production Deliverable allocated. |
| Q-02 | CONTINGENT — SOW-0033, PKG-03: new bespoke tooling/companion/adapter needs a demonstrated gap. | No production Deliverable allocated. Existing-tool repair under SOW-0009/0024 is proposed; that does not assume a new product. A gap can be investigated locally; changed commitments return to the owner. |
| Q-03 | RESPONSIBILITY — all eight Deliverables have an explicit TBD implementation contributor. Agent 0's integration role is established; no individual assignments have been made. | Assign a capable owner in each bounded execution brief. Does not require a new staffing layer or block structural review; no work is silently assigned to this preparer. |
| Q-04 | INPUT BINDING — DEL-05-01_consumer-use-guide, SOW-0020: named consumer, maintained contract/fixture location and exact revision remain TBD. | Must be resolved before A6/named compatibility is claimed or an incompatible change proceeds. Continue independent use-guide work. No unauthorized consumer access/contact implied. |
| Q-05 | CANDIDATE BASIS — DEL-05-02_publication-candidate, SOW-0022/0023: actual verified candidate revision, candidate label and comparison basis remain TBD until publication preparation. | Bind real sources for A7; do not invent a release or assume main was published. Owner release remains a separate act. |

The material choice for the owner now is the proposed Package/Deliverable
structure and exception treatment. Q-01 remains a reserved future disposition;
Q-02 stays conditional. Staffing, case selection and exact version/input bindings
are operationally unresolved where stated; they are not concealed scope changes
or extra approvals. Agent 0 has reviewed this candidate against the accepted
basis, current sources and the selected method; no blocking finding remains
before the owner's Group 2 decision.

## 11. Coverage telemetry and preparation checks

| Field | Group 2 candidate value |
|---|---|
| Revision | G2-candidate-2, 2026-10-31 |
| ScopeItemCount | 33: 26 IN, 5 OUT, 2 TBD, unchanged from accepted Group 1 |
| PackageCount | 5 flat Packages, one declared discipline each |
| DeliverableCount | 8 proposed, each coupled to one parent and one concrete artifact kind |
| ObjectiveCount | 5 accepted identities/meanings |
| UnassignedScopeItems / multiply assigned Package homes | 0 / 0 |
| ScopeItemsWithoutDeliverableMapping | 0 IN items; all seven OUT/TBD items have empty production mapping |
| UnmappedObjectives | 0; every objective has supporting proposed Deliverables |
| Responsibility completeness | 8 explicit TBD contributor assignments; Agent 0 integration owner retained |
| Anticipated artifact completeness | 8 of 8 cards name concrete artifact sets, source homes, evaluation and input/use conditions |
| OpenIssuesByType | Reserved disposition 1 (Q-01); conditional scope 1 (Q-02); staffing 1 covering 8 assignments (Q-03); external input binding 1 (Q-04); publication candidate basis 1 (Q-05) |
| Material implementation findings | 2: setup-path applicability (F-01), shared-reference applicability (F-02); neither claims a Group 1 contradiction or completed repair |
| Source / criterion coverage | O1–O5, R01–R17 including all R04 operations, A1–A8 retained and linked to proposed contributions |

Preparation checks on this candidate:

- **Identity and accepted-basis fidelity — pass:** all three Group 1 manifest
  entries verify; the PRD hash, current HEAD and branch match the assignment.
  The snapshot and Group 1 pointer match their committed bytes. All 33 accepted
  scope IDs, statements, classifications, source/objective mappings and substantive
  qualifications are preserved; only SOW-0011's checkpoint-status note changes.
  The five objective table rows are identical to the accepted rows. Vocabulary
  changes only update the historical proposal/stage standing.
- **Allocation and references — pass:** one valid flat Package home per scope
  item; all IN items map to a same-Package Deliverable; no OUT/TBD production
  mappings. Eight unique filesystem-safe DEL IDs have sequential within-Package
  counters and correct coupling. All SOW/OBJ/PKG/DEL references resolve; card
  scope/objective fields agree with the ledger and the objective summary. All
  R01–R17 and A1–A8 coverage rows remain present. Local Markdown file targets
  resolve; no conflict markers are present.
- **Design and boundary inspection — no blocking structural finding identified
  by the author:** five single-discipline declarations; eight concrete kind-level
  artifact sets with explicit goals, evaluation, sources and use conditions.
  Shared-source editing, bootstrap setup, historical retention and independent
  adoption are addressed in §9. Repeated instances do not become Deliverables.
  Responsibility is explicitly TBD in eight cases (Q-03), not falsely assigned.
  Implementation prerequisites and input gaps remain F-01/F-02 and Q-04/Q-05.
- **Public-content screening — local checks pass:** the maintained credential
  scanner's `findings` function screened the candidate bytes without findings.
  The maintained private-term scanner used its permitted local host-term source
  without printing terms; candidate content/path and JUnit hostname screening
  found none. This does not claim checking the hosted `PRIVATE_TERMS` secret set
  or future commit metadata; required integration checks remain with Agent 0.
- **Write boundary — pass:** only PROJECT_DECOMP.md is modified; no untracked
  outputs, staged changes, snapshot edits or live localities were created. Checks
  ran in memory without modifying validators or creating test artifacts.

Agent 0 independently reviewed the package purposes, deliverable goals, concrete
output kinds, input/use conditions, shared-file boundaries and bootstrap route.
Source inspection confirmed the setup-path mismatch. Read-only checks verified
the immutable Group 1 manifest, accepted statement/objective fidelity, scope
allocation, card/ledger/summary agreement, links and stage boundaries. Candidate
credential and available local host-term screening passed. The proposal needs no
substantive repair before presentation; F-01/F-02 and Q-01–Q-05 retain their stated
treatment. This review does not substitute for the independent Group 3 audit.
No implementation,
consumer qualification, setup, publication release or product acceptance is
claimed by these counts. Sources/tools were inspected, not exercised for product
behavior; no frozen/product builds or external consumer operations were run.

The existing XRG decomposition checker consumes Deliverables.csv/ScopeLedger.csv
(and optional context registers); it does not inspect this inline representation.
Its skipped-family result would not validate this candidate. DOMAIN validation
is inapplicable. Read-only in-memory checks can validate these Markdown tables
without inventing companion registers or weakening a validator. Group 3's
independent final audit and the owner's final acceptance remain outstanding.
Live locality/ScopeOfWork checks apply after authorized setup, not to this design.

## 12. Working-package inventory and next boundary

`execution/_Decomposition/PROJECT_DECOMP.md` remains the sole canonical **Group 2
candidate**. Scope allocation is in §4; concrete outputs and needed inputs are
local to each §8 card; summaries derive from those declarations. No CSV/JSON
companions or separate dependency/review/handoff registers are needed at this size.

The accepted Group 1 snapshot and `_LATEST_GROUP1.md` remain byte-identical and
continue to govern the basis. There is no Group 2 acceptance snapshot or pointer,
no final accepted pointer and no setup in this contribution. Agent 0's review is
complete; the owner's Group 2 decision is pending. After that decision, the
coordinator finalizes its snapshot before the independent Group 3 audit. Stop
here until that boundary is crossed under the actual authority.
