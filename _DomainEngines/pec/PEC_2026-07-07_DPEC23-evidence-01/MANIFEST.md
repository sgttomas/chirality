# PEC_2026-07-07_DPEC23-evidence-01 — TOU West Doe import capture

> **Immutable evidence pack (D-PEC-23).** Count-level results + content
> hashes only; **no verbatim real project rows are committed** (owner's
> 2026-07-05 capture basis, D-PEC-01/RV-11). This is the same workbook family
> as the 26020 pilot (real project content). Governance: the ruled-by-
> direction packet `../../projects/pec/execution/_Coordination/_DECISIONS/D-PEC-23_tou_west_doe_demo_project.md`
> and the tranche `../../projects/pec/execution/_Coordination/TRANCHE_2026-07-07_D-PEC-23_tou_west_doe_demo.md`.

## What ran

- **Owner approval of record (2026-07-08, verbatim):** "Merge PR #106 and I
  approve the import." — discharges FILE_DROP_RUNBOOK v1.1 RV-7 and the
  profile's `import.csv requires_human_confirmation` on the presented step-3
  proposal (Receipt 54).
- **Basis:** the committed demo database (`projects/pec/pec-demo.db`, the
  `demo`-token scratch/demo mutation basis; F-PEC-1 permits it). A
  `VACUUM INTO` backup was taken before any write. The schema-fit code was
  present (PR #106 merged, `fb9a10be5`).
- **Mechanism:** the run-local loader `projects/pec/pilot-scratch/import-ready/
  tou-west-doe/load.ts` (gitignored) created the project, mirrored the AUR
  cast's role grants onto it, inserted 44 roster placeholders
  (`@placeholder.invalid`, no login), then ran the six §16 imports through the
  real `importContract` in dependency order (mdl → rail → decisions →
  schedule → tracker; risks skipped — the workbook is an unpopulated 100-row
  scaffold).

## Result — new project

| Field | Value |
|---|---|
| project id | 2 |
| code | `TWD` (⚑ default ratified by the owner approval) |
| name | TOU West Doe |
| timezone | America/Edmonton (⚑ default ratified) |
| roster placeholders created | 44 |

## Result — per-contract ImportReport (count level only)

| Contract | accepted | updated | intakeCreated | conflicts | rejected |
|---|---|---|---|---|---|
| mdl | 457 | 0 | 0 | 0 | 0 |
| rail | 0 | 0 | 254 | 0 | 18 |
| decisions | 52 | 0 | 0 | 0 | 10 |
| schedule | 127 | 0 | 0 | 0 | 0 |
| tracker | 54 | 0 | 0 | 0 | 11 |
| risks | — | — | — | — | — (skipped: unpopulated scaffold) |

Rejects are genuine source-data gaps, not import faults: 18 RAIL rows
(17 blank need-by + 1 literal "Ongoing"), 10 decisions (8 authority `None`
+ 2 blank rows), 11 tracker rows (package names resolving to no MDL package).
Full per-row reports (`report-*.json`) stay uncommitted beside the loader —
they carry real keys, excluded per the capture basis.

## Result — schema-fit columns populated (D-PEC-23 payload)

Read back from `pec-demo.db` (project_id = 2), confirming the new columns
carry data rather than sitting inert:

| Register | rows | schema-fit columns populated |
|---|---|---|
| packages | 142 | area 141/142, package_type 142/142 |
| intake (RAIL) | 254 | area 54/254 (only rows with a populated source AREA) |
| decisions | 52 | open_date 52/52, source 52/52 |
| schedule | 127 | row_type 127/127, percent_complete 127/127 |
| tracker | 54 | package_type_approved 54/54 |

## Content hashes (SHA-256)

Input workbooks (`projects/pec/pilot-scratch/input/`):

```
bf73c03f5f753652c7d0e62086dedbbcc6f6642de29b32976e814efc7860db74  mdl.xlsx
545655199557527fc2d41b938bfec173ec70bd3e00f6caff817d69db37c33e84  rail.xlsx
a5207b320fa2dcd81d9b31e28cff0d4623bbd2981b9cb8e06a825f8f165078c8  decisions.csv
b6b1ea0ef6b4a4ed44132e13ae1727032dcddae02d2b174115b5272914d92125  risk.xlsx
42e68a3c5cd792534bf8184a57dad96c16b0950abb051d377ee7e507fb7757ea  schedule.csv
01fc38f085dc8218c0e006d8a27c8ad7fa157c964ffe4041a7599ebc54f6bf9e  tracker.xlsx
```

Mapped import-ready CSVs (`…/import-ready/tou-west-doe/`, gitignored):

```
f068bf8a46d332a698e26d84730cd52a7fdfb2d79188c43afe22d677eae1fd2c  mdl.csv
0842a16a92010fb36ce7c62f3311f1624880e16460bc79533b898f080ae9ebaa  rail.csv
5f3a69057610b468f317528ffcadc5ed689c151bb42d84f55c5c3bd68b6207fa  decisions.csv
0b7db814a216724891c7ac74ec7e5faa2cb6b427ee184003302fd3dc4ef2b0b4  schedule.csv
9b5a9c3def2b8831a90ecac79be863b882a231fe27a10753643c273211d1f614  tracker.csv
f334bc14e3a417c71bb2a39bbc9de5cc891e104f9516d933af06290f488bcb52  roster.csv
```

## Rollback

The pre-import `VACUUM INTO` backup restores `pec-demo.db` to its pre-load
state; the DB file is otherwise the owner's to keep or reset. Deleting
project id 2 is not an app path (controlled records have no hard-delete) —
rollback is by backup restore.
