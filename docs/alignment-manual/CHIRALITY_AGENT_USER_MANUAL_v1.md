# Chirality Agent User Manual

Version 1 · 22 September 2026 · repository source basis `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`

An operational companion to [*Project Management for Human–Agent Teams, Consolidated v2*](Project_Management_for_Human_Agent_Teams_Consolidated_v2.md), for agents developing projects in the Chirality repository. Authored from the supplied [Consolidated v1](Project_Management_for_Human_Agent_Teams_Consolidated_v1.md) and the repository comparison recorded for this edition.

**Status:** explanatory documentation. This manual supplies navigation, working explanations, and illustrative examples. It does not amend instructions, adopt a workflow, activate project work, change a lifecycle state, accept a product, or authorize release. Follow the actual human direction, applicable adopted instructions, selected method, brief, and host permissions. Recheck the linked live sources when using a later checkout. The dated project crosswalk below is a reading of this source basis, not a standing report of current project status. [Root entry][root-entry] · [Runtime contract][runtime-contract]

## Contents

1. [Use the guide at the right scale](#use-the-guide)
2. [Enter or resume an undertaking](#entry)
3. [Choose responsibilities and execution resources](#roles)
4. [Read paths, records, and authority](#records)
5. [Understand the development route](#phases)
6. [Form the basis, decompose, and set up](#formation)
7. [Work from deliverable contracts](#deliverables)
8. [Read dependencies and resolve cycles](#dependencies)
9. [Construct and traverse a local work graph](#local-graph)
10. [Commission and coordinate bounded work](#delegation)
11. [Implement, verify, review, and integrate](#implementation)
12. [Reconcile the records with the result](#reconciliation)
13. [Handle decisions, change, and unresolved concerns](#change)
14. [Enter Chirality App development](#app)
15. [Enter Piping development](#piping)
16. [Enter Runtime development](#runtime)
17. [Enter PEC development](#pec)
18. [Recover, hand off, and close an undertaking](#recovery)
19. [Create or improve reusable methods](#authoring)
20. [Worked operational examples](#examples)
21. [Source map and terminology](#sources)

<a id="use-the-guide"></a>

## 1. Use the guide at the right scale

Begin with the result the human wants and the undertaking already in progress. Determine whether the assignment is project formation, an existing project's development, a bounded maintenance change, an inquiry, or separately authorized Root governance work. These can share tools and records without sharing every stage or checkpoint. A small authorized documentation correction does not require a new PRD, a new decomposition, a project-wide dependency audit, or a replacement work graph. A new product with unsettled scope needs more basis work before production can be meaningfully bounded. [Root entry][root-entry] · [WORKING_ITEMS][working-items]

Use the human-facing manual for the management argument: establish intent, make the basis usable, organize contributions, examine them, preserve their consequences, and deliver an identified result. Use this guide to find the repository instruments that implement those ideas. Use the owning project's live entry to decide what applies now. The human manual deliberately distinguishes examples, proposals, and supplied source snapshots; a method described there does not become operational merely by being described. [Human manual, preface and source notes][human-manual]

Three questions keep the work proportional:

1. **What decision or operation is next?** Read enough to support it, including consequential inputs and downstream effects.
2. **What could make its result unusable?** Select the checks, review, and evidence that detect those failures.
3. **What must another participant recover?** Preserve the basis, actual outcome, remaining obligations, and next safe action without duplicating the entire history.

This is a working aid, not another mandatory form. Root explicitly permits ad hoc plans and ordinary conversational briefs. A workflow is optional unless the assignment or an accepted instrument requires it; creating or revising a reusable workflow is the important exception, discussed in [section 19](#authoring). An agent may act and make routine choices within clear authorization. It should prepare consequential human decisions, rather than multiply prompts for each tool result or harmless implementation detail. [Root entry][root-entry] · [Create a workflow][create-workflow]

Keep four distinctions visible throughout the work:

| Distinction | Operational consequence |
|---|---|
| Description and authority | A report of what code does cannot replace an accepted requirement. |
| Preparation and execution | A launch brief proves that instructions were prepared; an actual child record establishes that work ran. |
| Evidence and acceptance | A passing check supports a bounded claim; the applicable human act governs acceptance. |
| Source integration and release | Commit, push, PR, and merge concern Git state; none independently issues a deliverable or publishes a product. |

These distinctions are grounded in the [invariant catalog][contract], [delegation decision D-GOV-35][dgov35], and [Chirality change conventions][chirality-change]. They allow extensive autonomous preparation and execution while preserving the decisions the human has retained.

The common route in this guide applies across project types. The exact product, source boundaries, domain constraints, checks, and adoption state remain local. In particular, current App and Piping use a selected local work graph; Runtime and PEC retain different continuation rules. Do not export one project's newest loop into its siblings without their adoption. [App loop][app-loop] · [Piping loop][piping-loop] · [Runtime loop][runtime-loop] · [PEC loop][pec-loop]

<a id="entry"></a>

## 2. Enter or resume an undertaking

Resolve the checkout before interpreting paths. A linked worktree has its own `REPO_ROOT`; a path copied from another session may point to a different checkout. Establish the project and active role, read the applicable entry instructions, and recover the current undertaking before creating replacement work. Only then decide which deeper records and methods are needed. [SPEC §0.2][spec] · [Root entry][root-entry]

The following shell block is a read-only orientation example for an agent with shell access. It does not fetch remote state or execute project gates. Select the real project folder; `chirality-app-dev` is only the example value.

```sh
REPO_ROOT="$(git rev-parse --show-toplevel)"
WORKING_ROOT="$REPO_ROOT/projects/chirality-app-dev"
git -C "$REPO_ROOT" status --short --branch
git -C "$REPO_ROOT" rev-parse HEAD
git -C "$REPO_ROOT" worktree list
cat "$REPO_ROOT/AGENTS.md"
cat "$REPO_ROOT/agents/AGENT_HELP_HUMAN.md"
cat "$WORKING_ROOT/AGENTS.md"
cat "$WORKING_ROOT/loop/LOOP_INIT.md"
```

A HELP_HUMAN instance whose effective ceiling does not permit shell execution asks an authorized actor to perform the Git observations or uses available read capabilities. The presence of a shell example never changes that ceiling. Record a tool or permission gap accurately rather than claiming that the displayed commands ran. [Role registry][registry] · [Runtime contract][runtime-contract]

For an existing project, recover five things before dispatch: the intended outcome and latest steering; the live authority and accepted basis; the continuation cursor selected by the project; the actual code/file state; and the active ownership of files and shared resources. A completed child may have left an unmerged patch. An interrupted test may still own an application window. A current pointer can name an ongoing governed program whose phase rules are narrower than ordinary development. [App loop][app-loop] · [Piping loop][piping-loop] · [Runtime loop][runtime-loop] · [PEC loop][pec-loop]

For App and Piping, read the graph selected by `loop/LOOP_INIT.md`, then any linked phase cursor, owner direction, and handoff. Compare material statements with the branch, working tree, named unmerged worktrees, and referenced evidence. Preserve useful completed results. A missing graph target is a recovery problem; it is not equivalent to a pointer deliberately set to `none`. A completed graph stays selected until a successor undertaking is chosen. [App loop][app-loop] · [Piping loop][piping-loop]

For Runtime, start with migration acceptance and the authority/decomposition pointers, then `execution/_Coordination/HANDOFF_STATE.md` and the newest loop receipt. For PEC, perform its prescribed discovery and re-derive selectable work from deliverable Remaining sections, gates, and exact ruled packets. Neither project inherits App/Piping's removal of routine receipts. [Runtime loop][runtime-loop] · [PEC loop][pec-loop]

A useful first return is short but decisive: “The selected undertaking is X, based on Y. The working tree contains Z. A is ready within the current scope; B waits for the named owner act. I will continue with A and preserve B.” Where no lawful production activation exists, identify the useful readiness preparation already authorized and the exact decision that blocks production. Avoid describing a missing input as a blanket inability to investigate or prepare. [WORKING_ITEMS][working-items] · [Runtime loop][runtime-loop]

An illustrative launcher for the current App entry is:

```text
Resolve REPO_ROOT with git rev-parse --show-toplevel.
Set WORKING_ROOT to {REPO_ROOT}/projects/chirality-app-dev.
Read {REPO_ROOT}/AGENTS.md and agents/AGENT_HELP_HUMAN.md.
Act as HELP_HUMAN for WORKING_ROOT.
Read the project AGENTS.md and loop/LOOP_INIT.md.
Recover the selected undertaking and follow its live authority.
Steer for this run: continue the authorized verification work;
retain all existing holds and return any design-changing finding.
```

The wording illustrates an assignment, not a reusable workflow or current owner instruction. Substitute the actual project and steering. Do not treat a blank steer as cancellation of existing directions, or a new conversation as release of a pause. Where continuing intent is genuinely unclear, first recover enough state to make the human's choice concrete. [Construct a local work graph][construct-graph] · [HELP_HUMAN][help-human]

<a id="roles"></a>

## 3. Choose responsibilities and execution resources

Chirality has four standing roles. A role describes a contribution, a workflow describes a method, a brief describes this assignment, and the host supplies actual capabilities. Do not create an expanded permanent roster merely because the work has many specialties. Put the specialty in the bounded assignment and its context. [Root entry][root-entry] · [Role registry][registry]

| Role | Type | Use it for | Required relationship |
|---|---:|---|---|
| HELP_HUMAN | 0 | Alignment, continuity, cross-undertaking coordination, and preparing consequential choices with the human. | Coordinates managers and may directly dispatch a bounded Type 2 contribution. |
| HELPS_HUMANS | 1 | Conceiving and designing projects, workflows, tools, and their boundaries. | Returns a sufficiently understood design and open questions for implementation; may delegate bounded execution. |
| WORKING_ITEMS | 1 | Organizing implementation, assigning bounded work, checking interfaces, and integrating the undertaking. | Owns the combined result; returns design-changing findings through the human or HELP_HUMAN. |
| TASK | 2 | One bounded contribution under its brief and selected method, if any. | Returns work, evidence, and coordination needs to its caller; does not delegate. |

Read the [active role instruction][registry], not every role body on routine entry. Wider consultation is appropriate for comparison or coordination when needed, with origins and hashes recorded in governed evidence. A fresh named child receives the intended full role and its bounded brief. A full-history fork preserves context; it does not by itself establish a different role or a fresh independent reviewer. [Root entry][root-entry] · [Runtime contract][runtime-contract]

The registry gives HELP_HUMAN a read-only managed ceiling: `read`, `delegate_agent`, and `send_agent_update`, with `write_scope: none`. Its responsibility for continuity does not authorize direct file edits. Route graph maintenance, decision transcription, and other writes to an authorized recorder or manager with exact targets. A manager's own ceiling also does not grant unrestricted writes; its brief must supply them. [Role registry][registry] · [Runtime contract, structured brief compatibility][runtime-contract]

Native delegation needs equally accurate description. D-GOV-35 distinguishes Chirality-managed `delegate_agent` sessions from delegated-harness-native descendants. Native descent alone assigns no Chirality role, proves no non-delegation enforcement, and creates no acceptance authority. If the native host exposes broad tools while role and brief restrictions are instruction-asserted, report that fact. Never describe the host as mechanically enforcing a restriction merely because the agent followed it. Conversely, broad filesystem capability is not permission to exceed the assignment. [D-GOV-35][dgov35] · [Root entry][root-entry]

Choose the arrangement around coordination needs. A small read-only comparison may go directly from HELP_HUMAN to TASK. An undertaking with implementation, evolving inputs, repairs, review, and integration usually benefits from WORKING_ITEMS. Several independent scopes can share a manager; a problem spanning Packages can require one coherent undertaking. A Package does not automatically require its own manager, nor does a graph node require a separate agent. [HELP_HUMAN][help-human] · [WORKING_ITEMS][working-items] · [App project instructions][app-agents]

Model and reasoning settings are separate from role and Type. A difficult bounded review can require more capability than routine coordination. Consider the question, context, uncertainty, consequences, available checks, and total effort through repair and integration. Follow the current project convention and per-run steering; record actual model identity only when exposed by the host. App and Piping retain model allocation in run strategy and evidence, while PEC retains a distinct historical model convention that must be read in its own instructions. No role number is a capability ranking. [App execution attribution][app-agents] · [Piping execution attribution][piping-agents] · [PEC session convention][pec-agents]

<a id="records"></a>

## 4. Read paths, records, and authority

`REPO_ROOT` is the active checkout. `WORKING_ROOT` is the selected project or domain workspace. `INSTRUCTION_ROOT` is the runtime-declared shared instruction surface. `EXECUTION_ROOT` and other tokens resolve from the anchors defined in SPEC and the project. In-tree projects may read shared instructions outside their working root; those reads confer no permission to edit the shared surface. External v2 working repositories use a physically disjoint instruction root under their registration contract. [SPEC §§0.2–0.3][spec]

Normalize `ScopePath` and every write target to real absolute paths and verify containment in the authorized working root. Include generated files, evidence, caches with consequential effects, and helper outputs in the assessment. A symlink or `..` must not escape the boundary. Root instruction and governance maintenance is separately authorized work, not an ordinary project's side effect and not a revival of retired Root product execution. Durable instructions use anchors or relative paths; machine-absolute paths belong only in run evidence where they record actual execution. [SPEC §0.2][spec] · [CONTRACT K-WRITE-2][contract] · [DIRECTIVE §2.6][directive]

Use each record for the kind of truth it owns:

| Record | Use | Do not infer |
|---|---|---|
| Human ruling and decision register | Exact accepted choice, subject, conditions, and publication/adoption requirements. | A tracking row or agent transcription is itself a fresh ruling. |
| PRD and accepted decomposition | Purpose, scope, objectives, allocation, identity, and accepted boundaries. | Every aspirational PRD sentence is an activated implementation tranche. |
| `ScopeOfWork.md` or valid active legacy kit | The deliverable's production target and evaluation relationships. | Current code overrides an unsatisfied requirement. |
| `_STATUS.md` | Canonical lifecycle and, where adopted, current Remaining obligations. | Lifecycle is a percentage or automatically changes when tests pass. |
| `Dependencies.csv`, `_DEPENDENCIES.md` | Local dependency declarations, identities, provenance, and satisfaction. | A central graph image is a substitute source of dependency truth. |
| Local work graph | Selected route, executable contributions, prerequisites, results, and recovery. | It creates scope, overrides holds, or accepts a phase. |
| Run evidence and snapshots | What was supplied, done, observed, checked, and accepted at an identified boundary. | Historical success establishes current success without checking intervening changes. |
| Memory, plans, summaries, maps | Context, reasons, navigation, and historical explanation. | They supersede the current authority or select work contrary to the adopted loop. |

The source-of-truth rules are in [CONTRACT][contract], [SPEC][spec], and the [concordance method][concordance]. A useful index leads back to those records. It is acceptable to use search, a graph projection, or a generated status report to locate them; it is not acceptable to silently promote the projection into authority.

Read status statements at their actual scope. A source may be ratified Root governance, a prospective interface authorized for implementation, a project adoption record, a candidate implementation, or frozen historical evidence. The shared runtime-contract header carries a prospective/adoption qualification; establish each consumer's actual adoption from its owning records and later scoped acts. The current decomposition standard identifies its v3 grouped-checkpoint amendment as prospective and names the earlier ratified edition. A visible latest file is therefore not sufficient evidence that an active project has adopted its procedure, and an older header does not cancel a later accepted adoption. [Runtime contract][runtime-contract] · [Decomposition standard][decomp-standard]

Use the four project views proportionately. The tree locates the work and its identity; the production graph shows required relationships; the source/decision network exposes warrants and supersession; the attention view gathers what matters for the present question. Follow a reference when its meaning affects the next operation. There is no standing requirement to construct all four views or scan the entire repository. Git ancestry locates revisions; it does not prove production dependence. [Root entry][root-entry]

When sources disagree, identify the actual contradiction, their status and revisions, the work affected, and the decision needed. Continue independently authorized work whose basis is sound. Do not resolve a live authority conflict by choosing whichever text is easiest to implement, newest by timestamp, or closest to the current directory. [CONTRACT K-CONFLICT-1][contract] · [Concordance method][concordance]

<a id="phases"></a>

## 5. Understand the development route

The human manual describes a six-part route: conceptual work, FEED, 30%, 60%, 90%, and 100% delivery. These names explain how the character of the work changes. They are not arithmetic measurements, automatic software statuses, or a requirement to restart every phase when maintaining an established project. Enter the verified current position and reopen only decisions whose basis or consequences have changed. [Human manual §§1.7, 4.12, 5.11–6][human-manual] · [Root entry][root-entry]

| Phase in the explanatory route | Work emphasized | Useful basis for the next undertaking |
|---|---|---|
| Conceptual | Align intent, understand the product, identify constraints, develop the PRD or appropriate basis document. | Identified accepted direction, clear unresolved questions, and a usable basis for division. |
| FEED | Decompose accepted scope and prepare the project workspace and production contracts. | Stable identities, scope coverage, usable deliverable definitions, and declared coordination. |
| Work toward 30% | Establish the means of execution, declare dependencies, examine coupling, resolve ordering, and construct the first usable objective-relative DAG. | The accepted graph basis, resolved or explicitly held coupling, and an executable route. |
| Work toward 60% | Develop technical details and interfaces through local undertakings; revise the project graph when warranted by scope/decomposition change. | A clearer route to completion with sufficiently developed relationships and recorded design decisions. |
| Work toward 90% | Carry the details into produced deliverables over longer horizons, integrate, reconcile, verify, and account for residual work. | An identified candidate and evidence for concentrated product examination. |
| After 90%, toward 100% and delivery | Move from produced deliverables into concentrated product examination and debugging, then into the organization's 100% publication/delivery pipeline. Testing has also occurred throughout earlier development. | Delivered identity, continuing obligations, recipient information, and the applicable human acts. |

This table is an explanation of the [human manual][human-manual], not a new gate definition. A real project can have uneven maturity: one interface may be settled while another Package still needs design. Do not force all deliverables into the same maturity claim or assume that closing a local undertaking advances the project. Stage gates remain human-managed milestones under the project's own records. [SPEC §3.3][spec] · [TYPES §5.2][types]

Deliverable lifecycle is a separate axis. The shared sequence is `OPEN → INITIALIZED → SEMANTIC_READY → IN_PROGRESS → CHECKING → ISSUED`, with the semantic step optional where inapplicable. The state says which production and change-control regime applies; it does not report “60% complete.” Read `_STATUS.md` and the adopted transition rules, including any project-specific semantics. [SPEC §3][spec]

Where the concordance lifecycle applies, `IN_PROGRESS` is the honest state whenever warranted open work remains. Entry to `CHECKING` needs warranted-empty Remaining, a candidate-specific checking basis, and a human declaration freezing the candidate. Evidence must support the emptiness. Removing list entries or closing all known graph nodes cannot prove that no obligation was omitted. During checking, append review evidence to the appropriate records rather than editing frozen claim surfaces. A required correction returns through the human-authorized reversal; `ISSUED` changes use governed scope change. [SPEC §3.4][spec] · [Concordance §4][concordance]

The practical distinction matters in reports. “Implementation and focused regression checks complete; native recovery witness remains” is a useful assignment result. It is not a declaration that the deliverable is ready for checking. “The PR merged” identifies source integration. It is not professional acceptance or publication. “The graph is complete” concerns the graph's stated undertaking and conditions. Its scope may be much smaller than a project milestone. [Chirality change conventions][chirality-change] · [Construct a local work graph][construct-graph]

Delivery likewise follows an actual arrangement, not a universal invented final workflow. Identify the recipient, delivered version, accepted scope, required packaging or transmittal, verification, operational responsibilities, and remaining obligations from the project. Prepare the package before seeking the reserved release or acceptance act. Preserve a prior authorized release as history without inferring authority for another. [Human manual, chapter 6][human-manual] · [App development boundaries][app-agents] · [Root entry][root-entry]

<a id="formation"></a>

## 6. Form the basis, decompose, and set up

For a new undertaking, HELPS_HUMANS helps turn intention into a concrete account the human can inspect. Identify the product, intended users, purpose, conditions of use, constraints, required outcomes, interfaces, exclusions, and open choices. Preserve the distinction between the human's commitment and the agent's interpretation. A PRD should be clear enough to support its next use; it need not pretend every technical question has been answered. Label uncertainty and explain what would resolve it. [HELPS_HUMANS][helps-humans] · [Human manual, chapters 1–2][human-manual]

Prepare a source map before substantial drafting. For each significant statement, establish what the source may support: a governing requirement, an accepted decision, observed behavior, a proposed direction, or background explanation. Read the actual source where its meaning matters. A title, search result, extracted snippet, or old summary may identify the material without establishing the claim. Keep unresolved conflicts visible instead of blending incompatible positions into confident prose. [DIRECTIVE §§2.4–2.5][directive] · [CONTRACT K-PROV-1, K-INVENT-1, K-CONFLICT-1][contract]

The human manual describes a software PRD method and grouped decisions, but this repository's catalog at the stated basis contains no registered `software-prd` workflow. Conduct PRD formation through the authorized design brief and adopted project method, or prepare a reusable method through `create-workflow` if explicitly asked. Do not claim that a described source-bundle method is installed, selected, or executed. Discovery comes from the effective catalog and actual package identity. [Workflow index][workflow-index] · [Runtime contract][runtime-contract]

Before decomposition, identify the accepted basis and exact applicable protocol. The repository contains `project-decomp` for project scope, `software-decomp` for software, and `domain-decomp` for knowledge domains. Their current packages express grouped checkpoints, while the current decomposition standard explicitly retains a prospective-status warning and identifies the earlier ratified edition. Use the project's adopted edition and recorded authority. Do not silently substitute the latest package into an in-flight accepted method. [Decomposition standard][decomp-standard] · [Project decomposition][project-decomp] · [Software decomposition][software-decomp] · [Domain decomposition][domain-decomp]

The practical decomposition work is to normalize scope, relate it to objectives, propose coherent flat partitions, define bounded production units and anticipated artifacts, and verify coverage. Preserve stable IDs. A Package boundary must express a useful responsibility, not merely a document chapter or temporary agent allocation. A deliverable should be small enough to understand and examine as a contribution while retaining the interfaces and work needed to make it usable. Do not invent scope to make an elegant tree or discard difficult items to make coverage appear complete. [Decomposition standard][decomp-standard] · [CONTRACT K-HIER-1, K-ID-1][contract]

Prepare the material before each required checkpoint: proposed basis or structure, source mappings, coverage results, ambiguous allocations, exceptions, and a recommendation. The human decides an inspectable package. A deterministic finding normally routes correction within authorized preparation; it does not independently create another human gate. Conversely, a passed ledger validator cannot accept the meaning or boundary of the decomposition. [Root entry][root-entry] · [Project decomposition][project-decomp]

After acceptance, `project-setup` inspects the existing workspace, accepted decomposition, coordination representation, and selected activation scope. It can coordinate scaffolding, production contracts, semantic work, dependency extraction, and other selected setup stages. Existing partially completed setup is recovered from what actually exists. Use accepted choices already in the coordination record rather than asking the human to repeat them. The workflow does not justify running every optional pipeline. [Project setup][project-setup] · [Setup contract][setup-contract]

The `preparation` skill is structural. It creates accepted folders and source-faithful control files idempotently, preserves pre-existing paths, and reports exactly what was created or skipped. An existing empty file is still existing work. Missing accepted metadata is a missing input, not an invitation to supply plausible scope. Production text belongs to its own bounded stage. New PROJECT/SOFTWARE deliverables use `scope-of-work` initialization; legacy four-document examples in older setup resources do not authorize new legacy production. [Preparation skill][preparation] · [Setup contract][setup-contract] · [Scope-of-work workflow][sow-workflow]

Coordination mode is consequential. `NOT_TRACKED` means dependency coordination occurs outside the files: report no computed ready/blocked judgment from an incomplete graph. `DECLARED` means the recorded critical edges are a partial view. `FULL_GRAPH` means declarations are intended to cover the selected graph semantics, with closure and cycle treatment needed before computing its blockers. A dependency graph is also not automatically a schedule: scheduling needs its own accepted basis, duration posture, calendar, and hard/soft relationship rules. [Setup contract][setup-contract]

<a id="deliverables"></a>

## 7. Work from deliverable contracts

Locate a deliverable through its stable ID and accepted decomposition, then read the current production format and control records. At `INITIALIZED` or later, PROJECT/SOFTWARE production has exactly one valid canonical format: a valid `ScopeOfWork.md`, or the complete retained four-document kit under the authorized legacy transition. Both complete formats are a temporary isolated migration state only with exact migration authority; they are not a normal accepted baseline. Partial or invalid production is a concrete defect to report. [SPEC §2][spec] · [Scope-of-Work standard][sow-standard]

The Scope-of-Work standard's activation is conditional on D-GOV-16. Its recorded owner ruling approves the exact successor standard and transition, while retaining implementation and migration boundaries. This illustrates how to read a conditional header: follow the named act, then determine the applicable project adoption and source state. Do not infer a blanket conversion mandate from the schema's availability. [D-GOV-16][dgov16] · [Scope-of-Work standard][sow-standard]

Read `ScopeOfWork.md` as a production contract. It connects the deliverable's contribution to project scope and Package objectives; defines outputs and behavior; states requirements and completion criteria; names production and verification methods; records governing decisions; and binds these through the Output and Evaluation Matrix. Its philosophical labels help distinguish the questions each section answers. They do not substitute for concrete requirements and evidence. [Scope-of-Work standard §§3–5][sow-standard]

| Identifier | Meaning | How it is used |
|---|---|---|
| `OUT-*` | Expected output | Locate the artifact or behavior and the scope/objective it serves. |
| `CLM-*` | Descriptive claim | Examine the stated condition and its warrant. |
| `REQ-*` | Requirement | Preserve the obligation when implementation falls short. |
| `AC-*` | Acceptance criterion | Retain exact identity and wording in compiled review material. |
| `VER-*` | Verification method | Establish which examination addresses the criterion. |
| `AX-*` | Governing value, rationale, or authority constraint | Follow the decision or constraint that governs choices. |
| `TBD-*`, `CON-*` | Unresolved information or conflict | Assign investigation or obtain the owning decision. |
| `REM-*` | Remaining item | Keep it in `_STATUS.md`, linked to the production target. |

These IDs are local to one contract. For a cross-deliverable reference, use a qualified citation such as `DEL-01-02/REQ-003`; the slash spelling is canonical in the current workflow. The standard also retains the hyphen-qualified form. A bare `REQ-003` means the local contract's requirement and can silently misdirect a reader or parser when used for an upstream obligation. Preserve accepted IDs through edits. [Scope-of-work workflow][sow-workflow] · [Scope-of-Work standard §4][sow-standard]

Follow an output through its matrix rows into the required conditions, methods, and evidence expectation. Check the pairing, not only that every ID appears somewhere. The workflow permits grouped acceptance criteria only when each inherits the same verification-method set; a row that combines unrelated criteria and methods can falsely imply coverage. A boundary exclusion also needs an owner for the excluded acts and a cited claim carrying that ownership. “This deliverable does not do X” is incomplete if X remains necessary and nobody owns it. [Scope-of-work workflow][sow-workflow]

Compile review criteria with the registered deterministic checklist tool when the method calls for it. It retains source order, exact text, qualified identity, source location, contract hash, and the linked method or explicit human review. Do not create a second paraphrased acceptance namespace. The compiler establishes fidelity of the checklist; review establishes what the candidate supports, and the applicable human act establishes acceptance. [Scope-of-Work standard §§4, 10][sow-standard]

`_STATUS.md ## Remaining` records the current gap against the target where adopted. State the unsatisfied condition, affected contract reference, needed contribution, dependencies, and evidence that permits closure. Distinguish missing production, missing verification, an unresolved decision, and a documentation discrepancy. If a repair is complete but its backcheck remains, the obligation is still open at that extent. Removing an item requires support for its actual closure condition. [Concordance §§2, 4][concordance] · [Bounded reconciliation][bounded-reconciliation]

Keep control files separate. `_CONTEXT.md` preserves identity and decomposition traceability; `_REFERENCES.md` locates sources; dependency records state relationships; Memory provides useful rationale or continuation context. Read `_MEMORY.md` and any compatibility `MEMORY.md` according to what the folder actually uses. None independently changes scope or lifecycle. Do not recreate retired legacy production files while reconciling a converted deliverable. [SPEC §2][spec] · [Bounded reconciliation][bounded-reconciliation]

Format conversion is a special bounded operation. It preserves content and lifecycle, isolates the temporary dual format, maps source ranges, verifies parity, creates a clean finalized contract, and integrates an atomic replacement. Semantic changes are conflicts for their owning decision process. An `ISSUED` deliverable needs the separately specified human representation-replacement approval. The on-demand `ScopeOfWork.html` derivative is non-authoritative and is not tracked per deliverable. These rules do not prohibit a separately authorized documentation manual having its own HTML edition. [Scope-of-Work standard §§6–10][sow-standard]

<a id="dependencies"></a>

## 8. Read dependencies and resolve cycles

A dependency is a specific relationship supported by source evidence. Begin with the declared coordination mode and the graph objective. Build-order, runtime calls, information flow, deployment, and knowledge relationships are different semantics. A graph can be correct for one and misleading for another. Record the objective before treating arrows as ordering instructions. [Cycle-driven resolution §§1–3][cycles] · [Setup contract][setup-contract]

The local dependency records remain authoritative under K-DEP-1. Project DAGs and closure snapshots are approved or derived views for stated purposes; they do not create a second central dependency database. Inspect the selected project snapshot through its live pointer and verify its source basis. A newly opened session does not warrant rebuilding a still-current accepted DAG. Re-derivation is event-driven by decomposition revision or scope change under the doctrine and the project's adopted triggers. [CONTRACT K-DEP-1][contract] · [Cycle-driven resolution §4][cycles]

`dependency-extract` works locally in two passes: definition anchors to existing tree/requirement identities, then execution relationships. It produces `Dependencies.csv` and `_DEPENDENCIES.md`; it does not restructure decomposition or build the whole project graph. Preserve evidence location, stable row identity, direction, explicitness, confidence, extraction history, and fulfillment state. Unresolved targets remain `UNKNOWN` or `TBD`; do not manufacture a deliverable to make an edge resolve. [Dependency extraction][dependency-extract]

Read extraction status separately from satisfaction. `ACTIVE` means a relationship is currently observed; it does not mean fulfilled. `RETIRED` preserves a formerly extracted relationship; it is not a lifecycle state. `SatisfactionStatus` records whether the input remains pending, is in progress, is satisfied, or has another permitted disposition. An `IN_PROGRESS` dependency field is a different vocabulary from a deliverable's `IN_PROGRESS` lifecycle. Normalize legacy labels only under authorized writes and preserve their origin. [Dependency extraction][dependency-extract] · [SPEC §3.4][spec]

Readiness follows the project rule. For example, App and PEC use a conjunction involving an active `PREREQUISITE`, an unsatisfied status, and the selected item's `Depends` line naming the target. Their other relationship types do not automatically block. Do not export that exact rule to another project without its adoption, and do not use any topology calculation to bypass a named owner gate or reliance hold. [App selection rules][app-agents] · [PEC loop §5][pec-loop]

A strongly connected component, or SCC, identifies a set with circular ordering under the selected semantics. Its condensation is acyclic, but collapsing the picture does not settle the underlying production decision. Unresolved cycle-participating edges stay non-gating: they cannot drive dispatch readiness, blocker queues, wave placement, schedules, or implementation-readiness claims. Keep independent work available from a verified basis. [Cycle-driven resolution §2][cycles]

The doctrine names four moves. **Decompose** separates an overly broad node, often an interface from implementation. **Invert** places dependence behind a contract. **Merge** treats the coupled work as one indivisible unit. **Cut** reclassifies an edge as outside the graph's objective. Record the rationale for every remedy. Decompose and invert are design refinements agents may propose; cut and merge encode interpretive authority and are human-gated. Use a short note for an obvious bounded refinement and a decision packet for contested or objective-dependent choices. [Cycle-driven resolution §§2–3][cycles]

An acyclic graph is not proof of a complete or useful graph. Verify inventory coverage, missing targets, edge meanings, and relevant external inputs before drawing a readiness conclusion. An omitted dependency can make the topology look cleaner while making execution less reliable. A large SCC should direct attention to decomposition and meaning; it is not a reason for a tool to auto-cut relationships until the drawing passes. [Cycle-driven resolution][cycles] · [Dependency extraction][dependency-extract]

<a id="local-graph"></a>

## 9. Construct and traverse a local work graph

In the adopted App and Piping loop, the local graph turns an intended outcome and route through the project DAG into executable contributions. Keep one graph for the undertaking across sessions. It can contain design, inquiry, implementation, verification, independent review, integration, and reconciliation. It is an executable plan, not a replacement scope register or another lifecycle authority. [Construct a local work graph][construct-graph] · [App loop][app-loop] · [Piping loop][piping-loop]

Start by recovering intent. Identify the wanted result, priorities, approach, exclusions, completion conditions, and their sources in steering or decisions. Interpret clear direction without requiring the human to supply node IDs or a finished specification. Clarify only gaps that materially change scope, ordering, effort, or completion. Preserve a pause. If the same undertaking continues, revise its useful graph instead of creating another because the conversation is new. [Construct a local work graph §1][construct-graph]

Select the smallest coherent route. Locate the deliverables serving the outcome, follow upstream to required inputs, and follow downstream far enough to understand affected consumers. Read current contracts, Remaining, dependencies, relevant decisions, implementation, tests, and consequential unmerged changes. A desired result without a sound deliverable mapping needs an explicit mapping investigation or scope decision; forcing it into a convenient folder conceals the problem. [Construct a local work graph §§2–3][construct-graph]

Where the concordance method owns information homes, executable deliverable residuals still come from their Remaining records, with ruled program work under its activation. The local graph composes and elaborates that authorized work into useful outcomes. It may expose a new gap requiring a warranted Remaining update or a decision, but cannot originate new production scope merely by adding a node. Historical plans remain context; they do not become alternative queues. [Concordance §§2, 6][concordance] · [App F-APP-5][app-agents]

Give every executable node a meaningful result, stable ID, deliverable mapping, required inputs, write boundary, completion check, current state, and evidence or blocker. Dependencies name the particular condition a node needs: an adopted interface, a checked artifact, a human decision, a review, or an updated record. Keep ownership and informational links distinguishable from prerequisites. “Work on Package 4” does not define a return the parent can assess. [Construct a local work graph §§3–4][construct-graph]

An illustrative route for a save-recovery capability is:

```text
Clarify recovery contract
          |
          v
Implement bounded recovery --> independent review --> repair/backcheck
          |                                         |
          v                                         v
Exercise connected native journey -------------> integrate/check
                                                    |
                                                    v
                                      Reconcile affected deliverables
                                                    |
                                                    v
                                      Return the bounded undertaking
```

The diagram is illustrative. Its exact ordering, review stage, authority, and checks must come from the real brief and project. For example, an unavailable native witness can keep its node open while an independently useful code contribution proceeds; it cannot be relabeled complete to finish the diagram. [App checks][app-agents] · [Construct a local work graph][construct-graph]

Plan bounded reconciliation throughout the route, after stable coherent results and before work that relies on the updated record. Implementation and reconciliation have distinct completion conditions. A graph that ends at “merge code” can omit document consequences and verification residuals even though the implementation itself is useful. Reconciliation can run alongside independent implementation with disjoint writes. [Bounded reconciliation][bounded-reconciliation] · [Construct a local work graph §4][construct-graph]

For a new graph, the method prefers `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`. Preserve a useful existing location or representation, including JSON. Record its actual project-relative path in the loop pointer. An authorized recorder updates the pointer if it is outside the coordinator's write ceiling. One maintainer incorporates child returns against the latest graph so concurrent edits do not erase each other. [Construct a local work graph §5][construct-graph]

The template's states are `PLANNED`, `READY`, `ACTIVE`, `BLOCKED`, `UNCERTAIN`, and `COMPLETE`. Retain any existing adopted schema and explain what its states mean. A status label needs grounds: the input satisfying readiness, the operation currently active, the exact blocked act, or the evidence meeting completion. Keep source revision, uncommitted/unmerged work, active workers, resource ownership, holds, and next safe actions in recovery information. [Graph template][graph-template]

Walk the route before dispatch. Check executable cycles, omitted verification, shared assumptions, interface ownership, and integration capacity. Then advance ready authorized work without requesting approval for every routine node. Bring consequential choices through their owning process. A completed graph remains selected and visible; it does not start another phase, release a product, or issue a deliverable. [App loop][app-loop] · [Piping loop][piping-loop]

<a id="delegation"></a>

## 10. Commission and coordinate bounded work

A useful brief gives an executor enough purpose to make sound local choices and enough boundary to avoid inventing authority. It states the result and its use; accepted basis; relevant sources and scope; exact allowed writes; exclusions; required checks; expected return; parent; and return path. Small read-only work can use the retained launch message itself. Larger or governed work needs the structured record required by its method. Do not duplicate forms solely to make a small task look formal. [Root entry][root-entry] · [Runtime contract][runtime-contract] · [App instructions][app-agents]

For `software-bounded-implementation`, the required brief names `ScopePath`, selected `Workflow`, `PackageID`, `DeliverableIDs`, `Objective`, `AcceptedBasis`, `AllowedWriteTargets`, `EXCLUSIONS`, `AcceptanceCriteria`, `ExpectedReturn`, `PROFILE_PATH`, and `ApplyEdits: true`. The profile identifies registered checks; the brief supplies the applicable execution authorization. If write authority is absent, the executor returns a proposal rather than applying changes. [Bounded implementation brief][implementation-brief]

Before launch, preserve the supplied basis and actual method identity. Under governed delegation, sealing and the applicable human authorization are requirements; a nonempty approval-reference field does not establish that approval occurred. Cite an existing applicable owner act when it already authorizes the assignment. Do not manufacture a new permission ceremony or invent approval-token syntax. If a particular workflow reserves a fresh gate, prepare its concrete decision package before pausing at that gate. [CONTRACT K-SEAL-1][contract] · [Chirality change conventions][chirality-change]

Record actual parentage and mechanism. Distinguish a managed child session from a native descendant, a prepared brief from an executing child, and intended model allocation from observed model identity. Retain the actual supplied role, sources, selected methods/resources, revisions or hashes, relevant permissions, substitutions, and enforcement limits. A same-model independent review may still be useful, but must not be described as model diversity. [D-GOV-35][dgov35] · [Runtime contract][runtime-contract] · [Piping review rules][piping-agents]

Give concurrent workers disjoint writes or explicit serialized ownership. Include generated artifacts, shared configuration, graphs, and evidence destinations. Separate files do not guarantee technical independence: two workers can implement incompatible assumptions about the same interface. Bind the shared contract and revision in both briefs and identify the owner of any change. A common test database, browser, native application, or port can also require serialized use even when source changes are independent. [Runtime contract, coordination and evidence][runtime-contract] · [App instructions][app-agents]

TASK reports findings to its parent. The parent assesses consequences and relays the relevant information to affected workers, with its standing intact: observation, hypothesis, proposal, or accepted decision. A changed file on disk does not prove that a running child received amended instructions. Supply a versioned brief amendment through the available mechanism and establish its receipt before relying on affected continuation. Preserve prior basis and history. [Runtime contract][runtime-contract] · [TASK][task]

On return, examine artifacts and evidence against the brief. Check scope, changed paths, fulfilled criteria, missed interfaces, unresolved findings, and the contribution's fit with the receiving state. Distinguish usable partial work from completion. A manager who silently fills gaps in a child's report can obscure what the child actually did; retain the original return and record the parent's assessment and any authorized repair separately. [WORKING_ITEMS][working-items] · [Runtime contract][runtime-contract]

Adjust delegation when evidence calls for it. Repeated repair attempts without new information need a changed diagnosis or narrower question. A queue of unexamined returns needs review and integration capacity before more production. When uncertain shared definitions dominate, concentrate that design work; when established interfaces permit independence, increase useful concurrency. These are implementation choices within the approved strategy, not reasons to invent standing staffing quotas. [Piping instructions][piping-agents] · [Human manual §§4.3, 4.6, 5.4][human-manual]

<a id="implementation"></a>

## 11. Implement, verify, review, and integrate

Start implementation from the accepted objective, current candidate, explicit write fence, exclusions, and checking basis. Inspect the smallest coherent implementation and test surface. Make the change needed to establish the behavior, including source, tests, configuration, or documentation when their relationship requires it. Preserve unrelated user work. A local repair does not authorize unrelated dependency or public-contract changes, migrations, release, or operations excluded by its brief or method. Authorized registered setup may proceed within those boundaries. [Bounded implementation][bounded-implementation] · [Chirality change conventions][chirality-change]

Use tests to examine the requirement, not to invent it. Identify the expected result and its source. Protect adopted tolerances, oracles, limits, and checks when they conflict with implementation. A known failure disappears illegitimately if its criterion is removed or weakened. Diagnose the discrepancy, preserve the measured result, and bring a protected-criterion conflict to the owner with a recommendation. Hold the affected acceptance or merge while independent work proceeds. [App review rules][app-agents] · [Piping software checks][piping-agents]

Select verification from the actual affected behavior and project requirements. The project-local `software-workflow.json` supplies registered command arrays, working directories, always-checks, and path mappings. The selector proposes affected checks; it does not execute them or prove coverage. Consider indirect consumers and mandatory project checks that path matching may not capture. An empty selection or exit-zero result supports no broader conclusion than the operation actually performed. [Software profile contract][software-profile]

This copyable inspection example asks which checks the current App profile selects for a hypothetical project-relative source path. It changes no product files and does not run the selected checks:

```sh
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
python3 tools/software_workflow/select_affected_checks.py \
  projects/chirality-app-dev/software-workflow.json frontend/src/example.ts
```

Replace the example with the complete actual changed-path list. The command interface was checked with `--help` during preparation of this manual. The check runner is a separate operation. The following is deliberately a template, not a command to execute unchanged:

```text
python3 tools/software_workflow/run_registered_checks.py \
  <project/software-workflow.json> \
  --check <explicit-authorized-check-id> \
  --output <authorized-evidence-path.json>
```

Supply each authorized check explicitly; omitting `--check` causes the current runner to run all registered checks. The output path also needs authorization. The bounded implementation method prohibits unregistered install, release, network, and destructive commands. A missing prerequisite should return as a specific preparation need or revised assignment, not an improvised command outside that method. [Registered runner][registered-runner] · [Implementation tool policy][implementation-tools]

A registered check may own a bounded service lifecycle. The runner can allocate a loopback port, start the service, wait for readiness, inject declared environment values, run the check, and shut down the service. Preserve the distinction between service setup failure, timeout, and a product check failure. An App premerge command run without its required service is not the registered check. Coordinate ordinary dev servers with build and premerge operations so shared output directories are not written concurrently. [Software profile, managed service][software-profile] · [App profile][app-profile] · [App checks][app-agents]

Exercise the actual consumer route as soon as it becomes operable. For an interactive change, inspect resulting model, history, and persisted state as well as visible feedback. Relevant journeys can include editing, invalid input, cancellation, apply/reject, undo/redo, save/reopen, interruption, and recovery. For a service, examine the request, response, state changes, failure behavior, and subsequent consumer operation. Component tests and connected checks answer different questions. [App development checks][app-agents] · [Piping software checks][piping-agents]

Use native application evidence for a native-host claim where the owning criterion requires it. Browser evidence can support browser behavior but cannot silently substitute. Agent-operated exercises can provide reproducible observations; they do not lift practitioner-usability holds or supply professional acceptance. If the host cannot run a required check, retain the exact command, reason, candidate, and outstanding verification. In App this is recorded as `HOST_RERUN_REQUIRED`; a missing profile binding is a different failure. [App host-capability rule][app-agents] · [Piping software checks][piping-agents]

Evidence should make the observation reconstructible at the claimed scope. Identify inputs, candidate, relevant configuration, tool/environment versions, command or actions, expected outcome, observed outcome, exit status, and needed raw output. Retain non-secret bytes and a bounded rerun method where required. Record skipped, unavailable, interrupted, failed, and passed separately. Use one canonical copy with references from the graph or deliverable. Formatting a result does not upgrade its warrant. [App evidence contract][app-agents] · [Piping evidence contract][piping-agents]

Review the complete frozen candidate independently before a mergeable slice integrates. The reviewer did not implement the change and receives the requirements, full diff, relevant evidence, and limits. App product source retains its explicit fresh read-only `TASK + software-code-review` path. Examine changes to tests and criteria as closely as production code. Repair actionable findings, preserve disagreements and their grounds, and backcheck the changed content and affected consequences. A review of an earlier revision does not cover later edits automatically. [App review rules][app-agents] · [Piping review rules][piping-agents] · [Software code review skill][software-code-review]

Before Git closeout, inspect the receiving state, current diff, index, upstream changes, and owned file set. Recheck interactions introduced by integration. For `sgttomas/chirality`, standing owner authorization permits commit, push, PR creation/update, and merge within authorized scope once required CI and independent review cover the actual candidate with no unresolved blockers. Explicit holds and later owner directions prevail. Use configured identity and truthful attribution; do not imply personal owner review. This authority grants no product acceptance, release, or protection bypass. [Root entry][root-entry] · [PRD Root merge policy][root-merge] · [Chirality change conventions][chirality-change]

<a id="reconciliation"></a>

## 12. Reconcile the records with the result

Bounded reconciliation is ordinary production work on the affected records, not merely a report that somebody should update them later. Identify one deliverable or a small connected group, the stable result to compare, actual candidate and evidence, governing decisions, named document sections, and permitted writes. Read current controlling amendments before relying on older text. If the mapping is uncertain, return that specific question. [Bounded reconciliation §§1–2][bounded-reconciliation]

Compare in both directions. Follow the document's affected claims into the implementation and evidence: is the described behavior present, is the constraint enforced, and was the claimed check performed? Then follow the bounded implementation result back into the documents: did it settle a TBD, change an interface, reveal a limitation, satisfy a prerequisite, or leave an unrecorded consequence? A future requirement can legitimately remain unimplemented. A resolved setup assumption should not remain current merely because it was once true. [Bounded reconciliation §3][bounded-reconciliation]

Classify the response before editing:

| Finding | Warranted response |
|---|---|
| Current description lags established behavior | Update the description and evidence within authorized scope. |
| Implementation does not meet a requirement | Preserve the requirement; record and route the concrete production gap. |
| Accepted decision changes the intended design | Apply its exact consequences to the named carriers, retaining its basis. |
| Evidence is missing | Preserve the limitation and assign the required examination. |
| Proposed departure or conflicting authority | Prepare the specific proposal or decision; do not silently normalize it. |
| Current records already match | Return a supported no-change result at the inspected scope. |

These are actions under the [bounded reconciliation method][bounded-reconciliation], not a new taxonomy that replaces a formal program's controlled dispositions.

Keep claims at the level the project needs to preserve. Root concordance Revision 2 gives three tests: changing the statement would require a decision; another deliverable, user, project, or governing document relies on it; or named verification can check it. A statement failing all three is implementation detail, kept in code, tests, or developer documentation and cited as supporting evidence when useful. A decision-bound mechanism still belongs on the claim surface. Borderline cases remain visible for human ruling. [Concordance §3.1][concordance]

For example, “a failed save preserves the prior accepted document” is a stable product obligation. The name of a private helper used to implement it usually is not. A storage representation depended on by another consumer may itself be an adopted interface requirement. The distinction turns on the statement's consequences and warrant, not whether its vocabulary sounds technical. Granularity repair cannot erase a requirement or reverse a decision simply because the code now differs. [Concordance §3.1][concordance]

D-GOV-44's Revision 2 applies through its stated effective and adoption rules. In-flight programs keep their selected kernel/workflow bytes until their own authorized adoption. A new Root principle and a receiving notice do not silently revise a running program's repair posture. The App September 21 program's later owner rider was explicitly separated from publication of the principle. Follow that program's actual records before acting. [D-GOV-44][dgov44]

Make authorized document edits and check them together. Update fulfilled Remaining conditions only with support. Keep structured dependencies and their summary consistent when both are affected. Preserve IDs, source references, future scope, historical text, and other contributors' changes. Lifecycle, acceptance, identity, formal dependency-basis, and pinned-authority changes retain separate authority. Code repair is a separate node unless the brief explicitly includes it. A report-only return leaves application outstanding when writes were authorized and required. [Bounded reconciliation §§4–5][bounded-reconciliation]

A formal corpus concordance program is a larger selected method with activation, frozen discovery, calibration, bounded waves, independent verification, cross-Package synthesis, human dispositions, authorized repairs, and post-repair backcheck. It does not run merely because a small code slice needs document upkeep. Under the shared method, activation and its record land on the required common baseline before dispatch; discovery remains separate from repair; the pinned method does not drift as later files change. [Concordance §§3, 5–7][concordance] · [Reconciliation workflow][reconciliation-workflow]

The unit of formal comparison is the claim. One deliverable can contain aligned claims, stale wording, unimplemented obligations, and uncertain evidence simultaneously. Preserve that distinction in summaries. A discovery backcheck does not verify later repairs. Re-examine the actual repaired source state and account for residuals, stale derivatives, blockers, and rerun needs under the program's contract. Completion is evidence coherence at its declared scope, not issuance or professional approval. [Concordance method][concordance] · [Reconciliation workflow][reconciliation-workflow]

<a id="change"></a>

## 13. Handle decisions, change, and unresolved concerns

First identify what changed. A local implementation choice, an observed defect, a stale description, an unresolved design question, a changed accepted commitment, and a new human priority require different responses. Record the affected statement or interface, candidate, observation, consequence, and proposed next step. Exercise ordinary discretion inside the brief. An explicit adopted choice, protected criterion, owner-held act, or material scope change needs its owning decision before reversal. [WORKING_ITEMS][working-items] · [App selection and decisions][app-agents] · [Piping decisions][piping-agents]

Prepare human decisions as concrete reviewable packages. Explain the current basis, finding, alternatives, recommendation, affected scope, risks, reversibility, and what each choice enables. Include the proposed text or artifact when feasible. Name the actual act requested: choosing an interface, accepting an amendment, opening a fence, freezing a candidate, or authorizing release. Do not smuggle several different acts into a generic “approve.” Preserve the human's words and distinguish them from the agent's interpretation; silence is no ruling. [Root entry][root-entry] · [CONTRACT K-AUTH-1, K-BIND-1][contract]

For accepted decomposition change, use the selected applicable `scope-change` method. Its current package groups preparation around the requested change and impact, the exact amendment and propagation plan, and the independently examined poststate. Preserve stable identity and lineage. Apply only accepted changes, route remediation to the owners of affected surfaces, regenerate or explicitly account for derivatives, and return unresolved obligations. Use the project's adopted checkpoint edition rather than imposing a new one from this guide. [Scope change][scope-change] · [Decomposition standard][decomp-standard]

Follow consequences through consumers. An upstream amendment can affect local context, contracts, dependency records, graph snapshots, active briefs, and earlier verification. A graph helps locate relationships; it does not decide the impact. Under the invariant catalog, changed governed inputs create dirtiness and downstream staleness for human triage. Preserve earlier evidence as history and explain whether a current claim needs rework, review, or a supported no-impact disposition. [CONTRACT K-STALE-1, K-STALE-2, K-VAL-1][contract]

Instruction changes need their own authorized scope and tranche manifest. A designated current-graph pointer update inside an authorized undertaking is navigation maintenance; changing loop behavior is an instruction amendment. Notify affected loops whose pinned authority corpus or mirrors are changed. A notice communicates a change; the receiver decides adoption and updates its own basis. Do not write sibling records or re-pin their contracts under a general desire for consistency. [Root entry][root-entry] · [Chirality change conventions][chirality-change]

Keep ordinary pending work in its owning execution arrangement. Waiting for a review slot, input, or planned later node is not last-resort deferral. First seek an appropriate node in the current authorized undertaking. A concern without a current home—because ownership, scope, or an external precursor remains unresolved—may be preserved as a Task Management candidate with its source and allocation condition. The human manual's distinction helps avoid hiding active obligations in a distant register. [Human manual §5.6][human-manual] · [Task Management workflow][task-management]

Task Management makes concerns visible for human disposition and routes resulting work to the instrument that owns it. An action register is not an execution-progress database and cannot replace deliverable Remaining, a work graph, a decision register, or a scope-change workflow. Candidate harvesting does not itself promote a concern into an action or authorize implementation. Owner-invoked sweeps and invocation-local read-only federation remain bounded by their selected method; they create no universal loop-entry sweep or standing new gate. Preserve unresolved commitments while treatment is settled. [Task Management workflow][task-management] · [CONTRACT §1.14][contract]

<a id="app"></a>

## 14. Enter Chirality App development

Use `projects/chirality-app-dev` as `WORKING_ROOT`, its `AGENTS.md` for repository-development constraints, and `init/dev-loop-init-prompt.md` → `loop/LOOP_INIT.md` for entry. `instructions/AGENTS.md` is the guidance shipped to App users; it has a different applicability from the repository-development entry. The source basis for implementation is the PRD, accepted decomposition and scope changes, live DepClosure pointer, relevant deliverable contracts, decisions, and actual brief. [App project instructions][app-agents] · [App loop][app-loop]

At this manual's dated basis, the loop selects `execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/WORK_GRAPH.json`. The September 22 local-method notice preserves that whole-corpus run's method, pinned basis, phase cursor, and owner gates; it does not resume development. D-APP-130 accepts the R4 decision book as the R5 basis, expressly rules no packet, and authorizes no repair. Packet rulings must be recorded and merged before repair dispatch. This is a recovery example, not a permanent next-action instruction: re-read the actual selected run and later acts. [App local-method notice][app-local-notice] · [D-APP-130][dapp130]

Before relying on, dispatching, promoting, or consuming an accepted dependency for an App deliverable, run APP-HOLD-1 for the exact target and act. The following is a template from the App working root; choose the actual permitted operation and declared entry path:

```text
python3 execution/_Scripts/app_hold.py check \
  --operation <reliance|dispatch|checking-promotion|accepted-dependency-consumption> \
  --entry-path <actual-entry-path> --target <DEL-ID>
```

The pipe-separated operation field denotes alternatives, not a literal shell argument. A missing preflight, held target, malformed basis/admission, or register/scan disagreement blocks the act. Historical DEL-09-07 admissions are not current reusable exceptions. The check never authorizes an authority-corpus re-pin. [APP-HOLD-1 rules][app-agents] · [App hold tool][app-hold]

Source principally lives under `frontend/src`, `frontend/electron`, `frontend/packages`, and `frontend/scripts`; the frontend workspace contains its tests and build configuration. Current App and Runtime manifests require Node `>=22.19.0`; the older App build guide's `>=20` statement is stale at this basis. Read the current executable manifest and disclose discrepancies rather than installing from an outdated prose requirement. [App package manifest][app-package] · [Runtime package manifest][runtime-package] · [App build guide][app-build]

The registered App checks include `frontend-test`, `frontend-typecheck`, `frontend-build`, `frontend-premerge`, `harness-self-check`, `harness-pytest`, and `app-hold-integrity`. Project instructions additionally specify their applicable closeout, product-source, UI, native-host, packaging, and corpus-reconciliation obligations. Stop the ordinary dev server before build/package/premerge operations. The registered premerge check owns a stub service and `HARNESS_BASE_URL`; calling its npm script alone does not supply that setup. [App profile][app-profile] · [App checks][app-agents]

`npm test`, `npm run typecheck`, and `npm run build` are declared in the frontend manifest; use them only as selected authorized checks. Packaging is separate: `desktop:prepare` prepares/builds inputs, while `desktop:pack` and `desktop:dist` consume prepared inputs and perform their declared verifiers. Their existence grants no signing, notarization, distribution, or release authority. Retained compatibility scripts do not establish another qualified MVP engine. Codex remains the App target, with application-owned Runtime hosting the stock Codex App Server under the current accepted boundaries. [App package manifest][app-package] · [App development boundaries][app-agents] · [Runtime PRD revision][runtime-revision]

<a id="piping"></a>

## 15. Enter Piping development

Use `projects/chirality-piping`, its project `AGENTS.md`, and `init/dev-loop-init-prompt.md` → `loop/LOOP_INIT.md`. Follow `docs/PRD.md`, `execution/_Decomposition/SOFTWARE_DECOMP.md`, applicable amendments, and `execution/_DAG/_LATEST.md` for the actual source basis. Older README or workplan selectors cannot displace the current entry. However, live instructions explicitly retain F-PIP-1 through F-PIP-4 by reference to the historical workplan's fence section; its old F-PIP-5 selection procedure is superseded. Historical location and live incorporation are different facts. [Piping instructions][piping-agents] · [Piping loop][piping-loop]

At the stated basis, the selected graph is the September 21 whole-corpus reconciliation undertaking. Its graph, handoff, and `RESUME.md` banner can lag the phase events. Follow the linked resume instructions and replay `RUN_STATE.jsonl` rather than choosing the most convenient visible summary. The D-73 activation bounds discovery to its ruled phases; later repair/backcheck phases need their separate authority. Its addendum instructs that selected audit to use identified existing CI and clean-sweep evidence and run no test suite. General development commands below do not override that run-specific instruction. [Piping selected-run resume][piping-resume] · [D-73 ruling][piping-d73] · [D-73 addendum][piping-d73-addendum]

The principal product surfaces are `core/` Rust crates, `apps/desktop/` frontend and native Tauri shell, and `tests/` plus `validation/` benchmarks, hand calculations, and witnesses. Deliverable production and evidence remain under the execution hierarchy and owning run locations. There is no project-root Cargo workspace manifest at this basis: select the affected crate manifest or the maintained runner's discovered set. Frontend build or browser testing does not establish a native packaged witness. [Piping package manifest][piping-package] · [Piping operational source map][piping-report]

The profile registers `desktop-test`, `desktop-build`, `piping-pytest`, `evidence-sweep`, and shared harness checks. Project npm scripts expose `build:wasm:desktop`, `test:desktop`, and `build:desktop`. Standalone desktop tests need the generated WASM when absent. Product-code merges additionally require the DEC-025 sweep on a clean candidate, applicable CI, and fresh independent review of the complete candidate. Select work and commands from the actual brief and instructions; a partial capability sweep cannot establish the full gate. [Piping profile][piping-profile] · [Piping package manifest][piping-package] · [Piping software checks][piping-agents]

The domain boundary is critical. `domains/piping-design/` includes vetted conceptual prose, but extracted equation artifacts remain unreviewed OCR/pdf2md material pending the maintainer's manual review. They may not supply authoritative equations for physics models, solver/kernel work, or analytical verification. Use the maintainer's vetted engineering sources and report review status. Keep software verification, engineering validation, practitioner usability, code-compliance claims, professional reliance, lifecycle issuance, and release distinct. [Piping knowledge-source and claim fences][piping-agents]

After an authorized coherent result, reconcile the affected Scope of Work, Remaining, dependency, and evidence statements. Preserve future requirements and any accepted bespoke representation in the selected corpus; do not convert formats incidentally. Current graph/result records can carry continuity without duplicate session receipts, while historical receipt integrity checks and method-specific handoffs remain applicable. [Piping loop][piping-loop] · [Piping reconciliation continuity][piping-agents]

<a id="runtime"></a>

## 16. Enter Runtime development

Use `projects/chirality-runtime/AGENTS.md` and its `loop/LOOP_INIT.md`. Recover the accepted ownership through `execution/_Coordination/MIGRATION_ACCEPTANCE_2026-09-06.md`, then `docs/PRD_AUTHORITY.md`, `docs/PRD.md`, and `execution/_Decomposition/_AUTHORITY.md`. Read `HANDOFF_STATE.md`, the newest receipt, and later linked amendments together. An old candidate label does not nullify a later owner act; migration acceptance does not activate every carrier or release every hold. [Runtime entry][runtime-agents] · [Runtime loop][runtime-loop]

The seven-carrier register and SCA-003-era records preserve a frozen accepted basis. The September 12 D-GOV-43/SCA-004 packet overlays that reading: it retires six carriers in place, revises retained stewardship, closes the obsolete held bindings through a purpose change, and preserves the separately disposed R16-B relationship. Some PRD, Scope-of-Work, register, and pointer bytes stay unchanged because Root pins them. Read the overlay and status histories; do not “repair” their old counts or frozen text merely to match a newer summary. Closure by retirement does not assert that the old held empirical acts were performed. [Runtime PRD revision][runtime-revision] · [Runtime impact assessment][runtime-impact]

The current architectural reading is an application-owned Runtime service hosting stock Codex. The App is its production consumer. Retained daemon package names, compatibility providers, and historical supplier/LaunchAgent proof records do not revive a separate daemon deployment, qualify another MVP engine, or authorize a client integration. Runtime owns its product contracts and services; shared instruction/tool changes route to Root, and client changes route to the owning project. PEC compatibility remains an opportunity to verify, not an MVP prerequisite silently declared satisfied. [Runtime PRD revision][runtime-revision] · [Runtime entry][runtime-agents]

Source is principally in the `contracts`, `core`, `daemon`, `client`, and `cli` packages, all under `packages/`; inspect their actual roots and dependencies before editing. Tests live in the maintained test surfaces, with frozen execution evidence kept outside the executable test inventory. The project manifest declares Node `>=22.19.0`, `npm run typecheck`, `npm test`, and `npm run build`. The profile registers `typecheck` and `unit` as always-checks. A connecting App/Runtime change also needs verification of the real client path; two component passes do not establish integration. [Runtime package manifest][runtime-package] · [Runtime profile][runtime-profile] · [Chirality change conventions][chirality-change]

For an authorized shell-equipped actor, these are read-only sourced posture views from the checkout, not acceptance operations:

```sh
python3 tools/practitioner_harness/harness.py status --project runtime
python3 tools/practitioner_harness/harness.py drift --project runtime
```

The full live Runtime entry also specifies remote refresh and Git observations for actual execution. Do not claim fresh remote state from these two views alone. Its first return identifies divergence, local changes, accepted authority, current lifecycle/holds, exact task boundaries, available checks, prerequisites, and the next lawful manager action. [Runtime loop][runtime-loop] · [Practitioner harness][harness]

Runtime's September 22 local-method notice is intake only. It does not adopt App/Piping's graph or receipt changes. Preserve a durable project handoff under the governing run's closeout contract and record actual checks. Runtime explicitly claims no receipt validator or automatic receipt-format enforcement; do not invent one. [Runtime local-method notice][runtime-local-notice] · [Runtime loop][runtime-loop]

<a id="pec"></a>

## 17. Enter PEC development

PEC is the coordination plane: a rebuildable, non-authoritative projection of governed file truth with an ephemeral presence layer. It dispatches nothing, arbitrates nothing, and has no ruling-write path. Its value must survive graceful absence: no governed act may require PEC. Read the product's current exact source and owner records; do not treat an advisory PEC result as authority. [PEC instructions][pec-agents]

The live entry is `projects/pec/loop/LOOP_INIT.md`, reached through the project's current launcher and `AGENTS.md`. The loop's full Step 0 refreshes remote references, validates receipts, checks retired-workplan absence, reads decision/profile/decomposition/hold sources, and discovers actual Remaining surfaces. Do not substitute a general quick-start command block for this adopted procedure during execution. The retained `_DomainEngines/pec` paths in old citations resolve through D-PEC-80's relocation maps; they are not a second live loop. [PEC loop][pec-loop]

Select work from deliverable `_STATUS.md ## Remaining` and the exact scope of its grant. A missing Remaining section means no recorded selectable scope, not completion and not permission to invent an assignment. The loop permits an explicitly scoped owner request for preparation or correction without a Remaining item, but that exception does not authorize production or bypass a merged owner prerequisite. Owner acts and hold releases required by the loop are observed on fetched `origin/main`; predecessor work on the run branch is a different condition. [PEC loop §5][pec-loop]

The write fences are unusually specific. Default project-local surfaces are bounded coordination, the listed instruction surface, and the one-time status pointer allowance. Every other write—including new v2 source, scaffolding, manifests, and configuration—requires an owner-ruled D-PEC packet naming exact paths, acts, verification, and rollback. Existing code or a valid PRD grants no broader implementation permission. Instruction changes also retain Root's applicable scope requirements. [PEC write fences][pec-agents] · [PEC loop §3][pec-loop]

The old `core`, `server`, `web`, `agent-sidecar`, `tools`, `fixtures`, and prototype workspace manifests are a frozen reference corpus. Read and cite them; do not edit, delete, or repurpose them as live v2 implementation. Do not run the old server or a mutating CLI against a non-scratch database. V2 carries useful machinery as cited patterns under its exact packets. It remains content-minimal: paths, counts, SHAs, states, and hashes, not file or diff contents. Runtime retains session/delegation/turn ownership; PEC creates no second execution loop. [PEC frozen-corpus and data rules][pec-agents]

Before dispatch, review, fan-in, production reliance, consumption, or promotion, perform the reliance-hold preflight for the actual target and operation. Its interface is:

```text
python3 execution/_Scripts/pec_reliance_hold.py \
  --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv \
  --target <exact-project-relative-target> \
  --operation <actual-intended-operation>
```

The tool supports `historical-read-only-inspection`, `exact-correction-preparation`, `candidate-validation`, `dispatch-for-production`, `rely-for-production`, `consume`, and `promote`. Use the intended act, not a less restrictive label. Missing or malformed hold data fails closed. A successful historical inspection preflight authorizes only that checked inspection. [PEC loop §8][pec-loop] · [PEC hold tool][pec-hold]

Current bounded v2 code exists under `v2/src/pec_v2`, with API contracts, configuration, standard-library tests, posture tools, and documentation in adjacent v2 folders. Older “implementation does not exist” prose is dated product-stage history. Later exact packet evidence establishes particular work without proving full product readiness. Similarly, an adopted candidate PRD postimage is not necessarily applied to the live PRD. Read the controlling act and actual files. [PEC operational source map and currency review][pec-report]

The current software profile registers `v2-api-contract`, `v2-loop-registry`, `v2-store-guard`, `v2-core-posture`, and `harness-self-check`. Use an explicitly compatible Python and the exact packet's finite checks; a legacy prototype npm CI pass does not prove that v2 checks ran. Required system kill/parity evidence remains unmet when unavailable, not an invented pass. Existing role/model conventions and stale launcher references need owning-loop compatibility treatment; a newer Root notice alone does not silently migrate PEC's accepted method. [PEC profile][pec-profile] · [PEC loop §8][pec-loop] · [PEC operational review][pec-report]

PEC retains one branch per run, one commit and receipt per iteration, a validated receipt chain, and a PR at terminus or when a merged prerequisite is needed. The September 22 notice leaves its accepted basis unchanged. Keep those outputs while App/Piping use their graph-based continuity. Close out only exact granted scope and preserve human-gated lifecycle, artifact acceptance, release, and professional reliance as separate acts. [PEC loop §§5–7][pec-loop] · [PEC local-method notice][pec-local-notice]

<a id="recovery"></a>

## 18. Recover, hand off, and close an undertaking

Recover from the actual state before repeating work. Inspect the selected cursor, branch and worktrees, staged and unstaged changes, outputs, still-running workers, and shared resources. Determine what happened after the last recorded update. Preserve incomplete but useful work and verify its evidence. Establish that prior workers have stopped or explicitly transfer ownership before reassigning their files or application state. An interruption is not a reason to discard a partial result or report an unobserved test as failed. [App loop §0][app-loop] · [Piping loop §0][piping-loop]

If a pointer is missing or contradictory, search the pertinent records and history for the intended target. Do not select a convenient alternative until its relationship to the undertaking is established. In App or Piping, a historical receipt used as a recovery cursor needs its integrity validator. The following are alternatives for the respective project, from the checkout; they are not mandatory additions to every ordinary graph continuation:

```sh
python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .
python3 tools/validation/validate_piping_loop_receipts.py --repo-root .
```

A failed cursor cannot support reliance. Independently verified work can continue from a separate sound basis. Validation establishes structural evidence, not authentication of owner prose. PEC has its own live receipt-validation obligation; Runtime explicitly has no corresponding validator claim. [App loop][app-loop] · [Piping loop][piping-loop] · [PEC loop][pec-loop] · [Runtime loop][runtime-loop]

Use the existing continuation home. For App/Piping development, the current graph and linked results may already contain everything a successor needs; no separate handoff or receipt is required solely because a session ends. A selected formal workflow may still require a handoff, snapshot, or receipt. Runtime and PEC retain their own closeout contracts. Preserve the real method rather than adopting one universal documentation ritual. [App instructions][app-agents] · [Piping instructions][piping-agents] · [Runtime loop][runtime-loop] · [PEC loop][pec-loop]

A dependable continuation account identifies the intended result, checked revision, local or unmerged changes, accepted inputs, completed contributions, evidence, unresolved checks/findings, active operations and ownership, holds, next safe action, and rerun triggers. Link detail instead of copying it. Before retiring a temporary worktree, retain evidence and results at a location the successor can actually read. Do not point to a deleted output and call the work recoverable. [Construct a local work graph §5][construct-graph] · [Chirality change conventions][chirality-change]

Close the undertaking against its stated conditions, including integration, required review, verification, and planned reconciliation. If the human explicitly reduces or otherwise bounds the conclusion, retain that decision and surviving obligations. Return the result at the scope it establishes. A completed contribution can be fit for the next use while leaving a deliverable or product incomplete. Warranted Remaining stays open; a deferred concern retains its owner and allocation condition. [WORKING_ITEMS][working-items] · [Bounded reconciliation §5][bounded-reconciliation]

For delivery, identify the exact delivered candidate and applicable human approval, recipient, package, operating limits, and continuing responsibilities. Preserve the difference between build output, transmitted artifact, and accepted baseline. Safety-significant, contractual, and professional work remains subject to its domain authority. Chirality's professional-responsibility model reserves approval, issuance, signature, seal, and reliance decisions to the accountable human; an agent never claims those acts for itself. This manual does not establish jurisdiction-specific legal or code compliance. [DIRECTIVE §3][directive] · [CONTRACT K-AUTH-1][contract] · [Human manual, chapter 6][human-manual]

<a id="authoring"></a>

## 19. Create or improve reusable methods

Keep roles, workflows, skills, tools, briefs, and plans distinct. A workflow is reusable method guidance in a canonical `WORKFLOW.md` package. A skill is bounded reusable instruction in `SKILL.md`. A deterministic tool performs an operation; it neither confers permission nor accepts its subject. A brief binds the present work. An ad hoc plan can be useful without being registered as a reusable workflow. Repetition is a reason to consider method development, not authority to amend an active method silently. [Root entry][root-entry] · [Runtime contract][runtime-contract]

Discover before loading. Inspect the effective catalog's name, description, origin, compatibility, and collision status, then load only the selected entrypoint and stage resources. Unqualified workflow lookup uses project, user, then bundled precedence. Preserve the full selected identity—kind, source, source-root ID, and name—through execution and replay. For example, the current App/Piping loop explicitly selects the bundled `chirality-root` local-graph methods. A later same-name discovery cannot replace that selection silently. [Runtime contract, libraries and catalogs][runtime-contract] · [Workflow index][workflow-index]

Legacy `TaskSkill` and unqualified converted workflow names use the explicit compatibility mapping. A source-qualified workflow identity preserves its historical workflow and bypasses that alias conversion. Retired named agents are mapped through compatibility records; they are not reintroduced as standing roles. Record what was supplied and what resolved. If historical bytes cannot be recovered, report that limit instead of replaying today's same-name file as though it were the original. [Runtime contract, workflow packages][runtime-contract]

Before creating or revising any reusable workflow, load `create-workflow` from the intended library basis. Establish purpose, applicability, inputs, outputs, decisions, checks, recovery, and destination. A small method may need one file. Keep run-specific private facts and permissions in briefs. A project/user method request does not authorize changing the bundled library. Use existing revision mechanisms and preserve prior content before an accepted replacement. [Root entry][root-entry] · [Create a workflow][create-workflow]

In the App authoring path, prepare `.chirality/workflow-drafts/<name>/WORKFLOW.md` under the project or user root, with needed resources inside the draft package. The human inspects it, requests changes in chat, and registers the reviewed bytes through the Workflows panel. Do not write straight into the live catalog as a substitute for review, claim an unobserved registration, or automatically run the new method. Another host presents the complete method and resource inventory for explicit acceptance before registration through available tools. [Create a workflow][create-workflow]

Validate metadata, folder/name agreement, resource containment, links, and intended source identity; walk through a representative success and interruption. Distinguish that walkthrough from execution evidence. Bundled Root authoring separately updates the catalog and generated index under its authorized scope and checks. Runtime discovery or reference-tool success does not establish production provider qualification. Skills and tools need the same care with provenance, scope, actual availability, and applicable ownership, even though their packaging differs. [Create a workflow][create-workflow] · [Runtime contract][runtime-contract]

Domain methods deserve their own source treatment. `domain-decomp` preserves source admission, fidelity, atomization, category/knowledge-type meaning, disagreement, and independent examination. DOMAIN/KTY material is outside the PROJECT/SOFTWARE Scope-of-Work conversion standard. Research work should identify its accepted snapshot, retrieval basis, bounded question, independently checked evidence, and recoverable return through the selected method. Neither a retrieved passage nor a generated knowledge artifact becomes a validated engineering equation by being indexed. [Domain decomposition][domain-decomp] · [Research orchestration][research-orchestration] · [Scope-of-Work standard §1][sow-standard] · [Piping source rules][piping-agents]

<a id="examples"></a>

## 20. Worked operational examples

The following examples are constructed teaching cases. They report no real authorization, execution, test, acceptance, or current project status. Their purpose is to show how to make the next contribution concrete without requiring the human to fill a form. Apply the actual sources cited in the preceding sections.

### A small documentation correction

The human asks to fix a broken guide link. Recover the relevant instruction and link target, inspect the existing diff, and make the authorized bounded edit. Check the resulting link and any affected document rendering. Obtain the independent candidate review and applicable repository closeout checks required for the slice. Do not open a new product PRD or rebuild its DAG. If inspection reveals that the proposed target is obsolete, repair the link to the supported current entry or return that concrete ambiguity with evidence. [Root entry][root-entry] · [Chirality change conventions][chirality-change]

An appropriate return might read:

> Updated the guide's entry link to the live project launcher and preserved the historical reference in its source note. The link and rendered heading resolve. Independent review found no blocking issue on the submitted revision. This documentation change does not alter the project's selected undertaking or instructions.

The actual return should link the changed artifact and identify actual verification. Do not copy this sample's claimed results into a real run without performing them.

### A bounded implementation brief

Suppose the human has authorized repair of a save operation that overwrites intervening edits. The parent first reads the adopted save contract, current implementation, failing observation, consumer interface, and applicable holds. It prepares this kind of assignment, with actual IDs, paths, and checks substituted:

```text
Objective: Preserve intervening edits when applying a prepared proposal.
Basis: The adopted revision-comparison contract and identified failing case.
Scope: The save/apply boundary and its focused regression coverage.
Writes: Exact implementation and test files; one evidence result location.
Exclusions: No storage-format change, lifecycle edit, or unrelated UI cleanup.
Checks: Registered focused checks plus the required connected journey.
Return: Diff, tested candidate, observed outcomes, evidence, and residuals.
Parent: The implementation manager; return interface changes before applying.
```

This concise human-readable explanation complements any required structured fields. If the diagnosis shows the interface itself cannot express the needed condition, the child returns that design question. It does not silently change every caller or weaken the expected preservation behavior. [Bounded implementation][bounded-implementation] · [Implementation brief][implementation-brief]

### A decision package the human can act on

Suppose two deliverables cannot be ordered because each needs an unresolved contract from the other. Prepare the source-linked SCC and a remedy before asking for a decision:

> The export writer needs an accepted schema; the schema task currently waits for the writer's implementation evidence. I propose separating the schema definition from its implementation validation. The definition would supply the writer, and a later validation task would check their combined result. The attached draft shows the affected claims, edges, and checks. This preserves both obligations and leaves the existing implementation usable. The decision requested is acceptance of this exact scope/dependency amendment under the project's process; implementation would then continue from the revised basis.

The real packet identifies exact candidate bytes, alternatives, consequences, and the reserved act. If the remedy is a cut or merge, obtain the doctrine's human decision. A graph visualization alone is insufficient. [Cycle-driven resolution][cycles] · [Scope change][scope-change]

### A repair that is useful but incomplete

The implementation passes its focused tests, but native interruption recovery remains unobserved. Report the code result and keep the evidence node open. Reconcile any stale “not implemented” wording only to the extent supported, while retaining the required native observation in Remaining. A good return names the next action instead of declaring the whole feature passed. [App evidence rules][app-agents] · [Bounded reconciliation][bounded-reconciliation]

> The repair and focused regression checks are complete on the identified candidate. Independent review and the affected backcheck found no blocking issue. The required native interruption scenario could not run in this host and remains recorded with its exact command and starting conditions. The implementation is ready for that examination; no checking promotion or release is claimed.

### A stale continuation summary

The graph says “review next,” while its linked event log records a review and subsequent correction. Read the governing resume method, inspect the actual patch and review return, and determine whether the correction was backchecked. Preserve the review as evidence of its original candidate. Update continuation through the authorized maintainer only after recovering the actual result. Do not repeat review blindly or conclude that the later correction inherited the earlier pass. This is the kind of discrepancy found in the dated Piping source survey. [Piping resume][piping-resume] · [Piping operational review][piping-report]

<a id="sources"></a>

## 21. Source map and terminology

This manual was authored from the supplied Consolidated v1 manuscript and repository basis stated above, with independent coverage reports for all four projects. The [undertaking brief](../../plans/evidence/2026-09-22_alignment_manual/BRIEF.md), [project coverage report](../../plans/evidence/2026-09-22_alignment_manual/project-coverage.md), and [author source manifest](../../plans/evidence/2026-09-22_alignment_manual/guide-author-sources.json) preserve the assignment, observed limits, and consulted origins/hashes. These are evidence for this documentation undertaking, not new project authority.

| Need | Primary navigation |
|---|---|
| Runtime entry, roles, authority, permission intersections | [Root entry][root-entry], [role registry][registry], [Runtime contract][runtime-contract], [CONTRACT][contract] |
| Paths, lifecycle, dependency representation | [SPEC][spec], [TYPES][types], [cycle doctrine][cycles] |
| Formation and setup | [decomposition standard][decomp-standard], [workflow index][workflow-index], [project setup][project-setup] |
| Production and examination | [Scope-of-Work standard][sow-standard], [software profile][software-profile], [concordance method][concordance] |
| Repeated development | [construct local graph][construct-graph], [bounded reconciliation][bounded-reconciliation], each project's live loop |
| Change, integration, residual concerns | [scope change][scope-change], [Task Management][task-management], [Chirality change][chirality-change] |
| Professional and domain limits | [DIRECTIVE][directive], the actual project rules, accepted domain sources and responsible human's decisions |

**Undertaking** means an identified body of work with a purpose and completion conditions; it can span sessions and Packages. **Session** means an interaction period in its actual host. **Candidate** means the particular source/artifact state being examined. **Snapshot** preserves identified material at a governed boundary. **Derivative** is a generated or interpreted view whose sources and status must remain explicit. **Hold** is a restriction on a named act; ordinary progress does not dissolve it. **Acceptance** is the applicable human act about an identified subject. [Root entry][root-entry] · [CONTRACT][contract] · [Runtime contract][runtime-contract]

The human-facing manual uses **reckoning** for agent interpretation, comparison, inference, and selection, reserving **judgment** for the accountable human. Some operational role files use “judgment” in its ordinary task-performance sense. Read both without attributing professional or acceptance authority to the agent. **Verification** examines conformity to stated criteria; **validation** examines fitness for the intended use. State exactly what each check supports, who examines its adequacy, and what remains. [Human manual, preface and §1.5][human-manual] · [DIRECTIVE §3][directive]

[root-entry]: ../../AGENTS.md
[registry]: ../../agents/registry.json
[help-human]: ../../agents/AGENT_HELP_HUMAN.md
[helps-humans]: ../../agents/AGENT_HELPS_HUMANS.md
[working-items]: ../../agents/AGENT_WORKING_ITEMS.md
[task]: ../../agents/AGENT_TASK.md
[runtime-contract]: ../AGENT_WORKFLOW_RUNTIME.md
[contract]: ../CONTRACT.md
[spec]: ../SPEC.md
[types]: ../TYPES.md
[directive]: ../DIRECTIVE.md
[human-manual]: Project_Management_for_Human_Agent_Teams_Consolidated_v2.md
[chirality-change]: ../../.agents/skills/chirality-change/SKILL.md
[root-merge]: ../PRD_ROOT.md#531-merge-gate-policy--the-d-8-successor
[dgov16]: ../governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md
[dgov35]: ../governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md
[dgov44]: ../governance_harness/_DECISIONS/D-GOV-44_concordance_claim_granularity.md
[workflow-index]: ../../workflows/index.json
[decomp-standard]: ../DECOMPOSITION_STANDARD.md
[project-decomp]: ../../workflows/project-decomp/WORKFLOW.md
[software-decomp]: ../../workflows/software-decomp/WORKFLOW.md
[domain-decomp]: ../../workflows/domain-decomp/WORKFLOW.md
[project-setup]: ../../workflows/project-setup/WORKFLOW.md
[setup-contract]: ../../workflows/project-setup/resources/contract.md
[preparation]: ../../.agents/skills/preparation/SKILL.md
[sow-standard]: ../DELIVERABLE_SCOPE_OF_WORK_STANDARD.md
[sow-workflow]: ../../workflows/scope-of-work/WORKFLOW.md
[cycles]: ../CYCLE_DRIVEN_RESOLUTION.md
[dependency-extract]: ../../workflows/dependency-extract/WORKFLOW.md
[concordance]: ../DELIVERABLE_CONCORDANCE_METHOD.md
[construct-graph]: ../../workflows/construct-local-work-graph/WORKFLOW.md
[graph-template]: ../../workflows/construct-local-work-graph/resources/work-graph-template.md
[bounded-reconciliation]: ../../workflows/bounded-reconciliation/WORKFLOW.md
[bounded-implementation]: ../../workflows/software-bounded-implementation/WORKFLOW.md
[implementation-brief]: ../../workflows/software-bounded-implementation/resources/brief.md
[implementation-tools]: ../../workflows/software-bounded-implementation/resources/tools.md
[software-profile]: ../SOFTWARE_WORKFLOW_PROFILE.md
[registered-runner]: ../../tools/software_workflow/run_registered_checks.py
[software-code-review]: ../../.agents/skills/software-code-review/SKILL.md
[reconciliation-workflow]: ../../workflows/reconciliation/WORKFLOW.md
[scope-change]: ../../workflows/scope-change/WORKFLOW.md
[task-management]: ../../workflows/task-management/WORKFLOW.md
[create-workflow]: ../../workflows/create-workflow/WORKFLOW.md
[research-orchestration]: ../../workflows/research-orchestration/WORKFLOW.md
[harness]: ../../tools/practitioner_harness/README.md
[app-agents]: ../../projects/chirality-app-dev/AGENTS.md
[app-loop]: ../../projects/chirality-app-dev/loop/LOOP_INIT.md
[app-profile]: ../../projects/chirality-app-dev/software-workflow.json
[app-package]: ../../projects/chirality-app-dev/frontend/package.json
[app-build]: ../../projects/chirality-app-dev/docs/BUILD_AND_RELEASE.md
[app-hold]: ../../projects/chirality-app-dev/execution/_Scripts/app_hold.py
[app-local-notice]: ../../projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md
[dapp130]: ../../projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-130_RULING_R4_GATE_RUN_D128_2026-09-22.md
[piping-agents]: ../../projects/chirality-piping/AGENTS.md
[piping-loop]: ../../projects/chirality-piping/loop/LOOP_INIT.md
[piping-profile]: ../../projects/chirality-piping/software-workflow.json
[piping-package]: ../../projects/chirality-piping/package.json
[piping-resume]: ../../projects/chirality-piping/execution/_Reconciliation/DeliverableConcordance/RECON_2026-09-21_WHOLE_CORPUS/RESUME.md
[piping-d73]: ../../projects/chirality-piping/execution/_Coordination/_DECISIONS/D-73_RULING_2026-09-21.md
[piping-d73-addendum]: ../../projects/chirality-piping/execution/_Coordination/_DECISIONS/D-73_RULING_ADDENDUM_2026-09-21.md
[piping-report]: ../../plans/evidence/2026-09-22_alignment_manual/project-piping-notes.md
[runtime-agents]: ../../projects/chirality-runtime/AGENTS.md
[runtime-loop]: ../../projects/chirality-runtime/loop/LOOP_INIT.md
[runtime-profile]: ../../projects/chirality-runtime/software-workflow.json
[runtime-package]: ../../projects/chirality-runtime/package.json
[runtime-revision]: ../../projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_DGOV43_HOLD_CLOSURE_20260912/PRD_REVISION.md
[runtime-impact]: ../../projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_DGOV43_HOLD_CLOSURE_20260912/Impact_Assessment.md
[runtime-local-notice]: ../../projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md
[pec-agents]: ../../projects/pec/AGENTS.md
[pec-loop]: ../../projects/pec/loop/LOOP_INIT.md
[pec-profile]: ../../projects/pec/software-workflow.json
[pec-hold]: ../../projects/pec/execution/_Scripts/pec_reliance_hold.py
[pec-report]: ../../plans/evidence/2026-09-22_alignment_manual/project-pec-notes.md
[pec-local-notice]: ../../projects/pec/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md
