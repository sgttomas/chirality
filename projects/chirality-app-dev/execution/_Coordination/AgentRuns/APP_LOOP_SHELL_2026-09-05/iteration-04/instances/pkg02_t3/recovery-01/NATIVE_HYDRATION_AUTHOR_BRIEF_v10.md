# Sealed TASK repair brief
RequestedBy: WORKING_ITEMS /root/pkg02_finish
RunID: APP_LOOP_SHELL_2026-09-05 iteration04
ParentInstanceID: /root/pkg02_finish
ChildInstanceID: native_hydration_author
PackageID: PKG-02
DeliverableID: DEL-02-03
TaskSkill: software-bounded-implementation
ApplyEdits: true
Objective: implement only the locally hydration-stable FileTreePanel capability fix sealed in recovery-01/NATIVE_HYDRATION_AMENDMENT_v10.json. Read this amendment and the prior brief for context; this brief supersedes its two-path objective.
AcceptedBasis: recovery-author-v9/SOURCE_MANIFEST_v9.json and SOURCE_DIFF_v9.json, actual native-v9-host failure and browser/hydration-capability-v9 diagnostic. Read root/App AGENTS, agents/AGENT_TASK.md, skills/software-bounded-implementation/SKILL.md, software-workflow.json and current DEL02-03 contract.
AllowedTools: read, write, bash. No delegation, browser/native/build/global processes, Git, shared state, network/provider/runtime/account actions.
AllowedWriteTargets: frontend/src/components/shell/file-tree-panel.tsx and frontend/src/__tests__/components/file-tree-panel.test.tsx within App; new immutable evidence only under this T3/recovery-author-v10/**. All other16 source identities, especially WorkspaceProvider and globalCSS, read-only.
Acceptance: prove matching SSR and first client output when provider capability changes false(server) to true(client), postmount native Choose folder enabled and callable, browser fallback retained, legacy callers preserved. No suppressHydrationWarning or error filtering. Focused existing file-tree tests plus meaningful hydration regression.
Outputs: SOURCE_MANIFEST_v10.json and SOURCE_DIFF_v10.json over entire18 original-baseline scope using prior schema, exact bytes and hashes; allother16 unchanged; focused command/env/version/exits/logs; D64 tenfields/fourlenses with EffectStatus HELD and separate truthful draft effects; author return. Fresh APP-HOLD dispatch/reliance required. Parent handles global gates and new actual browser/native.
Provenance: delegated-harness-native TASK Agent2, instruction-asserted, model/engine actual known only; exact serving ID unavailable. No siblings/children.
Escalate any new finding or need beyond2paths; do not widen scope.
