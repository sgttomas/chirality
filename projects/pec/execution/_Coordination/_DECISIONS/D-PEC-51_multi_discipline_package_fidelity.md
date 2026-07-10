# D-PEC-51 — RULED: multi-discipline package fidelity

**Status:** RULED 2026-07-09 — owner-directed execution
**Decision ID:** D-PEC-51
**Prepared by:** PEC work loop agent; the owner supplied the ruling and modeling direction.

## Owner direction and verified defect

Owner direction of record (Ryan Tufts, in-session, 2026-07-09):

> “The action item superset is acceptable.”

> “Yes display multiple disciplines if the data is as such.”

The dated MDL carries a discipline for every represented package. Packages
`26020-PKG-136` and `26020-PKG-137` each carry both Process and Piping. The
current schema flattens package discipline to one scalar, the MDL v2 importer
writes discipline only to deliverables, and the Packages register omits the
package discipline even where RAIL populated it. The owner accepts the current
RAIL work-item/action superset, so issue-record semantics are unchanged.

## Ruled behavior

1. Add an additive package-to-discipline association preserving every distinct
   attested `(package, discipline)` pair and the source contract.
2. Backfill the legacy scalar package discipline and the discipline facts
   already retained on existing deliverables into the association table; keep
   the scalar field for compatibility while new read surfaces use the complete
   distinct association set.
3. MDL v2 and RAIL v2 both record every provided package discipline. Re-import
   remains idempotent and no discipline is inferred.
4. Packages register and detail display all associated disciplines; the
   register supports direct discipline filtering, sorting, searching, and CSV.
5. RAIL issues remain the existing package-anchored work-item/action superset.

## Exact fence

- `projects/pec/core/src/types.ts`, `projects/pec/core/test/fixtures.ts`
- `projects/pec/server/src/db.ts`
- `projects/pec/server/src/repo.ts`
- `projects/pec/server/src/services/views.ts`
- `projects/pec/server/src/import/index.ts`
- `projects/pec/server/test/**`
- `projects/pec/web/src/pages/Packages.tsx`
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/IMPORT_MAPPING.md`
- this packet, the PEC decision register, the standing PEC workplan, and the
  PEC loop receipt ledger
- local/demo DB backup, migration, and verification (never committed)

No new dependency, no issue-model change, no professional/issuance claim, and
no production/non-demo database mutation.

The additive source-fidelity and migration shape follows the ruled D-PEC-41
contract-v2 precedent: preserve attested values losslessly, retain legacy
compatibility fields, and make the richer read projection authoritative for
new display behavior.

## Verification and rollback

- Migration/backfill test; MDL/RAIL multi-discipline import and idempotency
  tests; Packages API/UI projection tests.
- Full PEC typecheck/tests/build/drill; demo DB backup and `quick_check`;
  browser verification of Process + Piping on packages 136/137 and unchanged
  package issue counts; self-check, coord-check, and `git diff --check`.
- Rollback source by reverting the tranche. Rollback demo data by restoring
  the verified pre-migration backup.

## Human ruling

**RULED:** preserve and display multiple package disciplines when the sources
carry them; retain the action-item superset exactly as directed above.
