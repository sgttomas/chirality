# Agent roles and workflow instructions — revised proposal

Prepared by HELPS_HUMANS. The human accepted the original audit proposal, confirmed retention of Packages and Deliverables in PROJECT_DECOMP, and then accepted the workflow concept developed in the conversation. This revision incorporates that direction. The detailed loading and migration design below is proposed implementation detail; live instructions and runtime contracts have not yet changed.

This document is the current proposal entrypoint. It supersedes the original proposal's skill-conversion framing and general-discovery recommendation. The original audit packet remains the source evidence for passage-level deletions, compression, contradictions, tool repairs, and behavioral probes. [Per-agent revision](AGENT_DISPOSITIONS.md) applies this change to all 34 roles and links directly to their original cards. [Package migration map](WORKFLOW_MIGRATION.md) covers all 45 current packages under `skills/`.

## The distinction to express

**Agent instructions establish a role:** a characteristic way of attending, judging, acting, and taking responsibility across assignments. Retained roles use PROTOCOL, SPEC, STRUCTURE, and RATIONALE to express that orientation concisely.

**Workflow instructions organize an undertaking:** the purpose, relevant knowledge, judgments, relationships, evidence, operations, and conditions by which work develops toward its result. A workflow may branch, iterate, revise its approach, involve human decisions, and distribute work. The instruction should specify where judgment is needed and what makes progress meaningful. Its sequence is as fixed or open as that undertaking requires.

**A brief instantiates the undertaking:** the current scope, inputs, output targets, permissions, and requested result. **Tools execute defined operations.** An agent enacts the workflow with the tools and authority available to its session. Agent 0/1/2 continue to describe role positions in delegation.

This replaces the assumption that the present repo-native collection should become generally discoverable skills. Standards and architecture documents must adopt the new distinction alongside the concrete loader changes. Existing uses of “workflow package” should be reconciled with workflow definitions and run artifacts, eliminating redundant terminology where the same thing is meant.

## Revised agent dispositions

The original audit's 12 `CONVERT_TO_SKILL` recommendations become **EXTRACT_WORKFLOW_AND_REVIEW_ROLE**. Extract the undertaking into a workflow definition; then determine whether a lasting named role adds useful orientation across assignments. Retirement is an outcome to establish through that review and a working replacement route.

The other 20 smaller-instruction proposals and two tool-conversion proposals continue. Workflow extraction also applies to the detailed methods identified inside retained roles. AUDIT_EPISTEMIC and RESEARCHER keep their explicitly open lasting-role questions. PDF2MD and DRAWING_EXTRACT still require an orchestration owner; assigning that work to PROJECT_SETUP would amend its present charter. This revision does not choose that owner.

**PROJECT_DECOMP retains Packages, Deliverables, their relationships to objectives, and judgment about their boundaries in its role instructions.** Detailed identifiers, columns, and output templates belong in its workflow/profile resources. The same principle applies to other role-defining conceptual relationships identified by the audit.

## Proposed packaging

Use `workflows/<name>/WORKFLOW.md` as the authoritative entrypoint. Keep existing package names initially so the migration isolates the conceptual and loading change. A short name and description may support filesystem lookup and validation. Description text serves the selected undertaking; it does not need to compete for general skill discovery.

Supporting files exist where the workflow benefits from them:

- `references/` for substantial schemas, stage-specific guidance, and detailed review criteria;
- `assets/` for templates and material used in outputs;
- `scripts/` for helpers specific to that workflow.

Shared tools remain under `tools/`. Existing useful companion content can be retained or reorganized during the rewrite; every package need not acquire the same companion files. Simple input requirements and essential result checks belong directly in WORKFLOW.md. A larger undertaking can link a dedicated input schema, review reference, or output template at its point of use. Body organization follows the undertaking; this revision adds no universal four-section requirement for workflows.

## Explicit loading and context

The proposed runtime behavior is:

1. Ordinary sessions receive their role and task context. Workflow packages and the collection-wide description catalog stay outside the model prompt.
2. A human invocation or an explicit binding in the selected undertaking names the workflow. A manager reads the orchestration definition relevant to its assignment. A bounded worker receives its selected workflow definition with its brief.
3. The executing agent loads resources needed by the selected mode or stage. Essential instructions for that mode are available before it acts; conditional resources are read when their branch becomes relevant.
4. Selecting a child workflow delivers that workflow's context to the assigned child. The manager receives the information needed to select, brief, and assess that work. The whole descendant collection is not hydrated into either context.
5. The runtime records the definition revision and resources actually supplied/read in the execution evidence where supported. Resuming checks their compatibility with the run's input basis before reusing results.

This is workflow selection from the current undertaking, not automatic description matching against every package. A shared resolver can look up names deterministically without placing its inventory in the prompt. The resolver must report missing or conflicting bindings explicitly.

Propose **`Workflow: <name>`** as the new selection field, usable for manager and worker assignments. During migration, an adapter maps existing `TaskSkill` values to the corresponding workflow and records the resolution. If both fields appear, equal resolved targets are accepted and differing targets are an input conflict. Existing historical briefs remain readable through the adapter. Newly rendered briefs use the new field after their consumers have migrated.

TASK remains the bounded execution role. Managers can enact their own orchestration workflows and dispatch workers for constituent undertakings. Loading a workflow supplies instructions; actual delegation, tool access, and write authority come from the executing session and its brief.

## Tool invocation

WORKFLOW.md identifies the operation, its applicable inputs, and how to interpret its result. The executing agent calls a repository command through the shell, a package helper from `scripts/`, or an available structured/MCP tool. Concrete paths and dependencies resolve against the declared instruction/tool root; invocation can then work from a project execution directory.

For example, dependency extraction still reasons over source documents and invokes the shared dependency validator for mechanical checks. Moving the workflow definition does not require copying that validator or turning semantic extraction into code.

Separate tool-use guidance from mechanically enforced permissions. Replace the current custom `allowed-tools` syntax only with an adopted runtime policy representation and a tested transition for each supported invocation class. Record the effective tool policy and distinguish what the harness enforces from what instructions assert. Preserve the actual command/input/output contracts unless their existing defects require the repairs named in the audit.

A standard skill package is an optional adapter for a specific host or distribution need. It would be generated or explicitly maintained from the workflow source, with appropriate dependencies. General skill installation and automatic catalog exposure are outside this migration's default design.

## Implementation sequence

1. **Shared definitions and loading:** amend root definitions, the workflow-component standard, TASK, the selected runtime resolver, and validators together. Establish explicit selection, selective resource loading, resolved policy, and the legacy field adapter. Refresh applicable root-surface ownership rules to include `workflows/`.
2. **Two representative undertakings:** migrate one existing bounded workflow, such as dependency extraction, and one manager workflow, such as evaluation. Exercise input resolution, stage-specific resources, tool invocation, and manager/worker context separately. Both are concrete candidates for implementation planning.
3. **Collection migration:** move the 45 inventoried packages using the per-package map, reconcile companion contents, update live references and generated briefs, preserve declared legacy status, and resolve reader compatibility. Expand or combine packages only when their content and callers support that decision.
4. **Role reduction and extraction:** apply the accepted per-agent changes using workflow destinations. Build the two tool replacements and the other repairs before retiring their corresponding execution routes. Assess named-role usefulness and assign residual ownership for the 12 extraction candidates.
5. **Integration:** validate runtime context, results, callers, governance adoption, public export, project authority corpora and pinned mirrors. Route coordination notices for the actual touched surfaces. Retire compatibility adapters when the live reader/writer census and archived-run replay requirements allow it.

## Acceptance evidence

Use actual prompt/context captures to verify an ordinary session contains no workflow catalog or bodies; a selected manager receives its orchestration definition; and a worker receives only its selected undertaking and relevant resources. Check these separately for supported native and managed invocation routes. A remaining instruction-only load rule must be reported as such.

Exercise an ordinary run, a judgment-dependent branch, and a partial-run recovery. Verify tool invocation from a different execution directory, current/legacy selection fields, missing resources, read/write boundaries, and unchanged output compatibility. Compare the reduced roles against the original audit's behavioral probes, including the human design conversation for HELPS_HUMANS.

Structural validation must accept the proposed package shape and catch broken bindings. Behavioral checks must demonstrate that flexible execution still reaches the warranted result. The proposal itself is validated for source identity, coverage, and links; these future runtime and behavioral checks have not yet been executed.

## Status

The requested proposal revision is complete. The accepted conceptual direction is recorded in [HANDOFF_STATE.md](HANDOFF_STATE.md); specific remaining choices and implementation dependencies stay visible there. No live agent, workflow, runtime, or governing standard has been rewritten in this revision packet.
