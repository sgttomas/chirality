# Chirality 3.0.0: owner trial notes

Status: the first signed package is preserved, but it is held from public
distribution while the reported production dependency advisories are repaired.
A replacement artifact will be identified here after review and verification.

Source: `9eaddb5965642a783ad700743eecdf876e9e0104`, merged through
[PR #778](https://github.com/sgttomas/chirality/pull/778). The merged tree equals
the independently reviewed candidate. All required CI passed, including 364
Runtime tests and 2234 frontend tests; four frontend tests remain explicitly
skipped. Packaging evidence is in `BUILD_EVIDENCE_20260913.md`.
This record is not publishing approval.

Preserved first installer: `/Users/ryan/.claude/chirality-build-user-journeys-20260912-out/Chirality-3.0.0-arm64.dmg`
(337,955,318 bytes). SHA-256:
`321a4de9c8155be1fcd0a24f3aebfae55693df181a3151c5ad16952ef8171cb1`.
The App is Developer ID signed; Gatekeeper reports Unnotarized Developer ID
until the owner's notarization/stapling step. The installer has not been
published or installed over the owner's application.

## What changed

- Progress stays with the active assistant response. Separate native messages,
  reasoning summaries, tool activity and the final answer retain their boundaries.
  The Activity panel remains available.
- Native questions and approvals appear in the conversation. Chats can indicate
  that an answer is needed. Native work checklists, observed delegated agents
  and running-turn steering are available where Codex supplies them.
- Plan Refresh no longer shows background polling as repeated manual refreshes.
- The core `create-workflow` method is included in the guidance. Workflows created
  or revised in chat become discoverable without manually refreshing the library.
  Skills continue working in the background, with their browsing UI hidden.
- The first folder picker starts at home; subsequent use remembers the explicitly
  chosen folder. Home is not automatically made into a project.
- Native attachments can be chosen outside the project. The chosen file is copied
  into that project's `.chirality/attachment-inputs` folder, retaining its name.
  This does not extend the agent's access to the source folder.
- Continuing chats stay associated with their own project, even when another
  project's conversation is used. A booted chat can recover from an attachment
  failure before its first successful Codex turn. Open file previews refresh after
  the conversation updates the file.

## What the campaign established

Eight real, fictional knowledge-work journeys passed independent artifact review:
meeting actions, venue selection, conflicting guidance, workshop planning,
monthly briefing, supplier comparison, recurring operations and deadline changes.
The recurring workflow was saved, reused, revised and reused across three actual
cycles. Additional native checks exercised questions, steering, Stop and resume,
approval denial and renewal, folder selection and attachment delivery.

These were real Codex sessions on production source, with overlapping model work.
They were not observations of actual novice customers or one hundred prior chats.
The signed package receives its own build and integrity checks; development
observations do not establish install-over preservation.

## Short final check

Use your normal intended Chirality profile for the install-over comparison. Keep
both installers. Do not substitute the retired R17 profile or a fresh empty profile.
The existing full inventory is in
`../APP_V3_UI_REFINEMENT_20260912/UPDATE_PRESERVATION_ACCEPTANCE.md`; its older
artifact names are historical. Use this campaign's build record for the new one.

1. Before quitting the previous installation, note two chats in different folders.
   Leave one with an unsent draft, attachment and selected workflow; retain a plan
   in the other. Note appearance, folder, model and reasoning selections.
2. Quit, install the new candidate, and reopen. Confirm those chats, draft,
   attachment, workflow, plan and settings remain, and the account is still signed
   in. Confirm About reports `3.0.0`.
3. Continue one retained chat with a small request. In another, ask for a short plan,
   answer any question, execute it, then use **Turn into workflow**. Find the saved
   workflow and reuse it in a fresh chat with changed inputs.
4. Attach one harmless file through the native picker and ask about its contents.
   Inspect a saved result through its chat link. Check that progress, questions and
   the final answer are easy to follow.
5. Open About and Check for Updates. It should report the public release result
   without installing anything. Report issue should open the public GitHub issue
   page without adding chat or account content.

Existing edited instructions are preserved during an update. Settings lets you
inspect them and restore the new defaults with a backup. Review the new core
workflow guidance there if your previous copy predates it. New installations seed
the current product guidance automatically.

## Limits to carry forward

- Native agent status only reflects observed events. A primary turn ending does
  not prove every child completed, and missing assignment/result details remain
  unknown. Other chats' needs-answer indicators have bounded polling latency.
- The campaign saw one recoverable binding error when two browser renderers
  initialized concurrently. Ordinary folder selection recovered it; later
  overlapping work passed. The standard desktop has one main conversational view.
- Selected attachment copies are retained for retry and history. Removing a chip
  does not reclaim its staged copy in this release.
- The earlier UI review's keyboard-focus contrast, declined-folder notice and
  unbound-draft folder behavior remain follow-up observations, not claims of
  newly established defects. Its historical manifest and timeout notes are
  superseded by this candidate's passing validation and scoped fixture repair.
- Notarization/stapling, install-over acceptance, the final guidance discussion
  and explicit publishing direction remain owner milestones. Prior installers,
  worktrees and evidence stay preserved until verification.
