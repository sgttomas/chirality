# TRANCHE 2026-07-06 — D-PEC-13 tracker contract v1

> **Epistemic status: execution vehicle for a ruled decision — not new
> authority.** The authority is the owner's D-PEC-13 O-A ruling (verbatim in
> `_DECISIONS/D-PEC-13_package_tracker_import_contract.md`, Human-ruling
> section; ruling received with `main` at `c4e00afbb`). This packet pins the
> ruled fence for execution and **may not widen it** (the packet's own rule);
> any needed widening returns to the owner as its own row. Precedent:
> `TRANCHE_2026-07-05_D-PEC-08_upload_agent_v1.md`;
> `_DECISIONS/D-PEC-17_builtin_agent_ui_source_tranche.md`.

## What ships (the ruled design, unchanged)

The sixth §16 import contract `tracker` + its proposal-shaped agent path,
exactly as specified in the ruled packet: a new first-class import-owned
`package_tracker` record (one row per tracked procurement package;
`UNIQUE(project_id, tracking_no)`); CSV contract columns per the packet table;
closed stage vocabulary `not_started | in_progress | complete | issued |
not_applicable` (normalized, unrecognized values reject the row); within-file
duplicate `tracking_no` → first occurrence wins, later occurrences land as
report **conflicts**, never applied, never silent; stated `package` anchor
must resolve or the row rejects (schedule precedent); NO intake fallback
(ruled divergence from RAIL — register rows, not action statements);
re-import always refreshes (import-owned, no in-app edit path in this scope);
`tracker` export case mirroring import columns (§16 round-trip);
`trackerRegisterView` + one new read-only route `GET /api/projects/:pid/tracker`;
Admin dropdown/export list entries; the one-line `CONTRACTS` allowlist
extension in the proposal seam.

## Exact file fence (verbatim from the ruled packet; anything outside is out of scope)

- `projects/pec/core/src/types.ts` (+ `core/src/index.ts` re-export if the
  export list is explicit): `PackageTracker` interface; `'package_tracker'`
  in the record-type enumeration. `ProjectSnapshot` NOT touched;
  `core/src/snapshot-index.ts` NOT touched; `server/src/repo.ts` NOT touched.
  No permission change, no new act family.
- `projects/pec/server/src/db.ts`: additive `package_tracker` table
  (`UNIQUE(project_id, tracking_no)`).
- `projects/pec/server/src/import/index.ts`: `importTracker`; `tracker` case
  in `importContract`; `tracker` case in `exportRegister`.
- `projects/pec/server/src/services/proposals.ts`: one-line `CONTRACTS`
  allowlist extension (refusal-message text follows the array).
- `projects/pec/server/src/services/views.ts`: `trackerRegisterView`.
- `projects/pec/server/src/api.ts`: exactly one new read-only route
  `GET /api/projects/:pid/tracker`.
- `projects/pec/web/src/pages/Registers.tsx`: read-only Tracker tab (no
  mutation controls).
- `projects/pec/web/src/pages/Admin.tsx`: `tracker` entries in the
  `CONTRACTS` dropdown list and the `EXPORTS` list.
- `projects/pec/server/test/import-tracker.test.ts` + a proposal-path test
  pinning `contract=tracker` (allowlist acceptance): synthetic fixtures only;
  v1+v2 idempotency, duplicate-key conflict, vocabulary rejection, anchor
  resolution/rejection, round-trip export.
- Coordination (not source): `IMPORT_TEMPLATES/tracker-template.csv` +
  IMPORT_MAPPING §tracker; this tranche packet; the D-PEC-13 ruling section;
  the register flips (D-PEC-13 → RULED; new residual row); the receipt; the
  evidence dir + proposals mirror.
- **Zero new dependencies** (ADR-002 / F-PEC-3); no root-manifest change; no
  lifecycle/state-machine addition.
- **Per the ruling's recorded interpretation: `_DomainEngines/profiles/pec.yaml`
  is NOT touched by this tranche** (the ruling did not open the profile-note
  edit; parked residual, receipt-recorded).
- **STOP clause (D-PEC-17 rider-8 pattern):** if execution discovers a
  DB-migration need beyond the additive table, an out-of-fence file, or
  behavior beyond the ruled design, STOP and return to the owner — no in-run
  fence widening.

## Rollback plan (from the ruled packet)

Branch-first (`codex/pec-dpec13-tracker`); the PR is the unit of revert — one
`git revert` of the merge commit restores the prior surface. The
`package_tracker` table is additive and inert when unreferenced (no existing
code path reads it; no migration of existing data; drill/backup surface
unchanged — the SQLite backup copies the whole DB file regardless of table
set). The allowlist, view, route, and dropdown entries revert with the same
commit.

## Verification plan (workplan step-4, at the tranche PR's final SHA)

pec `npm run typecheck && npm test && npm run build && npm run drill`
(including the new tests); repo self-check with no unexplained baseline
shift; full `tools/` pytest; coord-check on the committed range;
`git diff --check`; **adversarial scope check** — `git diff --name-only` on
the tranche commits ⊆ the fence above plus the enumerated coordination
surfaces; CI green; **owner merge is the gate** (no standing self-merge
authorization exists at execution time — the ruling's unless-clause does not
fire).

## Evidence bar (from the ruled packet)

Immutable `PEC_2026-07-06_DPEC13-evidence-01/`: **synthetic** tracker CSV
(v1 + edited v2) through the live proposal seam on a fresh scratch DB —
propose → dry-run → accept → apply; v2 update-in-place counts; one
duplicate-key conflict; one stated-anchor rejection; export-and-compare
round-trip; governance mirror under `_DomainEngines/proposals/pec/`;
demo-cast admin accept/apply disclosed per act with `force: false`; SHA-256
manifest; scratch DB deleted after capture. Then the **real** tracker.xlsx
run on the pilot-scratch standing instance (D-T0-20 O-B item (iv) visibility;
owner-clarified scratch/demo mutation basis), captured at the ruled grain:
count-level results + hashes only, **no verbatim real rows committed**
(ruling default, Decision-to-rule item 4). WF-5 discharges only when the
contract is shipped AND the live v1+v2 evidence is captured (D-PEC-10
direction item 3 bar).
