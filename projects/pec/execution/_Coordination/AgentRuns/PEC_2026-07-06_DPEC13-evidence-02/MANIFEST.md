# PEC D-PEC-13 evidence 02 — the AMENDED package-keyed `tracker` contract, live proposal-path evidence (synthetic + real)

> **Epistemic status: immutable evidence snapshot** (D-T0-13 capture
> convention). Facts only; no pilot-readiness, correctness, go-live, or
> WF-5-discharge claim is made by this pack itself (F-PEC-2) — discharge
> accounting belongs to the receipt. Imported stage values are plain imported
> fields, not lifecycle assertions. Part 2 is scratch-basis evidence on the
> owner's designated standing pilot-scratch instance — no real-record
> durability claim.
>
> **Relation to evidence-01:** `PEC_2026-07-06_DPEC13-evidence-01/` remains
> the honest record of the PRE-amendment run (tracking_no-keyed contract);
> **this pack supersedes its results for the shipped contract** — the owner
> amendment below governs, and the code at this pack's SHA carries the
> amended semantics.

## Basis (authority chain, each verified in the live tree before acting)

- **Ruling:** D-PEC-13 O-A, owner-ruled 2026-07-06 (packet
  `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-13_package_tracker_import_contract.md`,
  Human-ruling section, verbatim: "Proceed with 1. Rule D-PEC-13 as follows.
  Use the tracker.xlsx provided as your template and proceed accordingly.").
- **OWNER AMENDMENT (2026-07-06, in-session, Ryan Tufts, verbatim — governs
  over the packet's prose per its amendment clause; recorded in the packet's
  Human-ruling section):**

  > You should match the tracker entries with the PKG-#### numbers we're using.
  > Keep the CoA number but don't key on that.

  Recorded interpretation (in the packet): the idempotency key moves from
  `tracking_no` (the CoA number) to the resolved `package.code`; `package` is
  row-required and must resolve (`UNIQUE(project_id, package_id)`); the CoA
  number is retained verbatim as plain optional non-unique data, never a
  conflict source; the duplicated CoA value (workbook rows 16/54) stops being
  an import defect — both rows key on their distinct packages and both land;
  unresolvable rows reject as owner-side data gaps (NO intake fallback);
  within-file duplicate semantics move to the package key.
- **Capture default (ruled item-4, unchanged by the amendment):**
  manifests/hashes-only grain for all tracker.xlsx-derived captures —
  committed evidence uses synthetic fixtures; the real-run capture is
  count-level + hashes + row coordinates.
- **Mapping of record:** `IMPORT_TEMPLATES/IMPORT_MAPPING.md` §tracker as
  amended 2026-07-06 (package = the key; tracking_no = plain data).
- **Evidence bar:** the ruled packet's evidence convention (v1 + edited v2
  through the live proposal seam; duplicate-key conflict; anchor rejection;
  export round-trip; governance mirror; demo-cast disclosure; SHA-256
  manifest; scratch DB deleted), re-run under the amended semantics.
- **Visibility basis:** D-T0-20 O-B — tracker.xlsx is owner-dropped weekly
  file, enumeration item (iv); proposal records/reports item (ii); the
  pilot-scratch instance is owner-clarified inside the scratch/demo mutation
  basis.
- **Code under test:** branch `codex/pec-dpec13-tracker`, verified at run
  start AND run end at `9d086d783` ("D-PEC-13 owner amendment — tracker keyed
  on package (PKG-####); CoA number kept as plain data; old-shape scratch
  rebuild migration; 14 tests"): `importTracker` package-keyed
  (`server/src/import/index.ts:493-583`), `UNIQUE(project_id, package_id)`
  DDL + the old-shape rebuild migration (`server/src/db.ts` PACKAGE_TRACKER_DDL
  + openDb), six-contract allowlist (`services/proposals.ts:22`). No tracked
  file was edited by this capture; every file in this pack and the one
  proposals-mirror file are new.
- **Precedent form:** `PEC_2026-07-06_DPEC13-evidence-01/` (this pack follows
  its structure file-for-file, with `07a` and part2 `04-migration-evidence`
  added).

## Actors (WF-8 split, both parts)

| Part | Agent (propose / export / view) | Demo-cast admin (accept / apply ONLY) |
|---|---|---|
| 1 (synthetic scratch) | `pec-agent@rehearsal.demo`, personId 16, `is_admin=0`, coordinator — provisioned script-side (basis prep) | `admin@aurora.dev`, personId 15 — the seed cast's admin, disclosed per act |
| 2 (pilot-scratch standing) | `pec-agent@rehearsal.demo`, personId 46, `is_admin=0`, coordinator — reused person row (evidence-01/triage lineage); fresh ephemeral credential script-side | `pec-demo-admin@rehearsal.demo`, personId 47, `is_admin=0`, project-role `admin` — person row reused from evidence-01 (not recreated); fresh ephemeral credential script-side; disclosed per act |

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
- Part 2, IPR-0002 accept — demo-cast as `pec-demo-admin@rehearsal.demo`; version + source-SHA-256 echo.
- Part 2, IPR-0002 apply — demo-cast as `pec-demo-admin@rehearsal.demo`; **force: false**; applied.

## Part 1 — synthetic evidence (fresh scratch DB, committed verbatim)

Instance: fresh scratch DB seeded by the D-PEC-06-guarded `npm run seed`
(PEC_DB at a scratch-token path in the session scratchpad), served on `:4899`;
**deleted after capture** (+wal/shm). Basis prep script-side: agent person
provisioned; the seed cast provided the demo admin and FOUR distinct anchor
package targets (`PKG-P`, `PKG-M`, `PKG-PI`, `PKG-EI` — the amended key needs
several); `PKG-NOPE` verified absent; the fresh DB's base schema already
carries the amended shape (`package_id NOT NULL` — nothing to migrate;
`artifacts/part1/00a-basis-prep.json`).

| Step | Act | Result |
|---|---|---|
| 1 | Agent proposed `tracker-syn-v1.csv` (6 data rows: (a) one duplicate PACKAGE-key pair on `PKG-P`; (b) one unresolvable package key; (c) two rows sharing ONE CoA tracking number on DIFFERENT packages; plus a clean row) → IPR-0001 | dry-run: **4 create, 0 update, 1 conflict (row 5, key `PKG-P`: "duplicate package in file; first occurrence applied, this one skipped"), 1 rejected (row 6: `package "PKG-NOPE" matches no package code`), 0 to intake** |
| 2 | Demo-cast accept + apply (force: false) | applied; **apply report identical to dry-run** (deterministic preview held) |
| 3 | Register view after v1 | **4 rows, all 4 anchored; the two rows sharing CoA value `99999-01-PT-01-777` BOTH landed on their distinct packages (`PKG-M`, `PKG-PI`) — the amendment's direct consequence, exercised synthetically** |
| 4 | Agent proposed edited `tracker-syn-v2.csv` (the 4 applied package keys; stage-value changes on all 4 + `vendor_awarded` populated on one + **the CoA number RENUMBERED on the `PKG-EI` row (`…-004` → `…-104`)**) → IPR-0002 | dry-run: **0 create, 4 update-in-place on the package key, 0 conflicts, 0 rejected, 0 to intake** — no duplication; the renumbered CoA updated as plain data |
| 5 | Demo-cast accept + apply (force: false) | applied; apply report identical to dry-run (`07a-v2-dryrun-vs-apply.json`) |
| 6 | Agent fetched `GET /export/tracker.csv`; column-for-column compare vs applied v2 (D-PEC-12 §5), keyed on the AMENDED key `package`, all 25 columns | **pass: header match, 4/4 rows, 0 mismatches** (`artifacts/part1/09-roundtrip-compare.json`) |

Source hashes: v1 `60ba85491dfa2e95442f74990176c9cda637388c53945bafa08425cde7917358`,
v2 `dd2bcbaa8697a093cf83b15ea37d23e28399705e89a8a4c8abd040e07e22aa91` (both
committed under `inputs/` — synthetic, fictional content only; CoA-shaped
values use a fictional `99999-` prefix that cannot collide with real values).

## Part 2 — the real tracker.xlsx run (pilot-scratch standing instance; CAPTURE-LIMITED)

Committed at the ruled grain: **counts + hashes + row coordinates only. No
verbatim real rows, package names, package codes, vendor names, or tracking
numbers appear in any committed artifact** (see the compliance check below).
Raw payloads live untracked at
`pilot-scratch/derived/dpec13-tracker2-run-20260706/`, referenced by hash in
`artifacts/part2/01-run-counts.json`.

| Step | Act | Result (count-level) |
|---|---|---|
| 1 | Preflight: `:4899` free; owner dev server on `:4811` live, untouched; no process held the standing DB; no wal/shm | pre-run backup (byte-identical, cmp-verified) → `pilot-scratch/backups/pre-tracker2-20260706/`, SHA-256 `b2780788a36c40659b27e0ed39be60c4af7d8c63efa171b97b398c0f78ffd2ed` (= evidence-01's post-run hash: unchanged since) |
| 2 | Script-side basis prep (server down): fresh ephemeral credentials for personId 46/47; **the shipped old-shape rebuild migration fired at this openDb** — `package_tracker` (64 old-shape rows, keyed on tracking_no) dropped and recreated EMPTY at the amended shape | before/after schema evidence from backup copies, read-only: `artifacts/part2/04-migration-evidence.json` |
| 3 | Agent-side mapping (IMPORT_MAPPING §tracker AS AMENDED) from `tracker.xlsx` (SHA-256 `01fc38f085dc8218c0e006d8a27c8ad7fa157c964ffe4041a7599ebc54f6bf9e` — matches the ruled packet) + `mdl.xlsx` unique-name resolution → `pilot-scratch/import-ready/tracker.csv` re-authored (untracked owner surface; SHA-256 `da6fadb1f9611fde4082355229e39b24cf59c43c9ac9fa3716cd99c21a521698` — **byte-identical to the evidence-01 CSV**, see Deltas item 1) | 65 rows / 25 columns; package key resolved 54/65 unique, 11 unmatched (kept in the CSV with a blank key so the CONTRACT rejects them), 0 ambiguous, **0 resolved-code collisions across workbook rows**; all 54 resolved codes pre-verified present in the standing DB; both duplicated-CoA rows (workbook 16/54) carry resolved, DISTINCT package keys |
| 4 | Agent proposed `contract=tracker` → IPR-0002 (this instance's second proposal) | dry-run: **54 create, 0 update, 0 conflicts, 11 rejected (all errors read exactly `package is required` — owner-side data gaps at workbook sheet rows 6, 17, 57, 58, 59, 60, 61, 62, 63, 64, 65), 0 to intake** — the amended expectation exactly |
| 5 | Demo-cast accept + apply (force: false) | applied; **apply report identical to dry-run** |
| 6 | Register view as the agent | **54 rows; anchored = 54 = ALL (packageId NOT NULL by construction under the amended key). The amendment's proof: exactly one CoA value is shared by 2 register rows, on 2 DISTINCT packages, both anchored — the workbook rows 16/54 pair, both landed** |
| 7 | Export round-trip fetch as the agent (NOT committed) | SHA-256 `2cc75f74d5e9f0e616095b0f3a8dcacf0a93c1cb79d38d245eaeadd5b3f77c9b`; 54 rows / 25 columns |
| 8 | Logout; script-side teardown (credentials disabled; 0 session rows); clean server stop; WAL checkpointed; post-run backup → `pilot-scratch/backups/post-tracker2-20260706/`, SHA-256 `776f98ae23600fc85e6046a1df08e4641c40c555eacb4e52fb904693ab6e1cce` | standing DB **retained** (owner-designated standing instance) |

Standing state undisturbed: intake items 272 → 272; dispositioned 257 → 257;
raised 15 → 15 (the D-PEC-10 triage dispositions untouched).

## Migration-fired evidence (the shipped openDb rebuild)

Captured read-only from backup copies (`artifacts/part2/04-migration-evidence.json`):

| | Before (pre-run backup) | After (post-run backup) |
|---|---|---|
| Key columns | `tracking_no NOT NULL` (the key), `package_id` nullable | `tracking_no` nullable (plain data), `package_id NOT NULL` (the key) |
| Unique constraint | `UNIQUE(project_id, tracking_no)` | `UNIQUE(project_id, package_id)` |
| Rows | 64 (evidence-01's pre-amendment import) | 0 at rebuild → 54 after this run's apply |

The rebuild dropped 64 import-owned, reproducible register rows (the shipped
migration's stated scratch-only basis); this run's re-import repopulated the
register from the same owner workbook under the amended key.

## Deltas found (live tree wins, recorded; nothing improvised)

1. **The re-authored real CSV is byte-identical to evidence-01's** (same
   SHA-256 `da6fadb1…`): the evidence-01 mapping already carried all 25
   columns with `package` populated where uniquely resolvable — the owner
   amendment changed the SERVER-side key semantics, not the authoring-side
   mapping, so an honest re-derivation from the workbooks reproduced the same
   bytes. Consequence: the same source file that produced
   64-create/1-conflict/0-reject under the old key produces
   54-create/0-conflict/11-reject under the amended key — the semantic change
   is entirely in the shipped contract, cleanly isolated by the evidence pair.
2. **The Part-2 demo-cast admin person already existed** (personId 47,
   provisioned by evidence-01): reused with a fresh ephemeral credential
   rather than recreated — the evidence-01 basis-prep script would have
   refused; the e2 script expects and verifies the existing row instead.
3. **Evidence-01's one-anchor-short delta is resolved by the amendment:**
   evidence-01 recorded 53/64 anchored (the second duplicate-CoA occurrence
   was skipped, its anchor never landed). Under the amended key both rows
   land and anchored = ALL (54/54) — recorded here as the amendment doing
   exactly what its recorded interpretation stated, not as a new surprise.
4. The branch did NOT advance during this run (`9d086d783` at start and end)
   — noted because evidence-01 had to record a mid-run advance.
5. At session start the owner's live dev server (`:4811`) held
   `pec-demo.db-wal/-shm` with working-tree modifications — observed state
   only; never touched by this run.

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
- **Read path (disclosed):** the package-code pre-check and the migration
  before/after captures ran read-only sqlite against byte-identical
  scratchpad copies of the pre-run and post-run backups (never the live DB;
  deleted after use) — the triage-01 read-path convention; content classes
  read sit inside the D-T0-20 O-B enumeration on the scratch basis.
- **Migration side-effect disclosed, not improvised:** the old-shape rebuild
  is the shipped `openDb` behavior at this pack's SHA; it fired at the
  script-side basis-prep open (first open with the amended code), before
  server start; the pre-run backup preserves the pre-migration state.
- No pec source change; no tracked-file edit; no git commit/branch/push by
  this capture; no tier-0 act; no register/receipt/packet/profile write; no
  external egress.
- **Capture-limit compliance (ruled item-4 default), checked mechanically:**
  every distinct real cell value and `;`-joined fragment (length ≥ 4,
  closed-vocabulary tokens excluded) from the authored real CSV — **357
  needles** — was searched case-insensitively against every committed file of
  this pack (MANIFEST and SHA256SUMS included) plus the proposals mirror
  (25 files): **0 hits**. The duplicated CoA value is referred to only as
  "the duplicated tracking-number value (workbook rows 16/54)"; the 11
  data-gap rows only by their workbook sheet-row coordinates.

## Artifacts

- `inputs/tracker-syn-v1.csv`, `inputs/tracker-syn-v2.csv` — the synthetic
  fixtures (fictional content only; `99999-` CoA prefix).
- `artifacts/part1/00-agent-login.json` … `11-server-log.txt` — the full
  Part 1 lifecycle verbatim (propose / demo-cast accept / demo-cast apply ×2,
  dry-run-vs-apply checks for BOTH proposals, export, round-trip compare,
  register view, basis-prep record, server log).
- `artifacts/part2/00-basis-prep.json`, `01-run-counts.json`,
  `02-mapping-counts.json`, `03-backups-and-schema.json`,
  `04-migration-evidence.json`, `05-server-log.txt` — Part 2 at the ruled
  count-level + hash + row-coordinate grain.
- Mirror artifact (non-authoritative, batch form disclosed):
  `_DomainEngines/proposals/pec/OP_2026-07-06_DPEC13_evidence02_IPR-0001-0002.md`.
- `SHA256SUMS` — SHA-256 over every committed artifact in this pack.
