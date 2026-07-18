# Session init prompts

Each section below is a **standalone launcher**. To start a session, copy the
text **between the `<init-prompt>` tags** for the launch you want, substitute any
remaining `<PLACEHOLDER>` tokens, and paste it as the first message.

Six launchers live here:

1. **Generic project launcher** — a fill-in template for any workspace/persona.
2. **Root-governance work loop launcher** — the standing root control-plane loop.
3. **Bridge work loop launcher** — the app-dev ↔ piping tier-0 bridge loop.
   Its file is `_DomainEngines/bridge/LOOP_INIT.md` (note the order:
   `LOOP_INIT`, not `INIT_LOOP`).
4. **PEC work loop launcher** — implements
   `plans/pec_bridge_integration_plan_2026-07-04.md` (pec tier-0 registration),
   then continues as the standing pec loop. Its file is
   `_DomainEngines/pec/LOOP_INIT.md`.
5. **Piping work loop launcher** — the chirality-piping project development
   loop. Its file is `projects/chirality-piping/loop/LOOP_INIT.md`.
6. **App-dev work loop launcher** — the chirality-app-dev project development
   loop. Its file is `projects/chirality-app-dev/loop/LOOP_INIT.md`.

Every project also carries the same launcher in its own `init/init-prompt.md`
(pec's points at the pec loop above), so the per-project copy and the section
here are interchangeable.

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

## 2. Root-governance work loop launcher — ACTIVE

Paste-ready as written; replace `<none>` with a per-run steer if you want one.

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Read `{REPO_ROOT}/execution/_Coordination/LOOP_INIT.md` and follow it: pursue
the loop's inherent goals — recorded in its newest standing workplan — as far
as live authority permits.

Steer (this run): <none>
</init-prompt>

The launcher is deliberately thin. Root `execution/_Coordination/` is a
governance control plane, not a project package or decomposition root. Its
LOOP_INIT and newest standing workplan select the appropriate Agent 0/1 role
for each lane; root-wide WORKING_ITEMS entry is not permitted.

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

---

## 5. Piping work loop launcher (chirality-piping development) — ACTIVE

Paste-ready as written; replace `<none>` with a per-run steer if you want one.

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to
`{REPO_ROOT}/projects/chirality-piping`.

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.

Act as `HELP_HUMAN` for `{WORKING_ROOT}`.

Read `{WORKING_ROOT}/loop/LOOP_INIT.md` and follow it: pursue the loop's
inherent goals as far as live authority permits.

Steer (this run): <none>
</init-prompt>

Entry is typed: the launcher selects `HELP_HUMAN` under the owner's
instruction-separation direction (recorded verbatim in
`projects/chirality-piping/execution/_Coordination/AgentRuns/INSTRUCTION-SEPARATION-20260717/RUN_RECORD.md`).
The goal, protocol, fences, and pointer index live in
`projects/chirality-piping/loop/LOOP_INIT.md` → the newest standing
`WORKPLAN_*.md` beside it → its receipts. This supersedes the older
status-laden entry (`execution/_Coordination/NEXT_INSTANCE_PROMPT.md`), which
remains as a historical map.

---

## 6. App-dev work loop launcher (chirality-app-dev development) — ACTIVE

Paste-ready as written; replace `<none>` with a per-run steer if you want one.

<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.

Act as `HELP_HUMAN` for `{WORKING_ROOT}`.

Read `{WORKING_ROOT}/loop/LOOP_INIT.md` and follow it: pursue the loop's
inherent goals as far as live authority permits.

Steer (this run): <none>
</init-prompt>

Same thin-launcher rationale as §3: the goal, protocol, fences, and pointer
index live in `projects/chirality-app-dev/loop/LOOP_INIT.md` → the newest
standing `WORKPLAN_*.md` beside it → its receipts. This supersedes the older
status-laden entry (`execution/_Coordination/NEXT_INSTANCE_PROMPT.md`), which
remains as a historical map.
