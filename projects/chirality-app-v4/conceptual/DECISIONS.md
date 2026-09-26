# Chirality App v4 — owner directions and decisions

Standing: **record of the owner's own directions and decisions.** Entries here
quote the owner. Agent interpretation of an entry is kept in
[`WORKING_RECORD.md`](WORKING_RECORD.md) or [`QUESTIONS.md`](QUESTIONS.md),
never here. A direction settles what it actually covers; it is not a product
requirement until the candidate PRD states it and the owner accepts that PRD.

New entries are appended. An entry is never edited to change its meaning; a
later direction supersedes an earlier one explicitly.

## OD — directions given in the opening brief (2026-09-25)

Source: the owner's opening message to HELPS_HUMANS in the session that
created this working root (preserved verbatim in the run record,
[`OPENING_BRIEF.md`](../execution/_Coordination/AgentRuns/V4-CONCEPT-20260925/OPENING_BRIEF.md)).
The quotations below are exact; the grouping and IDs are the agent's.

| ID | Subject | Owner's words |
|---|---|---|
| OD-01 | Undertaking | "Begin the conceptual undertaking for Chirality App v4.0. Resolve REPO_ROOT from this worktree and establish the new working root at projects/chirality-app-v4/ after inspecting existing state." Role: HELPS_HUMANS, Type 1. Workflow: `chirality-root:bundled:workflow:reverse-engineer-software`. |
| OD-02 | Reason for restarting | "Chirality App has developed through successive instantiations: software informed specifications, which informed another implementation. Each generation has reflected our evolving understanding of agents and the technology available to support them." "We want to recover that value while reconsidering the product's architecture and expression from its nucleus: a new PRD and coherent core documents." |
| OD-03 | Suppliers | "My direction is to build from capable existing agent harnesses and application foundations where appropriate. Investigate actual suitability before selecting one; no supplier has been chosen for v4." |
| OD-04 | Primary and secondary expression | "The primary product expression is workflow capability and an interface within applications I build, especially engineering design and analysis applications such as SWBPIPE. The standalone application is secondary: it gives the workflow-making persona a direct expression, while that persona can also operate through other applications." |
| OD-05 | Human and agent interaction | "Human and agent interaction should support shared understanding of meaningful objects, state, operations, results, and recovery. Examine structured interfaces, computer use, or combinations according to the activity. Shared access does not transfer human decision rights." |
| OD-06 | Project management | "Project-management capabilities also matter because coordinating agents at scale produces those needs." |
| OD-07 | Thesis carried forward | "Carry the complete docs/thesis directory forward unchanged, preserving its attribution and stated standing. Put any successor-specific interpretation outside those preserved files." |
| OD-08 | Manuals | "The manuals describe practices to try again, examine through use, and improve through feedback. Recover their purposes and conditions rather than automatically reproducing every historical mechanism." |
| OD-09 | References and archives | "Pin the investigation revision separately from the published v3.0.1 fallback release in sgttomas/chirality-app. Preserve both references." "Inventory relevant Git-ignored archives in the original checkout at /Users/ryan/ai-env/projects/chirality and establish stable read access." "Preserve the old projects and archives until I decide v4 has replaced the fallback." |
| OD-10 | Output and standing | "Develop a fresh PRD and supporting core documents with me. Keep source evidence, interpretations, proposed choices, and accepted commitments identifiable. Root governance applies; old product choices and execution structures do not automatically become v4 requirements." |
| OD-11 | First undertaking | "Start with the reference inventory, a proportionate investigation plan, and consequential product questions. Bring concrete exemplars, lessons, and alternatives into our conversation as the work proceeds." |
| OD-12 | First completion boundary | "The first completion boundary is an independently reviewed seed set presented for my acceptance. Identify its governing documents, preserved references, open questions, and conditions for further work." |
| OD-13 | After acceptance | "A fresh implementation session will start from that accepted seed set. It will establish its own decomposition, setup/initiation, production contracts, dependency mapping, and subsequent development route. Historical material remains available for investigation; consequential new findings must enter the seed basis explicitly before being treated as additional product requirements." |

## Decisions — owner's answers of 2026-09-25

Source: the owner's reply in session, preserved exactly in
[`OWNER_ANSWERS_2026-09-25.md`](../execution/_Coordination/AgentRuns/V4-CONCEPT-20260925/OWNER_ANSWERS_2026-09-25.md).
The question text and option wording referred to are in
[`QUESTIONS.md`](QUESTIONS.md) as of commit `866897631`. "Settles" states
only which option the owner's words select; where the words select no
option, the entry says so. Consequences and open follow-ups are recorded in
`QUESTIONS.md` (dispositions) and the working record.

| ID | Question | Owner's words (exact) | Settles |
|---|---|---|---|
| D-01 | Q-01 nucleus | "CORRECTION: Not the place where methods are made, those are made in each of the applications according to the needs and uses.  The standalone App is the App for Creating Workflows.  It is the exemplar of what then resides in various guises in the specific applications (but different workflows, skill, tools, etc.) though the same four agents are applicable across the board and still no expansion of numbers or roles is planned (but could yet still come about)." … "we can discuss this further to hone in on the best expression of the "working statement"." | Corrects the proposed statement; the working statement stays open for discussion |
| D-02 | Q-02 host integration | "I accept your recommendation." | Option D (one host-integration contract, used first by an outside controller and then by an embedded panel), with the embedded service as the leading topology pending the supplier experiments |
| D-03 | Q-03 workflow | "I accept your recommendation." | Option C (method guidance with declared checkpoints) |
| D-04 | Q-04 autonomy | "It needs to be option B because that's the only way to not over-simplify the work.  Let the user and the agent figure out how to best work with one another.  The outputs will be validated by the human to the degree warranted by the situation." | Option B (graduated autonomy); the sub-questions on classifier approval modes and always-reserved acts are not answered by these words |
| D-05 | Q-05 supplier | "A local model server is a requirement.  The harness must not be constraining, nor is it even the product at this point, so I just want the best tool for the job and the easiest to maintain.  T3 Code will cover a lot of ground …  But I need local model server to be on part as far as the harness goes. …" (full text in the preserved answers) | A local model server is required. No option letter selected; T3 Code named as the owner's current leading candidate, subject to local-model support. The harness is not the product. |
| D-06 | Q-15 distribution | "v4.0 should be Mac first.  Get that working well and we can consider other OS compatability.  The user should have oAuth, API, and local model as the options available to them, and potentially all at once." | Mac first for v4.0; OAuth, API key and local model available to the user, possibly simultaneously |
| D-07 | Q-06 records | "I accept your recommended proposal." | The proposal: host keeps domain truth; workflow definitions, owner decisions and accepted records as files; harness stores operational; each run leaves a compact record linking host receipts |
| D-08 | Q-07 users and hosts | "I am preparing PEC, yes.  And Domains.  Both must be considered as connectors to the App.  Neither depends on the other.  The App consumes what each of those two prepares." | PEC and Domains are connectors whose prepared outputs the App consumes; they are independent of each other. (The persona and host recommendation was not otherwise addressed.) |
| D-09 | Q-08 project management | "I agree with your recommendation.  There's more to it than that, but option B is clearly the choice of those three that I will agree on." | Option B for v4.0; the owner signals further scope to discuss |
| D-10 | Q-09 roles | "I accept your recommendation." | Roles shown in the standalone app; in hosts they recede behind a single agent seat and workflows |
| D-11 | Q-10 replacement | "I approve option (b), which builds on what option (a) proposes." | Replacement condition: one live embedded journey in SWBPIPE from request to human acceptance, building on the standalone core loop at v3.0.1's level. Item (c) was not selected. |
| D-12 | Q-11 build method | "I think we look at a radically different way of developing this project. … So that structure is good and will be retained.  But to guide the work graphs we have the agents follow the Project Management manual according to the Agents User Manual, is my proposal.  We should discuss this." (full text in the preserved answers) | Not a decision: the owner's proposal, opened for discussion |
| D-13 | Q-12 review | "I accept your recommendation.  But we can use a Claude reviewer with a different model if we get to that point and the Codex session isn't available." | Codex reviewer, with a Claude reviewer on a different model as fallback |
| D-14 | Q-13 archives | "Yes." | Make the protective clone (done 2026-09-25; see `reference/archives/ARCHIVES.md`) |
| D-15 | Q-14 v3 examination | "I have updated to v3.0.1 now and it's open on my machine." | v3.0.1 is installed and available for Stage E1 |
