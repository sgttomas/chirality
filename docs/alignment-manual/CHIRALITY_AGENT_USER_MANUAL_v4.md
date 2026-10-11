# Chirality Agent User Manual

## Working in the current repository

Edition 4

This guide is for people directing agents and agents carrying out authorized development in `sgttomas/chirality`. It applies the general management method to current repository files and tools. It is not the user manual for the App product, a release authorization or an additional instruction layer.

Root `AGENTS.md`, the active project's `LOOP_INIT.md`, the conversation and applicable current product commitments govern the work. This guide explains their use. If it conflicts with them, identify the conflict and repair the guide; do not reinstate an obsolete procedure.

The [Field Book](Project_Management_for_Human_Agent_Teams_Field_Book_v2.md) is the short management reference. The [management manual](Project_Management_for_Human_Agent_Teams_Consolidated_v9.md) explains the method and its reasons. Use the stable [manual index](README.md) to discover current editions. Record a specific edition when the exact source matters.

## 1. Select the active work

The conversation supplies the intended result, scope and authorization. A new session does not cancel prior direction or prove that earlier work is complete. Recover the relevant unfinished work before replacing it.

| Scope | Repository-relative entry | Current use |
|---|---|---|
| Root | `execution/_Coordination/LOOP_INIT.md` | Shared instructions, workflows, skills, tools, CI and reference documents, as steered. |
| App v4 | `projects/chirality-app-v4/loop/LOOP_INIT.md` | The current App and application-host integration work. |
| SWBPIPE | `projects/chirality-piping/loop/LOOP_INIT.md` | Piping design and stress-model authoring. |
| Frozen products | `projects/FROZEN.md` | Historical recovery of App v3, Runtime and PEC; no development or verification without explicit reactivation. |
| Domain engines | Owning instructions under `_DomainEngines/` | Work only under a steer covering that scope. |

Resolve the checkout before using paths. A linked worktree has its own root. The following observations do not change files:

```sh
git rev-parse --show-toplevel
git status --short --branch
git rev-parse HEAD
```

Read Root `AGENTS.md`, the project entry and the active role when a role is selected. Then locate the affected deliverable or shared component. Read the PRD and companions for the requirements and interfaces involved, rather than reading the entire governance history.

A useful first return identifies the work already available, the next authorized step and any specific missing input. Do not reconstruct a standing backlog from archived plans.

## 2. Use roles as contributions

Agent 0's responsibilities stay with the agent working with the owner: purpose, continuity and reserved choices. Other roles are opportunities to contribute, not mandatory stops.

| Role | Useful contribution |
|---|---|
| HELP_HUMAN | Align the undertaking with the owner and maintain continuity. |
| HELPS_HUMANS | Develop conception, design and concrete alternatives. |
| WORKING_ITEMS | Carry implementation through repair and integration. |
| TASK | Complete a bounded assignment; does not delegate. |

One session may work directly across alignment, design and implementation. Delegate where independent contributions or a separation of concerns help. Give each contribution enough context and authority to continue through ordinary repairs.

HELP_HUMAN is no longer inherently read-only. In Root's resolver, write targets come from an explicit normalized assignment and effective tool policy. Missing write authorization grants no targets. A read-only host still wins. A role never grants actual host permissions.

TASK remains non-delegating even when a host offers delegation tools. It returns opportunities for further decomposition to its caller. Its assignment may be the conversation; a separate brief file is not inherently required.

Use the host's actual dispatch and return mechanism. Do not equate a prepared prompt, queued message or completed turn with delivered work. Return result locations, checks and unresolved matters without creating a separate record unless one is needed.

## 3. Work from the deliverable

Active project deliverables use `execution/PKG-nn/DEL-nn-nn/`.

| Source | Purpose |
|---|---|
| `ScopeOfWork.md` | Contribution, commitments and acceptance criteria. |
| `Design/` | Useful technical detail, interfaces and current technical decisions. |
| `deliverable.yaml` | Required inputs and conditions, relevant code paths and check references. |
| Code, fixtures and tests | Implementation and executable examination. Their maintained location need not be the deliverable folder. |
| PR and Git history | What changed, why, what was checked and what remains open. |

There is no routine deliverable lifecycle file or Working/Issued split. Do not recreate `_STATUS.md`, MEMORY rows, dependency mirrors or progress registers. Existing historical files remain evidence of earlier arrangements, not templates for new work.

Edit the current source when its meaning changes. A new commitment or changed acceptance criterion remains reserved for the owner unless already authorized. Apply an authorized decision without asking for the same approval again. A factual repair should not silently narrow a commitment.

The deliverable is the unit of responsibility, not an exclusive code ownership boundary. Several deliverables can use the same code. State those relationships where useful without inventing exclusive ownership.

## 4. Query dependencies

Run the deliverable CLI from the repository root. It requires Python 3 and PyYAML. The CLI reports JSON and does not maintain a generated register.

```sh
python3 -m tools.deliverables --project projects/chirality-app-v4 neighborhood DEL-07-02
python3 -m tools.deliverables --project projects/chirality-piping neighborhood DEL-04-01
```

| Command | What it establishes |
|---|---|
| `neighborhood <DEL>` | Declared direct inputs and consumers. |
| `impact <DEL>` | Declared downstream reach, including non-gating relationships. |
| `touches <rev or PR:n>` | Relevant deliverables for changed code paths; missing mappings remain visible. |
| `dag-diff <tag>` | Declaration changes against a baseline revision. |
| `check` | Structural errors, unresolved references and reported cycles. |

A single Git revision supplied to `touches` means that commit's changes, not the difference between that revision and the working tree. A PR reference requires authenticated `gh` access. The [CLI README](../../tools/deliverables/README.md) defines the supported forms and current limits.

Each need identifies a supplier and a condition. Optional fields describe timing, gating and evidence. The consumer maintains its needs; reverse links are derived. Update unchanged rows only when their meaning actually changes.

A present file proves presence, not suitability. A merge proves integration, not acceptance or fulfillment. The agent must inspect the relevant condition and evidence. The tool does not infer that a test passed or a deliverable is complete.

`check` rejects malformed metadata and escaping paths. It reports unresolved suppliers, planned paths and cycles without treating them as automatic failures. Missing edges do not prove independence. Examine shared interfaces, code and resources before dividing work.

A baseline tag supports comparison and recovery. It does not approve every future dependency change. Ordinary changes do not require a new tag or a currency packet. Preserve actual owner holds and specific adopted acceptance requirements.

## 5. Carry the work through

The common working cycle is:

1. Establish the objective, scope and actual starting state.
2. Locate affected commitments, inputs and consumers.
3. Work directly or arrange useful bounded contributions.
4. Produce, examine, repair and integrate the result.
5. Update current sources when meaning changes.
6. Return the usable result and unresolved reserved choices.

Use [coordinated knowledge work](../../workflows/coordinated-knowledge-work/WORKFLOW.md) when related contributions must become one result. It supports direct work as well as delegation. It does not prescribe a fixed staffing diagram.

Keep one integration responsibility for a shared result and disjoint concurrent writes. Independent work need not wait for an unrelated branch. Shared memory, tools, application state, review capacity and integration cost can still require sequencing.

Prove a consequential interface through its consumer before expanding work that depends on it. Continue independent work while that premise is examined. Component agreement does not prove the common basis is correct.

Resolve ordinary implementation refinements within authority. Escalate changes to commitments, consequential shared assumptions, interfaces outside the assignment or reserved choices. Identify the affected work and the consequence of each choice.

A final documentation stage is not compulsory. Keep documents current as their meaning changes. Before completion, establish coverage of commitments, relationships and applicable examination. Add work only where a required claim remains unsupported.

## 6. Select proportionate verification

Root's rule is consequence-based:

| Change | Typical verification |
|---|---|
| Routine and reversible | Inspection or direct exercise. |
| Ordinary implementation | A focused check of the affected behavior. |
| Numerical meaning, persistence, permissions or destructive operations | Targeted regression checks and independent scrutiny by a separate agent. |
| Release | Examination of the actual product; release remains reserved. |

Do not alter a criterion merely to obtain a pass. Establish whether the source requirement, test or implementation is wrong. Preserve protected oracles and meaningful limits unless their owner authorizes a substantive change.

The single required GitHub result is `harness`. It combines repository checks and selected App v4 and Piping jobs. App v3, Runtime and PEC have no verification jobs. See [CI selection](../CI_SELECTION.md) for the maintained policy.

The aggregate fails when selected work fails, is cancelled or does not run. Unselected work is reported as unselected. A reused result names its earlier run and candidate; it does not claim new tests ran.

Do not repeat a passing hosted suite locally without a new change or unresolved concern. Check selection must cover actual consumers; an empty selection is not proof of safety.

For Root tools, inspect and then run the affected suite selection:

```sh
python3 tools/run_affected_tests.py --dry-run
python3 tools/run_affected_tests.py
```

For Piping, the profile selector accepts project-relative paths:

```sh
python3 tools/software_workflow/select_affected_checks.py projects/chirality-piping/software-workflow.json core/model_transform/physical_to_analytical/_solver_boundary_adapter.py
```

This command selects checks; it does not execute them. Piping's [CI strategy](../../projects/chirality-piping/docs/CI_STRATEGY.md) explains its current numerical, browser and Python coverage. DEC-025's blanket local sweep is not a merge requirement. The release sweep remains a separate optional release-preparation tool.

## 7. Integrate under the standing grant

For `sgttomas/chirality`, Root's standing Git grant covers commit, push, PR creation/update and merge within authorized work. It requires proportionate verification and passing required checks on the exact head. Independent scrutiny applies where consequence requires it.

The grant excludes protection bypasses, history rewrites, force pushes, permission changes and releases. Explicit holds remain effective. Use the [chirality-change skill](../../.agents/skills/chirality-change/SKILL.md) for branch and PR conventions.

The PR is the change record. State the problem, resulting behavior, checks and open matters. Quote the owner's words for a reserved decision without implying that the owner reviewed bytes they did not inspect.

Reassess affected checks after candidate changes. A review of an earlier revision does not automatically cover later edits. A passing rerun does not establish that a known defect was repaired.

Merge is a source-control operation. It does not issue a deliverable, approve engineering reliance or release a product. The actual integration must be confirmed before it is reported as complete.

## 8. Enter App v4 and SWBPIPE correctly

### App v4

Start at the [App v4 loop](../../projects/chirality-app-v4/loop/LOOP_INIT.md), then the affected deliverable. The App is a workflow-authoring exemplar and a basis for agent functions inside host applications.

Use [app/README.md](../../projects/chirality-app-v4/app/README.md) for current build and test entry points. Product role guidance and embedded workflows are separate consumers of Root sources; changes require an applicability assessment and valid source binding, not automatic copying.

The project entry defines scratch Codex homes, credential restrictions, download permissions and thesis protection. This guide does not relax them. An existing documented exception applies only within its actual authorization.

### SWBPIPE

Start at the [Piping loop](../../projects/chirality-piping/loop/LOOP_INIT.md), then current ScopeOfWork, Design and needs. The product is an analysis-grade piping design engine and stress-model authoring environment.

The loop carries F-PIP-1–4 and DEC-043. Those project boundaries remain authoritative. This guide does not restate or amend their held wording. In particular, the external corpus's extracted equation artifacts must not become authoritative physics references.

Frozen numerical references live in `validation/references/t3_r1/`. Their generators and consumers remain maintained. Do not modify reference results to make an implementation pass.

Product operations, professional acceptance and repository development are different activities. Removing development records does not remove a required product event, model history, stop/checkpoint record or user decision.

## 9. Preserve continuity without rebuilding history

Use current artifacts, tool queries, the conversation and PRs first. Keep one replaceable recovery note only when they cannot support continuation.

A useful recovery note distinguishes prepared work from executed changes, known results from pending checks, active operations from stopped ones, and local-only work from integrated work. It identifies the next useful action and material holds.

Inspect actual state before replaying an operation whose confirmation was lost. A new session does not release another worker's files or resources. Transfer ownership or confirm the operation stopped before assigning overlapping work.

Historical material remains available through Git and archive tags. [Frozen products](../../projects/FROZEN.md) explains recovery of retired product trees. Restoring files does not reactivate a product or its old procedures.

When removing a worktree, establish that its commits are preserved and that no unique local work or active operation will be lost. Ignored files are not protected by commit history. Keep necessary recovery material outside the active project; do not publish private session data.

## 10. Create and select methods

Use the role needed for the contribution, not a new permanent specialist for each subject. Select relevant workflows and load resources as needed. Root's `workflows/index.json` supports discovery.

Follow [create-workflow](../../workflows/create-workflow/WORKFLOW.md) when creating or revising a reusable method. A workflow describes a reusable approach; the current assignment supplies scope and authority. A workflow does not grant permissions or require an orchestration hierarchy.

For a Root package change, rebuild the index and check the affected behavior:

```sh
python3 tools/validation/build_workflow_index.py
python3 tools/validation/build_workflow_index.py --check
```

The first command writes the generated index. The second checks its currency. Product discovery and registration behavior is defined by adopted product contracts, not by this repository guide.

## 11. Use current pointers without losing source identity

The manual index has stable anchors for the management manual, Field Book and this guide. Those links answer “where is the current edition?” They do not answer “which edition supported this earlier decision?”

For ordinary discovery, use the stable index. When a requirement, comparison or accepted result depends on exact wording, identify the resolved edition and source revision. Existing Git provides the bytes; add a content hash only when a consumer requires one.

A changed index does not automatically amend App v4's product requirements or historical test fixtures. Update affected current consumers deliberately. Preserve the earlier edition while a live consumer still requires its bytes.

A source update can change language without changing meaning, or change the actual method. Compare the relevant sections and consequences. Do not substitute a new edition merely because its version number is higher.

## 12. Three practical cases

### A small reversible correction

The owner asks for a clearer message in the App. The agent finds the actual interface and its requirement, changes the text and exercises the affected state. It checks whether wording could misrepresent a permission or data operation. If not, ordinary proportionate verification is sufficient. It does not create a graph, run record or new management assignment.

### A consequential numerical change

The owner authorizes a bounded numerical repair. The owner of that work reads the current Design conditions and queries affected consumers. It checks the independent numerical reference and keeps parallel writers disjoint. An independent reviewer examines the substantive change. The agent runs affected checks, updates any changed condition in its current source, and integrates the reviewed candidate under the grant. A changed accepted tolerance goes to the owner instead of being silently adopted.

### Recovery after interruption

A check was started, but its final response was lost. The next session inspects the actual process and result location before running it again. It checks the working tree and current PR head. Valid completed work remains usable. A short recovery note is replaced with the current situation if one is still needed; no new handoff chain is created.
