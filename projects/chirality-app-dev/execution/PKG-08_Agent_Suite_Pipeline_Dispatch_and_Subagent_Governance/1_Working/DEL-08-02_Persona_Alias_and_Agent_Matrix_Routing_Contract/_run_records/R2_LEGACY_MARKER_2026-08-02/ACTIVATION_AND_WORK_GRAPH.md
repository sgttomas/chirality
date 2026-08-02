# DEL-08-02 Legacy Route Marker — Activation and Work Graph

- RunID: `APPDEV-PKG08-DEL0802-LEGACY-MARKER-2026-08-02`
- InstanceID: `WORKING_ITEMS-PKG08-DEL0802-R2`
- Manager: `WORKING_ITEMS` (Agent 1)
- Package: `PKG-08`
- Selected deliverable: `DEL-08-02` only
- Accepted Git basis: `1d4abf1cf1a23a33bd7fec59971251f86c010210`
- Authority basis: D-APP-74; SCA-APP-004; live DEL-08-02 ScopeOfWork and
  `_STATUS.md`; HELP_HUMAN activation brief dated 2026-08-02
- Method profile: `projects/chirality-app-dev/software-workflow.json`
- Posture: `TERMINAL_FAN_OUT_IN`
- Selection authority: HELP_HUMAN activation under the live ungated
  DEL-08-02 `[data-legacy]` Remaining item

## Frozen objective and boundary

Repair only the real `[data-legacy]` route marker mismatch. The Woven route
must emit `data-legacy="true"` at `?legacy=1` even when the injected legacy
content is unmarked. Preserve default Woven behavior, `legacy=1` query
semantics, unknown parameters, all four routes, legacy shell behavior/layout,
and persona/alias/guard/replay semantics.

The only source/test write targets are:

- `frontend/src/components/woven-dialogue/woven-dialogue-route.tsx`
- `frontend/src/__tests__/components/woven-dialogue-route.test.tsx`

Package-local evidence and deliverable state may be written only beneath the
selected DEL-08-02 folder. Packaged Desktop smoke remains residual. The run
does not write shared loop/plan/AgentRuns surfaces, PKG-02, dependencies,
decomposition, lifecycle/Checking Approval, decisions, Task Management,
parity, D-APP-84, the six UNKNOWN relations, or `runtime/**`.

## Work graph v1

| Node | Agent | Depends on | Writes | Return | Fan-in gate |
|---|---|---|---|---|---|
| N1 | one ephemeral generalist Agent 2 | frozen basis | exact source/test files plus `AGENT2_RETURN.md` | implementation, checks, diff, residuals | exact containment; focused tests; no contract weakening; evidence complete |
| N2 | WORKING_ITEMS | accepted N1 | DEL-08-02 `_STATUS.md`, `MEMORY.md`, package-local manager return | validated package handoff | browser/render and full registered checks; state/history preservation |

N1 is serialized as the Bash-bearing integration owner. There are no sibling
nodes and no concurrent writes.

## Escalation conditions

Escalate rather than proceed if the repair requires a public route/query
change, layout redesign, contract deletion/weakening, another package, a
runtime/dispatch/persona/guard/replay semantic change, lifecycle transition,
or any write beyond the frozen targets.
