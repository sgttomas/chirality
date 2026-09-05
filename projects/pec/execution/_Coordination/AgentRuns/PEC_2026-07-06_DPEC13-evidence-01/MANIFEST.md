# PEC D-PEC-13 evidence 01 — the `tracker` contract, live proposal-path evidence (synthetic + real)

> **Epistemic status: immutable evidence snapshot** (D-T0-13 capture
> convention). Facts only; no pilot-readiness, correctness, go-live, or
> WF-5-discharge claim is made by this pack itself (F-PEC-2) — discharge
> accounting belongs to the receipt. Imported stage values are plain imported
> fields, not lifecycle assertions. Part 2 is scratch-basis evidence on the
> owner's designated standing pilot-scratch instance — no real-record
> durability claim.

## Basis (authority chain, each verified in the live tree before acting)

- **Ruling:** D-PEC-13 O-A, owner-ruled 2026-07-06 (packet
  `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-13_package_tracker_import_contract.md`,
  Human-ruling section, verbatim: "Proceed with 1. Rule D-PEC-13 as follows.
  Use the tracker.xlsx provided as your template and proceed accordingly.").
  The two recorded in-packet defaults stand and bind this pack: (1) NO profile
  edit; (2) **capture limits (item-4 default): manifests/hashes-only grain for
  all tracker.xlsx-derived captures** — committed evidence uses synthetic
  fixtures; the real-run capture is count-level + hashes.
- **Evidence bar:** `projects/pec/execution/_Coordination/TRANCHE_2026-07-06_D-PEC-13_tracker_contract_v1.md`
  §"Evidence bar" — followed exactly (both parts below).
- **Visibility basis:** D-T0-20 O-B — tracker.xlsx is owner-dropped weekly
  file, enumeration item (iv); proposal records/reports item (ii); the
  pilot-scratch instance is owner-clarified inside the scratch/demo mutation
  basis.
- **Code under test:** branch `codex/pec-dpec13-tracker`, verified at run
  start at `b134e273c` (the shipped `tracker` contract —
  `server/src/import/index.ts` importTracker/export case,
  `services/proposals.ts` six-contract allowlist,
  `GET /api/projects/:pid/tracker` view route). During the run the branch
  advanced to `4bc1580be` (see Deltas item 5 — test + mapping-doc commit only;
  `git diff b134e273c..4bc1580be -- server/src core/src` is empty, so the
  executed server source is identical at both SHAs). No tracked file was
  edited by this capture; every file in this pack and the one proposals-mirror
  file are new.
- **Precedent forms:** `PEC_2026-07-05_L3-evidence-01/` (proposal-lifecycle
  pack), `PEC_2026-07-06_DPEC10-triage-01/` (standing-instance run: backups,
  basis-prep, read-path and teardown conventions),
  `PEC_2026-07-06_BRIDGE-evidence-01/` (per-act demo-cast disclosure table).

## Actors (WF-8 split, both parts)

| Part | Agent (propose / export / view) | Demo-cast admin (accept / apply ONLY) |
|---|---|---|
| 1 (synthetic scratch) | `pec-agent@rehearsal.demo`, personId 16, `is_admin=0`, coordinator — provisioned script-side (basis prep) | `admin@aurora.dev`, personId 15 — the seed cast's admin, disclosed per act |
| 2 (pilot-scratch standing) | `pec-agent@rehearsal.demo`, personId 46, `is_admin=0`, coordinator — reused from the triage run; fresh ephemeral credential script-side | `pec-demo-admin@rehearsal.demo`, personId 47, `is_admin=0`, project-role `admin` — provisioned script-side (this instance has no seeded demo admin; the owner's credential was never touched or used), disclosed per act |

All workflow acts ran through the live HTTP API on `127.0.0.1:4899` with
session auth — nothing bypassed RBAC. `is_admin` was never an acting basis
(both provisioned persons carry `is_admin=0`; the accept/apply basis is the
project admin ROLE). **`force` was never true anywhere** — the drivers
hard-code `force: false` with no override parameter. No LLM sidecar: direct
API, the rehearsal-01 mechanism; no LLM key sourced or fabricated.

## Demo-cast accept/apply disclosure (Receipt 34/35 convention; one line per act)

- Part 1, IPR-0001 accept — demo-cast as `admin@aurora.dev`; version + source-SHA-256 echo; no force parameter on accept.
- Part 1, IPR-0001 apply — demo-cast as `admin@aurora.dev`; **force: false**; applied.
- Part 1, IPR-0002 accept — demo-cast as `admin@aurora.dev`; version + source-SHA-256 echo.
- Part 1, IPR-0002 apply — demo-cast as `admin@aurora.dev`; **force: false**; applied.
- Part 2, IPR-0001 accept — demo-cast as `pec-demo-admin@rehearsal.demo`; version + source-SHA-256 echo.
- Part 2, IPR-0001 apply — demo-cast as `pec-demo-admin@rehearsal.demo`; **force: false**; applied.

## Part 1 — synthetic evidence (fresh scratch DB, committed verbatim)

Instance: fresh scratch DB seeded by the D-PEC-06-guarded `npm run seed`
(PEC_DB at a scratch-token path in the session scratchpad), served on `:4899`;
**deleted after capture** (+wal/shm). Basis prep script-side: agent person
provisioned; the seed cast provided the demo admin and the anchor package
target `PKG-P` (no extra record creation needed); `PKG-NOPE` verified absent
(`artifacts/part1/00a-basis-prep.json`).

| Step | Act | Result |
|---|---|---|
| 1 | Agent proposed `tracker-syn-v1.csv` (6 data rows: 4 clean incl. one resolving `package` anchor; 1 stated-but-unresolvable anchor; 1 within-file duplicate key) → IPR-0001 | dry-run: **4 create, 0 update, 1 conflict (duplicate tracking_no in file), 1 rejected (anchor matches no package code), 0 to intake** |
| 2 | Demo-cast accept + apply (force: false) | applied; **apply report identical to dry-run** (deterministic preview held) |
| 3 | Agent proposed edited `tracker-syn-v2.csv` (the 4 applied rows; stage-value changes on all 4 + one field change: `vendor_awarded` populated) → IPR-0002 | dry-run: **0 create, 4 update-in-place, 0 conflicts, 0 rejected, 0 to intake** — no duplication |
| 4 | Demo-cast accept + apply (force: false) | applied; apply report identical to dry-run |
| 5 | Agent fetched `GET /export/tracker.csv`; column-for-column compare vs applied v2 (D-PEC-12 §5), keyed on tracking_no, all 25 columns | **pass: header match, 4/4 rows, 0 mismatches** (`artifacts/part1/09-roundtrip-compare.json`) |
| 6 | Register view `GET /tracker` as the agent | 4 rows |

Source hashes: v1 `cf78131addd7254e96573600d9e9653698b99692e815ba511eab53ef3cf8388f`,
v2 `56337a6eb88c00b74f1ca222cadf067c19e66f06d6799b5df023ba89ec8e3647` (both
committed under `inputs/` — synthetic, fictional content only).

## Part 2 — the real tracker.xlsx run (pilot-scratch standing instance; CAPTURE-LIMITED)

Committed at the ruled grain: **counts + hashes only. No verbatim real rows,
package names, vendor names, or the duplicate key literal appear in any
committed artifact** (see the compliance check below). Raw payloads live
untracked at `pilot-scratch/derived/dpec13-tracker-run-20260706/`, referenced
by hash in `artifacts/part2/01-run-counts.json`.

| Step | Act | Result (count-level) |
|---|---|---|
| 1 | Preflight: `:4899` free; owner dev server on `:4811` live, untouched; no process held the standing DB | pre-run backup (byte-identical, cmp-verified) → `pilot-scratch/backups/pre-tracker-20260706/`, SHA-256 `94dc7a47206e22ac214a4835474aa28d980a10372718ab8f1e87126feff88ab9` (= the triage run's post-run hash: unchanged since) |
| 2 | Agent-side mapping (IMPORT_MAPPING §tracker) from `tracker.xlsx` (SHA-256 `01fc38f085dc8218c0e006d8a27c8ad7fa157c964ffe4041a7599ebc54f6bf9e` — matches the ruled packet) + `mdl.xlsx` unique-name resolution → `pilot-scratch/import-ready/tracker.csv` (untracked owner surface; SHA-256 `da6fadb1f9611fde4082355229e39b24cf59c43c9ac9fa3716cd99c21a521698`) | 65 rows / 25 columns; 64 distinct keys (the one duplicate pair = workbook sheet rows 16/54); anchors resolved 54/65 unique, 11 unmatched, 0 ambiguous; all 54 resolved codes pre-verified present in the standing DB |
| 3 | Agent proposed `contract=tracker` → IPR-0001 (this instance's first proposal) | dry-run: **64 create, 0 update, 1 conflict (the duplicated tracking-number value, workbook rows 16/54 — reported, never applied, never silent), 0 rejected, 0 to intake** — the ruled expectation exactly |
| 4 | Demo-cast accept + apply (force: false) | applied; **apply report identical to dry-run** |
| 5 | Register view as the agent | **64 rows; 53 with a resolved package link** (see Deltas: the 54th authored anchor sat on the skipped duplicate occurrence) |
| 6 | Export round-trip fetch as the agent (NOT committed) | SHA-256 `82a78424962d56d04fa4ca15f18bbea68fc17b9ed048b93ad852ae186e718e79`; 64 rows / 25 columns |
| 7 | Logout; script-side teardown (credentials disabled; 0 session rows); clean server stop; post-run backup → `pilot-scratch/backups/post-tracker-20260706/`, SHA-256 `b2780788a36c40659b27e0ed39be60c4af7d8c63efa171b97b398c0f78ffd2ed` | standing DB **retained** (owner-designated standing instance) |

Standing state undisturbed: intake items 272 → 272; dispositioned 257 → 257
(the D-PEC-10 triage dispositions untouched).

## Deltas found (live tree wins, recorded; nothing improvised)

1. **Anchor count achieved is 53/64 applied rows, not 54:** the authored CSV
   carries 54 resolved anchors, but both occurrences of the duplicated
   tracking-number value carry one — the second occurrence is skipped as the
   duplicate conflict, so its anchor never lands. 53 = 54 − 1, fully
   reconciled; no resolution failure occurred (0 anchor rejects; the
   54/54 pre-check held).
2. **The tasking's "admin@aurora.dev usable as demo-cast admin" holds for
   Part 1 only:** the standing pilot-scratch instance has no seeded demo cast
   (already recorded as a delta by the triage-01 pack), so Part 2's demo-cast
   admin was provisioned script-side, disclosed, `is_admin=0`, and disabled
   after.
3. **Schema auto-migration disclosed:** the standing DB gained exactly one
   table, `package_tracker` (sqlite_master diff pre vs post). The migration
   ran at the script-side basis-prep `openDb`, before server start; the
   pre-run backup preserves the pre-migration schema.
4. At session start the owner's live dev server (`:4811`) held
   `pec-demo.db-wal/-shm` with working-tree modifications — observed state
   only; never touched by this run.
5. **The branch advanced mid-run** (another session's commit, 2026-07-06
   11:05 local): `b134e273c` → `4bc1580be`, "D-PEC-13 verification follow-up —
   optional-header preservation + duplicate-vs-validation precedence
   documented and test-pinned". It touches only
   `server/test/import-tracker.test.ts` and
   `IMPORT_TEMPLATES/IMPORT_MAPPING.md`; the `server/src` + `core/src` diff
   between the two SHAs is empty, so every act in this pack executed
   byte-identical server code. Recorded, not improvised around.

## Disclosures / boundaries respected

- Scratch/demo mutation basis only. Part 1's fresh scratch DB (+wal/shm)
  **deleted after capture**; Part 2's standing DB **retained** with pre/post
  byte-identical backups (hashes above). The owner's `:4811` server,
  `pec-demo.db*`, `pec.db*`, and the restore DBs were never touched.
- **Ephemeral credential lifecycle:** all credentials generated at run time
  (`openssl rand`), held only in the session scratchpad, never committed;
  Part 1's died with the deleted DB; Part 2's two hashes overwritten
  non-verifiable at teardown (0 session rows remained); the secret files were
  deleted. Person rows remain for history attribution (triage-01 precedent).
- **Read path (disclosed):** the anchor pre-check ran read-only sqlite against
  a byte-identical scratchpad copy of the pre-run backup (never the live DB;
  deleted after use) — the triage-01 read-path convention; content classes
  read sit inside the D-T0-20 O-B enumeration on the scratch basis.
- No pec source change; no tracked-file edit; no git commit/branch/push by
  this capture; no tier-0 act; no register/receipt/packet/profile write; no
  external egress.
- **Capture-limit compliance (ruled item-4 default), checked mechanically:**
  every distinct real cell value and `;`-joined fragment (length ≥ 4,
  closed-vocabulary tokens excluded) from the authored real CSV — 357
  needles — was searched case-insensitively against every committed file of
  all committed files — this pack including MANIFEST and SHA256SUMS, plus the proposals mirror (23 files): **0 hits** (independently re-swept at verification with 328 needles, 0 hits). The duplicate
  key is referred to only as "the duplicated tracking-number value (workbook
  rows 16/54)".

## Artifacts

- `inputs/tracker-syn-v1.csv`, `inputs/tracker-syn-v2.csv` — the synthetic
  fixtures (fictional content only).
- `artifacts/part1/00-agent-login.json` … `11-server-log.txt` — the full
  Part 1 lifecycle verbatim (propose / demo-cast accept / demo-cast apply ×2,
  dry-run-vs-apply check, export, round-trip compare, register view,
  basis-prep record, server log).
- `artifacts/part2/00-basis-prep.json`, `01-run-counts.json`,
  `02-mapping-counts.json`, `03-backups-and-schema.json`,
  `04-server-log.txt` — Part 2 at the ruled count-level + hash grain.
- Mirror artifact (non-authoritative, batch form disclosed):
  `_DomainEngines/proposals/pec/OP_2026-07-06_DPEC13_evidence_IPR-0001-0002.md`.
- `SHA256SUMS` — SHA-256 over every committed artifact in this pack.
