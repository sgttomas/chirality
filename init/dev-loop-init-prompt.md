# Development-loop session init prompts

This is the root launcher catalog for development work loops. Its entries are
**alternative session-entry text**, not runtime agents, Agent 0 instances,
services, daemons, or simultaneously executed configuration. Choose one
launcher for each session. Task Management sessions use the separate
per-register launchers named `taskmgmt-init-prompt.md` beside this file and in
each project's `init/` folder.
`HELP_HUMAN` is the sole canonical Agent 0 role; it may be instantiated for a
particular session and loop scope without creating another Agent 0 authority.

To start a session, choose one entry below. For an embedded launcher, copy the
text between its `<init-prompt>` tags, substitute any remaining
`<PLACEHOLDER>` tokens, and paste it as the first message. The PEC entry points
to its canonical project-local launcher file instead of duplicating that
block here.

Six alternative launcher entries are cataloged:

1. **Generic project launcher** — a fill-in template for any workspace/persona.
2. **Root-governance work loop launcher** — the standing root control-plane loop.
3. **Bridge work loop launcher** — the app-dev ↔ piping tier-0 bridge loop.
   Its file is `_DomainEngines/bridge/LOOP_INIT.md` (note the order:
   `LOOP_INIT`, not `INIT_LOOP`).
4. **PEC work loop launcher** — enters the standing PEC coordination-plane
   loop. Its canonical paste-ready launcher is
   `projects/pec/init/dev-loop-init-prompt.md` and points to
   `_DomainEngines/pec/LOOP_INIT.md`.
5. **Piping work loop launcher** — the chirality-piping project development
   loop. Its file is `projects/chirality-piping/loop/LOOP_INIT.md`.
6. **App-dev work loop launcher** — the chirality-app-dev project development
   loop. Its file is `projects/chirality-app-dev/loop/LOOP_INIT.md`.

Project-local launcher files may mirror the catalog pattern. PEC deliberately
has one canonical launcher block at `projects/pec/init/dev-loop-init-prompt.md`; this
catalog references it rather than maintaining an interchangeable duplicate.

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

Set `WORKING_ROOT` to `{REPO_ROOT}`.

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.

Act as `HELP_HUMAN` for `{WORKING_ROOT}`.

Read `{REPO_ROOT}/execution/_Coordination/LOOP_INIT.md` and follow it: pursue
the loop's inherent goals — recorded in its newest standing workplan — as far
as live authority permits.

Steer (this run): <none>
</init-prompt>

Entry is typed, consistent with the project work-loop launchers (§§5–6):
the launcher selects `HELP_HUMAN`, the sole canonical Agent 0, instantiated
for the root governance scope. Root `execution/_Coordination/` is a
governance control plane, not a project package or decomposition root.
LOOP_INIT and the newest standing workplan still govern which lanes open;
`HELP_HUMAN` delegates lane work to the named Agent 1 managers or bounded
Agent 2 dispatches rather than becoming them, and root-wide WORKING_ITEMS
entry is not permitted. For a deliberately single-lane session entered
directly as an Agent 1, use the generic launcher (§1) instead.

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

## 4. PEC work loop launcher (standing coordination-plane loop) — ACTIVE

Copy the single paste-ready `<init-prompt>` block from
`projects/pec/init/dev-loop-init-prompt.md`. Replace its `<none>` placeholder with a
per-run steer if desired.

The launcher remains deliberately thin. `_DomainEngines/pec/LOOP_INIT.md`
hands the session to the newest standing `WORKPLAN_*.md` beside it and to the
live receipt/register discovery protocol. Those surfaces carry the current
goal, gates, fences, and state pointers; pasted launcher text does not duplicate
or override them.

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
