# Orchestration Plan — APPDEV_WOVEN_REDESIGN_2026-07-24 (v1)

**Adopted authority:** owner adoption in-session 2026-07-24 ("Adop the brief as-is. Proceed accordingly.") of `ADOPTED_BRIEF.md` (TRB-APPDEV-WOVEN-REDESIGN-2026-07-24) with defaults D1–D4. Owner execution direction: Agent 0 = HELP_HUMAN loop operator; Agent 1 and Agent 2 seats on `opus-5` subagents.
**Posture:** MIXED (selection authority: HUMAN for scope/models; AGENT_0 for stage graph). Plan v1 frozen before dispatch.
**Branch:** `feat/woven-redesign` off `main@403f228f4`. Baseline green: typecheck pass; vitest 127 files passed / 1 skipped, 944 tests passed / 4 skipped (after worktree-local rebuild of untracked `runtime/packages/*/dist` — no tracked change).

## Role mapping (platform-native subagent facility per AGENTS.md)

- **Agent 0:** HELP_HUMAN loop operator (this session) — supervision, dispatch, integration commits, gates, records. No design/content authoring beyond record-keeping.
- **Agent 1 (opus-5):** WORKING_ITEMS-posture validator/integration-owner instance — pre-dispatch brief review; per-stage return validation against sealed briefs (diff audit, trap checklist, invariant sweep); integration rulings inside accepted scope. Persistent across stages via continued messaging.
- **Agent 2 (opus-5):** one executor per stage instance, sealed brief in `instances/<ID>/LAUNCH_BRIEF.md`, write scope limited to the brief's file list.

## Stage graph (from ADOPTED_BRIEF §5, with one packaging amendment)

- 0 Setup — DONE (Agent 0): branch, fonts under `frontend/src/fonts/` (IBM Plex latin woff2 ×10 + OFL license, from `@fontsource/*` 5.3.0 npm tarballs), baseline.
- A Tokens & chrome (Agent 2 `A-TOKENS-CHROME`) — sole `globals.css`/`layout.tsx`/`shell-frame.tsx` owner this stage.
- B1 IA fold **+ B3 logo assets** (Agent 2 `B1-IA-FOLD-LOGO`) — amendment v1: B3 folded into the B1 instance as a disjoint second task (asset files only; consumers stay A-owned; favicon via `src/app/icon.svg` auto-route avoids the `layout.tsx` conflict). Non-consequential packaging change inside accepted scope (D-APP-64 latitude; rationale: fewer instances, zero shared writes).
- B2 Navigator session history (Agent 2, after A+B1 fan-in).
- C Defect & polish (Agent 2, after A/B1/B2).
- V Verification (Agent 2 ×2: invariant sweep; D-APP-36 browser evidence).
- Close (Agent 1 validation + Agent 0): gates, DEL records + D4 reconciliation, PLAN_COMPLETION_LOG, receipt, PR. Owner merges.

Concurrency: A ∥ B1 (write scopes disjoint — verified in ADOPTED_BRIEF §4/§5). B2 serialized after B1 (same file `navigator.tsx`) and after A (workspace-state schema). Failure isolation per brief §5.

## Returns

Each instance writes nothing outside its brief's file list; its terminal message is the return, persisted to `instances/<ID>/RETURN.md` by Agent 0 at fan-in with the Agent 1 validation verdict.
