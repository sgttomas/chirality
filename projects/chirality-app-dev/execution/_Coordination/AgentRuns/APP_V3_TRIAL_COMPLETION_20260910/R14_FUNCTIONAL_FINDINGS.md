# R14 functional trial findings

Build source05f11d5eb54a232b8b324e664fd59e3d500996af; Stage23. Lead HELP_HUMAN direct Computer Use. Owner directed broader functional testing before one consolidated repair tranche; do not rebuild per finding. Synthetic project /Users/ryan/dev/chirality-trial-20260911-r6. No publishing.

## Confirmed passes

- Guarded launch automatically starts/connects Runtime. Native folder picker binds existing project; no manual daemon operation.
- Owner completed Chrome OAuth/2FA; App reaches Ready, catalog controls enabled.
- New default HELP_HUMAN/gpt-5.6-sol low chat completed short response, returned idle. Session dee05735-3afb-4a92-a4bf-f4ff41ef2720.
- Continuing second turn: Attach files native picker selected trial-diagram.png; chip sent; actual Codex answered dominant color red, returned idle. This previously failed in R13; R14 cleanup repair now passes this native path.
- Plan Mode selectable separately from reasoning/permissions in continuing chat. Generated native plan revision1; history includes Native plan revised.

## Findings for consolidated repair

1. **Plan text rendering**: live Current plan renders JSON object including id/type/text and escaped newlines rather than plan Markdown. Actual native plan is object {id,type:plan,text:...}. Reproduction: select Plan Mode and request three-step report plan. Source nativePlanText in chat-panel.tsx and selected-session-replay-lens.tsx JSON-stringifies nonstrings. Also inspect export and Execute/Save workflow composer construction for same semantics. Preserve raw source events/history, project only meaningful plan text to user.
2. **Routine metadata clutter**: every turn exposes Recorded instruction basis/10supplied plus Instruction basis recorded; footer repeatedly shows unavailable primary activity/turn duration. These remain inconsistent with owner minimal primarysurface direction. Keep inspection available deliberately.

## Still to exercise

Plan revision, save/export/execute; workflow library selection and chat-driven saving; file viewer/inline links; alternate model/reasoning and directentry roles; chat search/history/reopen/rename/archive/restore; settings/appearance/About; interruption and account-status consequences; restart/persistence.

## Broader UI pass — September 11 continuation

- Native revision2 generated from a requested change; revision1 remains inspectable. Successful plan-only turn incorrectly shows “No assistant text was returned for this turn.”
- Save plan… produced no dialog or visible outcome on AX and physical-coordinate clicks. Source chat-panel.tsx savePlanRevision uses window.prompt, unsuitable for this Electron surface. Replace with native save flow; inspect overwrite path using window.confirm too.
- Save as workflow in chat populated editable draft, switched Plan Mode to Chat, retained bounded save-only instructions, but included JSON plan wrapper. Sending failed substantively: agent reported local code-mode host failed to start twice; no workflow created. This is a release blocker for tools/workflow creation, even though chat/image/native plan events pass. No repeated build attempted.
- Account menu has account/sign-out, Settings, Appearance, About. Dark/light toggles visibly work and light restored; About reports3.0.0-rc.1.
- Settings exposes “Client lacks models:read”, Anthropic/OMLX API-key panels and “Client lacks credentials:read”. Wrong for Codex-only MVP and needs cleanup without granting wider authority.
- Files Markdown viewer and image viewer pass (README84bytes; red trial image134bytes). Document metadata is prominent; optional inspection can retain it.
- Workflow central list, categories, search, inspect, selection/removal pass. Selecting research-orchestration keeps HELP_HUMAN role. Draft ordinary text plus selected method persists across panel switches; search/inspection state resets. Nothing sent for this selection test.
- Workflow page still prominently exposes Skills reference, verbose headings/banners, compatibility details, and obsolete legacy methods alongside new methods. Owner already requested compact UI and background skills. Keep explicit historical compatibility accessible without promoting it to normal choices.
- Agents tab shows Type0 / HELP_HUMAN / Top-level, appropriately concise.
- Chat rename native menu → app dialog → saved title “R14 functional trial” passes.

- Model catalog menu offers sol/terra/luna/5.5/spark; terra supports low/medium/high/xhigh/max/ultra. Selected terra medium, changed role to HELPS_HUMANS, and model silently reset to sol low. Re-selected terra medium then completed two no-tool turns. Direct-entry menu contains precisely Help Human/Helps Humans/Working Items.
- Both relative [Open trial README](README.md) and absolute [Open README](/Users/ryan/dev/chirality-trial-20260911-r6/README.md) assistant links render as localHTTP anchors and clicks do nothing (AX and physical clicks). Same file opens in Files pane. Native file navigation integration defect.
- Rename/search title, archive, archived listing, restore pass on synthetic chats.
- Clicking an earlier chat opens a verbose read-only diagnostics pane while main composer remains in another chat; Continue this chat resumes original role/model and native plan revision2, but visible history now omits ALL user messages and attachment chips. It shows assistant-only transcript with generic Assistant labels. This is a major conversation continuity/presentation defect; preserve full user+assistant+attachment history and normal chat entry.

- After Continue this chat resumed original HELP_HUMAN session, sent bounded1500-word no-tool interruption test and clicked Interrupt while Running. Result was ENGINE_UNAVAILABLE: Codex session closed (not clean cancelled). Draft restored. Next short no-tool follow-up failed ENGINE_UNAVAILABLE: Fresh candidate differs from its v2 instance admission. Do not infer account fenced or remove protection; diagnose resumption/interrupt/admission ownership separately. No auth/binding files touched.

## Consolidated implementation status

Source repairs complete with independent review/backcheck PASS: plan text/nativeexport/plan-only response; modelchoice acrossrolechange; acceptedusertext recovery and newattachment history; directchatentry andwrongcomposer guard; Codex-onlysettings andminimalmethod/statusUI; conversation-ownedfilecatalog andproperinlinecode; nativeinterruption with genuine terminal and nextadmission. Fullsuites plus isolatedtimingfailure rechecks pass as documented RUN_LOG. This is source/controlledadapter evidence, not nativeacceptance. No new App build yet.

Native rerun outstanding: actualtool execution and workflow creation/catalogrefresh aftermissinghost addition; plan export and executedplan; user+attachment replay/restart; repairedlinks and role/modelchoice; normalinterrupt followedbysuccess withoutsign-in reset. PDFdefault-app fallback was not re-exercised during this broadpass. Preserved R14 account is now sign-in-required; do not edit its auth/binding files to recover.
