# Woven Dialogue Implementation Orchestration Plan

**RunID:** `APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23`
**Status:** `IMPLEMENTATION_VALIDATED_PR_PENDING`
**Selection authority:** direct owner activation, 2026-07-23
**Posture:** `MIXED`

## Ownership

The root run is the supervising cross-package integration owner. It does not
collapse the three WORKING_ITEMS package boundaries:

- PKG-02 manager: DEL-02-01, DEL-02-02, DEL-02-04.
- PKG-05 manager: DEL-05-04.
- PKG-08 manager: DEL-08-02, DEL-08-03.

Each package manager reports to the root integration owner. Siblings do not
coordinate directly. Cross-package findings return to the root for
`RECORD | RELAY | AMEND | HOLD | REPLAN | ESCALATE | ROUTE` disposition.

## Work sequence

1. **R0 — parallel read-only reconnaissance**
   - Map current shell/dialogue/artifact ownership and package acceptance
     criteria.
   - Identify exact reusable components, compatibility constraints, missing
     projection inputs, and disjoint implementation seams.
2. **C0 — serialized contract freeze**
   - Root integration owner freezes shared component props, projection types,
     local-state schema/migration, route compatibility, and shared CSS/layout
     ownership.
3. **I0 — disjoint implementation**
   - PKG-02: dialogue-centred shell, Navigator/artifact composition, Work
     presentation, and local-state behavior in assigned files.
   - PKG-05: pure event/session projection and isolated replay-lens components
     in new package-owned files.
   - PKG-08: recorded hierarchy/routing projection and dispatch compatibility
     in new package-owned files/tests.
   - Root integration owner alone edits shared shell entry points, route
     composition, shared types, and global styles.
4. **F0 — serialized fan-in**
   - Root integrates accepted package returns and resolves only within the
     frozen contracts.
5. **V0 — validation and independent review**
   - Targeted tests, registered checks, full regression, build, packaged
     Desktop, accessibility review, and independent code/projection review.
6. **C1 — package return and CHANGE**
   - Update execution evidence without lifecycle advancement, commit the
     bounded tranche, open a PR, and retain the old UI until separate owner
     retirement authority.

## Fan-in result

The three package returns were accepted within the frozen contracts. The root
integration owner composed the Woven Dialogue shell, retained the legacy UI
behind `?legacy=1`, and preserved the existing route, API, SSE, runtime,
permission, and dispatch boundaries. Independent reviews found presentation
and evidence-honesty issues; all material findings were corrected before the
candidate was declared validated. No deliverable lifecycle state was advanced.

## Shared-write rules

Only the root integration owner may edit:

- existing route entry files under `frontend/src/app/`;
- existing shared shell entry/composition files;
- `frontend/src/app/globals.css`;
- existing shared layout-state/type files;
- package lockfiles and build configuration;
- cross-package AgentRuns fan-in/closeout records.

Package workers may write only their frozen disjoint targets. Any discovered
need to change the shared list is a coordination notice, not implicit
permission.

## Fan-in gates

- Reconnaissance returns distinguish facts, inference, unknowns, and
  recommendations.
- Contracts are frozen before implementation dispatch.
- Changed paths stay within each worker's fence.
- Projection code cannot manufacture project or runtime truth.
- Live dialogue/replay isolation and compatibility tests must pass before
  shell fan-in.
- No lifecycle, release, or old-UI retirement claim is accepted.
