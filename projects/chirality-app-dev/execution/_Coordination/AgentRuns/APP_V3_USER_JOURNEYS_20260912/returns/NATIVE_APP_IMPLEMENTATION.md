# Native App implementation return

TASK Type 2, delegated-harness-native child `native_app_author`; no delegation. Model inherited from parent (brief records gpt-6-astra medium). Active checkout: chirality-ui-refinement-packaged-20260912. Source implementation and focused checks complete; independent review and native qualification remain with parent. This is derivative implementation evidence, not accepted product authority or release acceptance.

## Result

- Live assistant items use the same Runtime `deriveTranscriptView` reducer as replay, retaining native item ID and commentary/final/null phase. Completed native item snapshots replace text; legacy aggregate output cannot overwrite native items. Reattachment replaces the active turn's prior replay projection instead of duplicating it. Retained activity uses raw admitted events for the same live/replay projections.
- Compact activity stays at the latest assistant item, shows supplied summaries, tools, native assignments/results and replaceable work checklists. Full summary/child details remain expandable. Removed the verbose composer-running banner; reconnect, waiting and Stop status remain at the assistant. Existing scrolling/reduced-motion behavior remains.
- Native children use raw params identity and actual `agentsStates`/thread/turn status. Collab call completion does not finish an assignment. Explicit `chirality/nativeChildren/observationEnded` displays the capture limit and keeps last-observed status. Agents tab now also shows native work, filtered to the primary session in the shell. Activity→Children uses the same reducer.
- One native request card appears in conversation; Plan references the conversation. Live authorized listings gate actionability and are rechecked before posting. Request identity includes session; historical pending events are never actionable. Resolved questions/approvals stay inspectable. Non-secret drafts have bounded memory-only recovery; secret drafts are never cached or printed in history. Late answer errors cannot leak into another session.
- `useLiveSessionRequests(sessionId, active)` shares one ref-counted polling subscription for badge and inline consumers. The exported `LiveSessionRequests` interface remains stable for the attention author's dialog. Session routing relies on existing ports; the separately discovered cross-folder port ownership repair is not claimed here.
- Steering route/port/client and composer Update action bind to the active Runtime turn and stable operation ID. Acknowledged receipt clears only the matching draft. Rejected/unknown delivery preserves it; unknown same-text resend is disabled, no automatic retry/new turn/Stop. Native evidence reconciles receipt. Reconnect/Stop state blocks steering dispatch, with a synchronous in-flight guard.
- Automatic Plan reads do not toggle manual Refresh busy state. The contained conversation catalog reads depth 4 so `.chirality/workflows/name/WORKFLOW.md` can resolve through existing catalog-membership, containment, symlink and root checks. No localhost URL conversion was introduced.

## Validation

APP-HOLD check executed once with operation `reliance`, entry `APP_V3_USER_JOURNEYS_20260912:NATIVE_APP_IMPLEMENTATION`, targets DEL-02-01, DEL-02-02, DEL-02-04, DEL-03-03: ALLOW, all CLEAR/NOT_HELD. Register SHA-256 d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c; scan fingerprint 350872de553b81ba726bca5d8bcff1e105e8b5bd7407bdec15bb8e9f08cdeffe; preflight HEAD 6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f.

- `./node_modules/.bin/tsc --noEmit --incremental false`: PASS after final edits.
- Focused 13-suite run: 167 tests PASS (native progress, native coordination, live requests, chat attach/steering/quiet Plan refresh, folder binding, request cards, Plan execution controls, turn activity, event views, API proxy steering, Runtime port, transcript replay).
- Final steering guard/reattach-status adjustment: affected chat-panel-turn-attach suite rerun, 33 tests PASS, plus typecheck PASS.
- Broader affected chat checks also covered model selectors, attachments and Runtime reconnect. Existing folder-binding suite emits an `act(async)` warning in its explicit empty-method-selection failure test; no failing assertion. No build, supplier/model execution, account call, live UI operation, Git mutation, or protected-state read was performed.

## Ownership and handoff

Routing chain files were frozen and returned to parent for the newly authorized session-routing author before final UI work. `woven-dialogue-shell.tsx` contains the attention author's changes; this child added only `nativeEvents={events.filter(event => event.sessionId === primarySessionId)}` to CoordinationPanel after parent explicitly transferred the file. The excluded library files were not edited. Parent integrates the routing repair, independently reviews the final combined diff, runs registered checks and native journeys, and owns release decisions.

Capture remains bounded by Runtime's observation lifetime. Known active children at parent termination are explicitly marked observation-ended; this implementation does not claim subsequent child state capture. Cross-folder attention/steering qualification depends on the separate session-routing repair. No acceptance pointer moved. Closure verdict: bounded App implementation complete, integrated qualification pending.

## Changed file manifest

Paths relative to projects/chirality-app-dev/frontend; hashes are the observed handoff bytes, not authority pins. Shared routing/shell files may change under the newly assigned authors/parent.

- `src/app/api/harness/session/[id]/turn/steer/route.ts` — `1f495a339e590e82a75f128126708b095dc2129eb3bb4bc04ae2da0262fe5231`
- `src/app/globals.css` — `55a110adc347a370f2502a378f793784b2924e49aaf032714adb97ead010608e`
- `src/components/shell/chat-panel.tsx` — `3f8c56008b0c798c37f32fd168605e8419f0e9b23d69a3933353c954d244ef75`
- `src/components/shell/conversation-message.tsx` — `393d209c4539a253df9fd150bf5a23ea74d72b8c567353b0ba3e58e0bec4d320`
- `src/components/shell/native-plan-panel.tsx` — `1983f82da6a62c5f835ecc2b6dcc63be4e49bc355252c7d9f9ec2dc0d3181b83`
- `src/components/shell/permission-requests.tsx` — `20495e4d580ab6f67e28e7b1ecd7f7a071a1f69f8d1cf0837ada25fa833a6fab`
- `src/components/shell/request-card.tsx` — `fdb3fccef316626e72d2329e95a1f8c869c8fd1d3f97261b7712922db7c64dc5`
- `src/components/shell/turn-activity.tsx` — `f3cb8210ec5460cf1b1e9b46f78cab57282f26310de30f5ee5de583a6aa1394f`
- `src/components/shell/subagent-stream-view.tsx` — `f6e45216737f317c50e6016074d12ddde7c25b388d1aba6e9b83535c706192fb`
- `src/components/woven-dialogue/coordination-panel.tsx` — `72f033f508b5f597d958bd3d79d11e0ddaf401187a50915349624b7318c4a539`
- `src/components/woven-dialogue/woven-dialogue-shell.tsx` — `79496ee078e8fd1608c459f8c87b3fd35e18f9388cb2519abeb58214df425917`
- `src/lib/harness/client.ts` — `723dc11667ff88cf19390d958ef83fca1a19d904c8e597edf323686e88670c80`
- `src/lib/runtime-client/daemon-harness-port.ts` — `6ebcb46d2efbc68101109da8ccca2a5a6c8906dda6524ba8d6a4a6f9da744e2a`
- `src/lib/runtime-client/runtime-daemon-harness-port.ts` — `f272f56beb67895bf8d344676dcd31495d71702aed5a23917fbbf561a4533ac2`
- `src/lib/shell/harness-event-views.ts` — `0a27ce21b6f892f4a215806393c33df8e3ab5bdc0bdd89d4f946638c4c65bbcd`
- `src/lib/shell/turn-activity.ts` — `7c6f69c226276a631ad3067d865fbd141bd30f84551eea7100ac29a511aefce5`
- `src/lib/shell/native-progress.ts` — `a9477666d4982813c44c33abc0c312d0716801ca3e40387ea0cdb572f3a298a5`
- `src/lib/workspace/use-conversation-file-catalog.ts` — `a04582a5f0a58029b1595a3ec614dd56b230400ed50199ef1cca2c98f71cd17c`
- `src/lib/woven-dialogue/contracts.ts` — `95574d701c6bb1bc3cd7f2077dcf812006edce05cdc45e91fb5dd80de5755371`
- `src/lib/woven-dialogue/selected-session-replay.ts` — `88c3882bfc60a5729d4aa957b830ebc055cce76350e6a002597b77a8b615ba3a`
- `src/__tests__/api/harness/daemon-proxy-boundary.test.ts` — `6a9aaaeeba3164df504e5747e329bd6fffb1e89eb1bed7a6214e29e4d8513467`
- `src/__tests__/api/harness/fake-daemon-harness-port.ts` — `a2652402cb894d63f08649edc39f70873086e3ba84ef69d950bad209d93322ed`
- `src/__tests__/api/harness/turn-route-attachments.test.ts` — `3dfb1ce495fb2a074928c49c5daf5be8bf47cb7b1e65ac801dc410a4383d5f43`
- `src/__tests__/components/chat-panel-folder-binding.test.tsx` — `82caed438b5ae2d8233c4edbff7b643f5caffabcf10462f2130f4d7330f2cf20`
- `src/__tests__/components/chat-panel-turn-attach.test.tsx` — `d1078abdcde3d6d779f781f7d7b5c86c8c187ec473e9be54fa0a729db52ac988`
- `src/__tests__/components/live-session-requests.test.tsx` — `06b693884fb284e017584e98c2514b6a9d2b1fe6962233a5627a32cd46e70baa`
- `src/__tests__/components/native-coordination.test.tsx` — `24aa0e15eead0499f9040b3708512e09a3d3e1cdc2aeb055196bf47156293bd9`
- `src/__tests__/lib/native-progress.test.ts` — `3578e1a75e904d888e3e7ae30ab5face7df86e27c9c9577d764147ce1b197e68`

## Supplied basis

- `AGENTS.md` — `c3fb6dbe394c168f75f12e761fce47b80a81ab9ae1bd41cfb0d28dd1e4003352`
- `projects/chirality-app-dev/AGENTS.md` — `3b1c1ffdc5d99b035bb08164cc3b6e1425e57431c89d22902f6ba88cbb3adb79`
- `agents/AGENT_TASK.md` — `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PLAN.md` — `62bd95560c979477244a5132e37343d2f31718419853aeeb7bce6c61062ac619`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/NATIVE_INTERACTIONS_PROPOSAL.md` — `818b8c380d7c25c706e8e259161e8ef760bf5b4d1965473aa889fd8f31553914`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_APP_IMPLEMENTATION.md` — `d1698974897319c86ec3d1eeb3fbf3b4a84607dd9507683e2664fff9ef1b83da`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_PROTOCOL_MAPPING.md` — `56e906f89359f2508680e5628a011e60efb46122664dc6d45c10aabb02fe7664`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_RUNTIME_IMPLEMENTATION.md` — `93ad4cde5c6a078f30f0ea5846911b4bef20ac096fb36acc971314fe8f52c023`

## Follow-up: definitely rejected bound send

Parent observed baseline J02 losing a second normal message after a cross-folder port replacement. Two new regressions confirm same-chat `Unknown session` rejection already preserves text for manual retry (both selected-context and turn-POST rejection). A concrete adjacent loss condition was reproduced: changing the visible context generation while a bound pre-turn request is outstanding caused catch to skip composer restoration and remove submitted transcript rows. The recovery now restores the original bound session draft key if writable and empty, without overwriting another draft or contaminating the newly selected chat. The error points to reopening the original chat for manual retry. A definitive pre-start rejection flag distinguishes this from a possibly accepted/transport-ambiguous turn; no automatic resend is introduced. This is a verified failure mode, not a claim that the baseline observation's entire causal chain was established.

Only chat-panel.tsx and its folder-binding regression suite changed for this follow-up. Typecheck PASS; folder-binding + turn-attach/steering suites PASS, 86 tests. Evidence: NATIVE_APP_REJECTED_SEND_TESTS.txt. Routing remains separately owned. Updated two file hashes above reflect this final follow-up freeze.
