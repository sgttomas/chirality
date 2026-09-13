# TASK: core workflow for creating workflows

Direct owner direction on 2026-09-13 UTC: make a CORE workflow that agents
follow when creating a workflow, teaching the Chirality conventions needed for
later consistency and reuse. Leave domain reasoning, writing approach, plan and
delegation to the agent and the actual undertaking. This is not a skill or a
workflow-authoring form. Owner also approved hiding Skills UI for this release;
that UI work is outside this assignment.

Type 2, gpt-6-astra medium, fresh context, no delegation. Read Root/App AGENTS,
agents/AGENT_TASK.md, workflows/README.md, catalog/index format, existing package
validator and App product instructions. Use the preserved former HELPS_HUMANS
method only as historical design evidence, not current mandatory gates.

Implement a concise `workflows/create-workflow/WORKFLOW.md` with useful source
and validation pointers. It should cover purpose/outcomes and adaptability;
project vs personal scope; canonical package names/frontmatter and optional
execution metadata/resources; required facts vs contextual choices; identifiable
inputs/outputs, dependencies, appropriate agent responsibilities, useful checks,
failure/recovery, reusability without embedding this run's private particulars;
existing-name conflicts and revision preservation; actual registration/discovery,
and a checkable return naming where saved and what was verified. No mandatory
extra approvals, specialized agent roster, exact prose template, repeat forced
delegation, Git requirement, or fabricated tools. Keep authoring proportional.

Add it as a core/central workflow to machine catalog and regenerate index using
the existing authoring utility. Add a brief mandatory-on-authoring pointer to
Root AGENTS and product instructions/AGENTS.md: load this core workflow before
creating or revising a reusable workflow, including ordinary conversational
requests, and use the selected library basis. The App/general-purpose method
must not inherit repository development governance or invent host permissions.

Allowed writes: new workflow package, workflows/catalog.yaml, workflows/index.json,
Root AGENTS.md and projects/chirality-app-dev/instructions/AGENTS.md. Parent
scope extension: tools/validation/build_workflow_index.py,
tools/validation/test_workflow_catalog.py, workflows/README.md and
workflows/catalog.schema.json may change to accommodate the new core entry.
Keep useful membership/order/schema agreement checks without incidental total
catalog counts. No
frontend code, role instructions, run records, manifests, notices, Git mutations,
App/supplier/model runs, private state, cleanup or publishing. Parent handles
manifest/notices and integration; request a scope adjustment if tests hard-code
the six central names. Run existing focused workflow/index/instruction validators
and report exact commands, findings and remaining integration needs. Parent owns
independent full-diff review and real authoring/reuse qualification.
