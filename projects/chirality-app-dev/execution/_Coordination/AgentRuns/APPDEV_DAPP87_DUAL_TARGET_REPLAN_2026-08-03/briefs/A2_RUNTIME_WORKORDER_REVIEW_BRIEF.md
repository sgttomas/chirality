# Sealed Brief — A2 Runtime, Work-order, and Validation Reviewer

Role: ephemeral Agent 2 generalist; no delegation.

Objective: independently analyze the frozen D-APP-87 basis for App
affected-client runtime requirements, deliverable/work-order implications, and
target-by-target validation. Do not define generic runtime or select
architecture.

Required review:

- state only App client requirements for both targets;
- mark generic runtime, sandbox, identity, version, resume, and Bash
  `BLOCKED_BY_ROOT` and trace them to current notices/rows;
- incorporate D-APP-89 completed migration evidence without treating facade
  retirement as complete;
- incorporate D-APP-88 R2 blocked/rollback evidence and routed Root notice
  without treating its hypothesis as cause;
- partition existing deliverables into candidate direct amendments,
  dependencies/cross-references, and no-change preservation;
- propose domain-first work ordering that reaches owner gates before
  implementation;
- construct common plus per-target source/UI/packaged/runtime-client evidence;
- enumerate later owner/foreign-loop gates.

Inputs: `ACTIVATION.md`, `BASIS_MANIFEST.csv`, `BASIS_INVENTORY.md`, and the
referenced repository files.

Write only:
`reviews/A2_RUNTIME_WORKORDER_RETURN.md` under this run root.

Return contract: findings, affected-client interface inventory, deliverable
partition, work order, validation matrix, blockers, and sufficiency verdict.
No source/authority/foreign write and no generic-contract selection.
