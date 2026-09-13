# Chirality 3.0.0: final release notes for the owner

The automatic-update fix is merged and the final installer is signed,
notarized and stapled. The owner authorized publication and subsequently
directed this agent to complete notarization using the existing Apple setup.
The [public v3.0.0 release](https://github.com/sgttomas/chirality-app/releases/tag/v3.0.0)
is live. See `PUBLIC_RELEASE_20260913.md` for the verified publication record.

Source: `6f41f93e74b31796302fd45a228ebeabdcd5dd0e`, merged through
[PR #781](https://github.com/sgttomas/chirality/pull/781). It includes the
journey/UI work in PR778 and dependency repair in PR779. The merged tree matches
the reviewed and tested candidate. Required CI passed with 364 Runtime tests
and 2238 frontend tests; four frontend tests are explicitly skipped. Native
startup showed a completed automatic check without pressing Check for Updates.
Controlled integration establishes the future-release badge and six-hour cadence.

Installer: `/Users/ryan/.claude/chirality-build-3-publish-20260913-out/Chirality-3.0.0-arm64.dmg`
(338,046,035 bytes, macOS Apple Silicon). Final post-staple SHA-256:
`8841144cbb3d90237295d0e2317f30e0bba58423d1e71a0bbf6f3b31f5821c85`.
The adjacent `.dmg.sha256` file records that exact downloadable artifact.

Developer ID signing and the packaged instruction/supplier/version checks
passed. Actual ASAR checks confirm the new startup/six-hour/cleanup wiring and
the retained dependency repairs. Apple accepted submission
`e8a2a95a-9851-4050-a187-175b98ed7a30`; stapler validation passed, and Gatekeeper
accepted the actual App mounted from the final DMG as Notarized Developer ID.
The final DMG has not been installed over the owner's App by this agent.
`BUILD_EVIDENCE_FINAL_UPDATES_20260913.md` preserves the original packaging
result; `PUBLIC_RELEASE_20260913.md` records its subsequent notarization.

Install this final download manually if your trial App already reports 3.0.0.
The checker compares version numbers and will not offer another 3.0.0 build.

All earlier installers, worktrees and their historical build evidence remain
preserved. This final installer supersedes the earlier source56c9f538d package
because it includes the automatic-update fix.

## What changed

- New releases are checked quietly at startup and every six hours while the App
  runs. A newer stable release produces the existing visible Update available
  indicator; downloading and installing stay explicit.

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
- Next, sharp and nanoid use the reviewed patched versions. The unused image
  optimizer is disabled; the actual production HTTP check confirmed normal
  App/static responses and refusal of optimizer requests before signing.

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

## Preserved installation checks

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
5. Open About after startup. The App should already have checked the public
   release feed automatically. Check for Updates remains available; neither
   path installs anything. Report issue should open the public GitHub issue
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
- The final production dependency audit has zero high or critical findings.
  One existing moderate PostCSS advisory remains, reported on PostCSS and its
  Next dependency row. Development-only advisories are recorded separately in
  the build evidence; this is not an entirely clean dependency audit.
- The earlier UI review's keyboard-focus contrast, declined-folder notice and
  unbound-draft folder behavior remain follow-up observations, not claims of
  newly established defects. Its historical manifest and timeout notes are
  superseded by this candidate's passing validation and scoped fixture repair.
- The owner authorized publication after the automatic-update fix and later
  authorized this agent to complete notarization, which passed. The earlier
  install-over checklist remains useful evidence to collect; that acceptance is
  not asserted here. Prior installers, worktrees and evidence remain preserved.
