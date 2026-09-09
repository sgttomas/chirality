# UI Source Freeze v7

Base commit: `c16812685831a1cae3d44bf478d08b033c605c3a`
Predecessors: UI source freezes v1 through v6 remain unchanged. V6 received
one independent P2 finding and is superseded by this freeze.

This successor retains the reviewed v4 presentation and adds restart-safe v3
conversation continuation. It preserves the Runtime session id, canonical root,
role, modes, active ordered methods, selection revision, instruction basis,
transcript, and recorded native-plan history. TASK and legacy untyped sessions
remain inspectable and read-only. Composer references merge into the active
Runtime selection, turn requests omit method overrides, and empty composers do
not stop active methods.

It closes all independent Astra pre-freeze findings: selections made while a
turn runs survive, including an explicit removal to an empty next-message set;
a rejected first method-bearing turn restores its unchanged retry state;
successful selection changes advance the local CAS state even when the provider
turn later fails; agent-driven selection revisions are adopted from the
authoritative replay session; bound drafts use the canonical session root;
historical assistant roles come only from turn-linked recorded bases (otherwise
rendering neutrally as Assistant); the Methods Refresh control refetches; and a
successful first turn consumes its prior unbound draft key so method references
cannot reappear in a later New chat. Success clearing and failure restoration
both act only when the submitted composer-selection generation is unchanged.

Validation before freeze:

- focused v3 UI/transport regressions: PASS — 9 files / 70 tests
- full frontend Vitest: PASS — 188 files / 1,993 tests; 1 file / 4 registered skips
- frontend and Electron TypeScript typecheck: PASS
- controlled mock-protocol App journey through Unix socket, RuntimeClient, and
  Next proxy: same `sess-controlled-1` reopened and continued with four retained
  transcript items; native Plan Mode remained unavailable; actual Methods
  Refresh produced a second successful catalog request
- authority corpus status/audit: v21, all 12 relevant members MATCH, no drift,
  all deliverable reference rows reconciled

The controlled browser screenshot is behavioral evidence only. Its IAB capture
stacked and clipped the primary panel, so visual acceptance continues to rely on
the earlier settled v4 desktop capture; no layout or styling changed in v7.
The controlled fixture is hand-seeded and does not qualify a native adapter,
supplier, or production Runtime resolver.

The independent reviewer must inspect 100% of each listed postimage and its base
diff, and rerun the preserved Astra counterexamples, including the V6 explicit
empty-selection failure case.

```text
76fe0ec866ee5ac885f9c59a57c0002a02ac36ac5d67b7d72e951836e0b8c0b2  frontend/src/__tests__/components/agent-matrix-panel.test.ts
efbd353ef77a73a32a00149a8452567f894f8d13998c58304994ac07e88acda1  frontend/src/__tests__/components/agents-projection.test.tsx
5dfd9e4aee4840b66b4c37646b9b38952b424c80e66f868b2cdd392c140b9040  frontend/src/__tests__/components/chat-panel-failed-send.test.ts
fd645ff910484e10318321e759908639a6b65e52407403c96f75ffdb47490e54  frontend/src/__tests__/components/chat-panel-folder-binding.test.tsx
a3c248a8c0bd785f73cfd756aa83c2512733828cb6fe6d27d8ea020d7e79463e  frontend/src/__tests__/components/historical-chat-reveal.test.tsx
e6b9ceb5a7f49124ff84a1020ae33839e8548eb7acd7c546ec1b33aa4ea9a52e  frontend/src/__tests__/components/loop-tertiary-routes.test.ts
edb7024edf0944917c3d9d3e3a99553cc06425c5fa5b25381a8805422b38b56b  frontend/src/__tests__/components/method-library-view.test.tsx
aad4bbde67085c185a586734f5805ac12707e5d68211453947f6052fa34ab96b  frontend/src/__tests__/components/right-panel-method-refresh.test.tsx
a9e3e41c531acadd9ff8175d23e2f381ccde46c0c003c9b4da316d95379a629f  frontend/src/__tests__/components/runtime-reconnect-refresh.test.tsx
02ea12536311b9dc8b779a98ea43317d18707af9774f2e0fcd3036a4ceb2c837  frontend/src/__tests__/components/selected-session-replay-lens.test.tsx
7ac9a9b8d0e0405ebb83e3037cbeab61add75bd1ac5af025ac47322b11b7544c  frontend/src/__tests__/components/woven-dialogue-route.test.tsx
7e8e1034d8b84a40c3f5f2b18ca199f96e1678dbd87d149656203d368e8067a7  frontend/src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx
a0cd828761a13371ab4e9961da32daa20a7b02f3acdc265175e9956a6a0edb56  frontend/src/__tests__/components/woven-right-panel.test.tsx
255e47a2a84b21db6bb9df3e41abfe7996207c5247eff3ba0e47aecf2995e747  frontend/src/__tests__/fixtures/controlled-v3-runtime.mjs
17111c3de7f1ffb0b38f6a1ab508fcb7bac39f8fb0e2d6b9a96e07a3648c2b30  frontend/src/__tests__/integration/v3-runtime-proxy.integration.test.ts
0494a69a0e41445c198f427f65abe1944d0b2fcff19b359690d9d5037ffb316c  frontend/src/__tests__/lib/agent-matrix-cells.test.ts
7260e158c18955b314eb14163771c8239ac34781fe8bcf53d5750c9fc43c581a  frontend/src/__tests__/lib/chat-organization.test.ts
4129f282ea06acd769eb616892885feb7bd3344fa0d8e82fb0cb26c9f29ed8a7  frontend/src/__tests__/lib/guarded-session-selection.test.ts
3040247da9cde2c6e1052e73b8f3765e826744807bf089831bba9ef68edd9ef6  frontend/src/__tests__/lib/harness-chat-draft.test.ts
2cf9e1564bda4bf893430b82316bd97825aba8c5d374ede5f04ff65bbb1fbb3a  frontend/src/__tests__/lib/method-selection-client.test.ts
2d135bf51d25ad910aa8286f74d935d76579b8a5ae2599803ed2151f41f44dc0  frontend/src/__tests__/lib/operator-projection.test.ts
6c475dbaefc8348b48c36092276548af8cbd598e6da12ce7575b6cdd4b609387  frontend/src/__tests__/lib/persona-resolution.test.ts
3d5f6478492b4603372fd5f32e176942275841daab1380ed61d3e0c6899350b8  frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts
9411e8ff6a106f15ba1b7f87882cd0d2929b3ea8478808c8ef3f0f4f3ca1cc61  frontend/src/__tests__/lib/selected-session-replay.test.ts
0d4377a1e56953535b78bb7154f6cce28155768e76e38a031b87ae6281325af6  frontend/src/app/globals.css
06294bda98ae9691e73353f26e57f94f517cd9c9e0e63051e1ecabb0f0218b5e  frontend/src/components/portal/agent-matrix.tsx
ad8aa9ab600ba6bbc4f965df6291bf8db1ce8a74b55921105a8e15129543c9a1  frontend/src/components/shell/account-popover.tsx
29938aa3cd877567d9620d8c2d56095f8dcf19c5851081243fce8dfddc6fce41  frontend/src/components/shell/chat-panel.tsx
93610e2681e3bb6b631efa143a52b3a37461a91a473d17255ce7fa7643c2cbe2  frontend/src/components/shell/loop-shell.tsx
b3223a4c3f2cc1171d950f3e150615784e68b6633741353273b1ec9100eca7d8  frontend/src/components/shell/persona-picker.tsx
a9be515bfe029bce30a5a81b44d7277acc23f9a38ba0b1b56cb1063c24e7fee2  frontend/src/components/shell/portal-loop-shell.tsx
83cd2fa9b1dade4ce2f250cda69902ea205928733b7dfe992e63b9337a9f0634  frontend/src/components/woven-dialogue/agents-projection.tsx
e1d4ec4b5f910c2d5613570b440d44976bf2eec88af1878bf269551707fdbc31  frontend/src/components/woven-dialogue/method-library-view.tsx
e9cec68b067d7574ffcf06f7dbe3ec86a85f5f7efde5c8be52b3ba770b306017  frontend/src/components/woven-dialogue/navigator.tsx
1f7ac32ac176c5ff78f00d4fb365294a3852789f3c8ac4987c878bbf78e55e1d  frontend/src/components/woven-dialogue/right-panel.tsx
1cac29ce24865b3380d4c01b1f686948d9f5f30638ab71c710582c1569e15833  frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx
7a8ec779dfb043c3e8bacf6369f1fbe1362f5b078a78dddff3750438727dd57e  frontend/src/components/woven-dialogue/woven-dialogue-route.tsx
fab483ab1266ff5533311cd5fd3dfe4c9eea631565a7332b0412a9674db28033  frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx
f8ec5e7d44e93223c2ec4e3be21d5e4d79fb802ac49a15ec415bc7d2dbcc963c  frontend/src/lib/harness/chat-draft.ts
b4f5d5f88e1c3771920c20e90f95dde47af12b1ec3376b1c953a8e4838504344  frontend/src/lib/harness/client.ts
3a3e4e34a60171f7261d26384aff4530df3c42550c1c288fd01895146b4f1db1  frontend/src/lib/harness/method-selection-client.ts
30a796dca3bdd721744b74fa192f8fa8b6036a50ac7bbc839b1232601141a638  frontend/src/lib/portal/agent-matrix-cells.ts
ef9611819801c240a37c13d8878a119ee36fa7a90081ed33ce3070924da8af62  frontend/src/lib/runtime-client/daemon-harness-port.ts
317f19e0d82b9daa0af98933ad2167ebf60d5ce33ef2742f54442938755b51e4  frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts
48eae60bc10e13133a19c7107ef083d32f5dd5ae4d1e79773700b3c796bcdad7  frontend/src/lib/shell/persona-resolution.ts
fd9143541893817eff7c876a58ed825ef7848234801dc2be7d49a9edb14e247f  frontend/src/lib/woven-dialogue/contracts.ts
4cd9c4fa46e88d90fa3ae8f2467262846bbb68fd2a2555ba2d8d929897b6c2e8  frontend/src/lib/woven-dialogue/operator-projection.ts
23c73b6c9d3d8f972f835fb88f15d579b96400a8c475d74ce6322149cde5f697  frontend/src/lib/woven-dialogue/selected-session-replay.ts
```
