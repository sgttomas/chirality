# Package activation and production

WORKING_ITEMS applies this method to a package-based undertaking; its general role also accepts other bounded undertakings.

1. Resolve PackageID, package path, selected deliverables, accepted source/decomposition basis, objective, completion criteria, authorization, dependencies, and write ownership. A single-deliverable undertaking selects that deliverable within its parent package.
2. Inspect package instructions, context/status/references, handoffs, dependencies, and Git state. Resolve each PROJECT/SOFTWARE representation as LEGACY_FOUR_DOC, SOW_V1, MIGRATION_DUAL, AMBIGUOUS, or INVALID. MIGRATION_DUAL requires the exact isolated conversion grant; ambiguous/invalid state remains blocked for dependent production.
3. Use `construct-local-work-graph` to derive the selected undertaking's work graph from consumer-local `deliverable.yaml` needs, scope and relevant work material in the project's adopted locality (`Work/` by the shared default). Include objectives, actual input/use conditions, read context, write ownership, integration owner, expected returns and concurrency. Assess each needed condition from evidence; retain source unknowns and reciprocal/technical holds. Record the descriptive posture and revise the plan as actual conditions change; a saved view does not become dependency authority.
4. Assign disjoint work whose actual input conditions permit the selected activity to TASK or an authorized ephemeral Type 2 instance. Each brief names its context, tools, writes, outputs, acceptance, dependencies, and return path. Serialize overlapping writes.
5. Record, relay, amend, hold, replan, escalate, or route updates through the parent. Version amendments and preserve claim status and evidence. A direct-human manager presents cross-package decisions to the human.
6. Validate each return’s artifacts, acceptance, tests, containment, conflicts, dependencies, and integration result. Accept, rerun, hold, or escalate; assess each dependant's actual needed condition and intended use before proceeding. Lifecycle state, file presence and a successful query do not establish suitability.
7. Return package status, accepted outputs, derivative disposition, validation,
decisions, waivers, notices, blockers, and rerun requirements. Route lifecycle
decisions through review and scope amendments through scope-change. Hand any
repository closeout evidence and exact change scope to the responsible current
role, which follows the applicable project's change skill or repository
conventions when present, or the generic `change` workflow otherwise. This
method itself does not require Git; preserve a historical `change` identity for
explicitly selected legacy runs.

When runtime telemetry is required, use tools/workflow_runtime/runtime_telemetry.py with stable session/event IDs. Record attempts, checks, retries, remediations, detection layers, failure classes, reason codes, member IDs, and dispositions. Exposed token/context occupancy may be recorded; missing measurements remain explicit. Bind RUNTIME_SUMMARY.json in the package manifest and disclose interrupted sessions and required reruns.

For representation conversion, load workflows/scope-of-work/resources/representation-migration.md. Each child brief names affected OUT-*, REQ-*, AC-*, VER-* IDs or the frozen mapping basis and exact migration authority.
