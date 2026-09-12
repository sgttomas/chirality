# Launch brief — TASK A: workflow navigation in the authoritative catalog layer

Role: TASK (Type 2). Engine/model: Claude Fable 5.1 (Claude Code Agent tool). No delegation.
Parent: implementing session for APP_V3_UI_REFINEMENT_20260912. Basis: 19bca4930.
Repository: /Users/ryan/dev/chirality/.claude/worktrees/project-first-impressions-06aed9 (git worktree; branch claude/chirality-ui-refinement-20260912; do not switch branches, do not commit, do not stash).

## Purpose

Move App workflow navigation classification into the Root workflow catalog
(`workflows/catalog.yaml` → generated `workflows/index.json` → Runtime
`MethodDescriptor`) so the App displays categories without interpreting
workflow bodies. Stop stamping every non-central workflow `compatibility:
legacy`; reserve `legacy` for genuinely superseded workflows and record their
replacement. Do not rewrite any WORKFLOW.md body. Do not change
`centralWorkflowNames` (the six stay as is).

## Contract (fixed; the App is being coded against it in parallel)

In `projects/chirality-runtime/packages/contracts/src/v3.ts`, add to `MethodDescriptor`:

```ts
export type MethodNavigationCategory = "core" | "specialist" | "superseded";
export type MethodNavigation = {
  category: MethodNavigationCategory;
  /** primary: shown at first glance; supporting: a bounded step of a primary workflow, shown under a disclosure. */
  tier: "primary" | "supporting";
  /** Position within its category (core) or group (specialist); 0-based. */
  order: number;
  /** Product display name when it differs from the identifier (Core only today). */
  displayName?: string;
  /** Specialist group; label as authored. */
  group?: { key: string; label: string };
  /** Superseded only: the current replacement workflow name. */
  supersededBy?: string;
};
// MethodDescriptor gains: navigation?: MethodNavigation;
```

`workflows/catalog.yaml` (JSON subset of YAML, as today) gains a top-level `navigation` object:

```json
"navigation": {
  "core": [ { "name": "project-setup" }, ..., { "name": "task-management", "displayName": "Manage tasks" }, { "name": "review", "displayName": "Review results" }, { "name": "reconciliation", "displayName": "Check project status" } ],
  "specialist": [ { "key": "plan-organize", "label": "Plan & organize", "workflows": [ { "name": "preparation" }, { "name": "x", "tier": "supporting" } ] }, ... ],
  "superseded": [ { "name": "pandid-valve-tile", "replacedBy": "pandid-valve-symbol-instance" }, ... ]
}
```

Generator rules (`tools/validation/build_workflow_index.py`):
- Every bundled workflow package appears exactly once across core, specialist groups and superseded; report missing/extra names precisely.
- `core` is exactly nine, in this order: project-setup, project-decomp, software-decomp, domain-decomp, research-orchestration, scope-change, task-management, review, reconciliation. It must include all six `centralWorkflowNames`. `displayName` only where given above.
- Specialist group keys are unique kebab-case; labels non-empty; `tier` defaults to `primary`.
- `replacedBy` must name an existing, non-superseded bundled workflow.
- Descriptor `compatibility` is `"legacy"` iff the workflow is superseded, else `"canonical"`. `central` stays true only for the six.
- Emit `navigation` on every workflow descriptor: `{category, tier, order, displayName?, group?, supersededBy?}`; `order` is the 0-based index within core, within its specialist group, or within superseded. Skills get no `navigation`.
- Keep `--check`, `--public-export`, `--bootstrap` behaviour. Update `workflows/catalog.schema.json` accordingly (keep `additionalProperties: false`).
- Regenerate `workflows/index.json` with the generator (byte-identical to generator output, as the test requires).

Runtime (`projects/chirality-runtime/packages/core/src/method-catalog.ts`): parse optional `navigation` from index entries with strict validation (unknown category/tier, non-integer order, non-string labels, or `supersededBy` on a non-superseded entry are invalid index entries); carry it onto the descriptor exactly as today's `central`/`compatibility` are (index-only; project and user packages never get one). Keep existing legacy alias behaviour untouched.

## Classification to apply (already decided by the parent; do not reopen)

Core (9, ordered): project-setup, project-decomp, software-decomp, domain-decomp, research-orchestration, scope-change, task-management (Manage tasks), review (Review results), reconciliation (Check project status).

Specialist groups (key → label → workflows; `(s)` = supporting tier):
- plan-organize → "Plan & organize": preparation, scope-of-work, four-documents, kty-metadata-align, aggregation, proposal-format
- research-understand → "Research & understand": researcher, domain-hypergraph, domain-engine, lens-register, semantic-lensing, semantic-matrix-build (s), content-digest, software-repository-reconnaissance
- extract-documents → "Extract from documents": pdf2md, pdf2md-orchestration, pdf2md-page-full (s), pdf2md-folio-extract (s), drawing-extract, drawing-extract-page (s), drawing-titleblock-page (s), equation-audit, equation-bbox-detect (s), equation-flag-interpret (s), dependency-extract, equipment-extract, domain-source-atomize (s), domain-prose-validate (s), pandid-valve-symbol-instance (s)
- create-publish-documents → "Create & publish documents": dbm-publisher, domain-documents, dbm-draft-review, dbm-publish (s), dbm-section-publish (s), dbm-concordance-seed (s), dbm-concordance-verify (s), dbm-postauthor-concordance (s)
- build-maintain-software → "Build & maintain software": software-bounded-implementation, software-code-review, software-defect-diagnosis, software-test-planning
- estimate-cost → "Estimate & cost": estimate-prep, estimate-snapshot, equipment-costing-extract
- review-check → "Review & check": audit-agents, audit-decomp, audit-dep-closure, audit-epistemic, audit-governance, audit-hypergraph-closure, deliverable-consistency, decomposition-package-review, evaluation-protocol, evaluation-report (s)
- manage-changes → "Manage changes": change, scope-change-packet, scc-resolution-case, kty-content-remediate, audit-scope-closure

Superseded: pandid-valve-tile → pandid-valve-symbol-instance; pdf2md-page → pdf2md-page-full; pdf2md-page-assets → pdf2md-page-full.

Total must be 71. If the on-disk set differs from this list, stop and report the difference instead of inventing a placement.

## Write scope (exact)

- workflows/catalog.yaml, workflows/catalog.schema.json, workflows/index.json (regenerated only)
- tools/validation/build_workflow_index.py, tools/validation/test_workflow_catalog.py, tools/validation/validate_workflow_metadata.py (only if it re-validates the catalog shape)
- projects/chirality-runtime/packages/contracts/src/v3.ts
- projects/chirality-runtime/packages/core/src/method-catalog.ts
- projects/chirality-runtime/tests/method-catalog.test.ts and any fixture it needs
- If a Root doc enumerates the index descriptor fields normatively (grep docs/ for `centralWorkflowNames` / `chirality-method-index`), update that one sentence and report it; otherwise touch no docs.

Nothing else. No WORKFLOW.md edits. No App (`projects/chirality-app-dev`) edits. No git commits.

## Checks to run and report (exact commands and results)

- `python3 tools/validation/build_workflow_index.py --check` (and whatever the script's usage says for regeneration)
- `python3 -m pytest tools/validation/test_workflow_catalog.py -q`
- `python3 -m pytest tools/validation -q -x -k "workflow or catalog or metadata"` (report any pre-existing failures separately)
- In projects/chirality-runtime: `npm run build` (or the package's typecheck) and `npx vitest run tests/method-catalog.test.ts tests/runtime-v3-api.test.ts`
- In projects/chirality-app-dev/frontend: `npx vitest run src/__tests__/scripts/prepare-packaged-instruction-root.test.ts` and `npm run instruction-root:prepare && npm run instruction-root:integrity` if they are quick; report any failure that the index change causes.
- `python3 tools/validation/validate_candidate_whitespace.py --base-ref 19bca4930`

## Return

Write your return to projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_UI_REFINEMENT_20260912/returns/TASK_A_RETURN.md: files changed, the exact partition counts (core/specialist per group/superseded/total), commands run with results, anything you could not do, and any doc sentence you changed. No em-dashes in prose.
