# Chapter 8 — Evidence and Evaluation

## 8.1 Subject and Evidence Basis

This chapter evaluates what the available evidence establishes about Root's
shared instructions, roles, methods, queries and connecting paths. Its source
basis is commit `a602024416ace9652f61bb2043889c307fd4e09d`. The analysis concerns
that implementation and its recorded examinations; it is not a fresh audit of
the current products. [Appendix E](appendix_e_development_history.md) preserves
the development record, earlier arrangements and the limits of that history.

Root's principal contribution is normative: purposes, responsibilities, distinctions
and criteria guide work while remaining open to correction. Its tools also make
some relationships operable. The App supplies the chiefly operative perspective;
Piping supplies the chiefly evaluative perspective as a domain-software instance.
Evidence in one perspective can inform another without establishing its claims.
Ontology, epistemology, praxeology and axiology concern all three.

The evaluation distinguishes specification, exercised behaviour and adequacy for
use. A written contract establishes what was required. A passing check establishes
what its inputs and predicates exercised. Professional adequacy and human
engagement need grounds appropriate to their own subjects.

## 8.2 Authorization and Enforced Boundaries

### 8.2.1 Responsibility and Authorization

The source basis contains four general role files:

| Role | Contribution |
|---|---|
| HELP_HUMAN / Agent 0 | Purpose, alignment and continuity with the person |
| HELPS_HUMANS | Design workflows, tools and projects with the person |
| WORKING_ITEMS | Own implementation, assignments and integration |
| TASK | Execute a bounded assignment without delegation |

These contributions describe responsibility. Human assignment and adopted policy
establish authorization; the host supplies capability and enforces permissions
on its actual paths. One session can carry several contributions. Agent 0's
continuing responsibilities need not imply a separate managerial tier.

### 8.2.2 Exercised Permission Behaviour

[PR #1223](https://github.com/sgttomas/chirality/pull/1223) couples the
HELP_HUMAN authorization interpretation with resolver boundary tests. The resolver
retains authorized write targets while denying unauthorized targets and respecting
a read-only host. Tests cover absent authorization and escaping targets, including
symlink escapes. This supports the resolver behaviour under the examined conditions.

That result does not establish containment of every command, host or App entry
point. An instruction, a tested path predicate and an operating-system sandbox
have different coverage. App v4's role configuration remains a product contract.
The [workflow resolver contract](../../tools/workflow_runtime/README.md) defines
its own operations; a claim about broader containment requires evidence about
broader paths.

## 8.3 Access to Relevant Meaning

### 8.3.1 Current Sources and Queries

Active project deliverables maintain commitments and acceptance criteria in
`ScopeOfWork.md`, useful technical reasoning in `Design/`, and consumer-owned
needs and conditions in `deliverable.yaml`. The
[Root entry](../../execution/_Coordination/LOOP_INIT.md) locates the shared
component and affected consumers; an active project entry locates product
commitments. The authorized undertaking directs the inquiry.

The [deliverable CLI](../../tools/deliverables/README.md) exposes
`neighborhood`, `impact`, `touches`, `dag-diff` and `check`. It reports source
locations and its observed basis, including working-tree changes. Code mappings
indicate relevance, not exclusive ownership. Missing mappings leave a partial
answer rather than proving absence of consumers.

`check` rejects malformed data and invalid or escaping identities and paths.
Unresolved suppliers, planned paths and cycles are reported distinctly. Mutual
or non-gating relationships can legitimately form cycles. The checker does not
establish an input's suitability; an agent must examine its condition and actual
contents within the assignment.

### 8.3.2 Preservation of Meaning Through Transformation

[App v4 PR #1213](https://github.com/sgttomas/chirality/pull/1213) and
[Piping PR #1216](https://github.com/sgttomas/chirality/pull/1216) provide bounded
evidence about preservation of dependency conditions. Source-row accounting and
comparison with identified graph bases detect omitted or changed declarations.
Independent examination of meanings complements those mechanical checks.

This supports preservation on the examined basis. It establishes neither that
the source declarations captured every real dependency nor that any supplier
met its consumer's condition. Several distinct conditions between the same pair
of deliverables must remain intelligible; reducing them to one readiness label
would lose part of the relationship.

### 8.3.3 Method Selection and Actual Consumers

Methods are indexed in `workflows/index.json` and selected as needed. The resolver
specifies ordered selection, explicit resources and source identities. Missing
or escaping selected resources fail resolution; omitted resources are not read.
Returned hashes identify the inputs read by the resolver. They do not establish
that the host delivered them to an agent or that the agent applied the method.

The [workflow index builder](../../tools/validation/build_workflow_index.py)
connects package metadata to the catalog. An adopted App bundle is a separate
consumer. The useful evidence concerns the saved source, selected identity,
affected consumer and checked connection. Updating a shared source alone cannot
establish adoption by each product.

## 8.4 Production, Examination and Integration

### 8.4.1 Continuing Ownership

The [coordinated-knowledge-work workflow](../../workflows/coordinated-knowledge-work/WORKFLOW.md)
organizes purpose, integration, contributions and scrutiny. Owners remain with
ordinary repairs. Independent work can continue while an unrelated branch is
unresolved; shared writes, interfaces, resources and review capacity can require
coordination. A missing declared edge cannot prove independence.

The implementation supplies a usable method, not proof that every undertaking
retains intent or reaches integration. Continuity draws on current artifacts,
conversation, tool queries and Git history, with recovery support where needed.
Recovery requires evidence from an actual continuation: a preserved conversation
alone does not establish that work resumed without loss or duplicated action.

### 8.4.2 Selected Checks and Reuse

The [CI selection reference](../CI_SELECTION.md) defines `harness` as the required
aggregate result for repository checks and selected active-product workflows.
Unrelated jobs can be skipped explicitly. A selected failed, cancelled or missing
job must prevent the aggregate from passing. Selection and failure propagation
are distinct properties requiring examination.

[PR #1214](https://github.com/sgttomas/chirality/pull/1214) supplies recorded
checks of that selection. Applicable prior passes can be reused, with the explicit
qualification that no new tests executed. A build cache is not a prior test result;
manual runs can obtain fresh evidence. Reuse depends on applicability to the
candidate and concern, rather than the mere existence of a green result.

The repository selects targeted regression checks and independent scrutiny for
numerical meaning, persistence, permissions and destructive operations. Routine
reversible work can be inspected or exercised directly. This selection principle
makes consequence and detectability relevant; it cannot establish that every
important behaviour was selected or that the checks cover it adequately.

### 8.4.3 Evidence at Connecting Paths

The integration reviews recorded in [Appendix E](appendix_e_development_history.md)
identified live technical references among intended removals. Repair needed both
relocation and consumer updates. A passing generated-product test did not establish
that the next generator invocation would remain usable. The connecting path,
rather than the isolated component, was the subject requiring examination.

[App PR #1240](https://github.com/sgttomas/chirality/pull/1240) supplies a different
witness: actual native interaction exposed role-header accumulation and input
autocorrection defects, followed by repair. This supports exercising the assembled
application. It does not establish general usability or absence of other defects.
The appropriate finding concerned product behaviour and prompted product repair.

Agents can perform extensive reckoning on such evidence: inference, criticism,
comparison, investigation and authorized action. Human judgment sets and revises
the undertaking's purpose and what the person can stand behind throughout.
Independent agent scrutiny can improve the grounds without performing that
person's act of reliance.

## 8.5 App and Domain-Software Evidence

### 8.5.1 Operative Perspective: The App

The [App PRD](../../projects/chirality-app-v4/docs/PRD.md),
[architecture](../../projects/chirality-app-v4/docs/ARCHITECTURE.md) and
[App thesis](../../projects/chirality-app-v4/docs/thesis/README.md) define the
application-specific inquiry. Conversations, request cards, workflow authoring,
trial runs and inspection of returned work supply operative paths through which
intent and methods can be tried and revised.

The [host-integration contract](../../projects/chirality-app-v4/docs/HOST_INTEGRATION.md)
proposes discoverable application capabilities. A common catalog does not establish
correct domain behaviour, good interfaces, recovery or every transport adapter.
[PR #1244](https://github.com/sgttomas/chirality/pull/1244) assigns file and record
writes, supplier interaction and capture of human acts to the Rust host, while
the web view presents and sends human-initiated requests. This ruling is a product
commitment; its text alone does not establish conformance of all paths.

An accepted act and substantive engagement remain different claims. Capturing a
human action can support attribution and identify its subject. It cannot establish
that the person understood the consequences or performed adequate professional
examination.

### 8.5.2 Evaluative Perspective: Piping

The [Piping PRD](../../projects/chirality-piping/docs/PRD.md) distinguishes
physical models, analytical models, analysis runs, comparison and handoff. These
objects need domain definitions, numerical implementation and evidence. The
[SWBPIPE thesis](../../projects/chirality-piping/docs/thesis/README.md) examines
that instantiation, including the limits of its calculations and engineering use.

Operation validation, numerical verification and engineering adequacy answer
different questions. Operation validation examines whether a proposed change
satisfies the engine's defined conditions. Numerical verification examines
calculation against an appropriate reference or method. Engineering adequacy
concerns whether physical intent, model assumptions, cases, alternatives and
results support the proposed use. Passing the first cannot establish the others.

The [illustrative support-arrangement revision](WORKED_EXAMPLE.md) links those
questions to practical alternatives and the person's choice and revision. It is
an illustration, not measured evidence. Piping is one domain-software instance;
its numerical results do not establish economical transfer to all domains.

### 8.5.3 Iterative Feedback

A domain finding can reveal a missing distinction in Root's criteria. An App
refusal or recovery failure can reveal an inadequate operative path. A changed
physical purpose can require another model or alternative. Iterative feedback
means that these findings can revise each perspective and their relationships.
The four philosophical questions recur across that feedback rather than assigning
one perspective to one thesis or fixing a mandatory sequence.

A successive implementation also needs examination of retained learning. A new
PRD or version number cannot establish that prior defects, useful interfaces and
owner decisions were considered. Root's source accessibility helps that inquiry;
actual receiving-product evidence must establish the result.

## 8.6 Assessment and Remaining Questions

| Claim | Relevant evidence at the basis | Limit or remaining question |
|---|---|---|
| Authorized paths are distinguished | Resolver tests and assignment/policy interpretation | Coverage of each host and actual entry path |
| Dependency meanings are preserved in the examined transformation | Source accounting, graph comparison and independent examination | Missing original declarations and present input suitability |
| Methods can be selected from explicit sources | Resolver operations, resource boundaries and source identities | Delivery, interpretation and adoption by actual consumers |
| Integration can detect failures beyond component checks | Reference/consumer findings and native-use repair | Common assumptions and interactions outside the examinations |
| Human acts can have identified subjects | Product commitments and attributable decisions where captured | Competence, understanding and substantive engagement |
| The arrangement transfers useful means | App and domain-software implementations | Adaptation costs and use by another practitioner |

The basis supports feasibility of specific mechanisms and production paths.
Repository instructions, role files, selected methods, deliverable sources and
the query CLI are in use; the relevant Git and CI paths have been exercised.
[PR #1238](https://github.com/sgttomas/chirality/pull/1238) provides the accepted
manuals describing that working model. Their existence does not imply that the
whole system is fully validated.

Evaluation must include applicable obligations, uncertain premises, negotiable
preferences and control costs separately. Required conditions retain their
standing. Attention, delay, maintenance, false alarms and missed-error consequences
matter in choosing how to meet them. More records or checks need a concrete
contribution to the work; fewer controls need evidence that their functions are
unnecessary or adequately served elsewhere. There is no universal scalar or
mandated process that resolves this assessment.

The most useful further investigations concern connecting paths: whether a fresh
participant finds a governing condition and its supplier; whether a method change
reaches its adopted consumer; whether a reviewer receives the candidate and actual
basis; and whether interruption permits reliable continuation. Their outcomes
must concern usable work, consequential errors and total effort, including owner
attention. These research questions create no product commitments or standing
implementation backlog.

Controlled productivity, comparative error detection, professional suitability,
portability and sustained adoption remain unestablished. The development record's
reported improvements do not isolate causal effects from model capabilities,
accumulated knowledge, work begun earlier or the owner's involvement. Activity
counts cannot supply those missing comparisons.

## 8.7 Summary

Root's evidence supports a revisable environment in which sources, methods,
relationships, authorization and continuing ownership can connect production to
examination and correction. The strength of each finding remains bounded by its
actual subject, source basis and checked path.

App and Piping expose operative and evaluative questions that Root alone cannot
answer. Their findings can revise the common means through iterative feedback.
Accountable human judgment remains situated engagement throughout that relation;
neither implementation traces nor passing checks establish it on the person's behalf.
