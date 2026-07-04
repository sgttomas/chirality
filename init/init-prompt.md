# Session init prompts

Each section below is a **standalone launcher**. To start a session, copy the
text **between the `<init-prompt>` tags** for the launch you want, substitute any
remaining `<PLACEHOLDER>` tokens, and paste it as the first message.

Four launchers live here:

1. **Generic project launcher** — a fill-in template for any workspace/persona.
2. **Root-governance WORKING_ITEMS launcher** — the standing WORKING_ITEMS entry.
3. **Bridge work loop launcher** — the app-dev ↔ piping tier-0 bridge loop.
   Its file is `_DomainEngines/bridge/LOOP_INIT.md` (note the order:
   `LOOP_INIT`, not `INIT_LOOP`).
4. **PEC work loop launcher** — implements
   `plans/pec_bridge_integration_plan_2026-07-04.md` (pec tier-0 registration),
   then continues as the standing pec loop. Its file is
   `_DomainEngines/pec/LOOP_INIT.md`.

---

## 1. Generic project launcher (fill the placeholders)

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to `{REPO_ROOT}/<TARGET_WORKSPACE_REPO_SUBPATH>`; for root-governance work, set `WORKING_ROOT` to `{REPO_ROOT}`.

Read `{REPO_ROOT}/agents/<AGENT_INSTRUCTION_FILE>`.

Act in the `<AGENT_NAME>` persona for `{WORKING_ROOT}`.

Then read `{WORKING_ROOT}/<COORDINATION_PROMPT_SUBPATH>` and follow the instructions.
</init-prompt>

---

## 2. Root-governance WORKING_ITEMS launcher

<init-prompt>
Your goal is to complete the inherent goals of this project that you will discover as you follow those instructions.

Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to `{REPO_ROOT}`.

Read `{REPO_ROOT}/agents/AGENT_WORKING_ITEMS.md`.

Read `{WORKING_ROOT}/AGENTS.md`.

Act in the `WORKING_ITEMS` persona for `{WORKING_ROOT}`.

Then read `{WORKING_ROOT}/execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and follow the instructions.
</init-prompt>

---

## 3. Bridge work loop launcher (app-dev ↔ piping tier-0 bridge) — ACTIVE

Paste-ready as written; replace `<none>` with a per-run steer if you want one
(e.g. `prepare only — do not execute adopted briefs`).

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Read `{REPO_ROOT}/_DomainEngines/bridge/LOOP_INIT.md` and follow it: pursue the loop's
inherent goals — recorded in its standing plan — as far as live authority permits.

Steer (this run): <none>
</init-prompt>

The launcher is deliberately thin: the loop's goal, protocol, and specifics live
in `_DomainEngines/bridge/LOOP_INIT.md` → its standing plan → its receipts, which
change at their own pace. A stale pasted copy of this launcher can only mispoint,
never override protocol; the steer overrides the loop's default posture but never
the owner gate (K-AUTH-1). To launch a different loop later, point the same
pattern at that loop's own `<LOOP_DIR>/LOOP_INIT.md`.

---

## 4. PEC work loop launcher (pec tier-0 registration → standing pec loop) — ACTIVE

Paste-ready as written; replace `<none>` with a per-run steer if you want one
(e.g. `author the tier-0 package only — do not open PRs yet`).

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Read `{REPO_ROOT}/_DomainEngines/pec/LOOP_INIT.md` and follow it: pursue the loop's
inherent goals — recorded in its standing plan — as far as live authority permits.

Steer (this run): <none>
</init-prompt>

Same thin-launcher rationale as §3: the goal (implement
`plans/pec_bridge_integration_plan_2026-07-04.md`, stop at the owner gates, then
the standing pec goal once ruled), the protocol, and the fences live in
`_DomainEngines/pec/LOOP_INIT.md` → `WORKPLAN_2026-07-04_pec_loop.md` → its
receipts.
