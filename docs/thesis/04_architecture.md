# Chapter 4 — Architecture

## 4.1 Overview

Chirality's architecture is a set of revisable responses to the four questions
established in Chapter 3: what the work concerns, what supports its claims, how
it becomes usable, and what matters in its conduct and consequences. Those
questions motivate design choices; they do not uniquely determine a filesystem,
role hierarchy, approval protocol or execution topology.

This chapter describes the repository's operating architecture after the October
2026 reset and distinguishes it from the earlier architecture. The comparison
matters because the earlier thesis treated several subsequently retired
mechanisms as necessary conditions of accountability. Their removal while the
accountability commitments remain is evidence against that necessity claim. It
is not proof that the replacement is universally better.

The current source basis is [AGENTS.md](../../AGENTS.md), the
[deliverable-query contract](../../tools/deliverables/README.md), the four
[role files](../../agents/), and the active products' adopted definitions.
These are different kinds of source: instructions state expected conduct, tool
contracts describe bounded behaviour, and product requirements describe intended
capabilities. This chapter does not turn a requirement into evidence that its
implementation has been qualified. The historical invariant families are
examined in [Appendix A](appendix_a_invariant_catalog.md); that appendix is not a
second source of repository instructions.

## 4.2 The Foundational Decision: Current Artifacts and Derived Views

### 4.2.1 The Graph Model

Active project work is organized around deliverable folders. A deliverable's
`ScopeOfWork.md` holds commitments and acceptance criteria. `Design/` holds useful
technical detail. `deliverable.yaml` identifies the deliverable and states its
needs, with optional code paths and check references. A consumer declares what
it needs from a supplier; tools derive reverse links and graph views.

The graph is a representation of declared relationships, not the undertaking
itself. A need can name a deliverable, an external supplier, a document, a
package or an unresolved target. A condition may require interpretation that no
schema check can perform. Cycles can represent mutual interface development or
other legitimate relationships; their presence alone does not establish an
impossible execution order. Selected planning baselines can be DAGs without
requiring every useful relationship to be a DAG edge.

The current query interface provides `neighborhood`, `impact`, `touches`,
`dag-diff` and `check`. Results identify their observed basis and expose unknowns.
They do not mark a deliverable complete or infer acceptance from a merge. The
consumer declarations remain the sources; no generated progress register is
committed as a competing representation.

### 4.2.2 Why the Artifact Choice Matters

Plain, versioned artifacts support direct inspection, meaningful diffs, stable
references and recovery of committed versions. They also let agents use ordinary
file and Git tools instead of relying on a separate coordination service. Keeping
the current meaning in the deliverable reduces the number of places that must
be reconciled after a decision.

These are advantages of the chosen arrangement, not exclusive properties of
files. A database-backed application can also preserve provenance, versions and
attributable decisions. Conversely, a Git repository can contain misleading
claims, incomplete history or inconsistent declarations. A commit identifies
recorded content; it does not establish its correctness, the completeness of the
record or the authenticity of every represented human act.

The earlier formulation, “if it is not in a versioned file, it does not exist for
purposes of reliance,” was too broad. Purpose and authorization can arise in the
conversation. Applications have operational state. Domain engines maintain
models and results in their own stores. What matters is that the grounds needed
for a particular use are accessible and sufficiently identified. The current
artifact policy is one practical way to serve that requirement for development.

### 4.2.3 Scope and Limits of the Filesystem Commitment

Repository commitments, designs and dependency declarations live in files.
Execution services may hold process state, requests, credentials under their
custodian, caches and recoverable session data. Domain applications own their
canonical models and numerical results. These stores have different purposes;
the existence of one does not authorize it to override another.

Derived indexes and caches can improve access when their basis and invalidation
behaviour are understood. There is no philosophical requirement to forbid them.
The design concern is whether a reader can identify what a result is based on,
where current meaning is maintained and how divergence is resolved.

Git preserves committed history. It does not automatically preserve unsaved
work, external services or every input to an analysis. Recovery requirements must
therefore be stated for the operation in question rather than assumed from the
presence of a repository.

## 4.3 Entity Model and Domain Ontology

### 4.3.1 Project Hierarchy

The active repository convention is:

```text
projects/<project>/execution/
└── PKG-nn/
    └── DEL-nn-nn/
        ├── ScopeOfWork.md
        ├── Design/             # where useful
        └── deliverable.yaml
```

Packages group deliverables. The flat layout makes navigation predictable; it
is not a claim that every domain has a naturally flat ontology. An intended
work product is distinct from the folder used to manage it. Source code can live
elsewhere, and several deliverables can be relevant to the same code.

The earlier `1_Working`, `2_Checking` and `3_Issued` arrangement coupled file
location to production status. Removing those locations changes the repository
representation, not the distinction between development, examination and
acceptance.

### 4.3.2 Stable Identifiers

Package and deliverable identifiers provide references that survive ordinary
text changes and help tools join declarations. In the active layout they follow
`PKG-nn` and `DEL-nn-nn`. A stable identifier does not establish that a deliverable's
meaning is unchanged: a scope revision can preserve identity while altering a
commitment, and that alteration still requires the appropriate authority.

Code-path mappings express relevance, not exclusive ownership or fulfilment.
An unmapped path produces a partial answer. It is not evidence that the change
has no consumers, nor a reason to initiate a repository-wide metadata exercise.

### 4.3.3 Deliverable Content and Its Home

The three current artifact types divide responsibility without claiming that
all useful content fits a closed schema:

| Artifact | Purpose | What it does not establish |
|---|---|---|
| `ScopeOfWork.md` | Intended result, commitments and acceptance criteria | That the result exists or is accepted |
| `Design/` | Technical reasoning, constraints and relevant sources | That every assumption has been demonstrated |
| `deliverable.yaml` | Needs, conditions and useful code/check pointers | Completion, suitability or an execution schedule |

A decision changes the text it governs. The PR describes the change, its reason,
checks and unresolved matters; Git retains the earlier text. Sources and
references remain where they help the work rather than in compulsory mirror
files. A record is justified by a concrete consumer, acceptance requirement or
recovery need.

### 4.3.4 Structural and Dependency Views

The package tree supports composition and navigation. The dependency graph
supports investigation of inputs and consumers. Neither view alone determines
what can safely proceed. The tool can reveal that two deliverables have no
recorded dependency, while their implementations still share a file, a memory
budget or an unresolved interface.

`impact` follows declared downstream relationships, including non-gating ones.
It identifies candidates for examination, not an automatic list of invalidated
work. `dag-diff` compares declarations against an identified baseline; it does
not accept the new graph. Ordinary authorized dependency updates need no new
acceptance ceremony unless they change a reserved commitment or baseline.

### 4.3.5 The Four Structures

The tree, graph, relationship network and attention discussed in Chapter 3 are
complementary perspectives:

- **Tree:** what the undertaking is composed of at a useful level of detail.
- **Dependency graph:** which contributions need which inputs and conditions.
- **Relationship network:** sources, decisions, shared concepts and other links
  relevant to interpretation, including those outside execution order.
- **Attention:** the activity through which a participant selects, relates and
  synthesizes what matters for the question in hand.

Attention is not another mandatory stored graph. Nor must every relationship
be extracted into metadata before work can proceed. A machine-readable link is
useful when a real query needs it; otherwise a clear reference in the relevant
design may suffice. These views assist reckoning and human judgment without
exhausting situated understanding.

## 4.4 Work, Evidence and Acceptance

### 4.4.1 The Earlier Six-State Model

The earlier implementation used `OPEN`, `INITIALIZED`, `SEMANTIC_READY`,
`IN_PROGRESS`, `CHECKING` and `ISSUED`. Its labels combined evidence that files
had been created, progress descriptions and human decisions. `_STATUS.md` was
intended to be their canonical indicator.

That state machine is no longer the active development model. Its historical
value was making some distinctions explicit. Its cost was maintaining a second
description of work that could diverge from the artifacts and could imply more
than a label supported.

### 4.4.2 Actions and Authority

The current operating model separates ordinary action from reserved decisions.
Agents can investigate, implement, examine, repair and integrate within the
owner's authorization and the host's permissions. Changes to commitments or
acceptance criteria, releases, risk acceptance and explicit holds remain owner
matters. The repository's standing Git grant permits authorized integration
under its verification conditions; a merge is not acceptance for professional
reliance.

Human judgment is situated, committed engagement throughout the undertaking.
It shapes purpose, distinctions, evidence and what the person will stand behind.
An acceptance is one expression of that engagement, not its entire content.
Neither a lifecycle transition nor a record can perform judgment for the person.

### 4.4.3 Stage Gates and Useful Checkpoints

A project can require an accepted baseline, a release decision or another
consequential checkpoint. Its purpose, subject and authority must be clear.
Those needs do not justify a human gate at every internal agent handoff or
ordinary implementation step.

The current architecture therefore permits project-specific checkpoints while
rejecting a universal development lifecycle. A tool may enforce objective
preconditions for an operation; passing them is evidence about those conditions,
not permission to claim professional approval.

### 4.4.4 Observable Facts Instead of Stored Progress

The question “what can proceed here?” draws on current conditions, available
inputs, relevant checks, in-flight changes and resource constraints. It is not
answered by a single stored status. A file's presence may establish availability
but say nothing about whether it contains the required interface. A passing
check establishes only the behaviour it exercises under its tested conditions.

Agents assess suitability using these facts and report uncertainty when it
matters. This assessment is part of their reckoning; it does not transfer the
person's accountable judgment to the query tool or agent.

### 4.4.5 Warrant and Revision

The earlier sequence `UNWARRANTED → CITED → REVIEWED → AUTHENTICATED` remains
useful as a historical account of concerns, but it is inadequate as a universal
progression of knowledge. A citation can be irrelevant; a reviewed claim can
later be contradicted; an authenticated result can be wrong. Several claims in
one artifact can have different grounds and limits.

The operative questions are what supports the claim, whether that support is
appropriate here, what remains uncertain, and who accepts which reliance.
Chapter 5 develops these questions. They require inspectable grounds, not a
second obligatory lifecycle register.

## 4.5 Roles and Responsibility

### 4.5.1 Structural Overview

The current role definitions offer four contributions:

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Purpose, alignment and continuity with the owner |
| HELPS_HUMANS | 1 | Make intent concrete through design |
| WORKING_ITEMS | 1 | Own implementation, contributors and integration |
| TASK | 2 | Carry one bounded assignment through ordinary repairs; no delegation |

The agent working with the person holds Agent 0's continuity responsibilities,
whatever role it entered through. A session can perform substantial work without
delegation. Managers and contributors are engaged when their contribution helps;
the types do not constitute a required staffing chart.

### 4.5.2 Authority Properties

A role describes responsibility. The assignment and host determine available
tools and write scope. HELP_HUMAN is not intrinsically read-only. TASK's
no-delegation rule remains a deliberate role boundary; a TASK can report an
opportunity to divide work to its caller without creating another hierarchy.

No role grants a right to override an explicit hold or make an owner-reserved
decision. Conversely, ordinary refinement of design within authorized work is
not automatically a reason to escalate. Relevant escalation concerns commitments,
consequential shared assumptions, interfaces outside the assignment or a reserved
choice.

### 4.5.3 Classification and Capability

Type numbers identify responsibilities, not model assignments or levels of
intelligence. Skills and workflows are methods selected for the work. A host's
ability to spawn agents does not itself authorize TASK to delegate, and a
permissive role description cannot expand a read-only host.

The repository resolver represents this distinction in policy construction. Its
[implementation](../../tools/workflow_runtime/resolve_workflow.py) explicitly
states that it reports policy rather than acting as a sandbox. A host must
actually enforce the relevant permissions. App v4's product settings have their
own adopted basis; repository role changes do not silently amend them.

## 4.6 Write Scope and Containment

### 4.6.1 Assignment-Specific Scope

A writing assignment needs a usable boundary: the intended changes, affected
objects and prohibited areas. The required precision depends on the operation.
A code change may span source, tests and a design note; it need not fit one
folder merely because the older role catalog assigned folder-based categories.

Missing authorization does not imply unrestricted writes. Explicit read-only
conditions remain effective. Where a tool accepts paths, normalized containment
and symlink handling are concrete implementation concerns, separate from the
agent's willingness to follow instructions.

### 4.6.2 Shared Work and Protected Objects

Concurrent contributors should have disjoint writes, or one owner must integrate
shared changes. A read-only review can overlap production when its basis remains
clear. Independence in the dependency graph is an opportunity to investigate
concurrency, not proof that shared writes or resources are absent.

Domain applications add stronger object-level restrictions. The adopted
[product boundaries](../PRODUCT_BOUNDARIES.md) reserve protected domain changes
to the declared engine-controlled path. The engine owns canonical model state;
this is a storage and operation authority, not a guarantee of engineering truth.
Applicable proposal, validation and human-acceptance requirements remain product
contracts. Removing repository record duties does not remove those contracts.

### 4.6.3 What Can Be Enforced

| Mechanism | Bounded contribution | Limit |
|---|---|---|
| Assignment and instructions | State objective, scope and prohibited actions | Following prose is not guaranteed |
| Resolver and schema validation | Reject malformed declarations and some escaping paths | Do not inspect every real effect of an arbitrary command |
| Host permissions | Restrict actions on the enforced execution path | Depend on implementation and coverage of alternative paths |
| Domain operation validation | Check specified model constraints before application | Does not establish all physical or professional adequacy |
| Review and targeted checks | Detect selected errors and assess evidence | Can share assumptions or miss unexamined failures |

This allocation is more precise than saying that instructions themselves create
fault containment. A claimed enforced property needs an identified mechanism,
its coverage and appropriate evidence.

### 4.6.4 Fault Containment and Its Costs

Containment can limit the consequences of an error, but path separation alone
does not isolate shared assumptions, resource exhaustion or misleading outputs.
Worktrees reduce some write conflicts; they do not make integration automatic.
Additional layers can also create stale permissions, waiting and duplicated
state. Their value must be assessed against the failures they address and the
burden they impose.

## 4.7 Commitments, Design Hypotheses and Evidence

### 4.7.1 Three Kinds of Claim

The earlier R-, I- and K-series catalogs mixed values, representations,
procedures and enforcement claims. The revised analysis distinguishes:

1. **Normative commitments:** what responsibility and values the undertaking
   chooses to preserve, such as attributable human acceptance.
2. **Design hypotheses:** how an arrangement is expected to serve those
   commitments, such as identifying the exact subject of an acceptance.
3. **Observed outcomes:** what inspection, tests or use establish about a
   particular implementation and basis.

An acceptance commitment does not prove that a SHA-binding mechanism is sufficient
for it. A successful test of that mechanism does not establish that the person
understood the subject. Appendix A retains the historical identifiers for
comparison and points to adopted product contracts where they still apply.

### 4.7.2 Assurance and the Limits of Layering

Instructions, deterministic checks, host enforcement and human examination can
complement one another. They can also share the same mistaken premise. Merely
counting layers provides no assurance that one failure cannot compromise the
result.

Verification is selected by consequence and detectability. Routine reversible
changes can be inspected; ordinary implementation receives a focused check;
numerical meaning, persistence, permissions and destructive operations warrant
targeted regression checks and independent scrutiny. The repository's required
`harness` result aggregates the checks selected for the candidate. Passing CI
is bounded evidence for integration, not a certificate of product correctness.

The cost of control belongs in this assessment. Repeated records and checks can
consume the attention needed for substantive examination. Conversely, a cheap
numerical oracle that consistently passes can remain valuable because it detects
a consequential failure that would otherwise remain silent.

## 4.8 Coordination and Continuing Ownership

### 4.8.1 Contributions Rather Than a Spawning Chart

The [coordinated-knowledge-work workflow](../../workflows/coordinated-knowledge-work/WORKFLOW.md)
organizes purpose, integration, production and independent examination. An agent
can carry several responsibilities when the work permits. Separate contributors
are useful for parallel lines, different expertise or independent scrutiny;
creating the largest possible agent tree is not itself an outcome.

Independent work need not wait behind an unresolved branch. Shared writes,
resource limits, review capacity and integration costs can still justify
sequencing. These are properties of the undertaking, not universal serial or
parallel defaults.

### 4.8.2 Continuity and Recovery

Continuity comes primarily from current artifacts, the conversation, tool queries
and the existing change history. A replaceable recovery note is useful when
those sources do not suffice across an interruption. It is not a routine second
work graph or a record of every action.

A resumed participant does not acquire the earlier participant's whole situated
understanding by reading a file. Recovery must be tested against an actual task:
can the participant identify the current objective, basis, unresolved matters and
next authorized action without repeating or losing consequential work?

### 4.8.3 The Working Cycle

The current repository cycle is to establish the objective and authorization,
locate affected artifacts, query inputs and consumers, perform and examine the
work, update current meaning where necessary, and return the usable result.
Ownership continues through ordinary repairs and integration. The agent stops
when the agreed result is established rather than inventing administrative
closeout.

The cycle can proceed under standing authority. It does not require a human
confirmation at each iteration. An unresolved owner-reserved decision pauses the
affected action, while independent authorized work can continue.

### 4.8.4 App Exemplar and Domain Application

App v4 develops the human-agent relationship through workflow authoring, trial,
conversation, requests and recovery. Its [PRD](../../projects/chirality-app-v4/docs/PRD.md)
and [architecture](../../projects/chirality-app-v4/docs/ARCHITECTURE.md) preserve
useful native supplier capabilities while rejecting the former Runtime service
as its required topology. Shared semantics do not imply a universal shared
service. App v3, Runtime and PEC are frozen; their recovery is described in
[projects/FROZEN.md](../../projects/FROZEN.md).

SWBPIPE supplies a demanding domain realization. Its [PRD](../../projects/chirality-piping/docs/PRD.md)
distinguishes physical models, analytical models, analysis results, comparisons
and downstream handoff. Human and agent requests are intended to use meaningful
operations through common validation and application. The numerical engine must
be examined on its own terms; it cannot inherit adequacy from the agent framework.

Re-deriving an application from a current PRD is an interpretive design activity,
not deterministic compilation. Requirements, retained lessons, native-use
findings and implementation evidence inform what is reused and what is replaced.
The value of repeated derivation depends on preserving learning and useful
behaviour, not merely producing a new codebase quickly.

## 4.9 Assignment and Result Interfaces

### 4.9.1 The Assignment

An assignment can be the conversation. It needs sufficient purpose, context,
boundaries and expected result for its recipient to act. Reusable tools may need
strict schemas; that does not make every agent brief a fixed parameter table.
The current repository requires a dispatched brief to be given in full in the
dispatch and to refer to repository sources, avoiding hidden instruction sets in
scratch space or host-side persona files.

Identical inputs do not guarantee equivalent model outputs. Repeatability claims
must identify the actual execution and assessment conditions. Missing information
is handled according to its significance: report a real blocker, investigate a
resolvable uncertainty, and continue unaffected work.

### 4.9.2 The Result

A return gives the result location, checks, material findings and unresolved
choices. Contributors inspect returns through the host's actual completion
mechanism. A separate return file, receipt or tool-root snapshot is not a general
requirement.

Some outputs need durable records: an accepted artifact, numerical evidence,
recoverable operation outcome or release package. Their form follows the
consumer's need. Machine-generated execution history can be useful for debugging
and recovery without requiring agents to duplicate it in authored summaries.

### 4.9.3 Historical Preservation and Current Meaning

Current documents are edited in place when their meaning changes. Git preserves
committed versions, while selected tags identify baselines and recovery points.
A tag that records an owner decision must accurately identify that decision; its
creation is not the decision itself.

The earlier immutable snapshot convention preserved many copies in the working
tree. The reset retained historical recovery while removing routine copies and
the obligations that produced them. This is a change in preservation mechanism,
not permission to erase evidence required for a specific reliance or recovery.

## 4.10 Summary

The current architecture makes relevant objects and relationships accessible,
claims and limits inspectable, action and correction practicable, and reserved
commitments attributable. Files, queries, roles, permissions and review are
particular means toward those ends. They are not jointly sufficient to guarantee
truth, professional adequacy or accountable human engagement.

Agents can exercise extensive reckoning: investigate, infer, compare, propose,
check and act within authority. Human judgment remains situated and committed
engagement with what matters and what the person will stand behind. Greater agent
capability can alter the appropriate delegation and verification arrangements
without itself transferring that judgment. This account does not require a claim
that every possible future machine must lack it.

October's transformation is therefore an architectural result worth examining:
some mechanisms formerly presented as necessary were removed while the guiding
commitments remained. Whether the replacement improves throughput, recovery and
quality over sustained development remains an empirical question.
