# Agent 2 Return — DEL-08-02 Real Legacy Route Marker

- RunID: `APPDEV-PKG08-DEL0802-LEGACY-MARKER-2026-08-02`
- ChildInstanceID: `A2-DEL0802-LEGACY-MARKER`
- AcceptedBasis and execution HEAD: `1d4abf1cf1a23a33bd7fec59971251f86c010210`
- Result: `COMPLETE_WITH_EXTERNAL_CHECK_LIMITATIONS`
- Delegation: none
- Commit/push/merge: none

## Exact changed files

1. `projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-route.tsx`
2. `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-route.test.tsx`
3. `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-02_Persona_Alias_and_Agent_Matrix_Routing_Contract/_run_records/R2_LEGACY_MARKER_2026-08-02/AGENT2_RETURN.md`

No status, memory, activation, loop, plan, decomposition, dependency,
lifecycle, decision, Task Management, parity, runtime, or other manager-owned
surface was edited by this child.

## Implementation and rationale

`WovenDialogueRoute` now owns the legacy-route marker. Its legacy branch wraps
the injected `ReactNode` in a semantic-free `div` bearing
`data-legacy="true"`. The boundary uses inline `display: contents`, so it does
not generate a layout box and therefore does not alter the injected legacy
content's layout. A boundary is required because `legacy` is an arbitrary
`ReactNode`; cloning only a child element would not cover strings, fragments,
arrays, or other valid node forms.

The focused test now injects an unmarked `<main>Legacy</main>`. It proves that:

- the default Woven branch contains no `data-legacy` marker;
- `legacy=1` produces exactly one `data-legacy="true"` marker owned by the
  route component;
- the boundary is layout-neutral through `style="display:contents"`; and
- the injected legacy content remains present.

## Validation evidence

- `npm test -- --run src/__tests__/components/woven-dialogue-route.test.tsx`
  — PASS: 1 file, 2 tests.
- `npm run typecheck`
  — PASS: frontend and Electron TypeScript checks.
- `npm run build`
  — PASS: Next production build, static generation of 24 pages, and Electron
  build.
- `npm test`
  — EXTERNAL FAILURE: 139 files passed, 1 failed, 1 skipped; 1095 tests
  passed, 1 failed, 4 skipped. The sole failure is the concurrently modified,
  out-of-scope
  `src/__tests__/components/woven-dialogue-navigator.test.tsx` test
  `toggles from recent to all recorded sessions and back through the actual control`,
  where Next `Link` raises `ReferenceError: self is not defined`. The focused
  route suite passes independently.
- `npm run harness:validate:premerge`
  — ENVIRONMENTAL FAILURE: no harness server was listening at
  `http://127.0.0.1:3000`; the generated summary records eight `fetch failed`
  setup/probe results and no product assertion. This command needs rerun in
  its server-backed validation environment.
- `git diff --check`
  — PASS: no whitespace errors in the combined worktree diff.
- Containment audit
  — PASS for this child: its only source/test edits are the two authorized
  targets above, plus this authorized return. Concurrent PKG-02 navigator
  changes/run records and the environment `frontend/node_modules` symlink
  were observed and left untouched.

## Source/test hashes

- `woven-dialogue-route.tsx` SHA-256:
  `3c23b857727b1911c25bd1027089520e8f102a445a689e6a7677713f840ad10b`
- `woven-dialogue-route.test.tsx` SHA-256:
  `83847096d8a0e3949ead1dbacce98b7a62cc691c252bfd3f0c24335eb5a426d8`

## Limitations and escalation

The objective is implemented and its focused/type/build checks pass. Before
fan-in acceptance, the manager should rerun the full Vitest suite after the
concurrent navigator change is stabilized and rerun the premerge harness with
its required server active. Neither limitation warrants an out-of-scope edit
by this child.
