# Independent frontend recovery review

**REVISE: one P2 identity finding.** Independent TASK / gpt-6-astra medium, no delegation. All ten `FRONTEND_SCOPE.json` postimage hashes matched at review; no native execution or full suite run.

Final backcheck: **PASS; finding resolved.** Updated postimages require authoritative v3 roleId / legacy persona equality and reject missing identities. Four focused no-send conflict regressions cover the gap. All updated hashes match; see COMBINED_REVIEW.md. The original finding below is preserved as review history.

`chat-panel.tsx:719–724,772` checks a reconciled session's ID and project root but does not check its current role. It then sets `nextSession.persona` to the locally selected role. A same-session record whose role changed after the pending/history snapshot is accepted as though it still had that old role; `submitDraft` sees `roleChanged === false` and skips explicit role replacement. Consequently the UI can label the next prompt with one role while Runtime executes its current different role. Compare v3 `roleId` (and legacy persona where present) against the pending role before accepting reconciliation; reject conflict or explicitly coordinate the role change. Add a same-ID/root, changed-role regression proving no user prompt is sent.

Otherwise the bounded recovery design is sound: retained created identity prevents extra create/boot calls, three boot markers gate new v3 history continuation, unconfirmed states preserve the draft, model/effort remain fixed, and absent legacy bootstrap flags preserve compatibility. Saved-message error copy is conditional on the pre-prompt path rather than claimed for arbitrary transport errors. Existing focused test evidence was inspected without duplication.
