# PEC L2 evidence capture 02 - backup.restore MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence - not authority.** L2
> `backup.restore` evidence per the D-T0-13 O-A staging ruling, the D-T0-17
> L1-acceptance ruling, and the owner continuation direction recorded in
> Receipt 9. Captured outputs are derivative packages, not substitute
> authority; PEC's source, tests, and governed decisions remain authoritative.
> Immutable after publication - corrections go in a new dated snapshot.

## What this proves

The next backup L2 seam, `backup.restore`, can run through PEC's domain-owned
backup tool against an explicitly scratch database by setting `PEC_DB` and
`PEC_BACKUP_DIR`. The tool restored a previously captured SQLite backup over a
post-backup-mutated scratch database and moved the current database aside as
`*.pre-restore`. Verification confirms:

- source backup and restored database both pass `PRAGMA integrity_check` and
  contain only the `pre-backup` marker row;
- the moved-aside pre-restore database passes `PRAGMA integrity_check` and
  contains both `pre-backup` and `post-backup` marker rows;
- no PEC server was running and no non-scratch database was touched.

This is not evidence for real pilot restore, imports, pilot readiness, real-data
handling, Gate 2 profile adoption, or any L3/proposal-shaped API path.

## Source refs

- Tree: `origin/main` / local continuation branch base @ `c7d754174` after PR
  #61 merge.
- Staging authority:
  - `_DomainEngines/_DECISIONS/D-T0-13_pec_integration_staging.md`: O-A ruled
    L0 now, L2 destination through read-only L1 then per-operation L2.
  - `_DomainEngines/_DECISIONS/D-T0-14_pec_data_residency.md`: CLOSED default;
    scratch/demo evidence is lawful, real instance-content capture is not.
  - `_DomainEngines/_DECISIONS/D-T0-17_pec_l1_acceptance.md`: L1 accepted as
    proven; per-operation L2 unlocked on demo/scratch basis until D-PEC-01.
- Tool exercised: `projects/pec/tools/backup.ts` with command `restore`.
- Profile operation row: `_DomainEngines/profiles/pec.yaml`
  `deterministic_tools[].id == backup.restore`.

## Actor / visibility basis

- Owner direction (2026-07-04, in-session, Ryan Tufts): "I approve merger of
  the PR.  Then continue with the remaining work."
- Actor: PEC work loop agent, using that direction as the human confirmation
  for a scratch-only `backup.restore` operation.
- Visibility/residency basis: D-T0-14 CLOSED default - committed repository
  code plus a scratch SQLite database under the OS temp directory.
- No PEC server was started. No non-scratch database was opened. No real PEC
  instance content was read, captured, or egressed.

## Commands and captures

All commands were run from the repository root unless otherwise noted.

| Step | Command / action | Exit | Output capture | Result |
|---|---|---:|---|---|
| Scratch setup | Node `node:sqlite` script creates a scratch DB with one `pre-backup` marker row and WAL mode | 0 | `scratch-db-setup.log` | scratch DB created under OS temp |
| Backup source | `cd projects/pec && PEC_DB=$scratch_db PEC_BACKUP_DIR=$scratch_backups node --disable-warning=ExperimentalWarning tools/backup.ts backup` | 0 | `backup-create.log` | source backup written as `pec-20260704-214358.db` |
| Post-backup mutation | Node `node:sqlite` script inserts one `post-backup` marker row | 0 | `mutate-after-backup.log` | live scratch DB now contains both markers |
| L2 operation | `cd projects/pec && PEC_DB=$scratch_db PEC_BACKUP_DIR=$scratch_backups node --disable-warning=ExperimentalWarning tools/backup.ts restore pec-20260704-214358.db` | 0 | `backup-restore.log` | restored source backup over scratch DB; current DB moved aside |
| Artifact copy | copy source backup, restored DB, and pre-restore DB into this snapshot | 0 | `artifacts/` | self-contained scratch evidence artifacts |
| Verification | Node `node:sqlite` `PRAGMA integrity_check` and marker query over source, restored, and pre-restore DBs | 0 | `integrity-check.log` | all `ok`; restored DB lacks post-backup marker; pre-restore DB preserves it |

Captured artifact SHA-256:

```
dcd8135f387b4e1ecd6b7b1a6a4c21c5b60656760af33bca6d45340cbec366c6  scratch-db-setup.log
9e0ad8d687089c7e61a4fb4b3d8d3eb37f81945a4cc1ceab0bf8ffb22c51a43d  backup-create.log
b04602f7f89bc9566f0ea57af67ac8f15468224d243e9170a685417fefd82726  mutate-after-backup.log
4e72af80d6bb45d289814ed58b9add8c6c1594de4c489b52f2042efbb502ca00  backup-restore.log
1df171944ad0a6413e157f0abfc1e9acc5fbb902fe6638fb467be9d3715dae1b  integrity-check.log
dc621a1391a9b8ec52719347f6fd39dbdfc17d45c3c002e481764426b2d4318b  run-paths.log
2e69eaba55d5290051465827d8bbf4c7e7ac131921895d04d2797cc9b37c67de  artifacts/pre-restore-db.db
c0fda65d6897d918d1dd27ce83503bd1a6d399aaf348cb29fc0a73b5c23d278b  artifacts/restored-db.db
c0fda65d6897d918d1dd27ce83503bd1a6d399aaf348cb29fc0a73b5c23d278b  artifacts/source-backup-pec-20260704-214358.db
```

## Warnings and limitations

- The log files are run-record evidence and carry machine-absolute temp paths
  (permitted for evidence artifacts by SPEC path-anchoring rules); they are
  machine-specific and non-portable.
- The scratch DB is intentionally minimal. This capture validates the
  `backup.restore` operation seam, not the semantic completeness of PEC project
  data in a backup or restore.
- D-T0-14 remains CLOSED. D-PEC-01 is still required before any real MDL, RAIL,
  pilot, or other PEC instance data basis is exposed to agents.
- Profile status remains DRAFT and Gate 2 remains owner-only/open.
