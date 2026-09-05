# D-PEC-01 Pilot Evidence 03 — roster + RAIL/decisions real import — MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence — not authority.** Third D-PEC-01
> capture, executed under the O-A ruling and the owner's 2026-07-05 rulings:
> "Create placeholders" (roster) and "Proceed with this as-is unless you
> recommend changes now (do it!)" (mapping defaults ratified; two recommended
> changes applied). Immutable after publication.

## What this proves

With the placeholder roster in place, the populated real workbooks are now IN
the scratch pilot instance end-to-end: 457 deliverables (evidence-02), 254 of
272 RAIL items as unanchored intake awaiting coordinator triage (§16 I-2
design), and 52 of 62 decisions. Every residual reject is a workbook data gap
with a row-level report, not a tool failure.

## Identity

| Field | Value |
|---|---|
| Evidence package | `PEC_2026-07-05_DPEC01-pilot-evidence-03` |
| Branch | `codex/pec-dpec01-evidence-03` off `main` `d80cccf5d` (PR #77 merge) |
| Governing decisions | D-PEC-01 O-A + owner basis + 2026-07-05 roster/defaults rulings (Receipt 19, verbatim) |
| Actor / DB / server | `ryan@chirality.ai`, scratch `pilot-scratch/db/pec-scratch-import.db`, `127.0.0.1:4899`; ephemeral credential destroyed after capture |

## Roster applied

`projects/pec/execution/_Coordination/IMPORT_TEMPLATES/ROSTER_PLACEHOLDERS.csv`
(SHA-256 `29f1c7fe503f8ac4656e1ec995f7a7a73bd7f5179e80c7abe09c20cb1657fb3f`):
44 placeholder persons — workbook strings verbatim, `@placeholder.invalid`
emails, `password_hash='placeholder:no-login'`, no roles. `None` deliberately
excluded. First application created `"PC` from the quoted `"PC, DC, SCM"`
(naive comma-split — operator error, noted in `IMPORT_MAPPING.md`); fixed
in-place before the fix-batch import.

## Inputs (regenerated per the ratified mapping + applied changes)

| File | Rows | SHA-256 | Change vs evidence-02 |
|---|---:|---|---|
| `pilot-scratch/import-ready/rail.csv` | 272 | `a88bd76c795dcc7375c3e1b25481b72d83e51b14ddffba23013b8319ecce4605` | `raised_date` defaulted to `2026-07-05` when blank (199 rows, tagged in notes); `package` ← workbook AREA |
| `pilot-scratch/import-ready/rail-fix-pcdcscm.csv` | 16 | `55a229310360f34b03033cdd530ba8265bc8c41d5b6901e6bd7b9b3b85432c1a` | the 16 rejected `PC, DC, SCM` rows only — full-file RAIL re-import would duplicate intake (see behaviors below) |
| `pilot-scratch/import-ready/decisions.csv` | 62 | unchanged (`346779ad…`) | — |

## Import results

| Run | Accepted | Rejected | Intake created | Notes |
|---|---:|---:|---:|---|
| RAIL (full) | 0 | 34 | **238** | unanchored by design — no `deliverable_ref` in workbook; AREA carried as anchor suggestion |
| RAIL (fix batch) | 0 | 0 | **16** | after the `PC, DC, SCM` roster fix |
| decisions | **52** | 10 | 0 | |

Residual rejects (row-level detail in committed reports):

- RAIL 18 net: 17× `need_by is required`, 1× `need_by must be YYYY-MM-DD`
  (junk `1900-11-27`); the 16 owner-match rejects were cured by the fix batch.
- decisions 10: 8× authority `None`, 2× blank authority, 2× blank status.

## Observed seam behavior (candidate tool improvement)

RAIL re-import is **not idempotent for unanchored rows**: intake items are not
matched by `item_id`, so re-importing a full RAIL file duplicates previously
intaken rows. This run avoided it by re-importing only rejected rows. Logged
here for the harness/tool backlog conversation; no pec source was changed.

## Captured artifacts (committed, unredacted per owner ruling)

| Artifact | SHA-256 |
|---|---|
| `api/import_rail_report.json` | `687fcd3a4df105aaf1373ccd1d5000859f08f8637aa55cbc98ebab6aef819905` |
| `api/import_rail_fix_report.json` | `9e28faabc4eb7453057223f58f7dc81253d6579d16f0e65e0ac9a1e290199c1b` |
| `api/import_decisions_report.json` | `6fa84599886cd002945ee06bde3ce5ab0f90c4daad3267275a4bae3a69e94e4f` |
| `api/exports/intake.csv` (254 real intake items) | `c1bdf944733ffa2742ed8ca667e7e52abfbc457a9694aa9b0ba5a424137c3434` |
| `api/exports/decisions.csv` (52 real decisions) | `733047ff9b5beefbdf5ef9161d7e889b52a4bc8b5b525bee7f47bd6848de5e56` |
| `api/exports/log.csv` (admin history view) | `2bd97e6dbfe23c5dd217ba52b7ab4a302d097531d44d4285ac6a5029f9eb82cf` |
| `api/overview.json` (PM home over the loaded instance) | `5492b9b8bdbf1f175e8db198bc1534277507f4ca5a01ac7c81dc28dd86a884a6` |
| `backup-post-import.log` (backup `pec-20260705-163034.db`, 976 KiB, exit 0) | `7029abf00f879001c805f00897eeaaad76711107dbcfefdf5c2055dfa5806a79` |

## Limitations

- No `force=true`; scratch DB only; no real production DB exists.
- Placeholder persons are roster scaffolding, not identity claims; they cannot
  log in and carry `@placeholder.invalid` addresses.
- Next §16 step in-app is coordinator triage of the 254 intake items —
  a reserved human workflow (agents do not disposition intake).
- No Gate 2 adoption, L3 act, pilot-readiness/go-live claim, or reserved PEC
  human act.

## Gate Outcome

D-PEC-01's rehearsal scope is now exercised end-to-end on the populated
workbooks. Remaining data gaps are owner/pilot-team side (dates, authorities,
risk log, schedule export). The real-backup restore rehearsal still awaits a
real pilot DB (owner ruled it out of scope this run).
