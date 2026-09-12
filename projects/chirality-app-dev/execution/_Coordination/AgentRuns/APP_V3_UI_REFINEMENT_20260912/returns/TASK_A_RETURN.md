# TASK A return: workflow navigation in the authoritative catalog layer

Role: TASK (Type 2), Claude Fable 5.1 via the Claude Code Agent tool. No delegation.
Basis: 19bca4930 on branch claude/chirality-ui-refinement-20260912 (worktree
/Users/ryan/dev/chirality/.claude/worktrees/project-first-impressions-06aed9).
Nothing committed, stashed, or switched.

Mid-task course correction from the coordinator was applied: the specialist
`group` object also carries `order`, the 0-based index of the group in
`catalog.yaml` `navigation.specialist`. Everything else follows the brief.

## Files changed (all within the brief's write scope)

- workflows/catalog.yaml: added top-level `navigation` with `core` (9), eight
  `specialist` groups, and `superseded` (3). `centralWorkflowNames` untouched.
- workflows/catalog.schema.json: `navigation` added as a required property with
  nested `additionalProperties: false` objects; core fixed to 9 items; specialist
  entries take optional `tier` (primary or supporting); superseded entries require
  `replacedBy`; workflow names validated by a shared `$defs/workflowName` pattern.
  Top-level `additionalProperties: false` kept. Group order is not authored in the
  catalog; it is derived from array position by the generator.
- workflows/index.json: regenerated only, with the generator (byte-identical to
  generator output; `--check` passes).
- tools/validation/build_workflow_index.py: `CORE`, `CORE_DISPLAY_NAMES`,
  `NAVIGATION_CATEGORIES`, `NAVIGATION_TIERS` constants; new `parse_navigation()`
  that validates the partition (core exactly the nine in order, displayName only
  where fixed, unique kebab-case group keys, non-empty labels, tier default
  primary, every name placed once, `replacedBy` naming an existing non-superseded
  workflow) and returns per-workflow navigation descriptors including
  `group.order`; descriptor `compatibility` is now `legacy` iff superseded, else
  `canonical`; `navigation` emitted on every workflow descriptor and never on
  skills; precise `navigation/package disagreement: missing=[...], extra=[...]`
  error; a closing check that legacy is reserved for superseded workflows.
  `--check`, `--public-export`, `--bootstrap` behaviour kept; `--bootstrap` now
  preserves an existing catalog `navigation` block (or writes a core-only
  skeleton when none exists) so it still works on Root.
- tools/validation/test_workflow_catalog.py: fixture root now creates the nine
  core packages and a navigation block; updated the classification test
  (canonical for all non-superseded, legacy only for the three superseded,
  central still the six, no navigation on skills); added four tests covering the
  Root partition counts and orders, missing/extra/malformed entries, superseded
  replacement rules, and the fixed core list with bounded display names.
- projects/chirality-runtime/packages/contracts/src/v3.ts: added
  `MethodNavigationCategory`, `MethodNavigation` (with
  `group?: { key; label; order }`), and `navigation?: MethodNavigation` on
  `MethodDescriptor`.
- projects/chirality-runtime/packages/core/src/method-catalog.ts: `IndexEntry`
  gains optional `navigation`; new `parseNavigation()` with strict validation
  (unknown fields, unknown category or tier, non-integer or negative order,
  non-string displayName or label, non-kebab group key, group order not a
  non-negative integer, group on a non-specialist entry, missing group on a
  specialist entry, `supersededBy` on a non-superseded entry, missing
  `supersededBy` on a superseded entry, navigation on a skill entry, and category
  disagreeing with compatibility are all invalid index entries, surfacing through
  the existing invalid-index path as `malformed-execution-metadata` on the source
  root). Navigation is carried onto the descriptor exactly as `central` and
  `compatibility` are: index-only, so project and user packages never get one.
  Legacy alias behaviour untouched.
- projects/chirality-runtime/tests/method-catalog.test.ts: two new tests
  (navigation carried from the bundled index onto workflow descriptors only, with
  a same-named project workflow getting none; a table of malformed navigation
  entries each rejected, plus the category/compatibility mismatch). No new
  fixture files were needed.

Not changed: tools/validation/validate_workflow_metadata.py (it delegates to
`validate_and_build` and does not re-validate the catalog shape itself). No
WORKFLOW.md bodies, no App files, no docs. `grep -rn "centralWorkflowNames\|chirality-method-index" docs/`
returned nothing, so no doc sentence was changed (the only non-code hit is
agents/registry.json, which names the index schema and paths only).

## Partition counts (on-disk set matched the brief's list exactly: 71 of 71, no missing, no extra)

- core: 9 (order 0..8: project-setup, project-decomp, software-decomp,
  domain-decomp, research-orchestration, scope-change, task-management "Manage
  tasks", review "Review results", reconciliation "Check project status")
- specialist: 59 across 8 groups (group order 0..7):
  - 0 plan-organize "Plan & organize": 6
  - 1 research-understand "Research & understand": 8 (1 supporting)
  - 2 extract-documents "Extract from documents": 15 (9 supporting)
  - 3 create-publish-documents "Create & publish documents": 8 (5 supporting)
  - 4 build-maintain-software "Build & maintain software": 4
  - 5 estimate-cost "Estimate & cost": 3
  - 6 review-check "Review & check": 10 (1 supporting)
  - 7 manage-changes "Manage changes": 5
- superseded: 3 (pandid-valve-tile -> pandid-valve-symbol-instance,
  pdf2md-page -> pdf2md-page-full, pdf2md-page-assets -> pdf2md-page-full)
- total workflows: 71; index methods: 79 (71 workflows + 8 skills); public
  export: 78. `compatibility: legacy` on exactly the 3 superseded; `central` true
  on exactly the 6.

## Commands run and results (all after the final group.order change)

- `python3 tools/validation/build_workflow_index.py` (regenerate): PASS, 79 methods.
- `python3 tools/validation/build_workflow_index.py --check`: PASS, 79 methods.
- `python3 -m pytest tools/validation/test_workflow_catalog.py -q`: 21 passed.
- `python3 -m pytest tools/validation -q -x -k "workflow or catalog or metadata"`:
  30 passed, 481 deselected. No pre-existing failures observed.
- projects/chirality-runtime: `npm run build` (tsc -b): exit 0, no diagnostics.
- projects/chirality-runtime: `npx vitest run tests/method-catalog.test.ts tests/runtime-v3-api.test.ts`:
  2 files, 47 passed.
- projects/chirality-app-dev/frontend: `npx vitest run src/__tests__/scripts/prepare-packaged-instruction-root.test.ts`:
  3 passed.
- projects/chirality-app-dev/frontend: `npm run instruction-root:prepare`: PASS,
  "prepared packaged instruction root (366 files)".
- projects/chirality-app-dev/frontend: `npm run instruction-root:integrity`:
  exit 1, "ENOENT: no such file or directory, scandir
  .../frontend/dist/mac-arm64/Chirality.app/Contents/Resources/instruction-root".
  There is no `dist/` directory in this worktree; the script verifies a packed
  Electron app, so this is a packaging precondition, not a failure caused by the
  index change.
- `python3 tools/validation/validate_candidate_whitespace.py --base-ref 19bca4930`:
  PASS (candidate whitespace is clean). Note this ran over every candidate change
  in the worktree, including the parallel App session's files.
- Extra behaviour probe on a scratch copy of workflows/, .agents/, agents/, tools/
  (outside the repository): `--bootstrap` then `--check` PASS with the catalog
  byte-identical to Root's; `--public-export` PASS with 78 methods and navigation
  on all 71 workflows.

## Observations

- The worktree also contains uncommitted App frontend changes and untracked files
  under projects/chirality-app-dev/frontend (electron/, src/components/shell/,
  woven-dialogue/, lib/shell/workflow-library.ts, and others) from the parallel
  App session. I did not touch them; `git diff --stat` restricted to my eight
  files shows 8 files changed.
- The runtime rejects a whole bundled index (all its packages surface as
  malformed) when any navigation entry is invalid, which matches how the existing
  invalid-entry checks behave; it does not degrade a single entry.
- Nothing in the brief was left undone.
