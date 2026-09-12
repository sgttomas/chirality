# Packaged UI refinement candidate

Status: PR #776 is merged with all three CI checks passing. The source includes
the live recovery fixes, editable shared guidance, automatic role delivery, public updates,
Report issue and Turn into workflow. Its single replacement package is complete
and signed, awaiting owner notarization and trial acceptance. See
`LIVE_VERIFICATION_20260912.md` and `PRODUCT_GUIDANCE_AND_UPDATES.md`.

Candidate source: `26657ff9080efbba7ec1e71e6f1d08731462de0f`, merged PR #776.
Version: `3.0.0-rc.1`, macOS Apple Silicon, macOS 15 or later.
This hand-off records a review candidate, not trial acceptance or publishing approval.

## Artifact and installation

DMG: `/Users/ryan/.claude/chirality-build-ui-recovery-20260912-out/Chirality-3.0.0-rc.1-arm64.dmg`.
DMG size: 337,427,404 bytes. SHA-256 before notarization/stapling:
`d3d32be65e515d48035fd923b08870a30f3cde2f42d5c04558e2153746408caf`.
The sequential build, artifact identity, dependency boundary, instruction bundle
and strict signatures passed. Gatekeeper reports Unnotarized Developer ID;
that check awaits owner notarization and stapling. Exact results are in
`BUILD_EVIDENCE_REPLACEMENT_20260912.md` beside this file.
The earlier `85f19f019` package and `BUILD_EVIDENCE_20260912.md` remain historical.

Notarization, stapling and the native checks are owner acts. The agent has not
launched this candidate. The latest handoff's guarded-launcher restriction remains
in force for agent-assisted trial launches; an older checklist's direct-launch
wording does not override it. Do not use the R17 installation, userData or Codex
home for this trial.

Keep the previous A2 build and its installer until the replacement is verified.
Both builds report `3.0.0-rc.1`, so identify the old build by source `388de6973`
and this one by `26657ff90`, as well as recording the version strings.

Check for Updates reads the public Chirality App release repository. Checking
does not download or install anything; Download opens the browser when a newer
stable version exists. This candidate does not install itself or relaunch the
App. Report issue opens the public GitHub issue form with no logs or user data
attached.

Settings now opens the editable shared AGENTS.md and offers Restore default
with a backup. Common guidance and the active role are supplied automatically;
fresh named children receive their intended role. Edits apply at a verified idle
boundary and prior instructions remain in history. Codex's own base and native
project instruction discovery remain in place. All instructions are open source.

## Owner checks

Use the full `UPDATE_PRESERVATION_ACCEPTANCE.md` beside this file. Its practical
sequence is:

1. In the existing A2 installation, open chats in two folders. Leave an unsent
   draft with a file attachment and selected workflow, execute a plan revision in
   the other chat, pin a chat, set Appearance, and note the current folder and
   each chat's model, reasoning, role and permissions.
2. Confirm About Chirality explains the manual update path. The old A2 build
   reports that no release source is configured.
   In the replacement, Check for Updates uses the public releases. At source
   verification it correctly reported Up to date against public v2.0.0. Leave
   conditional Download behavior unverified if no newer release is offered.
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
6. Record the two source revisions, artifact hashes and version strings with
   your observations. Both installers report the same version, so that label
   alone does not identify which build was tested.

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

Final source review passed on `3ad6fac0d`, all 104 changed paths; later changes
before merge contain only the review return and run log. Full Runtime 342 tests
and frontend 2185 tests pass, four existing skips. Primary and fresh-child
guidance, edits after restart and without restart, Restore default, public
updates and Report issue were tested directly. Temporary probes were removed
and the owned development instance stopped.

The earlier third independent source review left these notes, which
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
- The saved prompt direction is now implemented at
  `projects/chirality-app-dev/instructions/AGENTS.md`, with its editable App
  copy available through Settings. Review its behavior and wording before
  publishing; further wording decisions remain yours.
- Publishing still requires your explicit direction after the trial.
