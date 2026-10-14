# Chapter 5 — Epistemic Architecture

---

## 5.1 Introduction

Three questions must remain separate:

1. What evidence or argument supports the claim?
2. What does that claim mean in the situation and for the intended purpose?
3. Who authorizes reliance on it, within what scope?

A citation can support a claim while leaving its relevance and intended use
unsettled. Authentication records an accountable act; it does not make the
content true or establish adequate engagement. Judgment shapes the undertaking
throughout, while agents extend reckoning through inquiry and action.

Knowledge resources are artifacts supporting situated knowing: models, sources,
calculations and returned findings help a participant inquire and act. Their
organization can preserve useful relations without containing or reproducing
everything a knower brings to the undertaking.

---

## 5.2 The Problem: Absence of Intrinsic Epistemic Warrant

The literature documents fluent but unsupported or false model outputs
[CITE:Ji2023] [CITE:Huang2023]. The important problem here is that fluent
presentation does not establish grounds for reliance. Correct and incorrect
claims can have similar surface forms. A model's confidence or a second
model's agreement cannot by itself distinguish them.

This problem extends beyond generated prose. A cited source may be wrong,
an equation may be applied outside its assumptions, a test may examine the
wrong property, and a deterministic calculation may use the wrong units.
Even faithful extraction establishes what a source says, not necessarily
what holds in the world.

Engineering review therefore needs access to the inputs, transformations,
assumptions and checks relevant to the intended claim. Review effort can be
targeted when these are accessible, but neither labels nor provenance justify
spot-checking a consequential claim without considering its failure modes.
The amount and independence of examination depend on consequence,
detectability and the evidence already available.

Chirality's response is to make useful grounds and limits discoverable in the
work's current artifacts and tools. It does not require a parallel description
of every sentence. A calculation file with its inputs and an applicable
oracle may be more informative than a prose register declaring that the
calculation passed.

---

## 5.3 The Four Mechanisms

The four mechanisms below are design approaches to recurring problems. Their
implementation must serve an actual reader, check or reliance decision. The
identifiers provide a cross-reference to [Appendix A](appendix_a_invariant_catalog.md);
[Appendix E](appendix_e_development_history.md) records the evolving implementations.

### 5.3.1 Mandatory Provenance (K-PROV-1)

**The enduring requirement.** A consequential extracted claim must be
traceable to the source said to support it, or its missing support must be
clear. Provenance need not require a separate register.

**Current application.** Keep the source reference with the claim or its
current technical basis. Identify a revision when changes in that source
would matter. Tools can resolve references and compare revisions. Neither
successful resolution nor an unchanged hash establishes that the source is
applicable or that the interpretation is correct.

The deliverable model keeps consumer needs and their conditions in
`deliverable.yaml`, with supporting explanation in current source documents where
useful. A query exposes relationships from these declarations.

**Worked example.** An agent reads a scope document stating that detailed
design requires approved structural analysis. The consumer's need can say:

> Structural analysis results from DEL-01-01, suitable for the detailed-design
> basis. Source: scope document §4.2.3, identified revision.

If the agent also infers that foundation design needs geotechnical results,
it can state that as an inferred need whose applicability remains to be
resolved. It should not attach an unrelated scope citation and present the
inference as an explicit requirement. The two needs differ in their grounds,
even if both ultimately prove useful.

A reviewer can inspect the stated requirement, the proposed inference and
the actual input. A supplier file's presence or merged PR does not establish
that either need has been met.

### 5.3.2 No Invention (K-INVENT-1)

**The enduring requirement.** Do not present an invented value as an observed,
extracted or accepted value. Make material unknowns apparent. This does not
prohibit creative alternatives, exploratory calculations or explicit
hypotheses.

A required missing input can block a particular calculation while leaving
other work possible. The appropriate response is to identify that boundary,
obtain or propose the missing input within authority, and continue unaffected
work. A universal halt state for every uncertainty would obstruct inquiry.

**Worked example.** A vendor data sheet gives an operating temperature range
of −20°C to +60°C and a flow rate of 500 m³/h, but no design pressure. A
conforming extraction identifies design pressure as unknown. An agent may
propose a candidate pressure for an explicitly bounded sensitivity study; it
must preserve that study's assumption and must not silently promote the
candidate into the accepted design basis.

Instructions can require this behaviour, and checks can detect some
violations. Neither instructions nor a `TBD` convention guarantee that every
missing input has been recognized.

### 5.3.3 Conflict Surfacing (K-CONFLICT-1)

**The enduring requirement.** Do not conceal a material disagreement among
sources or between evidence and the current basis. Show what conflicts, where
it comes from and what action or decision it affects.

Suppose the scope requires operation at −30°C and a vendor sheet gives a
−20°C limit. The conflict is not resolved by averaging the values or choosing
the more recent file. Its significance depends on whether the requirement,
equipment selection or interpretation is wrong. An agent can investigate,
propose alternatives and apply an already-authorized resolution. A change to
a reserved commitment or acceptance of risk belongs to the accountable
person.

The resolution changes the current governing text or product. Its reason and
material consequences belong in the undertaking's existing change record.
A conflict table can help with several related disputes; a separate permanent
ledger is not required for every discrepancy.

### 5.3.4 Epistemic Labeling

Labels can make an otherwise ambiguous distinction visible. They are
annotations about a claim, not rankings of its truth or substitutes for its
grounds.

| Label | Useful reading | What it does not establish |
|---|---|---|
| FACT | A stated observation or an accurately cited source statement | The source's truth, completeness or applicability |
| ASSUMPTION | A premise used provisionally in reasoning | That the premise is reasonable or safe for the intended use |
| PROPOSAL | A candidate action, requirement or interpretation | Authorization or acceptance |
| TBD | A recognized missing input or unresolved matter | That all gaps have been found |

An explicit source phrase, an assumption beside an equation, or a tool's
`unknown` result can carry the distinction without an uppercase label. Use
the form that helps the consumer interpret the work. A requirement to label
every non-trivial claim may create volume without making a consequential
assumption easier to find.

Labels and confidence estimates also differ. A precise quotation can be
labelled FACT while reporting a mistaken source. A well-supported inference
can remain an inference. Review must examine the grounds and purpose rather
than treat labels as permission to rely.

---

## 5.4 The Epistemic Architecture as a Coherent Theory

The mechanisms address related questions:

1. **Provenance:** where do the claim and its asserted grounds come from?
2. **No invention:** what is actually missing, and what has been hypothesized?
3. **Conflict surfacing:** which statements or conditions cannot jointly govern?
4. **Epistemic labeling:** what kind of assertion is being made?

Their common aim is inspectability. That aim is constrained by ontology
(which objects and claims are being examined), praxeology (how inspection
leads to action or repair) and axiology (which failures and costs matter).

A useful architecture can expose a missing source, a failed oracle or an
unresolved condition. Complete-looking evidence may share a mistaken premise,
and a validator detects only what its rule examines. Smith's distinction between
relative consistency of artifacts and correctness about the world remains
relevant here [CITE:Smith1985].

The theory therefore yields a design question rather than a unique schema:
what must be inspectable for this work's consequential claims to be examined,
and what representation makes that examination practicable?

---

## 5.5 Grounds, Examination and Accountable Reliance

Grounds, examination and reliance are related, independently revisable relations:

- **Grounds:** a claim may have observations, calculations or arguments without
  a citation. A cited claim may have inadequate grounds.
- **Examination:** review has a subject, method, scope, revision and findings.
  A review can weaken a claim, disclose missing premises or become inapplicable
  after a relevant change.
- **Reliance:** acceptance or authentication relates an accountable actor to
  identified content, scope and purpose. It is not a higher truth value.

These relations can be represented where they matter, without assigning every
claim a stored stage. A dependency query reports observable facts and
unknowns. An agent assesses whether an input meets its condition within the
assignment; a person exercises judgment where accountable commitment is at
issue. No aggregate count of citations or passed checks makes an undertaking
accepted.

The distinction between a **descriptive record** and a **constitutive act** is
important. An agent's note that an owner approved something is a report that
needs a source. Where an authorized process defines a person's action as
acceptance, a host may capture that action and its scope faithfully. The
person need not manually type every byte of the resulting record. Conversely,
a generated receipt or a hash match cannot invent the action or establish the
adequacy of the person's engagement.

Content identification supports the relation. A fingerprint can show which
bytes were named; identity controls can support attribution. They do not
establish that those bytes were reviewed adequately, that the source actor
was authorized, or that the conclusion was right. A later edit does not
rewrite the historical act. It raises the question of whether the prior
acceptance applies to the changed work.

---

## 5.6 Comparison to Alternative Approaches

This comparison concerns what the cited approaches contribute. It is not a
claim that all implementations of them lack provenance or uncertainty
reporting, nor a current benchmark ranking.

### 5.6.1 Reinforcement Learning from Human Feedback (RLHF)

RLHF trains behaviour using human preference signals [CITE:Ouyang2022]. Such
training does not by itself provide the evidence needed for a particular
engineering claim. Better model behaviour and better access to grounds can
both improve work; the remaining examination depends on the use.

### 5.6.2 Retrieval-Augmented Generation (RAG)

Retrieval makes source material available during generation [CITE:Lewis2020].
A retrieved passage can support a response, but its presence does not ensure
faithful interpretation or disclose interpolated assumptions. Specific source
references and examination of the resulting claim remain useful. Retrieval
through files and tools can serve the same general purpose where the task
requires it.

### 5.6.3 Post-Hoc Factuality Checking

Post-hoc checking can identify unsupported claims against a reference corpus
[CITE:Min2023]. Its value depends on the corpus, checking method and claim
coverage. A checker can itself be mistaken. Generation-time annotations and
later examination are complementary options, not competing guarantees.

### 5.6.4 Constitutional AI

Principle-guided critique can improve behaviour [CITE:Bai2022]. Agreement
with a principle does not supply empirical grounds for a domain claim, and a
model's critique can share the original error. The useful division is between
behavioural guidance and evidence appropriate to the claim, rather than an
assumption that one makes the other unnecessary.

### 5.6.5 Summary of Positioning

| Approach | Relevant contribution | Remaining question for this undertaking |
|---|---|---|
| Preference training | Improve model behaviour | What supports this particular claim? |
| Retrieval | Bring potentially relevant sources into the task | Are they applicable and faithfully used? |
| Post-hoc checking | Detect some unsupported or inconsistent claims | What did the check cover and miss? |
| Principle-guided critique | Examine output against stated principles | Is the critique itself well grounded? |
| Chirality's proposed epistemic architecture | Keep relevant grounds, limits and reliance relations inspectable | Does the actual arrangement improve examination at an acceptable cost? |

---

## 5.7 Enabling Professional Reliance

The potential contribution is practical: a reviewer can inspect a calculation's
basis, an input's revision, a material unresolved conflict and the claimed
extent of a check. The reviewer need not depend solely on an agent's summary
of those things. Existing product artifacts, source history and execution
results may already provide the necessary evidence.

This support can reduce repeated investigation. It cannot establish how much
review a particular professional work product needs. For a consequential
numerical claim, an independent calculation, oracle or method comparison may
matter more than extensive claim annotation. For an uncertain requirement,
direct engagement with the owner may matter more than another test.

The empirical questions are whether material problems are found in time,
whether the professional can understand the result and whether relevant
actions can be reconstructed when needed. Passing a schema check is evidence
about the schema check alone.

---

## 5.8 Summary

Chirality adopts a norm: claims should not exceed their available support, and
accountable reliance must remain distinguishable from production and
verification. It proposes inspectable sources, material unknowns, visible
conflicts and useful annotations as ways to support that norm.

These are design hypotheses with costs and limits. They warrant records where
a consumer, acceptance requirement or recovery need justifies them. Their
adequacy depends on whether participants can examine the material grounds and
act on findings in time for the intended use.

Agents can extend reckoning throughout the undertaking. Human judgment shapes
its purpose, interpretation, action and reliance; it is not exhausted by an
approval record. The architecture's contribution must be assessed through the
work it enables and the failures it helps reveal, not inferred from the
completeness of its own paperwork.
