# D-PEC-01 Pilot Evidence 04 — schedule + gap fills — full dataset loaded — MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence — not authority.** Fourth D-PEC-01
> capture, under the owner's 2026-07-05 rulings: PR #78 merge; "This is all
> test data so you can make up whatever dates you want to fill in what you
> need at this point."; D-PEC-07 O-C; "I've put `schedule.csv` in place of
> the PDF schedule file." Immutable after publication.

## What this proves

The complete populated dataset is now in the scratch pilot instance with
**zero outstanding rejects**: 457 deliverables, 272/272 RAIL items (unanchored
intake awaiting triage), 62/62 decisions, 127/127 schedule activities. The
D-PEC-07 zero-code file-drop pathway was exercised end-to-end on the owner's
dropped `schedule.csv` the same day it was ruled.

## Identity

| Field | Value |
|---|---|
| Evidence package | `PEC_2026-07-05_DPEC01-pilot-evidence-04` |
| Branch | `codex/pec-dpec01-evidence-04` off `main` (PR #78 merge) |
| Governing decisions | D-PEC-01 O-A basis; D-PEC-07 O-C; 2026-07-05 test-data-fill ruling (Receipt 20, verbatim) |
| Actor / DB / server | `ryan@chirality.ai`, scratch `pilot-scratch/db/pec-scratch-import.db`, `127.0.0.1:4899`; ephemeral credential destroyed after capture |

## Inputs

| File | Rows | SHA-256 | Note |
|---|---:|---|---|
| `pilot-scratch/input/schedule.csv` (owner-dropped) | 127 | `42e68a3c5cd792534bf8184a57dad96c16b0950abb051d377ee7e507fb7757ea` | PDF-extractor shape (MS Project); replaces `schedule.pdf` |
| `pilot-scratch/import-ready/schedule.csv` (mapped) | 127 | `b92456faa32cdd2eed67a558032136fdf27a0fd546db72bf7f9342c51ed0b9a4` | `activity_id←SCH-{id}`, `description←task_name` (+`[Summary]`/`[Milestone]` tags), ISO start/finish passthrough |
| `pilot-scratch/import-ready/rail-fix-dates.csv` | 18 | `43c8bab313c5640e8c7faa4cbef714aea019ae177e3a7320055a1c146b6fae2e` | the 18 date-gap rows; `need_by=2026-12-31` test placeholder, tagged in notes |
| `pilot-scratch/import-ready/decisions.csv` (refilled) | 62 | `16b9c34441d831eb1551cce94f960a0dde92b399116d10748bf09de18aa74987` | 10× authority→`Project`, 2× status→`identified`, tagged in rationale |

## Import results

| Run | Accepted | Updated | Rejected | Intake | Note |
|---|---:|---:|---:|---:|---|
| schedule (full) | **127** | 0 | 0 | 0 | first schedule import |
| RAIL date-fix batch | 0 | 0 | 0 | **18** | RAIL now 272/272 in instance |
| decisions (full re-import) | **10** | **52** | 0 | 0 | idempotent update-in-place again proven |

## Captured artifacts (committed, unredacted per owner ruling)

| Artifact | SHA-256 |
|---|---|
| `api/import_schedule_report.json` | `35a8a99c35914ffd1fbbde54711e5e7e245c427168043e9bc5f0412df32c8441` |
| `api/import_rail_datefix_report.json` | `163c07b0949526106ad4985d7e199bd0ae1336540f235692a49262a472723c30` |
| `api/import_decisions_refill_report.json` | `5a76420478b7eda8b30e9e943dcbc4bba9fa105782d3b08c7618065a19618ec2` |
| `api/exports/schedule.csv` (127 real activities) | `7cf17831a7c5456d4a9863e58ac63fedb57701b894ffeef4710e1d360dc4b6f8` |
| `api/exports/decisions.csv` (62) | `5300d01fe43bcb4ad8f777caab01980780567648589f1950896ad88b329b1bdf` |
| `api/exports/intake.csv` (272) | `b4237fbc3e608379d15d82af3eb9e4ddd5cdde7397aa282635b0f95ea96a56e5` |
| `api/exports/lookahead.csv` (plan cells + imported schedule) | `e096478aa07c9debff7ab3539c34572195d42bea41406deca2b039277ebce0ff` |
| `api/overview.json` | `52607f66fce2e17d471f28d1752ca2c107ed511f5935f249bacb424237460f03` |
| `backup-post-import.log` (backup `pec-20260705-170113.db`, 1.0 MiB, exit 0) | `190134d896d7cd7112c1b41622ed2690d90f43afe62d7bab1d8b30360b01937f` |

## Limitations

- Test-data fills are placeholders, tagged in-row (`need_by 2026-12-31`,
  authority `Project`, status `identified`) — replace via idempotent
  re-import when real values exist.
- Schedule Summary/Milestone rows were imported with tags rather than
  filtered — a lookahead-noise call the pilot team may want to revisit.
- No `force=true`; scratch DB only; no Gate 2/L3 implementation act; intake
  triage (272 items) remains the coordinator's reserved workflow.

## Gate Outcome

D-PEC-01's rehearsal is complete on the full populated dataset; the D-PEC-07
O-C pathway is formalized (`FILE_DROP_RUNBOOK.md`) and proven live. The L3
design brief is CANDIDATE at its adoption gate. Real-backup restore rehearsal
still awaits a real pilot DB.
