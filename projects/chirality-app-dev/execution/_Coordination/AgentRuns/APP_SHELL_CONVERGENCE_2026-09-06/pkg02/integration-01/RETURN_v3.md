# Bounded remediation return

Status: source frozen for fresh full-diff independent review; acceptance held.

Accepted base is e00238621db7a00b036245962c21e3fc6ed75452. This is a derivative implementation/evidence candidate, not accepted deliverable truth. Existing v2 remains historical, with source-review-03 BLOCK R1 and browser Settings obstruction finding retained.

## Repairs

Conversation binding is separate local state from the persona-specific runtime session cache. It retains actual recorded root and original selected-root draft identity across Agent changes, including refused provider synchronization. New persona sessions request the bound root; a different boot-returned root is rejected before changing binding or streaming. Explicit New chat alone releases the binding. The binding callback continues to drive Files and ShellFrame guards; composer folder and native/drop guards directly consume the enduring binding.

Settings positions its fixed popup from the actual trigger rectangle, using available space above or below, with a gap that leaves the trigger reachable. Resize/scroll reposition it. Escape closes and restores trigger focus; outside pointer closes it. Native details/summary pointer toggling remains intact. Actual pointer and responsive browser proof is still required; unit tests do not substitute for it.

## Feedback checks

Focused command from frontend: `npm test -- --run src/__tests__/components/chat-panel-folder-binding.test.tsx src/__tests__/components/shell-frame.test.tsx`. Final outcome PASS, 2 files / 17 tests, captured in focused-remediation-v3.log. Earlier focused run before Settings test addition passed 16 tests. The first new Settings fixture run failed 1/17 because its fake document lacked documentElement.setAttribute required by ThemeControl; the fixture was repaired and the final run passed. An initial root-relative edit command invoked from frontend failed FileNotFoundError and made no edit; its following focused test command passed. These failures are historical feedback, not final proof.

Registered frontend-typecheck PASS in typecheck-remediation-v3.json after final source/test edits. Git diff whitespace check PASS. Scope check PASS in scope-v3.json. No full suite or build was run for this remediation.

## Frozen handoff

SOURCE_MANIFEST_v3.json SHA256: 9241484bdda05836a5e8163d42fe84b62ff620520cdeeb23b250e64ccb782824. It contains all 25 source/test members, including the newly changed existing shell-frame.test.tsx. SOURCE_DIFF_v3.patch is the complete candidate diff against the accepted base, including new files. Only four members differ from the v2 source candidate: chat-panel.tsx, shell-frame.tsx, chat-panel-folder-binding.test.tsx, shell-frame.test.tsx. No source writes after this freeze.

Fresh full-diff independent review, actual browser normal-pointer toggle/dismissal proof, and final registered suite/native proof remain with the manager. No lifecycle transition, publication, no-folder capability or historical per-chat Reveal claim is made. Runtime identity: Codex native descendant, Agent2 TASK instruction-asserted; exact model identifier unavailable and not inferred. No delegation.
