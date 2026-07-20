# Sealed Child Brief — DEL-02-01 CQ-F1 Slice

- Parent: RECONCILIATION R1-RETRY
- Role form: ephemeral bounded Agent 2 generalist; do not delegate
- Frozen basis: `57652ba1cd0905e8f47131e4c4ebf518272f7c16`
- Exact population: 14 paths, each listed below exactly once
- Subject access: read-only
- Sole write: this directory's `RETURN.json`

## Objective

Inspect the exact 14 paths against live implementation, importing/calling surfaces,
tests, DEL-02-01's current ScopeOfWork/Specification/Datasheet/Procedure/Guidance,
`_STATUS.md ## Remaining`, dependencies, and governing D-APP-56/60/64/65/68/69
authority. Determine functional affinity, the nearest existing deliverable mapping or
an honest shared/unresolved boundary, evidence strength, materially important
alternatives, and the required `DISPOSITION_CLASS | OWNER_CLASS | NO_REPAIR |
BLOCKED_INPUT` route. Prior R4-P48 affinity is evidence only. Code is never authority.
Any ownership/scope/recorded-limit touch is fast-reject `OWNER_CLASS` and any accepted
mapping remains `PROPOSAL` only. Do not run tests or modify subjects.

## Exact paths and frozen Git blobs

1. `projects/chirality-app-dev/frontend/src/app/globals.css` — `6eb6d932410368d2163208fa40ec08061a4c9bb8`
2. `projects/chirality-app-dev/frontend/src/app/page.tsx` — `cd6f59518b286a5608a7437e5ff589dc784d6c6d`
3. `projects/chirality-app-dev/frontend/src/components/shell/chat-markdown.tsx` — `432a818cfbd7ddba0cb47ba6cf80bdfd807cec97`
4. `projects/chirality-app-dev/frontend/src/components/shell/document-view.tsx` — `6661e9bf29ef9d0f6bce7e9cf1f3273cd4eb2580`
5. `projects/chirality-app-dev/frontend/src/components/shell/file-picker.tsx` — `38ecfb7e6f5f9c07c14c2bc879cef151e27f0dd9`
6. `projects/chirality-app-dev/frontend/src/components/shell/session-list-view.tsx` — `f95349110f975b7ce8126bc7318538774a9daafe`
7. `projects/chirality-app-dev/frontend/src/components/shell/subagent-stream-view.tsx` — `c2dbe2ee7ece4d0e6485cf42c94c0c73b1c70d96`
8. `projects/chirality-app-dev/frontend/src/components/shell/tool-stream-view.tsx` — `d2551728e384695c40be1382ed9e55e059f6a5b1`
9. `projects/chirality-app-dev/frontend/src/components/workspace/harness-events-provider.tsx` — `b6cfd4af376a0cd6a606e55f1c0fa368ce0e61d3`
10. `projects/chirality-app-dev/frontend/src/lib/shell/ansi.ts` — `53500f33e066567f39f03978fd7f59f6b8ade9e0`
11. `projects/chirality-app-dev/frontend/src/lib/shell/document-view-state.ts` — `48282f1728ca102bfabe2cd2e35d3d3733bcb923`
12. `projects/chirality-app-dev/frontend/src/lib/shell/harness-event-buffer.ts` — `130cd4eb120ed1db6a6617c43f0f6547e8f56118`
13. `projects/chirality-app-dev/frontend/src/lib/shell/harness-event-views.ts` — `d55600739abd324041f187aea24077c6edb729e8`
14. `projects/chirality-app-dev/frontend/src/lib/workspace/navigation-intent.ts` — `81046ec9480496bea79a7ee2ae148815a48bdd43`

## Return contract

Write valid JSON to `RETURN.json` with top-level keys `basis`, `container`,
`expected_count`, `rows`, `slice_findings`, `disagreements`, `blockers`, and
`containment`. `rows` must contain 14 unique objects in the exact path order. Each
object must contain: `path`, `source_blob`, `source_sha256`, `implementation_summary`,
`implementation_citations`, `verification_evidence`, `normative_sources`,
`authority_anchors`, `lifecycle_state`, `remaining_evidence`, `prior_affinity`,
`candidate_mapping`, `mapping_status`, `competing_candidates`,
`rejected_alternatives`, `evidence_strength`, `concordance_disposition`,
`action_class`, `fast_reject_limits`, `rationale`, and `rerun_triggers`.

Acceptance: 14/14 exact scope; live line/path citations; no unsupported ownership;
every material alternative named; no subject writes; no claims beyond the frozen basis.
