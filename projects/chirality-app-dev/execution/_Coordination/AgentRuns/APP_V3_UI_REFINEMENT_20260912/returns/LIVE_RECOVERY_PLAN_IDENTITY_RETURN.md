# Plan-attempt identity author return

Author: `/root/live_reconnect_diagnosis`, gpt-6-astra/medium, Type 2.
Verbatim return follows.

Plan-attempt repair is complete and frozen. No commit or Runtime changes.

Changed four files:

- `src/components/shell/chat-panel.tsx`
- `src/lib/harness/plan-executions.ts`
- `src/__tests__/components/chat-panel-turn-attach.test.tsx`
- `src/__tests__/lib/plan-executions.test.ts`

The initial attempt contains the preallocated UUID. ChatPanel explicitly writes that record synchronously before POST; it does not rely on the later React persistence effect. Recovered settlement requires exact identity equality. Idless or mismatched attempts become Unknown without adopting another turn’s identity.

Tests verify storage at dispatch, ambiguous response followed by unmount/reload, matching completion, mismatched/legacy Unknown, and no second POST.

**Validation:** 82/82 focused tests passed; frontend and Electron typecheck passed; `git diff --check` passed. No outstanding failure in this continuation.
