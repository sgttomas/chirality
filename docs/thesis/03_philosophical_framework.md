# Chapter 3 — Philosophical Framework

---

## 3.1 Introduction

This chapter explains the philosophical commitments and design questions of the
Chirality Framework [CITE:Chirality_FRAMEWORK]. Chapter 4 examines their
architectural expressions. The distinction matters: an enduring responsibility
does not uniquely determine a gate, document format, agent hierarchy or runtime.

The framework developed in dialogue with practice. Earlier versions organised
work through document kits, lifecycle records and prescribed delegation. Later
revisions removed much of that machinery while retaining explicit purpose,
evidence, integration responsibility and human authority. That experience is a
reason to distinguish commitments from the mechanisms chosen to serve them.
It is not, by itself, evidence that the replacement is best in every setting.

Ontology asks what exists and how it is represented. Bunge and Wand and Weber
provide a source for assessing representations in information systems
[CITE:Bunge_ontology] [CITE:Wand_Weber_ontology]. Epistemology concerns knowledge
and its grounds; provenance models provide one operational vocabulary
[CITE:W3C_PROV2013]. Praxeology concerns action and practical reasoning, for
which systems engineering offers methods [CITE:INCOSE2023]. Axiology concerns
values, purposes and consequences, including professional obligations
[CITE:APEGA_RWO2021]. These are related questions, not a sequence of mandatory
forms.

This chapter distinguishes three kinds of claim. **Normative commitments** state
what the framework values or what an applicable obligation requires. **Design
hypotheses** propose how a mechanism could serve those commitments. **Empirical
findings** report what examination establishes in actual use. Philosophical
coherence can support a design argument; it cannot substitute for evidence of
performance, compliance or transfer to another domain.

---

## 3.2 The Four Pillars

### 3.2.1 Ontology — What Exists in the System

The ontological commitment is to preserve distinctions that matter to the work.
A requirement, an assumption, a physical model, a proposed operation, a result
and an acceptance are different things. Confusing them can authorize an action
that nobody intended or make a result appear better supported than it is.

Three levels must remain distinct:

| Level | Example | What examination must establish |
|---|---|---|
| Work or domain entity | A support, an intended deliverable, a required input | What it is, how it relates to the purpose, and which constraints apply |
| Representation | A model object, ScopeOfWork, dependency declaration or graph view | What it denotes, what it omits, and whether it remains faithful |
| Implementation convenience | A lock, cache, index or temporary file | What operation it supports and whether its failure affects the work |

Bunge and Wand and Weber inform the examination of domain representations
[CITE:Bunge_ontology] [CITE:Wand_Weber_ontology]. Their use here does not justify
the earlier claim that every software construct must correspond directly to a
thing in the domain. Locks and caches can be legitimate implementation objects.
They must not silently become sources of domain truth or authority.

The filesystem is a shared working medium, not the ontology itself. In current
repository practice, a deliverable folder brings together commitments, design
and declared needs. Tools derive relationships from those sources. The folder
can misrepresent the work; the graph can omit a dependency. A query must report
its basis and unresolved inputs rather than treat successful parsing as proof
of suitability. Product engines may own domain state under their applicable
contracts, so not every authoritative fact is a Markdown file.

The tree answers what belongs within a larger undertaking. The dependency graph
answers what one contribution needs from another. A network can expose other
relevant connections, such as a common source or decision. These are views of
the work and need not be separately authored stores. Attention is the activity
through which participants relate these views to the undertaking. A missing
edge cannot establish independence: shared writes, resources and interfaces may
still connect apparently separate tasks.

The distinction between descriptive and constitutive records also requires
care. A stress result describes a state of affairs and can be wrong. An approval
record may be part of an institutional act if the applicable process gives it
that role. Its formal presence alone does not establish that the actor had
authority, adequately examined the subject or engaged with its consequences.
A recorded decision and a well-founded decision remain different claims.

### 3.2.2 Epistemology — What Can Be Known, and How

Fluent output is not self-certifying. A numerical value and plausible citation
can look credible while being unsupported. Retrieval and other techniques can
improve grounding, but the presence of a source does not establish that it
supports every inference made from it [CITE:Ji2023].

The framework therefore asks that material grounds and their limits be
inspectable. A source can support a definition without supporting a numerical
formula extracted from it. A test can establish specified behaviour without
establishing fitness for every use. Agreement among agents can show consistency
with a shared premise while leaving that premise unexamined.

#### The Ontology of the Epistemology

The framework uses six concepts to expose these distinctions. They are tools
for inquiry, not an exhaustive state space of knowledge.

| Concept | Meaning | Limit |
|---|---|---|
| Claim | An assertion about a subject | A clear assertion may still be false |
| Warrant | Relevant grounds: a source, observation, calculation, test or argument | Confidence and fluency alone do not establish adequacy |
| Status | A scoped classification useful to examination | A label is not its supporting evidence |
| Gap | Missing information or grounds whose consequence matters | Recording a gap does not resolve it |
| Conflict | Incompatible claims requiring examination of sources, scope or meaning | Some conflicts can be resolved by inquiry; others require a choice |
| Ruling | A decision by the relevant authority | Authority can settle a choice, not manufacture factual support |

FACT, ASSUMPTION, PROPOSAL and TBD are useful conventions where a consumer needs
them. They must not imply that a cited statement is universally true or that
an adopted assumption has become an observation. Nor does every routine
implementation proposal require a new owner decision. Its authority depends on
the assignment, commitments and reserved choices.

Provenance, explicit uncertainty, conflict surfacing and examination can make
unsupported claims easier to find. The early system enforced these through
required CSV fields, labels and review tables. Those historical mechanisms
must be assessed separately from their purpose. A source-field validator detects
a missing field; it does not determine whether the source is faithful, relevant
or sufficient. An instruction against invention is not a guarantee that an agent
will never fabricate content.

Current product commitments may retain specific provenance, authority and
content-binding requirements. This philosophical account neither removes those
requirements nor extends them to consumers that did not adopt them. Current
repository practice instead maintains relevant grounds with the work and queries
the needed context. Conversation supplies present intent, while source documents
and existing change records preserve what later use requires.

#### The Warrant Lifecycle

Earlier versions represented warrant development as:

```
UNWARRANTED → CITED → REVIEWED → AUTHENTICATED
```

The notation is retained here to explain the historical design. It is not a
required deliverable lifecycle. It combines different relationships:

| Question | Relevant relation |
|---|---|
| What supports this claim? | Claim to evidence, with scope and limits |
| What examination has occurred? | A subject and revision to a review method, examiner and findings |
| What reliance has been accepted? | An accountable person to identified content, purpose and conditions |

These relationships can change independently. A claim can acquire contrary
evidence after review. A technically supported result may have no accepted use.
A person can accept reliance under stated uncertainty without converting that
uncertainty into a fact. Authentication changes normative standing; it does not
add another experimental observation.

Review is therefore inquiry into adequacy for a purpose, not completion of a
universal sequence. A content hash can identify what was examined or accepted
where that binding is required. It cannot establish the meaning, quality or
sufficiency of the examination. Nor does a review record prove the person's
committed engagement. Appendix D offers an interpretation of commitment, not a
formal definition of review or authentication.

Chapter 5 develops the epistemic mechanisms. Their value depends on whether they
help expose a consequential uncertainty and whether actual examination can act
on it. More recorded state is not automatically more knowledge.

### 3.2.3 Praxeology — How Work Is Done

The praxeological question is how intention becomes a usable result through
investigation, production, examination, repair and integration. Responsibility
must persist across these activities. It need not be divided among agents at
every boundary.

The current roles describe contributions. Agent 0 holds purpose and continuity
with the owner. HELPS_HUMANS contributes design. WORKING_ITEMS owns an
implementation undertaking and integration. TASK executes a bounded assignment
and does not delegate. Except for Agent 0's continuing responsibilities, the
undertaking determines which roles are useful. One session may carry the work
without delegation.

Responsibility, staffing and permissions are different. A role identifies a
contribution; an assignment identifies the present objective and limits; a host
supplies actual tools and enforces some permissions. The role name alone cannot
grant tools or impose a universal read-only rule. Written boundaries and
mechanical containment must be described according to what they actually enforce.

One coordinator owns a shared result. Independent work need not wait behind an
unresolved branch. Shared writes, interfaces, resource limits and review capacity
can nevertheless justify sequencing. The graph identifies declared relationships;
participants must examine whether apparent independence is real.

Owners continue through ordinary repairs. A finding changes the relevant action,
not necessarily the staffing. Existing evidence remains useful unless a change,
contradiction or uncovered concern invalidates it. An uncertain outcome requires
inspection before an action is repeated. A separate approval is needed only
where authority or an applicable condition requires it.

This practice preserves explicit holds and owner-reserved commitments. It removes
the inference that accountable work must have a gate at every phase or a separate
record at every handoff. The method must support progress, correction and recovery
within authority, with costs proportionate to the undertaking.

### 3.2.4 Axiology — What the System Values

Professional responsibility and public welfare remain central commitments. Agent
capability does not authorize an agent to certify, seal or issue professional
work for reliance. Applicable professional obligations remain with the person
who undertakes them; Chapter 6 examines that setting.

The axiology also includes useful attention, maintainability, user agency and
timely delivery. These are not costs external to accountability. A register can
bury a consequential decision. A repeated approval can train a person to respond
mechanically. Unnecessary checking can displace examination of a more consequential
uncertainty. Removing such a control can improve both throughput and responsible
engagement.

A control is justified when its contribution to understanding, reliability or
appropriate authority warrants its attention, delay and complexity. That is not
permission to disregard a required condition. It is a basis for choosing and
revising the mechanisms that meet the condition. Silent numerical error warrants
a different examination from a reversible wording change.

Values can be expressed in requirements, defaults, interfaces and prohibitions.
Those expressions can guide action without becoming the person's commitment.
The framework cannot mechanize the person's answerability by encoding a value
function. It can make tradeoffs visible, preserve their consequences and help the
person respond to them.

---

## 3.3 The Fractal Property

The *fractal property* names the recurrence of the four questions at different
scales. A numerical result, a deliverable, an application and the framework itself
can each be examined for their entities, grounds, course of action and values.
The term describes this recurrence rather than a mathematical fractal.

Earlier document kits assigned Datasheet, Specification, Guidance and Procedure
to the four pillars. Governance texts used a similar division. These were
historical implementations, not necessary consequences of the questions. The
current deliverable model can answer several questions in one ScopeOfWork or
Design document and derive other information through tools.

| Scale | Example of a useful distinction |
|---|---|
| Numerical result | A passing example does not establish accuracy outside its tested range |
| Deliverable | Implementation completion does not establish owner acceptance |
| Application | An available operation does not establish authority to apply it |
| Framework | A coherent mechanism does not establish that its benefit exceeds its cost |

Repeating the questions can expose a neglected relationship. Repeating the
forms without that purpose can create administrative work. Recurrence is a design
resource, not proof of completeness or a requirement for four documents.

---

## 3.4 The Load-Bearing Pillar

Earlier revisions called epistemology the load-bearing pillar and argued that
the other three existed to serve it. The concern motivating that emphasis remains:
plausible agent output can conceal weak grounds. But the proposed thought
experiment did not establish a hierarchy among the pillars.

Removing prescribed gates does not remove praxeology. Replacing a filesystem
schema does not remove ontology. The October transformation changed those
mechanisms while preserving distinctions and responsibilities. It is evidence
against treating the earlier mechanisms as necessary, not a demonstration that
one pillar can be omitted.

The four perspectives constrain one another:

- Purpose and consequences determine which uncertainty is worth investigating.
- Ontological distinctions identify the subject of a claim or operation.
- Evidence can expose a flawed distinction, assumption or intended use.
- Practice determines whether inquiry, correction and acceptance can affect the
  actual result.
- Experience of control costs can require a different method of examination.

Epistemology thus has a particular emphasis in this study, while adequacy depends
on all four. Inspectable warrant is valuable because of what people need to do
and stand behind. It must be connected to a subject and a workable course of
action. No pillar alone establishes suitability for professional practice.

Productivity and accountable reliance can support each other. Redundant records
can impede both; useful checks can improve both. The design question is which
arrangement enables useful work with adequate evidence and appropriate authority,
not how much administrative structure demonstrates concern for accountability.

---

## 3.5 The Pillars as the Ontology of Professional Accountability

The four pillars offer a compact evaluative framework. They are not an exhaustive
ontology of everything a professional can perceive or a proof that every
accountable system must adopt Chirality's vocabulary.

| Question | A failure it can expose |
|---|---|
| What kind of thing is this? | Treating a proposed model change as an applied result |
| What supports the claim? | Relying on a passing check beyond the claim it tested |
| How does this become usable work? | Leaving completed contributions without integration |
| What matters and to whom? | Improving a local metric while reducing user control or safety |

Consider an agent proposing a support change in SWBPIPE. The physical model,
proposal, applied operation, analysis result and acceptance must remain distinct.
The result depends on identified inputs, methods and assumptions. The operation
needs an actual route through validation and application, including refusal of
stale inputs and recovery where supported. The person retains applicable
engineering and reliance decisions. These questions guide the design without
selecting a unique API, file format or process topology.

Systems engineering supplies methods that can serve those questions
[CITE:INCOSE2023]. Their selection is a design hypothesis to examine in use.
A failed recovery can reveal that the outcome model was incomplete. A new risk
can require a different test. A more capable agent can make an old supervision
step unnecessary. These revisions can improve coherence because the framework
is mutually corrective, rather than a one-way derivation from philosophy to code.

---

## 3.6 The Chirality of Knowledge

The project name identifies one explanatory claim: there is a permanent
accountability gap between externalizable information and accountable
knowing. The metaphor is deliberately bounded. It does not supply a geometry
of knowledge, divide knowledge into a fixed number of parts, or make every
duality in the architecture chiral.

### 3.6.1 Information and the Knower

Information can be recorded, transmitted, copied, cited, compared, and
organized. Knowledge is a situated achievement of a knower. Without a knower,
information is not known as knowledge. The thesis does not impose the usual
factive condition that only true belief can count as knowledge: a person may
know wrongly, incompletely, or provisionally and later revise what they know.
Professional evidence and review matter partly because knowing can be
mistaken.

This position separates two questions that are easily conflated:

1. **What does a person know from the information?** This is situated in the
   knower and may differ with context, purpose, experience, and time.
2. **What reliance has an accountable actor accepted?** This is recorded by a
   scoped act bound to identified content.

Evidence and review may discipline what a person knows. Authentication
answers the second question by evidencing the actor's attributable acceptance
of reliance; it neither creates knowledge nor establishes reality as it
ultimately is.

### 3.6.2 The Accountability Gap and Operational `Gap`

The permanent **accountability gap** is the non-identity between information
and accountable knowing. No artifact, provenance chain, semantic model, or
approval record is identical with a person's knowing. More information may
change what a person knows; it does not remove the need for a knower or make
the resulting knowing universal.

The operational primitive `Gap` has a narrower meaning. It records that a
warrant has not been found for a claim. An operational `Gap` is remediable:
a source may be located or a claim revised. A ruling may authorize action
under uncertainty without supplying the missing warrant. The accountability
gap is not missing evidence and cannot be closed by another citation. Keeping the terms separate prevents a permanent feature of knowing
from being mistaken for a workflow defect.

### 3.6.3 Configurational Multiplicity

Identical information may occasion different knowledge in different knowers,
or in one knower under different contexts, purposes, or times. This thesis
calls that openness **configurational multiplicity**. The phrase does not
claim that every interpretation is equally good or that evidence is
irrelevant. It says that information underdetermines the situated knowing it
may occasion.

Chirality's schemas, Knowledge Types, semantic lenses, and knowledge graphs
are therefore scaffolding rather than exhaustive categorizations. They make
important questions and relationships inspectable, support comparison, and
focus professional review. They do not define a closed state space containing
everything any knower can perceive in the information. A semantic model can
organize a work product for a stated purpose; it does not legislate the limits
of knowledge.

Authentication stabilizes one accountable relation within this multiplicity.
An identifiable actor binds acceptance to identified content or SHA, scope,
and purpose. That act gives the information accountable-reliance status
within the stated relation. Another knower may know something different from
the same information, and the authenticating actor may later revise their own
knowing through a new attributable act.

### 3.6.4 Philosophical Precedents and Limits

The framework draws resources from six philosophical precedents without
claiming exact correspondence or derivation.

**Niels Bohr's complementarity** [CITE:Bohr1958] provides a precedent for
resisting the demand that every adequate account collapse into one
description. The thesis borrows only that restraint. It does not import a
physical theory into epistemology.

**Michael Polanyi's personal and tacit knowing** [CITE:Polanyi1958]
[CITE:Polanyi1966] and his later work with Harry Prosch [CITE:Polanyi1975]
support the priority of the knower, the personal contribution to knowing, and
the fiduciary character of professional commitment. Polanyi is a principal
resource for understanding why knowing cannot be exhausted by explicit
information. The framework does not claim to formalize Polanyi exactly.

**Brian Cantwell Smith's registration and answerability**
[CITE:Smith1996], together with his distinction between computational
reckoning and judgment [CITE:Smith2019], provides a principal resource for
the accountability gap. Registration is an achievement of a situated
subject, and judgment involves answerability not supplied by formal
calculation alone. The framework uses this distinction without treating
Smith's metaphysics as an architectural specification.

**Reckoning can be extensive.** In this framework, agents can investigate,
infer, compare, propose, assess, plan, check and act within granted authority.
Those activities can involve sophisticated reasoning and adaptation. Calling
them reckoning does not reduce them to trivial calculation or imply a need for
rigid procedures.

**Judgment is situated and committed.** It is the person's world-involving
engagement with what the work means, what matters and what they will stand
behind. It shapes purpose, framing, interpretation and action throughout the
undertaking. Final acceptance is one expression of judgment; an approval record
neither exhausts it nor proves sufficient engagement.

**Responsibility is distinct from capability.** The present professional
allocation places accountable judgment and duty of care with the person. Greater
agent capability can change delegation, supervision and verification without
itself transferring that responsibility. This is not a metaphysical proof of
what every future machine could or could not become. It also prescribes no
read-only Agent 0, mandatory manager layer or repeated approval of ordinary work.

For clarity, this thesis uses *assessment*, *evaluation*, *interpretation* and
*selection* for agent activities when *judgment* would confuse this distinction.
Ordinary operational uses of the word elsewhere do not confer professional
authority.

**Wilfrid Sellars' space of reasons** [CITE:Sellars1956] clarifies that
justification is not reducible to causal description. In Chirality this
supports the practical distinction between producing an output and giving
inspectable grounds for reliance. It does not place machines and humans in
mutually exclusive metaphysical realms.

**Robert Brandom's inferentialism** [CITE:Brandom1994] illuminates the
normative statuses undertaken when a person makes and defends a claim. It
helps explain why attributed commitment matters, but the project's
operational `Claim`, `Warrant`, and `Ruling` primitives are governance
constructs rather than translations of Brandom's system.

**Nishida Kitaro's account of maintained tension**
[CITE:Nishida1945] provides a precedent for relations whose difference need
not be erased through synthesis. The framework takes from Nishida the
permission to leave a constitutive gap open, not a claim that his
contradictory self-identity and this accountability account share one
structure.

Polanyi and Smith carry the principal philosophical weight: Polanyi for the
knower's personal and fiduciary involvement, Smith for situated registration,
judgment, and answerability. The other precedents sharpen particular
features. None warrants a claim of geometric refinement or exact
correspondence.

### 3.6.5 What the Chirality Metaphor Contributes

The metaphor gives the project a compact name for an orientation that cannot
be delegated away: information may be externalized, while knowing and
accountable reliance remain situated in persons. The architecture can expose
the informational substrate and record an accountable relation across the
gap. It cannot replace the knower with the record.

Polanyi's account of tacit integration gives this limit a positive structure
[CITE:Polanyi1975]. In the from–to structure of knowing, a person attends
*from* subsidiary particulars *to* a focal whole, and particulars scrutinized
in themselves lose the joint meaning they subtend. The governed record is
designed to occupy the subsidiary position: the practitioner attends from
claims, grounds, models and their relationships to the engineering reality
that remains focal. On this reading, explicit representation can support
integrated understanding. A failure occurs when recording displaces attention
to the work — a failure mode this thesis names directly (§6.9.4, §9.2.6).
Several disciplines serve the intended orientation: generated output must not
claim acceptance in its own voice (§6.8.3), and examination responds to the
consequence and detectability of error (§5.7). A record is useful through what
it lets participants examine and do, not merely because it exists.

This contribution is narrower than an architectural prescription. `Claim` and
`Warrant`, meaning and commitment, and the four
accountability pillars remain important distinctions, but they are not
independent chiral structures. The primary chirality is only the
accountability gap. The value of the metaphor is explanatory economy, not
formal precision.

### 3.6.6 Why the Gap Is Not a Synthesis Problem

The contrast with Hegelian synthesis is practical rather than a claim about
all dialectical philosophy. In professional AI governance, it would be a
mistake to treat better output as progressively eliminating the accountable
professional. Capability can reduce effort and error while leaving the
allocation of authority unchanged.

Chirality therefore optimizes for visibility and attributable reliance
across the gap, not for erasing it. This position does not deny that human and
machine activity can be deeply integrated. It denies only that integration,
accuracy, or fluency by itself transfers duty of care or makes authentication
automatic. The gap persists because information and accountable knowing are
not the same kind of status.

### 3.6.7 Engineering Regulation and Accountable Reliance

The APEGA practice standard *Relying on the Work of Others and Outsourcing*
[CITE:APEGA_RWO2021] is evidence for the practical importance of this
distinction, not proof of a metaphysical thesis. Its requirements for direct
supervision and control, thorough review, and authentication place obligations
on the professional who relies on work prepared by others. They do not make
the producer's capability a substitute for the professional's attributable
act.

Authentication, as used here, binds an accountable actor to identified
content, scope, and purpose. It confers accountable-reliance status; it does
not turn information into knowledge, guarantee correctness, or determine what
another knower must know. That interpretation distinguishes evidence and
examination from accountable commitment. It does not require the historical warrant lifecycle
or establish that a particular repository process satisfies a professional
standard.

Other frameworks address supporting parts of the architecture. Bunge and
Wand and Weber [CITE:Bunge_ontology] [CITE:Wand_Weber_ontology] inform the
ontological pillar; W3C PROV [CITE:W3C_PROV2013] supplies a provenance
vocabulary; Toulmin [CITE:Toulmin1958] is a precedent for the operational
distinction between claims and warrants; and the INCOSE handbook
[CITE:INCOSE2023] supplies the systems-engineering disciplines discussed in
Chapter 7. These relationships support the architecture without multiplying
the primary chirality.

---

## 3.7 Summary

The four pillars provide enduring, mutually corrective questions about work.
They direct attention to relevant distinctions, grounds, courses of action and
values. They do not uniquely derive a document kit, gate sequence, staffing
arrangement or runtime.

The reckoning/judgment distinction preserves both sophisticated agent capability
and the person's situated commitment. Agents can carry substantial authorized
work. The person remains responsible for the professional reliance they accept,
and that engagement begins before the final approval.

The primary chirality remains the non-identity between externalizable information
and accountable knowing. Evidence and records can support that relation without
performing it. The recurring four questions apply to Chirality itself: its
mechanisms require examination for adequacy, cost and limits of transfer.
