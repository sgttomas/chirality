# Systems Engineering Design Analysis — Agent Instruction Architecture

This standalone companion summarizes [Chapter 7](07_se_design_analysis.md).
The detailed analysis lives there so that the thesis does not maintain two full
accounts of the same architecture. Section numbers are retained for existing
references, including the `FindingSeverity` compatibility reference in §7.3.

The current operating basis is [AGENTS.md](../../AGENTS.md), current project
commitments and executable tool contracts. This document is explanatory. It
neither reinstates the retired R-, I- and K-series development procedures nor
amends adopted product contracts. [Appendix A](appendix_a_invariant_catalog.md)
provides the historical comparison.

## 1. Architecture & Structural Design

### 1.1 Layered Separation of Concerns

Authority, responsibility and execution capability are different. The owner
sets purpose and reserved decisions; roles describe contributions; assignments
and hosts establish permitted effects. Instructions request behaviour, while
particular tool and host mechanisms can enforce narrower properties.

### 1.2 Modularity & Encapsulation

Active deliverables maintain ScopeOfWork, useful Design content and dependency
conditions. They are units of meaning and work, not necessarily isolated code
modules. Shared code and cross-deliverable undertakings require explicit
integration responsibility rather than compulsory folder-bound staffing.

### 1.3 Interface Contracts

Assignments, dependency conditions, tool schemas and product operations are
interfaces with different semantics. Syntactic validity does not establish that
an input is suitable. A strict tool schema is useful without making every agent
assignment a sealed parameter table.

## 2. Configuration Management & Baseline Control

### 2.1 Version Control as a Development Record

Git preserves committed versions and supports comparison and recovery. PRs
explain changes and their examination. Neither is a complete event record of
external services, unsaved work or human engagement.

### 2.2 Identifying the Subject of Acceptance

A revision or digest identifies content. It does not establish truth or a human
act. Applicable product contracts can require specific bindings; ordinary
development follows its current authority rather than inheriting a universal
reapproval duty from every new commit.

### 2.3 Change Impact

Derived dependency views identify potentially affected consumers. They do not
mark every consumer stale or establish that a missing edge means independence.
Meaningful changes are investigated; reserved decisions remain with the owner.

### 2.4 Preservation

Current meaning is edited in place. Committed history and selected tags preserve
earlier versions. Extra records are warranted by a concrete consumer, acceptance
requirement or recovery need; immutable run snapshots are not a general duty.

## 3. Verification & Validation

### 3.1 Decomposition and Integration

The V-model supplies useful questions about the relation between requirements
and examination of the result. It does not uniquely prescribe stages, documents
or separate agents. Implementation and use can expose requirements that need
revision through the appropriate authority.

### 3.2 Consequential Checkpoints

Routine reversible work can be inspected, ordinary implementation receives a
focused check, and consequential numerical, persistence, permission or destructive
changes warrant targeted regression checks and independent scrutiny. Passing a
selected check does not constitute professional acceptance.

### 3.3 Coverage Analysis

Coverage measures need a subject. Migration-row accounting, code exercised and
numerical cases establish different bounded facts. None establishes the complete
adequacy of the product or its requirements.

### 3.4 Traceability

Traceability is useful when it connects a real question to sources, assumptions,
consumers and checks. Repeating those relationships in multiple registers can
create inconsistent answers without adding useful evidence.

## 4. Safety & Reliability Engineering

### 4.1 Fault Containment

Host permissions and domain-controlled operations can restrict actual effects.
A role label or natural-language instruction alone is not a sandbox. Containment
claims must identify the path enforced and possible paths outside it.

### 4.2 Failure Visibility

Unknown outcomes, refusals and unexecuted work must remain distinguishable from
success where recovery or reliance depends on that distinction. Visibility is
an implementation property to examine, not a consequence of naming an invariant.

### 4.3 Context Boundaries

A clear assignment and identified sources help establish the basis of a result.
They cannot erase model priors or guarantee that a sealed brief captures every
relevant condition. Privacy and access limits belong in actual host and product
boundaries.

## 5. Requirements Engineering

### 5.1 Decomposition & Allocation

Decomposition interprets intention into workable results and relationships. Its
completeness cannot be proven merely from a flat folder layout or a populated
allocation table.

### 5.2 Requirements Traceability Views

Generate the view needed by the actual consumer. Current ScopeOfWork, Design and
consumer-owned needs provide the primary development sources; missing mappings
remain explicit rather than being counted as absence of impact.

### 5.3 Acceptance Criteria Allocation

The PRD and acceptance criteria constrain development, but do not compile into a
unique implementation. Re-derivation incorporates prior defects, use and owner
interpretation. Its value depends on retaining learning as well as producing code.

## 6. Control and Feedback

### 6.1 The Working Loop

Purpose, action, examination, correction and integration can remain with one
agent or involve contributors. Ownership continues through ordinary repairs.
This is a useful feedback description, not a proof of convergence.

### 6.2 Feedback Across Contributions

Independent work can proceed while another branch is unresolved. Shared writes,
resource limits and integration costs may justify sequencing. Recovery from an
interruption must be assessed through an actual continuation attempt.

### 6.3 Authority and Stopping

Standing authority permits ordinary progress; a reserved decision stops the
affected action. Human judgment shapes the undertaking throughout. Completion of
the agreed result stops work without a compulsory closeout packet.

## 7. Specification and Formal Methods

### 7.1 Invariant Systems

Historical invariant catalogs combined values, procedures and tool properties.
Naming a rule did not mathematically formalize it or establish its enforcement.
Current adopted contracts must be consulted in their current homes.

### 7.2 Preconditions and Postconditions

Executable checks can enforce explicit input conditions and produce bounded
results. Prose assignments do not guarantee stochastic agent postconditions.
Formal proof would require a model, assumptions and a proof of the stated property.

### 7.3 The Type System

Types can make interface distinctions checkable while leaving semantic adequacy
open. The following **legacy review-format vocabulary** is retained exactly
because [Compatibility formats §10.6](../COMPATIBILITY_FORMATS.md#106-review-finding-severity)
cites this section:

```text
FindingSeverity : CRITICAL | MAJOR | MINOR | OBSERVATION
```

These values classify review findings about deliverable content for consumers of
that format. They are distinct from historical governance-verifier severities
(`BLOCK`, `REVIEW`, `WARN`, `INFO`, `NOT_APPLICABLE`) and the former agent-conformance
rubric. Their preservation does not require every current review to use the
legacy format or reinstate its lifecycle gates. No enum value itself establishes
the technical severity of a finding.

Likewise, `FACT`, `ASSUMPTION`, `PROPOSAL` and `TBD` can support a review without
exhaustively or exclusively classifying all claims. Correct spelling of a label
is not evidence that its interpretation is correct.

### 7.4 State Machines

Product request, persistence and operation protocols can benefit from explicit
state machines. The retired deliverable lifecycle was one particular application
of the technique, not a necessary representation of all work and acceptance.

## 8. Human Factors & Decision Authority

### 8.1 Responsibility Allocation

Agent 0 holds purpose and continuity with the person. Other roles are used as the
undertaking needs them; TASK does not delegate. Agents can perform substantial
reckoning within authority. The person's situated, committed judgment is not
transferred by increased agent capability.

### 8.2 Cognitive Load

Clear current artifacts and concise returns can reduce investigation. Labels,
registers and records can also obscure relevant questions. Their cost includes
the human and agent attention needed to maintain and interpret them.

### 8.3 Proportionate Rigor

Rigor concerns adequate examination of consequential failures. Control count is
not a useful substitute. A control earns its place through the failures it
addresses, its cost and the limits of alternative feedback.

## 9. Cross-Cutting Patterns

### 9.1 Tree, Graph, Network and Attention

Composition, dependency and relevance are views of the undertaking. Attention
relates them for a purpose. They need not be four separately maintained datasets.

### 9.2 Local Meaning with Derived Views

Consumer declarations support on-demand queries without a competing authored
graph. A fresh query is still only as adequate as the declarations it reads.

### 9.3 Evidence and Its Limits

Provenance enables examination but does not validate an inference. Independent
review is valuable where assumptions and consequences warrant it; several checks
can still share an error.

### 9.4 Complementary Controls

A control contributes assurance only within its actual coverage. Several layers
do not prove that no single failure can compromise a result.

## 10. Assessment

The reset removed mechanisms previously presented as necessary while retaining
purpose, evidence, integration responsibility and reserved human decisions. That
challenges the necessity of the earlier arrangement. Sustained productivity,
recovery and transfer to other practitioners remain empirical questions.

### 10.1 The Revisable Relationship

Ontology, epistemology, praxeology and axiology supply enduring questions.
Architecture supplies revisable responses. An SE analysis should show how a
response addresses those questions, what it costs and what evidence supports it.
It should not treat an intelligible design as proof of accountable practice.
