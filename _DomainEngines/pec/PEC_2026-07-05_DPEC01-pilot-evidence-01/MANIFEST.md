# D-PEC-01 Pilot Evidence 01 — MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence — not authority.** First real-data
> rehearsal capture under the D-PEC-01 O-A ruling and the owner-supplied
> execution basis (2026-07-05). Captured outputs are derivative packages, not
> substitute authority; pec's tests and source govern. Immutable after
> publication — corrections go in a new dated snapshot.

## What this proves

The real pilot workbooks were shaken down against the §16 import contracts
end-to-end: SHA-256 anchored inputs, verbatim CSV conversion, the as-is
pilot-drill and authenticated API import results (all four contracts reject at
the required-column check — the workbooks are raw client artifacts, not
contract-shaped exports), a per-contract column-gap analysis, and the scratch
backup→restore rehearsal over the owner-supplied paths. The §16 export
round-trip also produced the exact contract-shaped CSV template the pilot team
needs to target.

## Identity

| Field | Value |
|---|---|
| Evidence package | `PEC_2026-07-05_DPEC01-pilot-evidence-01` |
| Git SHA at run start | `4477c8554` (branch base `59d1e4c7c` = `origin/main`) |
| Branch | `codex/pec-dpec01-pilot-evidence` (stacked on `codex/pec-receipt16-dpec01-basis-gate`) |
| Governing decision | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-01_pilot_rehearsal_real_data_authorization.md` (RULED O-A 2026-07-05) |
| Related gates | D-PEC-04 Gate 2 deferred; D-PEC-05 L3 deferred; `force=true` separate ruling required |
| Operator | PEC work loop agent; basis supplied in-session by owner (Ryan Tufts) |
| Date/time | 2026-07-05 (America/Edmonton) |

## Owner-Supplied Basis

Recorded verbatim in
`../PEC_2026-07-05_DPEC01-execution-basis/OWNER_INPUTS.md` (filled 2026-07-05),
including the raw-content ruling: "I'm okay with the agents reading the raw
files … I'm controlling the data appropriately." Real backup artifact: OUT OF
SCOPE this run (no real pilot DB exists yet); the real restore rehearsal
(PILOT.md §5) becomes its own later evidence run.

## Input File Hashes (all under `projects/pec/pilot-scratch/input/`, uncommitted/gitignored)

| Input | File | SHA-256 | Size | Notes |
|---|---|---|---|---|
| MDL | `mdl.xlsx` | `bf73c03f5f753652c7d0e62086dedbbcc6f6642de29b32976e814efc7860db74` | 47,373 B | sheet "Master Deliverables List", 458 data rows |
| RAIL | `rail.xlsx` | `545655199557527fc2d41b938bfec173ec70bd3e00f6caff817d69db37c33e84` | 88,614 B | sheet "RAIL", 338 rows incl. banner block |
| Decisions | `decisions.xlsx` | `426055769ad1be1ac0a2b363ffa5150888da6394b6d492f00dae77a1ef871d85` | 22,525 B | sheet "Sheet1", 62 data rows |
| Risks | `risk.xlsx` | `b6b1ea0ef6b4a4ed44132e13ae1727032dcddae02d2b174115b5272914d92125` | 43,582 B | **delta:** owner basis says `risks.xlsx`; live file is `risk.xlsx` |
| Schedule | `schedule.pdf` | `ca3cbfb7f32820f0e2534c82abc84e0fbb2040635b1082c69039f2067c51bf7e` | 224,601 B | PDF — not importable verbatim; §16 schedule contract is CSV/XER-derived (D-04) |

Verbatim CSV conversions (openpyxl 3.1.5, first sheet, `str()` cell rendering,
dates ISO; under `projects/pec/pilot-scratch/derived/`, uncommitted):

| Derived CSV | SHA-256 |
|---|---|
| `mdl-verbatim.csv` | `c0938c3e5131971e133dff904bbbf9cfd8b3d2246e8c39e870c98e234e40ef11` |
| `rail-verbatim.csv` | `2dc983051772f440a09457b5e1af12f33fe83731e07d421fa1a51176a60caae9` |
| `decisions-verbatim.csv` | `d485285c01b00afb92fff5b77dd0f1e17aa611d95e40ff8092fb39bd5bbd0034` |
| `risks-verbatim.csv` | `257b2d1e0fff4cfc220d5cad9388ef36c516d095e4dd0315ff9440ef56837ea9` |

## Commands

| Step | Command summary | Environment | Exit | Artifact |
|---|---|---|---|---|
| Hash inputs | `shasum -a 256 input/*` | n/a | 0 | tables above |
| Convert | openpyxl verbatim xlsx→csv + gap analysis | scratch only | 0 | `column-gap-analysis.json` |
| Drill (as-is) | `node tools/pilot-drill.ts --mdl/--rail/--decisions/--risks <verbatim CSVs>` | drill's own OS-temp scratch DB (removed after) | 1 | `pilot-drill-asis.log` |
| Bootstrap | actor+project insert via server repo (drill pattern) | scratch import `PEC_DB` | 0 | noted below |
| API rehearsal | server `:4899` on scratch import DB; login; `POST /api/projects/1/import/:contract`; export; logout | scratch import `PEC_DB` | 200/400s | `api/` |
| Backup | `tools/backup.ts backup` | scratch import `PEC_DB`, `PEC_BACKUP_DIR=pilot-scratch/backups/` | 0 | `backup-restore.log` |
| Restore | `tools/backup.ts restore <backup>` | scratch restore `PEC_DB` | 0 | `backup-restore.log` |

## Import Results (as-is, both seams)

All four contracts reject at the required-column check before any row is
processed — via the drill (throws on MDL, exit 1) and per-contract over the
authenticated API (HTTP 400 each, `api/import_*_asis.json`):

| Contract | §16 required columns missing (as-is) | Detected real header row | Required columns present in real header |
|---|---|---|---|
| MDL | all 8 (`doc_no, title, package, discipline, owner, current_rev, state, due_date`) | row 2 | `discipline` only |
| RAIL | all 9 (`item_id, statement, type, log, owner, need_by, status, raised_by, raised_date`) | row 7 | `status` only |
| Decisions | 5 (`decision_id, title, statement, authority, need_by`) | row 1 | `status` only |
| Risks | all 6 (`risk_id, title, cause, consequence, owner, status`) | row 10 | none (row 10 is still legend-adjacent; sheet mixes legend + log) |

Full detail per contract (detected headers, present/missing lists, row
counts): `column-gap-analysis.json`.

## Restore Results

| Check | Value |
|---|---|
| Backup written | `pilot-scratch/backups/pec-20260705-154636.db` (340.0 KiB), exit 0, WAL-safe VACUUM INTO |
| Backup SHA-256 | `03928fb7c932d0eab13ac2e343d6e4378c4fbdd672ca03b0675a2d427262a11f` |
| Scratch restore target | `pilot-scratch/db/pec-scratch-restore.db` — restored, exit 0 |
| Restored SHA-256 | identical to backup (`03928fb7…`) |
| Pre-restore scratch DB preserved aside | yes (`pec-scratch-restore.db.pre-restore`) |
| Real pilot DB mutated | No — none exists; only `pilot-scratch/db/*` touched |

## Captured Derivative Artifacts (committed, owner-permitted unredacted)

| Artifact | SHA-256 | Raw real content? |
|---|---|---|
| `column-gap-analysis.json` | `63246c437220ae42902391518bdea38d7b2fc4324cae50886f9e2f073ed375cf` | header names + counts only |
| `pilot-drill-asis.log` | `211e46e222d777c7e4231814fcb829269b6cac15a7134c34dbb449bbffc2b508` | no (error path before rows) |
| `backup-restore.log` | `65fefadf33d09b052d4aab3c2b637edecd4b25cf9af36999c791594e3654b548` | no |
| `api/login.json`, `api/auth_me.json` | `b2d3537182…`, `3cac1a5232…` | no (session body; cookie jar not committed, destroyed) |
| `api/import_{mdl,rail,decisions,risks}_asis.json` | `27ac8e66dd…`, `261390f15d…`, `1e49a4021f…`, `411823a89d…` | error payloads only |
| `api/exports/mdl.csv` | `1fd11a5ea6fa0d218ada9f64a39cb35fa6d83e1eb3145adcf2815c586db01c6c` | no — empty §16 export = the contract-shaped template |

## Deltas found (live tree wins; also in OWNER_INPUTS.md and Receipt 17)

- Basis `risks.xlsx` → live `risk.xlsx` (hash-anchored above).
- `pilot-drill.ts` always creates its own OS-temp scratch DB; the
  owner-supplied scratch import `PEC_DB` was exercised via the API-mode
  rehearsal + backup/restore instead.
- A second PEC server (owner dev, `--watch src/index.ts`) was live on `:4811`
  during the run; the capture server used `:4899` and `127.0.0.1` explicitly.
  Nothing was sent to the owner server beyond four unauthenticated requests
  that returned 401 before the collision was noticed.
- Actor `ryan@chirality.ai` did not exist in any scratch DB; it was
  bootstrapped (instance admin + project role `admin`, full visibility per the
  basis) with an ephemeral throwaway password, destroyed with the cookie jar
  after capture.

## Limitations

- No `force=true` was used.
- No raw real input file or DB file was committed; committed artifacts are
  listed above and contain at most header names, counts, and error payloads.
- No Gate 2 adoption; no L3 design/execution; no pilot-readiness or go-live
  claim; no professional approval, check acceptance, decision outcome,
  revision issue, waiver judgment, or other reserved PEC human act.
- The real-data **row-level** import rehearsal has not happened yet: the
  workbooks are not §16 contract-shaped, and mapping their columns to the
  contract (e.g. what is `owner`, `current_rev` for MDL) is pilot-team /
  owner judgment, not an agent act. It proceeds when the owner supplies
  contract-shaped exports (the `api/exports/mdl.csv` template shows the
  target) or rules a column mapping.

## Gate Outcome

D-PEC-01 rehearsal executed to the honest boundary: inputs hash-anchored,
as-is shakedown captured on both seams, column gap quantified, owner-supplied
scratch backup/restore paths proven. Parked: contract-shaped exports or a
mapping ruling (owner), then evidence-02 does the row-level real import; the
real-backup restore rehearsal awaits a real pilot DB.
