# Project Management for Human Agent Teams

## Field Book

Edition 2

This field book helps a person direct work with agents. It identifies the next useful question, action or decision. It does not prescribe a fixed team, a universal approval sequence or a set of administrative records.

The [management manual](Project_Management_for_Human_Agent_Teams_Consolidated_v9.md) explains the reasoning and develops examples. The [operational guide](CHIRALITY_AGENT_USER_MANUAL_v4.md) applies the method in the Chirality repository. The [manual index](README.md) identifies current editions. An edition used for an accepted decision remains identifiable even when the current edition changes.

## 1. Start from the intended result

Establish what the person needs to be able to do, for whom, and under which conditions. Distinguish the desired result from a proposed implementation. Ask which observations would support a conclusion that the result is usable.

For existing work, recover the relevant current basis before replacing it. Read the current artifacts and inspect the actual candidate. Use history to resolve a specific uncertainty, not to reconstruct every earlier activity.

A useful opening account contains the result, authorized scope, current position, next useful work and material unknowns. It may be a few sentences in the conversation. It need not become a separate brief file.

The recurring course is:

```text
Understand the result and current basis
                 |
Locate affected work, required inputs and consumers
                 |
Work directly or arrange useful contributions
                 |
Produce -> examine -> repair -> integrate
                 |
Update current commitments or conditions when their meaning changes
                 |
Establish the usable result and any reserved decision
```

Move through this course as the work requires. A missing input holds only work that depends on it. A completed step does not create a duty to write another record.

## 2. Keep responsibility clear

The agent working with the person carries Agent 0's responsibilities: purpose, continuity and preparation of reserved choices. Other roles are available contributions.

| Role | Contribution |
|---|---|
| HELP_HUMAN | Maintains the relationship between the person's purpose and the work. |
| HELPS_HUMANS | Develops conception, design, alternatives and their implications. |
| WORKING_ITEMS | Carries implementation through repair and integration. |
| TASK | Completes one bounded contribution and does not delegate. |

One session can perform substantial work without delegation. A role is not a required staffing position. The assignment and host permissions determine allowed actions; a role does not grant tools or write access.

When delegating, give a contributor a coherent result to own through ordinary repairs. Identify the relevant basis, write boundary, checks, return location and matters requiring another decision. Use the conversation or existing assignment rather than a mandatory form.

Keep one integration responsibility for a shared result. This does not require one agent to perform every operation. It identifies who will examine how the contributions fit and carry the combined result to use.

## 3. Establish a sufficient basis

A useful basis states the intended result, requirements, constraints, interfaces, exclusions and acceptance responsibilities. It distinguishes commitments from proposals and assumptions.

Preserve the four perspectives:

- **Ontology:** what the work contains and how its parts relate.
- **Epistemology:** what supports its claims and where support is missing.
- **Praxeology:** how contributions become a usable result.
- **Axiology:** which purposes, values and consequences matter to the choices.

These are questions for understanding. They do not require four separate documents or four approval rounds.

Record a settled commitment where it governs the work. Keep an unresolved matter with its consequence, required input and point of need. A decision to proceed with uncertainty does not convert an assumption into a fact.

A scope change, reliance decision or release can require the person's judgment. Routine implementation choices within granted authority do not need renewed approval. Present a reserved choice with its alternatives, consequence and recommendation; prepare the actual candidate before asking for its acceptance.

## 4. Define contributions and relationships

Give each deliverable a stable identity and a complete responsibility. Avoid splitting work merely to create more assignments. Distinguish the deliverable, the working unit and the integration batch.

A production contract identifies the contribution, outputs, governing constraints, acceptance criteria, interfaces and methods of examination. The representation can vary. It must let a producer and a receiver establish what is required without inventing missing commitments.

The consumer states what it needs from another contribution and when it needs it. State the condition, not only the supplier's name. A path match, present file or merged PR does not prove the input is suitable.

Tools can derive upstream and downstream relationships from those declarations. Use the relevant neighbourhood to find inputs, consumers and opportunities for concurrent work. Missing edges do not prove independence. Check shared interfaces, write targets and resources where they matter.

Cycles require interpretation. Mutual design can proceed through coordinated iterations. An execution cycle may require a staged contract, changed boundary or owner decision. Do not remove a necessary relationship merely to make a diagram acyclic.

Keep finer implementation relationships where their consumers can use them. Add machine-readable detail when an actual query needs it. Do not maintain a second progress graph merely to repeat the source state.

## 5. Arrange useful progress

Independence is an opportunity for concurrent progress. Do not hold independent work behind an unresolved branch. Consider shared writes, memory, review capacity and integration cost when choosing concurrency.

Test a consequential premise through a usable path before expanding work that depends on it. Independent work can continue. An early path should exercise a difficult interface or assumption, not only an easy isolated component.

| If this is uncertain | Establish this next |
|---|---|
| What the person wants | A concrete interpretation or alternative the person can inspect. |
| Whether an input is suitable | The relevant condition and evidence from the input or its consumer. |
| Whether components work together | An actual connecting operation and its resulting state. |
| Whether a contributor is progressing | The last actual operation, partial result or host completion state. |
| Why work is waiting | The specific input, decision, resource or integration step that releases it. |

Use host mechanisms for dispatch and returns. A queued message does not prove execution. A completed turn does not prove all assigned work was delivered. Account for dispatched work without requiring separate return files.

Keep owners with their work through findings. Transfer ownership at a clear boundary when continuation is not possible. Preserve valid output and inspect uncertain operations before repeating them.

## 6. Examine the claim that matters

Verification asks whether the result meets specified requirements. Validation asks whether it serves the intended use. Different claims require different evidence.

A schema check can establish structure. A source comparison can establish fidelity. A numerical oracle can test a defined calculation. A user exercise can reveal whether an interaction is usable. None automatically establishes the others.

Match assurance to consequence and detectability. Routine reversible work may need inspection or direct exercise. Numerical meaning, persistence, permissions and destructive operations commonly need targeted regression checks and independent scrutiny. Applicable professional, contractual and project requirements still govern.

Do not change an expected result solely to obtain a pass. Establish whether the requirement, test or implementation is wrong. Escalate a reserved change while continuing unaffected work.

Identify the actual candidate and the conditions examined. Reuse valid evidence when those conditions still apply. Repeat affected checks when a change or unresolved concern warrants it, not because another stage or agent now handles the work.

Before completion, examine three questions:

1. Does the result cover the applicable commitments?
2. Do the required relationships and interfaces work together?
3. Does the evidence support the claim and proposed use?

An empty task list is not an answer. A separate closeout stage is unnecessary when current work and evidence already establish the answers.

## 7. Keep current information, not an activity history

Maintain the authoritative artifacts when a commitment, design or dependency condition changes. The change record explains the reason and identifies unresolved consequences. Version control preserves earlier text.

A record needs a concrete consumer, an acceptance requirement or a recovery need. A useful record can be a required test result, a decision with material conditions, or the identity of a candidate proposed for release. Its form follows its purpose.

Do not prescribe routine receipts, memory rows, reading logs, copied source or handoff chains. Product records required by the application or its users are a different matter; reducing development administration does not remove those requirements.

At an interruption, keep one replaceable recovery note if current artifacts and the conversation are insufficient. Identify prepared versus executed work, pending checks, active operations, local-only work and the next useful action. Do not repeat an operation whose completion is uncertain until its actual state has been inspected.

## 8. Use development positions as questions

Conceptual, FEED, 30%, 60%, 90% and delivery positions can help explain how work changes. They are not measurements of tasks, code or effort completed.

| Position | Question |
|---|---|
| Conceptual | Is the intended outcome understood well enough to choose a basis? |
| FEED | Are scope, contribution boundaries and principal interfaces sufficiently defined? |
| 30% | Are production commitments, required inputs and examination methods usable? |
| 60% | Are the consequential design and integration premises established well enough to expand dependent work? |
| 90% | Is the assembled result ready for its remaining concentrated examination? |
| Delivery | Are acceptance, release and continuing responsibilities established for the identified result? |

An undertaking can combine positions or revisit an affected part. This guide neither creates stage gates nor cancels adopted ones. A project that has a human gate still brings that gate to its decision owner.

At a 60% assessment, explain developed interfaces, unresolved coupling, proposed work grouping and residual risks. Do not weaken designs to eliminate cycles. Do not continue analysis indefinitely when a usable integration path can answer the consequential question. The applicable owner decides qualifications or changes to commitments.

## 9. Finish and transfer responsibility

Completion concerns the agreed result and its applicable evidence. Acceptance and release remain distinct acts. State what is usable, which conditions were checked and what remains unresolved.

For delivery, identify the actual artifact, revision, permitted use, limitations and continuing owner. Exercise the package or transfer path the receiver will use where that is necessary to establish delivery.

A handover needs enough information for the receiver's work. It does not require a fresh narrative of the project. Keep necessary operational instructions, recovery information and accepted limitations with the delivered result.

Continue improving the method from actual work. Look for repeated discovery, avoidable waiting, duplicate checks, delayed integration and defects that escape. Use existing evidence to assess comparable completed work. Do not create another reporting system merely to demonstrate efficiency.
