# Packaged UI refinement candidate

Status after the owner's additional live checks: the artifact below is preserved
historical evidence. Live checks found and repaired recovery/cause and panel-width
defects; the replacement package waits for independent review and merge. See
`LIVE_VERIFICATION_20260912.md`. This hand-off will be updated with the replacement
artifact and the filled-in manual checklist after that build succeeds.

Candidate source: `85f19f019589b798331c804c4b206e34849eeab5`, merged PR #775.
Version: `3.0.0-rc.1`, macOS Apple Silicon, macOS 15 or later.
This hand-off records a review candidate, not trial acceptance or publishing approval.

## Artifact and installation

DMG: `/Users/ryan/.claude/chirality-build-ui-85f19f019-out/Chirality-3.0.0-rc.1-arm64.dmg`.
The exact build results, artifact digest and signature state are in
`BUILD_EVIDENCE_20260912.md` beside this file.

Notarization, stapling and the native checks are owner acts. The agent has not
launched this candidate. The latest handoff's guarded-launcher restriction remains
in force for agent-assisted trial launches; an older checklist's direct-launch
wording does not override it. Do not use the R17 installation, userData or Codex
home for this trial.

Keep the previous A2 build and its installer until the replacement is verified.
Both builds report `3.0.0-rc.1`, so identify the old build by source `388de6973`
and this one by `85f19f019`, as well as recording the version strings.

No release feed is configured. Check for Updates currently reports that fact;
this candidate is installed manually, and it does not install itself or relaunch
the App. Setting up the publishing feed is outside this hand-off.

## Owner checks

Use the full `UPDATE_PRESERVATION_ACCEPTANCE.md` beside this file. Its practical
sequence is:

1. In the existing A2 installation, open chats in two folders. Leave an unsent
   draft with a file attachment and selected workflow, execute a plan revision in
   the other chat, pin a chat, set Appearance, and note the current folder and
   each chat's model, reasoning, role and permissions.
2. Confirm About Chirality explains the manual update path. With no configured
   feed, Check for Updates should only report that no source is configured.
   The conditional Download/running-work note cannot be exercised while no
   download is offered; do not report that branch as a live pass.
3. Finish or explicitly stop running work, then quit the App. Closing its window
   and quitting the application are different: a closed window permits work to
   continue; quitting stops it.
4. Install the candidate over the previous A2 application and reopen it with the
   same A2 userData/profile. Using a fresh profile for this particular comparison
   would not test preservation. Do not copy or inspect credential files.
5. Confirm both chat histories, unsent draft and attachment/workflow references,
   per-chat folders and settings, plan execution attempts, saved project/personal
   workflows, pinned chats, layout, Appearance and sign-in survived. Note any
   missing or changed item before proceeding.

Then complete the distinct packaged checks in
`../APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md`: post-staple
signature assessment, quit/relaunch and continued conversation, Chirality-scoped
sign-in/sign-out with another Codex client unchanged, and window closure during
tool work followed by recovery without duplicate execution. Use an isolated A2
trial profile for account testing; do not mix that fresh-profile check with the
same-profile update comparison. OAuth and 2FA remain yours.

The preservation checklist is still awaiting your observations. A failing
observable is a candidate defect to report, not something to repair by clearing
user data or resetting the account.

## Known observations and review notes

The previous session observed an old chat named **Assistant** (15:33, no recorded
messages) fail to start with `ENGINE_UNAVAILABLE`, while a different older chat
resumed normally. That session recorded it as outside its refinement changes.
This packaging run has not investigated or established its cause. Report a
recurrence separately from success on newly created chats.

The third independent source review returned PASS. It left these notes, which
are distinct from confirmed blocking findings:

| Reference | What remains |
|---|---|
| R-A | Keyboard focus on Specialist category headings changes colour but has no outline; visibility may be weak. |
| R-B | Declining New chat during a cross-folder open removes an existing notice for that target folder. |
| R-C | An unbound chat with an unsent draft can switch folders without confirmation, following the existing draft behaviour. |
| R-D | The update controller has an unused stored reference; no observed user failure. |
| R-E | Resolved before PR #775 merged: the manifest now names reviewed candidate `51faa0a12`, and only records changed afterwards. |
| R-F | An instruction-integrity test timed out once during concurrent/full-suite load and passed alone. The source file was outside the refinement diff; this is retained evidence, not proof that rerunning repaired a defect. |

Earlier reviews also retain potential edge cases: canonicalized or unavailable
folder handling; a brief Send-enabled interval while a running chat reconnects
(Runtime rejects a duplicate turn and restores the draft); restoring a document
switches the sidebar to Files; per-session draft keys have no eviction; and
event-driven rendering may need attention on long histories. A cancelled Locate
folder operation may leave a pending selection that later reports the chat was
not found. Some UI paths, including long-stream follow and the revised sign-in
ceremony, lacked direct live verification in the refinement session.

The complete records are `returns/REVIEW_RETURN.md`, `REVIEW_RETURN_2.md` and
`REVIEW_RETURN_3.md`. Earlier actionable findings were fixed and reviewed; their
historical failing verdicts are not new blockers against the merged candidate.
Agent review is not owner approval.

## Deferred cleanup and discussion

- Preserve `/Users/ryan/.claude/chirality-build-a2` and
  `/Users/ryan/.claude/chirality-build-a2-out` until you confirm verification.
- Keep the fresh build checkout/output and evidence available for diagnosis.
- When you share your documentation, return to the prior session's
  `refinement-notes.md` at the scratch path recorded in `HANDOFF_20260912.md`.
- The product instruction draft remains the separate planning document
  `plans/chirality_product_agents_md_direction_2026-09-12.md` at repository root.
  This build does not activate that draft or complete the final prompt discussion.
- Publishing still requires your explicit direction after the trial.
