# Chapter 7 — Systems Engineering Design Analysis

## 7.1 Introduction and Method

This chapter examines Chirality through eight systems engineering disciplines:
architecture, configuration management, verification and validation, safety and
reliability, requirements engineering, control, formal methods and human factors.
The INCOSE handbook supplies the general disciplinary vocabulary
[CITE:INCOSE2023]. The repository supplies a case, not a demonstration that the
chosen mechanisms follow necessarily from those disciplines or from the four
pillars.

The analysis compares the current operating model described in Chapter 4 with
the earlier instruction architecture. It distinguishes normative commitments,
design hypotheses and observed implementation properties. Current sources include
[AGENTS.md](../../AGENTS.md), the [deliverable CLI](../../tools/deliverables/README.md),
[CI selection](../CI_SELECTION.md) and the active products' definitions. Historical
R-, I- and K-series rules are examined in Appendix A. Their presence in an earlier
catalog establishes that they were specified, not that they were effectively
enforced or necessary.

This distinction changes the earlier analysis substantially. Natural-language
rules are not formal verification. A review checklist is not evidence of complete
review coverage. Several layers of controls do not establish independence of
failure. A mapping from the four pillars to useful SE concerns is an interpretive
design argument, not a causal proof or a unique derivation of an architecture.

## 7.2 Architecture and Structural Design

### 7.2.1 Layered Separation of Concerns

The current arrangement separates three concerns without prescribing one physical
layout for every application:

- **Authority:** what the person has authorized and what remains reserved.
- **Responsibility:** who maintains purpose, produces a contribution and integrates
  the result.
- **Information and execution:** where current meaning is maintained, what tools
  reveal, and what the host actually permits.

Earlier descriptions conflated these concerns by assigning immutable write scopes
to role names and by treating a mandatory agent hierarchy as the source of human
authority. The current repository permits HELP_HUMAN to write within its assignment
and host permissions. Agent 0 can carry work directly. TASK remains a bounded
executor that does not delegate.

The distinction between instructions and product content is also contextual.
Repository instructions can be changed through an authorized Root undertaking;
they are not universally immutable. An application's bundled instructions have
an adopted product basis and must not be silently changed merely because a
repository role file changed.

### 7.2.2 Modularity and Encapsulation

A deliverable folder is a useful unit for maintaining commitments, design and
needs. It need not contain all implementation files or represent an isolated
module. Shared code can serve multiple deliverables, and one contributor can own
a coherent undertaking across several folders.

Modularity is therefore assessed by the change and integration burden, not folder
count alone. A clear local condition may reduce investigation. An artificial
boundary may instead require several synchronized edits. Disjoint concurrent
writes help integration, but do not establish that the contributors' assumptions
are compatible. One participant retains responsibility for the shared result.

### 7.2.3 Interface Contracts

The current development interfaces include the assignment, ScopeOfWork, technical
design, consumer-owned dependency conditions and executable tool contracts. They
have different degrees of machine-checkability. YAML syntax and path containment
are checkable; whether an input meets a condition can require interpretation.

For products, the relevant interfaces are meaningful application operations and
supplier protocols. [App v4's architecture](../../projects/chirality-app-v4/docs/ARCHITECTURE.md)
keeps native supplier capabilities and distinguishes common semantics from a
shared service topology. [SWBPIPE's PRD](../../projects/chirality-piping/docs/PRD.md)
requires model changes to pass through the domain engine. These are concrete
design choices whose implementation and usefulness must be examined separately.

## 7.3 Configuration Management and Baseline Control

### 7.3.1 Version Control as a Development Record

Git identifies committed versions, supports comparison and preserves recoverable
history while those objects remain available. PRs supply change rationale and
verification evidence. Current documents are edited in place rather than copied
into a new run folder after every action.

Git is not a complete execution event store. It does not automatically record
unsaved changes, external inputs, host state or a person's actual engagement. The
earlier assertion that it provides every configuration-management function by
itself overstated the evidence. The relevant question is whether the configuration
needed to reproduce or examine a particular result can be identified and recovered.

### 7.3.2 Identifying the Subject of Acceptance

A commit or content digest can identify the subject of a decision. That can
prevent a reader from confusing an accepted revision with a later one. It does
not establish that the named person made the decision or understood its subject.

An acceptance's meaning also includes its scope and purpose. The historical
SHA-binding contract remains applicable where an adopted product requires it;
this analysis does not amend that contract. For ordinary development, a changed
commit does not itself require renewed owner approval for every unchanged
commitment. The current authority and the consequences of the change determine
what must be examined or decided.

### 7.3.3 Change Impact and Staleness

A dependency query can reveal affected consumers. It cannot conclude that every
consumer is invalid merely because an upstream file changed. An implementation
change may preserve the required interface; a small wording change may alter a
critical condition.

The active model therefore returns relationships and observable facts rather than
propagating a maintained stale flag. Agents investigate relevant effects within
their assignments. Reserved commitment, acceptance or risk changes go to the
owner. This preserves useful impact analysis without making every transitive
edge a compulsory human triage item.

### 7.3.4 Preservation Without Routine Copies

The older architecture required immutable run snapshots and mutable `_LATEST`
pointers. That provided visible history at the cost of copying sources, outputs
and summaries into the working tree. October replaced this general duty with
Git recovery, selected tags and records justified by actual consumers.

Some evidence must still be preserved: a relied-upon analysis basis, a release
package or the outcome needed to recover an interrupted operation. Its retention
requirements follow that use. Neither universal snapshots nor universal deletion
is an adequate policy.

## 7.4 Verification and Validation

### 7.4.1 Decomposition and Integration

The V-model is useful as a reminder to connect requirements with the evidence
needed to examine the integrated result [CITE:INCOSE2023]. It does not require
that all design proceed down a completed hierarchy before implementation begins,
or that every upward integration step become a separate human gate.

A current ScopeOfWork identifies intended results and acceptance criteria.
Implementation, use and review can reveal inadequate assumptions or missing
requirements. Authorized refinements update the relevant design; changes to
reserved commitments require the owner's decision. This feedback makes the
relationship iterative rather than a one-way derivation.

### 7.4.2 Checkpoints by Consequence

The current verification rule is proportionate to consequences. Reversible work
can be inspected. Ordinary implementation receives a focused check. Numerical
meaning, persistence, permissions and destructive operations require targeted
regression checks and independent scrutiny. Releases remain owner acts and need
checks of the actual product.

This is a selection principle, not an exemption from evidence. The repository's
required `harness` result fails when a selected product path fails or fails to
report as required. Passing it still does not establish that every important
behaviour was selected or adequately tested. Selection and the behaviour of the
checks are themselves implementation concerns.

### 7.4.3 Coverage and What It Measures

Coverage needs a stated subject. Lines exercised, requirements linked, dependency
rows migrated and numerical cases checked measure different things. None is a
complete measure of product adequacy.

The dependency migrations provide a bounded example. Accounting for each active
source row and comparing migrated edges against an accepted DAG can detect lost
or altered declarations. Independent examination of representative meanings
adds evidence that the migration preserved conditions. Neither establishes that
the original declarations captured every real dependency.

Checks survive because of the consequential failures they can detect, their
cost, overlap and whether failure would otherwise become visible in time. A
low recent failure rate is not by itself a reason to remove a cheap numerical
oracle. Repeated checks of unchanged applicable inputs are not inherently more
informative because they occur in another session.

### 7.4.4 Traceability for an Actual Question

Useful traceability lets a participant move from a claim or proposed change to
its relevant source, assumptions, consumers and checks. It need not be represented
three times in a ledger, a dependency row and a context mirror.

The current artifact model puts each condition where it is used and derives
reverse links. A source pointer assists inspection; it does not validate the
inference. Where a question cannot be answered from the declarations, the gap is
reported and investigated. The architecture cannot promise complete traceability
merely because every populated field conforms to a schema.

## 7.5 Safety and Reliability Engineering

### 7.5.1 Fault Containment

Host permissions and domain-operation boundaries can reduce the effects of
mistakes. Their assurance concerns the actual execution paths they govern. An
instruction to remain in a folder is different from a path check, and a path check
is different from a sandbox restricting the effects of arbitrary commands.

The [workflow resolver](../../tools/workflow_runtime/resolve_workflow.py)
constructs policy and rejects invalid declarations; it explicitly is not a
sandbox. That distinction prevents a narrow test result from being presented as
a complete containment argument. Safety analysis must consider unsafe interactions
as well as component failures [CITE:Leveson2011].

### 7.5.2 Failure Visibility

An unknown outcome, missing input or contradicted claim must remain distinguishable
from success. Visibility depends on detecting and reporting the condition; it is
not guaranteed by an instruction to expose uncertainty. Product operations also
need to distinguish refusal, non-execution, successful application and lost
acknowledgement when those distinctions affect recovery.

A failure can be harmless in one context and consequential in another. A missing
optional reference can permit a partial query. A missing numerical input may
require refusal. The response follows the condition's meaning, not a universal
rule that every unknown either blocks everything or can be ignored.

### 7.5.3 Context Boundaries

The earlier sealed-context model sought to make inputs explicit before delegated
execution. Its useful concern was the basis of a result. A closed brief does not,
however, remove learned model priors or establish that the agent used only
intended information. Claims of complete context isolation require an execution
mechanism and evidence beyond a metadata presence check.

The current repository supplies the full assignment in the dispatch, keeps
instructions in repository sources, and retrieves additional material according
to the task. Privacy and access limits remain enforceable host or product
boundaries. Task context can evolve through relevant discoveries without a new
routine sealing ceremony.

## 7.6 Requirements Engineering

### 7.6.1 Decomposition and Allocation

Decomposition makes a large intention workable by identifying results, boundaries
and connections. It is an interpretation of source requirements, not proof that
the source was exhaustive or that every resulting partition is natural.

Stable identifiers and a predictable folder layout help agents locate the work.
Acceptance criteria belong to the current commitment; code paths identify
relevant implementation. Neither a flat layout nor a one-to-one allocation rule
is a universal requirement for every domain.

### 7.6.2 Traceability Views

A requirements-to-deliverables view can be generated when an actual review needs
it. Its value is answering whether a commitment has an implementation and a
suitable examination basis. A maintained matrix is justified when its consumer
requires it; otherwise direct references and queries can provide the same useful
navigation with fewer synchronization duties.

Missing mappings remain visible. Tool output should not turn a partial mapping
into an apparent completeness claim.

### 7.6.3 Acceptance Criteria and Re-Derivation

A PRD does not compile deterministically into an application. It leaves design
choices that must be informed by the owner, supplier capabilities, prior defects
and actual use. App v4 illustrates this: it preserves purposes and selected useful
behaviours while revising the former Runtime topology and integration approach.

A new implementation should be assessed for retained learning as well as speed.
If it repeatedly loses valuable behaviour or rediscovers earlier failures, its
PRD-led derivation has not preserved enough of the undertaking's knowledge.
Changes to criteria remain attributable owner decisions; implementation evidence
can motivate those decisions without making them automatically.

## 7.7 Control and Feedback

### 7.7.1 The Working Loop

A feedback interpretation remains useful: establish an objective, act, inspect
the result, compare it with what is needed and correct. The actor need not change
at each step. Sustained ownership keeps an agent with the ordinary repairs and
integration that make its contribution usable.

This is an analogy to control, not a demonstrated control-theoretic model with
proven convergence. The objectives, available information and even the relevant
state description can change as work reveals new conditions.

### 7.7.2 Observables and Objectives

Useful observations include whether an operation applied, which check ran, what
an input contains and which consumers declare a need. “All deliverables say
ISSUED” is no longer an objective or a measurement in the active model. Nor would
it have established usefulness or adequacy in the earlier one.

A completed undertaking needs evidence tied to its actual purpose. The owner
must be able to understand what was achieved, what remains uncertain and what
reliance is being proposed. A dashboard can assist that understanding but cannot
replace it.

### 7.7.3 Feedback Across Contributors and Sessions

A contributor can continue independent work while a related branch is unresolved.
Coordination becomes necessary where results affect shared assumptions, interfaces
or writes. The host's completion mechanism delivers returns; the integrating
participant examines them and resolves their relationship to the whole.

Conversation and current artifacts support continuity. Recovery is a practical
property to test after an interruption, not a guarantee supplied by a handoff
file. A replacement participant may need to re-establish context even when the
preserved facts are accurate.

### 7.7.4 Authority and Stopping

Human authority does not imply a required confirmation at every control cycle.
Standing authorization permits ordinary work to continue. An explicit hold or
reserved choice stops the affected action. Completion of the agreed result is
also a stopping condition; agents should not invent records to prolong closeout.

Judgment remains the person's situated, committed engagement throughout the work.
The agent's planning, evaluation and adaptive action are reckoning within the
assigned authority. A stronger capacity for reckoning can change suitable
supervision without itself transferring judgment.

## 7.8 Specification and Formal Methods

### 7.8.1 Historical Invariant Families

The R-, I- and K-series catalogs named important concerns but combined distinct
kinds of claim. Some rules expressed values, others prescribed files or phases,
and others asserted properties of tools. Calling each an invariant did not give
it a mathematical semantics or an enforcement mechanism.

Appendix A preserves the historical families as an analytical comparison. Adopted
product contracts still apply through their current sources. Retired workflow
duties do not become current again because the thesis discusses their IDs.

### 7.8.2 Preconditions and Postconditions

Executable tools can check explicit preconditions and report well-defined
outcomes. The deliverable checker, for example, distinguishes malformed metadata
from well-formed unresolved relationships. A successful structural check therefore
has a narrower meaning than “all needs are met.”

Agent assignments can state expected results and conditions, but stochastic
execution does not acquire guaranteed postconditions from prose. The resulting
work must be inspected or tested as appropriate. A formal proof claim would need
a specified model, assumptions and an actual proof, not a table of intended
behaviours.

### 7.8.3 Types and Interpretive Limits

Types reduce ambiguity at particular interfaces. The active YAML schema rejects
invalid identities and malformed fields while preserving unresolved suppliers.
Legacy formats can remain documented for adopted consumers without defining
current development behaviour.

The older labels `FACT`, `ASSUMPTION`, `PROPOSAL` and `TBD` are useful distinctions
in some reviews; they are not an exhaustive, mutually exclusive ontology of every
claim. A proposal can contain supported facts and untested assumptions. Checking
a label's spelling cannot establish the appropriateness of its classification.

The exact legacy `FindingSeverity` enum remains in the standalone
[SE companion, §7.3](SE_Design_Analysis.md#73-the-type-system) because the
compatibility-format reference still cites it. Retaining that interface does not
reinstate the older review gates.

### 7.8.4 State Machines Where They Fit

State machines remain useful for product behaviour such as requests, process
ownership or persistence operations when they describe actual transitions and
failure outcomes. Retirement of `_STATUS.md` is not an argument against state
machines in software.

It is an argument against treating one administrative lifecycle as an adequate
model of every deliverable's condition, claims and human acceptance. The proper
scope of a state machine follows the behaviour being controlled.

## 7.9 Human Factors and Decision Authority

### 7.9.1 Responsibility Allocation

The person retains judgment and reserved commitments. Agent 0 maintains purpose
and continuity in the interaction; managers and executors are opportunities for
useful contributions. TASK's non-delegation rule provides a particular boundary
once that role is selected. None of this requires the owner to personally repeat
every implementation decision or review every reversible edit.

An agent can help frame an ambiguous choice, but the framing is itself an object
of examination. A choice reduced to two options is not necessarily easier to
judge well if it conceals relevant alternatives or assumptions.

### 7.9.2 Cognitive Load and Attention

A clear source, concise return or explicit uncertainty can reduce investigation.
Repeated registers, notices and status mirrors can increase it. Labels do not
eliminate the need to examine claim reliability, and an immutable record can
still be wrong or distracting.

The reset treats attention as a scarce part of professional work. Information
should be sufficient to review, use or recover the result, with detail accessible
when needed. The value of this arrangement must be assessed in actual use,
including by someone other than its author.

### 7.9.3 Proportionate Rigor

Rigor concerns the adequacy of an examination for its consequences, not the
number of forms or test runs. Numerical meaning warrants stronger evidence than
a reversible wording change. A routine change can become consequential when it
alters executable configuration or an embedded source.

The cost of a control is part of its evaluation: execution time, maintenance,
attention, false alarms and lost opportunities to perform substantive work.
Removing a control is justified when its useful function is unnecessary or
adequately served elsewhere, not merely because it is inconvenient.

## 7.10 Cross-Cutting Patterns

### 7.10.1 Tree, Graph, Network and Attention

Composition, dependency and relevance are distinct views of the work. Attention
selects and relates them in a particular inquiry. A schema can support these
activities without exhaustively representing the world or a person's knowledge.
The graph can reveal opportunities for parallel work while leaving shared-write,
resource and interpretation questions unresolved.

### 7.10.2 Local Meaning and Derived Views

Consumer-owned needs let an agent examine a relevant neighbourhood without a
global state census. A generated answer avoids maintaining a second authored
graph, but its freshness is only relative to the declarations it read. Stale or
incomplete declarations still yield stale or incomplete answers.

The maintenance responsibility is therefore to update current meaning when it
changes, leaving unchanged declarations alone. No storage arrangement eliminates
that responsibility.

### 7.10.3 Evidence and Its Limitations

Sources, checks and independent examination make grounds inspectable. They do
not guarantee that every unsupported claim is discoverable or that a cited source
warrants the conclusion. Shared errors in models, fixtures and expectations can
survive several apparent layers of verification.

SWBPIPE makes this limitation concrete: a result can pass software validation
without becoming professional engineering approval. App workflow recovery
similarly cannot be inferred solely from a recovered conversation. Each claim
requires evidence about its own subject.

### 7.10.4 Complementary Controls

Controls are complementary when they address distinct failure modes or provide
independent evidence. Duplicating the same assumption in instructions, a schema
and a test may create repetition without independence. The assurance argument
must identify what each control checks and what remains outside it.

The architecture thus supports a bounded argument about failures, not a blanket
claim that no single failure can compromise system integrity.

## 7.11 Assessment

### 7.11.1 What SE Contributes

The disciplines provide useful ways to ask whether boundaries are clear,
configurations identifiable, interfaces coherent, evidence appropriate, failures
recoverable and human attention well directed. They are resources for design and
criticism. Their value is not established by implementing a named artifact for
each discipline.

### 7.11.2 A Revisable Relationship to the Four Pillars

| Pillar | SE questions it motivates | What remains contingent |
|---|---|---|
| Ontology | Which objects, identities and relationships need to be distinguished? | Folder layout, schemas and storage topology |
| Epistemology | What supports a claim and how can its limits be examined? | Checks, source bindings and evidence formats |
| Praxeology | How do contributions become a usable result through action and correction? | Staffing, workflow stages and coordination mechanisms |
| Axiology | Whose purposes and responsibilities matter, and what costs are acceptable? | Decision interfaces and proportionate controls |

These questions constrain one another. A recovery failure can reveal a missing
outcome distinction. A new risk can change the examination needed. Excessive
procedure can consume the attention that sound judgment requires. The framework
is coherent through such correction, not through permanent commitment to one
architecture.

### 7.11.3 Bounded Conclusion

October removed lifecycle status, routine record duties, compulsory authored work
graphs and much associated enforcement while retaining current commitments,
reserved decisions and consequence-based verification. This is evidence that the
older mechanism set was not necessary to express those commitments. The repository
changes do not by themselves prove improved safety, a precise productivity gain
or economical transfer to another domain.

Those questions require use, failure analysis and recovery evidence over time.
The defensible design claim is that Chirality supplies an inspectable, revisable
arrangement for capable agent reckoning within human purposes and authority.
Systems engineering helps examine that arrangement; it does not certify the
quality of human judgment or settle the philosophical capacities of all future
machines.
