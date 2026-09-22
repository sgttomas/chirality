# Review of Preface and Chapters 1–2

Review date: 2026-09-22. Repository basis: `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`.

The opening chapters are substantively strong and should retain most of their prose. The material corrections concern **which described methods are currently adopted, which remain proposals, and which source artifacts are actually available**. The treatment of reliance, human acceptance, product versus project, requirements versus evidence, and revision-bound review is worth preserving.

This is a bounded assessment, not an acceptance of the manuscript or an instruction amendment. The parent integrates the recommendations into the incremented edition and separate agent guide.

## Assignment, execution boundary, and coverage

- Actual role: TASK, Type 2, `/root/manual_review_manager/manual_ch1_ch2`.
- Parent: HELPS_HUMANS, `/root/manual_review_manager`; root coordinator: HELP_HUMAN, `/root`.
- Actual delegation mechanism: a running native Codex collaboration descendant, launched through `collaboration.spawn_agent`; not a Chirality-managed `delegate_agent` session. The parent supplied the role and bounded assignment. This agent loaded its TASK body explicitly and did not delegate.
- Active instruction basis: Root `AGENTS.md`, `agents/AGENT_TASK.md`, the undertaking [brief](BRIEF.md), and the parent's bounded assignment. Other workflow and skill bodies below were consulted as comparison sources, not selected as execution instructions. No other full role body was loaded for this review.
- Host access was unrestricted filesystem access, network enabled, approval policy `never`. The two-file write limit, prohibition on project edits and Git operations, and no-delegation rule were instruction restrictions, not sandbox enforcement. Only this report and its [source manifest](review-ch1-ch2-sources.json) were written. No commit, push, merge, project act, lifecycle change, or live graph update was performed.
- Exact runtime model identifier and the parent's history-fork settings were not independently exposed or inspected. No model-diversity or fresh-history-isolation claim is made.

Every assigned manuscript line was read. An initial large display truncated part of lines 1–310; it was discarded as completeness evidence and repaired by the continuous, untruncated reads below. Reading was not limited to headings or search results.

| Material | Assigned lines | Continuous full-line reads | Coverage |
|---|---:|---|---|
| Title, contents, Preface | 1–42 | Within 1–120 | Complete |
| Chapter 1 body | 43–506 | 1–120, 121–240, 241–360, 361–480, 481–600 | Complete |
| Chapter 1 source notes | 507–542 | Within 481–600 | Complete |
| Chapter 2 body | 543–1169 | 481–600, 601–720, 721–840, 841–960, 961–1080, 1081–1212 | Complete |
| Chapter 2 source notes and following boundary | 1170–1212 | Within 1081–1212 | Complete |

All ranges include blank lines, specimens, captions, tables, and source notes. The source manifest contains SHA-256 identities, paths, complete-read ranges, search-only excerpts, and the limits of the checks. The manuscript has 3,731 lines; lines 1213 onward were outside this assignment. No external regulatory or historical fact-check was conducted. The APEGA, Alberta DBM, and thesis claims remain attributed statements from the manuscript, not independently renewed confirmations by this review.

## Strengths to retain

1. **Purpose and reliance are connected.** Lines 47–82 distinguish product, project, undertaking, responsibility, and the intended use of a return. This supports both audiences without pretending that agents become accountable professionals.
2. **Initiative is compatible with bounded authority.** Lines 88–134 and 164–172 allow interpretation, investigation, and useful proposals while keeping human commitments and adoption identifiable. Avoid rewriting these passages into a permission request for every routine act.
3. **Evidence does not become authority by being persuasive.** Lines 178–210, 610–656, 775, and 1003–1059 distinguish source direction, implementation observation, acceptance, source identity, and provenance. The separation between the accepted candidate and its subsequent acceptance record is particularly useful.
4. **Stage labels do not imply numerical completion.** Lines 218–229 and 279–285 carefully separate the author's stage model, lifecycle position, local completion, and remaining obligations. Keep the attribution to the author's engineering interpretation.
5. **The role repertoire is already close to current Root.** Lines 291–307 and 875–932 correctly preserve four roles, direct Type 0-to-Type 2 dispatch, manager-owned integration, and the prohibition on Type 2 delegation. The current [Root entry](../../../AGENTS.md) and [TASK body](../../../agents/AGENT_TASK.md) support these distinctions.
6. **The graph account is appropriately conditional.** Lines 327–361 distinguish composition, dependency direction, input standing, readiness, closure, and real resolution of coupling. Lines 457–505 correctly preserve graph identity across sessions and distinguish a prepared repair from backchecked completion.
7. **PRD development is substantive writing.** Lines 663–819 explain activity, states, technical content, exclusions, source roles, and uncertainty instead of turning the document into an inventory of links. The editor example is consistently labelled as constructed; preserve that status.
8. **The detailed FEED claims checked here agree with current sources.** The three grouped decomposition checkpoints, immutable snapshots, package assignment, software Context Envelopes, and discipline/artifact-kind distinction are supported by the current [software contract](../../../workflows/software-decomp/resources/contract.md), [software method](../../../workflows/software-decomp/resources/method.md), and [project contract](../../../workflows/project-decomp/resources/contract.md).
9. **The matrix warning is exact and useful.** Lines 1139–1148 accurately explain why criteria with different method sets cannot safely share a matrix row. Current [scope-of-work instructions](../../../workflows/scope-of-work/WORKFLOW.md), lines 106–114, and [checks](../../../workflows/scope-of-work/resources/checks.md), lines 43–47, support it. Keep the worked example.
10. **Review covers the changed candidate.** Lines 938–997 and 1013–1025 preserve independence, repair, backcheck, normative set identity, and historical review scope. These are not redundant formalities; they prevent one revision's review from being silently applied to another.

## Findings and precise proposed edits

The locations below refer to immutable v1 line numbers. Replacement wording is proposed editorial text; it creates no new project authority.

### R1 — Update the loop's adoption status and preserve project differences

**Material correction.** Lines 438, 455, 521, 527, and 1186 describe archive loops as proposed. At the reviewed basis, the persistent graph loop and two supporting methods are adopted Root/App/Piping source. The source note's historical provenance should remain, but it must no longer be the only account of operational status. Runtime and PEC did not acquire the App/Piping procedure merely by receiving a notice.

Evidence: current [App loop](../../../projects/chirality-app-dev/loop/LOOP_INIT.md), [Piping loop](../../../projects/chirality-piping/loop/LOOP_INIT.md), [September 22 implementation record](../../../execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md), [tranche manifest](../../../docs/governance_harness/tranche_manifests/ROOT-LOCAL-WORK-GRAPH-METHODS-20260922.yaml), [App notice](../../../projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md), and [Runtime notice](../../../projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md).

Replace line 438 with:

> At the repository basis examined for this edition, the App and Piping development loops use the six numbered sections shown in Figure 1.4. Their persistent local-graph procedure and the supporting `construct-local-work-graph` and `bounded-reconciliation` methods were integrated on 22 September 2026. Each project's current pointer selects its undertaking. Existing runs retain their selected methods, pinned basis, phase cursors, and owner gates until their own adoption. The traversal below concerns work after the phase DAG is established; earlier dependency and coupled-question work follows the owner's steer and its selected method.

Replace the beginning of line 455, retaining the explanation of the pointer summaries, with:

> *Figure 1.4. The six section names in the current App and Piping development loops at revision `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`. The pointer summaries explain their function. Chapter 4 develops the sequence in detail.*

Insert after that caption:

> This is a project-specific application, not one universal session-entry contract. Runtime recovers its accepted carrier scope, authority, handoff, and latest receipt through its own loop entry. PEC re-derives live work from deliverable `Remaining` records and its applicable owner packets. Read the selected project's current instructions before choosing a continuation procedure. A notice that a shared method exists does not adopt it for another project or reopen held work.

Replace Chapter 1 source [6], line 521, with:

> **[6] Entry and development.** The original manuscript cited the supplied `dev-loop-init-prompt.md` and proposed loops in `development-loop.zip`. The Piping launcher reproduced here also matches `projects/chirality-piping/init/dev-loop-init-prompt.md`. Current repository application is documented by the App and Piping `loop/LOOP_INIT.md` files and `execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md`, at the edition's recorded revision. Historical archive provenance and current project adoption are distinct.

Replace Chapter 1 source [9], line 527, with:

> **[9] Local graph and reconciliation methods.** Current maintained sources are `workflows/construct-local-work-graph/WORKFLOW.md`, its `resources/work-graph-template.md`, and `workflows/bounded-reconciliation/WORKFLOW.md`. Their registered identities are `chirality-root:bundled:workflow:construct-local-work-graph` and `chirality-root:bundled:workflow:bounded-reconciliation`. The original manuscript's archive references are historical provenance. Method selection and in-flight run adoption remain explicit.

Replace Chapter 2 source [5], line 1186, with:

> **[5] Development continuity.** The current App and Piping loop entries, their launchers, and the maintained local-graph construction method support the continuation account. Earlier archive loops remain historical sources. Existing runs retain their own selected methods and gates; Runtime and PEC retain their separate project entry procedures. Method-specific handoffs remain distinct from ordinary continuation under the adopted local-graph loops.

**Important integration limit:** Both App and Piping currently select September 21 whole-corpus reconciliation graphs. The September 22 App notice explicitly says the change neither switches that run to bounded reconciliation nor resumes development. Do not describe the new loop as permission to traverse its selected graph or start product work in this documentation task.

### R2 — Put the draft PRD method's status at its first introduction

**Material clarification.** Line 553 says the workflow "gives this preparation a defined method," while the unregistered draft status is clearest only at lines 1174–1176. A reader using Chapter 2 as an operating guide could infer an installed canonical workflow. A semantic scan of the current Root catalog found no `software-prd`; the two new graph methods are present. This establishes catalog absence at this basis, not absence from every user's personal library.

Replace the first two sentences of line 553 with:

> This chapter describes the proposed `software-prd` method, draft version 1, as an authoring pattern for human review. It is not registered in the Root workflow catalog at the repository basis examined for this edition. Under that proposed method, HELPS_HUMANS works with the human to develop the product account, examines the supporting material, and brings an identified, reviewed document back for acceptance.

Keep the remainder of the paragraph. Replace line 1176 with:

> The `software-prd` package described here is draft version 1, identified by the original manuscript as prepared for human review under `create-workflow`. The source note names a workflow entrypoint and two supporting guides; those original package files were not available for independent examination in this bounded repository review. This chapter does not register the method or establish successful execution. Before operational use, obtain and inspect the intended package and preserve its source-qualified identity. An authorised ad hoc PRD assignment remains an ad hoc undertaking unless a reusable workflow is deliberately adopted.

If the parent locates and actually includes the original package, update only the availability sentence to name its verified location and hash. Do not convert source retrieval into an adoption claim.

### R3 — Repair the publication's source-availability claims

**Material provenance correction.** The Preface's line 41 names a companion editorial report, and line 1176 says the complete proposed PRD instructions accompany the source bundle. The initial imported `docs/alignment-manual` directory contained only v1 Markdown, DOCX, and PDF. The manuscript's source notes name many original archives and author directions without providing recoverable local locations. A source title or an internal cross-reference does not itself supply those missing bytes.

Replace the last sentence of line 41 with:

> This edition's review record identifies the repository sources actually examined, their revisions, and the limits of that comparison. Original source-note titles are retained as provenance; where the underlying material is not included or independently available, the edition says so rather than implying a complete accompanying source bundle.

The parent should make "review record" a real relative link to its consolidated assessment and manifest. This bounded report cannot stand in for the full-book assessment.

After line 509, insert:

> Source notes distinguish current repository instructions, historical drafts and archive references, constructed examples, and external domain references. Current-repository claims in this edition are tied to the recorded comparison revision. References retained from the original manuscript do not imply that their underlying files or external publications were re-examined for this revision.

For both chapters, keep historical source labels and add clickable current paths where verified. In particular, qualify bare `AGENT_*.md` as `agents/AGENT_*.md` and `registry.json` as `agents/registry.json`; use current `workflows/...` paths for locally checked methods without pretending they are byte-identical to the original ZIP contents. The review manifest is evidence of this comparison, not a substitute for missing original author directions or for current project authority.

### R4 — Make Types, actual delegation, and method identity operationally clear

**Useful boundary clarification.** The role account is substantially accurate. "Three modes" in line 291 is inconsistent with current Root's Type terminology, and the account does not explain that a role label, written brief, or fork alone does not establish an executing child in the intended role. This distinction matters directly to an agent user guide.

Replace the first sentence of line 291 with:

> The method uses four roles in three Types: HELP_HUMAN is Type 0, HELPS_HUMANS and WORKING_ITEMS are Type 1, and TASK is Type 2; Agent 0, 1, and 2 are shorthand for these Types.

After line 307, insert:

> Executable delegation requires an actual child execution through the available host. Record its parent, intended role, supplied instruction basis, bounded brief, enforcement limits, and return. A written assignment is not evidence that the child ran. A full-history fork also does not by itself establish a different role; the intended role and applicable guidance must be supplied explicitly. An instruction-limited write scope should not be described as sandbox enforcement when the host still grants broader access.

Then insert this short distinction, or put it in the operational companion if Chapter 1 would become too dense:

> A role describes the agent's contribution; a workflow supplies a method; a skill supplies reusable contextual instruction; a tool performs an available operation; and the brief bounds the present assignment. None enlarges the authority of another. In Chirality, discover the applicable method, retain its source-qualified identity, and load only the body and resources needed for the work. A same-named method from a different origin is not an interchangeable source.

Evidence: [Root entry](../../../AGENTS.md), especially Roles, Skills and workflows, Tools and briefs, and the execution/delegation paragraphs. The current [TASK instructions](../../../agents/AGENT_TASK.md) directly support the no-further-delegation and usable-return requirements.

### R5 — Distinguish a new-project sequence from resuming existing authorised work

**Practical clarification.** Lines 134, 190, 245, 371, 887, and 1150 give the manual's initial development sequence. The maintenance exclusion in Chapter 2 and the resume discussion already mitigate overreach, but an agent reading the first chapter can still mistake the sequence for a requirement to reopen an established project's PRD, decomposition, or setup on every new assignment.

Insert after line 245:

> This is the initial course for the development undertaking described here. In an existing project, recover the accepted basis and completed preparation before deciding what remains to do. A repair, continuation, or bounded change within that basis does not restart conception and setup merely because it begins in a new conversation. Reopen only the decisions affected by the proposed change and follow the owning project's current activation and change rules.

Evidence: [project-setup contract](../../../workflows/project-setup/resources/contract.md), lines 19–46, begins with actual-state inspection and forbids re-asking already-recorded decisions; current App/Piping loops preserve existing graph identity and pinned run bases. This addition should not weaken the author's chosen sequence for genuinely new production work.

### R6 — State the current infer-and-clarify behavior when no graph is selected

**Precision improvement.** Line 459 says to establish the intended course "from the owner and the project." Read mechanically, this can create another approval request despite an adequate current brief. The adopted graph method explicitly permits supported inference and focused questions only for material gaps.

Replace the third and fourth sentences of line 459 with:

> A pointer deliberately set to `none` means no undertaking is currently selected there. Recover the intended result from the owner's steering, conversation, and relevant project records. Where that basis is adequate, state the interpretation and construct the graph within the authorised scope; clarify only gaps that would materially change the scope, ordering, effort, or completion conditions.

Preserve the paragraph's missing-target and historical-evidence qualifications. Evidence: [construct-local-work-graph](../../../workflows/construct-local-work-graph/WORKFLOW.md), lines 17–43; App loop lines 50–64; Piping loop lines 46–60.

### R7 — Explain current Git integration separately from governed acceptance

**Operational omission, not an existing contradiction.** Line 277 correctly says merge, acceptance, publication, and handover differ. The agent guide should make the standing Git grant explicit so it does not add a per-merge permission gate that current Root removed.

Optional repository application paragraph after line 277, or include it in the companion guide:

> In this Chirality repository, the owner's standing Git authorisation permits agents to commit, push, open or update pull requests, and merge within authorised work. Merge still requires the applicable CI and independent review to cover the actual candidate with no unresolved blocking findings. This authorisation does not accept a governed basis, lift a project hold, expand scope, or release a product. Record the distinction rather than asking for a new Git decision already covered by the standing grant.

Evidence: [Root entry](../../../AGENTS.md), Execution and governance, standing owner authorization of 2026-09-12. The bounded task's own prohibition on Git operations remained in force despite that general grant.

### R8 — Add the source/decision network and attention view to the graph explanation

**Useful completeness improvement.** Line 341 explains tree and production dependencies well. Current Root gives four complementary reading views: tree, production graph, source/decision network, and attention. The latter two connect the manuscript's philosophical discussion to practical context recovery without requiring another formal graph.

Insert after line 341:

> Two further views help recover what the work means. The source and decision network connects claims to evidence, constraints, provenance, and supersession across folders. The attention view brings the material relevant to a present question together through comparison, decomposition, and synthesis, leaving traces in briefs, decisions, and outputs. Use whichever views answer the question; this does not require constructing four graphs or surveying the whole repository. Git ancestry records change history, but does not by itself establish production dependency or accepted authority.

Evidence: [Root entry](../../../AGENTS.md), Reading project information. Keep these practical views distinct from the four philosophical perspectives in the Preface; they are not four new approval gates or a replacement taxonomy.

### R9 — Name preparation as the current skill and preserve legacy formats

**Small current-source correction.** Chapter 2 source [10] cites an archived `preparation/WORKFLOW.md`; the current project-setup method deliberately discovers and applies the effective `preparation` skill. The body describes the behavior accurately but should avoid teaching the archived packaging as the current invocation form.

At line 1106, replace "Preparation creates" with:

> The effective `preparation` skill creates

In source [10], preserve the archive citation as provenance and append:

> Current repository setup discovers the source-qualified `preparation` skill; the project-local entrypoint is `.agents/skills/preparation/SKILL.md`. `workflows/project-setup/resources/method.md` records that selection and routes new PROJECT/SOFTWARE production to `scope-of-work`, `MODE=INIT`. Existing complete legacy contracts keep their compatibility route until an authorised conversion; setup does not silently recreate or migrate them.

Evidence: [preparation skill](../../../.agents/skills/preparation/SKILL.md), [setup method](../../../workflows/project-setup/resources/method.md), lines 87–111 and 144–157, and [setup contract](../../../workflows/project-setup/resources/contract.md), lines 67–80. Keep the existing prose about optional Memory and preserving even empty existing files. Figure 2.7 already labels its listed records as a selection, so omission of `_SEMANTIC.md` from that illustrative subset is not a completeness defect.

### R10 — Restore the missing local figure without changing its standing

**Initial packaging defect; parent reports repair.** Line 333 references `assets/Figure_1_1.png`. That path did not exist at the first inspection, so Markdown readers could not see the chapter's only image. The parent subsequently reported restoration of the exact figure from the supplied DOCX with extraction/placement evidence. This reviewer did not perform that extraction or visual comparison.

For v2, retain the image reference and the caption's constructed-example qualification once the restored asset is included and its link is checked. Do not label it as an executed project's DAG. The final asset-existence check is recorded in this report's manifest; parent visual evidence owns image fidelity.

### Optional light editing

The PRD-maturity risk recurs at lines 196, 263, and 865. The repetition is defensible for teaching, but line 263 can be shortened without losing the later worked case:

> The phase review should examine whether unresolved PRD questions are becoming embedded in dependent designs. Familiarity, limited scope, and close coordination can support a modest basis; interacting interpretations can instead require costly reconciliation. Sections 1.6 and 2.7 develop this contingent risk. [1, 2]

Do not broadly compress the repeated editor example: its recurrence exposes different relationships among intent, evidence, scope, verification, and acceptance.

## Operational lessons for the separate agent guide

| Guide need | Procedure and limit to express | Primary source |
|---|---|---|
| Enter the right undertaking | Resolve repository and project, load Root/applicable project instructions and the actual role, recover live steering, then follow that project's entry. Do not automatically load every role or workflow. | Root `AGENTS.md`; TASK body |
| Choose current project continuation | App/Piping: current loop pointer and graph; Runtime: accepted carrier scope, authority, handoff and receipt; PEC: deliverable `Remaining` and exact owner packets. Treat these as dated repository observations. | Four inspected loop entries |
| Recover before repeating | Compare graph or handoff with branch, local/unmerged work, evidence, active operations and holds. Verify previous writers have stopped or transfer ownership before reassigning files and shared test resources. | App/Piping loop §0 |
| Preserve graph continuity | Keep one graph for the undertaking. `none` permits supported construction under existing direction; a missing target requires recovery. A completed graph remains selected until another undertaking is chosen. One maintainer integrates concurrent updates. | Graph method §§1, 5; loop §5 |
| Respect navigation versus authority | An authorised current-pointer edit is navigation maintenance. Changing loop behavior is an instruction amendment. Notices inform receiving projects; they do not repin, adopt, activate or release them. | Root entry; Sept22 notices |
| Delegate actual bounded work | Use a real available delegation mechanism, supply intended role and basis, record parentage and actual enforcement, and keep Type 2 non-delegating. A launch brief and a returned execution are different facts. | Root entry; TASK body |
| Select methods honestly | Discover source-qualified workflow/skill identity. Retain origin and hash. Do not assume the manuscript's draft `software-prd` is installed; obtain it or use an explicitly bounded ad hoc authoring brief. | Root entry; Root catalog; draft availability limit |
| Keep reconciliation executable | Plan bounded document changes after coherent code/evidence and before dependents that need updated records. Preserve unmet requirements; a report alone does not finish an authorised edit assignment. Do not switch the current whole-corpus runs to this method by implication. | Bounded reconciliation §§1–5; App Sept22 notice |
| Separate completion from acceptance | Node completion, implementation, reconciliation, lifecycle, governed acceptance, and release answer different questions. The exact candidate, evidence, review, human act, and open obligations must remain recoverable. | Manual §§1.6–1.10, 2.9–2.12; current loop §5 |
| Close Git work without extra gates | Apply standing Git authorization, actual-candidate CI and independent review; preserve explicit holds and project acceptance/release boundaries. | Root Execution and governance |
| Maintain usable source records | Distinguish current instructions, adopted sources, proposals, examples, historical evidence, and unavailable inputs. A hash identifies content; it does not establish its truth, authority, or current applicability. | Manual §§2.2, 2.6, 2.10; Root selective-context requirement |
| Preserve setup and local contracts | Inspect before initialization, preserve existing files, invoke the effective preparation skill for structure, use `SOW_V1` for new PROJECT/SOFTWARE production, and retain exact criterion–method pairing. | Current setup, preparation and scope-of-work sources |

## Return and limits

The assigned line coverage is complete. Current local evidence supports the retained role, decomposition, setup, and verification distinctions, with the corrections above. The manuscript's external domain references, original author conversations, DBM archive packages, and unregistered `software-prd` package were not independently revalidated here. Their absence from this review is not evidence that their content is false; it limits what this review can attest.

The source manifest records every file whose contents were supplied during this bounded review, including partial and search-only reads. No source hash is presented as an authority ruling. The parent must integrate these findings with the other chapter reviews, verify the final combined candidate, and keep original v1 bytes unchanged.
