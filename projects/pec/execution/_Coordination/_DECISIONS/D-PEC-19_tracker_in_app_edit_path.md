# D-PEC-19 - PROPOSAL: tracker in-app edit path and import conflict guard

**Status:** PROPOSAL / AWAITING_RULING.
**Date prepared:** 2026-07-06
**Decision ID:** D-PEC-19
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act
is the owner's (K-AUTH-1; D-GOV-04). This packet authorizes no implementation
unless and until the owner rules an option that opens the source fence below.

Structure precedent: D-PEC-13 opened this row as a residual when the tracker
contract shipped import-owned and read-only; D-PEC-17 supplies the folded
source-tranche packet form; D-PEC-09 supplies the narrow-repair precedent.

## Why this row exists

D-PEC-13 shipped the sixth Section 16 contract, `tracker`, as an import-owned register
with no in-app edit path. That was deliberate: the ruled tranche kept the
Package Tracker useful quickly and parked targeted in-screen edits behind this
separate row.

The owner's workflow intent of record, quoted verbatim in D-PEC-13 from the
D-PEC-10 packet, includes:

> The interface will also allow the human to make targeted changes within the
> current screen and what it shows. But the agent is the primary means of
> making updates.

D-PEC-13 recorded the residual explicitly: if the owner later wants targeted
tracker edits, that adds an edit act plus the `lastChangeIsImport` conflict
guard, and opens a named register row. This is that row.

## Verified current state

| Fact | Source |
|---|---|
| Tracker rows are first-class `package_tracker` records, one row per package; the resolved package is the idempotency key and CoA tracking number is plain data. | `projects/pec/core/src/types.ts:719-748`; `projects/pec/server/src/db.ts:24-58`; owner amendment in `D-PEC-13_package_tracker_import_contract.md` |
| The import path updates existing tracker rows by `package_id` and currently always refreshes; `_force` is unused because no in-app edit path exists. | `projects/pec/server/src/import/index.ts:510-586` |
| Existing import contracts use `lastChangeIsImport(...) && !force` as the conflict guard when an in-app edit can race a re-import. | `projects/pec/server/src/import/index.ts` |
| The server exposes only a read route for tracker: `GET /api/projects/:pid/tracker`. | `projects/pec/server/src/api.ts:281` |
| The UI tracker tab states the row is read-only and has no mutation controls. | `projects/pec/web/src/pages/Registers.tsx:909-963` |
| `import.propose` includes the coordinator/document-control lane; `import.accept` stays admin-only. A tracker edit must not widen accept/apply authority or become an agent bypass around RBAC. | `projects/pec/core/src/permissions.ts:225-231` |

## Decision to rule

Whether to add an in-app tracker edit path for targeted human edits inside the
Tracker screen, and pair it with the import-side conflict guard needed to keep
weekly re-imports from silently overwriting human screen edits.

## Scope boundary

This packet is a proposal. It authorizes no source change, test change, profile
edit, data mutation, evidence run, import behavior change, or release act until
the owner rules. Under any option, the package-keyed tracker contract from the
D-PEC-13 owner amendment remains intact: edits never change `package_id`, and
`tracking_no` remains plain editable data, not a key.

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Authorize the bounded source tranche in this packet: add targeted tracker edits plus import conflict guard. | One branch may implement exactly the fence below, then stop at owner merge. |
| O-B | Adopt the design only and open a successor source-tranche row. | No source change under this row; preserves a second owner gate before implementation. |
| O-C | Defer. | Tracker remains import-owned/read-only; targeted screen edits wait. |

## Recommended option

O-A. The row is a direct residual of the owner's targeted-edit workflow intent,
the change is narrow, and the guard is mechanical: once humans can edit tracker
rows, the weekly import must report those edits as conflicts rather than
overwriting them.

## O-A tranche design

### Behavior

1. The Tracker tab gains an edit affordance for mutable tracker fields:
   `trackingNo`, `packageName`, `discipline`, `area`, package type fields,
   line items, vendors, expected delivery date, cost estimate, comments, and
   the twelve stage fields. `packageId` is not editable in v1 because it is the
   D-PEC-13 idempotency key.
2. The edit API uses optimistic concurrency: the request carries `version`; a
   stale edit returns the existing repo 409/version-conflict shape.
3. The edit validates the same closed stage vocabulary and `YYYY-MM-DD` date
   shape as the import contract. Invalid values reject; they are never silently
   coerced.
4. A successful edit records human history on `package_tracker`. That makes
   `lastChangeIsImport('package_tracker', id)` false until the next import
   refreshes the row.
5. Tracker import changes from "always refresh" to the same guarded pattern as
   the other editable import contracts: if a matching row's last change is not
   import and `force` is false, the row reports a conflict and does not mutate.
   `force=true` remains available only through existing human-admin apply/direct
   import gates; the agent's `import.propose` path still cannot accept/apply.
6. When an import does update a tracker row, it records import history as it
   does today, restoring the import watermark.

### Exact source fence

| File | Permitted change |
|---|---|
| `projects/pec/core/src/permissions.ts` | Add a narrow `tracker.update` permission, no wider than `risk.update`/`interface.update` and not granted to viewer-only roles. |
| `projects/pec/server/src/services/tracker.ts` | New service with `updateTrackerRow(...)`: permission check, versioned repo update, validation helpers, history record. |
| `projects/pec/server/src/api.ts` | Add exactly one mutation route, `PUT /api/projects/:pid/tracker/:id`, plus the existing permission probe can expose `tracker.update` automatically. |
| `projects/pec/server/src/import/index.ts` | Add the `package_tracker` `lastChangeIsImport` guard to `importTracker`; do not change package-key idempotency, export shape, or other contracts. |
| `projects/pec/web/src/pages/Registers.tsx` | Add tracker edit controls/modal in the existing Tracker tab only. No new navigation surface. |
| `projects/pec/server/test/import-tracker.test.ts` | Pin guarded import behavior: human edit creates conflict without force; force refreshes; import-watermark restored after refresh. |
| `projects/pec/server/test/*tracker*.test.ts` or an existing server route test file | Pin edit permission, version conflict, validation rejection, and successful history. |

No profile edit, root manifest change, dependency change, migration outside the
existing table, new operation family, new accept/apply authority, or agent
sidecar change is in scope. If execution discovers one is required, stop and
return to the owner with a new row.

### Verification plan

At the final implementation SHA: `PYTHONDONTWRITEBYTECODE=1 python3
tools/practitioner_harness/harness.py self-check`; full `tools/` pytest if
`tools/**` changes; PEC `npm run typecheck && npm test && npm run build && npm
run drill`; `git diff --check`; coord-check on the committed range; adversarial
scope check that changed paths are a subset of the fence above plus the
coordination packet/register/receipt. CI green; owner merge remains the gate
unless the owner explicitly grants merge authority in-session.

### Rollback plan

The PR is the rollback unit. Reverting the implementation commit removes the
route, service, UI controls, tests, and guarded tracker-import behavior. The
underlying `package_tracker` table and D-PEC-13 import contract remain intact.

## On ruling

- **O-A:** record the owner ruling verbatim here; flip this row
  AWAITING_RULING -> RULED; execute the fenced source tranche branch-first;
  run the verification plan; append a loop receipt; stop at owner merge unless
  merge authority is explicitly granted.
- **O-B:** record the ruling verbatim; flip this row RULED as design-only;
  open the successor source-tranche row NOT_PREPARED with the fence above; no
  source change under D-PEC-19.
- **O-C:** record the deferral verbatim; tracker stays read-only.

## Human ruling

AWAITING_RULING.
