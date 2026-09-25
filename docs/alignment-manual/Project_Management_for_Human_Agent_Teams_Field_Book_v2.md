# Project Management for Human–Agent Teams

Field Book

This is the short form of the manual. It follows a project from what someone wants to the thing delivered, and says at each step who does what and what to keep on record. Keep it beside the work as a checklist. The [full manual](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md) explains the reasons, with examples, and the [Chirality Agent User Manual](CHIRALITY_AGENT_USER_MANUAL_v3.md) shows how it is done in the Chirality repository.

If you join a project already under way, find out where it actually stands before doing anything. The project's own instructions and decisions come first; this book does not replace them.

## 1. What the method rests on

**People decide; agents do the work.** A person sets the aim, makes the choices that matter, and decides what to rely on and what to deliver. Agents can do a great deal within that, but being able to do something is not permission to approve it.

**Agents' work is checked before it is relied on**, as you would check work from anyone else.

**The record lets someone else pick the work up.** Another person or agent should be able to see what was decided, what was made, what was checked, and what is left.

Reference: [Manual, Preface](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#h_preface).

## 2. The route

```text
What is wanted, and the limits on it
        ↓
An accepted basis: the requirements document
        ↓
The work divided into deliverables, each with a contract
        ↓
The order the deliverables depend on each other: the project graph
        ↓
A piece of work selected, with its own plan: the work graph
        ↓
Make → check → review → fix → merge      repeat while work remains
        ↓
Bring the records up to date with what was made
        ↓
Test the product in use; fix, and test again
        ↓
Deliver, and hand over responsibility
```

The route passes through six stages. A stage gate is where a person decides whether the work is ready to go on.

| Stage | Ready to go on when |
|---|---|
| Concept | The aim, users, scope and limits are written down, and the basis is accepted. |
| FEED (front-end engineering design) | The work is divided into packages and deliverables, and the workspace is set up. |
| 30% | Each deliverable has a contract saying what it must produce and how it will be checked, and the dependencies form a first project graph. |
| 60% | The design and interfaces are worked out, and no further change to how the work is divided is expected. |
| 90% | The work is made, merged and recorded, and one identified version is ready to test in use. |
| 100% | The people with authority have accepted it, and it has been delivered with its limits and with someone responsible for it. |

The percentages mark positions, not effort. Parts of a project can be at different stages, and testing goes on throughout, not only at the end.

At each gate, show the person deciding what is settled, what is not, what the next stage would rely on, and what you propose. They decide whether to go on, go on with conditions, change direction, or ask for more work.

Reference: [Manual §1.7](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_7).

## 3. Who does what

| Role | Chirality name | What it does |
|---|---|---|
| The person | | Sets the aim and the limits; makes the decisions that matter; decides what to rely on and what to deliver. |
| Alignment agent | HELP_HUMAN | Works with the person directly, keeps the work in line with what they want, and keeps it going from one session to the next. |
| Design manager | HELPS_HUMANS | Works out the basis, the options and the interfaces with the person. |
| Execution manager | WORKING_ITEMS | Plans a piece of work, hands out its parts, and checks and merges what comes back. |
| Executor | TASK | Does one bounded job and reports the result, how it was checked, and what is unresolved. It does not hand work on. |

Use only the roles the job needs. On a small job, one agent can do several.

Agents carry routine work forward on their own. When a decision belongs to the person, the agent brings it as a concrete choice: the options, the evidence, and what follows from each.

Reference: [Manual §§1.8, 4.3](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_8).

## 4. What to keep on record

| Record | What it holds |
|---|---|
| Basis (PRD or DBM) | What is wanted, the requirements and limits, what is excluded, and the open questions that have been accepted. |
| Decomposition | How the scope is split into packages and deliverables, and who is responsible for each. |
| Deliverable contract | What the deliverable must produce, how each part will be checked, and the evidence expected. |
| Project graph | What each deliverable needs from the others, and so the order of the work. |
| Work graph | The plan for the piece of work under way: its steps, who owns each, and where each stands. |
| Evidence | What was checked, on which version, and what was seen. |
| Decisions | Who decided what, about what, and on what conditions. |
| Memory | One line for each run of work, pointing to the records above. |

Keep four things apart: the project's stage, a deliverable's state, a job being finished, and something being accepted. Finishing a job accepts nothing.

Reference: [Manual §§1.6–1.9](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_6).

## 5. Agree the basis

1. Write down what is wanted, who it is for, and what it has to do.
2. Note the scope, the limits, the sources that govern it, its interfaces, and what is excluded.
3. Look into anything uncertain that affects the next decision. Keep prototypes labelled as prototypes.
4. Write the basis: a product requirements document (PRD), a design basis memorandum (DBM), or whatever the project uses.
5. Check it. Does it cover everything? Is it consistent? Does each claim have a source? What is still open? Fix it and check again.
6. Put it to the person for acceptance, and record what they decided and on what conditions.

Keep what is required, what is assumed, and what is only proposed apart. Permission to proceed on an assumption does not make it true. Leave gaps visible rather than filling them with guesses. For each open question, note what it affects, who owns it, and whether it must be settled before the next stage.

Reference: [Manual §§2.1–2.11](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_2_1).

## 6. Divide the work and put it in order

**Divide the scope.** Give each part of the scope one home, in one package. Name each deliverable and draw its boundaries. Check that together the deliverables cover the whole scope, with nothing missing and nothing done twice.

**Write each deliverable's contract.** Say what it must produce, the requirements and interfaces it answers to, how each will be checked, and what evidence will show it. Keep the chain in view: output, requirement, check, evidence, decision.

**List the dependencies.** For each, say who supplies what, to whom, and when it is needed.

**Break any loops.** Where dependencies go round in a circle, treat the loop according to what it actually means:

| Move | When to use it |
|---|---|
| Split | The work needs different inputs at different times; divide it, keeping all of its scope. |
| Reverse | A contract between the two pieces can let the dependency run the other way. |
| Merge | The two pieces cannot be separated; make them one piece of work. The person decides. |
| Cut | The dependency is outside what the graph is for; set it aside and keep track of it. The person decides. |

Draw the project graph (a directed acyclic graph, or DAG) before the 30% gate. It can include dependencies not yet met. A graph without loops can still be missing something, so check that every source was read.

Reference: [Manual §§3.1–3.12](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_3_1).

## 7. Carry a piece of work through

Each piece of work gets one work graph, which carries it across sessions and agents. The project graph says what depends on what; the work graph plans the work now in hand.

**1. Find out where things stand.** Read the person's direction and the basis. Compare the work graph with the actual files, unmerged work, evidence and open decisions. Don't redo work that is already merged, and make sure anyone who worked on it before has stopped before you take over their files.

**2. Plan the route.** Say what finishing means. Give each step an output, what it needs first, an owner, the files it may change, and how it will be checked. Plan one update of the records at the end.

**3. Brief each job.** Give each executor a brief:

| Brief | Says |
|---|---|
| Purpose | What the job is for, and where it fits. |
| Basis | The sources, requirements and decisions it works from. |
| Context | What it needs to know, and where to find it. |
| Permissions | What it may do and use, and what is reserved for the person. |
| Files | Exactly what it may change, and what it must not touch. |
| Return | What to hand back: the result, the checks, the evidence and the limits. |

Give each shared file one owner, and let only that owner change it. Run only as many jobs at once as you can check and merge.

**4. Make, check, review, fix, merge.** Verification asks whether the work meets its requirements; validation asks whether it is fit for use. Test how the parts work together, not only each part alone. Have the work reviewed independently where that is required. Fix what the review finds, within the brief, and check again. Never weaken a test or a reference result to make the work pass. Merge into the actual current state, test the result, and repeat while work remains.

**5. Bring the records up to date.** Check both ways: every obligation has its output and evidence, and everything built answers to something in scope. Correct the records. If something required is missing, send it back to step 4. Add a line to memory.

**6. Finish.** Check that the finishing conditions are met. Record what was done, what is left, and where the rest has gone. In software, update the records before the final pull request, then review and merge it. Finishing a piece of work does not accept or release the product.

Putting work off does not meet a requirement. If a real problem has nowhere to go, record it with an owner and a time to look at it again; the person decides what becomes of it.

Reference: [Manual §§4.1–4.11, 5.2–5.8](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_4_1).

## 8. Test the product

**Freeze a version.** Before formal testing, show that nothing required is left undone; an empty to-do list does not show it. Then hold the version fixed while it is tested, and record findings separately. A fix goes back through the work and produces a new version to test.

**Test it in use.** Define the task, the starting state, the version, the environment, what should happen, and what to keep. Follow a user's path from start to end, including saving, errors and recovery. An agent can run scenarios under the person's direction; bring in a practitioner where the question needs one. A simulated environment shows only what it actually exercised.

**Fix defects one at a time.** Keep the observation, reproduce it, find the cause, make a narrow fix, have it reviewed, and test again.

**Ask for the decision.** Present the exact version, what the evidence supports, what is still limited, and the decision you need.

Reference: [Manual §§5.9–5.14](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_5_9).

## 9. When something goes wrong

| Situation | What to do |
|---|---|
| Information is missing | Mark the gap and what it affects, and give someone the job of finding out or deciding. Don't fill it with a guess. |
| Sources disagree | Set out the competing claims and propose a way through; the person with authority decides. |
| Something needed isn't ready | Hold the work that needs it; carry on with work that doesn't. |
| The work fails its requirement | Fix the work, not the requirement. |
| Evidence is missing or out of date | Check again on the current version, and qualify the old claims. |
| A document is out of date | Decide whether it states a commitment or only describes how something works, and correct it at that level. |
| The scope or an agreed interface must change | Prepare the change and its effects, get the decision, and carry it through everything affected. |
| A session is cut off | Record where things stand, what is running, who owns what, and the next step. Check that against the actual state before resuming. |
| The project is cut back, paused or stopped | Record what happened, what changed, and who is responsible for what remains. |

Reopen only what the change affects, and keep the work that is still good.

Reference: [Manual §§1.9, 4.7, 5.10](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_1_9).

## 10. Deliver and hand over

1. Follow the organisation's delivery process, and find the person who can accept and release the result.
2. Tie their decision to the exact product, version, scope, purpose and conditions.
3. Prepare and check what the recipient will receive, including instructions and records.
4. State the limits, the exclusions, and anything unresolved.
5. Hand over support, operation, maintenance and future changes, and say where the records are.
6. Record what was actually delivered, against what the project set out to do.

A good handover says what the result is, what it rests on, what it may be used for, its limits, who is responsible for it now, and how to recover it.

Reference: [Manual chapter 6](Project_Management_for_Human_Agent_Teams_Consolidated_v7.md#ch_6).
