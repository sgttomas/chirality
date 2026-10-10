# Chapter 9 — Discussion

---

## 9.1 Introduction

The thesis offers a framework and a developing case, not a proof that one
architecture is necessary for accountable agent-assisted work. Its enduring
questions concern what the work is, what supports its claims, how it is
carried into use, and what values and responsibilities govern it. The
implementation is a revisable response to those questions.

This chapter distinguishes normative commitments, design hypotheses and
empirical findings. The allocation of accountable judgment to people is a
commitment of the present system. The proposition that a particular
interface or record helps a person exercise that judgment is a design
hypothesis. Observations of its use can support, qualify or challenge that
hypothesis. Success at one level does not settle the others.

---

## 9.2 Limitations

### 9.2.1 No Controlled Empirical Validation

The architecture has not been validated through a controlled study with
practising engineers. The repository demonstrates substantial agent-assisted
production, examination and repair. It does not establish that Chirality:

- improves detection of consequential errors compared with other workable
  arrangements;
- reduces total effort for a comparable accepted result;
- improves calibration of professional confidence;
- transfers to another practitioner without its author's continuing help;
- meets professional regulatory obligations in a particular deployment.

The owner reports a material improvement in agent behaviour and productivity
after the October reset. The subsequent PRs show connected product work.
Both are relevant evidence, but neither isolates cause or supplies a
productivity multiplier. Work began at different times, agents and suppliers
changed, generated material dominates some diffs, and the owner continued to
steer. PR, line and file counts must not substitute for comparable completed
work.

### 9.2.2 Regulatory Interpretation, Not Endorsement

Chapter 6 examines professional supervision, review and reliance through a
particular reading of APEGA materials [CITE:APEGA_RWO2021]. That reading is
an argument to examine, not endorsement by the regulator and not a finding
of compliance. The description of an agent as a relied-upon contributor or
as a tool does not discharge the person's actual duties.

An implementation can preserve identified inputs, actions and decisions.
It cannot establish that a professional was competent, performed sufficient
review, or made a valid professional authentication merely because a record
exists. Application acceptance, approval of repository work and professional
authentication must remain distinct. The appropriate interpretation and
practice requirements need confirmation for the actual jurisdiction, work
and date of use.

### 9.2.3 Jurisdiction-Specific Regulatory Framework

The detailed regulatory discussion is specific to its Alberta basis. Other
jurisdictions and disciplines have their own definitions of competence,
supervision, review, authentication and responsibility. Similar language is
not evidence that requirements or legal consequences are interchangeable.

The portable research question is whether the application makes relevant
work, grounds and acts inspectable. The legal adequacy of a deployment
requires a separate, current assessment. The four philosophical questions
are not a regulatory checklist that certifies its answer.

### 9.2.4 Instruction-Level Enforcement

Instructions guide agent behaviour; they do not mechanically prevent every
prohibited action. A resolver, sandbox, schema validator or operation engine
can enforce particular predicates, subject to its entry points and coverage.
Independent review supplies a different kind of examination. A human
acceptance supplies an attributable commitment, not automatic error detection.

Earlier editions grouped these under an invariant-enforcement model and
sometimes inferred fault containment from declared write scopes. The revised
account requires a property-specific argument: what is prevented, by which
mechanism, under which conditions; what is merely requested; what is detected
afterward; and what remains dependent on practice. A conforming test of path
containment does not prove semantic correctness, and multiple layers can
share the same mistaken assumption.

Removing an obsolete validator can improve the system when its duty no
longer serves the work. It does not remove the need to examine the actual
permission, persistence and domain boundaries that remain.

### 9.2.5 LLM Capability Evolution

Agent capabilities affect the appropriate delegation, instruction, recovery
and verification arrangements. A procedure that once compensated for poor
continuity may later interrupt useful work. Improved inference can make
larger assignments practical; new capabilities can also expose new failure
paths. A cheaper or degraded model may require more support or a narrower
assignment. Benefit is not automatically monotonic in a fixed harness.

The historical K-* catalog mixed several kinds of rule: professional
commitments, product properties, operational conventions and accommodations
for then-current hosts. It was therefore incorrect to predict that model
changes could never justify an amendment to any invariant. Retaining a
responsibility boundary does not preserve every mechanism formerly used to
support it.

This revision concerns means, not an automatic transfer of authority.
An agent's increased capability can warrant a revised assignment. It does
not itself perform the person's committed judgment or grant institutional
standing. Section 9.3.5 develops that distinction.

### 9.2.6 Over-Proceduralization and the Displacement of Attention

The July discussion identified a limitation that the October reset later
made concrete. Records, labels and procedures can help a practitioner attend
to work; they can also become the objects of attention themselves. Polanyi's
account of subsidiary and focal awareness helps describe this reversal
[CITE:Polanyi1975]. The problem is not merely document volume. It is a loss
of integrated meaning when administrative particulars displace the
engineering question they were intended to support.

The reset removed routine receipts, duplicated status, authored progress
graphs and other record duties, together with their enforcement. Decisions
now change their current governing text; tools derive relationships; Git and
PRs retain history. This is evidence against the necessity of those earlier
mechanisms for every undertaking. It is not controlled proof that every
remaining mechanism is optimal or that every removed one lacked value.

The axiological assessment must include attention, delay, maintainability,
user agency and the consequences of missed error. A control is valuable to
the extent that its contribution to understanding, reliability or appropriate
authority justifies those costs. Efficiency does not override every other
value, but its costs cannot be excluded from the comparison.

Some records remain essential: an identified result, a consequential human
act or an uncertain operation outcome may need a durable trace. Machine
execution history can also support diagnosis and recovery. Their function
justifies them; routine duplication of the same account does not. No amount
of recording can compel substantive judgment or guarantee that a person
understands what they accept.

---

## 9.3 Generalizability

### 9.3.1 Across Engineering Domains

The four questions are plausible across domains: distinguish the objects and
relationships; expose relevant grounds and limits; make action, correction
and integration practicable; and locate values and responsibility. They do
not prescribe the same artifacts or controls everywhere.

App v4 and SWBPIPE provide different tests of the approach. Workflow authoring
exposes intent, assignments, interaction and returned work. Piping introduces
numerical meaning, domain state, units, persistence and consequential
engineering interpretation. The common human/agent operation interface is a
design hypothesis being developed, not an already demonstrated general
platform for every professional application.

Portability would be supported by another useful application adopting the
pattern with manageable adaptation, and by its actual performance. A shared
schema alone does not establish that result.

### 9.3.2 Across Regulatory Jurisdictions

The general distinction between producing information and taking
responsibility for reliance can inform work in different jurisdictions.
It does not transport the Alberta regulatory interpretation unchanged.
Each application needs its own account of who may act, what review is due,
which records matter and what constitutes authentication, if applicable.

A successful translation may change controls substantially while preserving
the framework's questions. Such a change is evidence of adaptation rather
than necessarily a failure of the framework.

### 9.3.3 The Four-Pillar Framework as an Evaluation Lens

The framework is useful when it exposes a missing distinction or an
unsupported architectural claim:

| Perspective | Question for an implementation |
|---|---|
| Ontology | Can participants distinguish the relevant work objects, relations and acts from their representations? |
| Epistemology | Can they inspect the grounds, assumptions, conflicts and limits of material claims? |
| Praxeology | Can authorized work proceed, be examined, corrected, integrated and recovered? |
| Axiology | Are the purposes, tradeoffs and responsibilities explicit enough to assess the arrangement? |

These questions constrain one another. A failure of recovery may reveal a
missing distinction between an attempted and a completed action. A newly
identified consequence may change the appropriate examination. A
burdensome control may consume the attention needed for substantive review.
There is no linear derivation from one pillar to a uniquely correct
architecture, and no pillar's importance permits neglect of the others.

The lens is non-exhaustive. It guides inquiry; it does not supply a complete
ontology of work or guarantee that a system answering each question is
adequate.

### 9.3.4 Epistemic Relations as Portable Concepts

Claims, grounds, uncertainty, gaps, conflicts and decisions are useful
concepts beyond this implementation. They need not all become fields in a
register. Their representation should make the relevant relation discoverable
where an undertaking needs it.

The former sequence UNWARRANTED → CITED → REVIEWED → AUTHENTICATED was a
historical mnemonic that combined unlike relations. Citation identifies a
source; examination assesses something about its use; authentication is a
particular attributable act. A cited claim can be wrong, a review can be
limited, and a person can stand behind an identified result while disclosing
uncertainty. These are not successive degrees of truth.

What can transfer is a disciplined distinction among evidence, situated
understanding and accountable reliance. The adequacy of a chosen
representation remains a design hypothesis. It cannot externalize everything
a knower brings to the work.

### 9.3.5 Capability-Invariance of the Authority Boundary

The heading identifies the narrower claim retained from the earlier thesis:
**greater agent capability does not by itself transfer accountable judgment.**
It does not mean that write scopes, role arrangements, gates or the historical
invariant catalog must remain unchanged.

Smith's distinction between reckoning and judgment supplies the philosophical
vocabulary [CITE:Smith2019]. Reckoning can be extensive and sophisticated:
agents investigate, infer, plan, compare, criticize, propose, check and act
within granted authority. This account does not equate reckoning with a
simple calculation or require its execution through rigid procedures.

Judgment is the person's situated and committed, world-involving engagement
with what the work means, what matters and what they will stand behind. It
shapes the question, relevant distinctions and grounds for reliance
throughout an undertaking. A final approval is one possible expression of
that engagement. Its record neither exhausts judgment nor guarantees its
substance.

The present professional allocation reserves accountable commitments to
people. That allocation permits substantial agent initiative and continuing
authority for ordinary work. It does not entail a read-only Agent 0,
mandatory managerial tiers or renewed approval at every internal step.
The agent responsibilities and the person's judgment concern different
relations to the undertaking.

Collins's account of socially acquired tacit knowledge contributes a further
reason to examine context and participation rather than equating capability
scores with accountable standing [CITE:Collins2010]. It does not settle the
metaphysical possibilities of future artificial systems. Any proposed
reallocation of professional responsibility would require an explicit
institutional and normative argument; it is not an inference from improved
output or delegated execution.

The former prediction of zero capability-triggered K-* amendments is
withdrawn. Each claimed property needs examination on its own terms.
Improved models may change how responsibility is supported while leaving
its current allocation in place. Conversely, a familiar mechanism may no
longer support that allocation adequately. The framework's value lies in
making such questions explicit and revisable.

### 9.3.6 Relationship to the AI Alignment Problem

Model-level work seeks desirable behaviour through training, feedback and
other interventions [CITE:Ouyang2022] [CITE:Bai2022]. Chirality examines the
system of use: how outputs, operations, evidence and human acts are related
in an undertaking.

These concerns are complementary. The framework does not make a model
truthful or safe under arbitrary deployment. Nor can an attribution record
prevent every misuse of an output. The aim is to support appropriate action
and reliance through useful distinctions, permissions, feedback and
inspectable decisions. Whether these mechanisms succeed is an empirical
question about the deployed system and its users.

The reckoning/judgment distinction prevents the architecture from treating
capability or an approval trace as a substitute for the person's engagement.
It is a constraint on the account of the system, not a claim that an
instruction can enforce all professional conduct.

### 9.3.7 Convergent Practice: Large-Project Delivery as Prior Art

The owner proposed that Chirality's structural views reflect recurring needs
of complex knowledge work, familiar from large-project delivery. That is a
useful comparative hypothesis. The earlier version of this subsection
extended a working-session observation into broad claims about project
practice without an independently sourced comparison. Those claims are not
established by this case.

The proposed correspondences can be stated without treating them as proof:

| View | Question | Candidate comparison in project delivery |
|---|---|---|
| Tree | What is the work composed of? | Work breakdown and scope definition |
| Dependency graph | What input or condition does this work need? | Precedence and interface planning |
| Relationship network | What other material bears on this question? | Cross-references, sources and decision history |
| Attention | How are contributions interpreted and brought into a coherent result? | Definition, coordination, review and synthesis |

These are views and activities, not four required databases. A dependency
graph need not be wholly acyclic: an executable ordering must respect actual
prerequisites, while mutual design relationships can be legitimate cycles.
A network of relevant material can be queried from current documents and
history without an append register. Attention remains the integrating
activity; its quality cannot be inferred from the presence of the other
three representations.

Neither agents nor people require every contextual fact to be written before
work can occur. Hosts preserve different kinds of state, people carry tacit
understanding, and participants can retrieve or investigate what is missing.
The practical problem is recoverable access to the relevant basis, including
uncertainty about that basis. Exhaustive institutional transcription is
neither demonstrated as possible nor shown necessary.

The comparison also must not equate a software acceptance control with an
engineer's authentication, or presume that software work lacks consequential
accountability. Analogies can identify design questions; their adequacy needs
examination within the receiving practice. An independent comparison with
project-delivery methods and a second practitioner's use would be more
informative than further elaboration of the analogy by its author.

---

## 9.4 Future Work

### 9.4.1 Empirical Validation

The first aim is to assess comparable usable results, consequential escaped
errors, recovery, and total effort. Existing PR, CI and session evidence can
support bounded observation without a new administrative register. Measures
must account for work begun earlier, generated content, task mix and the
owner's time.

A controlled study with practitioners could compare arrangements on error
detection, calibrated confidence and review effort. Self-reported confidence
alone is insufficient: an interface can increase confidence without improving
its grounds. The study should also examine whether participants understand
the scope and limits of what they accept.

### 9.4.2 Enforcement at Consequential Boundaries

Future engineering should target actual permission, operation, persistence
and recovery boundaries. For example, an unknown action outcome calls for
recovery semantics; an escaping write target calls for effective containment.
Neither problem necessarily requires a general runtime governance engine.

Each proposed control should state the consequential failure it addresses,
its real enforcement path, its residual limits and its cost. Historical
requirements for status propagation or universal receipts are not a standing
implementation backlog.

### 9.4.3 Empirical Validation of Epistemic Representation

Compare representations by whether people can find grounds, recognize
uncertainty, identify conflicting assumptions and understand what changed.
Useful studies could examine source-linked results, short contextual
qualifications and existing current documents. Counts of CITED or REVIEWED
labels are not adequate proxies for quality.

The inquiry is whether the representation supports judgment, not whether a
historical warrant lifecycle can be made universal.

### 9.4.4 Formal Analysis of Specific Properties

Formal methods may help with narrowly defined properties such as path
containment, state transitions, refusal of stale operations or duplicate
application after interruption. Their value depends on a faithful model,
verified implementation correspondence and coverage of the actual entry
points.

A proof about such a model cannot establish that an engineering claim is
true, that the intended need is met, or that a person has exercised
judgment. The scope of a proof must accompany its result.

### 9.4.5 Multi-Jurisdiction Regulatory Mapping

A receiving jurisdiction's requirements should be investigated when a
concrete deployment needs them. The result may require changed practice or
product behaviour. This thesis neither pre-authorizes that use nor makes a
broader regulatory survey a prerequisite for current development.

### 9.4.6 Multi-User Concurrent Execution

Concurrent agents already contribute to repository work. The additional
question is multiple accountable people acting on a shared undertaking:
which authority applies, how concurrent edits are handled, and how each
person understands another's commitments.

Locks can address certain write conflicts. They cannot alone resolve
conflicting purposes or responsibility. A useful test should examine a
concrete shared activity and its recovery paths instead of assuming one
coordination topology solves both mechanical and human problems.

### 9.4.7 Extension to Other Applications and Agent Platforms

The current design separates useful interface meanings from a mandatory
shared service. A practical transfer test is one domain operation available
through human and agent entry points with common validation, meaningful
refusal, inspectable outcomes and recovery.

The cost of adding another operation or application matters. A large adapter
and record burden would qualify the claim of useful proliferation even if
the interfaces were technically compatible. Native supplier capability
should be preserved where it serves the work; portability is not a reason
to recreate an unused general platform.

### 9.4.8 A Second Accountable Professional, Outside Software

The author remains a significant part of the functioning system. The owner
sets direction, supplies domain interpretation and detects process burdens.
A second accountable professional undertaking useful work without that
continuous translation would test whether the framework transfers.

The inquiry should observe what the practitioner can understand and use,
which sources and tools help, what requires explanation, what consequential
errors escape and what the work costs in attention and effort. A proposal,
investigation or calculation package outside software would broaden the
case. Success should not require the participant to reproduce the author's
vocabulary or organization.

---

## 9.5 Summary

Chirality offers a coherent framework and an evolving implementation case.
Its strongest result is a practical separation of work, evidence, action and
accountable commitment while agents perform substantial reckoning. Its
mechanisms remain hypotheses to be examined in use.

The October transformation strengthens the case by making earlier controls
revisable, not by proving the current arrangement final. Professional
reliance, generality, productivity and transfer to other practitioners remain
bounded empirical questions. The framework should expose the limits of its
own claims with the same care it asks of the work it supports.
