# Project Management for Human–Agent Teams

Field Book

Follow the route from intended result to delivery. Enter an existing project at its verified position. Apply the method within the project's accepted instructions, decision rights, and working conditions.

The [full manual](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md) supplies the explanations and examples. The [Chirality Agent User Manual](CHIRALITY_AGENT_USER_MANUAL_v3.md) supplies repository application and source links.

## 1. The project route

```text
Intended result and constraints
              |
Accepted project basis
              |
Packages, deliverables, and production contracts
              |
Dependencies and project execution order
              |
Selected undertaking and current work graph
              |
Produce -> check -> review -> repair -> integrate
              |                    ^
Close the records ----------------+  if required work remains
              |
Complete the undertaking
              |
Examine the produced product -> correct and re-examine
              |
Authorise delivery and transfer responsibility
```

| Position | Establish before advancing |
|---|---|
| Conceptual | Intended outcome, users, scope, constraints, and an accepted project basis. |
| FEED — front-end engineering design | Accepted division into packages and deliverables; workspace and coordination arrangements. |
| 30% — execution definition | Local production contracts, evaluation arrangements, dependencies, and an initial project directed acyclic graph (DAG). |
| 60% — detailed development | Developed design and interfaces; an execution route for which further structural changes are no longer anticipated. |
| 90% — produced deliverables | Intended contributions integrated, records reconciled, and an identified product ready for concentrated examination in use and debugging. |
| 100% — delivery | Applicable acceptance and delivery decisions completed; identified product delivered with its limitations and continuing responsibilities. |

Percentage labels describe development positions. They do not measure effort, code, or tasks completed. Testing accompanies development throughout. Parts of a project may occupy different positions.

At a stage gate, present what has been established, what remains unresolved, what the next work would rely on, and the proposed continuation. The human decides whether to advance, qualify, redirect, or require further work.

Reference: [Manual §1.7](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_7).

## 2. Responsibilities and information

| Participant | Responsibility |
|---|---|
| Human | Establish intent and constraints; decide consequential choices, accepted commitments, reliance, and delivery. |
| Alignment agent — Type 0 | Maintain alignment and continuity with the human; coordinate managers and connected undertakings. |
| Design manager — Type 1 | Develop the project basis, alternatives, interfaces, and proposed methods with the human. |
| Execution manager — Type 1 | Organise the undertaking; commission contributions; coordinate, examine, and integrate returns. |
| Executor — Type 2 | Complete one bounded assignment and return its result, evidence, limitations, and unresolved matters. |

Use only the roles and instances the work needs; a small undertaking need not instantiate the full hierarchy.

The corresponding Chirality role names are HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS, and TASK. A Type 2 executor does not delegate. A role specifies responsibility; a workflow specifies a method; the brief bounds this assignment; the host determines actual capabilities.

Carry routine work forward within existing authority. Bring decisions reserved to the human as concrete choices with evidence and consequences. An agent's capability does not confer approval authority.

Information passes through these records:

| Record | Carries |
|---|---|
| Project basis | Intended outcome, requirements, constraints, exclusions, and accepted open questions. |
| Decomposition | Scope allocation, package objectives, deliverable identities, and responsibility. |
| Deliverable production contract | Required outputs, criteria, interfaces, examination methods, and expected evidence. |
| Dependency records and project DAG | Required contributions, suppliers, consumers, and production order. |
| Current work graph | Selected execution, prerequisites, findings, results, integration, and continuation. |
| Artifacts and evidence | What was produced and what was observed on identified versions. |
| Decisions | Who decided what, for which content and scope, under what conditions. |
| Local memory | Terse references to work performed and its central records. |

Read the project through four views as needed: **tree** for composition, **production graph** for sequence, **source and decision network** for relevant relationships, and **attention** for the material needed to resolve the present question.

Keep project stage, deliverable lifecycle, task completion, and acceptance distinguishable. Each describes a different condition.

References: [Manual §§1.6–1.9](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_6), [§4.3](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_4_3).

## 3. Establish the basis

1. State the result sought, its users, and the activity it must support.
2. Identify scope, constraints, governing sources, interfaces, exclusions, and acceptance responsibilities.
3. Investigate uncertain matters that affect the next decision. Keep prototypes and proposed solutions identifiable.
4. Write the product requirements document (PRD), design basis memorandum (DBM), or corresponding project basis.
5. Check its coverage, consistency, sources, and unresolved questions. Repair and recheck the assembled candidate.
6. Present the identified document for acceptance. Record the actual decision and the conditions on proceeding.

A requirement states a needed result or constraint. An assumption remains an assumption after permission to proceed on it. A proposal becomes an accepted commitment only through the applicable decision. Missing information stays visible as an unresolved matter.

For each open matter, record its consequence, owner, required resolution, and the work it limits. Decide which matters prevent the next phase and which can remain open under stated conditions.

**Result:** a usable accepted basis, with a definite scope and an accountable treatment of unresolved matters.

References: [Manual §§2.1–2.7](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_2_1), [§§2.9–2.11](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_2_9).

## 4. Define the work and its order

### Allocate the scope

Give each scope item one accountable package home. Define deliverables with stable identities, complete responsibilities, and usable boundaries. Several deliverables may contribute to one objective. A bounded assignment can contribute to a deliverable without becoming another deliverable.

Check that the division covers the accepted scope without omissions or duplicated responsibility. Obtain the applicable acceptance, then prepare the working locations and coordination records. Preserve existing work and identifiers.

### Define production and examination together

For each deliverable, state:

- Its contribution and required outputs.
- Governing requirements, constraints, interfaces, and sources.
- Acceptance criteria and the methods used to examine them.
- Expected evidence and the people or agents responsible for each examination.
- Excluded acts and the receiving responsibility for any obligation carried elsewhere.

Map **output → requirement or criterion → examination → evidence → decision**. Keep claims at the level the project needs to preserve; cite incidental implementation details as evidence.

### Establish the dependencies

For each relationship, identify the supplier, consumer, required contribution, point of need, source, and present satisfaction. Distinguish a relationship defining the product from one imposing production order.

Check the inventory and source coverage before analysing topology. Report unreadable registers, unresolved targets, exclusions, and missing relationships. An acyclic selection can still be incomplete or incorrectly stated.

Resolve cycles according to their actual meaning:

| Move | Required treatment |
|---|---|
| Decompose | Separate contributions that need different inputs or can be established at different times; preserve their combined scope. |
| Invert | Introduce or refine a contract that supports the revised dependency direction. |
| Merge | Make the coupled work one accepted unit, with combined inputs, responsibility, and examination. Human decision required. |
| Cut | Establish that the relationship falls outside the graph's stated objective; retain its other consequences. Human decision required. |

A grouped cycle still contains work whose order needs resolution. Excluding an unresolved relationship from a graph does not supply its missing input. Hold the dependent work; continue separately authorised investigation and independent work.

Establish the initial project DAG before the 30% gate. Preserve its objective, node inventory, relationship meaning, source revisions, exclusions, examination, and decisions. Dependencies may remain pending within an accepted DAG.

**Result:** identified production commitments and a defensible order for developing them.

References: [Manual §§3.1–3.8](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_3_1), [§§3.9–3.12](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_3_9), [§5.5](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_5_5).

## 5. Carry an undertaking through to completion

Use one current work graph to carry the selected undertaking across assignments and sessions. Link it to the affected deliverables and project dependencies. The project DAG describes production relationships; the work graph organises the work now selected.

### 1. Orient and recover

Read the human's steering and the accepted basis. Compare the current graph with actual revisions, local and unmerged work, evidence, open decisions, holds, and active operations. Verify that earlier work was integrated before repeating it. Confirm that previous workers have stopped or transfer ownership before reassigning their files or resources.

### 2. Construct or revise the route

State the intended result and completion conditions. Give each work node an output, prerequisites, owner, write boundary, examination, and place in integration. Include needed investigations and decisions.

Prepare one planned final documentation and governance closeout after the intended implementation and evidence have been integrated. Documents and reconciliations needed to perform or constitute an earlier contribution travel with that contribution.

Renew the project DAG when its governing relationships change. A new conversation or rearranged assignment alone does not require a successor DAG.

### 3. Commission ready work

Supply each executor with a bounded brief:

| Brief field | State |
|---|---|
| Purpose | Required contribution and its place in the undertaking. |
| Basis | Identified sources, candidate, requirements, and accepted decisions. |
| Context | Material needed for this assignment and where to retrieve it. |
| Authority and tools | Permitted operations, actual capabilities, and reserved decisions. |
| Write scope | Exact targets and protected boundaries. |
| Return | Outputs, checks, evidence, limitations, and destination. |

Keep shared writes under one owner. Control shared interfaces, applications, test fixtures, and other resources. Parallel work requires both usable inputs and compatible working conditions. Size concurrency to the team's capacity to examine and integrate returns.

### 4. Produce, examine, repair, and integrate

Perform the work against its governing basis. Use deterministic tools for operations they can reliably perform. Preserve the actual inputs, candidate, relevant observations, and limitations.

Verification examines conformity to specified requirements. Validation examines fitness for the intended use. Exercise connected behavior and the relevant environment as well as component behavior.

Review the identified contribution independently where required. Diagnose findings, repair within authorised scope, and recheck affected behavior. Preserve the meaning and independence of acceptance criteria and reference results during repair.

Integrate against the actual receiving state and examine the combined behavior. Update the graph at meaningful returns. Repeat this step while required production work remains.

### 5. Close the records

After intended implementation and evidence integration, compare both directions:

- **Commitment to result:** locate the output and evidence for each applicable obligation.
- **Result to commitment:** account for implemented behavior and changed interfaces against accepted scope.

Correct affected claims and records. If required implementation or evidence is missing, return it to execution and repeat the affected comparison after repair. A closed node or merged contribution does not itself trigger a separate formal reconciliation pass.

Keep work already allocated to the current graph or an identified successor there. Consider Task Management intake only for a material, evidenced concern without such a home. Record its owner and condition for reconsideration; preserve human authority over promotion and disposition. A transfer or deferral does not satisfy an unmet requirement.

Add terse local memory entries: **run and date; work performed; links to the central evidence, decisions, and integration record**. Keep detailed decisions at their authoritative sources and future execution in its owning graph.

### 6. Complete the undertaking

Confirm that the result meets the stated completion conditions. Record what was achieved and the actual disposition of remaining obligations. In a software undertaking using pull requests, close the records before the final PR; perform required checking and review, then merge under the applicable authority. The PR and Git record establish the merge when it occurs.

Preserve the completed graph and its relationship to the result. Report completion at the undertaking's scope. A new objective requires new steering; completing this undertaking does not by itself accept or release the product.

References: [Manual §1.10](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_10), [§§4.1–4.11](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_4_1), [§§5.2–5.8](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_5_2).

## 6. Examine the produced result

### Establish the candidate's position

Account for three forms of coverage:

| Coverage | Establish |
|---|---|
| Scope | Applicable outputs and production obligations are fulfilled. |
| Relationships | Required interfaces and dependencies have been exercised or otherwise examined on a supported basis. |
| Evaluation | Required methods were applied to the identified candidate; evidence supports the claimed extent. |

For entry to formal frozen-candidate checking, establish that no applicable production obligation remains unfulfilled within the proposed scope. An empty graph or work list is not this account. Required production checks precede freezing; the planned formal examination remains ahead.

The human decides the checking basis and proposed reliance. During formal checking, hold the candidate's claims fixed and record findings separately. A necessary correction returns through the authorised production process and produces a candidate for the appropriate re-examination.

### Examine the product in use

Define the activity, starting state, candidate, environment, expected behavior, and observations to retain. Exercise the connected user or consumer journey. Examine resulting state, persistence, errors, and recovery where relevant.

An agent may operate suitable scenarios under human direction. Arrange practitioner examination where the question or governing criterion requires it. A substitute environment or automated scenario supports only the behavior it actually exercises.

For a defect: preserve the observation, reproduce it, identify the cause, apply a bounded repair, review it, and repeat affected examination. Reopen dependent evidence when its basis changes.

Present the exact candidate, supported conclusions, unresolved limitations, and requested decision. Keep production completion, formal checking, human acceptance, and publication distinct.

References: [Manual §§5.9–5.14](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_5_9).

## 7. Treat exceptions at their source

| Condition | Action |
|---|---|
| Required information is absent | Mark the gap, identify its consequence, and assign investigation or a decision. Do not fill it with an unsupported value. |
| Sources conflict | Identify the competing claims and their standing; prepare a proposed treatment and its consequences for the authorised decision-maker. |
| A prerequisite is unavailable | Hold dependent production. Advance work whose inputs and authority are sufficient. |
| The implementation fails its requirement | Diagnose and repair the implementation; retain the governing criterion. |
| Evidence is absent or applies to an older candidate | Obtain the required examination on the applicable candidate; qualify earlier claims. |
| A description is stale | Check whether it states an enduring commitment or incidental mechanism. Repair the claim at the appropriate level and link the implementation evidence. |
| Scope or an accepted interface must change | Prepare the amendment and impact assessment; obtain the decision and propagate it through affected contracts, dependencies, graphs, work, and evidence. |
| Work has no current or successor home | Arrange conditional intake, ownership, and reconsideration without silently changing the obligation. |
| A session is interrupted | Preserve actual state, active operations, ownership, blockers, and next action. Recover these against reality before resuming. |
| A project is reduced, suspended, or ended | Record the actual outcome, changed commitments, retained work, and decisions about continuing responsibilities. |

Reopen only the decisions and checks whose basis or consequences are affected. Preserve valid work and historical evidence. A changed instruction or shared source takes effect in another undertaking through its applicable adoption arrangements.

References: [Manual §1.9](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_9), [§§4.7, 4.11](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_4_7), [§§5.6, 5.10, 5.13](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_5_6).

## 8. Deliver and hand over

1. Join the organisation's established delivery procedure and identify the person authorised to accept and release the result.
2. Bind the decision to the actual product, version, scope, purpose, and conditions.
3. Prepare and verify the package that the recipient will receive, including required instructions and supporting records.
4. State known limitations, exclusions, unresolved obligations, and the decisions governing them.
5. Transfer ownership of support, operation, maintenance, recovery, and future changes. Identify where the recipient can find the applicable records.
6. Record what was actually delivered and how it relates to the original or amended objectives.

A useful handover identifies **the result, its basis, its permitted use, its limitations, its next responsible owner, and the means of recovery**.

Reference: [Manual chapter 6](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_6).
