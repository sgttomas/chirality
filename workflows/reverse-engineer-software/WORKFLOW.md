---
name: reverse-engineer-software
description: Examine existing software and reconstruct a specification of its capabilities, behaviour, relationships, and constraints to support designing a new implementation. Use when a reference product is a starting point for developing product intent.
---
# Reverse engineer software

Develop an account of existing software that another participant can use to
reason about a new implementation. Follow what people and other systems can
accomplish, the behaviour that makes this possible, and the choices that shape
the experience. Let the human's reactions guide investigation and emerging
intent. Keep the reference account and desired departures distinguishable.

The normal output is a reference specification with supporting evidence,
coverage limits, and a record of proposed or adopted departures. Its acceptance
as a reference does not make every observed behaviour a requirement for a new
product. A focused feature or connected activity can be the whole assignment.

## Frame the investigation

Start with the reference software, the purpose of examining it, and whatever
the human already wants to preserve or change. Recover these from the existing
conversation where possible. Develop missing direction through concrete examples.
An initial interest may be exploratory; a complete new-product concept is not
a prerequisite.

Identify the actual available sources: a running product, user demonstrations,
documentation, interface descriptions, source code, tests, or retained examples.
Record the version, edition, configuration, user role, and date where they affect
the evidence. If those are unknown, preserve the limitation. Source code is
optional. Documentation alone can support a documented capability account, with
execution behaviour explicitly unexamined.

Agree a useful investigation boundary and next use. State which activities or
capabilities deserve depth, what access is available, and the conditions for
stopping or expanding the investigation. Existing explicit direction can settle
these matters. Return to the human when findings suggest a consequential scope
change; continue ordinary investigation within the agreed boundary.

Resolve an authorised output location and working record. A small assignment can
use `REFERENCE_SPEC.md` and `INVESTIGATION_RECORD.md`. Keep existing conventions
where they serve the work. Record actual instruction and workflow origins,
source identities, the assignment, and permitted operations. Inspection does
not authorise implementation or unrestricted operation of the reference system.
Use disposable examples for experiments that change state, within actual access
and permission boundaries.

HELPS_HUMANS normally leads the full interpretation and design conversation.
A participant in another active role applies the method within its brief and
returns coordination needs to its caller; selecting this workflow does not
change the participant's role. Keep one owner of the assembled account.
Bounded observations, code traces, comparisons, and checks may be assigned to
TASK where delegation is available and useful; retain
their briefs, supplied sources, returns, and limits. TASK does not delegate.
Arrange sustained investigation orchestration through WORKING_ITEMS when needed,
preserving the human's direction and integration responsibility.

## Discover connected capabilities

Begin with representative things someone can accomplish. Follow a connected
activity from its initial conditions to its useful result. For a service or
library, examine callers, exchanges, and resulting state. For an interactive
application, examine user actions and the information or state they affect.

Build a provisional map of capabilities, important objects, and relationships.
Use navigation, documentation, demonstrations, or code to discover further
possibilities, then examine the ones relevant to the purpose. A menu inventory
can help locate behaviour but does not establish its meaning or completeness.

Record coverage as work proceeds: what was examined, mentioned by a source but
not exercised, inaccessible, or deliberately outside scope. A missing control or
unsuccessful attempt does not establish that a capability is absent. Check whether
version, role, configuration, or starting state explains the difference when it
matters to reconstruction.

## Investigate the behaviour that matters

For each consequential capability, establish as far as the available evidence
allows:

- who or what uses it, for what purpose, and under which starting conditions;
- the inputs, objects, relationships, actions, outputs, and state transitions;
- persistence, ownership, interfaces, and dependencies on other capabilities;
- meaningful boundary cases, interruptions, errors, and recovery;
- operating conditions and qualities that affect whether the result is useful.

Choose questions whose answers could change the reconstructed account. Where
practical, design a small experiment that distinguishes competing explanations:
state the question, setup, action, observation, and limit of the result. Change
one relevant condition at a time when that helps isolate the cause. Record
enough context for another participant to repeat or inspect the evidence.

Use source code and tests to trace consequential mechanisms when available.
Identify the examined revision and whether it corresponds to the running
product. Code paths, tests, documentation, and observed execution can disagree;
investigate the discrepancy rather than silently choosing one account. A test
definition is distinct from a recorded passing execution.

Do not infer numerical guarantees from a single successful example. Preserve
the conditions of any measured behaviour. Keep inaccessible behaviour and
unsettled explanations visible while continuing useful work elsewhere.

## Express the reference specification and develop departures

Translate findings into a readable account of capabilities and behaviour. Give
consequential statements stable references and an evidence route. Distinguish
direct observations, documented claims, code findings, supported inferences,
and unresolved questions. Explain important relationships in the body so a
reader can understand the software without reconstructing it from an evidence log.

Describe behaviour at the level needed for a new design. For example, an observed
folder sidebar may reveal a capability to organise persistent objects. Further
investigation is needed to establish whether membership is exclusive, whether
moving an object changes its identity, and what happens to existing references.
Retain interaction details that explain consequential behaviour or
distinguishing qualities; record separately whether the human wants to
preserve them.
Do not assume that a visible arrangement reveals the underlying architecture.

The [worked example](resources/worked-example.md) shows how a connected
behavioural account can retain evidence, unknowns, and proposed departures.
Use it when an illustration helps; its structure is not a required template.

Bring the emerging account back into conversation throughout the work. Offer a
concrete scenario, alternative, or discrepancy; invite the human's reaction;
identify which distinction their response changes; revise the account and the
next investigation accordingly. Understanding the reference and developing new
intent can proceed together.

Keep a separate account of desired departures: what the human wants to preserve,
change, extend, or omit; why; its source and decision status; and what it depends
on. Agent suggestions remain proposals until adopted. A defect or restriction
in the reference can inform a choice without becoming a required feature.
Preserve the original finding when the desired outcome differs from it.

## Check the account and establish its useful limits

Walk representative scenarios through the assembled specification. Check that
the described objects, state changes, interfaces, and outcomes fit together.
Look for contradictions, capabilities named without behavioural meaning, hidden
assumptions, and gaps that would force a future designer to guess consequential
behaviour. Trace statements back to their actual sources.

Have consequential findings independently checked against original evidence by
a competent human or a separately prepared agent that did not author those
findings. Scale the coverage to the proposed reliance. Supply the actual source
and candidate rather than only the author's interpretation. Preserve the checked
revision, coverage, findings, and limitations. Author self-checks do not establish
independence; an unavailable check remains an explicit outstanding obligation.

Repair supported errors and backcheck affected relationships. Put consequential
unresolved choices before the human in a concrete form. Separate a defect in the
account from uncertainty in the reference and from a desired change to the new
product; each calls for different work.

The useful stopping point is reached when the agreed scope is described well
enough for the intended next design activity and the remaining uncertainty is
explicit. State which gaps prevent that next use and which can be carried with
an owner and a condition for resolution. Do not claim exhaustive reconstruction
from a limited sample or replace this judgment with a feature-count score.

State whether the account is ready for the agreed next use, a useful partial
return, or awaiting a required check. Identify unreviewed consequential claims
and the reliance that remains unresolved. When a reviewer is unavailable,
return the supported account with the outstanding obligation. Exploratory use
may carry a clearly identified question forward; do not present its answer as
established or imply that the required check occurred.

## Return and continue

Return the reference specification, evidence locations, coverage and unresolved
work, review results, and the separately identified departures. Identify the
exact document revision and reference-product basis. The human examines what
can be relied upon and decides the next undertaking. Record the actual decision,
its scope, and conditions separately from agent recommendations.

PRD development can consume this account alongside other product intentions and
evidence. Carry forward the accepted choices and unresolved questions without
silently promoting the entire reference specification into new requirements.
Further investigation may be requested as the product design develops. Follow
existing authorisation for continuation; this method itself does not authorise
implementation or create an automatic downstream launch.

Before interruption, retain completed observations, current files, decisions,
open questions, review coverage, and the next useful investigation. On resumption,
inspect actual files and source availability. When the reference version or
candidate changes, preserve prior evidence and reopen the affected claims and
decisions. If access is lost, return the supported partial account with its
specific limitations. A stopped or partial investigation remains a valid return.
