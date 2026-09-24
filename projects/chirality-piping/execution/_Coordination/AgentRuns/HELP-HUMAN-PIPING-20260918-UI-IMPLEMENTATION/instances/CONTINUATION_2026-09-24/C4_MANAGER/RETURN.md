# C4 manager source return

Local source freeze: `0ec48a4f891de3a1a48fb967c52da75b0640a196` on `codex/piping-c4-policy-20260924`, parent/base `5cfd2257cafca0fb141fc7dd5085c627d8caae9e`. Six added source/test files only, 510 lines. Evidence is recorded in the subsequent local evidence-only commit. No push, PR or merge. Parent-supplied C4_MANAGER_BRIEF.md remains unmodified and untracked here, outside manager-owned evidence.

## Result and inspection

The pure policy uses existing ModelIndex/EntityKey identities, supports existing node/pipe/support/component identity labels, prioritizes primary → hover → separately supplied current-row node → remaining ordered selection, and deduplicates valid roles. It applies Hide/eligibility before mode allocation. Budget is floor(drawable CSS width × height / 3600); all eligible context is attempted first, ordinary labels use slots left by successful context placements, Off retains context, and All removes the count cap. It returns placed, suppressed, ineligible and unplaced identities/reasons plus actual planned placement counts and context overflow. The future renderer must reconcile diagnostics to applied visible DOM; these pure results alone are not rendering evidence.

Placement consumes measured plate dimensions and caller-supplied required geometry picking rectangles. It tries at most 24 deterministic positions, preserves containment/non-overlap/obstacle exclusion, rejects malformed measurements/obstacles, and reports failures. Invalid current-row non-node publication is diagnosed without stealing the entity's legitimate selected/ordinary role. Hidden context remains ineligible. No absent engineering plate is invented.

Manager inspected all final source/test files and child return, verified their hashes against TASK_POLICY/BASIS_AND_OUTPUT_HASHES.json, inspected the staged six-file index and committed scope, and ran Git whitespace diagnostics successfully. This is manager integration inspection, not required fresh-context independent complete-diff review. No observed source blocker remains from that static inspection; compilation/runtime correctness is unverified.

The first draft rescanned all obstacles; manager requested repair following ROOT's cost concern. Final layout reuses validated 64px-cell collision indexes, caps grid references per rectangle/query at 256, and uses an exhaustive fallback for large rectangles or unsafe cell coordinates. These are indexing choices, never label-count caps. Ordering costs O(N log N); typical queries inspect intersected buckets plus oversized obstacles. Dense/oversized worst case remains O(N × (P + N)) over the fixed 24 candidate positions; memory has up to 256 references per indexed obstacle. No measured performance, arbitrary-selection guarantee, global packing optimality or qualification is claimed.

## Verification and remaining work

Maintained tests cover CSS budgets (138/230), 139 context overflow, 120 successful of 139 context plus 18 ordinary slots, Off/All, role dedup/current-row independence, typed shared IDs, Hide in every mode, unsupported/invalid geometry, deterministic ordering, containment/picking/collision failures, invalid rectangles, and spatial-index equivalence against exhaustive overlap including boundaries and extreme finite coordinates. Tests were authored but **none executed**. Local node_modules are absent and normal Vitest setup unconditionally awaits loadWasmEngine; no installation, setup bypass or alternate harness was attempted. No browser/native/server/build/WASM/timed work ran.

Pending normal command from REPO_ROOT after ROOT admits dependencies/engine setup/resources:

```sh
npm --prefix projects/chirality-piping/apps/desktop test -- src/features/viewport/labelPolicy.test.ts src/features/viewport/labelPlacement.test.ts src/features/viewport/labelCollisionIndex.test.ts
```

[UI_HANDOFF.md](UI_HANDOFF.md) gives the exact requested owning-writer scopes: canvas PipeViewport/resource integration and measured/projection/picking inputs; separate shell actual current-row publication, shared three-mode action/session semantics, and truthful diagnostics/accessibility. All existing shared files and protected D-72 helpers/fixtures/oracles/numeric limits are untouched. Later fresh review, applicable ordinary checks/DEC-025, connected native evidence, owner-held second-profile population freeze and timed qualification remain outstanding. This return completes only the isolated pure-source contribution, not C4 or the UI programme.

## Provenance

Actual parent `/root`, manager `/root/c4_manager` WORKING_ITEMS Type 1, child `/root/c4_manager/policy_task` TASK Type 2. Child launched fresh via collaboration.spawn_agent with Astra/low under the preserved owner allocation and ceased writing before freeze. Parent and manager source origins/hashes are in SUPPLIED_BASIS.json; child origins/output hashes and return are under TASK_POLICY. DELEGATION.md records boundaries and actual mechanism. Raw readiness/freeze outputs are under _run_records. Manager consulted TASK instructions before dispatch as required; no children were delegated by TASK.
