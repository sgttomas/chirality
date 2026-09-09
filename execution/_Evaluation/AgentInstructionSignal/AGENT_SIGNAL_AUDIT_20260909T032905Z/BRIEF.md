# Agent instruction audit — sealed brief

Parent: HELPS_HUMANS, direct human entry. Decision authority: the user.
Authorization: the user requested separate subagents to audit current instructions and write a proposal for each agent, and directed positive task framing.
Basis: HEAD 781b478176db46ca66ebd38991607612e0ce9338; subject bytes pinned in SOURCE_MANIFEST.json. This is the inspected worktree basis. Reports are candidate decision support derived from it.
Delegation: delegated-harness-native through Codex collaboration. Each child is an ephemeral Agent 2 auditor. Declared scope and non-delegation are instruction-asserted; actual harness execution supplies parentage. Each child executes its bounded assignment directly.

## PROTOCOL
Read every assigned agent instruction in full. Identify the strongest recurring pattern of attention, judgment, method and responsibility it is intended to evoke. Propose the clearest, most concise expression that retains what makes that agent distinct and useful.

Examine PROTOCOL, SPEC, STRUCTURE and RATIONALE as complementary ways to express that core. Examine the surrounding material by the contribution it makes to the role, its actual execution environment, and its interfaces. Use concrete evidence to explain choices to retain, compress, relocate or remove content. Compare existing skills, tools, callers and runtime consumers where relevant. Treat observation, interpretation and proposed changes distinctly.

Inspect actual runtime and validator support when deciding where a responsibility can reside. State unverified dependencies as uncertainties. Develop concrete behavioral probes by which the user could judge a future candidate. Focused agent methods and the four-section form are valued design features in this conversation.

## SPEC
Cover exactly the subjects in your group. Every agent receives a specific proposed disposition and actionable section-level changes, supported by source line anchors and brief excerpts. Explain the contribution of retained material as clearly as the reason for changed material. State the governing decisions, machine consumers, compatibility implications and user decisions implicated by each consequential change.

The proposal is assessed for faithful role distinction, coherent reasoning, evidence, actionable changes and honest uncertainty. Static inspection supports design hypotheses; behavioral probes describe future evidence to collect.

## STRUCTURE
Read scope: relevant files inside this repository, including subject instructions, AGENTS.md, docs/WORKFLOW_COMPONENT_STANDARD.md, applicable governance decisions, skills/README.md, live skill contracts, tools/REGISTRY.md, validators and implementation/caller evidence. Historical material is evidence of prior choices. Model capability assumptions are session-specific per D-GOV-17.

Write scope: your assigned child output directory only. Repository subjects remain read-only. Execute locally with read/search tools and report-writing tools. Git use is read-only; all network, publication, execution of production workflows and shared-state changes are outside this assignment.

Outputs:
1. PROPOSAL.md — one card per agent: distinctive core (2–4 sentences), proposed disposition (RETAIN/SLIM/MERGE/CONVERT_TO_SKILL/CONVERT_TO_TOOL/RETIRE), concrete changes covering major sections/functional blocks, source anchors, retained essentials, relocation destination (existing/candidate/TBD), governance/harness dependencies, and a behavioral probe.
2. COVERAGE.json — per role: source path, SHA-256, read_complete, major sections examined, disposition, uncertainties.
3. RETURN.md — summary, source evidence, outputs, limitations, blockers and handoff.

Write proposals at the level needed for the user to decide what should change. Full rewritten instructions can be a later assignment. A concise shared explanation may serve multiple cards when each card identifies its concrete application.

## RATIONALE
The user wants to see the role core more clearly and understand which surrounding instruction material helps express or execute it. The audit tests how to strengthen that signal, using ontology, epistemology, praxeology and axiology as perspectives where useful. Current governance supplies the execution boundary; proposed revisions to it are explicit decision candidates.

Parent fan-in checks all 34 subjects covered exactly once, unchanged source hashes, substantive per-agent recommendations and evidence, and compatibility across both groups. Parent produces a consolidated proposal and explicit handoff. All outputs remain candidate, derivative audit evidence pending user judgment.
