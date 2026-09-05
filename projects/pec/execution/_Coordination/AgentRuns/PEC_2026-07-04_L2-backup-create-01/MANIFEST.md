# PEC L2 evidence capture 01 - backup.create MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence - not authority.** L2
> `backup.create` evidence per the D-T0-13 O-A staging ruling and the D-T0-17
> L1-acceptance ruling. Captured outputs are derivative packages, not
> substitute authority; PEC's source, tests, and governed decisions remain
> authoritative. Immutable after publication - corrections go in a new dated
> snapshot.

## What this proves

The first per-operation L2 seam, `backup.create`, can run through PEC's
domain-owned backup tool against an explicitly scratch database by setting
`PEC_DB` and `PEC_BACKUP_DIR`. The tool produced a WAL-safe SQLite backup via
`VACUUM INTO`; the copied snapshot artifact passes `PRAGMA integrity_check` and
contains the scratch evidence marker.

This is not evidence for `backup.restore`, imports, pilot readiness, real-data
handling, Gate 2 profile adoption, or any L3/proposal-shaped API path.

## Source refs

- Tree: `origin/main` / local branch base @ `a20ce9c6c`.
- Staging authority:
  - `_DomainEngines/_DECISIONS/D-T0-13_pec_integration_staging.md`: O-A ruled
    L0 now, L2 destination through read-only L1 then per-operation L2;
    `backup.create` first.
  - `_DomainEngines/_DECISIONS/D-T0-14_pec_data_residency.md`: CLOSED default;
    scratch/demo evidence is lawful, real instance-content capture is not.
  - `_DomainEngines/_DECISIONS/D-T0-17_pec_l1_acceptance.md`: L1 accepted as
    proven; per-operation L2 unlocked on demo/scratch basis until D-PEC-01.
- Tool exercised: `projects/pec/tools/backup.ts` with command `backup`.
- Profile operation row: `_DomainEngines/profiles/pec.yaml`
  `deterministic_tools[].id == backup.create`.

## Actor / visibility basis

- Actor: PEC work loop agent under the standing loop direction for this run:
  pursue inherent goals as far as live authority permits.
- Visibility/residency basis: D-T0-14 CLOSED default - committed repository
  code plus a scratch SQLite database under the OS temp directory.
- No PEC server was started. No non-scratch database was opened. No real PEC
  instance content was read, captured, or egressed.

## Commands and captures

All commands were run from the repository root unless otherwise noted.

| Step | Command / action | Exit | Output capture | Result |
|---|---|---:|---|---|
| Scratch setup | Node `node:sqlite` script creates a scratch DB with one `evidence_marker` row and WAL mode | 0 | `scratch-db-setup.log` | scratch DB created under OS temp; one marker row |
| L2 operation | `cd projects/pec && PEC_DB=$scratch_db PEC_BACKUP_DIR=$scratch_backups node --disable-warning=ExperimentalWarning tools/backup.ts backup` | 0 | `backup-create.log` | backup written as `pec-20260704-213204.db` |
| Artifact copy | copy generated backup DB into this snapshot | 0 | `artifacts/pec-20260704-213204.db` | self-contained scratch backup artifact |
| Verification | Node `node:sqlite` `PRAGMA integrity_check` over source backup and snapshot artifact | 0 | `integrity-check.log` | both report `ok`; marker row preserved |

Captured artifact SHA-256:

```
3381e774408724391eab9a96270d636fd2d2ee04960b1ebd63cb0643f303248d  scratch-db-setup.log
b0a8757184f7e679d0f9aad8d36a9ce08424f6d533eb04db55beaa73ea4f71b7  backup-create.log
c09a74bc9c039290813d055608b383a418f3b2433c5c6067091dece477e3719a  integrity-check.log
8f538eac51c1376e2e96efe65f593eca2b96b69af7ec89434ae9a0122e2e8fb3  artifacts/pec-20260704-213204.db
```

## Warnings and limitations

- The log files are run-record evidence and carry machine-absolute temp paths
  (permitted for evidence artifacts by SPEC path-anchoring rules); they are
  machine-specific and non-portable.
- The scratch DB is intentionally minimal. This capture validates the
  `backup.create` operation seam, not the semantic completeness of PEC project
  data in a backup.
- D-T0-14 remains CLOSED. D-PEC-01 is still required before any real MDL, RAIL,
  pilot, or other PEC instance data basis is exposed to agents.
- Profile status remains DRAFT and Gate 2 remains owner-only/open.
