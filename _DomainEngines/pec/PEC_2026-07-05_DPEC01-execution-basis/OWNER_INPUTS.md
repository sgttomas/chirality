# D-PEC-01 Execution Basis - Owner Inputs Needed

> **Epistemic status:** derivative execution-basis request, not authority.
> Authority remains `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-01_pilot_rehearsal_real_data_authorization.md`
> and the owner's supplied execution basis. Do not start the evidence run from
> this file alone.

## Gate

D-PEC-01 O-A authorizes the narrow pilot-only real-data rehearsal, with two
riders:

- SHA-256 hashes of real input files are permitted in manifests.
- The exact spreadsheet/export paths, actor/visibility basis, scratch
  DB/backup locations, and capture limits must be supplied by the owner before
  the evidence run begins.

`force=true` remains off and requires a separate ruling. D-PEC-05 keeps L3
deferred until after D-PEC-01 pilot evidence is captured.

## Owner-Supplied Basis (supplied 2026-07-05, in-session, Ryan Tufts)

| Required input | Owner value |
|---|---|
| MDL spreadsheet/export path | `projects/pec/pilot-scratch/input/mdl.xlsx` |
| RAIL spreadsheet/export path | `projects/pec/pilot-scratch/input/rail.xlsx` |
| Decisions spreadsheet/export path, if in scope | `projects/pec/pilot-scratch/input/decisions.xlsx` |
| Risks spreadsheet/export path, if in scope | `projects/pec/pilot-scratch/input/risks.xlsx` (live tree: file is `risk.xlsx` — delta recorded below) |
| Schedule spreadsheet/export path, if in scope | `projects/pec/pilot-scratch/input/schedule.pdf` |
| Actor identity for any authenticated API capture | `ryan@chirality.ai` |
| Visibility basis for that actor | full (all three logs) |
| Scratch `PEC_DB` path for import rehearsal | `projects/pec/pilot-scratch/db/pec-scratch-import.db` |
| Scratch backup directory | `projects/pec/pilot-scratch/backups/` |
| Real backup artifact path for restore rehearsal, if in scope | OUT OF SCOPE this run — no real pilot DB exists yet; the real restore rehearsal (PILOT.md §5) becomes its own later evidence run |
| Scratch restore target `PEC_DB` path | `projects/pec/pilot-scratch/db/pec-scratch-restore.db` |
| Whether agents may view raw file contents | YES — owner ruling 2026-07-05: "I'm okay with the agents reading the raw files … I'm controlling the data appropriately." |
| Whether unredacted exports/reports may be committed | YES — run-generated exports and reports may be committed unredacted (same ruling). The raw input spreadsheets and DB files themselves remain uncommitted (and are gitignored under `pilot-scratch/`). Committable artifacts must be written OUTSIDE `pilot-scratch/` (evidence-snapshot dir), since that tree is ignored wholesale. |
| Capture limits beyond hashes/counts/timings/reject summaries | none — full content capture permitted per the above; hashes still anchor the evidence chain (rider 1) |

### Deltas found at execution (live tree wins; recorded per loop rule)

- Owner basis names `risks.xlsx`; the live file is
  `projects/pec/pilot-scratch/input/risk.xlsx`. Content identity is anchored by
  the SHA-256 in the evidence manifest; the run uses the live file.
- `tools/pilot-drill.ts` always creates its own scratch DB under the OS temp
  directory (drill design; the profile's `pec.drill` note says the same). The
  owner-supplied scratch import `PEC_DB` is therefore exercised by the
  API-mode import rehearsal (server + `POST /api/import/:contract`), which is
  also where the actor/visibility basis applies.
- The import layer is CSV-only (`server/src/import/csv.ts`); the `.xlsx`
  inputs are converted verbatim (first sheet, no header mapping) to scratch
  CSVs before import; original and derived hashes are both recorded.
  `schedule.pdf` is hashed but not importable verbatim: the schedule contract
  is CSV/XER-derived (D-04) and a PDF has no verbatim CSV form — recorded as a
  limitation, owner to supply a spreadsheet export if schedule import is
  wanted in a later run.

## Evidence Run Shape Once Basis Exists

The next branch-first evidence run should create a new immutable snapshot under
`_DomainEngines/pec/` with a manifest that records:

- git SHA and governing decision/ruling pointers;
- owner-supplied paths and SHA-256 hashes of real input files;
- actor and visibility basis;
- commands, environment variables, scratch database path, and backup directory;
- accepted/updated/conflict/rejected counts and row-level reject summaries;
- restore rehearsal source/target paths and backup hashes;
- explicit limitations: no `force=true`, no Gate 2 adoption, no L3 apply path,
  no pilot-readiness or go-live claim.

`RUNBOOK.md` and `MANIFEST_TEMPLATE.md` in this directory provide the execution
shape and manifest fields for that future evidence run. They are templates only
and do not authorize the run before the owner-supplied basis exists.

## Parked Until Supplied

Absent the owner values above, the lawful next step is only accounting and
preparation. The D-PEC-01 evidence run must not begin.
