# Owner direction transcript — Root cross-loop carrier unblock

Classification: `CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING RECORD`

Owner: Ryan Tufts

Date: 2026-08-21

> Steer (this run): STANDING DIRECTION — Root session steer (cross-loop unblock: validator doctrine alignment + carrier decisions). This session's shape is owner-directed; measure it against this direction. The Root loop's own instruments, registers, and receipt rules govern protocol and fences throughout; K-AUTH-1 holds — every disposition below that is marked human-only comes back to me, not to any agent.
>
> Context. Both project loops are now waiting on Root. The App loop's DEL-08-04 Remaining names TM-ROOT-125 as its external dependency; App TM-APP-032 waits on TM-ROOT-117; App TM-APP-027/028 wait on a DEL-02-06 compatibility completion. This session exists to move those three carriers.
>
> Objective 1 — TM-ROOT-125: align validator and allowlist with the ratified Agent 0 direct-Agent-2 dispatch doctrine (the engineering product of this session). AGENTS.md (2026-08-02) and agents/AGENT_HELP_HUMAN.md (PR #569) permit Agent 0 to directly dispatch bounded Agent 2 instances (TASK or opted-in ephemeral generalists) under sealed briefs, but tools/validation/validate_agent_instructions.py still enforces the superseded rule (lines ~270-271 raise AGENT0_CHILD_TYPE for any non-Agent-1 entry in an Agent 0 subagents allowlist; ~272-280 raise GENERALIST_PARENT_TYPE for allow_generalist_agent2 on a non-Agent-1 file), and tools/validation/test_validate_agent_instructions.py (~lines 167-183) pins that behavior. Amend the validator and its tests so an Agent 0 file may allowlist canonical TASK and carry an explicit generalist opt-in, while every other superseded-rule rejection remains fail-closed; then update AGENT_HELP_HUMAN.md frontmatter to declare the now-lawful children. These are instruction-surface changes: ship the G4 tranche manifest(s) in the same tranche and update any policy test pinning the touched text. On landing, close TM-ROOT-125 per your register's rules and route the reciprocal coordination notice to the App loop naming exactly what changed, so App can run its DEL-08-04 post-root cross-surface integration check against its already-landed harness implementation (App commit ac2cd801a, App Receipt 172). The notice is coordination, not authority — App adopts under its own instruments.
>
> Objective 2 — TM-ROOT-117: prepare the D-APP-48 successor-identity decision packet (decision preparation, not implementation). TM-ROOT-117 is the Root carrier for App's TM-APP-032 wait. Prepare the owner decision packet: either name an exact accepted successor identity for the D-APP-48 mechanism with its human-acceptance record, or propose re-scoping App's trigger. Present the packet to me as a decision slate with a non-binding recommendation and stop — the ruling is mine. On my ruling, close the row RESOLVED_BY_DECISION per your register's rules and route the reciprocal notice to the App loop.
>
> Objective 3 — DEL-02-06 compatibility completion: assess and advance or return a slate. App TM-APP-027/028 wait on Root DEL-02-06 (PKG-02, Generic Runtime Stewardship and Release Assurance) accepting a compatibility-completion package: the positive-decimal Root compatibility epoch plus the complete six-member binding manifest. Determine from DEL-02-06's live activation state what its instruments authorize now. If bounded production toward that package is lawfully selectable, take the largest bounded slice; if it is gated on owner decisions, return the exact decision slate instead — do not manufacture planning records to simulate progress. Check your inbound coordination surfaces for the App loop's routed carriers on this subject before starting.
>
> Closeout. One tranche, one branch, one PR against main; commits in dependency order; receipt per your loop's local rules with transcription of this direction as owner steer; no artifact-proof label; no merge — PR review and merge remain owner acts. If an objective fails its checks or dead-ends on a missing basis, land what passed, record the exact blocker, and stop. Decisions needing me: park them in one list at the end; do not let them stall the other objectives.

## Effect boundary

This transcript records the owner's in-session direction. Human-only rulings
identified in that direction remain pending until the owner returns an exact
selection. The transcript is evidence for the bounded tranche; it is not a
substitute for the Root register, DEL-02-06 acceptance instruments, App loop
adoption, PR review, or merge.
