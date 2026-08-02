# Agent 2 Brief — DEL-08-02 Real Legacy Route Marker

- RequestedBy: `WORKING_ITEMS-PKG08-DEL0802-R2`
- RunID: `APPDEV-PKG08-DEL0802-LEGACY-MARKER-2026-08-02`
- ParentInstanceID: `WORKING_ITEMS-PKG08-DEL0802-R2`
- ChildInstanceID: `A2-DEL0802-LEGACY-MARKER`
- Agent form: ephemeral bounded generalist Agent 2; delegation prohibited
- PackageID: `PKG-08`
- DeliverableID: `DEL-08-02`
- AcceptedBasis: Git `1d4abf1cf1a23a33bd7fec59971251f86c010210`;
  D-APP-74; SCA-APP-004; live DEL-08-02 ScopeOfWork, `_STATUS.md`, MEMORY, and
  prior Woven run record
- Dependencies: none beyond the accepted basis

## Objective

Implement only the real `[data-legacy]` route marker repair. Make
`WovenDialogueRoute` emit `data-legacy="true"` for the `legacy=1` branch even
when its injected `legacy` ReactNode is unmarked, and update its focused test
to prove the real component owns that marker contract.

## Declared reads and tools

Read scope is the project root plus root agent/runtime doctrine needed to
understand this sealed brief. Tools: bounded file reads/edits, Git read-only
inspection, and Bash only for the named test/typecheck/build checks. Because
the child bears Bash, the managed scope is the whole project root and this
child is the serialized integration owner; semantic writes remain limited to
the exact targets below.

## Allowed write targets

- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-route.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-route.test.tsx`
- `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract/_run_records/R2_LEGACY_MARKER_2026-08-02/AGENT2_RETURN.md`

## Exclusions

Do not edit status/memory; any shared loop, plan, or AgentRuns surface; PKG-02;
dependency/decomposition/lifecycle/decision/TM/parity/D-APP-84/UNKNOWN state;
or `runtime/**`. Do not commit, push, merge, install dependencies, change
package manifests, or launch another agent.

## Acceptance checks and expected return

Run the focused route test and relevant registered frontend checks feasible in
the environment. The test must inject legacy content without `data-legacy`
and still observe exactly the component-owned marker. Preserve default Woven
absence of the marker and `legacy=1` behavior. Avoid a layout-affecting wrapper;
if a marker boundary is needed, demonstrate why its rendering semantics are
layout-neutral. Return exact changed files, implementation rationale, command
results, diff/whitespace/containment result, limitations, and any escalation.

Stop and return a blocker if meeting the objective requires any excluded
semantic or write-scope change.
