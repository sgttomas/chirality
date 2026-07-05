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

## Owner-Supplied Basis

| Required input | Owner value |
|---|---|
| MDL spreadsheet/export path | TBD - owner supplied |
| RAIL spreadsheet/export path | TBD - owner supplied |
| Decisions spreadsheet/export path, if in scope | TBD - owner supplied |
| Risks spreadsheet/export path, if in scope | TBD - owner supplied |
| Schedule spreadsheet/export path, if in scope | TBD - owner supplied |
| Actor identity for any authenticated API capture | TBD - owner supplied |
| Visibility basis for that actor | TBD - owner supplied |
| Scratch `PEC_DB` path for import rehearsal | TBD - owner supplied |
| Scratch backup directory | TBD - owner supplied |
| Real backup artifact path for restore rehearsal, if in scope | TBD - owner supplied |
| Scratch restore target `PEC_DB` path | TBD - owner supplied |
| Whether agents may view raw file contents | TBD - owner supplied |
| Whether unredacted exports/reports may be committed | TBD - owner supplied |
| Capture limits beyond hashes/counts/timings/reject summaries | TBD - owner supplied |

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
