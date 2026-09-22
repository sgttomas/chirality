# Chapters 3–4 review

Review date: 2026-09-22. Repository basis: `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8` (the merge of PR #846, “Adopt persistent work graph loops and bounded reconciliation”). Review subject: Consolidated v1, lines 1213–2625, including both chapters' source notes. Recommendations below are proposals for the parent to integrate; they change no operating instructions, accepted project basis, or project state.

The chapters are substantially sound and should be preserved. The main improvements concern the standing of their sources and the distinction between the new App/Piping development loops, existing governed runs, and the different Runtime/PEC entry contracts. Most of Chapter 4 already describes the method now adopted in App and Piping. A wholesale rewrite would lose useful precision.

## Execution and coverage

Actual child: `/root/manual_review_manager/manual_ch3_ch4`, TASK, Type 2. Parent: `/root/manual_review_manager`, HELPS_HUMANS, Type 1; supervising ancestor: `/root`, HELP_HUMAN, Type 0. Mechanism: delegated-harness-native Codex collaboration, evidenced by this child's delivered assignment and parent messages; this was not a Chirality-managed `delegate_agent` session. No delegation was performed. The child read the active TASK role and deliberately consulted the other three role files only to compare the manuscript's role account. Those other roles were not activated.

The host exposes unrestricted filesystem access, network access, shell tools, and an approval policy of `never`. The two-file write boundary, prohibition on Git mutations, and non-delegation boundary are instruction restrictions, not separately enforced filesystem sandbox restrictions. Only this report and its companion source manifest were written. No project workflow was executed, no skill was applied as an execution method, and no tests, Git mutation, network lookup, project acceptance, or release operation was performed. Workflow and skill bodies read below were comparative source material. Exact backend model and reasoning effort were not independently exposed to this child; no inherited model label from historical project records is claimed as this execution's identity.

The initial oversized batch was truncated and is excluded from the full-reading attestation. The following numbered, untruncated reads cover every requested line continuously; no paragraph, diagram, table, blank line, or source note within the range was skipped.

| Read | Lines inclusive | Lines read | Content covered |
|---|---:|---:|---|
| 1 | 1213–1388 | 176 | Chapter 3 opening; scope, Packages, Deliverables, coverage and audit introduction |
| 2 | 1389–1565 | 177 | Decomposition acceptance; setup; production contract; evaluation and exclusions |
| 3 | 1566–1741 | 176 | Setup return; continuity; dependencies; graph analysis; SCC treatment |
| 4 | 1742–1918 | 177 | SCC treatment; initial DAG; every Chapter 3 source note; Chapter 4 opening and steer |
| 5 | 1919–2094 | 176 | Steering; persistent local graph; role/delegation arrangement |
| 6 | 2095–2270 | 176 | Resources; technical detail; briefs; permissions; concurrency; findings |
| 7 | 2271–2446 | 176 | Decisions; amendments; execution; evidence; review and integration |
| 8 | 2447–2625 | 179 | Bounded reconciliation; recovery; phase continuation; every Chapter 4 source note; next-chapter anchor |
| **Total** | **1213–2625** | **1,413** | **Continuous complete assigned coverage** |

The [source manifest](review-ch3-ch4-sources.json) records exact source paths, SHA-256 identities, read ranges, and the distinction between full reads, selected excerpts, and search locators. Local sources were checked proportionately; this is not a complete audit of every referenced workflow or its executable tooling. Original ZIP archives and the claimed accompanying source bundle were not present in the inspected `docs/alignment-manual` inventory. Repository counterparts do not prove byte equality with those archives.

## Strengths to preserve

- §§3.1–3.4 preserve conditions while splitting obligations and distinguish allocation, adequacy, and satisfaction. The example of a valid mapping that omits required preservation behavior is particularly useful.
- §§3.2–3.3 distinguish the durable Package/Deliverable decomposition from code layout and temporary assignments. A Deliverable can span sessions without acquiring an invented durable task hierarchy.
- §§3.6–3.7 connect criteria, verification, evidence, and boundary ownership precisely. Separate matrix rows for different method sets prevent false coverage.
- §§3.9–3.12 state graph objective and arrow direction, preserve ANCHOR/EXECUTION distinctions, examine missing-register coverage before topology, and separate active relationships from satisfied prerequisites. SCC condensation is correctly treated as diagnosis rather than proof that internal work is executable.
- §§4.2–4.3 distinguish project DAG, local work graph, and delegation hierarchy. They already reject one manager per Package, one agent per node, and Type as an intelligence ranking.
- §§4.5–4.10 distinguish a written brief from an executing child, inspection from acceptance, registered checks from permission, fresh-context review from model diversity, and a passing rerun from repair of the known defect.
- §4.11 makes reconciliation produce authorized document edits, keeps future requirements intact, separates code repair, and checks concurrent changes before saving. Its recovery instructions and single-maintainer rule are strong.

## Surgical revisions

The manuscript line numbers below identify the unchanged v1. Proposed wording is ready to insert or replace; the parent should adapt numbered source references to the final v2 source list.

### C34-01 — Update proposal-only source standing, without rewriting its history

**Material correction.** Lines 1842, 1942, 1964, 2106, 2438, 2589, and 2593 describe the App/Piping loop as proposed or only supplied. That was a valid statement about the manuscript's input. At the review basis, the two loop replacements and bundled methods are integrated, and the source notes should identify the current counterparts separately.

Replace line 1942 with:

> The App and Piping development loops adopted in the repository on 22 September 2026 use the same traversal sequence. Their project pointers, checks, and selected graphs differ. The Runtime and PEC loops retain their own entry and closeout contracts. This chapter develops the App/Piping local-graph method; its application elsewhere requires the owning project's adopted basis.

Replace “the proposed development loops” in Figure 4.2's caption with “the App and Piping development loops”. Replace “The proposed loop provides” at line 2106 with “The App/Piping development-loop procedure provides”. Replace “The proposed loop points” at line 2438 with “The App/Piping development loops point”. These are dated source corrections, not new adoption acts.

Replace Chapter 4 source [2] with:

> **[2] Development loops and adoption.** The original manuscript used `development-loop.zip`, `loop-1/loop/LOOP_INIT.md` and `loop-2/loop/LOOP_INIT.md`, as supplied proposals. This repository edition additionally uses `projects/chirality-app-dev/loop/LOOP_INIT.md` and `projects/chirality-piping/loop/LOOP_INIT.md` at the dated review basis. Their adoption is recorded in `execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md`, its instruction-tranche manifest, and the routed project notices. Both loops use sections 0–5 and persistent graph recovery. Runtime and PEC received notices; their loop procedures were not replaced. Read the current launcher and the owning project's instructions for the applicable entry and checks.

Update Chapter 3 source [12] similarly: preserve its archive attribution as original provenance, then name the current launcher, App/Piping loop paths, and adoption record. Update Chapter 4 sources [5] and [11] to include the current `workflows/construct-local-work-graph/` and `workflows/bounded-reconciliation/` counterparts. For source [12], explicitly name the current App `AGENTS.md` “Development checks and evidence” section and Piping `AGENTS.md` “Software checks” section; the earlier loop remains dated provenance.

Evidence: [adoption record, lines 7–38](/Users/ryan/.codex/worktrees/da43/chirality/execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md:7), [tranche manifest](/Users/ryan/.codex/worktrees/da43/chirality/docs/governance_harness/tranche_manifests/ROOT-LOCAL-WORK-GRAPH-METHODS-20260922.yaml:19), [App loop](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-app-dev/loop/LOOP_INIT.md:29), [Piping loop](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-piping/loop/LOOP_INIT.md:25), [Runtime notice](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md:14), [PEC notice](/Users/ryan/.codex/worktrees/da43/chirality/projects/pec/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md:14).

### C34-02 — Preserve the method and owner gates of the run selected by a new loop

**Material missing qualification.** Chapter 4's recovery account is good but does not expressly cover the actual adoption case: both live pointers select existing September 21 whole-corpus reconciliation runs. A newly adopted entry procedure does not switch those runs to bounded reconciliation or resume paused development.

Insert after line 1968:

> Follow any phase cursor or handoff linked by the selected graph. A continuing governed run retains its selected method, pinned source basis, and owner gates until that run adopts a change through its own decision path. In the September 2026 App and Piping adoption, the new loop pointers select existing whole-corpus reconciliation graphs; selecting those graphs neither replaces their method with bounded reconciliation nor resumes development.

Replace the last sentence of line 2035 with:

> At the dated repository basis, both App and Piping retain selected graphs under `AgentRuns`; existing useful graphs need not move merely because the preferred location for new graphs is `WorkGraphs`.

Insert after line 2035 or alongside its pointer instruction:

> Updating the designated pointer within an authorized undertaking is navigation-state maintenance. Changing the loop's behavior or constraints is an instruction change with its own authority and manifest. Neither act supplies new production scope.

In §§4.2 and 4.11, identify the adopted methods as `chirality-root:bundled:workflow:construct-local-work-graph` and `chirality-root:bundled:workflow:bounded-reconciliation` once, then retain the short names in running prose. An identical unqualified name in another library is not automatically the same selected method.

Evidence: [App loop, lines 31–33](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-app-dev/loop/LOOP_INIT.md:31), [Piping loop, lines 27–29](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-piping/loop/LOOP_INIT.md:27), [App adoption notice, lines 14–25](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md:14), [method identities and integration treatment](/Users/ryan/.codex/worktrees/da43/chirality/execution/_Coordination/LOCAL_WORK_GRAPH_METHODS_20260922.md:17), [Root pointer rule](/Users/ryan/.codex/worktrees/da43/chirality/AGENTS.md:229). The selected graph contents were inspected as recovery records, not revalidated as current project status.

### C34-03 — Bound the “no new handoff or receipt” rule

**Material application risk.** Line 2530 can be read as a repository-wide instruction. It is current App/Piping development-loop practice, with exceptions for separately selected workflows. Runtime explicitly retains its governing closeout handoff contract; PEC retains one receipt per iteration and validation. The manual should not cause an agent to retire these contracts by analogy.

Replace line 2530 with:

> In the adopted App/Piping development loops, ordinary continuation needs no additional session handoff or receipt when the graph and linked results already contain the required facts. A separately selected workflow retains its own output contract, and other project loops retain their adopted continuity requirements. Existing handoffs and receipts remain historical evidence; apply the owning validation rule before using a historical receipt as a recovery cursor. Continue the selected undertaking without creating a duplicate graph or restarting completed work.

Add “where the owning loop and selected method permit” to line 1940's final clause about a fresh session beginning without a separate handoff. Keep the existing distinction at lines 1595 and 2605 between workflow stages/output contracts and project phases.

Evidence: [App instructions, lines 196–210](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-app-dev/AGENTS.md:196), [Piping instructions, lines 73–87](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-piping/AGENTS.md:73), [Runtime closeout](/Users/ryan/.codex/worktrees/da43/chirality/projects/chirality-runtime/loop/LOOP_INIT.md:34), [PEC iteration and closeout](/Users/ryan/.codex/worktrees/da43/chirality/projects/pec/loop/LOOP_INIT.md:246).

### C34-04 — Recognize an active legacy production contract and the actual SOW activation record

**Compatibility correction.** §§3.6 and 4.11 describe `ScopeOfWork.md` well, but the current graph and reconciliation methods explicitly accommodate an active legacy four-document kit. An agent should not initialize a new SOW simply because an existing deliverable lacks that filename, or edit archived legacy copies after conversion.

Insert after line 1459:

> This chapter uses the Scope-of-Work format for new production authoring. Before working on an existing Deliverable, establish its active production format and governing adoption. A valid legacy-only `Datasheet.md`, `Specification.md`, `Procedure.md`, and `Guidance.md` kit can remain authoritative during its authorized transition. Inspect that kit where it is still active; do not recreate retired files or treat archived copies as current. Format conversion is a separate, lifecycle-neutral undertaking.

Add this row immediately after the SOW row at line 2468:

> | Active legacy `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md` | Inspect the equivalent definition, requirements, method, and rationale where this remains the governing production format. Do not recreate retired files or update archived copies as current documents. |

Append to Chapter 3 source [7] and the corresponding Chapter 4 source [7]:

> In the repository, D-GOV-16 is recorded as RULED APPROVED on 12 July 2026. That record establishes the activation decision; it does not make every individual conversion, lifecycle transition, or later amendment accepted. The active format and applicable adoption must still be recovered for the Deliverable being used.

Evidence: [SOW standard §§2 and 7](/Users/ryan/.codex/worktrees/da43/chirality/docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md:24), [D-GOV-16 approval and single-format transition](/Users/ryan/.codex/worktrees/da43/chirality/docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md:3), [graph construction's legacy compatibility](/Users/ryan/.codex/worktrees/da43/chirality/workflows/construct-local-work-graph/WORKFLOW.md:65), [bounded reconciliation's file table](/Users/ryan/.codex/worktrees/da43/chirality/workflows/bounded-reconciliation/WORKFLOW.md:40).

### C34-05 — State the default repair for mechanism-level prose

**Substantive clarification.** Lines 1505–1507, 2135, and 2486 correctly explain stable claims. Current D-GOV-44 adds a concrete default when existing text has fallen behind implementation: lift the statement to claim level and move mechanism detail into evidence. Merely refreshing the mechanism description is not the default. This also needs the in-flight adoption boundary in C34-02.

Insert after line 2482:

> For stale mechanism-level wording, apply the decision, interface, and named-verification tests before choosing the repair. Where the adopted claim-granularity rule applies, prefer to restate the stable obligation and move the mechanism detail into supporting evidence. Retaining a mechanism-level claim needs the owning ruling's reason, for example that the mechanism itself is decision-bound. A granularity correction does not authorize changing a requirement; borderline classifications remain visible for the owning decision.

Update Chapter 3 source [17] and Chapter 4 source [14] to cite the repository's `docs/DELIVERABLE_CONCORDANCE_METHOD.md` Revision 2, §3.1, and D-GOV-44 as well as the originally supplied Revision 2. Do not state that all open runs adopted the new revision: D-GOV-44 explicitly preserves the App run's pinned Revision 1 pending its later rider.

Evidence: [concordance §3.1, lines 94–137](/Users/ryan/.codex/worktrees/da43/chirality/docs/DELIVERABLE_CONCORDANCE_METHOD.md:94), [bounded reconciliation, lines 67–77](/Users/ryan/.codex/worktrees/da43/chirality/workflows/bounded-reconciliation/WORKFLOW.md:67), [D-GOV-44 in-flight boundary](/Users/ryan/.codex/worktrees/da43/chirality/docs/governance_harness/_DECISIONS/D-GOV-44_concordance_claim_granularity.md:83).

### C34-06 — Make the actual delegation classes and role delivery explicit

**Operational clarification, preserving the existing account.** §4.3 correctly distinguishes roles from model capability, and line 2194 correctly distinguishes a brief from actual execution. A short addition would prevent readers from assuming that any native child is a correctly initialized TASK or that declared role tools are a proven sandbox.

Insert after line 2194:

> Chirality distinguishes managed `delegate_agent` sessions from delegated-harness-native descendants. Record the class actually used, the actual parent and child, the supplied full role and brief, and the limits the host enforces. Native child creation alone does not establish a role change, and a full-history fork alone does not replace a role. A role or brief restriction can be instruction-asserted in a broadly writable host; describe it that way rather than claiming sandbox enforcement. Record unavailable or unconfirmed context delivery as a limit on reliance.

Preserve line 2052's **declared** read-only ceiling: the current registry still declares `HELP_HUMAN` read-only. Do not “correct” it by inferring write authority from the broad host. Its wording can link to the current registry and clarify that an authorized manager or executor performs the write. The guide should separately explain repository role doctrine, managed Runtime configuration, and the actual host mechanism used for a given run.

Evidence: [Root delegation and host rules](/Users/ryan/.codex/worktrees/da43/chirality/AGENTS.md:174), [registry HELP_HUMAN ceiling](/Users/ryan/.codex/worktrees/da43/chirality/agents/registry.json:9), [runtime actual-enforcement boundary](/Users/ryan/.codex/worktrees/da43/chirality/docs/AGENT_WORKFLOW_RUNTIME.md:30), [fresh-role context and fork limits](/Users/ryan/.codex/worktrees/da43/chirality/docs/AGENT_WORKFLOW_RUNTIME.md:167).

### C34-07 — Repair source traceability and identify current method kinds

**Evidence correction.** Lines 1818 and 2617 promise a preserved accompanying source bundle. No such bundle was found beside the three original manual files. The v2 should link its actual review/source manifest rather than imply that missing ZIPs, complete archive contents, or an editorial report were inspected.

Replace the final sentence of line 1818 and the first sentence of line 2617 with a source note such as:

> The original archive citations preserve the manuscript's source provenance. This repository edition identifies the current counterparts examined in its dated review record; it does not establish that unavailable archive bytes match those counterparts.

Then link the source manifest actually delivered by the parent. Retain archive titles as historical citations unless their original files are available for correction.

In Chapter 3 source [5], add the current counterpart `.agents/skills/preparation/SKILL.md`; in §3.5 line 1399, change “the effective, source-qualified `preparation` method” to “the effective, source-qualified `preparation` skill”. Its historical archive called it a workflow, while the current setup contract calls it a skill. The current method still preserves existing files, including empty ones, and permits only structural preparation. Likewise use the current skill catalog identity when presenting `deliverable-consistency` in the agent guide; do not launch an obsolete role or workflow merely from an archive name.

Evidence: [preparation skill](/Users/ryan/.codex/worktrees/da43/chirality/.agents/skills/preparation/SKILL.md:1), [project-setup current contract](/Users/ryan/.codex/worktrees/da43/chirality/workflows/project-setup/resources/contract.md:38), [source-qualified preparation selection](/Users/ryan/.codex/worktrees/da43/chirality/workflows/project-setup/resources/method.md:87). The directory inventory, not a whole-disk search, establishes the limited bundle-availability observation.

### C34-08 — Keep the phase model visibly attributed

**Optional cross-chapter clarification.** The initial-DAG/30%, structural-confidence/60%, longer-horizon/90% account is the author's framework, not a measured percentage of completion or evidence that any current project passed a gate. Its source notes and Figure 4.10 already say much of this. If the parent finds no sufficiently prominent explanation in earlier chapters, add after Chapter 3's opening:

> The phase designations in this manual express the author's development model. They are not measured percentages of work completed, and they do not establish the current stage of any repository project. A project's phase transition is supported by its own adopted criteria, evidence, and human decision.

Do not invent an additional universal gate, numerical acceptance threshold, or blanket prohibition on revising a DAG after 60%. Preserve lines 2551 and 2573, which correctly keep the expectation revisable and reject a numerical completeness test.

## Lessons for the comprehensive agent guide

| Guide subject | Concrete operational lesson |
|---|---|
| Entry and current basis | Resolve the active checkout, read applicable Root/project instructions and the actual role, then the owning loop. Read its live pointer and linked phase cursor; inspect Git/worktree state and current evidence before repeating work. A pointer selects navigation, not authority. |
| App and Piping | Follow their persistent graph loop and source-qualified bundled graph/reconciliation methods. At this basis, the selected graphs belong to whole-corpus reconciliation runs with retained pins and gates. Show this as a dated example, not as a permanent next action. |
| Runtime | Follow migration acceptance, PRD/decomposition authority, the seven-carrier register, activation requirements, holds, handoff and receipts. The loop explicitly selects no inferred DAG priority. Do not copy the App/Piping no-receipt rule. |
| PEC | Read current Remaining, exact owner packets and reliance holds. The loop retains per-iteration discovery, gates, receipt validation and exact write fences. A PRD, concern register, or historical workplan does not open implementation scope. |
| Roles and dispatch | Type is responsibility, not complexity. Type 2 never delegates. Distinguish actual child launch, delivered role/context, parentage, and transport from a prepared brief. Record host enforcement separately from instruction restrictions. |
| Selection and graphs | Keep project DAG, local execution graph, and delegation hierarchy distinct. Name a node's required result, basis, writes and completion evidence. Select coherent work serving current intent, including enabling inputs, without inventing scope from a lifecycle label. |
| Local contracts | Establish the active production format before editing. Use SOW for current/new canonical production, or the active legacy kit where its transition remains valid. Do not reactivate archived forms. |
| Verification and review | Derive checks from criteria and current project profiles; confirm actual command/tool availability. Protect the oracle. Review the actual frozen candidate; later changes need affected coverage. Native-host claims need their required native evidence. |
| Reconciliation | Plan bounded document updates after stable results and before dependent use. Compare both directions; keep unimplemented commitments; lift stale mechanism detail under the adopted claim rule; leave lifecycle, scope, pins and formal DAG changes to their owners. |
| Continuity and closeout | One maintainer integrates graph returns. Recover active operations before reassignment. Use graph/results to avoid duplicate narratives only where the current loop permits; preserve all selected workflow outputs. Integration, node completion, Deliverable acceptance, issuance and release remain separate. |

For Runtime and PEC, these guide entries are entry-contract observations, not dispatch authorizations or a full project status audit. No claimed live prerequisite satisfaction was derived from a graph label alone.

## Source standing and limits

- **Current adopted App/Piping practice:** the September 22 integration record, manifests, instructions, loop files and routed notices establish persistent local graph traversal and bounded reconciliation for authorized development. They explicitly preserve in-flight run pins and gates.
- **Current governing method with project/run adoption limits:** the ratified concordance kernel, cycle doctrine, SOW standard and their decision records require the appropriate project or run basis. Their presence does not erase a local hold or prove downstream qualification.
- **Prospective interface:** `docs/AGENT_WORKFLOW_RUNTIME.md` labels itself a prospective v3 interface and says it does not establish host enforcement or downstream adoption. Its role/permission vocabulary must not be narrated as proof of a currently running managed provider.
- **Historical execution evidence:** selected App/Piping graphs retain Claude/Opus execution attribution. Preserve those facts as history; they neither identify this Codex review nor establish another qualified App MVP engine.
- **Author framework and examples:** stage percentages, illustrative graphs, proposal-rejection examples and specimen contracts explain the method. They are not actual project acceptance, validated engineering designs, dispatches or observed performance results.
- **Not verified here:** original archive bytes; the external theory texts named only in manuscript source notes; all workflow implementations and tool bindings; current remote-main status beyond the local review commit; current completion of either live reconciliation program. No external fact-check was needed for these bounded repository corrections.

All requested manual lines were examined. Remaining integration work belongs to the parent: apply selected edits to v2, build the guide, replace source-bundle promises with the actual delivered evidence links, and independently review the completed candidate.
